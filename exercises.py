scorpions = {"emperor", "red claw", "arizona", "forest", "fat tail"}
snakes = {"python", "cobra", "viper", "anaconda", "mamba"}
spiders = {"tarantula", "black widow", "wolf spider", "crab spider"}
vespas = {"yellowjacket", "hornet", "paper wasp"}

arachnids = spiders.union(scorpions)
print(sorted(arachnids))

arachnids1 = spiders | scorpions
print(sorted(arachnids1))
