# NOTE Communication

<!-- vscode-markdown-toc -->

- [Commands Overview](#CommandsOverview)
- [JSON (typescript) interface](#JSONtypescriptinterface)
- [JSON Example: Set/Get GPIO pins for LEDs](#JSONExample:SetGetGPIOpinsforLEDs)
- [Listen for motion sensor events](#Listenformotionsensorevents)

<!-- vscode-markdown-toc-config
	numbering=false
	autoSave=true
	/vscode-markdown-toc-config -->
<!-- /vscode-markdown-toc -->

## <a name='CommandsOverview'></a>Commands Overview

- `config`
  - `set`
    - `led <gp:nr> ...`: [Set GPIO configuration for LEDs (ex.: rgbw)](#SetGPIOpinsforLEDs)
    - `motion <gp:nr>`: Set motion sensor pin
    - `motion-timeout <milliseconds:nr>`: Set motion sensor timeout value
    - `pwm-range <min:nr> <max:nr>`: Set PWM range
  - `get`
    - `led`: [Get GPIO configuration for LEDs (ex.: rgbw)](#GetGPIOpinsforLEDs)
    - `motion`: Get motion sensor pin
    - `motion-timeout`: Get motion sensor timeout value
    - `pwm-range`: Get PWM range
- `info`
  - `get`
    - `temp`: Get picow temp.
    - `disk-usage`: Get picow disk-usage
    - `version`: Get picow version
- `led`
  - `set`
    - `duty <nr>`: Set GPIO pin duty (PWM range min/max range)
  - `get`
    - `duty`: Get GPIO pin duty
- `motion`
  - `get`
    - `data`: Get motion sensor data
  - `event`
    - `watch`: [Listen for motion sensor events](#Listenformotionsensorevents)

## <a name='JSONtypescriptinterface'></a>JSON (typescript) interface

```typescript
interface Request {
  id?: number;
  group: "config" | "info" | "led" | "motion";
  type: "set" | "get" | "event";
  command: string;
  args?: (number | string)[] | null;
}

interface Response {
    id: number; # zero if no id in request
    error: string | null,
    data: any,
}
```

## <a name='JSONExample:SetGetGPIOpinsforLEDs'></a>JSON Example: Set/Get GPIO pins for LEDs

> `id` some identification number, to identify multiple responses

<a name="SetGPIOpinsforLEDs"></a>Set GPIO pins for LEDs (ex.: set pins for rgbw to 0-3)

```json
{
  "id": 1,
  "group": "config",
  "type": "set",
  "command": "led",
  "args": [0, 1, 2, 3]
}
```

Server response on success

```json
{
  "id": 1,
  "error": null,
  "data": null
}
```

<a name="GetGPIOpinsforLEDs"></a>Get GPIO pins

```json
{
  "id": 2,
  "group": "config",
  "type": "get",
  "command": "led",
  "args": null
}
```

Server response on success

```json
{
  "id": 2,
  "error": null,
  "data": [0, 1, 2, 3]
}
```

## <a name='Listenformotionsensorevents'></a>Listen for motion sensor events

This will return a data stream separated with newlines "\\n" every time a motion event happened

Example:

```json
{ "id": 0, "error": null, "data": null }
{ "id": 0, "error": null, "data": null }
{ "id": 0, "error": null, "data": null }
```
