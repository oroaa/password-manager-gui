from zxcvbn import zxcvbn

def analyze_pw(password: str):
    results = zxcvbn(password)

    responses = ["very weak", "very weak", "weak", "good", "strong"]

    result = [responses[results['score']], results['crack_times_display']['offline_slow_hashing_1e4_per_second']]

    # print("Password:", results['password'], "\nScore:", responses[results['score']],
    #       "\nEst. guesses needed to crack:", results['guesses'])
    # print("Estimated time to crack: ",
    #       results['crack_times_display']['offline_slow_hashing_1e4_per_second'])
    return result
