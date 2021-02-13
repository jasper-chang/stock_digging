import stockmining.datautils as sd


if __name__ == "__main__":
    print(sd.authentication.get_token(max_try=10))
    # token = sm.get_token(max_try=10)
    # print(token)