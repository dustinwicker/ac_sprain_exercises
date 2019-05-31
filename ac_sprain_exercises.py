import os
import pandas as pd
from datetime import datetime as dt

##################################################################################
### Create exercise list with stetches, exercises, sets, reps, and weight used ###
##################################################################################

### Date of Creation: 1/22/2019 ###

# Change to appropriate directory
os.chdir('/Users/dustinwicker/PyCharmProjects/ac_sprain')

# List of tuples for stretches
stretches = [("Laying on affected side, elbow on surface with fingers sticking up - bring back of hand to ground", '3 x 30 sec'),
             ("Laying on affected side, elbow on surface with fingers sticking up - bring palm to ground", '3 x 30 sec'),
             ("Affected arm across front of body", '3 x 30 sec'),
             ("Affected arm behind head in triangle", '3 x 30 sec'),
             ("Arms up holding top of door frame leaning forward", '3 x 30 sec'),
             ("External rotation", '3 x 30 sec'),
             ("Behind the back external rotation", '5 x 30 sec')]

# Create DataFrame using list of tuples created above
stretches = pd.DataFrame(stretches, columns=['Stretch', 'Repetitions'])

# # Title of csv
# title_of_document = "AC Sprain Shoulder Exercises"
#
# # Create csv (append exercises to below)
# stretches.to_csv(title_of_document+".csv", sep=',', index=False)
#
# # List of tuples for exercises
# exercises = [("Pistons", "1 x 20", 5),
#              ("Small circles - CW", "1 x 10", 5),
#              ("Small circles - CCW", "1 x 10", 5),
#              ("Drop to side (make L)", "1 x 10", 5),
#              ("Row to the sky", "1 x 10", 5),
#              ("I", "1 x 10", 3),
#              ("Y", "1 x 10", 3),
#              ("T", "1 x 10", 3),
#              ("Progressive Resisted: Extension (Prone)", "2 x 10", 3),
#              ("Progressive Resisted: External Rotation (Side-Lying)", "2 x 10", 3),
#              ("Elbow Extension: Resisted", "2 x 10", 3),
#              ("Strengthening: Scaption with External Rotation (30° off the wall)", "2 x 10", 3),
#              ("Hammer curls", "1 x 20", 5),
#              ("Bicep curls", "1 x 20", 5),
#              ("Regular pushups", "2 x 10", '-'),
#              ("Regular pushups with weight in each hand - going up to 90°", "1 x 10 (each arm)", 10),
#              ("Lunge position - opposite knee to opposite shoulder", "1 x 10 (each side)", 10),
#              ("Reverse fly on pec deck (palms down)", "1 x 10", 40),
#              ("Reverse fly on pec deck (palms up)", "1 x 10", 40),
#              ("Incline Press", "2 x 10", 10),
#              ("Lat Pull Down", "1 x 10", 60),
#              ("Lat Pull Down - undergrip (bicep curl)", "1 x 10", 60),
#              ("Seated Machine Back Row (palms facing each other)", "2 x 10", 60),
#              ("Rebounder (modified - laying on ground and throwing ball in air)", "1 x 25", 4),
#              ("Dips", "1 x 15", "55 (Using assisted weight machine)"),
#              ("Chinups", "1 x 15", "55 (Using assisted weight machine)"),
#              ("Shake bar", "1", "60 secs"),
#              ("Planks on bosi ball", "5", '10 secs on, 10 secs off for 90 secs'),
#              ("Shrugs", "2 x 15", 'Black resistance band'),
#              ("Strengthening: Resisted Diagonal", "2 x 15", 'Black resistance band'),
#              ("Pull out-in", "2 x 10", 'Black resistance band'),
#              ("Arms straight out, going to sides", "2 x 10", 'Double black resistance band'),
#              ("Internal rotation", "2 x 10", 'Black resistance band'),
#              ("External rotation", "2 x 10", 'Black resistance band')]
#
# # Create dataframe from list of tuples
# exercises = pd.DataFrame(exercises, columns=['Exercise', 'Repetitions', 'Weight (lbs)/Resistance'])
# print(exercises)
#
# # Append exercises to created csv
# exercises.to_csv(title_of_document+".csv", sep=',', mode='a', index=False)
#
# # List of tuples for current exercises (3/26/19) and options to send to Stephanie
# exercises = [("Pistons", "1 x 20", 5, "1 x 25", 5, "1 x 20", 10),
#              ("Small circles - CW", "1 x 10", 5, "1 x 15", 5, "1 x 10", 10),
#              ("Small circles - CCW", "1 x 10", 5, "1 x 15", 5, "1 x 10", 10),
#              ("Drop to side (make L)", "1 x 10", 5, "1 x 15", 5, "1 x 10", 10),
#              ("Row to the sky", "1 x 10", 10, "2 x 10", 10, "1 x 15", 15),
#              ("I", "1 x 10", 5, "1 x 15", 5, "-", "-"),
#              ("Y", "1 x 10", 5, "1 x 15", 5, "-", "-"),
#              ("T", "1 x 10", 5, "1 x 15", 5, "-", "-"),
#              ("Progressive Resisted: Extension (Prone)", "2 x 10", 3, "3 x 10", 3, "-", "-"),
#              ("Progressive Resisted: External Rotation (Side-Lying)", "2 x 10", 5, "3 x 10", 5, "-", "-"),
#              ("Elbow Extension: Resisted", "2 x 10", 5, "3 x 10", 5, "-", "-"),
#              ("Strengthening: Scaption with External Rotation (30° off the wall)", "2 x 10", 3, "3 x 10", 3, "2 x 10", 5),
#              ("Hammer curls", "1 x 20", 10, "1 x 25", 10, "1 x 20", 15),
#              ("Bicep curls", "1 x 20", 10, "1 x 25", 10, "1 x 20", 15),
#              ("Regular pushups", "3 x 10", '-', "3 x 15", '-', "-", "-"),
#              ("Regular pushups with weight in each hand - going up to 90°", "1 x 10 (each arm)", 10, "1 x 15 (each arm)", 10, "1 x 10 (each arm)", 15),
#              ("Lunge position - opposite knee to opposite shoulder", "1 x 10 (each side)", 10, "1 x 15 (each side)", 10, "1 x 10 (each side)", 15),
#              ("Reverse fly on pec deck (palms down)", "1 x 10", 50, "2 x 10", 50, "1 x 10", 60),
#              ("Reverse fly on pec deck (palms up)", "1 x 10", 50, "2 x 10", 50, "1 x 10", 60),
#              ("Incline Press", "2 x 10", 10, "2 x 15", 15, "3 x 10", 10),
#              ("Lat Pull Down", "1 x 10", 75, "2 x 10", 75, "1 x 10", 85),
#              ("Lat Pull Down - undergrip (bicep curl)", "1 x 10", 75, "2 x 10", 75, "1 x 10", 85),
#              ("Seated Machine Back Row (palms facing each other)", "2 x 10", 75, "3 x 10", 75, "2 x 10", 85),
#              ("Rebounder (modified - laying on ground and throwing ball in air)", "1 x 25", 4, "1 x 25", 6, "-", "-"),
#              ("Dips", "1 x 15", "70 (Using assisted weight machine)", "2 x 15", "70 (Using assisted weight machine)",
#                       "1 x 15", "80 (Using assisted weight machine)"),
#              ("Chinups", "1 x 15", "70 (Using assisted weight machine)", "2 x 15", "70 (Using assisted weight machine)",
#                       "1 x 15", "80 (Using assisted weight machine)"),
#              ("Shake bar", "1", "60 secs", "1", "120 secs", "1", "180 secs"),
#              ("Planks on bosi ball", "5", '10 secs on, 10 secs off for 90 secs', "5", '20 secs on, 10 secs off for 140 secs',
#                       "10", '10 secs on, 10 secs off for 190 secs'),
#              ("Shrugs", "2 x 15", 'Black resistance band', "3 x 15", 'Black resistance band', "-", "-"),
#              ("Strengthening: Resisted Diagonal", "2 x 15", 'Black resistance band', "3 x 15", 'Black resistance band', "-", "-"),
#              ("Pull out-in", "2 x 10", 'Black resistance band', "3 x 10", 'Black resistance band', "-", "-"),
#              ("Arms straight out, going to sides", "2 x 10", 'Double black resistance band', "3 x 10", 'Double black resistance band', "-", "-"),
#              ("Internal rotation", "2 x 10", 'Black resistance band', "3 x 10", 'Black resistance band', "-", "-"),
#              ("External rotation", "2 x 10", 'Black resistance band', "3 x 10", 'Black resistance band', "-", "-")]
#
# # Create dataframe from list of tuples
# exercises = pd.DataFrame(exercises, columns=['Exercise', 'Current Repetitions', 'Current Weight (lbs)/Resistance',
#                                              'Option A Repetitions', 'Option A Weight (lbs)/Resistance',
#                                              'Option B Repetitions', 'Option B Weight (lbs)/Resistance'])

# 4/8/2019 - advised I was ready to make increases delineated in red on AC Sprain Shoulder Exercise Adjustment Options.xlsx
# 5/31/2019 - updated reps and weights to various exercises
# List of tuples for exercises
exercises = [("Pistons","1 x 25", 5),
             ("Small circles - CW", "1 x 15", 10),
             ("Small circles - CCW", "1 x 15", 10),
             ("Drop to side (make L)", "1 x 15", 10),
             ("Row to the sky", "2 x 10", 10),
             ("I", "1 x 15", 5),
             ("Y", "1 x 15", 5),
             ("T", "1 x 15", 5),
             ("Progressive Resisted: Extension (Prone)", "3 x 10", 3),
             ("Progressive Resisted: External Rotation (Side-Lying)", "3 x 10", 5),
             ("Elbow Extension: Resisted", "3 x 10", 5),
             ("Strengthening: Scaption with External Rotation (30° off the wall)", "3 x 10", 3),
             ("Hammer curls", "1 x 20", 20),
             ("Bicep curls", "1 x 20", 20),
             ("Regular pushups", "3 x 15", '-'),
             ("Regular pushups with weight in each hand - going up to 90°", "1 x 15 (each arm)", 10),
             ("Lunge position - opposite knee to opposite shoulder", "1 x 15 (each side)", 10),
             ("Reverse fly on pec deck (palms down)", "3 x 10", 50),
             ("Reverse fly on pec deck (palms up)", "3 x 10", 50),
             ("Incline Press", "3 x 10", 15),
             ("Lat Pull Down", "3 x 10", 85),
             ("Lat Pull Down - undergrip (bicep curl)", "3 x 10", 85),
             ("Seated Machine Back Row (palms facing each other)", "3 x 10", 85),
             ("Rebounder (modified - laying on ground and throwing ball in air)", "1 x 25", 6),
             ("Dips", "2 x 15", "75 (Using assisted weight machine)"),
             ("Chinups", "2 x 15", "75 (Using assisted weight machine)"),
             ("Shake bar", "1", "180 secs"),
             ("Planks on bosi ball", "5", '20 secs on, 10 secs off for 140 secs'),
             ("Shrugs", "3 x 15", 'Black resistance band'),
             ("Strengthening: Resisted Diagonal", "3 x 15", 'Black resistance band'),
             ("Pull out-in", "3 x 10", 'Black resistance band'),
             ("Arms straight out, going to sides", "3 x 10", 'Double black resistance band'),
             ("Internal rotation", "3 x 10", 'Black resistance band'),
             ("External rotation", "3 x 10", 'Black resistance band')]

# Create dataframe from list of tuples
exercises = pd.DataFrame(exercises, columns=['Exercise', 'Repetitions', 'Weight (lbs)/Resistance'])

### Write stretches and exercises to excel sheet ###
# Title of document
title_of_document = "AC Sprain Shoulder Stretches and Exercises " + dt.today().strftime("%Y.%m.%d") +".xlsx"

# Create ExcelWriter with path and appropriate engine to write DataFrame objects into excel sheets
writer = pd.ExcelWriter(path= title_of_document, engine= "openpyxl")

# Write stretches to excel sheet
stretches.to_excel(writer, index=False)

# Write exercies to excel sheet below stretches
exercises.to_excel(writer, startrow=len(stretches)+2, index=False)

# Save created object to current directory
writer.save()