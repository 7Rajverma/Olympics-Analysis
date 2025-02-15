# Olympics-Analysis

## Overview 
    ##### This project is a Streamlit-based web application for analyzing historical Olympic data. The 
    ##### application provides insights into medal tallies, country-wise and athlete-wise performance, 
    ##### and various statistical analyses.

## Features 
   • Medal Tally: View Olympic medal counts by year and country.
   • Overall Analysis: Get statistics on editions, host cities, sports, events, athletes, and nations.
   • Country-wise Analysis: Analyze a country's Olympic performance over the years.
   • Athlete-wise Analysis: Study athlete age distributions, weight vs. height statistics, and gender participation trends.
   ![Screenshot 2025-02-14 223220](https://github.com/user-attachments/assets/c0a59383-229e-4684-84f1-930e7dfbfdfe)
   ![Screenshot 2025-02-15 144845](https://github.com/user-attachments/assets/6dc42243-c3e4-4d80-9e46-bd9d3539de76)
   ![Screenshot 2025-02-15 144927](https://github.com/user-attachments/assets/05b61a20-89f3-466a-9a7c-96bf3f3cc96e)
   ![Screenshot 2025-02-15 144947](https://github.com/user-attachments/assets/f6b9630c-cde4-42eb-80d2-86261ef88c0b)
   ![Screenshot 2025-02-15 145218](https://github.com/user-attachments/assets/399be661-2714-430c-9b7a-d17ef5d45ed2)
   ![Screenshot 2025-02-15 145049](https://github.com/user-attachments/assets/5b1f9e16-6f89-40f3-9697-aba853b3ad10)






    
## Technologies Used
     • Python
     • Streamlit
     • Pandas
     • Plotly
     • Seaborn
     • Matplotlib

## Project Structure
      |-- app.py              # Main Streamlit app
      |-- helper.py           # Functions for data processing & analytics
      |-- processing.py       # Data preprocessing scripts
      |-- athlete_events_25mb.csv  # Dataset with Olympic athlete event details
      |-- noc_regions.csv     # Mapping of NOC codes to regions

## Installation
   1. Clone this repository:
       git clone https://github.com/your-username/olympics-analysis.git cd olympics-analysis

   2. Install dependencies:
        pip install -r requirements.txt

   3. Run the application:
        streamlit run app.py

## Usage
   • Navigate to http://localhost:8501 in your browser after running the application.
   • Use the sidebar to select different analyses.
   • Interact with the visualizations to explore the Olympic data.

## Data Sources
   • athlete_events_25mb.csv: Contains historical Olympic event data.
   • noc_regions.csv: Provides National Olympic Committee (NOC) to region mappings.

## Contribution
    Feel free to fork the repository and submit pull requests for improvements.
## License
    This project is open-source under the MIT License.



      
