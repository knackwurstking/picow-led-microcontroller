# PicoW LED Microcontroller

<!-- vscode-markdown-toc -->

- [Command Table](#CommandTable)
- [Response / Request interface](#ResponseRequestinterface)

<!-- vscode-markdown-toc-config
	numbering=false
	autoSave=true
	/vscode-markdown-toc-config -->
<!-- /vscode-markdown-toc --># PicoW LED Micro Controller

## <a name='CommandTable'></a>Command Table

| Group  | Type  | Command        | Args                                       | Response Data                    |
| ------ | ----- | -------------- | ------------------------------------------ | -------------------------------- |
| config | set   | led            | `<gp (number)> ...`                        | `null`                           |
| config | set   | motion         | `<gp (number)>`                            | `null`                           |
| config | set   | motion-timeout | `<ms (number)>`                            | `null`                           |
| config | set   | pwm-range      | `<min (number)> <max (number)>`            | `null`                           |
| config | get   | led            | -                                          | `number[]`                       |
| config | get   | motion         | -                                          | `number`                         |
| config | get   | motion-timeout | -                                          | `number`                         |
| config | get   | pwm-range      | -                                          | `[number, number]`               |
| info   | get   | temp           | -                                          | `number`                         |
| info   | get   | disk-usage     | -                                          | `{ used: number, free: number }` |
| info   | get   | version        | -                                          | `string`                         |
| led    | set   | duty           | `<duty (number)> [<pin (number \| null)>]` | `null`                           |
| led    | get   | duty           | `<pin (number \| null)>`                   | `number[] \| number \| null`     |
| motion | event | start          | -                                          | -                                |
| motion | event | stop           | -                                          | -                                |

## <a name='ResponseRequestinterface'></a>Response / Request interface

> TODO: info about special `id` handling (-1 / no-response)

```typescript
interface Request {
  // TODO: ...
}

interface Response {
  // TODO: ...
}
```
