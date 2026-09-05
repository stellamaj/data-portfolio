# AI-Powered Data Cleaning Workflow

This project demonstrates an AI-powered automated workflow for cleaning Excel data before analysis. Data cleaning is a strong candidate for automation because it happens frequently, often involves repetitive steps with predictable outcomes, and automation can reduce effort, time and cost. The workflow uses Power Automate to detect newly added Excel files in a OneDrive folder, use AI to identify data type and format issues that may not be obvious from column headers alone, apply rule based cleaning steps, and notify a Data Analyst for final review before the data is used for analysis.

## Project overview

| Question | Answer |
|---|---|
| The problem, and who it affects | Data cleaning involves repetitive tasks that can take time and delay analysis. This affects Data Analysts who regularly prepare data for analysis. |
| The trigger | A new Excel file is added to the designated OneDrive or SharePoint folder. |
| One risk | AI could incorrectly identify a data type or format issue. |
| The safeguard against that risk | A Data Analyst reviews the AI findings and fixes any flagged issues before the rule based cleaning steps are applied. |

## Building the workflow in Power Automate

### Setup/Configuration

Open Power Automate and select the `Automated cloud flow` tile, since the workflow needs to start automatically when a new Excel file is added to a folder — not on a manual click or a fixed schedule.

<img src="images/setup.png" alt="Power Automate setup" width="700">

### Prerequisite

Before creating the flow, set up the folder in **OneDrive for Business** where the Excel files will be added. The trigger will monitor this folder for new files.

### 1. Trigger (Excel file added to OneDrive)

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

8. Check that the `Folder` field shows the correct folder (e.g. `/Netflix Dataset Cleaning`) and that the `Invalid parameters` warning has disappeared from the trigger box. Collapse the **trigger settings panel** to return to the flow canvas.

<img src="images/trigger-06.png" alt="Trigger settings panel with collapse button" width="700">

### Note about the original approach

The original approach was to trigger the workflow when a CSV file was added. However, Power Automate does not provide a `Convert file` action to convert a CSV file into an Excel file. Therefore, the workflow was changed so that an Excel file must be uploaded to the OneDrive folder as the prerequisite.

<!--

### 2. Convert file

1. Click the `+` below the trigger. The `Add an action` panel opens on the right.

<img src="images/convert-01.png" alt="Add an action panel" width="700">

2. Type `Convert file` in the `Search` field. The available options will appear below. Select `Convert File`.

<img src="images/convert-02.png" alt="Convert File search results" width="700">

The `Convert file` action has been added to the flow.

<img src="images/convert-03.png" alt="Convert file action in the flow" width="700">

3. In the `File` field, type `/` and select `Insert dynamic content` from the dropdown.

The file name is dynamic, so the flow can process a different CSV file each time it is triggered. Power Automate captures the name of the file that triggered the flow.

<img src="images/convert-04.png" alt="File field with Insert dynamic content option" width="700">
-->

### AI Step

1. Click the `+` below the trigger. The `Add an action` panel opens on the right.

<img src="images/ai-01.png" alt="Add an action panel" width="700">

2. Under `AI capabilities`, select `Run a prompt`.

<img src="images/ai-02.png" alt="AI capabilities with Run a prompt option" width="700">

The `Run a prompt` step has been added to the canvas as the second step in the flow. The `Create Connection` panel also appears on the left.

<img src="images/ai-03.png" alt="Run a prompt step and Create Connection panel" width="700">

3. In the `Connection name` field, enter a name for the connection. This is just a label to help you recognise the connection later, for example, `AI Prompt Connection`.

4. Leave `Authentication Type` set to `Oauth`, which is the standard sign-in method using your account. Select the `Sign in` button.

<img src="images/ai-04.png" alt="Create Connection panel with connection name and authentication type" width="700">

> **Note:** Being signed into Power Automate only gives you access to the app itself. Each individual action, such as `Run a prompt`, connects to a separate Microsoft service behind the scenes, so you need to sign in to that service as well.

5. Select `New custom prompt`. None of the ready-made prompts are designed to check data type and format issues, so a custom prompt is needed.

<img src="images/ai-05.png" alt="New custom prompt option" width="700">

6. In the `Custom Prompt` window, select the `+ Add content` button at the bottom.

<img src="images/ai-06.png" alt="Custom Prompt window with Add content button" width="700">

7. Under `Input`, select `Image or document`. This option allows you to add the content of the file. `Document input` is used as a placeholder in the prompt instructions.

<img src="images/ai-07.png" alt="Image or document option under Input" width="700">

8. Select `Close`. There is no need to change the name of the `Document input` placeholder.

<img src="images/ai-08.png" alt="Document input placeholder window with Close button" width="700">