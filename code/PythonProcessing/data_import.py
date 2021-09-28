import csv
import os

def import_benchmark_data(commit_file, result_directory):

    compression_speed = dict()
    decompression_speed = dict()
    labels = []

    with open(commit_file) as hash_file:
        for commit_hash in hash_file:
            # Check if a res file exists for this commit
            if not os.path.isfile(os.path.join(result_directory, commit_hash.strip() + ".res")):
                continue

            with open(os.path.join(result_directory, commit_hash.strip() + ".res")) as commit_file:
                reader = csv.reader(commit_file)
                labels.append(commit_hash)
                # Skip first 2 lines (Header and memcpy lines)
                next(reader)
                next(reader)

                for line in reader:
                    try:
                        compression_speed[line[0]].append(float(line[1]))
                        decompression_speed[line[0]].append(float(line[2]))
                    except KeyError:
                        compression_speed[line[0]] = [float(line[1])]
                        decompression_speed[line[0]] = [float(line[2])]
            # print(commit_hash.strip()+".res")

    return compression_speed, decompression_speed, labels