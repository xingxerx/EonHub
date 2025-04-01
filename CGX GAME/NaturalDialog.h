#ifndef NATURALDIALOG_H
#define NATURALDIALOG_H
#include <string>
enum class Command {
    NONE,
    OPEN_DOOR,
    CLOSE_DOOR,
    TURN_ON_LIGHTS,
    TURN_OFF_LIGHTS,
    STATUS,
    QUIT
};

struct ProcessResult {
    std::string response;
    Command command;
};

ProcessResult processNaturalLanguage(std::string input);

#endif
