# NFT Generator

This project is a Python-based NFT generator that creates unique NFT images by combining different layers of assets. It includes functionality for rarity weighting and ensures that no duplicate NFTs are generated.
##Features

    Efficient Image Generation: Preloads assets to memory for faster NFT generation.
    Rarity Weighting: Supports custom rarity weights for each asset, making some assets more common than others.
    Unique Combinations: Ensures that each NFT generated is unique by tracking used combinations.
    Customizable Layers: Easily configure different layers (e.g., background, body, accessories) and their respective assets.

## Project Structure


nft-generator/
│
├── assets/                     # Directory containing asset layers
│   ├── backgrounds/            # Background images
│   ├── bodies/                 # Body images
│   └── accessories/            # Accessory images
│
├── output_nfts/                # Directory where generated NFTs are saved
│
├── nft_generator.py            # Main NFT generator script
│
└── README.md                   # Project documentation

## Getting Started
### Prerequisites

    Python 3.6+

    Pillow Library: Used for image manipulation.

    Install via pip:

    bash

    pip install pillow

### Setup

    Clone the Repository

    bash

git clone https://github.com/Avishka-Udara/nft-generator.git
cd nft-generator

Organize Assets

Place your image assets into the appropriate subdirectories within the assets/ folder:

    backgrounds/
    bodies/
    accessories/

Ensure that the filenames match those used in the rarity_weights dictionary in nft_generator.py.

Run the NFT Generator

Open the nft_generator.py file and customize the configuration, including layer paths, rarity weights, and the number of NFTs to generate.

Run the script:

bash

    python nft_generator.py

## Example Configuration


layers = [
    {"name": "background", "path": "assets/backgrounds"},
    {"name": "body", "path": "assets/bodies"},
    {"name": "accessory", "path": "assets/accessories"},
]

rarity_weights = {
    "background": {"1.jpg": 5, "2.jpg": 3, "5.jpg": 1, "3.jpg": 3, "4.jpg": 3},
    "body": {"1-01.png": 4, "2-01.png": 2, "3-01.png": 6, "4-01.png": 1},
    "accessory": {"1-01.png": 7, "2-01.png": 4, "3-01.png": 2, "4-01.png": 1}
}

This setup will generate NFTs by combining random assets from each layer, taking into account the specified rarity weights.


## Output

Generated NFTs will be saved in the output_nfts/ directory. The console will print information about each generated NFT and a summary of the process.

### Customization

    Adding New Layers: You can add new layers by creating additional directories under assets/ and updating the layers list in nft_generator.py.
    Adjusting Rarity: Modify the rarity_weights dictionary to change the likelihood of each asset being selected.

### Contributing

Contributions are welcome! Please fork the repository and submit a pull request for review.

### License

This project is licensed under the MIT License - see the LICENSE file for details.

### Contact

For any questions or issues, feel free to contact me via avishkaudara123@gmail.com
