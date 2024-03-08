def main():
    filename = input("name: ").strip().lower()
    get_extension(filename)


def get_extension(filename):

    extension = filename.split(".")[-1]

    match extension:
        case "gif" | "jpg" | "jpeg" | "png":
            print(f"image/{extension}")
        case "pdf" | "zip":
            print(f"application/{extension}")
        case "txt":
            print("text/plain")
        case _:
            print("application/octet-stream")


main()
