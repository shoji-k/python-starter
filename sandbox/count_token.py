import tiktoken

enc = tiktoken.encoding_for_model("gpt-3.5")
tokens = enc.encode("Hello World!")
print(len(tokens))
print(tokens)
