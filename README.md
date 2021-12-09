:warning: Everything between << >> needs to be replaced (remove << >> after replacing)
# CS110 Project Proposal
# Vagabond Game
## CS 110 Final Project
### Fall 2021
### [Assignment Description](https://docs.google.com/document/d/1H4R6yLL7som1lglyXWZ04RvTp_RvRFCCBn6sqv-82ps/edit#)

[https://docs.google.com/document/d/1H4R6yLL7som1lglyXWZ04RvTp_RvRFCCBn6sqv-82ps/edit#](#)

<< [link to demo presentation slides](#) >>

### Team: Ampalker
#### John Paul Alker, Paul Ampadu

***

## Project Description *(Software Lead)*
Our project is of of a game with one main character and enemies that move back and forth. The main character can move horizontally and jump, and get into fights with enemies. When the enemy and main character fight, the main character most likely win the fight, but there is a small chance that he will lose to the enemy. If the main character loses all his health points, the game will be over. If the main character does not, he will win. 

***    

## User Interface Design *(Front End Specialist)*

![image](https://user-images.githubusercontent.com/89813338/140586605-9adc09ef-7bd7-4390-bd09-4385bbdeb792.png)

* This is the start menu
   
   
   ![image](assets/vagrant-level-demo.png)

* This is the first design concept for the map

***        

## Program Design *(Backend Specialist)*
* Non-Standard libraries
    * Pygame 
        * https://docs.google.com/document/d/1H4R6yLL7som1lglyXWZ04RvTp_RvRFCCBn6sqv-82ps/edit#
        * Pygame is a game library for python
* Class Interface Design
    * ![class diagram](assets/milestone3.png)

## Project Structure *(Software Lead)*

The Project is broken down into the following file structure:
* main.py
* bin
    * <all of your python files should go here>
* assets
    * <all of your media, i.e. images, font files, etc, should go here)
* etc
    * <This is a catch all folder for things that are not part of your project, but you want to keep with your project. Your demo video should go here.>

***

## Tasks and Responsibilities *(Software Lead)*

### Software Lead - Paul Ampadu and John Paul Alker

We both worked on the integration of classes and the controller, and collaborated on design features of the project. We intermingled in both front-end and back-end roles, collaborating with each other.

### Front End Specialist - Paul Ampadu

Front-end lead constructed the GUI and controller class for the game. Also aided with classes, specifically the Level, Constants, and Button class. Much of the work was collaborative between front end and back end. 

### Back End Specialist - John Paul Alker

Back-end specialist created Character, Door, Enemy, Saver, and Tiles class, and aided with the construction of the controller. Much of the work was collaborative between front end and back end. 

## Testing *(Software Lead)*
* After all of the code was finished for our final project, we pushed everything that we had to github and ran the program. We went through every feature in the game to see if it worked, recording the results in the ATP. For example, the program was to exit after the exit button on the menu was pressed. To see if this worked, we ran the code and clicked on the exit menu button after the program ran. If it worked, the program was to close. When we did end up getting it to close, we pushed the code to github. 

* Your ATP

| Step                  | Procedure     | Expected Results  | Actual Results |
| ----------------------|:-------------:| -----------------:| -------------- |
|  1  | Run game through terminal  | Menu appears with "Vagrant" title, exit and start screen  |          |
|  2  | Click exit button  | Program exits |                 |
|  3  | Run game through terminal  | Menu appears with "Vagrant" title, exit and start screen  |          |
|  4  | Click start button  | Map appears with character and enemies|                 |
|  5  | Press the left arrow key  | Character moves left |                 |
|  6  | Press the right arrow key  | Character moves right |                 |
|  7  | Press the space key  | Character jumps |                 |
|  8  | Collide character with an enemy | Character either loses a hitpoint or enemy vanishes |                 |
|  9  | Character collides with enemies until it loses all hitpoints or wins game | Character either dies and game over screen appears, or the a game won screen appears, respectively |                 |
|  10  | User exits the program by pressing the exit key | Program closes |                 |
