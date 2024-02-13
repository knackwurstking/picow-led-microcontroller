# What this project needs to do

- [What this project needs to do](#what-this-project-needs-to-do)
    - [Binary Communication Table](#binary-communication-table)
    - [Example: Set LED/GPIO configurations for colors (ex: r, g, b, w)](#0x01example)
    - [Example: Get the current LED/GPIO configuration for colors (ex: r, g, b, w)](#0x02example)
    - [Example: Set motion sensor GPIO pin](#0x03example)
    - [Example: Get motion sensor GPIO pin](#0x04example)
    - [Example: Set server address (ex.: "http://rpi-server:50833)"](#0x05example)
    - [Example: Get server address](#0x06example)
    - [Example: Set PWM range](#0x07example)
    - [Example: Get picow temp.](#0x21example)
    - [Example: Get picow disk-usage](#0x22example)
    - [Example: Get version](#0x23example)
    - [Example: Set GPIO LED pins duty (pwm-range)](#0x41example)
    - [Example: Get GPIO LED pins duty (pwm-range)](#0x42example)
    - [Example: Get motion sensor data](#0x61example)

## Binary Communication Table

> First byte will be the command and the second byte the data length

**config** commands in range from `0x01` -- `0x20`  
**info** commands in range from `0x21` -- `0x40`  
**led** commands in range from `0x41` -- `0x60`  
**motion** commands in range from `0x61` -- `0x80`  

|        Command                | Data Type | Description |
| ----------------------------: | :-------- | :---------- |
| config [`0x01`](#0x01example) | decimal... | Set LED/GPIO configurations for colors (ex: r, g, b, w) |
| config [`0x02`](#0x02example) | decimal... | Get the current LED/GPIO configuration for colors (ex: r, g, b, w) |
| config [`0x03`](#0x03example) | decimal | Set motion sensor GPIO pin |
| config [`0x04`](#0x04example) | decimal | Get motion sensor GPIO pin |
| config [`0x05`](#0x05example) | string | Set server address (ex.: "http://rpi-server:50833)" |
| config [`0x06`](#0x06example) | string | Get server address |
| config [`0x07`](#0x07example) | decimal | Set PWM range |
| info   [`0x21`](#0x21example) | float as string | Get picow temp. |
| info   [`0x22`](#0x22example) | string | Get picow disk-usage |
| info   [`0x23`](#0x23example) | string | Get version |
| led    [`0x41`](#0x41example) | decimal... | Set GPIO LED pins duty (pwm-range) |
| led    [`0x42`](#0x42example) | decimal... | Get GPIO LED pins duty (pwm-range) |
| motion [`0x61`](#0x61example) | string | Get motion sensor data |

<a id="0x01example"></a>

## Example: Set LED/GPIO configurations for colors (ex: r, g, b, w)

> No server response

### Data (Request)

- **group**: config `0x01`
- **data**: GP pins 0..3
- **data length**: `0x04` (_dynamic_)
- **data type**: decimal...

```python
[0x01, 0x04, 0x00, 0x01, 0x02, 0x03]
```

<a id="0x02example"></a>

## Example: Get the current LED/GPIO configuration for colors (ex: r, g, b, w)

### Data (Request)

- **group**: config `0x02`

```python
[0x02, 0x00]
```

### Data (Response)

- **group**: config `0x02`
- **data**: GP pins 0..3
- **data length**: `0x04` (_dynamic_)
- **data type**: decimal...

```python
[0x02, 0x04, 0x00, 0x01, 0x02, 0x03]
```

<a id="0x03example"></a>

## Example: Set motion sensor GPIO pin

> No server response

### Data (Request)

- **group**: config `0x03`
- **data**: GP13 (enable only)
- **data length**: `0x01` (1) for enable, `0x00` for disable (_fixed_)
- **data type**: decimal

```python
[0x03, 0x01, 0x0d]
```

<a id="0x04example"></a>

## Example: Get motion sensor GPIO pin

### Data (Request)

- **group**: config `0x04`

```python
[0x04, 0x00]
```

### Data (Response)

- **group**: config `0x04`
- **data**: GP13
- **data length**: `0x01` (1) (_fixed_)
- **data type**: decimal

```python
[0x04, 0x01, 0x0d]
```

<a id="0x05example"></a>

## Example: Set server address (ex.: "http://rpi-server:50833)"

> No server response

### Data (Request)

- **group**: config `0x05`
- **data**: "http://192.168.178.21:50833"
- **data length**: `0x1b` (27) (_dynamic_)
- **data type**: string

```python
[
    0x05,
    0x1b,
    0x68, 0x74, 0x74, 0x70, 0x3a, 0x2f, 0x2f, # http://
    0x31, 0x39, 0x32, 0x2e,                   # 192.
    0x31, 0x36, 0x38, 0x2e,                   # 168.
    0x31, 0x37, 0x38, 0x2e,                   # 178.
    0x32, 0x31, 0x3a,                         # 21:
    0x35, 0x30, 0x38, 0x33, 0x33              # 50833
]
```

<a id="0x06example"></a>

## Example: Get server address

### Data (Request)

- **group**: config `0x06`

```python
[0x06, 0x00]
```

### Data (Response)

- **group**: config `0x06`
- **data**: "http://192.168.178.21:50833"
- **data length**: `0x1b` (27) (_dynamic_)
- **data type**: string

```python
[
    0x06,
    0x1b,
    0x68, 0x74, 0x74, 0x70, 0x3a, 0x2f, 0x2f, # http://
    0x31, 0x39, 0x32, 0x2e,                   # 192.
    0x31, 0x36, 0x38, 0x2e,                   # 168.
    0x31, 0x37, 0x38, 0x2e,                   # 178.
    0x32, 0x31, 0x3a,                         # 21:
    0x35, 0x30, 0x38, 0x33, 0x33              # 50833
]
```

<a id="0x07example"></a>

## Example: Set PWM range

> No server response

### Data (Request)

- **group**: config `0x07`
- **data**: pwm-range 0-100
- **data length**: `0x02` (2) (_fixed_)
- **data type**: decimal

```python
[0x07, 0x02, 0x00, 0x64]
```

<a id="0x21example"></a>

## Example: Get picow temp.

### Data (Request)

- **group**: info `0x21`

```python
[0x21, 0x00]
```

### Data (Response)

- **group**: info `0x21`
- **data**: 22.36296 (Celsius)
- **data length**: `0x08` (8), (_dynamic_)
- **data type**: float as string

```python
[
    0x21,
    0x08,
    0x32, 0x32, 0x2e,            # 22.
    0x33, 0x36, 0x32, 0x39, 0x36 # 36296
]
```

<a id="0x22example"></a>

## Example: Get picow disk-usage

### Data (Request)

- **group**: info `0x22`

```python
[0x22, 0x00]
```

### Data (Response)

- **group**: info `0x22`
- **data**: "471040 397312" ("\<used> \<free>") (space in bytes)
- **data length**: `0x0d` (13), (_dynamic_)
- **data type**: string

```python
[
    0x22,
    0x0d,
    0x34, 0x37, 0x31, 0x30, 0x34, 0x30, # 471040
    0x20,                               # space
    0x33, 0x39, 0x37, 0x33, 0x31, 0x32  # 397312
]
```

<a id="0x23example"></a>

## Example: Get version

### Data (Request)

- **group**: info `0x23`

```python
[0x23, 0x00]
```

### Data (Response)

- **group**: info `0x23`
- **data**: "1.0.0"
- **data length**: `0x05` (5), (_dynamic_)
- **data type**: string

```python
[
    0x22,
    0x05,
    0x31, # 1
    0x2e, # .
    0x30, # 0
    0x2e, # .
    0x30  # 0
]
```

<a id="0x41example"></a>

## Example: Set GPIO LED pins duty (pwm-range)

> No server response

### Data (Request)

- **group**: led `0x41`
- **data**: min-max number per pin in order based on [pwm-range configuration](#0x07example) and [LED/GPIO configuration](#0x01example)
- **data length**: `0x04` (4), (_dynamic_)
- **data type**: decimal...

```python
[
    0x41,
    0x04,
    0x64, # 100
    0x64, # 100
    0x64, # 100
    0x64, # 100
]
```

<a id="0x42example"></a>

## Example: Get GPIO LED pins duty (pwm-range)

### Data (Request)

- **group**: led `0x42`

```python
[0x42, 0x00]
```

### Data (Response)

- **group**: led `0x42`
- **data**: min-max number per pin in order based on [pwm-range configuration](#0x07example) and [LED/GPIO configuration](#0x01example)
- **data length**: `0x04` (4), (_dynamic_)
- **data type**: decimal...

```python
[
    0x42,
    0x04,
    0x64, # 100
    0x64, # 100
    0x64, # 100
    0x64, # 100
]
```

<a id="0x61example"></a>

## Example: Get motion sensor data

### Data (Request)

- **group**: motion `0x61`

```python
[0x61, 0x00]
```

### Data (Response)

- **group**: motion `0x61`
- **data**: 5452 - time in ms from last motion detect event
- **data length**: `0x04` (4), (_dynamic_)
- **data type**: string

```python
[
    0x61,
    0x04,
    0x35, 0x34, 0x35, 0x32 # 5452
]
```
