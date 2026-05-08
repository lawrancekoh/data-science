#!/usr/bin/env python3
"""Data loading utilities for the 06 Fake News Detection project.
Downloads and caches datasets from Kaggle to make the project self-contained.
"""

import os
import json
import shutil
from pathlib import Path

# Check if kaggle is available
try:
    import kaggle
    KAGGLE_AVAILABLE = True
except ImportError:
    KAGGLE_AVAILABLE = False

# Project configuration
PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / "{data_dir}"
RAW_DIR = PROJECT_ROOT / "data/raw"
PROCESSED_DIR = PROJECT_ROOT / "data/processed"

# Create data directories if they don't exist
DATA_DIR.mkdir(parents=True, exist_ok=True)
RAW_DIR.mkdir(parents=True, exist_ok=True)
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

class KaggleDatasetDownloader:
    def __init__(self, dataset_name, kaggle_slug, files_to_download):
        self.dataset_name = dataset_name
        self.kaggle_slug = kaggle_slug
        self.files_to_download = files_to_download
        self.cache_file = RAW_DIR / ".{info['dataset_name'].replace(' ', '_')}_cache.json"

    def check_cache(self):
        """Check if dataset is already cached."""
        if self.cache_file.exists():
            with open(self.cache_file, 'r') as f:
                cache = json.load(f)
            current_files = {{}}
            for fname in self.files_to_download:
                fpath = RAW_DIR / fname
                if fpath.exists():
                    current_files[fname] = os.path.getmtime(fpath)
            
            if set(current_files.keys()) == set(cache.get('files', [])):
                all_match = True
                for fname, mtime in cache.get('files', []):
                    if fname in current_files:
                        if abs(current_files[fname] - mtime) > 1:
                            all_match = False
                            break
                if all_match:
                    print(f"✅ {{self.dataset_name}} is already cached.")
                    return True
        return False

    def download_dataset(self):
        """Download dataset from Kaggle."""
        if not KAGGLE_AVAILABLE:
            raise ImportError("Kaggle API is not available. Please install it with 'pip install kaggle'.")
        
        try:
            kaggle.api.dataset_download_files(
                self.kaggle_slug,
                path=str(RAW_DIR),
                unzip=True,
                quiet=False
            )
            print(f"✅ Downloaded {self.dataset_name} from Kaggle.")
            
            # Update cache
            cache_info = {{
                'files': [],
                'downloaded_at': str(datetime.now())
            }}
            for fname in self.files_to_download:
                fpath = RAW_DIR / fname
                if fpath.exists():
                    cache_info['files'].append({{
                        'name': fname,
                        'mtime': os.path.getmtime(fpath)
                    }})
            with open(self.cache_file, 'w') as f:
                json.dump(cache_info, f, indent=2)
                
        except Exception as e:
            print(f"❌ Error downloading dataset: {e}")
            raise

def load_covid_data():
    """
    Load COVID-19 dataset from Our World in Data.
    Returns: pandas DataFrame
    """
    import pandas as pd
    
    downloader = KaggleDatasetDownloader(
        dataset_name="Our World in Data - COVID-19",
        kaggle_slug="caesarmario/our-world-in-data-covid19-dataset",
        files_to_download=["owid-covid-data.csv", "OWID_data-descriptions.md", "world_in_data_covid19_tests.csv"]
    )
    
    if not downloader.check_cache():
        print("Downloading COVID-19 dataset...")
        downloader.download_dataset()
    
    filepath = RAW_DIR / "owid-covid-data.csv"
    if not filepath.exists():
        raise FileNotFoundError("COVID-19 dataset file not found after download. Please check the raw data directory.")
    
    df = pd.read_csv(filepath)
    print(f"✅ Loaded COVID-19 dataset: {len(df)} rows, {len(df.columns)} columns")
    return df

if __name__ == "__main__":
    try:
        df = load_covid_data()
        print(df.head())
    except Exception as e:
        print(f"Error: {e}")
