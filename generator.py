from PIL import Image
import os
import random
from collections import defaultdict

class NFTGenerator:
    def __init__(self, layers, rarity_weights, output_dir):
        self.layers = layers
        self.rarity_weights = rarity_weights
        self.output_dir = output_dir
        self.variation_counts = defaultdict(lambda: defaultdict(int))
        self.used_combinations = set()
        self.assets = self.preload_assets()
        
        os.makedirs(self.output_dir, exist_ok=True)

    def preload_assets(self):
        """Preload all assets into memory to speed up image generation."""
        assets = {}
        for layer in self.layers:
            layer_name = layer["name"]
            layer_path = layer["path"]
            files = os.listdir(layer_path)
            assets[layer_name] = {f: Image.open(os.path.join(layer_path, f)) for f in files}
        return assets

    def calculate_max_combinations(self):
        """Calculate the maximum number of unique NFTs that can be generated."""
        max_combinations = 1
        for layer in self.layers:
            max_combinations *= len(self.assets[layer["name"]])
        return max_combinations

    def select_random_asset(self, layer_name):
        """Select a random asset from a layer based on cumulative rarity weights."""
        files = list(self.assets[layer_name].keys())
        cumulative_weights = []
        current_weight = 0
        for f in files:
            current_weight += self.rarity_weights[layer_name].get(f, 1)
            cumulative_weights.append(current_weight)
        
        random_weight = random.uniform(0, cumulative_weights[-1])
        for i, weight in enumerate(cumulative_weights):
            if random_weight <= weight:
                chosen_file = files[i]
                break

        self.variation_counts[layer_name][chosen_file] += 1
        return chosen_file

    def generate_unique_combination(self):
        """Generate a unique combination of assets."""
        while True:
            combination = tuple(self.select_random_asset(layer["name"]) for layer in self.layers)
            if combination not in self.used_combinations:
                self.used_combinations.add(combination)
                return combination

    def generate_nft(self, nft_number):
        """Generate and save a single NFT."""
        base_image = None
        combination = self.generate_unique_combination()
        
        for i, layer in enumerate(self.layers):
            img = self.assets[layer["name"]][combination[i]]
            if base_image is None:
                base_image = img.copy()
            else:
                base_image.paste(img, (0, 0), img)
        
        base_image.save(os.path.join(self.output_dir, f"nft_{nft_number}.png"))
        print(f"Success! NFT {nft_number} generated using assets: {', '.join(combination)}")

    def generate_nfts(self, nft_count):
        """Generate multiple NFTs."""
        for i in range(nft_count):
            self.generate_nft(i + 1)

    def print_summary(self, nft_count):
        """Print the summary of the generation process."""
        print(f"{nft_count} NFTs have been generated and saved in {self.output_dir}")
        print("\nVariation Counts:")
        for layer, counts in self.variation_counts.items():
            print(f"{layer.capitalize()}:")
            for variation, count in counts.items():
                print(f"  {variation}: {count} times")
        
        print("\nRarity Weights Used:")
        for layer, weights in self.rarity_weights.items():
            print(f"{layer.capitalize()}:")
            for variation, weight in weights.items():
                print(f"  {variation}: weight {weight}")


# Configuration
layers = [
    {"name": "background", "path": "assets/backgrounds"},
    {"name": "body", "path": "assets/bodies"},
    {"name": "accessory", "path": "assets/accessories"},
]

rarity_weights = {
    "background": {"1.jpg": 10, "2.jpg": 3, "5.jpg": 1, "3.jpg": 3, "4.jpg": 3},
    "body": {"1-01.png": 10, "2-01.png": 2, "3-01.png": 6, "4-01.png": 1},
    "accessory": {"1-01.png": 10, "2-01.png": 4, "3-01.png": 2, "4-01.png": 1}
}

output_dir = r"E:\nft generator\output_nfts"

# Create NFT Generator instance
nft_generator = NFTGenerator(layers, rarity_weights, output_dir)

# Calculate and display the maximum number of NFTs that can be generated
max_nfts = nft_generator.calculate_max_combinations()
print(f"Maximum number of unique NFTs that can be generated: {max_nfts}")

# Number of NFTs to generate
nft_count = min(1000, max_nfts)  # Generate up to 1000 or the max possible

# Generate NFTs
nft_generator.generate_nfts(nft_count)

# Print summary
nft_generator.print_summary(nft_count)
