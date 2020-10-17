This is a compilation of mistakes I have made while learning Unreal Engine 4 and how they were fixed.

## General mistakes

### Getting started too late - you'll miss out on free assets

If you don't want to jump in an learn now, fair enough. But at least get an account, download the tool and start collecting the monthly free assets. When you are ready, you should have a nice little collection of useful things to use

### Relying on learning through youtube tutorials only

This stuff is complex and videos are a great way to learn, but dont forget to *frequently* go back to the source documentation, and read it. Especially after you've learn't how to do 'something' that works, go back and read the docs to understand how and why it works. 

### Don't agonize on the best / optimal way to do things too much

It is unlikely you will be deploying your game to a million users any month soon, so dont get distracted by the optimal way of doing things - if it works, that is a good start. Your only job at this stage is to know how you did it, and why it works.

## Blueprint Errors

### How do I know what to cast to? 

Blueprints often need a sequence of casts to get something done - and most of the video tutorials at some stage will bypass the reason they did this, leaving you confused.  You can pause the video and copy verbatum, but the best method is to read the docs and understand what you want to do. eg if you want to pass a variable to an actor, you need [blah]

### Blueprint variables not showing up (Forgetting to compile)

Always compile every blueprint after every change - it takes seconds and will instantly show issues with that blueprint. 


## Landscape errors

### Changing the material makes the screen go black

wait a few seconds / minutes for the PC to catchup
rebuild lighting
check the materail you dragged in (is it a material instance) - and is the colour green [meaning, you CAN drag it into that spot]


## Network / Multiplayer errors

### Not sure how to start with Multiplayer

The Unreal doco is the best start
https://docs.unrealengine.com/en-US/Gameplay/HowTo/Networking/TestMultiplayer/index.html
https://docs.unrealengine.com/en-US/Gameplay/Networking/index.html
UE4 Network Overview = http://cedric-neukirchen.net/Downloads/Compendium/UE4_Network_Compendium_by_Cedric_eXi_Neukirchen.pdf
Understand Gamemodes = https://docs.unrealengine.com/en-US/Gameplay/Framework/GameMode/index.html
How to make your game in multiplayer mode in Unreal Engine 4 https://indiewatch.com/2018/11/28/how-to-make-your-game-in-multiplayer-mode-in-unreal-engine-4/

### Clients connect to a server but have black screens, client works after server closes
When using a dedicated server and clients on different PC's
fixed by
- changing to num players 3
- turn OFF dedicated server
- making sure the gamemode and actors are replicated (all layers - cube, mesh, character)
