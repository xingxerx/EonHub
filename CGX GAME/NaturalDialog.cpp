#include "NaturalDialog.h"
#include <iostream>
ProcessResult processNaturalLanguage(std::string input) {
    ProcessResult result;
    result.response = "Processed: " + input;
    if (input == "open door") {
        result.command = Command::OPEN_DOOR;
    } else if (input == "close door") {
        result.command = Command::CLOSE_DOOR;
    } else if (input == "turn on lights") {
        result.command = Command::TURN_ON_LIGHTS;
    } else if (input == "turn off lights") {
        result.command = Command::TURN_OFF_LIGHTS;
    } else if (input == "status") {
        result.command = Command::STATUS;
    } else if (input == "quit") {
        result.command = Command::QUIT;
    } else {
        result.command = Command::NONE;
    }
    return result;
}
