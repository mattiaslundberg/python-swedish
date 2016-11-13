import codecs


class SwedishCodec(codecs.Codec):
    def encode(self, data, errors="strict"):
        return (data.encode("utf8"), len(data))

    def decode(self, data, errors="strict"):
        data_string = codecs.decode(data, "utf8")

        data_string = data_string.replace("Sant", "True")
        data_string = data_string.replace("om", "if")
        data_string = data_string.replace("skriv", "print")

        return (data_string, len(data))


class SwedishIncrementalEncoder(codecs.IncrementalEncoder):
    def encode(self, input, final=False):
        return SwedishCodec().encode(input)


class SwedishIncrementalDecoder(codecs.IncrementalDecoder):
    def decode(self, input, final=False):
        return SwedishCodec().decode(input)


class SwedishStreamReader(SwedishCodec, codecs.StreamReader):
    pass


class SwedishStreamWriter(SwedishCodec, codecs.StreamWriter):
    pass


def search(encoding):
    if encoding != "swedish":
        return None

    return codecs.CodecInfo(
        name="swedish",
        encode=SwedishCodec().encode,
        decode=SwedishCodec().decode,
        incrementalencoder=SwedishIncrementalEncoder,
        incrementaldecoder=SwedishIncrementalDecoder,
        streamreader=SwedishStreamReader,
        streamwriter=SwedishStreamWriter,
    )


codecs.register(search)
