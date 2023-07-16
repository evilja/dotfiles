while True:
  home = input("Whats your home name (/home/?): ")
  to = "/home/"+home
  print(f" Is this home name: {home}\n and this path {to} true? (Y/n) ",end="")
  if input().lower() == "y":
    print("okay\n")
    break

folders = ["config", "fonts", "icons", "gruvbox", "polybar-scripts", "wallpaper"]
ln_sf = "ln -sf {}/.icons/default {}/default".format(to, to)

for folder in folders:
  os.system("mv {} {}/.{}".format(folder, to, folder))

os.system(ln_sf)
pkgs = "i3-wm polybar rofi feh nbfc(optional_for_fans) kitty pamixer pipewire pulse neovim(nvchad)"
print(" You need to install these packages if you didn't:")
for pkg in pkgs.split(" "):
  print(pkg)

print("\nIf you don't need Automated internet conntection (via wpa_supplicant) or NBFC (Notebook Fan Control) you can remove it from i3 config.\nThey are at the end of the config.")

print(" * Also gruvbox folder doesn't actually have gruvbox. i am too lazy to change its name.")
