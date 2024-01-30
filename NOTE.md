# What this project needs to do

- [What this project needs to do](#what-this-project-needs-to-do)
    - [Checklist](#checklist)
    - [Binary Communication Table](#binary-communication-table)
    - [Example: Get LED GPIO pins](#0x01example)
    - [Example: Set LED GPIO pins](#0x02example)

## Checklist

-   [ ] Deliver the last motion time (seconds/microseconds since last motion)
-   [ ] Enable/Disable motion sensor
-   [ ] [Get the current LED/GPIO configuration for colors (ex: r, g, b, w)](#0x01example)
-   [ ] [Set LED/GPIO configurations for colors (ex: r, g, b, w)](#0x02example)

## Binary Communication Table

> First byte will be the command and the second byte the data length

**config** commands in range from `0x01` - `0x20`  
**info** commands in range from `0x21` - `0x40`  
**led** commands in range from `0x41` - `0x60`  
**motion** commands in range from `0x61` - `0x80`  

### todo:
- **config**: set LED GPIO pin (`0x01`)
- **config**: get LED GPIO pin (`0x02`)
- **config**: set motion sensor GPIO pin (`0x03`)
- **config**: get motion sensor GPIO pin (`0x04`)
- **config**: set server (`0x05`)
- **config**: get server (`0x06`)
- **config**: set PWM range (min-max, ex: 0-100, 0-255) (`0x07`)
- **info**: get picow temp. (`0x21`)
- **info**: get picow disk-usage (`0x22`)
- **info**: get version (ex: v1.0.0) (`0x23`)
- **led**: set GPIO LED pins duty (pwm-range) (`0x41`)
- **led**: get GPIO LED pins duty (pwm-range) (`0x42`)
- **motion**: ...

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
