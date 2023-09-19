from tensorflow.keras import models, layers


class ToxicCommentsClassifier:
    def __init__(self, input_dim, embedding_dim, max_length, weights_path=None):
        self.model = self._build_model(input_dim, embedding_dim, max_length)

        if weights_path:
            self.load_weights(weights_path)

    @staticmethod
    def _build_model(input_dim, embedding_dim, max_length):
        model = models.Sequential([
            layers.Embedding(input_dim=input_dim + 1, output_dim=embedding_dim, input_length=max_length),
            layers.Bidirectional(layers.LSTM(64, return_sequences=True)),
            layers.GlobalMaxPooling1D(),
            layers.Dense(128, activation='relu'),
            layers.Dense(256, activation='relu'),
            layers.Dropout(0.5),
            layers.Dense(128, activation='relu'),
            layers.Dense(6, activation='sigmoid')
        ])
        model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
        return model

    def load_weights(self, weights_path):
        self.model.load_weights(weights_path)

    def predict(self, data):
        return self.model.predict(data)

    def summary(self):
        return self.model.summary()
