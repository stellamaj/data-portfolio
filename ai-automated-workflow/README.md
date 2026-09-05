# AI-Powered Data Cleaning Workflow

This project demonstrates an AI-powered automated workflow for cleaning CSV data before analysis. Data cleaning is a strong candidate for automation because it happens frequently, often involves repetitive steps with predictable outcomes, and automation can reduce effort, time and cost. The workflow uses Power Automate to detect newly added CSV files in a OneDrive folder, use AI to identify data type and format issues that may not be obvious from column labels alone, apply rule based cleaning steps, and notify a Data Analyst for final review before the data is used for analysis.

## Project overview

| Question | Answer |
|---|---|
| The problem, and who it affects | Data cleaning involves repetitive tasks that can take time and delay analysis. This affects Data Analysts who regularly prepare data for analysis. |
| The trigger | A new CSV file is added to the designated OneDrive or SharePoint folder. |
| One risk | AI could incorrectly identify a data type or format issue. |
| The safeguard | A Data Analyst reviews the cleaned file before it is used for analysis. |

## Building the workflow in Power Automate

### Setup/Configuration

Opened Power Automate and selected the **Automated cloud flow** tile, since the workflow needs to start automatically when a new CSV file is added to a folder — not on a manual click or a fixed schedule.

<img src="images/setup.png" alt="Power Automate setup" width="700">

### Prerequisite

Before creating the flow, set up the folder in **OneDrive for Business** where the CSV files will be added. The trigger will monitor this folder for new files.

### Trigger

In the **Build an automated cloud flow** window:

1. Enter a name for the flow in the **Flow name** field (e.g. `Data Cleaning Notification`).
2. Select **When a file is created (OneDrive for Business)** as the trigger.
3. Select **Create**.

<img src="images/setup.png" alt="Build an automated cloud flow window showing the flow name field and OneDrive for Business file creation trigger" width="700">

At this stage, the flow canvas may show an **Invalid parameters** message. This is expected because the folder has not been selected yet.

4. Click the **When a file is created** box to expand the trigger settings.

<img src="images/trigger-02.png" alt="Flow canvas showing the Invalid parameters message" width="700">

5. Check the connection status. If it says **Not connected**, select the **Change connection** link.

<img src="images/trigger-03.png" alt="Trigger settings showing the connection status and Change connection link" width="700">

6. Select the existing **OneDrive for Business** connection. If its status icon shows that it is not active, click the connection row to select it. If it does not connect, select **Add new** to create a new connection and sign in.

<img src="images/trigger-04.png" alt="OneDrive for Business connections showing an inactive connection and the Add new option" width="700">

7. Check the connection status. It should show **Connected to [your_email_address]**. Then click the folder icon on the right side of the field. Instead of clicking **Root**, click the **>** arrow next to it to expand Root and display the folders inside. Find and select the folder in OneDrive that was set up earlier.

<img src="images/trigger-05.png" alt="OneDrive folder selection" width="700">

8. Check that the **Folder** field shows the correct folder (e.g. `/Netflix Dataset Cleaning`) and that the **Invalid parameters** warning has disappeared from the trigger box. Click **Save** in the top-right corner of the screen.

<img src="images/trigger-06.png" alt="Trigger settings showing the selected OneDrive folder with no Invalid parameters warning and the Save button" width="700">