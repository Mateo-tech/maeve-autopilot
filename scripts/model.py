import tensorflow as tf

model = tf.keras.models.Sequential([
    tf.keras.layers.Lambda(lambda x: x / 127.5 - 1,
                           input_shape=(128, 128, 1)),
    tf.keras.layers.Conv2D(32, (3, 3), padding='same'),
    tf.keras.layers.Activation('relu'),
    tf.keras.layers.MaxPooling2D((2, 2), padding='valid'),
    tf.keras.layers.Conv2D(32, (3, 3), padding='same'),
    tf.keras.layers.Activation('relu'),
    tf.keras.layers.MaxPooling2D((2, 2), padding='valid'),

    tf.keras.layers.Conv2D(64, (3, 3), padding='same'),
    tf.keras.layers.Activation('relu'),
    tf.keras.layers.MaxPooling2D((2, 2), padding='valid'),
    tf.keras.layers.Conv2D(64, (3, 3), padding='same'),
    tf.keras.layers.Activation('relu'),
    tf.keras.layers.MaxPooling2D((2, 2), padding='valid'),

    tf.keras.layers.Conv2D(128, (3, 3), padding='same'),
    tf.keras.layers.Activation('relu'),
    tf.keras.layers.MaxPooling2D((2, 2), padding='valid'),
    tf.keras.layers.Conv2D(128, (3, 3), padding='same'),
    tf.keras.layers.Activation('relu'),
    tf.keras.layers.MaxPooling2D((2, 2), padding='valid'),

    tf.keras.layers.Flatten(),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(1024),
    tf.keras.layers.Dense(256),
    tf.keras.layers.Dense(64),
    tf.keras.layers.Dense(1),
])

model.compile(optimizer='adam', loss="mse", metrics=["accuracy"])

