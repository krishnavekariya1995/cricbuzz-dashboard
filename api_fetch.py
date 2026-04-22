import requests
import pandas as pd


def update_matches():

    url = "https://cricbuzz-cricket.p.rapidapi.com/matches/v1/live"

    headers = {
        "X-RapidAPI-Key": "b1b267883emshb7acfaa80c297dep15d0e2jsn827395f3b59c",
        "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    matches = []

    # Safely loop through API data
    for match_type in data.get("typeMatches", []):
        for series in match_type.get("seriesMatches", []):

            if "seriesAdWrapper" in series:
                for m in series["seriesAdWrapper"].get("matches", []):

                    matches.append({
                        "team1": m["matchInfo"]["team1"]["teamName"],
                        "team2": m["matchInfo"]["team2"]["teamName"],
                        "venue": m["matchInfo"]["venueInfo"]["ground"],
                        "city": m["matchInfo"]["venueInfo"]["city"]
                    })

    # Convert to DataFrame
    df = pd.DataFrame(matches)

    # Save to CSV (for deployment)
    df.to_csv("matches.csv", index=False)

    return df


# Optional: run file directly for testing
if __name__ == "__main__":
    df = update_matches()
    print(df.head())