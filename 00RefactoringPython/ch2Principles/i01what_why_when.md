<b>重构</b>： 对软件内部结构的一种调整，目的是在不改变软件可观察行为的前提下，
提供可理解性，降低修改成本。

重构就只是整理代码？
某种程度是的，但重构不止于此，它提供了一种<b>更高效而且受控</b>的代码整理技术。

重构和性能优化？
性能优化通常也不改变组件的行为（除了速度），但是2者出发点不同：
性能优化往往让代码较难理解，但为了得到所需性能你不得不这么做。
<br><br>

![](https://raw.githubusercontent.com/greatabel/RefactoringPython/master/ch2Principles/2hats.jpeg)
<b>&nbsp;添加新功能</b>时候，你不应该修改既有代码，只管添加新功能。。通过测试，衡量工作进度。<br>
<b>&nbsp;重构时候</b>你就不能再添加功能，只管改进程序结构。此时不应该添加测试。<br>
软件开发中，你可能发现自己经常变换帽子，可能来回切换，但是无论何时你都要清楚自己戴的是哪一顶帽子。

![#f03c15](https://placehold.it/15/f03c15/000000?text=+) 
<b>why 需要重构？</b>
1. 改进软件设计<br>
···重构就像整理代码，让所有东西回到应处的位置，代码结构流失是累积性。<br>
···经常性的重构帮助代码维护自己该有的形态
2. 让软件更容易理解<br>
<img src="https://raw.githubusercontent.com/greatabel/RefactoringPython/master/ch2Principles/clean_window.jpg" height="100" width="100">
早起重构像：擦掉窗户上的污垢，使得你看的更远。重构把我带上更高理解层次；如果没有重构，我达不到这种层次。<br>
3. 重构提高编程速度
···重构帮助你更快速的开发程序<br>
···良好的设计是快速开发的根本
<img src="https://raw.githubusercontent.com/greatabel/RefactoringPython/master/ch2Principles/modao.jpg" height="200" width="200">


![#b49ee5](https://placehold.it/15/b49ee5/000000?text=+) 
<b>when 需要重构？</b>
- 事不过三， 三则重构
- 添加功能时候
- 修补错误时候
- review代码时候







