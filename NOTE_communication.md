# NOTE Communication

- `config`
  - `set`
    - `led <gp:nr> ...`: Set GPIO configuration for LEDs (ex.: rgbw)
    - `motion <gp:nr>`: Set motion sensor pin
    - `motion-timeout <milliseconds:nr>`: Set motion sensor timeout value
    - `pwm-range <min:nr> <max:nr>`: Set PWM range
  - `get`
    - `led`: Get GPIO configuration for LEDs (ex.: rgbw)
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
    - `???`: Listen for motion sensor events

## JSON (typescript) interface

Client Request:

```typescript
interface Request {
  id: number;
  group: "config" | "info" | "led" | "motion";
  type: "set" | "get" | "event";
  command: string;
  args?: (number | string)[] | null;
}
```

## JSON: `Command`

> `id` some identification number, to identify multiple responses

Set GPIO pins for LEDs (ex.: rgbw)

```json
{
  "id": 1,
  "group": "config",
  "type": "set",
  "command": "led",
  "args": [0, 1, 2, 3]
}
```

Get GPIO pins

```json
{
  "id": 2,
  "group": "config",
  "type": "get",
  "command": "led",
  "args": null
}
```
