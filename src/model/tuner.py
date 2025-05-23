import keras_tuner as kt
from src.model.builder import build_model

def model_builder(hp):
    hp_units = hp.Int('units', min_value=32, max_value=128, step=16)
    hp_learning_rate = hp.Choice('learning_rate', values=[1e-2, 1e-3, 1e-4])

    model = build_model(input_shape=8, learning_rate=hp_learning_rate)  # adjust based on your data
    return model

def tune_hyperparameters(X, y):
    tuner = kt.Hyperband(
        model_builder,
        objective='val_accuracy',
        max_epochs=20,
        factor=3,
        directory='tuner_results',
        project_name='diabetes_tuning'
    )

    tuner.search(X, y, epochs=50, validation_split=0.2, verbose=1)

    best_hps = tuner.get_best_hyperparameters(num_trials=1)[0]
    print(f"✅ Best hyperparameters: Units={best_hps.get('units')}, Learning rate={best_hps.get('learning_rate')}")

    return best_hps
