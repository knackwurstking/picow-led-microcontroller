# PicoW LED Micro Controller

- [General Info](#general-info)
- [Command Table](#command-table)
- [Request / Response Interface](#request-response-interface)

## <a id="general-info"></a>General Info

Default Port: 3000

## <a id='command-table'></a>Command Table

**Set**:

| Group  | Command   | Args          | Response Data |
| ------ | --------- | ------------- | ------------- |
| config | led       | `<pin> ...`   | `null`        |
| config | pwm-range | `<min> <max>` | `null`        |
| led    | duty      | `<duty> ...`  | `null`        |

**Get**:

| Group  | Command    | Args | Response Data                    |
| ------ | ---------- | ---- | -------------------------------- |
| config | led        | -    | `number[]`                       |
| config | pwm-range  | -    | `[number, number]`               |
| info   | temp       | -    | `number`                         |
| info   | disk-usage | -    | `{ used: number, free: number }` |
| info   | version    | -    | `string`                         |
| led    | duty       | -    | `[]number`                       |

## <a id='request-response-interface'></a>Request / Response Interface

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
