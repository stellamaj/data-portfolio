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

9. Enter the prompt next to the `Document input` placeholder and select the `Save` button.

<img src="images/ai-09.png" alt="Custom Prompt with instructions and Document input placeholder" width="700">

10. In the `Document input` field, type `/` and select `Insert dynamic content` from the dropdown.

<img src="images/ai-10.png" alt="Document input field with Insert dynamic content option" width="700">

11. Select `File content` from the `When a file is created` section in the dynamic content dropdown.

<img src="images/ai-11.png" alt="Dynamic content with File content option" width="700">

12. Select the `Save` button at the top right of the screen.

<img src="images/ai-12.png" alt="Save button at the top right" width="700">

> Note: The `base64(...)` part is Power Automate converting the file content into text so that the AI step can read it. The `Item.item/source` information is added automatically by AI Builder and does not need to be changed.

> The green confirmation banner indicates that the step has been completed successfully and the flow is ready to continue.

<img src="images/ai-13.png" alt="Completed Run a prompt step with green confirmation banner" width="700">

### 3. Data Analyst reviews AI findings

1. Click the `+` button below `Run a prompt` on the canvas to add the approval step.

<img src="images/approval-01.png" alt="Plus button below Run a prompt" width="700">

2. In the search box, type `Approval` and press `Enter`. Under `Standard approvals`, select `Start and wait for an approval`.

<img src="images/approval-02.png" alt="Approval search results with Start and wait for an approval" width="700">

> This pauses the flow and sends the Data Analyst a task to review the AI findings before the flow continues.

3. In the `Title` field, enter a title, for example, `Review AI data findings`. Then select the light bulb icon to insert dynamic content.

<img src="images/approval-03.png" alt="Approval title field with dynamic content icon" width="700">

4. Select `File name` under `When a file is created`.

<img src="images/approval-04.png" alt="File name under When a file is created" width="700">

5. In the `Assigned to` field, enter an email address (for this build, use your own email address).

> Note: Power Automate will search your organisation's contacts as you type. Select the matching contact that appears.

<img src="images/approval-05.png" alt="Assigned to field with email address" width="700">

6. Click in the `Details` field. Then select the dynamic content picker (lightning bolt) and, under `Run a prompt`, select `Text` to insert the AI's findings (the `Run a prompt` step's response/output).

<img src="images/approval-06.png" alt="Details field with Run a prompt Text option" width="700">

7. Select the `Save` button at the top right of the screen.

<img src="images/approval-07.png" alt="Save button at the top right" width="700">

### 4. Rule Based Cleaning

The rule based cleaning is done using an Office Script in Excel, which applies `CLEAN` and `TRIM` to text values and removes duplicate rows. This script is created directly in Excel Online, then called from Power Automate using the `Run script` action, so the same cleaning happens automatically every time the flow runs.

1. Add an Excel file containing the dataset to the designated OneDrive folder, for example, `netflix_titles.xlsx`.

<img src="images/rule-01.png" alt="Excel dataset file in OneDrive folder" width="700">

> Note: Uploading the file at this stage triggers the flow, even though the rule based cleaning step isn't built yet. This is fine while building the flow — it just causes an incomplete run that pauses at the approval step.

2. Open `netflix_titles.xlsx` in Excel Online.

<img src="images/rule-02.png" alt="netflix_titles.xlsx open in Excel Online" width="700">

3. Select `Automate` in the top ribbon.

<img src="images/rule-03.png" alt="Automate in the top ribbon" width="700">

4. Select `New Script`, then select `Create in Code Editor`.

<img src="images/rule-04.png" alt="New Script menu with Create in Code Editor option" width="700">

5. Select `Write a script`.

<img src="images/rule-05.png" alt="Write a script option" width="700">

6. Click into the code area, select all the existing text using `Ctrl+A` (Windows) or `Cmd+A` (Mac), delete it, and paste the following script:

```typescript
function main(workbook: ExcelScript.Workbook) {
  let sheet = workbook.getActiveWorksheet();
  let usedRange = sheet.getUsedRange();
  let values = usedRange.getValues();

  // Clean and trim every text cell, leave numbers and dates untouched
  for (let row = 0; row < values.length; row++) {
    for (let col = 0; col < values[row].length; col++) {
      let cell = values[row][col];
      if (typeof cell === "string") {
        let cleaned = cell.replace(/[\x00-\x1F\x7F]/g, "").trim().replace(/\s+/g, " ");
        values[row][col] = cleaned;
      }
    }
  }
  usedRange.setValues(values);

  // Remove duplicate rows, checking every column, assuming row 1 is headers
  let columnCount = usedRange.getColumnCount();
  let columnsToCheck: number[] = [];
  for (let i = 0; i < columnCount; i++) {
    columnsToCheck.push(i);
  }
  usedRange.removeDuplicates(columnsToCheck, true);
}
```

<img src="images/rule-06.png" alt="Office Script code editor with cleaning script" width="700">

7. Rename the script by selecting the `Rename` button and entering `CleanData`.

<img src="images/rule-07.png" alt="Rename button and CleanData script name" width="700">

8. Select the `▷` (play) button to run the script and check that it works on the file.

<img src="images/rule-08.png" alt="Play button to run the CleanData script on the file" width="700">

9. Go back to Power Automate to add the script as a step in your flow. Select the `+` button below `Start and wait for an approval`.

<img src="images/rule-09.png" alt="Plus button below Start and wait for an approval" width="700">

10. In the search box type `Run script`. In the results, select `Run script` under `Excel Online (Business)`.

<img src="images/rule-10.png" alt="Run script under Excel Online Business in the search results" width="700">

11. Select `Sign in` and follow the prompts to connect to `Excel Online (Business)` using the same Microsoft account you are already using.

<img src="images/rule-11.png" alt="Sign in to Excel Online Business" width="700">

12. Select the `Location` dropdown and choose `OneDrive for Business`.

<img src="images/rule-12.png" alt="Location dropdown with OneDrive for Business option" width="700">

12. Select the `Location` dropdown and choose `OneDrive for Business`.

<img src="images/rule-12.png" alt="Location dropdown with OneDrive for Business option" width="700">

13. Select the `Document Library` dropdown and choose `OneDrive`.

<img src="images/rule-13.png" alt="Document Library dropdown with OneDrive option" width="700">

14. Select the folder icon next to the `File` field and browse to select `netflix_titles.xlsx` from the `Netflix Dataset Cleaning` folder.

<img src="images/rule-14.png" alt="File selection showing netflix_titles.xlsx in the Netflix Dataset Cleaning folder" width="700">

15. Select the `Script` dropdown and choose `CleanData`, the script you created.

<img src="images/rule-15.png" alt="Script dropdown with CleanData selected" width="700">

> Note: The script isn't stored in the Excel file itself. It's saved to the Office Scripts library, which is tied to the Microsoft 365 account. Power Automate's `Run script` action reads from the same library, so any script created there appears automatically. No separate connecting step is needed.
>
> Office Scripts only work through Excel Online (Excel on the web), not the desktop app. That's why we had to write and run the script online.

16. Select the `Save` button at the top right of the screen.

<img src="images/rule-16.png" alt="Save button at the top right" width="700">

### 5. Notify Data Analyst

Power Automate notifies the Data Analyst that the cleaned file is ready after the rule based cleaning has finished.

1. Click the `+` button below `Run script` on the canvas.

<img src="images/notify-01.png" alt="Plus button below Run script" width="700">

2. In the search box, type `send an email` and press `Enter`. Look for `Send an email (V2)` under `Office 365 Outlook`, then select it.

<img src="images/notify-02.png" alt="Send an email V2 under Office 365 Outlook" width="700">