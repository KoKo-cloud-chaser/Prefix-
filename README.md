Prefix + is a small scritp that can be used thru CMD or just by double-clicking on the file<br>
It was made for helping people converting a DiffSinger dataset to be used with multidict update<br>

HOW TO USE?<br>
  1- Download the "prefix_plus.py" file and drag it somewhere safe<br>
  2- Run the scirpt thru the CMD interface or by double-clicking on it<br>
  3- enter the path of the folder containing all you .lab files<br>
    ex: C:\Users\user\Desktop\Dataset\LAB<br>
  4-Enter the suffix you'd like to use<br>
    ex: ja/ (the suffix should change based off the language of the dataset)<br>
  5- Enjoy your labels!!!<br>

TIPS:<br>
  1- By default the scirpt WILL AVOID these phonemes [SP] [AP] [cl] [vf] [q] [exh] [TRS]<br>
     To change the or to add more you can open the .py file with a text editor and change the line 5<br>
    ex:     exclude_labels = {"a", "i", "u", "e", "o", "N", "TRS", "pau", "sil"}<br>
    <br>
    <br>BEFORE‎‎‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎AFTER<br>
        0 288000000 SP                           0 288000000 SP<br>
        288000000 296636979 o                    288000000 296636979 ja/o<br>
        296636979 297178955 r                    296636979 297178955 ja/r<br>
        297178955 304845807 e                    297178955 304845807 ja/e<br>
        304845807 306000000 t                    304845807 306000000 ja/t<br>
        306000000 311351341 a                    306000000 311351341 ja/a<br>
        311351341 312129841 g                    311351341 312129841 ja/g<br>
        312129841 321000000 e                    312129841 321000000 ja/e<br>
        321000000 322246786 N                    321000000 322246786 ja/N<br>
        322246786 322776570 g                    322246786 322776570 ja/g<br>
        322776570 331500000 a                    322776570 331500000 ja/a<br>
        331500000 335937874 SP                   331500000 335937874 SP<br>
        <br>
        <br>
CREDITS:
DiffSinger : https://github.com/openvpi/DiffSinger<br>
