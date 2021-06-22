## [Cut-It/app.py](/Cut-It/app.py)
---
### Cut-It/app.`main` [class] [inherits: `GUI`]
Adds logic to the GUI class
<details style='color: #333333'><summary>Methods</summary><p>

#### `main`.\_\_init\_\_
*No documentation provided.*
#### `main`.\_loadSettings
<details style='color: #333333'><summary>Details</summary><p>

Loads all user data into instance vars
Fills in UI with Settings if initialLoad
</p></details>

#### `main`.\_\_loadSettingsUI
<details style='color: #333333'><summary>Details</summary><p>

Loads the Settings into the GUI
</p></details>

#### `main`.\_updateShortcut
<details style='color: #333333'><summary>Details</summary><p>

Updates shortcut when user wants to view a separate one
</p></details>

#### `main`.\_saveShortcut
<details style='color: #333333'><summary>Details</summary><p>

Saves shortcut to memory when user is done editing
</p></details>

#### `main`.\_loadShortcuts
<details style='color: #333333'><summary>Details</summary><p>

Inits custom keybindings for all user-defined shortcuts
</p></details>

#### `main`.\_saveSettings
<details style='color: #333333'><summary>Details</summary><p>

Saves settings to data.json 
</p></details>

#### `main`.\_updates
<details style='color: #333333'><summary>Details</summary><p>

Changes text of button to notify if update is needed or not
</p></details>

#### `main`.\_feedback
<details style='color: #333333'><summary>Details</summary><p>

Submits feedback
</p></details>

#### `main`.\_toggleTheme
<details style='color: #333333'><summary>Details</summary><p>

Changes theme from current to reciprocal (applies on reboot)
(eg. light -> dark, dark -> light)
</p></details>

#### `main`.\_addDelimiter
<details style='color: #333333'><summary>Details</summary><p>

Triggered when the evidence box's text changes
Adds closing bracket ] when an opening one [ is typed
</p></details>

#### `main`.\_toHTML
<details style='color: #333333'><summary>Details</summary><p>

Returns list: [text of card, html of card]
Copies plain & rich text to clipboard IFF :param: copy -> True
</p></details>

#### `main`.\_auto
<details style='color: #333333'><summary>Details</summary><p>

Adds MLA & Debate-Grade Citation and/or article text to evidence box
</p></details>

#### `main`.\_copy
<details style='color: #333333'><summary>Details</summary><p>

Copies card to clipboard
</p></details>

#### `main`.\_onClose
<details style='color: #333333'><summary>Details</summary><p>

Behavior for window close (saves card first)
</p></details>

#### `main`.\_tabChanged
<details style='color: #333333'><summary>Details</summary><p>

Saves settings and reapplies them on tab change
</p></details>

#### `main`.\_log
<details style='color: #333333'><summary>Details</summary><p>

Posts card objs to API for efficacy monitoring & paywall enforcement
& GitHub badge stats
</p></details>

#### `main`.\_\_loadAllCards
<details style='color: #333333'><summary>Details</summary><p>

Adds all cards to card history selector
</p></details>

#### `main`.\_saveCard
<details style='color: #333333'><summary>Details</summary><p>

Saves current card if it has data (is not blank)
</p></details>

#### `main`.\_newCard
<details style='color: #333333'><summary>Details</summary><p>

Saves old card and opens new one
</p></details>

#### `main`.\_loadCard
<details style='color: #333333'><summary>Details</summary><p>

Loads most recent card (saves previous one as well and adds to card selector)
</p></details>

#### `main`.\_deleteCard
<details style='color: #333333'><summary>Details</summary><p>

Deletes currently open card after second click for safety
</p></details>

#### `main`.\_addToCardSelector
<details style='color: #333333'><summary>Details</summary><p>

Adds current card to card selector
</p></details>

#### `main`.\_cardSelectionChanged
<details style='color: #333333'><summary>Details</summary><p>

Resets the delete status (clicked once) if the selected card changes
</p></details>

#### `main`.\_autoCiteAndPoll
<details style='color: #333333'><summary>Details</summary><p>

Adds MLA & Debate-Grade Citation & article text to evidence box
</p></details>

#### `main`.\_autoCite
<details style='color: #333333'><summary>Details</summary><p>

Adds MLA & Debate-Grade Citation to evidence box
</p></details>

#### `main`.\_autoPoll
<details style='color: #333333'><summary>Details</summary><p>

Adds article text to evidence box
</p></details>

#### `main`.\_print
<details style='color: #333333'><summary>Details</summary><p>

Triggers User Input for Directory and Saves Card as PDF
</p></details>

#### `main`.\_\_getSelectedText
<details style='color: #333333'><summary>Details</summary><p>

Returns cursor's start index and currently selected text in a tuple
</p></details>

#### `main`.\_\_addText
<details style='color: #333333'><summary>Details</summary><p>

Inserts formatted text at cursor position and reselects text
Copies text to clipboard
</p></details>

#### `main`.\_primaryEmphasis
<details style='color: #333333'><summary>Details</summary><p>

Styles text with Primary Emphasis
</p></details>

#### `main`.\_secondaryEmphasis
<details style='color: #333333'><summary>Details</summary><p>

Styles text with Secondary Emphasis
</p></details>

#### `main`.\_tertiaryEmphasis
<details style='color: #333333'><summary>Details</summary><p>

Styles text with Tertiary Emphasis
</p></details>

#### `main`.\_highlightP
<details style='color: #333333'><summary>Details</summary><p>

Highlights text with Primary Highlight Color
</p></details>

#### `main`.\_highlightS
<details style='color: #333333'><summary>Details</summary><p>

Highlights text with Secondary Highlight Color
</p></details>

#### `main`.\_bold\_
<details style='color: #333333'><summary>Details</summary><p>

Bolds selected text
</p></details>

#### `main`.\_underline\_
<details style='color: #333333'><summary>Details</summary><p>

Underlines selected text
</p></details>

#### `main`.\_italic\_
<details style='color: #333333'><summary>Details</summary><p>

Italicises selected text
</p></details>

#### `main`.\_clearFormatting
<details style='color: #333333'><summary>Details</summary><p>

Clears Formatting on selected text
</p></details>

#### `main`.\_minimizeText
<details style='color: #333333'><summary>Details</summary><p>

Minimizes Text 
</p></details>

#### `main`.\_bold
<details style='color: #333333'><summary>Details</summary><p>

Returns bolded version of :param: text
</p></details>

#### `main`.\_underline
<details style='color: #333333'><summary>Details</summary><p>

Returns underlined version of :param: text
</p></details>

#### `main`.\_italic
<details style='color: #333333'><summary>Details</summary><p>

Returns italicised version of :param: text
</p></details>

#### `main`.\_highlight
<details style='color: #333333'><summary>Details</summary><p>

Returns highlighted version of :param: text of the color :param: color
</p></details>

</p></details>

## [Cut-It/GUI.py](/Cut-It/GUI.py)
---
### Cut-It/GUI.`GUI` [class] [inherits: `QMainWindow`]
*No documentation provided.*
<details style='color: #333333'><summary>Methods</summary><p>

#### `GUI`.\_\_init\_\_
<details style='color: #333333'><summary>Details</summary><p>

Loads latest UI
</p></details>

#### `GUI`.addCardHistory
<details style='color: #333333'><summary>Details</summary><p>

Manually fill out the Card History groupBox (due to custom widgets)
</p></details>

#### `GUI`.updateStyling
*No documentation provided.*
#### `GUI`.addToolTips
<details style='color: #333333'><summary>Details</summary><p>

Adds in ToolTips
</p></details>

#### `GUI`.addAttrs
<details style='color: #333333'><summary>Details</summary><p>

Adds in missing attrs.
</p></details>

#### `GUI`.addDistroDetails
<details style='color: #333333'><summary>Details</summary><p>

Returns a formatted String to be inserted into the Distro box in the about section
</p></details>

</p></details>

## [Cut-It/install.py](/Cut-It/install.py)
---
### Cut-It/install.`install` [function]
*No documentation provided.*
## [Cut-It/utils/card.py](/Cut-It/utils/card.py)
---
### Cut-It/utils/card.`Card` [class] [inherits]
*No documentation provided.*
<details style='color: #333333'><summary>Methods</summary><p>

#### `Card`.isCard
<details style='color: #333333'><summary>Details</summary><p>

Returns (bool) if the card actually has data
</p></details>

#### `Card`.getDict
<details style='color: #333333'><summary>Details</summary><p>

Returns (dict) representation of the object
</p></details>

</p></details>

### Cut-It/utils/card.`Logger` [class] [inherits: `QThread`]
*No documentation provided.*
<details style='color: #333333'><summary>Methods</summary><p>

#### `Logger`.\_\_init\_\_
*No documentation provided.*
#### `Logger`.run
*No documentation provided.*
</p></details>

## [Cut-It/utils/citer.py](/Cut-It/utils/citer.py)
---
### Cut-It/utils/citer.`cite` [class] [inherits]
*No documentation provided.*
<details style='color: #333333'><summary>Methods</summary><p>

#### `cite`.\_\_init\_\_
<details style='color: #333333'><summary>Details</summary><p>

:param: URL (str) - the URL for your citation
:desc: creates citation
</p></details>

#### `cite`.cite
<details style='color: #333333'><summary>Details</summary><p>

gets raw citation data from API
</p></details>

#### `cite`.format
<details style='color: #333333'><summary>Details</summary><p>

formats raw citation date
</p></details>

#### `cite`.getMissingAttrs
<details style='color: #333333'><summary>Details</summary><p>

Returns a list of missing attributes (key) or None (if all present)
</p></details>

#### `cite`.debate
<details style='color: #333333'><summary>Details</summary><p>

Returns a simplified debate-ready citation
</p></details>

#### `cite`.mla
<details style='color: #333333'><summary>Details</summary><p>

Returns an MLA 8 citation
</p></details>

</p></details>

## [Cut-It/utils/clipboard_OSX.py](/Cut-It/utils/clipboard_OSX.py)
---
### Cut-It/utils/clipboard_OSX.`clipboard` [class] [inherits]
*No documentation provided.*
<details style='color: #333333'><summary>Methods</summary><p>

#### `clipboard`.add
<details style='color: #333333'><summary>Details</summary><p>

Injects both regular text (unformatted)
and html ('rich' text) to clipboard
</p></details>

</p></details>

## [Cut-It/utils/clipboard_WIN.py](/Cut-It/utils/clipboard_WIN.py)
---
### Cut-It/utils/clipboard_WIN.`clipboard` [class] [inherits]
*No documentation provided.*
<details style='color: #333333'><summary>Methods</summary><p>

#### `clipboard`.add
<details style='color: #333333'><summary>Details</summary><p>

Injects both regular text (unformatted)
and html ('rich' text) to clipboard
</p></details>

</p></details>

## [Cut-It/utils/data.py](/Cut-It/utils/data.py)
---
### Cut-It/utils/data.`init` [function]
Initializes both Card and Preferences storage
### Cut-It/utils/data.`getIndex` [function]
Returns (int) current card index
### Cut-It/utils/data.`setIndex` [function]
Sets the stored card index
### Cut-It/utils/data.`getPrefData` [function]
Returns a dict of data.json
### Cut-It/utils/data.`setPrefData` [function]
Writes to data.json
### Cut-It/utils/data.`getPref` [function]
Returns the value of the inputted preference key
### Cut-It/utils/data.`setPref` [function]
Sets the value of the inputted preference key to the
inputted value
### Cut-It/utils/data.`getShort` [function]
Returns the value of the inputted shortcut key
### Cut-It/utils/data.`setShort` [function]
Sets the value of the inputted shortcut key to the
inputted value
### Cut-It/utils/data.`getCardData` [function]
Returns a dict of cards.json
### Cut-It/utils/data.`setCardData` [function]
Writes to cards.json
### Cut-It/utils/data.`getCard` [function]
Returns card at start OR at supplied index
### Cut-It/utils/data.`addCard` [function]
Checks if a card contains information, if so adds it
to the end of cards.json, or if an index is 
supplied it will overwrite the card at that pos
### Cut-It/utils/data.`deleteCard` [function]
Deletes card at specified index
## [Cut-It/utils/distro.py](/Cut-It/utils/distro.py)
---
### Cut-It/utils/distro.`version` [function]
Returns current software version
### Cut-It/utils/distro.`tag` [function]
Returns current software tag
## [Cut-It/utils/export.py](/Cut-It/utils/export.py)
---
### Cut-It/utils/export.`PrintPDF` [class] [inherits: `QWidget`]
*No documentation provided.*
<details style='color: #333333'><summary>Methods</summary><p>

#### `PrintPDF`.\_\_init\_\_
*No documentation provided.*
#### `PrintPDF`.initUI
*No documentation provided.*
#### `PrintPDF`.getFile
*No documentation provided.*
#### `PrintPDF`.save
*No documentation provided.*
#### `PrintPDF`.finished
*No documentation provided.*
</p></details>

## [Cut-It/utils/ext_combobox.py](/Cut-It/utils/ext_combobox.py)
---
### Cut-It/utils/ext_combobox.`ExtendedComboBox` [class] [inherits: `QComboBox`]
*No documentation provided.*
<details style='color: #333333'><summary>Methods</summary><p>

#### `ExtendedComboBox`.\_\_init\_\_
*No documentation provided.*
#### `ExtendedComboBox`.goToStart
*No documentation provided.*
#### `ExtendedComboBox`.on\_completer\_activated
*No documentation provided.*
#### `ExtendedComboBox`.setModel
*No documentation provided.*
#### `ExtendedComboBox`.setModelColumn
*No documentation provided.*
</p></details>

## [Cut-It/utils/feedback.py](/Cut-It/utils/feedback.py)
---
### Cut-It/utils/feedback.`send_feedback` [function]
*No documentation provided.*
## [Cut-It/utils/MainWindow.py](/Cut-It/utils/MainWindow.py)
---
### Cut-It/utils/MainWindow.`RAW_UI` [class] [inherits: `QMainWindow`]
*No documentation provided.*
<details style='color: #333333'><summary>Methods</summary><p>

#### `RAW_UI`.setupUi
*No documentation provided.*
#### `RAW_UI`.retranslateUi
*No documentation provided.*
</p></details>

## [Cut-It/utils/resource.py](/Cut-It/utils/resource.py)
---
### Cut-It/utils/resource.`PATH` [class] [inherits]
*No documentation provided.*
<details style='color: #333333'><summary>Methods</summary><p>

#### `PATH`.get
<details style='color: #333333'><summary>Details</summary><p>

returns path for included files
(used when packaged into a binary)
</p></details>

</p></details>

## [Cut-It/utils/text_scraper.py](/Cut-It/utils/text_scraper.py)
---
### Cut-It/utils/text_scraper.`text` [class] [inherits]
*No documentation provided.*
<details style='color: #333333'><summary>Methods</summary><p>

#### `text`.scrape
*No documentation provided.*
</p></details>

## [Cut-It/utils/version_check.py](/Cut-It/utils/version_check.py)
---
### Cut-It/utils/version_check.`check` [function]
*No documentation provided.*
