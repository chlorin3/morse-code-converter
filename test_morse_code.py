from morse_code import text_to_morse


def test_one_word():
    assert text_to_morse("computer") == "—•—• ——— —— •——• ••— — • •—•"


def test_sentence_lower():
    assert text_to_morse("please help me") == "•——• •—•• • •— ••• • / •••• • •—•• •——• / —— •"


def test_sentence_upper():
    assert text_to_morse("PLEASE HELP ME") == "•——• •—•• • •— ••• • / •••• • •—•• •——• / —— •"


def test_numbers():
    assert text_to_morse("1234567890") == "•———— ••——— •••—— ••••— ••••• —•••• ——••• ———•• ————• —————"


def test_separator():
    assert text_to_morse("please help", "   ") == "•——•   •—••   •   •—   •••   •   /   ••••   •   •—••   •——•"


def test_symbols():
    assert text_to_morse(" %()co^lou]r.") == "—•—• ——— •—•• ——— ••— •—•"


def test_mix():
    assert text_to_morse("pLeaSE 854 me!") == "•——• •—•• • •— ••• • / ———•• ••••• ••••— / —— •"
