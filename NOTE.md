

# What this project needs to do

<!-- TOC -->

- [What this project needs to do](#what-this-project-needs-to-do)
    - [Checklist](#checklist)
    - [Binary Communication Table](#binary-communication-table)
    - [Example: Set LED GPIO pins](#example-set-led-gpio-pins)

<!-- /TOC -->

## Checklist

- [ ] Deliver the last motion time (seconds/microseconds since last motion)
- [ ] Enable/Disable motion sensor
- [ ] [Set LED GPIO configurations for colors (ex: r, g, b, w)](#example-set-led-gpio-pins)
- [ ] Get current LED GPIO configuration

## Binary Communication Table

> First byte will be the command and the second byte the data length  

| Command | Description |
| :-----: | :---------: |
| [`0x01`](#0x01example) | Set LED GPIO pins in use (ex: rgbw GPIO pins in use) |

<a id="0x01example"></a>

## Example: Set LED GPIO pins

Binary Example for RGBW stripes:  

**Command** "*0x01*" with data of length *0x04* (4)  
**Data**:  
* *0x00* (gp pin nr. 0)
* *0x01* (gp pin nr. 1)
* *0x02* (gp pin nr. 2)
* *0x03* (gp pin nr. 3)  

```python
[0x01, 0x04, 0x00, 0x01, 0x02, 0x03]
```
