einwohner= {
            "Berlin": 3669491,
            "Hamburg": 1847253,
            "München": 1484226,
            "Köln": 1087863,
            "Frankfurt aM": 763380,
            "Stuttgart": 635911,
            "Düsseldorf": 621877,
            "Leipzig": 593145,
            "Dortmund": 588250,
            "Essen": 582760,
            "Bremen": 567559,
            "Dresden": 556780,
            "Hannover": 536925,
            "Nürnberg": 518370
            }
einwohner["Bonn"] = 350000



for k,v in sorted(einwohner.items()):   # Schleife mit key und value durch gesamtes Dict
    print(f"{k:16} {v:7}")

# for k in einwohner:   # Schleife nur mit key durch gesamtes Dict
#     print(k,einwohner[k])
