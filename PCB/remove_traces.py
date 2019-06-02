
def good(line):
    if ("segment" in line and "0.2159" in line) or "via" in line:
            for i in range(166, 222):
                if "net " + str(i) in line:
                    return False
    return True


filename = "K-Type_original.kicad_pcb"
output_filename = "K-Type.kicad_pcb"
with open(filename) as file:
    with open(output_filename, "w+") as output_file:
        for line in file:
            if good(line):
                output_file.write(line)
