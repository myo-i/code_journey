import re
import os
FILE_PATH = "変換したJavaファイルのパス"
patternfilename = re.compile("public class (K+(A|B|C|D|J|Z|))(\S+) implements CobolRunnable")
patterncall = re.compile("b_RETURN_CODE.set\s\(call_(\w+).run\s\((.+)\)\);")



def main():
    # for fd_path, sb_folder, sb_file in os.walk('depget'):
    #     for fol in sb_folder:
    #         run(fd_path + '\\' + fol + '\\' + fol + ".java")
    run(FILE_PATH)


def run(FILE_PATH):
    with open(FILE_PATH, "r") as f:
        lines = f.readlines()
        count = 0
        nameargsdict = {}

        for index, line in enumerate(lines, start = 1):

            match = re.search(patternfilename, line)
            if match:
                group = match.group(1)
                importpack = f"package {group};\n"



            if "CobolModule.getCurrentModule ().clearParameter ();" in line:
                lines[index-1] = "<---- DELETE ---->\n"

            if "throw new CobolRuntimeException(cce);" in line:
                lines[index] = "INSERT RUN\n"


            # return  0:"filename1&args1, args2...", 1:"filename2&args1, args2..."
            match = re.search(patterncall, line)
            if match:
                filename = match.group(1) + "&" + match.group(2)
                nameargsdict.setdefault(count, filename)
                count += 1

        lines.insert(0, importpack)

        delete_sign(lines)

        # runを代入
        assign_run(lines, nameargsdict)
    
        # ファイル書き込み
        with open(FILE_PATH, "w") as f:
            f.writelines(lines)


        print(FILE_PATH)


def delete_sign(lines):
    for index, line in enumerate(lines, start=1):
        if "<---- DELETE ---->" in line:
            testindex = index
            while not "INSERT RUN" in line:
                lines[testindex-1] = ""
                line = lines[testindex]
                testindex += 1


# runを代入
def assign_run(lines, nameargsdict):
    keycount = 0
    for index, line in enumerate(lines):
        if "INSERT RUN" in line:
            valuelists = nameargsdict[keycount].split("&")
            keycount += 1

            runstatement = f"new {valuelists[0]}().run({valuelists[1]});\n"
            lines[index] = runstatement.rjust(len(runstatement) + 12)


if __name__ == "__main__":
    main()
