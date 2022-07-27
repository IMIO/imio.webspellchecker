*** Settings ***

Resource  plone/app/robotframework/keywords.robot
Resource  plone/app/robotframework/selenium.robot

Library  Remote  ${PLONE_URL}/RobotRemote
Library  plone.app.robotframework.keywords.Debugging

Test Setup  Open test browser
Test Teardown  Run keywords  Close all browsers

*** Variables ***

${SELENIUM_IMPLICIT_WAIT}  1
${WAIT_MORE}  5

*** Test cases ***

Scenario: As an editor, I am using Webspellchecker
    Given a logged-in editor
    and a document
    When I edit the document
    Then Webspellchecker is available
    Cancel edit

*** Keywords *****************************************************************

# --- GIVEN ------------------------------------------------------------------

a logged-in editor
  Enable autologin as  Editor  Contributor

a document
  Create content  type=Document  id=document-to-edit  title=Document to edit  text=<p id="p1">paragraph1</p><p id="p2">paragraph2</p><p>paragraph3</p><p>paragraph4</p>
  Go to  ${PLONE_URL}/document-to-edit
  Page Should Contain  paragraph1
  Page Should Contain  paragraph4
  Page Should Contain Element  css=#p1
  Page Should Not Contain Element  css=#p1 strong

# --- WHEN -------------------------------------------------------------------

I edit the document
  Go to  ${PLONE_URL}/document-to-edit/edit

save the document
  Unselect Frame
  Sleep  ${WAIT_MORE}  Wait for the modification of the content
  Click Button  Save

# --- THEN -------------------------------------------------------------------

Webspellchecker is available
  Page should contain element  name=form.widgets.IRichTextBehavior.text

Cancel edit
  Unselect frame
  Click element  css=#form-buttons-cancel
