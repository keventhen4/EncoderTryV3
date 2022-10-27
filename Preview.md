
# ETry
>Hello, this is ETry, an Encoder which attempts to encode and decode messages in Symmetric and RSA Asymmetric Key Encryption/Decryption when given the correct key(s). You can use those keys to create secret messages for your friends that most likely nobody else on the internet will be able to decode as long as you keep the key(s) a secret.

**Tips**
- When inputting key(s), please input the string version without the *b'*[key]*'* that surrounds the key. For example, a key in string format might read *b'abc'*. When inputting the key, input instead: *abc*
- When inputting text to be decrypted, please input the string format, following the rules of the first tip



>Example:

  When encrypting with Symmetric Key Cryptography:
- Values received from run:
  - Entered Text: yo watsup!
  - Key As String: b'ZGNQH16Y9nLdmTpESYcO1J8Qz6bC0CxYThFzRhwKTDw='
  - Encrypted Text As String: b'gAAAAABjKT7qdA_Li_RL1Ld0e2IP1Vz58ybTU41wJ2Powzb07j8--dDhPzZ6h1fAcH5q62BiTW5j-ZmKVTmdktx1GDP8POEajQ=='

When decrypting with Symmetric Key Cryptography:
- Values entered from run:
  - Key Entered: ZGNQH16Y9nLdmTpESYcO1J8Qz6bC0CxYThFzRhwKTDw=
  - Encrypted Text Entered: gAAAAABjKT7qdA_Li_RL1Ld0e2IP1Vz58ybTU41wJ2Powzb07j8--dDhPzZ6h1fAcH5q62BiTW5j-ZmKVTmdktx1GDP8POEajQ==
  - Decrypted Text: yo watsup!