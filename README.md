# CS110 Project Proposal
# Vagabond Game
## CS 110 Final Project
### Fall 2021 Section A0
### [Assignment Description](https://docs.google.com/document/d/1H4R6yLL7som1lglyXWZ04RvTp_RvRFCCBn6sqv-82ps/edit#)

[project description](https://docs.google.com/document/d/1H4R6yLL7som1lglyXWZ04RvTp_RvRFCCBn6sqv-82ps/edit#)

[link to demo presentation slides](https://docs.google.com/presentation/d/1oAw3T_M4SXxPpZiUHrMQwgNUH4la8D80np7toceEl-4/edit?usp=sharing)

### Team: Ampalker
#### John Paul Alker, Paul Ampadu

***

## Project Description *(Software Lead)*
Our project is of a game that has an enemy ghost move randomly on the screen. The main character has unlimited double jumps (to hit the ghosts) on the screen. There is a 3/5 chance that there will be a successful hit. If he does successfully hit the ghost, a dog fact appears on the screen as a reward. If he does not, "Miss!" will appear and there will be no dog fact.

***    

## User Interface Design *(Front End Specialist)*

![image](https://user-images.githubusercontent.com/89813338/140586605-9adc09ef-7bd7-4390-bd09-4385bbdeb792.png)

* This is the start menu
   
   
   ![image](assets/vagrant-level-demo.png)

* This is the first design concept for the map


* This is the final game GUI


   ![image](assets/guiguiguigui.png)

***        

## Program Design *(Backend Specialist)*
* Non-Standard libraries
    * Pygame 
        * https://docs.google.com/document/d/1H4R6yLL7som1lglyXWZ04RvTp_RvRFCCBn6sqv-82ps/edit#
        * Pygame is a game library for python
* Class Interface Design

    * This is the older class interface
    * ![class diagram](assets/milestone3.png)


    * This is the newer class interface
    ![image](https://user-images.githubusercontent.com/89813338/145519100-6bd096a7-66b5-44e9-9cc8-1fb9670e7d5b.png)

## Project Structure *(Software Lead)*

The Project is broken down into the following file structure:
* main.py
* bin
    * Button.py
    * Character.py
    * Constants.py
    * Enemy.py
    * Tiles.py
    * controller.py
    
* assets
   * Menu.png
   * Vagabond.png
   * Vagrant Exit.png
   * Vagrant Start.png
   * Vagrant Title PNG.png
   * Vagrant Title.png
   * class_diagram.jpg
   * cobbleSnowBedrock-PNG.png
   * cobbleSnowBedrock.psd.png
   * cobbleSnowCornerEdge-PNG.png
   * cobbleSnowMainRoad-PNG.png
   * ghost enemy.jpg
   * ghost.png
   * guiguiguigui.png
   * level sketch.png
   * milestone3.png
   * vagrant-level-demo.png
   
   
   
* etc
    * demo.mp4

***

## Tasks and Responsibilities *(Software Lead)*

### Software Lead - Paul Ampadu and John Paul Alker

We both worked on the integration of classes and the controller, and collaborated on design features of the project. We intermingled in both front-end and back-end roles, collaborating with each other.

### Front End Specialist - Paul Ampadu

Front-end lead constructed the GUI and controller class for the game. Also aided with classes, specifically the Button class. Much of the work was collaborative between front end and back end. 

### Back End Specialist - John Paul Alker

Back-end specialist created Character, Enemy, and Tiles class, and aided with the construction of the controller. Back-end also implemented a network based API to fulfill data permanence. Much of the work was collaborative between front end and back end. 

## Testing *(Software Lead)*
* After all of the code was finished for our final project, we pushed everything that we had to github and ran the program. We went through every feature in the game to see if it worked, recording the results in the ATP. For example, the program was to exit after the exit button on the menu was pressed. To see if this worked, we ran the code and clicked on the exit menu button after the program ran. If it worked, the program was to close. When we did end up getting it to close, we pushed the code to github. 

 Your ATP

| Step                  | Procedure     | Expected Results  | Actual Results |
| ----------------------|:-------------:| -----------------:| -------------- |
|  1  | Run game through terminal  | Menu appears with "Vagrant" title, exit and start screen  |     correct     |
|  2  | Click exit button  | Program exits |         correct        |
|  3  | Run game through terminal  | Menu appears with "Vagrant" title, exit and start screen  |     correct     |
|  4  | Click start button  | Map appears with character and enemies|         correct        |
|  5  | Press the a key  | Character moves left |         correct        |
|  6  | Press the d key  | Character moves right |        correct         |
|  7  | Press the space key  | Character jumps |         correct        |
|  8  | Press the space key many times | Character jumps many times (double jump feature) |        correct         |
|  9  | Collide character with an enemy | A "Hit!" and random dog fact will appear, or or a "Miss!" will appear |        correct         |
|  11  | User exits the program by pressing the top right exit button | Program closes |        correct         |
