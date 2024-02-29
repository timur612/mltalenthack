import os
import sys

from SECRET import API_KEY
from src.model import predict

if __name__ == "__main__":
    cv_path = os.path.join(os.path.dirname(sys.argv[0]), 'ANDREW MIRONOV.pdf')

    prediction = predict(cv_path, API_KEY)
    with open("ANDREW_MIRONOV.json", "w") as file:
        file.write(prediction)
