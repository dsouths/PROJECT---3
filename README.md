  

<h1>HANGMAN World Cup 22 Edition</h1>

Click for <b>[Deployed Website](https://hangman-worldcup22-edition.herokuapp.com/)</b>

Click for <b>[Github](https://github.com/dsouths/PROJECT---3)</b>


<!--ts-->
   * [Intro](#intro)
   * [UX](#ux)
   * [Features](#features)
   * [Validation Checks](#validation-checks)
   * [Bugs](#bugs)
   * [Technologies Used](#technologies-used)
<!--te-->

<h2>Intro</h2>
I have created a WORLD CUP 22 HANGMAN game which utilizes Python, with the purpose of the project to showcase the skills I have learned in the latest Code Institute module, Python. The game choses a word/country at random from the predetermined list of words/countries (playing in the World Cup 22), then replaces the letters with ~ and the player has a number of turns to pick the correct letters & then guess the word before the final hangman stage. The goal of the game is to entertain the user & challenge them to guess the correct letters and ultimately correct country playing in the world cup 22.. 

<h2>UX</h2>
 
I plan to incorporate the following into the user experience (UX):
 * a game that is easy to understand, intuative & entertaining for the user
 * the user can easily distinguish when the game is over & can easily restart the game to play again
 * the game should work without any bugs or faults  


<h2>Features</h2>

I plan to include the following features:
  * ~ is replaced with letter when correct letter is guessed
  * a guess of only one letter at a time is valid e.g. a allowed / ae not allowed
  * numbers are not a valid guess
  * with each wrong guess the hangman image/stage progresses until the game is over
  * max attempts of six 
  * game keeps track of guessed words & guessed letters & informs the player if they have already guessed them
 
In creating this game it gave me the opportunity to employ many aspects of Python I had covered on the Code Institute (CI) module. To enable me to create the features above I had to use the following within this project:
  * <b>LISTS -</b> creating lists & importing the random function to randomly chose a word from the word list 
  * <b>APPEND METHOD -</b> adding guessed letters & words into separate lists to keep track of guessed letters/words for player e.g. guessed_words.append(guess)
  * <b>WHILE LOOPS -</b> the condition for while loop is boolean value "True", used to loop over the letters multiple times & keep asking theplayer to guess a letter (each time the player guessed a letter) until the "letters guessed" becomes true. A for loop was not  suitable here as it loops over data once.  The guessed letters/words are stored in the variable guessed_letters/words 
  * <b>IF/ELIF/ELSE STATEMENTS</b> - including nested if/else statements. These were perfect for a hangman game as I required different outcomes depending on the user input e.g. if number was guessed/more than one letter guessed would be an invalid guess. They work by giving the instructions; if this is true, do this or if the next condition is true carry out this function, or if neither are true carry out a different function  
  * <b>FUNCTIONS -</b> I used the following functions; 
  
  * def pick_word(): takes a list of strings & returns one string e.g. the word at random from word list 
  * def play_game(word): is the main function of the game in determining the outcome of player choice. Also included game state if the guess if True or False
  * def main(): this function calls to action the play_game(word) function & also includes a while loop to ask if the player wants to play again. This keeps the player engaged & increases likelihood player will play another game.

 

<h2>Validation Checks</h2>


<h2>Bugs</h2>

<b>Letter "W" was coming up as an invalid entry - </b> I had not included it & had incorrectly typed "E" in it's place within the if statement "if guess not in 'ABCDEFGHIJKLMNOPQRSTUVEXYZ':". I amended this which fixed the issue

![image](https://user-images.githubusercontent.com/105642587/203580749-674317f3-069a-46dc-8ad4-265dae652cdb.png)

<b>Hangman stages not printing - </b> I had placed the hangman stages/images within a function, making them a local variable. When calling display_hangman outside of the function this was giving the error "local variable referenced before assignment". I moved the hangman stages variable outside of the function  to the start of the code, making them a global variable, which allowed me to call on them within the play_game() function.

![image](https://user-images.githubusercontent.com/105642587/203581900-65a0b41c-3486-4e6b-8c51-3ddf520e368e.png)

<b>Hangman stages appearing in wrong order - </b> I placed the display_hangman stages in the wrong order. I have attempts set  

![image](https://user-images.githubusercontent.com/105642587/203602251-8b61d914-3caa-405c-a7cd-c732e68810d8.png)



<br>
<hr>


  
<h2>Deployment</h2>

The website was deployed on Heroku via GitHub by using following steps:

<ol>
<li>Login into GitHub and locate the repository - pharmacy </li>
<li>At the top of repository locate the "settings" button and click on it </li>
<li>On the left sidebar find locate the "pages" button and click on it</li>
<li>Click on the branch dropdown menu and select: master</li>
<li>Click save</li>
<li>Link to your deployed repository appears</li>



</ol>
  
<h2>Technologies Used</h2>

* Python

<h3>Tools</h3>

* [Git hub](https://github.com/)
* [Git pod](https://www.gitpod.io/docs/configure/)
* [Heroku](https://dashboard.heroku.com/)
* [Am I Responsive](https://ui.dev/amiresponsive)
* [Stack OverFlow](https://stackoverflow.com/)
* [Evernote](https://evernote.com/)


<h3>Credits/References</h3>

<li><b>Code Institute - </b>giving me the knowledge & skills to develop this project</li>
<li><b>W3 Schools (https://www.w3schools.com/) - </b>clearing up some function queries I had</li>
<li><b>Stack Overflow - </b>another extremely useful resource I used to rectify many issues with my code throughout the project including how to make my game end when getting to max amount of points</li>

<h3>Acknowledgements</h3>

* <b>martina_mentor - </b>my mentor Martina who was always on hand to answer any questions
* <b>Code Institute Channel on Slack - </b> I found this a great resource with many knowledgeable people who were more than willing to answer my questions & help out.
* <b>Youtube</b> - I found a number of tutorials on youtube useful in helping me understand 

<h3>Final Note</h3>

I found this project to be particularly challenging, even more so than HTML & CSS. It was rewarding when functions worked correctly but was very frustrating when bugs appeared or functions would not work correctly. Through perseverance & the aid of my colleagues in the code institute slack channel, reviewing the Javascript module from Code Institute numerous times,  my mentor Martina, stack overflow threads & youtube tutorials I was able to improve my understanding of Javascript structure, functions & syntax. I hope to build on the skills I have developed & realise I can improve my knowledge futher by continuing to build other projects, which I plan to do.

Thank you

daves
