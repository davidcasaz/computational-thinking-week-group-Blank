def solution_station_5(name: str) -> int:
   
    lt = {
        1: ["Daeho","David","Kaisa","Oliver","Sara","Dan","Ivar","Lotte","Riya","Vassil",
            "Twan","Ester","Karolina","Lena","Margarita","Anna","Kien","Klaudia","Maliah","Todd"],
        2: ["Oumaima","Mathilde","Marie","Anita","Ziyan","Bernardo","Eleanor","Lorijn","Maria",
            "Younes","Yvan","Henning","Liangyu","Maciej","Toprak","Chris","GengXin","Mingze","Phoebe"],
        3: ["Betija","Haider","Kacper","Sophie","Amir","Baltasar","Isar","Jelle","Nicolas","David",
            "Ipek","Juan","Marfa","Maria","Alissa","Leopoldo","Mies","Jiaying","Kaixin","Mai","Sem","Tibbe"],
        4: ["Justus","Julia","Philip","Uli","Vanessa","Anna","Ekaterina","Thessa","Tongfei","Yang",
            "Benedikt","Jan","Nadee","Osjah","Tim","Eliana","Joana","Peilin","Pija","Wenhao"],
        5: ["Afua","Cristina","Greta","Jace","Laura","Anna","Bassant","Ivan","Juriaan","Kiavash"],
        6: ["Keitaro","Nohemi","Norina","Yifan","Yinan","Luo","Nikola","Olesya","Sophie","Tom"],
    }

    # Normalize the input
    key = name.strip().lower()

    # Find all team numbers that contain this name
    teams = [num for num, names in lt.items() if key in [n.lower() for n in names]]

    if not teams:
        raise ValueError(f"Name '{name}' not found in any learning team.")

    return min(teams)
