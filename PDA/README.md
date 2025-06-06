# This PDA validates nested comments using /* and */ delimiters, like in C/Java/JavaScript.
## How it works:

- Push: When finding /*, push a marker onto the stack (comment opened)
- Pop: When finding */, pop from stack (comment closed)
- Validation: Stack must be empty at the end (all comments closed)

## Valid examples from input.txt:

- "/* simple comment */" → One level 
- "/* outer /* inner */ outer */" → Properly nested 
- "/* first */ /* second */" → Sequential comments 

## Invalid examples:

- "/* unclosed comment" → Missing */ 
- "closed without open */" → No matching /* 
- "/* no */ matching /* pairs" → Unbalanced 
