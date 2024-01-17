# What this project needs to do

<!-- TOC -->

- [What this project needs to do](#what-this-project-needs-to-do)
    - [Checklist](#checklist)
    - [Binary Communication Table](#binary-communication-table)
    - [Example: Set LED GPIO pin](#example-set-led-gpio-pin)
    - [Example: Get LED GPIO pins](#example-get-led-gpio-pins)

<!-- /TOC -->

## Checklist

-   [ ] Deliver the last motion time (seconds/microseconds since last motion)
-   [ ] Enable/Disable motion sensor
-   [ ] [Set LED GPIO configurations for colors (ex: r, g, b, w)](#example-set-led-gpio-pin)
-   [ ] [Get current LED GPIO configuration]()

## Binary Communication Table

> First byte will be the command and the second byte the data length

|        Command         |                     Description                      |
| :--------------------: | :--------------------------------------------------: |
| [`0x01`](#0x01example) | Set LED GPIO pins in use (ex: rgbw GPIO pins in use) |

<a id="0x01example"></a>

## Example: Set LED GPIO pin 

Binary Example for RGBW stripes:

**Command** "_0x01_" with data of length _0x04_ (4)  
**Data**:

-   _0x00_ (gp pin nr. 0)
-   _0x01_ (gp pin nr. 1)
-   _0x02_ (gp pin nr. 2)
-   _0x03_ (gp pin nr. 3)

```python
[0x01, 0x04, 0x00, 0x01, 0x02, 0x03]
```

## Example: Get LED GPIO pins

@TODO: ...