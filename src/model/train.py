from src.model.builder import build_model
from tensorflow.keras.callbacks import EarlyStopping
import joblib

def train_model(X_train, y_train, X_val, y_val, save_path="models/diabetes_model.h5"):
    model = build_model(input_shape=X_train.shape[1])

    callbacks = [
        EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True)
    ]

    history = model.fit(
        X_train, y_train,
        validation_data=(X_val, y_val),
        epochs=100,
        batch_size=32,
        callbacks=callbacks,
        verbose=1
    )

    model.save(save_path)
    print(f"✅ Model saved to {save_path}")

    return model, history
