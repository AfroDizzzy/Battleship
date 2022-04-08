Created by: David Rhode
Dated: 08/04/2022
Version: 1.0

Running the game in windows (Unix users be gone!):
1: Install python3, follow these steps: https://phoenixnap.com/kb/how-to-install-python-3-windows
	1.1: Or make sure you are running the right version of Python
	1.2: Open a Command Prompt or Power shell. 
	1.3: Type "python -V"
	1.4: If the output is 3.xx.x youre good to go!
2: Make sure that both main.py and board.py are in the same directory!
3: Open a Command Prompt or Power shell
4: Navigate to the directory of both files
5: Input "python main.py"
6: ???
7: Profit!

10:Currently the game is set to normal mode, to change to cheater mode(for better debugging and assessment) change line 28 of main.py to gameboard.cheaterDisplay(gameBoard.getGrid())


Notes:
Other implementations or ways to make this game include:
https://gist.github.com/guimaion/9275543

And in Javascript:
https://github.com/Naturalclar/battleship-node
https://github.com/LearnTeachCode/Battleship-JavaScript/blob/gh-pages/battleship.js

I have decided to write my own approach as these implementions are very rigid and do not try to adhear to a more functional programming methodology. 
My pseudo functional approach allows me to debug faster and allows easier changing of values for future iterations of the game.


CODE DEBT
My favourate. This game needs unit tests written for it but due to time I have omited this from this release.
While I have tried to account for all edge cases and erronious user inputs, no doubt I have missed somethings. 
I have account for inputting a number out of the games board area, inputing a word instead of a number, and inputing negative numbers and decimal numbers. 

Further, it would be nice to clear the terminal after each game cycle. I have found the code neccesary to do this, but 
implementing would take more work than is worth the small edition.
