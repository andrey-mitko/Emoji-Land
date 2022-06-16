from generate_land import ask_for_number, generate_land
import os

os.makedirs("outputs", exist_ok=True)

output_cols = 65
output_rows = 42
output_noise_levels = [1, 5, 10, 20, 50, 100, 250, 500]


for nl in output_noise_levels:
    output = generate_land(output_cols, output_rows, nl)

    filename = os.path.join("outputs", f"test-{nl}.txt")

    with open(filename, "w") as f:
        f.write(output)
