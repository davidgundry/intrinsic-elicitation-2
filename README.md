# Intrinsic Elicitation, Experiment 2

Intrinsic Elicitation Experiment 2: Enjoyment and data quality in a game for human-subject data collection

This is a repository of materials and data for the Enjoyment and Data Collection in an Applied Game study.

## Directory Structure

* `data/` - processed/anonymised data
* `out/` - output of analysis scripts including data and graphs. Logs of script console output is saved here too
* `python/` - python scripts
* `r/` - r scripts
* `design/` - ethics, preregistration documents, etc.
* `final/` - versions of documents that have been officially submitted somewhere
* `materials/` - contains materials that were used in the experiment
* `design/` - ethics and preregistration documents
* `img/` - screenshots and video figures

## Pre-Registration

Pre-registration documents are found in `design/`. Dated uploads to OSF (which should match the records on OSF) are in `final/`. The power analysis script used in the pre-registration can be found in `r/`, which generated `out/power-anaysis.Rout`. You can generate this using the following command:

    R CMD BATCH --quiet r/power-analysis.r out/power-analysis.Rout

### Why 16 inputs?

Looking at the data from experiment 1, we found the game condition had slower input times. We found the value of 2.5 standard deviations above the mean for this group (above which you'd expect only approximately 0.6% of the data). This was equivalent to 29.5 seconds per input. Over 8 minutes this works out to 16.25 inputs. Rounding down gives 16 inputs over 8 minutes. 

## Data Collection

Data collection began at 14:35 on 15 Feb 2021 and ended at 19:40.

10 participant records were collected to ensure everything was functioning as it should. It was found that the average completion time was greater than 10 minutes. Before continuing, the study duration (time paid to participants) was increased to 12 minutes at £6:00 per hour = £1.20 A bonus payment of £0.20 was given to the original 10 participants.

Due to unexpectedly high number of exclusions (<16 moves and bugs), we ended up recruiting 35 more participants than originally planned. At 185 participants we ran out of money for the study. This meant we had not achieved our target sample size of at least 68 in each condition. We had 67 (a subsequent removal due to a participant returning their data reduced this to 66). 

* 185 submission recorded on Prolific (A further 26 participants began the study but returned their submission without submitting data, 1 participant returned their submission after submitting data. 6 participants timed out)
* 181 records retrieved from database (as there were 4 NOCODE submissions, presumably these were the missing records)
* Of these 1 returned their submission on Prolific even though it had been correctly submitted. This was removed before processing.
* 180 records were processed.

During (automated) processing:

* 0 participants were excluded due to missing prolific ids
* 9 were excluded from data because of language set to "other". As this would make them more identifiable in the final data (and they cannot be used for the analysis), they are not included in the published data.

The published dataset contains 171 records.

For the hypothesis tests:

* 7 removed due to < 16 moves
* 25 removed due to bugs

This leaves 139 records for hypothesis tests.

The raw data has now (16/02/2021) been deleted in line with the anonymisation procedure specified in the ethics application.

## Data Source

Data downloaded from [Restdb.io](https://restdb.io) using the script [get-restdb-data](https://github.com/davidgundry/get-restdb-data).

### Pre-anonymised Data Format

Data will be collected using the non-relational database service [restdb.io](https://restdb.io). All data will be downloaded as a json file.

The expected data format is in `design/example-identifiable.json`, it looks like this:

    [ 
        {"_id":"5f118222b0e1d1670001ce11","data":{"gameVersion":"Tool","loadTime":1594982440874,"uploadTime":1594982944816,"duration":485.424,"playDuration":480.002,"answers":["27","female","english","every-day","1","2","2","2","2","2","2","g","g","g","ng","ng","ng","nobug",null],"moves":[["circle","square","triangle"],["filled","empty","green"],["red","green","blue"],["big","empty","circle"],["small","empty","triangle"],["small","empty","triangle"],["filled","empty","green"],["red","green","blue"],["big","triangle","empty"],["small","empty","triangle"],["small","empty","circle"],["red","green","blue"],["empty","filled","green"],["empty","filled","green"],["green","red","blue"]],"moveDurations":[1.5314450000005309,1.916494999999486,1.7831050000004325,5.033134999999675,4.784264999998413,7.050825000000259,1.1063899999990099,2.8494300000002113,9.9504450000004,3.452929999999469,11.851834999999483,79.11336499999923,2.4985599999999977,34.44956000000093,3.0330149999990828]},"version":"1.0.0.IEX-enj-dataq-1.0.0.Tool","studyID":"daa2e38ef9864764b95f4e545","prolificPID":"6440a9870c404843a195ba4a","sessionID":"501617b49a904139b1608183","uid":176}
    ]

* **_id**: Database record ID
* **data**: Participant data recorded from game (a JSON object)
    * **gameVersion**: `Normal` or `Tool`
    * **loadTime**: a timestamp at the point the game loads (uses JavaScript `Date.now()`)
    * **uploadTime**: a timestamp at the point the game begins uploading data to the server, which is immediately upon the final questionnaire being submitted (uses JavaScript `Date.now()`)
    * **duration**: seconds between submission of pre-test questionnaire (and start of **tutorial**), and play-end interrupt before post-test questionnaire
* **version**: Game version and condition data was collected from
* **studyID, prolificPID, sessionID**: Values from the Prolific service for particiant payment purposes.
* **uid**: Auto-incrementing datanbase record UID.

For other variables, see the 'Data Format' section below.

### Anonymising Data

To prepare (i.e. anonymise) the raw data run the following command from the project directory. 

    python python/prepare-data_exp2.py

Edit that file to set the source data filename to match the one as downloaded.

The script will write files to disk in the folder "data". It will also write many files to disk in the same directory as the source (raw) data file. Many of these are for sanity checking purposes and should be deleted as they are not fully anonymised. The important files are:

* `data.json` (containing the main data)
* `duration.csv` (associating duration and condition)
* `age-gender.csv` (associating age and gender)

**Note:** The script shuffles the lines of the data file and it doesn't do any JSON parsing, so it is almost certain that the end-of-line commas will be incorrect. This will lead cause errors in later analysis scripts. To fix this, ensure there is a comma at the end of each line of data, except for the last one.

## Data Format

### Data.json

After processing, the data (`data.json`) looks like this:

    [
        {"data":{"gameVersion":"Tool","playDuration":480.002,"answers":["english","every-day","1","2","2","2","2","2","2","g","g","g","g","g","g","nobug",null],"moves":[["circle","square","triangle"],["filled","empty","green"],["red","green","blue"],["big","empty","circle"],["small","empty","triangle"],["small","empty","triangle"],["filled","empty","green"],["red","green","blue"],["big","triangle","empty"],["small","empty","triangle"],["small","empty","circle"],["red","green","blue"],["empty","filled","green"],["empty","filled","green"],["green","red","blue"]],"moveDurations":[1.5314450000005309,1.916494999999486,1.7831050000004325,5.033134999999675,4.784264999998413,7.050825000000259,1.1063899999990099,2.8494300000002113,9.9504450000004,3.452929999999469,11.851834999999483,79.11336499999923,2.4985599999999977,34.44956000000093,3.0330149999990828]},"version":"1.0.0.IEX-enj-dataq-1.0.0.Tool"}
    ]

* **gameVersion**: Either "Tool" (for the non-game version) or "Normal" (for the game version).
* **playDuration**: seconds between start of logged (non-tutorial) levels, and play-end interrupt before post-test questionnaire
* **answers**: Answers to the questions:
    1. What is your first language (`english`/`other`)
    2. How often do you play digital games? (`every-day`/`several-times-a-week`/`about-once-a-week`/`about-once-a-month`/`almost-never`)
    3. Seven (7) Likert scale (`1-5`) answers to the Intrinsic Motivation Inventory: Enjoyment Subscale, in default question order
    4. Six (6) grammaticality judgements of a list of simple sentence fragments (`g` if grammatical, `ng` if not grammatical)
        1. `red big square`
        2. `big red square`
        3. `big filled square`
        4. `filled red square`
        5. `red filled square`
        6. `filled big square`
    5. Answer to the question "Finally, did you encounter any bugs that may have had an effect on how you played the game? No/Yes" (`nobug`/`bug`)
    6. Description of the bug (optional, string / `null`)
* **moves**: Array of moves attempted by the player (sets of three words inputted, whether or not they trigger an action in the game). These are in order they were selected. Moves are in order attempted.
* **moveDurations**: Array of time taken (in seconds) for each move listed in `moves`.
* **version**: Game version and condition data was collected from

### Age and Gender

`data/age-gender.csv` has records in the format: `age (number entry), gender (female/male/other/prefer-not-to-say)`

    36,female
    19,female
    58,male

This also includes participants who are excluded from the hypothesis tests due to too few inputs. (This also applies to participants who reported bugs). If this were not the case, it would prevent changing the minimum-input threshold after data collection (for example, if it becomes clear that the threshold as set is too high) due to the excluded data already being deleted during the process of anonymisation. Either we might not record all the age/genders (if the threshold is lowered), or we record too many age/genders. As we want to publish `data.json` including particpants excluded due to low input (to allow re-running the analysis with different thresholds), it seems better to record the age/genders that match to this potential superset and accept that the counts may not add up to exactly the same number.

### Duration

`data/duration.csv` has records in the format: `condition (Normal/Tool), duration in seconds`

    Normal,486.424
    Tool,485.424
    Normal,482.424

Because the duration of play was controlled at 480 seconds (8 minutes), the variation that is observed here is accounted for by the time spent in the tutorial. To see the time spent while moves were being logged in the main game, see the `playDuration` variable in `data.json`. This `duration` is separated from the rest of the data as (in principle) a player who spent an exceptional amount of time in the tutorial could have their data identified in combination with Prolfic's log data. (`playDuration` is fixed to almost exactly 480 seconds, so there is no such threat.)

This also includes participants who are excluded from the hypothesis tests due to too few inputs (or reporting bugs) as above.

## Analysis

In the project directory (for this experiment) run the following commands (on Linux). These create (or overwrite) files in `out/`).

    python python/check_exclusions.py > out/check_exclusions.txt

    python python/create_data_csv.py
    
    python python/hypothesis_test_exp2.py > out/hypothesis_test_exp2.txt

    python python/duration_analysis.py > out/duration_analysis.txt

    python python/age_gender_analysis.py  > out/age_gender_analysis.txt
