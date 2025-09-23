-- Launch two Terminal windows running cmatrix and htop, and set them to a named profile
-- Replace "PROFILE_NAME" with the Terminal profile you prefer (e.g. "Pro", "Basic", or your custom profile name)

set PROFILE_NAME to "Vornado" -- <-- change this to your Terminal profile name

tell application "Terminal"
	activate
	
	-- First window: cmatrixß
	set win1 to do script "exec zsh -lc \"cmatrix\""
	-- apply profile to the tab (tab is returned by do script)
	try
		set current settings of tab 1 of window 1 to (settings set PROFILE_NAME)
	end try
	
	-- Second window: htop
	delay 0.2
	set win2 to do script "exec zsh -lc \"htop\""
	try
		set current settings of tab 1 of window 1 to (settings set PROFILE_NAME)
	end try
end tell
