def readingfile(path_to_file):
    """Reads a text file and returns product details in expected format."""
    item_list = []

    try:
        with open(path_to_file, "r") as f:
            for line in f:
                parts = line.strip().split(", ")
                if len(parts) == 5:
                    item = {
                        "name": parts[0],
                        "brand": parts[1],
                        "quantity": int(parts[2]),
                        "cost_price": float(parts[3]),
                        "origin": parts[4]
                    }
                    item_list.append(item)
        return item_list

    except FileNotFoundError:
        print(f"File not found: {path_to_file}")
        return []
    except Exception as err:
        print("Something went wrong while reading the file:", err)
        return []
