# MBTA

MBTA Simple Schedule

#### Running Locally

* Clone repo
  
* Create `virtualenv` and install dependencies:
    ```shell
    virtualenv -p /usr/bin/python .mbta && source .mbta/bin/activate && pip install -r requirements.txt
    ```
  The above will create a virtualenv called `.mbta` in your current directory. If you get out of the`virtualenv`
  and would like to reactivate again just run `source .mbta` and you'll have access to your dependencies again.
  
  >*NOTE*: Replace /usr/bin/python to path where your 3.7+ python binary is. This app was tested with version 3.7-3.9

* Append the `mbta` directory to your `PYTHONPATH`:
    ```shell
    export PYTHONPATH=${PYTHONPATH}:<path to mbta>
    ```
* Run the main app:
    1) If you have appended the `mbta` directory to your `PYTHONPATH`:
      
    ```shell
    python src/mbta_main_app.py
    ```
    
    2) If you didn't appended the `mbta` directory to your `PYTHONPATH`:
    
    ```shell
    PYTHONPATH=`pwd` python src/mbta_main_app.py
    ```

#### Running tests

* Run the main app:
    1) If you have appended the `mbta` directory to your `PYTHONPATH`:
      
    ```shell
    python  -m unittest {test_name} in {path_to}/MBTA/tests
    ```
    
    2) If you didn't appended the `mbta` directory to your `PYTHONPATH`:
    
    ```shell
    PYTHONPATH=`pwd` python  -m unittest {test_name} in {path_to}/MBTA/tests
    ```
#### Future work

* Currently, the lines and stops are querries every time the app is run and are cached in dictionaries. It would be
  good practice to use sqlalchemy to setup a local database to only query this on a scheduled basis instead of making
  calls to the MBTA
  
* Sometimes the times that are returned are empty or nulls, in that case, it would be good to use the schedule relation
  and displayed scheduled times intead of the predictions from the MBTA
  
* Add distinction between end of line and beginning, so that empty predictions don't look like the service is broken
