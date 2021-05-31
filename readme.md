### Kancolle Enemy Slot Calculator

As the number of planes of enemies are hidden from the player, players have to guess the slot sizes of each bomber to gauge how much air power to bring. This tool aims to brute force each individual plane slot size.


## Enemy slot stage 1 calculation

From [wiki](https://en.kancollewiki.net/Arill/Sandbox/Combat/Aerial_Combat), each enemy slot is subject to the following stage 1 loss
```python
loss = int(slot * (0.035 * rand(air_state) + 0.065 * rand(air_state)))
```
where `rand` is a function that returns an integer between 0 and `air_state` inclusive and `air_state` is given by the following table

```
| Enemy Air State | `air_state` |
|-----------------|-------------|
| AS+             | 1           |
| AS              | 3           |
| AP              | 5           |
| AD              | 7           |
| AI              | 10          |
```

Hence, if the player gets AI and the enemy gets AS+, the `rand` function returns two values: 0 or 1. There will be four possible outcomes of `loss`, which may be non-unique. If there are two slots, we add up `loss` per slot and there will be 16 different possible outcomes. Thus, the number of possible cases is given by `(2 * (air_state + 1)) ^ num_slots`.


## Slot Estimation

### Brute Force

To reduce the number of calculations, we limit `air_state` to 1 (so `2 ^ num_slots`) number of cases. From TsunDB, we are able to extract a large number of results for the stage 1 loss per enemy composisiton. We then brute force guesses of the enemy slot sizes and compare them to the actual result.


The limitation of this method is that we need enough samples to cover the entire result space.

### Expectation Value

Instead of hoping that every possibility is returned in the actual data, we calculate the expectation value of the slot loss and compare it to an initial guess. The guess is then optimized for the minimum distance between estimated and actual expectation values.

The limitation of this method is that we have a number of possibilities that are all valid.

TODO: Add constraints (total number of bombers/fighters, constrained sum slot size to max planes)

## Slot Ordering

After we obtain some results of the possible slot sizes, we need to arrange the slots and do a second check to ensure the guess fits the current air power bounds.


## Acknowledgements

This was originally suggested and implemented by Croshadow.
