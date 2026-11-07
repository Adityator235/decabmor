/**
 * Project Swastik - StarCare Pharmacy Patient Survey
 * Creates a Google Form with all 29 questions automatically.
 *
 * HOW TO USE:
 * 1. Go to https://script.google.com
 * 2. Click "New Project"
 * 3. Paste this entire script
 * 4. Click "Save" (Ctrl+S)
 * 5. Click "Run" -> select "createStarCareSurvey"
 * 6. Grant permissions when prompted
 * 7. The form will be created in your Google Drive
 */

function createStarCareSurvey() {
  var form = FormApp.create('StarCare Pharmacy - Patient Loyalty Survey');
  form.setDescription(
    'This survey helps StarCare Pharmacy understand what drives customer loyalty ' +
    'and repeat engagement. Your responses are anonymous and will be used for a high school ' +
    'business research project. Thank you for your time!'
  );

  // SECTION A: DEMOGRAPHICS
  form.addPageBreakItem()
    .setTitle('Section A: About You')
    .setInstruction('Just a few quick questions about your household.');

  form.addMultipleChoiceItem()
    .setTitle('A1. What is your age group?')
    .setRequired(true)
    .setChoices([
      form.createChoice('Under 18'),
      form.createChoice('18-24'),
      form.createChoice('25-34'),
      form.createChoice('35-44'),
      form.createChoice('45-54'),
      form.createChoice('55-64'),
      form.createChoice('65+')
    ]);

  form.addNumberItem()
    .setTitle('A2. How many people are in your household?')
    .setRequired(true)
    .setHint('Enter a whole number')
    .setInvalidChoiceMessage('Please enter a whole number.');

  form.addNumberItem()
    .setTitle('A3. How many prescriptions does your household fill per month?')
    .setRequired(true)
    .setHint('Enter a whole number')
    .setInvalidChoiceMessage('Please enter a whole number.');

  // SECTION B: PHARMACY USAGE
  form.addPageBreakItem()
    .setTitle('Section B: Your Pharmacy Habits')
    .setInstruction('Tell us about how you use StarCare.');

  form.addMultipleChoiceItem()
    .setTitle('B1. How long have you been a StarCare patient?')
    .setRequired(true)
    .setChoices([
      form.createChoice('Less than 1 month'),
      form.createChoice('1-6 months'),
      form.createChoice('6-12 months'),
      form.createChoice('1-2 years'),
      form.createChoice('2+ years')
    ]);

  form.addMultipleChoiceItem()
    .setTitle('B2. How often do you fill prescriptions at StarCare?')
    .setRequired(true)
    .setChoices([
      form.createChoice('Every time'),
      form.createChoice('Most of the time'),
      form.createChoice('Sometimes'),
      form.createChoice('Rarely'),
      form.createChoice('Never - first-time patient')
    ]);

  form.addMultipleChoiceItem()
    .setTitle('B3. Have you used StarCare home delivery?')
    .setRequired(true)
    .setChoices([
      form.createChoice('Yes, regularly'),
      form.createChoice('Yes, once or twice'),
      form.createChoice('No, but interested'),
      form.createChoice('No, not interested')
    ]);

  form.addMultipleChoiceItem()
    .setTitle('B4. How often do you purchase OTC or wellness products (vitamins, personal care) at StarCare?')
    .setRequired(true)
    .setChoices([
      form.createChoice('Every fill'),
      form.createChoice('Sometimes'),
      form.createChoice('Rarely'),
      form.createChoice('Never')
    ]);

  form.addCheckboxItem()
    .setTitle('B5. Which StarCare services have you used? (Select all that apply)')
    .setRequired(true)
    .setChoices([
      form.createChoice('Prescription filling'),
      form.createChoice('Custom compounding'),
      form.createChoice('Immunizations (flu shots, vaccines)'),
      form.createChoice('Medication Therapy Management (MTM)'),
      form.createChoice('Durable Medical Equipment (DME)'),
      form.createChoice('Veterinary medications'),
      form.createChoice('Home delivery'),
      form.createChoice('Greeting cards / gifts'),
      form.createChoice('None - I have only filled prescriptions')
    ]);

  form.addCheckboxItem()
    .setTitle('B6. What was your main reason for choosing StarCare? (Select all that apply)')
    .setRequired(true)
    .setChoices([
      form.createChoice('Personal recommendation from friend or family'),
      form.createChoice('Close to my home'),
      form.createChoice('Close to my work or school'),
      form.createChoice('My insurance requires it'),
      form.createChoice('My previous pharmacy closed'),
      form.createChoice('Staff recommendation'),
      form.createChoice('I wanted an independent or local pharmacy'),
      form.createChoice('Other')
    ]);

  // SECTION C: SATISFACTION DRIVERS
  form.addPageBreakItem()
    .setTitle('Section C: How We Are Doing')
    .setInstruction('Rate your satisfaction with each aspect of StarCare (1 = Very Dissatisfied, 5 = Very Satisfied).');

  var satisfactionItems = [
    'Staff knowledge about medications',
    'Wait time at pickup',
    'Clarity of copay explanation (did you know what you would pay before filling?)',
    'Store atmosphere and cleanliness',
    'Ease of online refill process',
    'Quality of compounding services',
    'Frequency of staff greeting you by name',
    'Overall satisfaction with StarCare'
  ];

  for (var i = 0; i < satisfactionItems.length; i++) {
    form.addLinearScaleItem()
      .setTitle(satisfactionItems[i])
      .setRequired(true)
      .setLeftLabel('Very Dissatisfied (1)')
      .setRightLabel('Very Satisfied (5)')
      .setMin(1)
      .setMax(5);
  }

  // SECTION D: LOYALTY INTEREST
  form.addPageBreakItem()
    .setTitle('Section D: Loyalty Program Interest')
    .setInstruction('StarCare is exploring a loyalty rewards program. Your input shapes what it looks like.');

  form.addMultipleChoiceItem()
    .setTitle('D1. Would you participate in a loyalty rewards program at StarCare?')
    .setRequired(true)
    .setChoices([
      form.createChoice('Definitely'),
      form.createChoice('Probably'),
      form.createChoice('Maybe'),
      form.createChoice('Probably not'),
      form.createChoice('Definitely not')
    ]);

  form.addCheckboxItem()
    .setTitle('D2. Which rewards would you value most? (Select up to 3)')
    .setRequired(true)
    .setChoices([
      form.createChoice('Discount on OTC/wellness products'),
      form.createChoice('Free health screening (blood pressure, glucose)'),
      form.createChoice('Priority service (skip the line)'),
      form.createChoice('Free home delivery'),
      form.createChoice('Birthday gift or card'),
      form.createChoice('Referral bonus (for bringing a friend)'),
      form.createChoice('Prescription copay assistance'),
      form.createChoice('Other')
    ]);

  form.addMultipleChoiceItem()
    .setTitle('D3. How likely are you to refer a friend or family member to StarCare?')
    .setRequired(true)
    .setChoices([
      form.createChoice('Very likely'),
      form.createChoice('Somewhat likely'),
      form.createChoice('Neutral'),
      form.createChoice('Somewhat unlikely'),
      form.createChoice('Very unlikely')
    ]);

  form.addMultipleChoiceItem()
    .setTitle('D4. Would you prefer a stamp card or a points-based system?')
    .setRequired(true)
    .setChoices([
      form.createChoice('Stamp card (buy X times, get Y free)'),
      form.createChoice('Points-based (earn points per dollar spent)'),
      form.createChoice('No preference')
    ]);

  form.addMultipleChoiceItem()
    .setTitle('D5. How often would you check your loyalty program status?')
    .setRequired(true)
    .setChoices([
      form.createChoice('Every visit'),
      form.createChoice('Weekly'),
      form.createChoice('Monthly'),
      form.createChoice('Rarely')
    ]);

  form.addMultipleChoiceItem()
    .setTitle('D6. Would you like to receive health tips via SMS or text message?')
    .setRequired(false)
    .setChoices([
      form.createChoice('Yes'),
      form.createChoice('No')
    ]);

  form.addTextItem()
    .setTitle('D7. What additional rewards would encourage you to return more often?')
    .setRequired(false)
    .setPlaceholder('Type your answer here...');

  // SECTION E: OPEN FEEDBACK
  form.addPageBreakItem()
    .setTitle('Section E: Your Thoughts')
    .setInstruction('Last section - your open feedback helps us improve.');

  form.addTextItem()
    .setTitle('E1. What is ONE thing StarCare could do to improve your experience?')
    .setRequired(true)
    .setPlaceholder('Type your answer here...');

  form.addTextItem()
    .setTitle('E2. What do you appreciate MOST about StarCare?')
    .setRequired(true)
    .setPlaceholder('Type your answer here...');

  form.addTextItem()
    .setTitle('E3. Any other comments or suggestions?')
    .setRequired(false)
    .setPlaceholder('Type your answer here...');

  form.setConfirmationMessage(
    'Thank you for completing the survey! Your responses are anonymous and will help ' +
    'StarCare Pharmacy serve you better.'
  );

  Logger.log('Form created successfully!');
  Logger.log('Form URL: ' + form.getFormUrl());
  Logger.log('Edit URL: ' + form.getEditUrl());
}
