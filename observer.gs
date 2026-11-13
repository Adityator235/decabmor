/**
 * Project Swastik - Competitor Observer App
 * Deploy as Web App on Google Apps Script
 *
 * HOW TO DEPLOY:
 * 1. Go to https://script.google.com
 * 2. Click "New Project"
 * 3. Delete all code in the editor
 * 4. Paste this ENTIRE file
 * 5. Click "Deploy" -> "New deployment"
 * 6. Click the gear icon -> "Web app"
 * 7. Description: "Competitor Observer"
 * 8. Execute as: "Me"
 * 9. Who has access: "Anyone"
 * 10. Click "Deploy"
 * 11. Copy the Web App URL
 * 12. Open on your phone
 */

function doGet() {
  return HtmlService.createHtmlOutputFromFile('index')
    .setTitle('Competitor Observer')
    .setXFrameOptionsMode(HtmlService.XFrameOptionsMode.ALLOWALL)
    .addMetaTag('viewport', 'width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no');
}

function saveData(data) {
  try {
    // Get or create the spreadsheet
    var sheetName = 'Observer Data';
    var ss;
    try {
      ss = SpreadsheetApp.getActiveSpreadsheet();
    } catch(e) {
      ss = SpreadsheetApp.create('Competitor Observer Data');
    }

    var sheet = ss.getSheetByName(sheetName);
    if (!sheet) {
      sheet = ss.insertSheet(sheetName);
      // Headers
      sheet.appendRow([
        'Timestamp', 'Observer', 'Pharmacy', 'Date', 'Visit Type',
        'Traffic Level', 'Total Observed', 'Served', 'Avg Wait (s)',
        'Avg Wait Display', 'Customers in Store', 'Staff at Counter',
        'Customer:Staff Ratio', 'Drive-Thru', 'Drive-Thru Cars',
        'Drop-off/Pickup', 'Specialty Pharmacy', 'Health Screenings',
        'Interaction (1-5)', 'Name Recognition', 'Med Counseling',
        'OTC Display', 'Loyalty Visible', 'Digital Engagement',
        'Atmosphere (1-5)', 'Overall (1-5)', 'Loyalty Notes', 'Other Notes',
        'Customer Wait Times JSON'
      ]);
    }

    // Format customer wait times as readable string
    var waitTimesStr = '';
    if (data.queueData && data.queueData.individualWaitTimes) {
      data.queueData.individualWaitTimes.forEach(function(c) {
        waitTimesStr += c.name + ': ' + (c.waitSeconds !== null ? c.waitSeconds + 's' : 'still waiting') + ' | ';
      });
    }

    // Save row
    sheet.appendRow([
      new Date(),
      data.user,
      data.pharmacy,
      data.date,
      data.visitType,
      data.trafficLevel,
      data.queueData.totalObserved,
      data.queueData.served,
      data.queueData.averageWaitSeconds,
      data.queueData.averageWaitDisplay,
      data.customersInStore,
      data.staffAtCounter,
      data.customerStaffRatio,
      data.driveThru,
      data.driveThruCars,
      data.dropoffPickup,
      data.specialtyPharmacy,
      data.healthScreenings,
      data.interaction,
      data.nameRecognition,
      data.medCounseling,
      data.otc,
      data.loyalty,
      data.digital,
      data.atmosphere,
      data.overall,
      data.loyaltyNotes,
      data.otherNotes,
      waitTimesStr
    ]);

    return { success: true, totalEntries: sheet.getLastRow() - 1 };
  } catch(e) {
    return { success: false, error: e.toString() };
  }
}

function getAllData() {
  try {
    var ss = SpreadsheetApp.getActiveSpreadsheet();
    var sheet = ss.getSheetByName('Observer Data');
    if (!sheet || sheet.getLastRow() <= 1) {
      return [];
    }

    var data = sheet.getDataRange().getValues();
    var rows = [];

    // Skip header row
    for (var i = 1; i < data.length; i++) {
      rows.push({
        timestamp: data[i][0],
        user: data[i][1],
        pharmacy: data[i][2],
        date: data[i][3],
        visitType: data[i][4],
        trafficLevel: data[i][5],
        totalObserved: data[i][6],
        served: data[i][7],
        avgWait: data[i][8],
        avgWaitDisplay: data[i][9],
        customersInStore: data[i][10],
        staffAtCounter: data[i][11],
        ratio: data[i][12],
        driveThru: data[i][13],
        driveThruCars: data[i][14],
        dropoffPickup: data[i][15],
        specialtyPharmacy: data[i][16],
        healthScreenings: data[i][17],
        interaction: data[i][18],
        nameRecognition: data[i][19],
        medCounseling: data[i][20],
        otc: data[i][21],
        loyalty: data[i][22],
        digital: data[i][23],
        atmosphere: data[i][24],
        overall: data[i][25],
        loyaltyNotes: data[i][26],
        otherNotes: data[i][27],
        waitTimes: data[i][28]
      });
    }

    return rows;
  } catch(e) {
    return [];
  }
}

function getSummary() {
  try {
    var ss = SpreadsheetApp.getActiveSpreadsheet();
    var sheet = ss.getSheetByName('Observer Data');
    if (!sheet || sheet.getLastRow() <= 1) {
      return { pharmacies: [], entries: 0 };
    }

    var data = sheet.getDataRange().getValues();
    var pharmacies = {};

    for (var i = 1; i < data.length; i++) {
      var pharma = data[i][2];
      if (!pharmacies[pharma]) pharmacies[pharma] = [];

      pharmacies[pharma].push({
        visitType: data[i][4],
        date: data[i][3],
        trafficLevel: data[i][5],
        avgWait: data[i][9],
        served: data[i][7],
        customersInStore: data[i][10],
        staffAtCounter: data[i][11],
        ratio: data[i][12],
        interaction: data[i][18],
        otc: data[i][21],
        loyalty: data[i][22],
        atmosphere: data[i][24],
        overall: data[i][25],
        otherNotes: data[i][27]
      });
    }

    return { pharmacies: pharmacies, entries: data.length - 1 };
  } catch(e) {
    return { pharmacies: {}, entries: 0 };
  }
}
