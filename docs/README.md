# Sign Language Gesture Control for Subway Surfers

## Overview
This project implements a real-time sign language gesture recognition system to control the Subway Surfers game. Using computer vision and machine learning, it translates hand gestures into game controls, making the game accessible through sign language.

## Features
- Real-time hand gesture recognition
- Low-latency game control
- Support for essential game actions:
  - Move Left (A gesture)
  - Move Right (D gesture)
  - Jump (E gesture)
  - Roll/Slide (K gesture)
  - Pause (P gesture)
- Performance monitoring with FPS display
- Configurable settings for gesture recognition sensitivity

## System Architecture

### Components
1. **Hand Detection Module**
   - Uses MediaPipe for real-time hand landmark detection
   - Processes video input from webcam
   - Extracts hand region for gesture recognition

2. **Gesture Recognition Model**
   - Deep learning model trained on sign language gestures
   - Converts hand landmarks into game control signals
   - Real-time prediction with confidence scores

3. **Game Controller**
   - Maps recognized gestures to keyboard inputs
   - Implements action debouncing to prevent input spam
   - Handles keyboard event simulation

### Directory Structure
```
SignLanguageRecogniser_Realtime/
├── docs/                    # Documentation files
├── src/                     # Source code
│   ├── config/             # Configuration files
│   ├── models/             # ML models and model-related code
│   └── utils/              # Utility functions and classes
├── tests/                   # Test files
├── notebooks/              # Jupyter notebooks for model training
└── requirements.txt        # Project dependencies
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/SignLanguageRecogniser_Realtime.git
cd SignLanguageRecogniser_Realtime
```

2. Create and activate a virtual environment:
```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the application:
```bash
cd src
python main.py
```

2. Position your hand in front of the camera
3. Use the following gestures to control the game:
   - A: Move Left
   - D: Move Right
   - E: Jump
   - K: Roll/Slide
   - P: Pause

4. Press 'q' to quit the application

## Configuration

The system can be configured through `src/config/settings.py`:

- Camera settings (ID, frame flip)
- Model parameters
- Hand detection settings
- Display options
- Game controller sensitivity

## Maintenance

To clean up temporary files and caches:
```bash
./cleanup.sh
```

## Performance Optimization

The system includes several optimizations:
1. Action debouncing to prevent input spam
2. Confidence threshold for gesture recognition
3. Consecutive prediction requirement for stability
4. Frame rate monitoring

## Troubleshooting

Common issues and solutions:
1. **Camera not detected**: Verify camera ID in settings.py
2. **Gesture not recognized**: Adjust confidence threshold
3. **Input lag**: Check FPS and adjust action cooldown
4. **False positives**: Increase required consecutive predictions
