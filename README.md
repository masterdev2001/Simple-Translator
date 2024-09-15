# translator
Build a simple translator app using Microsoft translator.

## How it works
- If you run the translator program, you can see the tray icon.
  And if you try to run translator program without closing previous one, you will get an error message Translator app is already running.
- If you right-click on the tray icon, you can see two options: "quit" and "settings". 
  If you click the quit, it will close the translator app.
  If you click the settings, it will show the setting dialog.
- In setting dialog, you can change the Auth Key, Hotkeys for source-to-target and target-to-source translation, source language and target language.
  At the moment, this translator supports 6 languages: English, Chinese, Japanese, Russian, French, and German.
- Then you can test this translator app on notepad. (Let's imagine, source language is English and target language is Chinese)
  - Write some english sentence and select it.
  - Then press source-to-target hotkey. Then the selected text will translate to Chinese.
  - Then select the Chinese text and press the target-to-source hotkey. Then the selected text will translate back to English.
  - If you didn't input the Auth key on setting dialog, there will be error notification "Auth Key is required.".
  - If the auth key is not valid one, then there will be error notification "Auth Key is not valid".