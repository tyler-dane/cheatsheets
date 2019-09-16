# VIM CHEATSHEET
- Use these commands from inside a `vim` session.
    - To open a test vim session, run this from the command-line: `vim ~/test-vim.sh`
- Text inside `{}` is swappable with the adjacent characters


### Getting Help
```bash    
:help           #Opens VIM help window in terminal
CTRL-W CTRL-W   #Jump from help window
CTRL-J          #Jump
CTRL-T CTRL-O   #Return to previous location
F1              #Opens OS help window
```

### `vimrc`
```
:so %               # Sources currently-open .vimrc
:so $MYVIMRC        # Sources .vimrc when from diff file    
```

### Navigation 
```
 _      # (underscore) Jumps to the first non-whitespace character on the same line the cursor is on
{+-}    # Jumps to first non-whitespace character on next/revious line
2w      # Moves cursor 2 words forward
3e      # Moves cursor to end of third word forward
0       # Moves cursor to start of line
A       # Appends cursor to end of line and enters insert mode
b	# jump to beginning of current word
e	# jump to end of current word
fX      to next 'X' after cursor, in the same line (X is any character)
FX      to previous 'X' before cursor (f and F put the cursor on X)
tX      til next 'X' (similar to above, but cursor is before X)
TX      til previous 'X'
;       repeat above, in same direction
,       repeat above, in reverse direction

CTL-G   # Shows location in the file and file status
G       # Moves cursor to bottom of file
gg      # Moves cursor to top of file
{#}G    # Moves cursor to the given line number
:{#}    # Moves cursor to the given line number
%                  # When cursor is over a (, [, or {, this finds the matching closing symbol.
```

### Searching
```
/{search}          # Searches for results in file
n                  # Cycles forward through results
N                  # Cycles backwards through results
*                  # Search forward for next occurence of word nearest cursor. Case insensitive                  
#                  # Same as `*` but backward
```



### Text Manipulation
```
>       # Indents highlighted text
{#}>    # Indents highlighted text for specified times
p       # Puts previously deleted text below the cursor
]p      # Same as above, but aligns block with surrounding text
r{x}    # Replaces text with the letter after r
R       # Replaces more than one character, entering you into Insert Mode
ce      # Changes until end of a word and enter Insert Mode. This is a better option than d[motion] when you want to insert text
c$      # Changes until end of line
o ; O   # Opens below, above -- enters you into Insert Mode
a       # Insert text AFTER the cursor

u       # Undo previous command
CTL-r   # Re-do prevoius command

Y       # Copies entire line (use *P* or *p* to then paste before/after current line)
y       # Yanks (copies) text
            EXAMPLE 1:
                yw  #Yanks word
            EXAMPLE 2:
                v       #Enters visual mode
                ARROWS  #Highlights command
                y       #Enters yank mode
                $      #Moves cursor to end of line (highlighting)
                p       #Puts (pastes) the text
                ESC     #Exits visual mode

yw	# yanks everything from cursor to end of word
yaw	# yanks entire word regardless of cursor location
:2,5y       # Yanks everything from lines 2-5
:m{#,0, $}    # Moves line to a line number or before first or after last line
```

#### Selecting and manipulating
```
/\c                         # case insensitive search (e.g. /\cSearchTerm)
~                           # Toggles capitalization of selected text (requires Twiddle case)
V                           # Select entire line
Vip or Vap                  # Select current paragraph
    o                       # Toggle between beginning and end of selected paragraph


                           # Note: may have to add `%` before these commands if not using an IDE
vi{(["'b}                  # Selects everything between `()`s or `[]`s or `""`s or `''`s or `<block>` on current line
ci{(["'}                   # Changes everything between ()s or []s or ""s or ''s on current line
di{(["' or %di{symbol}     # Deletes everything between {}s ()s or []s or ""s or ''s on current line
    

CTRL-v                      # Vertical / column select
```

### Deleting
```
dw      		# Deletes from cursor to end of word
daw     		# "Delete a word" (deletes entire word under cursor)    
caw     		# "Change a word" (deletes the word under the cursor and put you in insert mode)
d$      		# Deletes to end of line
de      		# Deletes to end of current word 
dd      		# Deletes entire line
C			# Deletes to end of line and enters Insert mode. Pair with `_` for quickly replace lines
:a,bd   		# Deletes from a to b
:,bd    		# Deletes from current location to b
:%s/phrase//gc		# Delete each 'phrase' in document, prompting for comfirmation

```

### Execute Commands
```bash
:!                          #Executes external shell command
v {motion} :w FILENAME      #Saves part of the file that you highlighted to current directory
:r FILENAME                 #Retrieves the highlighted text that you previously saved and enter it into current VIM session
:r !COMMAND [e.g. `:r !ls]  #Reads the output of an external command in the VIM session. Useful for log review.
.                           # Repeats last command
```

### Substitution
```bash
:%s/old/new/g        #Substitutes 'old' for 'new' in current line only
:%s/old/new/gc       #Globally substitutes 'old' for 'new', prompting for confirmation for each substitution
:%s/old/new/g       #Globally substitutes 'old' for 'new' without prompting for confirmation
:#,#s/old/new/g     #Substitutes 'old' for 'new', where #,# are the line numbers of the range of lines to substitute  
:6,11s/bad/good/g    # Substitutes in lines 6-11, including 6 and 11.

```
### Ignoring Case
```bash
EXAMPLE 1:      
    /ignore\c       #Searches for 'ignore' and ignores case
EXAMPLE 2:
    /ignore         #Searches for 'ignore'
    :set ic         #Sets 'ignore case' option
    :set hls is     #Sets hlsearch in search options
    /ignore         #Type command again for new options to take effect
    :set noic       #Disables ignoring case again
    :nohls          #Disables highlighting
```
### Commenting Out Blocks of Text:
```bash	
ESC
CTRL+v (visual block mode)
up/down arrow
SHIFT + I  #Or whatever text you want to include
ESC
```
### Uncommenting Blocks of Text:
```bash
ESC
CTRL + v 	#Enters visual block mode
(up/down arrow to select lines to uncomment)
x       	#Deletes comments
ESC         #Exits visual block mode
```

