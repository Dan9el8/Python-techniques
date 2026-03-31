def matching_statement():
    match lights:
    case "red":
    print("Stop")

    case "green":
    print("go")

    case("yellow"):
    print("wait")

    case _:
    raise RuntimeError