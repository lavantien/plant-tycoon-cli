# Plant Tycoon CLI

## Game Mechanics

- Players are able to buy seeds and sell plants
- Each plant will have an internal growth rate and DNA
- Mature plant will produce pollen and seeds
- Use pollen on different species to mutate the seeds
- Growing is done automatically

## Technical Decisions

- Text based or TUI?
- Procedure generated?
- Add tools, soils, insects, decorations, leaderboards, etc.?

## Design Document

<details>
    <summary>expand</summary>

### Game

- fixed maturity breakpoint

### A Plant

- genes: name, growthRate, price, seedType, bodyType, flowerType, fruitType, leafType, height, specialType, health, waterLevel, age

### Storage

- stores seeds based on seedType

</details>
