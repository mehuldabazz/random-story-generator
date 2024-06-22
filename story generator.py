import random

# Lists with expanded phrases
sentence_starters = [
    'About 100 years ago', 'In the 20 BC', 'Once upon a time', 'In the year 2100',
    'During the medieval times', 'Long, long ago in a distant land', 'On a stormy night',
    'In the ancient city of Babylon', 'On a warm summer evening', 'In the future, on a distant planet'
]
characters = [
    'there lived a king.', 'there was a man named Jack.', 'there lived a farmer.',
    'there was a brave knight.', 'there lived a wise old woman.', 'there was an adventurous young girl.',
    'there lived a curious scientist.', 'there was a humble blacksmith.', 'there lived a mysterious sorcerer.',
    'there was a clever merchant.', 'there lived a fearless explorer.', 'there was a cunning thief.',
    'there lived a legendary warrior.', 'there was a kind-hearted healer.'
]
times = [
    'One day', 'One full-moon night', 'Early one morning', 'On a windy afternoon', 'Just before dusk',
    'Late one evening', 'At the break of dawn', 'On a misty morning', 'During a thunderstorm', 'On a quiet night',
    'In the dead of night', 'At the height of summer', 'In the depths of winter', 'As the sun was setting'
]
story_plots = [
    'he was passing by', 'he was going for a picnic to', 'he decided to explore', 'he was on a quest to find',
    'he was journeying through', 'he stumbled upon', 'he was fleeing from', 'he was searching for',
    'he was heading towards', 'he was investigating', 'he was following a trail to', 'he got lost in',
    'he was leading a group towards', 'he was sent on a mission to'
]
places = [
    'the mountains', 'the garden', 'a dense forest', 'a deserted island', 'an ancient ruin', 'a bustling market',
    'a small village', 'the open sea', 'a mystical cave', 'a hidden valley', 'a forgotten temple', 
    'a haunted castle', 'a remote desert', 'a futuristic city', 'a snowy tundra'
]
second_characters = [
    'he saw a man', 'he saw a young lady', 'he encountered an old friend', 'he met a strange creature',
    'he found a lost child', 'he came across a talking animal', 'he discovered an injured soldier',
    'he was approached by a beggar', 'he saw a shadowy figure', 'he noticed a wandering minstrel', 
    'he ran into a mysterious stranger', 'he encountered a wise sage', 'he met a fellow traveler'
]
ages = [
    'who seemed to be in late 20s', 'who seemed very old and feeble', 'who looked very young and energetic',
    'who appeared to be middle-aged', 'who seemed ancient and wise', 'who looked like a teenager',
    'who was in his early 30s', 'who seemed to be in her early 40s', 'who appeared to be in his 50s',
    'who seemed to be in her late 60s', 'who looked ageless', 'who seemed to be in his prime'
]
works = [
    'searching something.', 'digging a well on roadside.', 'tending to a wounded animal.',
    'painting a beautiful landscape.', 'crafting a mysterious artifact.', 'reading an ancient manuscript.',
    'planting a tree.', 'building a small hut.', 'writing a letter.', 'cooking a delicious meal.',
    'studying the stars.', 'carving a statue.', 'playing a musical instrument.', 'sewing a garment.',
    'preparing a potion.', 'training a horse.'
]

# Function to generate a random story
def generate_story():
    sentence_starter = random.choice(sentence_starters)
    character = random.choice(characters)
    time = random.choice(times)
    story_plot = random.choice(story_plots)
    place = random.choice(places)
    second_character = random.choice(second_characters)
    age = random.choice(ages)
    work = random.choice(works)
    
    story = (f"{sentence_starter}, {character} {time}, {story_plot} {place}, {second_character} {age}, "
             f"{work} They talked for a while and decided to travel together. As they journeyed, they encountered "
             f"many challenges and made new friends. In the end, they discovered the true meaning of friendship and "
             f"bravery, and their adventures became the stuff of legends.")
    
    return story

# Generate and print a random story
print(generate_story())
