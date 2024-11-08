# Computer vision-based Trailer Positioning System
<p align="justify">
A computer vision-based trailer positioning system developed during my internship at Colombo International Container Terminal (CICT). This project aims to assist crane operators and truck drivers by optimizing container loading and unloading processes. Using real-time feedback displayed on an LED screen, drivers are guided to align trailers accurately in their lanes, reducing time and enhancing efficiency.
</p>

## Overview
<p align="justify">
  Efficient trailer alignment is critical in container terminals, as even minor misalignments can lead to delays and reduce overall operational efficiency. During this project, we explored several positioning methods, including laser sensor-based systems and 3D LiDAR for trailer detection and alignment. However, these approaches faced challenges, such as accuracy issues in terminal conditions, high installation costs, and maintenance difficulties.
</p><p align="justify">
 After extensive testing, we developed a computer vision-based solution that proved to be the most reliable and cost-effective method. This system uses real-time camera feeds to accurately detect trailer position and provides immediate feedback to drivers through an LED display. By guiding drivers with directional arrows for forward and backward movements, the system ensures precise alignment, reducing delays and enhancing workflow efficiency.
</p>

## Features
* Real-time Trailer Position Detection: The system can accurately detect trailers in any of five designated lanes, with the flexibility for the deck operator to switch the job lane at any time. This adaptability ensures that operations can be adjusted quickly to meet real-time demands.
* LED Feedback System: Displays directional arrows on an LED screen to guide the driver, with a green light indicating correct alignment.
* Custom Trained Model: The system is powered by a custom-trained model based on the pre-trained YOLOv8s-seg.pt segmentation model. We enhanced the model's accuracy by training it on a custom dataset, consisting of over 300 images captured in both day and night conditions at the terminal. This diverse dataset helped the model adapt to varying environmental factors and lighting conditions. Through fine-tuning and training on this dataset, we achieved over 80% accuracy in detecting trailer positions and container tops, ensuring reliable performance in real-world applications.

[Watch the demo video](https://www.linkedin.com/posts/viranjan-de-silva_computervision-yolov8-containerterminal-activity-7197870569726386176-FHVX?utm_source=share&utm_medium=member_desktop)
