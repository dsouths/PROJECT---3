![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome dsouths,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **August 17, 2021**

## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!

<h1>HANGMAN World Cup 22 Edition</h1>

<b>[Deployed Website](https://hangman-worldcup22-edition.herokuapp.com/)</b>

<b>[Github](https://)</b>

![am i responsive]()

<!--ts-->
   * [Intro](#intro)
   * [UX](#ux)
   * [Features](#features)
   * [Validation Checks](#validation-checks)
   * [Bugs](#bugs)
   * [Technologies Used](#technologies-used)
<!--te-->


<h2>Intro</h2>
I have created a WORLD CUP 22 HANGMAN game which utilizes Python, with the purpose of the project to showcase the skills I have learned in the latest Code Institute module, Python. The game choses a word/country at random from the predetermined list of words/countries (playing in the World Cup 22), then replaces the letters with _ and the player has a number of turns to pick the correct letters & then guess the word before the final hangman stage. The goal of the game is to enteratin the user & challenge them to guess the correct letters and ultimately country playing in the world cup 22.. 

<h2>UX</h2>
 
I plan to incorporate the following into the user experience (UX):
 * a game that is easy to understand, intuative & entertaining for the user
 * the game should work without any bugs or faults  


<h2>Features</h2>
I plan to include the following features:
  * _ is replaced with letter when correct letter is guessed
  * a guess of only one letter at a time is valid e.g. a allowed / ae not allowed
  * numbers are not a valid guess
  * with each wrong guess the hangman image/stage progresses until the game is over
  * max attempts of six 
  * game keeps track of guessed words & guessed letters & informs the player if they have already guessed them

<h3>Main Screen</h3>



<h3>Media Queries</h3>

I ensured the website would work on multiple screen sizes to ensure a smooth user experience irrespective of the device the user chose to use tablet, phone, desktop, etc. I did however chose a mobile first design & feel the game is optimal for mobile devices...entertainment & fun on the go  

<h2>Validation Checks</h2>

<b>W3c Html Validation service</b>


<b>Wev Dev Tools Chrome</b>

I used web dev tools in chrome to access the quality & accessibility of the webpage. It gave me insight into how the RockPaperScissors website performed & scored highly in Performance, Accessibility, Best Practices & SEO for both desktop & mobile devices

<b>Mobile Devices</b>

![lighthouse 1 ](https://user-images.githubusercontent.com/105642587/193277827-ce4090be-d69e-435d-b242-2fe1f1e3eb22.jpg)

<b>Desktop devices</b>

Initially the SEO was resulting in score of 89

![lighthouse desktop](https://user-images.githubusercontent.com/105642587/193277836-6eae1716-2487-4566-9383-d801ce09cb2e.jpg)

I added in meta descriptions within HTML header as per advice from lighthouse guidance & increased the score to 100 (seen below)

![lighthouse desktop 2](https://user-images.githubusercontent.com/105642587/196782302-9989e111-54fe-4c5d-b5d4-4905cd97af04.jpg)


<h2>Bugs</h2>

<b>Deployed website would not function - </b> Issue with relative & absolute file path for javascript file "app.js", would work with gitpod website preview using:
<script src="assets/app.js"></script>  

but would not function on deployed website. For javascript file to load correctly I changed to absolute file path  
<script src="/rockpaperscissors---P2/assets/app.js"></script>
<hr>
<b>Issue with gameOver function - </b> I had issues with getting game to stop when user or computer reached max_points (set to 10 in this example).I overcame this by setting a variable as "let isGameover = false;". Then adding isGameOver function into the game() function. So if isGameOver function is false then play the game. Within the game function the gameOver function was included to run with statements defined within the function gameOver() with an else if statement. These determined the conditions for who won, the user or computer or if the game was drawn. The code was executed if the conditions were true, i.e.
<br>


<hr>
<b>Restart button only appearing when game was over - </b> I initially had this as display:none within CSS but this did not work. I overcame this issue by including CSS styling rules within the gameOver function: 

  
<h2>Deployment</h2>

The website was deployed on GitHub by using following steps:

<ol>
<li>Login into GitHub and locate the repository - pharmacy </li>
<li>At the top of repository locate the "settings" button and click on it </li>
<li>On the left sidebar find locate the "pages" button and click on it</li>
<li>Click on the branch dropdown menu and select: master</li>
<li>Click save</li>
<li>Link to your deployed repository appears</li>



</ol>
  
<h2>Technologies Used</h2>

* HTML
* CSS
* Javascript

<h3>Tools</h3>

* [Git hub](https://github.com/)
* [Git pod](https://www.gitpod.io/docs/configure/)
* [W3c Html Validation service](https://validator.w3.org/)
* [W3c Css Validation service](https://jigsaw.w3.org/css-validator/)
* [JSHint JavaScript Validator](https://jshint.com/)
* [WebDev Checker](https://web.dev/measure/)
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
* <b>[GeeksForGeeks](https://www.geeksforgeeks.org/) - </b>useful resource to see worked examples to improve my understanding of JavaScript syntax & functions
* <b>Youtube</b> - I found a number of tutorials on youtube useful in helping me understand 

<h3>Final Note</h3>

I found this project to be particularly challenging, even more so than HTML & CSS. It was rewarding when functions worked correctly but was very frustrating when bugs appeared or functions would not work correctly. Through perseverance & the aid of my colleagues in the code institute slack channel, reviewing the Javascript module from Code Institute numerous times,  my mentor Martina, stack overflow threads & youtube tutorials I was able to improve my understanding of Javascript structure, functions & syntax. I hope to build on the skills I have developed & realise I can improve my knowledge futher by continuing to build other projects, which I plan to do.

Thank you

daves
