## Code Description

    File Name : DecoderLayers.py
    File Description : Setting up the decoder layers architecture and loading the trained model



    File Name : Engine.py
    File Description : Main class for starting different parts and processes of training and inference lifecycle



    File Name : EncoderLayers.py
    File Description : Setting up the encoder layers architecture and loading the backbone VGG model



    File Name : Inference.py
    File Description : Inference cycle for setting up the end to end pipeline of inferencing and saving the image



    File Name : References.py
    File Description : References class for keeping the constants and reference path to dataset and weights



    File Name : LoadData.py
    File Description : LoadDataset class for loading the image data and converting it to LAB format


## Steps to Run
`pip install -r requirements.txt`
- modify the path variables in references.py
- Modify `Engine.py` based on the mode that you are training on "Training" / "Inference"
- Run Code `python Engine.py`
