# PicoW LED Micro Controller

<!--toc:start-->

- [PicoW LED Micro Controller](#picow-led-micro-controller)
    - [General Info](#general-info)
    - [Command Table](#command-table)
    - [Request / Response Interface](#request-response-interface)

<!--toc:end-->

## General Info

Default Port: 3000

Download firmware from here: https://micropython.org/download/RPI_PICO_W/

## Command Table

**Set**:

| Group  | Command | Args           | Response Data |
| ------ | ------- | -------------- | ------------- |
| config | led     | `<pin> ...`    | `null`        |
| led    | color   | `<number> ...` | `null`        |

**Get**:

| Group  | Command    | Args | Response Data                    |
| ------ | ---------- | ---- | -------------------------------- |
| config | led        | -    | `number[]`                       |
| led    | color      | -    | `number[]`                       |
| info   | temp       | -    | `number`                         |
| info   | disk-usage | -    | `{ used: number, free: number }` |
| info   | version    | -    | `string`                         |

## Request / Response Interface

> NOTE: If the `Request` id is set to `-1`, the pico will skip the server response

```typescript
interface Request {
    id?: number;
    group: string;
    type: string;
    command: string;
    args?: any[];
}

interface Response {
    id: number;
    error: string | null;
    data: any | null;
}
```
