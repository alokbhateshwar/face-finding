🧍 Person Detection using OpenCV + MobileNet SSD
This project showcases a simple yet effective person detection system built with OpenCV's DNN module and a pre-trained MobileNet SSD model. It is designed to detect and localize humans (only class "person") in static images.

Whether you're a computer vision enthusiast, recruiter, or fellow developer, this project highlights my interest in applied AI and my skills in building efficient image processing pipelines.

🚀 Key Features
✅ Person Detection Only
Accurately detects human figures in photos using a lightweight and fast model.

✅ Pre-Trained Caffe Model
Utilizes MobileNetSSD trained on VOC dataset, no additional training needed.

✅ Bounding Box Visualization
Draws labeled boxes around detected persons for easy understanding of results.

✅ Easy to Run
Just one script (main.py) — no complex setup, no heavy dependencies.

✅ Modular Design
Well-structured code for easy extension to video input, real-time camera use, or multi-class detection.

⚠️ Disclaimer
This project detects only persons in images.
Age, gender, or facial features are not predicted in this version.
For full image classification or face recognition, separate models would be required.

🛠️ Technologies Used
🧠 OpenCV – Computer vision library used for model loading and image processing

💡 MobileNetSSD (Caffe) – Lightweight deep neural network trained on VOC classes

🐍 Python 3.x – Core language for scripting and implementation

💾 Caffe Model Zoo – Pre-trained model source

📷 Jupyter / VS Code – Development environment

📁 Project Structure
graphql
Copy
Edit
models/
├── MobileNetSSD_deploy.prototxt       # Network architecture
├── MobileNetSSD_deploy.caffemodel     # Pre-trained weights
main.py                                # Person detection script
input.jpg                              # Sample image for testing
README.md                              # Project documentation
▶️ How to Run
📦 Install OpenCV:

bash
Copy
Edit
pip install opencv-python
📂 Ensure your files are in the correct structure.

🖼️ Replace input.jpg with your own image or use the default.

🏃 Run the script:

bash
Copy
Edit
python main.py
🎯 The script will display the image with bounding boxes around detected people.

✨ Sample Output
arduino
Copy
Edit
Detected: Person
Bounding box drawn at coordinates: (x, y, width, height)
