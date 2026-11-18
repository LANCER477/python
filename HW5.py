def parse_ini_line(line: str) -> tuple[str, str] | None:
    line = line.strip()
    if not line or line.startswith('#') or line.startswith(';'):
        return None

    sep_idx = -1
    for i, ch in enumerate(line):
        if ch in (':', '='):
            sep_idx = i
            break

    if sep_idx == -1:
        return None

    key = line[:sep_idx].strip()
    val_part = line[sep_idx + 1:].lstrip()

    if not val_part:
        return key, ''

    if val_part[0] in ('"', "'"):
        quote_char = val_part[0]
        val_chars = []
        escaped = False
        i = 1
        while i < len(val_part):
            ch = val_part[i]
            if escaped:
                val_chars.append(ch)
                escaped = False
            elif ch == '\\':
                escaped = True
            elif ch == quote_char:
                break
            else:
                val_chars.append(ch)
            i += 1
        return key, ''.join(val_chars)
    else:
        for i, ch in enumerate(val_part):
            if ch in ('#', ';'):
                val_part = val_part[:i]
                break
        return key, val_part.strip()


def read_ini(filename: str) -> dict | None:
    try:
        with open(filename, "r", encoding="utf-8") as file:
            result = {}
            for line in file:
                parsed = parse_ini_line(line)
                if parsed:
                    k, v = parsed
                    result[k] = v
            return result
    except OSError as err:
        print(f"read_ini(): {err}")
        return None


def write_ini(filename: str, data: dict) -> bool:
    try:
        with open(filename, "w", encoding="utf-8") as file:
            for k, v in data.items():
                str_val = str(v)
                needs_quotes = (
                    any(c in str_val for c in (':', '=', '#', ';', '"', "'"))
                    or str_val.startswith(' ')
                    or str_val.endswith(' ')
                )
                if needs_quotes:
                    escaped = str_val.replace('\\', '\\\\').replace('"', '\\"')
                    formatted_val = f'"{escaped}"'
                else:
                    formatted_val = str_val
                file.write(f"{k} : {formatted_val}\n")
        return True
    except OSError as err:
        print(f"write_ini(): {err}")
        return False


def main():
    sample_ini_filename = "data_sample.ini"
    output_ini_filename = "data_saved.ini"

    sample_content = '''# Головний заголовок
; Коментар через крапку з комою

host : localhost ; адреса сервера
port : 3306      # порт
user : admin_user ; логін

pass_simple   : SimplePass123           ; звичайний пароль
pass_spaces   : "  spaces on edges  "   ; пароль із пробілами
pass_colons   : "user:secret:pass:999"  ; пароль з двокрапками
pass_hashes   : "c#sharp#key#hash"      ; пароль з '#'
pass_semicol  : "code;stmt;end;"        ; пароль з ';'
pass_all_spec : "  ::##;; secret! ;;##::  " ; спецсимволи
pass_escaped  : "quote\\\"inside:pass;word" # екранування лапок
'''

    try:
        with open(sample_ini_filename, "w", encoding="utf-8") as f:
            f.write(sample_content)
    except OSError as err:
        print(f"Помилка створення файлу: {err}")
        return

    config = read_ini(sample_ini_filename)
    if config is not None:
        for key, val in config.items():
            print(f"  {key:<15} = [{val}]")

        if write_ini(output_ini_filename, config):
            reloaded_config = read_ini(output_ini_filename)
            print(f"Збіг даних: {config == reloaded_config}")


if __name__ == '__main__':
    main()
