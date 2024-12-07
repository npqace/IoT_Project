# Hand Gesture Recognition Project

This project is designed to recognize hand gestures using machine learning and computer vision techniques. The project is divided into three main steps: data generation, model training, and gesture-based control.

## Project Structure
```
├── step0/
|   ├── data2/
|   ├── sign_imgs2/
|   ├── generate_landmark_data.py
|   ├── hand_gesture.yaml
|   └── requirements.txt
├── step1/
|   ├── data/
|   ├── models/
|   ├── hand_gesture_recognition.ipynb
|   └── hand_gesture.yaml
├── step2/
|   ├── models/
|   ├── controller.py
|   ├── detect_simulation.py
|   ├── hand_gesture.yaml
|   └── mock_controller.py
├── .gitignore
└── README.md
```

## Step 0: Data Generation

In this step, we generate the dataset required for training the hand gesture recognition model.

### Files

- `generate_landmark_data.py`: Script to capture hand landmarks and save them as CSV files.
- `hand_gesture.yaml`: Configuration file containing gesture labels.
- `requirements.txt`: List of dependencies required for this step.

### Usage

1. Navigate to `step0/` folder
    ```sh
    cd step0
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

3. Run the data generation script:
    ```sh
    python generate_landmark_data.py
    ```

## Step 1: Model Training

In this step, we train a neural network model to recognize hand gestures using the generated dataset.

### Files

- `hand_gesture_recgonition.ipynb`: Jupyter notebook for training the hand gesture recognition model.
- `hand_gesture.yaml`: Configuration file containing gesture labels.

### Usage
1. Open the Jupyter notebook and run the cells to train the model

## Step 2: Gesture-Based Control

In this step, we use the trained model to control devices based on recognized hand gestures.

### Files

- `controller.py`: Script to control devices using recognized gestures.
- `detect_simulation.py`: Script to simulate gesture detection and control.
- `hand_gesture.yaml`: Configuration file containing gesture labels.
- `mock_controller.py`: Mock controller for testing purposes.

### Usage
1. Navigate to `step2/` folder
    ```sh
    cd step2
    ```

2. Run the gesture detection and control simulation:
    ```sh
    python detect_simulation.py
    ```

## License

This project is licensed under the MIT License.