from sportradar import Tennis
import json

import pandas as pd

#h8w47gzf4ygv84jaa62jrb8k

tennis_obj = Tennis.Tennis("uzcb6y9ykvubwjcfw8rhrj2t")

# Get a list of all tournaments
daily_res_dict = tennis_obj.get_daily_results(2019,10,16).json()

#print(type(daily_results_json_response))
#daily_res_dict= json.loads(daily_results_json_response)

match_ids=[] 
for match in daily_res_dict["results"]:

    if match["coverage_info"]["detailed_serve_outcomes"] is True:
        match_ids.append(match["sport_event"]["id"])



print(len(match_ids))
dataset_li= []

i=0

for id in match_ids:
    if i>= 100:
        break
    try:
        statistics_dict= tennis_obj.get_match_summary(id).json()
        winner_id=statistics_dict["sport_event_status"]["winner_id"]
        stats_by_player_li= statistics_dict["statistics"]["teams"]
        player_A= stats_by_player_li[0]
        player_B= stats_by_player_li[1]
        
        if player_A["id"]== winner_id:
            output_winner= 1
        else:
            output_winner=-1

        player_A_stats= player_A["statistics"]
        player_B_stats= player_B["statistics"]

        ace_difference= player_A_stats["aces"]- player_B_stats["aces"]
        double_fault_difference= player_A_stats["double_faults"]- player_B_stats["double_faults"]
        total_breakpoints_difference= player_A_stats["total_breakpoints"]- player_B_stats["total_breakpoints"]
        first_serve_successful_percent_difference= player_A_stats["first_serve_successful"]- player_B_stats["first_serve_successful"]
        second_serve_successful_percent_difference= player_A_stats["second_serve_successful"]- player_B_stats["second_serve_successful"]

        row= [ace_difference, double_fault_difference,total_breakpoints_difference, first_serve_successful_percent_difference, second_serve_successful_percent_difference, output_winner]
        dataset_li.append(row)
        
    except:
        continue
    i+=1

print(dataset_li)

df = pd.DataFrame(dataset_li)

print("Saving the data...")
writer = pd.ExcelWriter('tennis_2019_10_16.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='welcome', index=False)
writer.save()




"""
[[1, -3, 7, 1], [-1, -2, -7, -1], [1, -1, 14, 1], [3, 11, -1, 1], [-1, -1, -7, -1], [-6, -3, -3, -1], [0, -4, 2, 1], [-1, 2, -5, -1], [3, 0, -1, 1], [-1, -6, 7, 1], [0, -2, 7, 1], [1, -4, 3, 1], [0, 1, -5, -1], [2, 2, 7, 1], [0, -4, -4, -1], [1, -1, 2, 1], [1, -12, -1, 1], [4, -6, 4, 1], [0, -1, -3, -1], [-2, 5, -3, -1], [1, -5, 8, 1], [0, 6, -2, -1], [1, 1, -3, 1], [0, 5, 0, 1], [0, 4, -6, -1], [4, -2, -9, 1], [5, 4, 0, 1], [-1, -2, -11, -1], [0, 0, 9, 1], [0, -5, -8, -1], [4, -6, 3, 1], [1, -1, -1, 1], [0, -3, 11, 1], [0, 0, -8, -1], [-2, -4, 2, 1], [0, 1, -1, -1], [1, -2, -3, 1], [-1, 0, -4, -1], [1, 7, -5, -1], [-2, 5, -7, -1], [3, 0, -3, 1], [1, -3, 3, 1], [3, -2, 5, 1], [0, -4, -2, 1], [-1, 2, 5, 1], [-1, 7, -2, -1], [2, -5, 6, 1], [-1, -1, -9, 1], [0, 2, 7, 1], [-1, -2, -10, -1], [-1, 3, -7, -1], [0, 0, -2, -1], [0, 3, -8, 1], [2, 2, -9, -1], [-1, -1, -8, -1], [2, 0, -5, -1], [2, 0, 6, 1], [0, 5, 4, -1], [0, -2, 5, -1], [-4, 1, 1, -1], [4, -2, 9, 1], [0, 9, -5, -1], [0, -5, 0, 1], [0, 1, 0, 1], [0, 3, -6, -1], [3, -1, 5, 1], [2, -3, -6, -1], [0, 3, -5, -1], [0, 1, -4, -1], [-3, 7, -11, -1], [-2, 0, -3, -1], [-1, -1, -3, -1], [-3, 1, -8, -1], [-1, 2, -1, 1], [-2, 5, -4, -1], [2, -5, -6, -1], [-3, 3, -7, -1], [-3, 1, 4, 1], [0, 1, 3, 1], [-1, 5, -2, -1]]
"""


