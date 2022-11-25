  

<h1>HANGMAN World Cup 22 Edition</h1>

![image](https://user-images.githubusercontent.com/105642587/203990534-858eecfa-7877-4bad-a22b-f82dd8d14c25.png)


Click for <b>[Deployed Website](https://hangman-worldcup22-edition.herokuapp.com/)</b>

Click for <b>[Github](https://github.com/dsouths/PROJECT---3)</b>


<!--ts-->
   * [Intro](#intro)
   * [UX](#ux)
   * [Features](#features)
   * [Validation](#validation)
   * [Media Queries](#media-queries)
   * [Bugs](#bugs)
   * [Improvements](#improvements)
   * [Technologies Used](#technologies-used)
<!--te-->

<h2>Intro</h2>

I have created a WORLD CUP 22 edition of the classic game Hangman, which utilizes Python, with the purpose of the project to showcase the skills I have learned in the latest Code Institute module, Python. The game choses a word/country at random from the predetermined list of words/countries (playing in the World Cup 22), then replaces the letters with ~ and the player/user has a number of turns to pick the correct letters & then guess the word before the final hangman stage. The "goal" of the game is to entertain the user & challenge them to guess the correct letters and ultimately correct country playing in the world cup 22.. 

<h2>UX</h2>
 
As a player/user of hangman I want to guess letters so that I can complete the word & guess it before the final hangman stage, to win the game. 

I plan to incorporate the following into the user experience (UX) to help achieve this:
 * a game that is easy to understand, intuative & entertaining for the user
 * the user can easily distinguish when the game is over & can easily restart the game to play again
 * when the game begins the letters appear as "~" to indicate how many letters are in the word
 * when the correct letter is guessed it appears in the word & the dashed word is update with the guess letters
 * the user can guess a word 
 * validation within the game to stop the user from guessing numbers or two or more letters incorrectly while still allowing player to guess the word
 * the game should work without any bugs or faults  


<h2>Features</h2>

I plan to include the following features:
  * ~ is replaced with letter when correct letter is guessed
  * a guess of only one letter at a time is valid e.g. a allowed / ae not allowed
  * numbers are not a valid guess
  * with each wrong guess the hangman image/stage progresses until the game is over
  * max attempts of six 
  * game keeps track of guessed words & guessed letters & informs the player if they have already guessed them

I have chosen a World Cup 22 theme to separate the hangman game from the many others out there & help create a positive emotional response with the player, & ultimately make the game more fun & entertaining.  Print statements are given when: 

<b>A correct letter is guessed: </b>

![image](https://user-images.githubusercontent.com/105642587/203985811-aa1f074b-354c-485e-8568-5188a828cf5f.png)

<b>A letter has already been guessed:</b>

![image](https://user-images.githubusercontent.com/105642587/203985985-f46461b3-4cd2-461d-8488-eb832482182c.png)

<b>An incorrect letter is guessed, including the stage of hangman (1-6):</b>

![image](https://user-images.githubusercontent.com/105642587/203986188-566cca1b-d4f7-4854-9a0b-247f744624b4.png)

<b>A validation checker to ensure only one letter or the word is guessed e.g. will not allow numbers of multiple letters to be guessed:</b>

![image](https://user-images.githubusercontent.com/105642587/203988874-e141de42-65bc-4a79-a490-1bb896e22e18.png)

 
In creating this game it gave me the opportunity to employ many aspects of Python I had covered on the Code Institute (CI) module. To enable me to create the features above I had to use the following within this project:
  * <b>LISTS -</b> creating lists & importing the random function to randomly chose a word from the word list 
  * <b>APPEND METHOD -</b> adding guessed letters & words into separate lists to keep track of guessed letters/words for player e.g. guessed_letters.append(guess)
  * <b>WHILE LOOPS -</b> the condition for while loop is boolean value "True", used to loop over the letters multiple times & keep asking theplayer to guess a letter (each time the player guessed a letter) until the "letters guessed" becomes true. A for loop was not  suitable here as it loops over data once.  The guessed letters/words are stored in the variable guessed_letters/words 
  * <b>IF/ELIF/ELSE STATEMENTS</b> - including nested if/else statements. These were perfect for a hangman game as I required different outcomes depending on the user input e.g. if number was guessed/more than one letter guessed would be an invalid guess. They work by giving the instructions; if this is true, do this or if the next condition is true carry out this function, or if neither are true carry out a different function  
  * <b>FUNCTIONS -</b> I used the following functions; 
  
  * def pick_word(): takes a list of strings & returns one string e.g. the word at random from word list 
  * def play_game(word): is the main function of the game in determining the outcome of player choice. Also included game state if the guess if True or False
  * def main(): this function calls to action the play_game(word) function & also includes a while loop to ask if the player wants to play again. This keeps the player engaged & increases likelihood player will play another game.

<h2>Validation</h2>

Using the CI Pep8 validator on Gitpod as per CI slack channel (as below):

![image](https://user-images.githubusercontent.com/105642587/203642414-3142dbf0-ec42-4322-ac49-1cef67ba6612.png)

![image](https://user-images.githubusercontent.com/105642587/203642292-4bc7462e-c565-4180-a653-e6e9ac3cb4f0.png)

![Screenshot_20221125_105631](https://user-images.githubusercontent.com/105642587/203970229-57a429dd-0b05-43ac-a2b2-52ee70fbc8fe.png)

I fixed a lot of the issues which included, trailing whitespace, lines too long (>79 characters) & spacing issues. Using the PEP8 rules improved the readibility of my code.    

I have also tested the deployed website by purposefully entering incorrect data to ensure validation is working correctly, & it is. 

![image](https://user-images.githubusercontent.com/105642587/203988874-e141de42-65bc-4a79-a490-1bb896e22e18.png)

![image](https://user-images.githubusercontent.com/105642587/203985985-f46461b3-4cd2-461d-8488-eb832482182c.png)

<h2>Media Queries</h2>

As this is a command line interface on a mock terminal there is less scope for reponsive design than my last two projects, using Javascript/CSS & HTML. As you can see above the mock terminal/heroku webpage displays well on different devices. I tested this on my own devices, PC, macbook & phone. 

<h2>Bugs</h2>

<b>Letter "W" was coming up as an invalid entry - </b> I had not included it & had incorrectly typed "E" in it's place within the if statement "if guess not in 'ABCDEFGHIJKLMNOPQRSTUVEXYZ':". I amended this which fixed the issue

![image](https://user-images.githubusercontent.com/105642587/203580749-674317f3-069a-46dc-8ad4-265dae652cdb.png)

<b>Hangman stages not printing - </b> I had placed the hangman stages/images within a function, making them a local variable. When calling display_hangman outside of the function this was giving the error "local variable referenced before assignment". I moved the hangman stages variable outside of the function  to the start of the code, making them a global variable, which allowed me to call on them within the play_game() function.

![image](https://user-images.githubusercontent.com/105642587/203581900-65a0b41c-3486-4e6b-8c51-3ddf520e368e.png)

<b>Hangman stages appearing in wrong order - </b> I placed the display_hangman stages in the wrong order. I have attempts set  

![image](https://user-images.githubusercontent.com/105642587/203602251-8b61d914-3caa-405c-a7cd-c732e68810d8.png)

<b>Importing words from Google Sheets - </b> I was having issues pulling a random words from the list on the google sheet. I followed the walkthrough love sandwiches which helped me through these issues. Initially I had the words list in a separate words.py file but decided to utilize the skills developed from love sandwiches walkthrough & use google sheets to host the list of words for hangman game. I ensured credentials (creds.json) where placed in the gitignore file to stop sensitive data being pushed to github, as per the Love Sandwiches walkthrough project.

![image](https://user-images.githubusercontent.com/105642587/203996385-cee25628-2f1b-478b-a3b0-b6c89a63c7fc.png)

<b>Issue with importing gspread when deploying to Heroku - </b> The deployed command line interface on Heroku was not functioning & could not import spread function. It became apparent that I had not completed the requirements.txt file or added the credentials info from the cred.json file to Heroku so it could not pull the data from the google sheet. After reviewing the love sandwiches walk through I figured out I had missed this & reconfigured the settings. This solved the issue...phew! 


<h2>Improvements</h2>

To improve on the game I would like to add more complexity to the game & add a difficulty level function to the game. I would include easy, medium & difficult words to challenge the user. 

<h2>Deployment</h2>

The website was deployed on Heroku via GitHub by using following steps:

<ol>
<li>Login into GitHub</li>
<li>Sign up & activate Heroku account </li>
<li>Create app & configure settings including adding buildpacks 
<li>Ensure GitHub is connected by logging into GitHub & accepting prompts to link Heroku account with GitHub</li>
<li>Set manual or automatic deployment. I set to automatic so any changes made to my repository are updated on Heroku. Click on "deploy branch"</li>
<li>Test deployed webpage to ensure it works correctly. CLick on open app to open deployed webpage</li>
</ol>

![Screenshot_20221125_112945](https://user-images.githubusercontent.com/105642587/203976604-694bdc11-5800-4a3f-88a2-e7669bd3fbd6.png)

![image](https://user-images.githubusercontent.com/105642587/203976832-2b29cc9e-c19f-4441-8838-ab380bf2cdb5.png)

![image](https://user-images.githubusercontent.com/105642587/203977558-271853f1-f246-4d57-9882-34961ae0fdbe.png)

![image](https://user-images.githubusercontent.com/105642587/203977927-411c3c2e-ca5a-4aa7-ab9b-8291bfa00a86.png)

![image](https://user-images.githubusercontent.com/105642587/203977961-2d4f61f2-22e0-48fe-89d9-95aa07a4d9f5.png)

  
<h2>Technologies Used</h2>

* Python

<h3>Tools</h3>

* [Git hub](https://github.com/) - hosting repository
* [Git pod](https://www.gitpod.io/docs/configure/) - open source developer platform automating the provisioning of ready-to-code developer environments.
* [Heroku](https://dashboard.heroku.com/) - container-based cloud Platform as a Service (PaaS). Used to deploy, manage, and scale the apps in a mock terminal 
* [Am I Responsive](https://ui.dev/amiresponsive) - checks if website fits different devices, e.g. tablets, phones, laptops, etc
* [Stack OverFlow](https://stackoverflow.com/) - a great source of knowledge 
* [Evernote](https://evernote.com/) - used to store & organise information & screenshots of project


<h3>Credits/References</h3>

<li> <b>Code Institute - </b> giving me the knowledge & skills to develop this project</li>
<li> <b>W3 Schools - </b>clearing up some function queries I had</li>
<li> <b>Stack Overflow - </b>another extremely useful resource I used to research bugs throughout the project</li>

<h3>Acknowledgements</h3>

* <b>martina_mentor - </b>my mentor Martina who was always on hand to answer any questions
* <b>Code Institute Channel on Slack - </b> I found this a great resource with many knowledgeable people who were more than willing to answer my questions & help out.
* <b>Youtube</b> - I found a number of tutorials on youtube useful in helping me understand the structure & syntax of Python, including those by MikhailLenko, Kite, 
Shaun Halverson, MJ Codes & Kylie Ying.  I used these, in particular, Kite & MikhailLenko, as a basis for my project & built my World Cup 22 edition around this code. They were helpful in understanding functions, while loops, lists & list methods such as append. 

<h3>Final Note</h3>

I found this project very challenging, as it was my first experience with Python.  Through perseverance & the aid of my colleagues in the code institute slack channel, reviewing the Python module from Code Institute numerous times,  my mentor Martina, stack overflow threads & youtube tutorials I was able to improve my understanding of Python structure, functions & syntax. I have taken on board feedback from my last project & have tried to employ as much of the advice given a possible namely; improving on git commits, being more concise with my git commits & expanding on validation & tests performed.  Hopefully this shows within this Python project!

Thank you

daves
