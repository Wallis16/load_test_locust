import pandas as pd

from sklearn.metrics import accuracy_score
from app.models.model_loader import load_model
from pathlib import Path
def main():
    model = load_model()

    BASE_DIR = Path(__file__).resolve().parent
    df_test = pd.read_csv(BASE_DIR / "test_set.csv")

    X_test = df_test.drop(columns=["target"])
    y_test = df_test["target"].astype(int)

    # predict
    preds = model.predict(X_test)

    # evaluate
    acc = accuracy_score(y_test, preds)

    print(f"Accuracy: {acc}")

    # sanity threshold
    assert acc > 0.7, f"Model accuracy too low: {acc}"

    print("Sanity check passed ✅")


if __name__ == "__main__":
    main()