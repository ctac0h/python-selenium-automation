Feature: Window handling


Scenario: User can open and close Amazon Blog
 Given Open Amazon page
 Then Save current window handles
 When Click on blog link “See daily updates at blog.aboutamazon.com”
 Then Switch to a new window
 Then Blog blog.aboutamazon.com is opened
 And User can open and close Blog menu
 And Close new window and switch back to original
