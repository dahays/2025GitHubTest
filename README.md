# Chapter 5 Team Project - Number Guessing Game
Hays, Paco

## Number Guessing Game Description
This is a menu driven number guessing game.  Two players will guess a number from 1 to the chosen value.
The game ends when someone correctly guesses the number.

### Number Guessing Game Flowchart
```mermaid
graph TD;
  main-->menu;
  main-->get_range;
  main-->player_1;
  main-->player_2;
  main-->game_over;
```

#### Function Diagrams

| `main`    |               |  Hays     |
| ------------------ | ------------- | ------------ |
| `argument:none`    | prompt the user with a menu  |              |
| ``     | calls all functions based on the menu choice  | outputs the winner             |
| ``      | returns nothing | '' |
***
| `function name2`    |               |     author   |
| ------------------ | ------------- | ------------ |
| `name:str`    | takes input from the user for ____  |              |
| `guess:integer`     | calculates ______  | outputs ____             |
| ``      | takes input for name ___ | returns total |
***
