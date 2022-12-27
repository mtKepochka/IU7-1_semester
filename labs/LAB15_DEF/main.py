# ИУ7-13Б
# Тюликов Максим Вячеславович
import struct as st

flag = 0
with open("Amogus.mp4", "rb") as file:
    file.seek(0, 2)
    max_size = file.tell()
    file.seek(0, 0)
    while file.tell() < max_size and flag != 1:
        d = file.read(4)
        s = int(list(st.unpack(">I", d))[0])
        d1 = file.read(4)
        s2 = st.unpack("4s", d1)[0].decode(encoding="ASCII")
        if s2 == "moov":
            while file.tell() < max_size:
                d = file.read(4)
                d1 = file.read(4)
                s = int(list(st.unpack(">I", d))[0])
                s2 = st.unpack("4s", d1)[0].decode(encoding="ASCII")
                if s2 == "mvhd":
                    file.read(12)
                    d = file.read(4)
                    d1 = file.read(4)
                    s = int(list(st.unpack(">I", d))[0])
                    s2 = int(list(st.unpack(">I", d1))[0])
                    print(s2/s, "- время в секундах")
                    flag = 1
                    break
                else:
                    file.read(s - 8)
        else:
            file.read(s - 8)
