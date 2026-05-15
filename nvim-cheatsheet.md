# Neovim Cheatsheet

### moving around
`:bd` | buffer delete - closes the file. 
`:bn` | buffer next - switch to another open file 
`:bp` | buffer prev
`:e .` | browse files

### finding stuff
`SPACE + s + f` | find files
`SPACE + s + g` | live grep (search file contents)
`SPACE /` | fuzzily search only the current buffer
`SPACE SPACE` | find open buffers

### LSP navigation (requires LSP attached)
`grd` | go to definition
`grr` | go to references (all usages)
`gri` | go to implementation
`grt` | go to type definition
`grn` | rename symbol (across files)
`gra` | code actions
`K` | hover (show type info)
`gO` | document symbols (functions, vars in file)
`gW` | workspace symbols (search entire project)
`CTRL-o` | jump back (after navigation)
`CTRL-i` | jump forward

### file navigation
`gf` | go to file under cursor (literal path)
`gd` | go to definition (LSP-aware, understands aliases)
`CTRL-w f` | open file in split
`CTRL-w gf` | open file in new tab
