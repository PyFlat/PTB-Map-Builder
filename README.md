<h1 align=center>Map-Builder for <a href="https://github.com/PyFlat-Studios-JR/Plant-The-Bomb">Plant-The-Bomb</a></h1>

# Credits:
- Some textures are from <a href="https://de.freepik.com/">Freepik.com</a>

# Control:
1. Key: **f**
    - Load file
2. Key: **r**
    - White texture (delete)
3. Key: **Ctrl+Z**
    - Undo changes (only working for one change)
4. Key: **Left click and Space**
    - Place a block
5. Key: **Right click**
    - Open enemy window

# Usage:
- Select the texture on the left side 
- Click in the field to place a block
- With the white texture you can delete blocks (orange button or r on the keyboard)
- The block types are explained [here](#blocks)
- With the red button you can delete everything
- With the green button the map will be saved as temp.json in the same folder as the map builder
- With f on the keyboard you can load a map
- Each map must have one player and at least one opponent if you want to be able to win (changes with update 1.3)

# Blocks:
<table>
  <tr>
    <th>Block</th>
    <th>Texture</th>
    <th>Explanation</th>
  </tr>
  <tr>
    <td>Player</td>
    <td><img src="https://github.com/PyFlat-Studios-JR/PTB-Map-Builder/blob/main/textures/00_%20player.png"></img></td>
    <td>The start position of the player</td>
   </tr>
   <tr>
    <td>Endstone</td>
    <td><img src="https://github.com/PyFlat-Studios-JR/PTB-Map-Builder/blob/main/textures/01_endstone.png"></img></td>
    <td>Indestructible walls</td>
   </tr>
   <tr>
    <td>Water</td>
    <td><img src="https://github.com/PyFlat-Studios-JR/PTB-Map-Builder/blob/main/textures/02_water.png"></img></td>
    <td>The player can not run over it but the explosion reaches the other side</td>
   </tr>
   <tr>
    <td>Wall</td>
    <td><img src="https://github.com/PyFlat-Studios-JR/PTB-Map-Builder/blob/main/textures/03_wall.png"></img></td>
    <td>Can be blown up by the player and can drop items</td>
   </tr>
   <tr>
    <td>+Bomb</td>
    <td><img src="https://github.com/PyFlat-Studios-JR/PTB-Map-Builder/blob/main/textures/04_%2Bbomb.png"></img></td>
    <td>Placeable item through which the player can place multiple bombs simultaneously</td>
   </tr>
   <tr>
    <td>+Range</td>
    <td><img src="https://github.com/PyFlat-Studios-JR/PTB-Map-Builder/blob/main/textures/05_%2Bfire.png"></img></td>
    <td>Placeable item through which the player has a longer explosion range</td>
   </tr>
   <tr>
    <td>Ghost</td>
    <td><img src="https://github.com/PyFlat-Studios-JR/PTB-Map-Builder/blob/main/textures/06_%2Bghost.png"></img></td>
    <td>Gives you a random curse</td>
   </tr>
   <tr>
    <td>+Dynamite</td>
    <td><img src="https://github.com/PyFlat-Studios-JR/PTB-Map-Builder/blob/main/textures/07_%2Bdynamit.png"></img></td>
    <td>Placeable item through which the player gets a dynamite in the inventory</td>
   </tr>
   <tr>
    <td>+Time-Bomb</td>
    <td><img src="https://github.com/PyFlat-Studios-JR/PTB-Map-Builder/blob/main/textures/08_%2Btime_bomb.png"></img></td>
    <td>Placeable item through which the player gets a time bomb in the inventory</td>
   </tr>
   <tr>
    <td>+Health</td>
    <td><img src="https://github.com/PyFlat-Studios-JR/PTB-Map-Builder/blob/main/textures/9_%2Bhealth.png"></img></td>
    <td>Placeable item through which the player gets one more life</td>
   </tr>
   <tr>
    <td>Enemy</td>
    <td><img src="https://github.com/PyFlat-Studios-JR/PTB-Map-Builder/blob/main/textures/10_enemy.png"></img></td>
    <td>Attacks the player, with right-click you can choose how many lives he has and if he does damage</td>
   </tr>
   <tr>
    <td>+Sword</td>
    <td><img src="https://github.com/PyFlat-Studios-JR/PTB-Map-Builder/blob/main/textures/11_%2Bsword.png"></img></td>
    <td>Bombs and dynamite do more damage to enemies but also to you</td>
   </tr>
   <tr>
    <td>+Atomic Bomb</td>
    <td><img src="https://github.com/PyFlat-Studios-JR/PTB-Map-Builder/blob/main/textures/12_%2Batomic_bomb.png"></img></td>
    <td>Like Dynamite but bigger</td>
   </tr>
   <tr>
    <td>Shield</td>
    <td><img src="https://github.com/PyFlat-Studios-JR/PTB-Map-Builder/blob/main/textures/13_shield.png"></img></td>
    <td>Your are immune against normal bombs, dynamite and enemy damage</td>
   </tr>
   
</table>