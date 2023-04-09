import undetected_chromedriver as uc


if __name__ == "__main__":
    trial = uc.Chrome()
    # trial.get("https://www.google.com")
    print(type(trial))