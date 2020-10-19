build_a_landscape

Copy of text from blog article published at https://www.lifepim.com/blog/6534_Steps_to_build_a_world_with_Unreal_Engine_4

The article has the steps needed to build a beautiful looking world using Unreal engine, using prebuilt assets (character model, trees, etc)

### High Level Steps

Setup Unreal Engine and download the assets you need
Make the landscape
Paint the ground
Add trees and flowers
Setup lighting by dropping in a nice sky
Add some animals
Drop in sounds
[img]UE4_game_sanct_shed_side2.PNG[/img]
     

### Setup Unreal Engine and download the assets you need

- new project using "3rd person" blueprint template, called "sanctuary"
- ignore the start zone - go to File > New > New Level. Choose "Default" not empty level 
- name the level as "lvl_sanct"
- select starting plate and delete it so there is nothing there 
- save the project and exit Unreal Engine
- Start the Epic Games Launcher and add the following projects from Library to your project 'sanctuary' 

Procedural Nature Pack Vol1 
GoodSky 
Fantasy and Medieval Architecture 
ANIMAL VARIETY PACK 


- Restart Unreal Engine and load the project "sanctuary"
- when Unreal opens the project it shows the original sample level. In the Content Browser, double click "lvl_sanct" from the root of content to show the level 



### Build the layout of the landscape

- click Landscape under top left MODES panel to bring up the green mesh in landscape creation (dont click create yet) 
- Pick a material for the landscape: Content Browser > Procedural Nature > search for grass_dirt_cobblestone THEN drag THIS to the LHS Panel landscape material 
- Click Create and after a second, you see a black screen (dont panic)

The landscape is showing black because we chose a composite material (grass, dirt, cobblestone, puddles) and this step shows how to expose those layers for painting.
- on the Modes panel, click Paint - you should see the target layers of the composite material
- there should be 4 layers for this one: click + sign, assign to "weighted layer", save anywhere as default name
- repeat for the remaining 3 years
Wait, 5 minutes for compilers to shade - then PAINT EACH LAYER 


SEE Author youtube for procedural generation
https://www.youtube.com/watch?v=rhDexjv-Tg8

NOTE - sometimes the layer textures will disappear and you wont be able to paint. Just click save and wait a second and it should return. 


- make hills with the sculpt tool
- Paint the ground
- choose the layer to paint (stone, dirt, grass, puddles)
- left mouse click to paint (change the brush size first to suit)


### Trees and flowers
In the animations / mesh subfolders of the projects you should be able to add trees, rocks

You can also "paint" foliage like flowers and grass onto the land 

go to foliage tool under landscape
drag in a material like grass or leaves and drop in onto the foliage area
left mouse click on your land to paint flowers
You can adjust density and falloff of the paint tool


### Lighting
Lighting is tricky and there are many resources on how to do it. For this exercise, we will use an add-on that looks quite nice

- Go to the Content browser and drag the BP_Goodsky icon from  

   Content > Goodsky > Blueprint

 onto your sky in the main window (changes to night sky)

- Play with settings of BP_GoodSky  in RHS Details pane (Sky Effect, etc)

Done - rebuild lighting and your world should look a lot nicer.

### Animals

- go to your content browser and the Animals folder
- in meshes, drag in an IDLE animation of an animal

### Adding sounds

When you add ambient sounds, first drag in an "Ambient Sound" from the All Classes in place mode on the LHS Panel
Then, select the sound and pick a WAV file for it - you need to pick the Sound Cue, NOT the sound wave.

To make the sound trigger, when player walks near it , you tick the Enable Volume Attenuation and then modify the parameters 
>    Inner Radius = 1300
>    Falloff Distance = 1800 (or play with the parameters)


IMPORTING SOUNDS

1. download the sound you want (MP3/WAV), or record 
2. Save to your project Content folder, reopen Unreal so it imports the asset
3. You need to make a Cue for the wav file and choose "Create Cue"
  (you can also use blueprints to make a cue [drag in output, drag in media player, link])



### References

UE4 Materials Notes = https://docs.unrealengine.com/en-US/Resources/ContentExamples/Materials/index.html

