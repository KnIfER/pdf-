#pdf-生词本生成器 (python2.7)
===================================
----------
目的：https://www.zhihu.com/question/57245075</br>
在手机上生成pdf单词本，以取代bluedict自带的。

原理是在手机端运用了Qpython联合ReportLab.</br>
基于ReportLab的一个同名例程.</br>

`1.`*test_multibyte_chs2.py——脚本*</br>
`2.`*facorites.txt——从bluedict中导出的单词本*</br>

The code was tested on **Qpython1.2.5**&&**ReportLab2.5** on my phone,but you can easily modify it to run it on PC with **ReportLab2.5** and **python2.7** installed.</br>

----------

安装:
-----------------------------------
`1.`从安卓App市场安装 Qpython1.2.5</br>
`2.`从github下载ReportLab.</br>
`3.`解压ReportLab-master.zip。</br>导航至 "...\ReportLab-master\src",复制两个文件夹——reportlab以及rl_addons\renderPM.粘贴它们到手机上的这个位置："(内部存储卡)/org.qpython.qpy/lib/python2.7/site-packages/".</br>
现在，你应该可以打开Qpython，在左拉菜单里启动python终端，然后顺利执行import reportlab命令</br>
`4.`复制 **test_multibyte_chs2.py** 与 **facorites.txt** 到："(手机内部存储卡)/org.qpython.qpy/scripts/".</br>
`5.`最后，在Qpython上，左拉菜单“程序”里，运行test_multibyte_chs2.py。</br>
根据实际情况，这个脚本里可能有两个路径要改：</br>"/storage/emulated/0/org.qpython.qpy/scripts/favorites.txt"</br>以及"/storage/emulated/0/org.qpython.qpy/scripts/rp2.pdf"</br>

----------
吾诚吾意，谨以此献志合者。</br>
/(ㄒoㄒ)/~~。
