Feature: Weather and Music Algorithm

  Scenario: Play Song When Alarm Goes Off
    Given we have a weather and music app
    And the alarm time is reached
    When a request is made to weather API
    And a weather-related music selection is made
    And a request is made to the music API
    Then a response is obtained containing a weather forecast
    And an appropriate music selection is made
    And a response is obtained containing a song
    And the song is played