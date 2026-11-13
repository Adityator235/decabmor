DEPLOY STEPS — Google Apps Script Web App
==========================================

1. Go to https://script.google.com
2. Click "+ New Project"
3. In the default "Code.gs" file, delete everything and paste the contents of observer.gs
4. Click the "+" next to "Files" → "HTML" → name it "index" → paste the contents of observer_app/index.html
5. Click "Deploy" → "New deployment"
6. Click the gear icon (⚙) → select "Web app"
7. Fill in:
   - Description: Competitor Observer v1
   - Execute as: Me (your email)
   - Who has access: Anyone
8. Click "Deploy"
9. Authorize permissions when prompted
10. Copy the Web App URL — that's your app

Open that URL on your phone. All data saves to a Google Sheet automatically.

To update the app after editing:
- Edit the code in Apps Script editor
- Click "Deploy" → "Manage deployments"
- Click the pencil icon → "New version" → "Deploy"
- The URL stays the same, just the latest code runs
