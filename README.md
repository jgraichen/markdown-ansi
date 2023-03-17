# markdown-ansi

A `pymdownx.superfences` formatter for rendering console output with ANSI colors.

Note: Only basic ANSI color escape sequences are supported.

## Usage

```yaml
markdown_extensions:
  - pymdownx.superfences:
      custom_fences:
        - name: ansi
          class: ansi
          format: !!python/name:markdown_ansi.ansi.fence_code_format
```
