
import random
import string

code_lines = []

# Header
code_lines.append("# Random 1000-line Python program")
code_lines.append("import random")
code_lines.append("import string")
code_lines.append("import math")
code_lines.append("import time")
code_lines.append("")

# Math utilities
for i in range(50):
    code_lines.append(f"def math_util_{i}(x):")
    code_lines.append(f"    return math.sqrt(x) + {i}")
    code_lines.append("")

# String utilities
for i in range(50):
    code_lines.append(f"def string_util_{i}(s):")
    code_lines.append(f"    return s[::-1] + '{i}'")
    code_lines.append("")

# Mini games
for i in range(20):
    code_lines.append(f"def guess_game_{i}():")
    code_lines.append("    secret = random.randint(1, 10)")
    code_lines.append("    guess = -1")
    code_lines.append("    while guess != secret:")
    code_lines.append("        guess = random.randint(1, 10)")
    code_lines.append("    return 'Guessed it!'")
    code_lines.append("")

# Simulations
for i in range(20):
    code_lines.append(f"def simulate_{i}():")
    code_lines.append("    position = 0")
    code_lines.append("    for _ in range(100):")
    code_lines.append("        position += random.choice([-1, 1])")
    code_lines.append("    return position")
    code_lines.append("")

# Utility functions
for i in range(100):
    code_lines.append(f"def util_func_{i}(a, b):")
    code_lines.append(f"    return a + b + {i}")
    code_lines.append("")

# Dummy class
code_lines.append("class RandomClass:")
for i in range(50):
    code_lines.append(f"    def method_{i}(self, x):")
    code_lines.append(f"        return x * {i}")
    code_lines.append("")

# Main runner with calls
code_lines.append("def main():")
for i in range(50):
    code_lines.append(f"    print(math_util_{i}({i}))")
for i in range(50):
    code_lines.append(f"    print(string_util_{i}('hello'))")
for i in range(10):
    code_lines.append(f"    print(guess_game_{i}())")
for i in range(10):
    code_lines.append(f"    print(simulate_{i}())")
for i in range(10):
    code_lines.append(f"    print(util_func_{i}(1, 2))")
code_lines.append("    obj = RandomClass()")
for i in range(10):
    code_lines.append(f"    print(obj.method_{i}(5))")
code_lines.append("")

code_lines.append("if __name__ == '__main__':")
code_lines.append("    main()")

# Fill the rest with dummy functions
line_count = len(code_lines)
dummy_index = 0
while line_count < 1000:
    code_lines.append(f"def dummy_func_{dummy_index}():")
    code_lines.append(f"    return 'This is dummy line {dummy_index}'")
    code_lines.append("")
    dummy_index += 1
    line_count = len(code_lines)

# Save to file
output_path = "/mnt/data/random_1000_line_program.py"
with open(output_path, "w") as f:
    f.write("\n".join(code_lines))

output_path