
# Project Description

## Name : Real Time Pedestrian and Vehicle Detection using Computer Vision [Web App] 

Detecting pedestrians and vehicles in a real-time environment can be quite challenging, especially when there are a lot of details to consider. 

The project is a basic prototype of detecting pedestrians and vehicles separately in a live video. However, for testing purposes, car dashcam recordings, available on youtube have been used.

The front-end GUI has also been implemented so that users can directly feed their videos and check for accuracy.

To keep the method simple enough, for this project, Haar Cascade Classifiers have been used :

Haar Cascade Classifier XML Files : 
- Pedestrians: https://raw.githubusercontent.com/ope...
- Cars: https://raw.githubusercontent.com/and...

A much similar approach is being used by Tesla in their self-driving cars, rather than using LIDAR technology. Some articles related to this : 

- Tesla's CV: https://softmax.substack.com/p/teslas...
- Why LIDAR is doomed: https://www.voltequity.com/article/wh...

Ending Credits 
- Made using Python and OpenCV
- @Author : Sagar Bapodara


## Acknowledgements

I would like to thank Clever Programmer for creating an awesome basic prototype tutorial. 

I would also like to thank Miguel Riem Oliveira and Vitor M F Santos for their amazing research paper.

Research Paper : https://www.researchgate.net/figure/Car-dataset-taken-by-Brad-Philip-and-Paul-Updike-California-Institute-of-Technology-It_fig5_267863282
## Tech Used 

**Language:** Python

**Front-End:** Streamlit

**Libraries:** OpenCV, Streamlit

_Please Note that this technology is being used for the latest version. Further improvements in the project may result in changes in the technology used. It will be updated above as well._ 
## Working Demo 

The demo working of this web app can be found here : https://youtu.be/Olgb3hlpSV8


## Installation / Working

Clone this repository or Download the files into your local system. 

- Extract the ZIP file (if you directly download from Github Web)
- Open your Command Prompt (CMD) where the project files have been downloaded.
- Type the following command : 

```bash
python main.py
```
- Type the following command (for web app) : 

```bash
streamlit run main_web.py
```
## Further Improvemets (In Progress)

- Connecting Live Feed as Input and Process Output in MP4 Format
- Calculating real-time distances between various vehicles using Live Feed
- Calculating the speed of vehicles and alerting the driver based on 'near distance' as parameter.
- Adding more detection details such as animals, emergency vehicles, pathways, etc. 
  
## 🚀 Thanks

Thanks for looking into the project and being here. Feel free to share your reviews/suggestions/remarks! :)

**If you found it useful, leave a ⭐ here!**

## License

[MIT](https://choosealicense.com/licenses/mit/)

  
