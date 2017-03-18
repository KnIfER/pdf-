Simple pdf-generator on phone (python2.7)</br>
===================================
----------
simple python pdf generator that convert a sheet of new words into a pdf.
This time,I choose to resort to reportlab for my solution.</br>
I based my work on a ReportLab sample file;I was lazy even to change the name(lol).</br>

*test_multibyte_chs2.py——script*</br>
*facorites.txt——sheet of new words exported from bluedict*

The code was tested on **Qpython1.2.5**&&**ReportLab2.5** on my phone,but you can easily modify it to run it on PC with **ReportLab2.5** and **python2.7** installed.</br>

----------

Install:
-----------------------------------
`1.`install Qpython1.2.5 from android App Market</br>
`2.`download ReportLab from github.</br>
`3.`extract the file,navigate to "...\ReportLab-master\src",and copy the two folder there(reportlab and rl_addons\renderPM) to this location on your phone:"(internal sdcard)/org.qpython.qpy/lib/python2.7/site-packages/".</br>
now you should be able to start a console via Qpython,and import reportlab without errors.</br>
`4.`copy **test_multibyte_chs2.py** as well as **facorites.txt** to:"(internal sdcard)/org.qpython.qpy/scripts/".</br>
`5.`run test_multibyte_chs2.py on App Qpython through program menu.</br>
(change the directory"/storage/emulated/0/org.qpython.qpy/scripts/favorites.txt"and"/storage/emulated/0/org.qpython.qpy/scripts/rp2.pdf"in the file if necessary.)
