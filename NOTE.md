# What this project needs to do

<!-- TOC -->

- [What this project needs to do](#what-this-project-needs-to-do)
    - [Checklist](#checklist)
    - [Binary Communication Table](#binary-communication-table)
    - [Example: Get LED GPIO pins](#example-get-led-gpio-pins)
    - [Example: Set LED GPIO pins](#example-set-led-gpio-pins)

<!-- /TOC -->

## Checklist

-   [ ] Deliver the last motion time (seconds/microseconds since last motion)
-   [ ] Enable/Disable motion sensor
-   [ ] [Get the current LED/GPIO configuration for colors (ex: r, g, b, w)](#example-get-led-gpio-pins)
-   [ ] [Set LED/GPIO configurations for colors (ex: r, g, b, w)](#example-set-led-gpio-pins)

## Binary Communication Table

> First byte will be the command and the second byte the data length

|        Command         | Description                                                        |
| :--------------------: | :----------------------------------------------------------------- |
| [`0x01`](#0x01example) | Get the current LED/GPIO configuration for colors (ex: r, g, b, w) |
| [`0x02`](#0x02example) | Set LED/GPIO configurations for colors (ex: r, g, b, w)            |

<a id="0x01example"></a>

## Example: Get LED GPIO pins

**Command** `0x01` with data of length `0x00` (0)  
**Data**:

```python
[0x01, 0x00]
```

<a id="0x02example"></a>

## Example: Set LED GPIO pins

**Command** `0x02` with data of length `0x04` (4)  
**Data**:

-   _0x00_ (gp pin nr. 0)
-   _0x01_ (gp pin nr. 1)
-   _0x02_ (gp pin nr. 2)
-   _0x03_ (gp pin nr. 3)

```python
[0x02, 0x04, 0x00, 0x01, 0x02, 0x03]
```
