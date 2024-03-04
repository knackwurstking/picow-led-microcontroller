<!-- vscode-markdown-toc -->

- [Binary Communication Table](#BinaryCommunicationTable)
- [Example: Set GPIO configurations for colors (ex: r, g, b, w)](#Example:SetGPIOconfigurationsforcolorsex:rgbw)
- [Example: Get the current GPIO configuration for colors (ex: r, g, b, w)](#Example:GetthecurrentGPIOconfigurationforcolorsex:rgbw)
- [Example: Set motion sensor GPIO pin](#Example:SetmotionsensorGPIOpin)
- [Example: Get motion sensor GPIO pin](#Example:GetmotionsensorGPIOpin)
- [Example: Set motion sensor timeout](#Example:Setmotionsensortimeout)
- [Example: Get motion sensor timeout](#Example:Getmotionsensortimeout)
- [Example: Set PWM range](#Example:SetPWMrange)
- [Example: Get PWM range](#Example:GetPWMrange)
- [Example: Get picow temp](#Example:Getpicowtemp)
- [Example: Get picow disk-usage](#Example:Getpicowdisk-usage)
- [Example: Get version](#Example:Getversion)
- [Example: Set GPIO pins duty (pwm-range)](#Example:SetGPIOpinsdutypwm-range)
- [Example: Get GPIO pins duty (pwm-range)](#Example:GetGPIOpinsdutypwm-range)
- [Example: Get motion sensor data](#Example:Getmotionsensordata)

<!-- vscode-markdown-toc-config
	numbering=false
	autoSave=true
	/vscode-markdown-toc-config -->
<!-- /vscode-markdown-toc --># What this project needs to do

# TODO: Missing b"\\n" End-Byte information

## <a name='BinaryCommunicationTable'></a>Binary Communication Table

> First byte will be the command, and the second byte the data length

**config** commands in range from `0x01` -- `0x20`\
**info** commands in range from `0x21` -- `0x40`\
**led** commands in range from `0x41` -- `0x60`\
**motion** commands in range from `0x61` -- `0x80`

|                                                                  Command | Data Type       | Description                                                    |
| -----------------------------------------------------------------------: | :-------------- | :------------------------------------------------------------- |
|          config [`0x01`](#Example:SetGPIOconfigurationsforcolorsex:rgbw) | decimal...      | Set GPIO configurations for colors (ex: r, g, b, w)            |
| config [`0x02`](#Example:GetthecurrentGPIOconfigurationforcolorsex:rgbw) | decimal...      | Get the current GPIO configuration for colors (ex: r, g, b, w) |
|                         config [`0x03`](#Example:SetmotionsensorGPIOpin) | decimal         | Set motion sensor GPIO pin                                     |
|                         config [`0x04`](#Example:SetmotionsensorGPIOpin) | decimal         | Get motion sensor GPIO pin                                     |
|                         config [`0x05`](#Example:Setmotionsensortimeout) | string          | Set motion sensor timeout                                      |
|                         config [`0x06`](#Example:Getmotionsensortimeout) | string          | Get motion sensor timeout                                      |
|                                    config [`0x07`](#Example:SetPWMrange) | decimal         | Set PWM range                                                  |
|                                    config [`0x08`](#Example:GetPWMrange) | decimal         | Get PWM range                                                  |
|                                     info [`0x21`](#Example:Getpicowtemp) | float as string | Get picow temp.                                                |
|                               info [`0x22`](#Example:Getpicowdisk-usage) | string          | Get picow disk-usage                                           |
|                                       info [`0x23`](#Example:Getversion) | string          | Get version                                                    |
|                          led [`0x41`](#Example:SetGPIOpinsdutypwm-range) | decimal...      | Set GPIO pins duty (pwm-range)                                 |
|                          led [`0x42`](#Example:GetGPIOpinsdutypwm-range) | decimal...      | Get GPIO pins duty (pwm-range)                                 |
|                            motion [`0x61`](#Example:Getmotionsensordata) | string          | Get motion sensor data                                         |

## <a name='Example:SetGPIOconfigurationsforcolorsex:rgbw'></a>Example: Set GPIO configurations for colors (ex: r, g, b, w)

> No server response

1. <u>**Data (Request)**</u>

   - **group**: config `0x01`
   - **data**: GP pins 0..3
   - **data length**: `0x04` (_dynamic_)
   - **data type**: decimal...

   ```python
   [0x01, 0x04, 0x00, 0x01, 0x02, 0x03]
   ```

## <a name='Example:GetthecurrentGPIOconfigurationforcolorsex:rgbw'></a>Example: Get the current GPIO configuration for colors (ex: r, g, b, w)

1. <u>**Data (Request)**</u>

   - **group**: config `0x02`

   ```python
   [0x02, 0x00]
   ```

1. <u>**Data (Response)**</u>

   - **group**: config `0x02`
   - **data**: GP pins 0..3
   - **data length**: `0x04` (_dynamic_)
   - **data type**: decimal...

   ```python
   [0x02, 0x04, 0x00, 0x01, 0x02, 0x03]
   ```

## <a name='Example:SetmotionsensorGPIOpin'></a>Example: Set motion sensor GPIO pin

> No server response

1. <u>**Data (Request)**</u>

   - **group**: config `0x03`
   - **data**: GP13 (enable only)
   - **data length**: `0x01` (1) for enable, `0x00` for disable (_fixed_)
   - **data type**: decimal

   ```python
   [0x03, 0x01, 0x0d]
   ```

## <a name='Example:GetmotionsensorGPIOpin'></a>Example: Get motion sensor GPIO pin

1. <u>**Data (Request)**</u>

   - **group**: config `0x04`

   ```python
   [0x04, 0x00]
   ```

1. <u>**Data (Response)**</u>

   - **group**: config `0x04`
   - **data**: GP13
   - **data length**: `0x01` (1) (_fixed_)
   - **data type**: decimal

   ```python
   [0x04, 0x01, 0x0d]
   ```

## <a name='Example:Setmotionsensortimeout'></a>Example: Set motion sensor timeout

The motion sensor timeout will reset the value back to 0 if a specific timeout
(milliseconds) is reached.

> No server response

1. <u>**Data (Request)**</u>

   - **group**: config `0x05`
   - **data**: 60000 (60 seconds)
   - **data length**: `0x05` (5) (_dynamic_)
   - **data type**: string

   ```python
   [
       0x05,
       0x05,
       0x06, 0x00, 0x00, 0x00, 0x00, # 60000
   ]
   ```

## <a name='Example:Getmotionsensortimeout'></a>Example: Get motion sensor timeout

Returns the motion sensor timeout in milliseconds.

1. <u>**Data (Request)**</u>

   - **group**: config `0x06`

   ```python
   [0x06, 0x00]
   ```

1. <u>**Data (Response)**</u>

   - **group**: config `0x06`
   - **data**: 60000 (60 seconds)
   - **data length**: `0x05` (5) (_dynamic_)
   - **data type**: string

   ```python
   [
       0x06,
       0x05,
       0x06, 0x00, 0x00, 0x00, 0x00, # 60000
   ]
   ```

## <a name='Example:SetPWMrange'></a>Example: Set PWM range

> No server response

1. <u>**Data (Request)**</u>

   - **group**: config `0x07`
   - **data**: pwm-range 0-100
   - **data length**: `0x02` (2) (_fixed_)
   - **data type**: decimal

   ```python
   [0x07, 0x02, 0x00, 0x64]
   ```

## <a name='Example:GetPWMrange'></a>Example: Get PWM range

1. <u>**Data (Request)**</u>

   - **group**: config `0x08`

   ```python
   [0x08, 0x00]
   ```

1. <u>**Data (Response)**</u>

   - **group**: config `0x08`
   - **data**: pwm-range 0-100
   - **data length**: `0x02` (2) (_fixed_)
   - **data type**: decimal

   ```python
   [0x08, 0x02, 0x00, 0x64]
   ```

## <a name='Example:Getpicowtemp'></a>Example: Get picow temp

1. <u>**Data (Request)**</u>

   - **group**: info `0x21`

   ```python
   [0x21, 0x00]
   ```

1. <u>**Data (Response)**</u>

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

## <a name='Example:Getpicowdisk-usage'></a>Example: Get picow disk-usage

1. <u>**Data (Request)**</u>

   - **group**: info `0x22`

   ```python
   [0x22, 0x00]
   ```

1. <u>**Data (Response)**</u>

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

## <a name='Example:Getversion'></a>Example: Get version

1. <u>**Data (Request)**</u>

   - **group**: info `0x23`

   ```python
   [0x23, 0x00]
   ```

1. <u>**Data (Response)**</u>

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

## <a name='Example:SetGPIOpinsdutypwm-range'></a>Example: Set GPIO pins duty (pwm-range)

> No server response

1. <u>**Data (Request)**</u>

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

## <a name='Example:GetGPIOpinsdutypwm-range'></a>Example: Get GPIO pins duty (pwm-range)

1. <u>**Data (Request)**</u>

   - **group**: led `0x42`

   ```python
   [0x42, 0x00]
   ```

1. <u>**Data (Response)**</u>

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

## <a name='Example:Getmotionsensordata'></a>Example: Get motion sensor data

A value of 0 means no motion detected, or timeout reached since the last activation

1. <u>**Data (Request)**</u>

   - **group**: motion `0x61`

   ```python
   [0x61, 0x00]
   ```

1. <u>**Data (Response)**</u>

   - **group**: motion `0x61`
   - **data**: 5452 -- time in ms from last motion detect event
   - **data length**: `0x04` (4), (_dynamic_)
   - **data type**: string

   ```python
   [
       0x61,
       0x04,
       0x35, 0x34, 0x35, 0x32 # 5452
   ]
   ```
