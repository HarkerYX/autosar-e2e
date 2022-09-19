def calculate_crc8(
    data: bytes, start_value: int = 0xFF, first_call: bool = True
) -> int: ...
def calculate_crc8_h2f(
    data: bytes, start_value: int = 0xFF, first_call: bool = True
) -> int: ...
def calculate_crc16(
    data: bytes, start_value: int = 0xFFFF, first_call: bool = True
) -> int: ...
def calculate_crc32(
    data: bytes, start_value: int = 0xFFFFFFFF, first_call: bool = True
) -> int: ...
def calculate_crc32_p4(
    data: bytes, start_value: int = 0xFFFFFFFF, first_call: bool = True
) -> int: ...
def calculate_crc64(
    data: bytes, start_value: int = 0xFFFFFFFFFFFFFFFF, first_call: bool = True
) -> int: ...