# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-01-23

### Added
- Initial release of Sign Language Gesture Control system
- Real-time hand gesture recognition using MediaPipe
- Game control integration with Subway Surfers
- Performance monitoring with FPS display
- Configurable settings for gesture recognition
- Documentation and setup instructions
- Cleanup script for maintenance

### Features
- Support for 5 basic gestures:
  - A: Move Left
  - D: Move Right
  - E: Jump
  - K: Roll/Slide
  - P: Pause
- Action debouncing system
- Consecutive prediction validation
- Confidence threshold filtering

### Technical
- Implemented HandDetector class for gesture processing
- Created GestureModel class for sign recognition
- Added GameController for keyboard simulation
- Integrated MediaPipe for hand tracking
- Added configuration system
- Implemented performance optimization features

### Documentation
- Added comprehensive README
- Created technical documentation
- Included contribution guidelines
- Started changelog tracking
