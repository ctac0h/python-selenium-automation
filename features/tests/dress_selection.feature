Feature: Test for dress selection


  Scenario Outline: User can select product colors
    Given Open Amazon Product <pid> page
    Then Verify user can select through <colors>
    Examples:
      | pid | colors |
      | B07K16Z8LH | ["emerald","ivory","navy","black"] |
      | B07BJKRR25 | ["Black","Blue Overdyed","Dark Wash","Indigo Wash","Light Wash","Medium Wash","Rinse","Vintage Light Wash"] |


