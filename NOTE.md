# What this project needs to do

- [What this project needs to do](#what-this-project-needs-to-do)
    - [Binary Communication Table](#binary-communication-table)
        - [todo](#todo)
    - [Example: Get the current LED/GPIO configuration for colors (ex: r, g, b, w)](#0x01example)
    - [Example: Set LED/GPIO configurations for colors (ex: r, g, b, w)](#0x02example)
    - [Example: Set motion sensor GPIO pin](#0x03example)
    - [Example: Get motion sensor GPIO pin](#0x04example)
    - [Example: Set server address (ex.: "http://rpi-server:50833)"](#0x05example)
    - [Example: Get server address](#0x06example)
    - [Example: Set PWM range](#0x07example)

## Binary Communication Table

> First byte will be the command and the second byte the data length

**config** commands in range from `0x01` - `0x20`  
**info** commands in range from `0x21` - `0x40`  
**led** commands in range from `0x41` - `0x60`  
**motion** commands in range from `0x61` - `0x80`  

|        Command                | Description                                                        |
| :---------------------------- | :----------------------------------------------------------------- |
| config [`0x01`](#0x01example) | Get the current LED/GPIO configuration for colors (ex: r, g, b, w) |
| config [`0x02`](#0x02example) | Set LED/GPIO configurations for colors (ex: r, g, b, w)            |
| config [`0x03`](#0x03example) | Set motion sensor GPIO pin                                         |
| config [`0x04`](#0x04example) | Get motion sensor GPIO pin                                         |
| config [`0x05`](#0x05example) | Set server address (ex.: "http://rpi-server:50833)"                |
| config [`0x06`](#0x06example) | Get server address                                                 |
| config [`0x07`](#0x07example) | Set PWM range                                                      |

### todo:
- **info**: get picow temp. (`0x21`)
- **info**: get picow disk-usage (`0x22`)
- **info**: get version (ex: v1.0.0) (`0x23`)
- **led**: set GPIO LED pins duty (pwm-range) (`0x41`)
- **led**: get GPIO LED pins duty (pwm-range) (`0x42`)
- **motion**: get motion sensor data (`0x61`)

<a id="0x01example"></a>

## Example: Get the current LED/GPIO configuration for colors (ex: r, g, b, w)

**Command** `0x01` with data of length `0x00` (0)  
**Data**:

```python
[0x01, 0x00]
```

<a id="0x02example"></a>

## Example: Set LED/GPIO configurations for colors (ex: r, g, b, w)

**Command** `0x02` with data of length `0x04` (4)  
**Data**:

-   _0x00_ (gp pin nr. 0)
-   _0x01_ (gp pin nr. 1)
-   _0x02_ (gp pin nr. 2)
-   _0x03_ (gp pin nr. 3)

```python
[0x02, 0x04, 0x00, 0x01, 0x02, 0x03]
```

<a id="0x03example"></a>

## Example: Set motion sensor GPIO pin

@todo: ...

<a id="0x04example"></a>

## Example: Get motion sensor GPIO pin

@todo: ...

<a id="0x05example"></a>

## Example: Set server address (ex.: "http://rpi-server:50833)"

@todo: ...

<a id="0x06example"></a>

## Example: Get server address

@todo: ...

<a id="0x07example"></a>

## Example: Set PWM range

@todo: ...
