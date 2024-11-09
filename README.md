Prefix + is a small scritp that can be used thru CMD or just by double-clicking on the file<br>
It was made for helping people converting a DiffSinger dataset to be used with multidict update

HOW TO USE?
  1- Download the "prefix_plus.py" file and drag it somewhere safe
  2- Run the scirpt thru the CMD interface or by double-clicking on it
  3- enter the path of the folder containing all you .lab files
    ex: C:\Users\user\Desktop\Dataset\LAB
  4-Enter the suffix you'd like to use
    ex: ja/ (the suffix should change based off the language of the dataset) 
  5- Enjoy your labels!!!

TIPS:
  1- By default the scirpt WILL AVOID these phonemes [SP] [AP] [cl] [vf] [q] [exh] [TRS]
     To change the or to add more you can open the .py file with a text editor and change the line 5
    ex:     exclude_labels = {"a", "i", "u", "e", "o", "N", "TRS", "pau", "sil"}

DiffSinger: https://github.com/openvpi/DiffSinger
