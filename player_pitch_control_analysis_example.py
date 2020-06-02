"""
In this file, we provide examples of how to use the tools developed in PlayerEventAnalysis.py

This file looks at event 820 of the Metrica data, and generates the following plots
    1. The space generated by the off ball movement of Away Player 19
    2. The space captured by Away Player 19
    3. The amount of pitch control that would be gained and lost by moving Away Player 19 10 meters
        towards the center of the pitch
    4. The optimal velocity vector of Away Player 19 after fitting a Bayesian Optimization with an assumed
        maximum speed
    5. The optimal velocity vector and location of Away Player 19 after fitting a Bayesian Optimization with an assumed
        maximum speed, and a maximum distance from the current location
    6. The space generated by the off ball movement of Home Player
    7. The space captured by Home Player 4
    8. The amount of pitch control that would be gained and lost by moving Home Player 4 5 meters
        towards the center of the pitch
    9. The optimal velocity vector of Home Player 4 after fitting a Bayesian Optimization with an assumed
        maximum speed
    10. The optimal velocity vector and location of Home Player 4 after fitting a Bayesian Optimization with an assumed
        maximum speed, and a maximum distance from the current location

In addition, we also calculate the amount of space created in each of those 10 scenarios.
"""

# I don't usually recommend using import *, so be careful in the future when using this
import data_setup as data
import matplotlib.pyplot as plt
from PlayerEventAnalysis import PlayerEventAnalysis

# We will generate space creation and plots for one player on both teams

# region Away Player 19 analysis
common_kw_args = {
    "tracking_home": data.tracking_home,
    "tracking_away": data.tracking_away,
    "params": data.params,
    "events": data.events,
    "event_id": 820,
    "gk_numbers": data.GK_numbers,
    "field_dimens": (106.0, 68.0),
    "n_grid_cells_x": 50,
}

example_player_analysis_away = PlayerEventAnalysis(
    **common_kw_args, team_player_to_analyze="Away", player_to_analyze=19,
)

# Let's look at some outputs for making the player's movement stationary

# First, let's look at the amount of space the player created with his/her off ball run
print(
    example_player_analysis_away.team_player_to_analyze
    + " Player "
    + str(example_player_analysis_away.player_to_analyze)
    + " created "
    + str(
        int(
            example_player_analysis_away.calculate_space_created(
                replace_function="movement", replace_x_velocity=0, replace_y_velocity=0
            )
        )
    )
    + " m^2 of space with his movement during event "
    + str(example_player_analysis_away.event_id)
)

# Now, let's plot the space created and conceded by his run
example_player_analysis_away.plot_pitch_control_difference(
    replace_function="movement", replace_x_velocity=0, replace_y_velocity=0
)
plt.show()

# Let's look at the space the player is gaining by being on the right wing
print(
    example_player_analysis_away.team_player_to_analyze
    + " Player "
    + str(example_player_analysis_away.player_to_analyze)
    + " occupied "
    + str(
        int(
            example_player_analysis_away.calculate_space_created(
                replace_function="presence"
            )
        )
    )
    + " m^2 of space during event "
    + str(example_player_analysis_away.event_id)
)

# And plot this space on the pitch:

example_player_analysis_away.plot_pitch_control_difference(replace_function="presence")
plt.show()


# Now, let's examine what would happen if we moved the player 10 meters towards the middle of the pitch
print(
    example_player_analysis_away.team_player_to_analyze
    + " Player "
    + str(example_player_analysis_away.player_to_analyze)
    + " would have occupied a difference of "
    + str(
        int(
            -1
            * example_player_analysis_away.calculate_space_created(
                replace_function="location", relative_x_change=0, relative_y_change=10
            )
        )
    )
    + " m^2 of space during event "
    + str(example_player_analysis_away.event_id)
    + " if they were 10 meters towards the center of the pitch"
)

# And let's plot this difference graphically:
example_player_analysis_away.plot_pitch_control_difference(
    replace_function="location", relative_x_change=0, relative_y_change=10
)
plt.show()

# Finally, let's take a stab at trying to determine the optimal location and velocity vector for the given player
example_player_analysis_away.get_optimal_location_on_pitch(
    size_of_grid=20, location_trials=100, velocity_trials=25, max_velocity=5
)

example_player_analysis_away.get_optimal_location_on_pitch(
    location_trials=0, velocity_trials=50, max_velocity=12
)

# endregion

# region Home Player 4
# Let's do the same analysis for Home Player 4:
example_player_analysis_home = PlayerEventAnalysis(
    **common_kw_args, team_player_to_analyze="Home", player_to_analyze=4,
)

# Let's calculate the amount of space the player is gaining by running towards his own goal

print(
    example_player_analysis_home.team_player_to_analyze
    + " Player "
    + str(example_player_analysis_away.player_to_analyze)
    + " created "
    + str(
        int(
            example_player_analysis_home.calculate_space_created(
                replace_function="movement", replace_x_velocity=0, replace_y_velocity=0
            )
        )
    )
    + " m^2 of space with his movement during event "
    + str(example_player_analysis_home.event_id)
)

# And plot the space gained and conceded:

example_player_analysis_home.plot_pitch_control_difference(
    replace_function="movement", replace_x_velocity=0, replace_y_velocity=0
)
plt.show()

# Overall space creation analysis:

print(
    example_player_analysis_home.team_player_to_analyze
    + " Player "
    + str(example_player_analysis_home.player_to_analyze)
    + " occupied "
    + str(
        int(
            example_player_analysis_home.calculate_space_created(
                replace_function="presence"
            )
        )
    )
    + " m^2 of space during event "
    + str(example_player_analysis_home.event_id)
)

# And plot this space on the pitch:

example_player_analysis_home.plot_pitch_control_difference(replace_function="presence")
plt.show()

# Let's see what happens if we move this defender 5 meters closer to Forward 23:

print(
    example_player_analysis_home.team_player_to_analyze
    + " Player "
    + str(example_player_analysis_home.player_to_analyze)
    + " would have occupied a difference of "
    + str(
        int(
            -1
            * example_player_analysis_home.calculate_space_created(
                replace_function="location", relative_x_change=0, relative_y_change=5
            )
        )
    )
    + " m^2 of space during event "
    + str(example_player_analysis_home.event_id)
    + " if they were 5 meters towards the center of the pitch"
)

example_player_analysis_home.plot_pitch_control_difference(
    replace_function="location", relative_x_change=0, relative_y_change=5
)
plt.show()

# Plot optimal location and velocity vector
example_player_analysis_home.get_optimal_location_on_pitch(
    size_of_grid=20, location_trials=100, velocity_trials=25, max_velocity=5
)

# Plot optimal velocity vector
example_player_analysis_home.get_optimal_location_on_pitch(
    location_trials=0, velocity_trials=50, max_velocity=5
)
# endregion