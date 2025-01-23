# Sign Language Recognizer for Subway Surfers

A real-time hand gesture recognition system that controls Subway Surfers game using sign language.

## Project Structure
```
├── src/
│   ├── gesture_control/         # Main package
│   │   ├── config/             # Configuration settings
│   │   ├── data/               # Training data
│   │   ├── models/             # Model related code
│   │   │   └── saved_models/   # Trained model files
│   │   └── utils/              # Utility functions
│   └── main.py                 # Application entry point
├── notebooks/                  # Jupyter notebooks for training
└── requirements.txt            # Project dependencies
```

## Setup

1. Create a virtual environment:
```bash
python -m venv env
source env/bin/activate  # On Linux/Mac
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Activate your virtual environment if not already active
2. Run the application:
```bash
cd src
python main.py
```

3. Use the following gestures to control Subway Surfers:
- A: Left
- D: Right
- E: Jump
- K: Roll
- P: Pause

Press 'q' to quit the application.

## Requirements
- Python 3.8+
- Webcam
- Dependencies listed in requirements.txt
