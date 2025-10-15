import numpy as np
import itertools
import time

# --- Part 0: User Configuration ---
print("--- Alien Affinity Analysis Setup ---")
# 1- Enable user to input the number of rows (records)
while True:
    try:
        rows_input = input("Enter the number of records (default: 5000): ")
        if rows_input == "":
            num_records = 5000
            break
        num_records = int(rows_input)
        if num_records > 0:
            break
        else:
            print("Please enter a positive number.")
    except ValueError:
        print("Invalid input. Please enter a whole number.")

# 2- Enable user to input the number of columns (features)
while True:
    try:
        cols_input = input("Enter the number of features (default: 6): ")
        if cols_input == "":
            num_features = 6
            break
        num_features = int(cols_input)
        if num_features > 1:
            break
        else:
            print("Please enter a number greater than 1.")
    except ValueError:
        print("Invalid input. Please enter a whole number.")

print("-" * 35 + "\n")

# --- Main Loop to Guarantee a Result ---
# 3- Run in a loop until at least one rule is found
iteration_count = 0
while True:
    iteration_count += 1
    print(f"--- Attempt #{iteration_count}: Generating and Analyzing Dataset ---")

    # --- Part 1: Generate the Alien Dataset ---
    # Dynamically generate feature names and probabilities if defaults are not used
    if num_features == 6 and cols_input == "":
        feature_names = [
            'Has Tentacles', 'Is Green', 'Bioluminescent',
            'Telepathic', 'Armored Skin', 'Flies'
        ]
        probabilities = [0.7, 0.6, 0.55, 0.4, 0.3, 0.2]
    else:
        feature_names = [f'Feature_{i}' for i in range(num_features)]
        # Generate a descending list of probabilities for more interesting data
        base_probs = np.linspace(0.8, 0.15, num_features)
        probabilities = np.round(np.sort(base_probs)[::-1], 2)

    aliens_dataset = np.zeros((num_records, num_features), dtype=int)
    for i in range(num_features):
        random_values = np.random.rand(num_records)
        aliens_dataset[:, i] = (random_values < probabilities[i]).astype(int)
    
    print(f"Dataset with {num_records} records and {num_features} features created.")

    # --- Part 2: Affinity Analysis Logic ---
    support_threshold = 0.30
    confidence_threshold = 0.70

    all_rules = []
    filtered_rules = []
    feature_indices = list(range(num_features))

    for itemset_size in range(2, num_features + 1):
        for itemset in itertools.combinations(feature_indices, itemset_size):
            itemset = list(itemset)
            itemset_support_count = np.sum(np.all(aliens_dataset[:, itemset], axis=1))
            itemset_support = itemset_support_count / num_records
            
            if itemset_support >= support_threshold:
                for i in range(1, len(itemset)):
                    for antecedent in itertools.combinations(itemset, i):
                        antecedent = list(antecedent)
                        consequent = [item for item in itemset if item not in antecedent]

                        antecedent_support_count = np.sum(np.all(aliens_dataset[:, antecedent], axis=1))
                        if antecedent_support_count == 0:
                            continue

                        confidence = itemset_support_count / antecedent_support_count
                        
                        consequent_support_count = np.sum(np.all(aliens_dataset[:, consequent], axis=1))
                        if consequent_support_count == 0:
                            lift = 0
                        else:
                            consequent_support = consequent_support_count / num_records
                            lift = confidence / consequent_support
                        
                        rule_data = {
                            "antecedent": antecedent,
                            "consequent": consequent,
                            "support": itemset_support,
                            "confidence": confidence,
                            "lift": lift
                        }
                        all_rules.append(rule_data)
                        
                        if confidence >= confidence_threshold:
                            filtered_rules.append(rule_data)
    
    # Check if we found any rules. If so, break the main loop.
    if len(filtered_rules) > 0:
        print(f"Success! Found {len(filtered_rules)} rule(s) in attempt #{iteration_count}.\n")
        break
    else:
        print("No rules met the criteria. Regenerating dataset and trying again...\n")
        time.sleep(1) # Pause briefly to allow user to read the message

# --- Part 3: Display Results in a Table ---
print("--- FINAL ANALYSIS RESULTS ---")
print(f"Filtered Rules (Support > {support_threshold*100:.0f}% AND Confidence > {confidence_threshold*100:.0f}%):")
header = f"{'Rule':<45} {'Support (%)':<15} {'Confidence (%)':<18} {'Lift'}"
print("-" * 100)
print(header)
print("=" * 100)

for rule in filtered_rules:
    antecedent_names = ', '.join([feature_names[i] for i in rule['antecedent']])
    consequent_names = ', '.join([feature_names[i] for i in rule['consequent']])
    rule_str = f"{antecedent_names} -> {consequent_names}"
    
    support_str = f"{rule['support'] * 100:.2f}"
    confidence_str = f"{rule['confidence'] * 100:.2f}"
    lift_str = f"{rule['lift']:.2f}"
    
    row = f"{rule_str:<45} {support_str:<15} {confidence_str:<18} {lift_str}"
    print(row)

print("-" * 100)
print(f"Total rules found: {len(filtered_rules)}\n")


print("\nAll combinations from popular itemsets (for reference):")
print("-" * 100)
print(header)
print("=" * 100)

for rule in all_rules:
    antecedent_names = ', '.join([feature_names[i] for i in rule['antecedent']])
    consequent_names = ', '.join([feature_names[i] for i in rule['consequent']])
    rule_str = f"{antecedent_names} -> {consequent_names}"
    
    support_str = f"{rule['support'] * 100:.2f}"
    confidence_str = f"{rule['confidence'] * 100:.2f}"
    lift_str = f"{rule['lift']:.2f}"
    
    row = f"{rule_str:<45} {support_str:<15} {confidence_str:<18} {lift_str}"
    print(row)
print("-" * 100)
