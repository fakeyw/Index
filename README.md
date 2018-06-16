A structure as named layers, for searching use.

```
OLD type of tree:

ROOT
+---page
|   +---news
|   |   +---recent
|   |   |   +---newB
|   |   +---hot
|   |       +---newA
|   +---games
|       +---zelda
+---users
|   +---space
+---admin
    +---users

NEW type of tree:

ROOT
├─ page
│  ├─ news
│  │  ├─ recent
│  │  │  └─ newB
│  │  └─ hot
│  │     └─ newA
│  └─ games
│     └─ zelda
├─ users
│  └─ space
└─ admin
   └─ users
```



