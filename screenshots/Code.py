import tensorflow as tf
import numpy as np

class TextGenerator:
    def __init__(self, vocab_size, embedding_dim=128, lstm_units=128):
        self.vocab_size = vocab_size

        self.model = tf.keras.Sequential([
            tf.keras.layers.Embedding(vocab_size, embedding_dim),
            tf.keras.layers.LSTM(lstm_units, return_sequences=True),
            tf.keras.layers.LSTM(lstm_units),
            tf.keras.layers.Dense(vocab_size, activation='softmax')
        ])

        self.char2idx = {}
        self.idx2char = {}

    def preprocess_text(self, text, sequence_length=40):
        chars = sorted(list(set(text)))
        self.char2idx = {c: i for i, c in enumerate(chars)}
        self.idx2char = {i: c for c, i in self.char2idx.items()}

        encoded = np.array([self.char2idx[c] for c in text])

        X, y = [], []
        for i in range(len(encoded) - sequence_length):
            X.append(encoded[i:i + sequence_length])
            y.append(encoded[i + sequence_length])

        return np.array(X), np.array(y)

    def compile_and_train(self, X_train, y_train, epochs=20):
        self.model.compile(
            loss='sparse_categorical_crossentropy',
            optimizer='adam',
            metrics=['accuracy']
        )

        self.model.fit(
            X_train,
            y_train,
            epochs=epochs,
            batch_size=64
        )

    def generate_text(self, seed_text, num_chars=100, temperature=1.0):
        generated = seed_text

        for _ in range(num_chars):
            input_seq = [self.char2idx[c] for c in generated[-40:]]
            input_seq = tf.expand_dims(input_seq, 0)

            predictions = self.model(input_seq)[0]
            predictions = np.log(predictions + 1e-8) / temperature
            probs = tf.nn.softmax(predictions).numpy()

            next_idx = np.random.choice(len(probs), p=probs)
            next_char = self.idx2char[next_idx]

            generated += next_char

        return generated


# ===== Пример использования =====
if __name__ == "__main__":
    text = (
        "нейронные сети это круто "
        "rnn умеют работать с последовательностями "
        "lstm запоминают контекст "
    )

    gen = TextGenerator(vocab_size=len(set(text)))
    X, y = gen.preprocess_text(text)

    gen.compile_and_train(X, y, epochs=50)

    print("\nСгенерированный текст:")
    print(gen.generate_text("нейронные сети ", temperature=0.5))
