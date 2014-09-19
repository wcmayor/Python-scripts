import plistlib
import os.path
plist = plistlib.readPlist("library.xml")
for playlist in plist["Playlists"]:
    try:
        filename = os.path.join('playlists', str(playlist['Name']) + ".m3u")
        with open(filename, "a") as i:
            i.write("#EXTM3U\n")
        for track in playlist['Playlist Items']:
            with open(filename, "a") as i:
                i.write("/mnt/music/" + str(plist["Tracks"][str(track['Track ID'])]['Location'][49:]).replace("%20", " ").replace("%5B", "[").replace("%5D", "]") + "\n")
    except:
        continue;
