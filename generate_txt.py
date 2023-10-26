import os
import random

# Set the path to the folder containing the files
folder_path = 'dataset'
train_ratio = 0.8  # 80% of the data for training
test_ratio = 0.1   # 10% of the data for testing
validation_ratio = 0.1  # 10% of the data for validation

# Get a list of all files in the folder
files = [file for file in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, file))]

# Calculate the number of files for each split
num_files = len(files)
num_train = 80 #int(train_ratio * num_files)
num_test = 10 #int(test_ratio * num_files)
num_validation = 10 #int(validation_ratio * num_files)

# Randomly shuffle the list of files
random.shuffle(files)

# Split the files into train, test, and validation sets
train_files = files[:num_train]
test_files = files[num_train:num_train + num_test]
validation_files = files[num_train + num_test:]

# Write file paths to respective text files
with open('train.txt', 'w') as train_file:
    train_file.write('\n'.join([os.path.join(folder_path, file) for file in train_files]))

with open('test.txt', 'w') as test_file:
    test_file.write('\n'.join([os.path.join(folder_path, file) for file in test_files]))

with open('validation.txt', 'w') as validation_file:
    validation_file.write('\n'.join([os.path.join(folder_path, file) for file in validation_files]))

print(f"Successfully segregated {num_train} files for training, {num_test} files for testing, and {num_validation} files for validation.")
