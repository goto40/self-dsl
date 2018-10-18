# Deploy your DSL as eclispe plugin

## Manual way to export and install a plugin

 * Within eclipse Export your language as "Deployable features".
 * Select the "*.feature" project of your language.
 * Select an archive file name to export your plugin
 * In the "Options" tab: "Browse" for "Categorize repository" and select the
    "*.repository" project of your language.
 * Click "finish".

Then, you can install the plugin from the exported archive in an eclipse
installation (You can, e.g., copy your eclipse folder, start the copy, install
your plugin and give the eclipse to another person). Installation is done
using the menu: "Help/Install New Software".

Notes: (1) When installing the plugin, it may be useful to disable 
"Contact all update sites..." (this caused problems in some examples). 
(2) You are also prompted, that the new plugin is not signed (you must 
accept this in order to continue).


## Create a product

(work in progress)


