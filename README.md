# Coupe d'été
**Processing sketch for a nice summer haircut.**

This is a Processing sketch written in Python mode that generates simple visual compositions (fixed image) with a bunch of hair-like particles in a gradient of lengths and denisties.

![Coupe d'été](https://github.com/julienlabat/coupe_d_ete/blob/main/2021_05_29/coupe_d_ete_1914333515.png "Coupe d'été")

See **2021_5_29** folder for png of examples.

## Editing and running the code
You need [Processing 3](https://processing.org/download/) with Python mode installed to edit and execute the code. The main file is **coupe_d_ete.pyde**

## Saving generated pictures
**export.py** defines the mousePressed method to save and export sketch parameters. When executing the code, a click on the canvas will save a `.png` file of the generated image as well as a `.txt` file containing the variables set at the top of the `.pyde` file in a new folder named with the date (so you can play around with them and keep track of which variables values produce which kind of pictures).
