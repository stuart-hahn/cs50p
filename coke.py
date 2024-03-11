def main():
    total = 0
    while total < 50:
        print(f"Amount due: {50 - total}")
        coin = int(input("Insert coin: ").strip())
        if coin == 25 or coin == 10 or coin == 5:
            total += coin
        else:
            print("Invalid coin. Please enter 25, 10, or 5.")

    change = total - 50
    print(f"Change owed: {change}")


if __name__ == "__main__":
    main()
