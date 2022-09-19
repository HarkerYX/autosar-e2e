import e2e.crc

# fmt: off
def test_calculate_crc8():
    assert 0x59 == e2e.crc.calculate_crc8(bytearray(b"\x00\x00\x00\x00"))
    assert 0x59 == e2e.crc.calculate_crc8(b"\x00\x00\x00\x00")
    assert 0x37 == e2e.crc.calculate_crc8(b"\xF2\x01\x83")
    assert 0x79 == e2e.crc.calculate_crc8(b"\x0F\xAA\x00\x55")
    assert 0xB8 == e2e.crc.calculate_crc8(b"\x00\xFF\x55\x11")
    assert 0xCB == e2e.crc.calculate_crc8(b"\x33\x22\x55\xAA\xBB\xCC\xDD\xEE\xFF")
    assert 0x8C == e2e.crc.calculate_crc8(b"\x92\x6B\x55")
    assert 0x74 == e2e.crc.calculate_crc8(b"\xFF\xFF\xFF\xFF")

def test_calculate_crc8_h2f():
    assert 0x12 == e2e.crc.calculate_crc8_h2f(bytearray(b"\x00\x00\x00\x00"))
    assert 0x12 == e2e.crc.calculate_crc8_h2f(b"\x00\x00\x00\x00")
    assert 0xC2 == e2e.crc.calculate_crc8_h2f(b"\xF2\x01\x83")
    assert 0xC6 == e2e.crc.calculate_crc8_h2f(b"\x0F\xAA\x00\x55")
    assert 0x77 == e2e.crc.calculate_crc8_h2f(b"\x00\xFF\x55\x11")
    assert 0x11 == e2e.crc.calculate_crc8_h2f(b"\x33\x22\x55\xAA\xBB\xCC\xDD\xEE\xFF")
    assert 0x33 == e2e.crc.calculate_crc8_h2f(b"\x92\x6B\x55")
    assert 0x6C == e2e.crc.calculate_crc8_h2f(b"\xFF\xFF\xFF\xFF")

def test_calculate_crc16():
    assert 0x84C0 == e2e.crc.calculate_crc16(bytearray(b"\x00\x00\x00\x00"))
    assert 0x84C0 == e2e.crc.calculate_crc16(b"\x00\x00\x00\x00")
    assert 0xD374 == e2e.crc.calculate_crc16(b"\xF2\x01\x83")
    assert 0x2023 == e2e.crc.calculate_crc16(b"\x0F\xAA\x00\x55")
    assert 0xB8F9 == e2e.crc.calculate_crc16(b"\x00\xFF\x55\x11")
    assert 0xF53F == e2e.crc.calculate_crc16(b"\x33\x22\x55\xAA\xBB\xCC\xDD\xEE\xFF")
    assert 0x0745 == e2e.crc.calculate_crc16(b"\x92\x6B\x55")
    assert 0x1D0F == e2e.crc.calculate_crc16(b"\xFF\xFF\xFF\xFF")

def test_calculate_crc32():
    assert 0x2144DF1C == e2e.crc.calculate_crc32(bytearray(b"\x00\x00\x00\x00"))
    assert 0x2144DF1C == e2e.crc.calculate_crc32(b"\x00\x00\x00\x00")
    assert 0x24AB9D77 == e2e.crc.calculate_crc32(b"\xF2\x01\x83")
    assert 0xB6C9B287 == e2e.crc.calculate_crc32(b"\x0F\xAA\x00\x55")
    assert 0x32A06212 == e2e.crc.calculate_crc32(b"\x00\xFF\x55\x11")
    assert 0xB0AE863D == e2e.crc.calculate_crc32(b"\x33\x22\x55\xAA\xBB\xCC\xDD\xEE\xFF")
    assert 0x9CDEA29B == e2e.crc.calculate_crc32(b"\x92\x6B\x55")
    assert 0xFFFFFFFF == e2e.crc.calculate_crc32(b"\xFF\xFF\xFF\xFF")

def test_calculate_crc32_p4():
    assert 0x6FB32240 == e2e.crc.calculate_crc32_p4(bytearray(b"\x00\x00\x00\x00"))
    assert 0x6FB32240 == e2e.crc.calculate_crc32_p4(b"\x00\x00\x00\x00")
    assert 0x4F721A25 == e2e.crc.calculate_crc32_p4(b"\xF2\x01\x83")
    assert 0x20662DF8 == e2e.crc.calculate_crc32_p4(b"\x0F\xAA\x00\x55")
    assert 0x9BD7996E == e2e.crc.calculate_crc32_p4(b"\x00\xFF\x55\x11")
    assert 0xA65A343D == e2e.crc.calculate_crc32_p4(b"\x33\x22\x55\xAA\xBB\xCC\xDD\xEE\xFF")
    assert 0xEE688A78 == e2e.crc.calculate_crc32_p4(b"\x92\x6B\x55")
    assert 0xFFFFFFFF == e2e.crc.calculate_crc32_p4(b"\xFF\xFF\xFF\xFF")

def test_calculate_crc64():
    assert 0xF4A586351E1B9F4B == e2e.crc.calculate_crc64(bytearray(b"\x00\x00\x00\x00"))
    assert 0xF4A586351E1B9F4B == e2e.crc.calculate_crc64(b"\x00\x00\x00\x00")
    assert 0x319C27668164F1C6 == e2e.crc.calculate_crc64(b"\xF2\x01\x83")
    assert 0x54C5D0F7667C1575 == e2e.crc.calculate_crc64(b"\x0F\xAA\x00\x55")
    assert 0xA63822BE7E0704E6 == e2e.crc.calculate_crc64(b"\x00\xFF\x55\x11")
    assert 0x701ECEB219A8E5D5 == e2e.crc.calculate_crc64(b"\x33\x22\x55\xAA\xBB\xCC\xDD\xEE\xFF")
    assert 0x5FAA96A9B59F3E4E == e2e.crc.calculate_crc64(b"\x92\x6B\x55")
    assert 0xFFFFFFFF00000000 == e2e.crc.calculate_crc64(b"\xFF\xFF\xFF\xFF")
# fmt: on