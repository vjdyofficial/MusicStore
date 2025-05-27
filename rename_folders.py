import os

# List of new folder names from your CSV (in order)
new_names = [
    "80sCity","80sGirl","Andromeda","AutumnRetro","Backmaps","BacktotheVice","BeautifulDay","BeTogether","Birthday","BoringDays",
    "ChillCity","CityParty","ColdOutside","ColladalaRetro","Collide","DecktheHalls-BallsEdition","Dissolved","DontLetmego","DoveBeach","Dream-Vocal",
    "Dream","ElephantLily","EntryoftheGladiators","Essence","Eternity","EverybodytoDance","Festival","GirlofRussia-ExtendedMix","GirlofRussia-TranceMix","GirlofRussia",
    "Happiness","HappyDaypart2","HappyDesigning","HappyJamaican","HappyNight","HappyTown-PartyMix+Vocal","HappyTown-PartyMix","HappyTown","HauntedHitch","Impressive",
    "Inspiration","Intense","Kaye","Lonely-Party+Lead","Lonely-Party","Lonely","MerryChristmas.BallsEdition","Midnight-RLDavidRemix","Midnight","Milestone-RLDavidRemix",
    "Milestone","MushroomBeep","News-Short","News-Sting","News","NiceBeautifulGirl","OneNightinJamaica","OntheBeach","OntheCafe","OriginofXiaomi",
    "OutofNowhere","OvertheCounter","Perspective","PinaColada","Promenade","Proxima","Regardless","RetroFuture","RetroGirl","SadDay",
    "SadTown","Sheissobeautiful","Situation","SleepingBeauty-Instrumental","SleepingBeauty-Lead","SleepingBeauty","Soca","Sosadtosee","Source","SpreadtheLove",
    "Stargazer-RLDavidRemix","Stargazer","SummerTreats","Supercharge-DeepHouse","Supercharge","Survival-DesertDelicacies","Survival-RLDavidRemix","Survival-TraditionalVersion","Survival","ThanksgivingDay",
    "Tiramisu","View","WallsThemeSong","Windy"
]

# Path to the folder containing the folders to rename
base_path = r"c:\Users\Vinscent Joshua\Documents\GitHub\MusicStore\AlbumArts\vjdyofficialmusic-2023"

# Get a sorted list of current folder names (excluding files)
current_folders = [f for f in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, f))]
current_folders.sort()

# Check if the number of folders matches the number of new names
if len(current_folders) != len(new_names):
    print(f"Folder count ({len(current_folders)}) does not match name count ({len(new_names)}).")
else:
    for old, new in zip(current_folders, new_names):
        old_path = os.path.join(base_path, old)
        new_path = os.path.join(base_path, new)
        if old != new:
            os.rename(old_path, new_path)
            print(f"Renamed: {old} -> {new}")
        else:
            print(f"Skipped (already named): {old}")