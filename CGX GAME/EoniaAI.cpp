// EoniaAI.cpp
#include <iostream>
#include <string>
#include "NaturalDialog.h"
#include "EoniaAI.h"
#include "CGXAI.h"
using namespace std;

// Reality class methods implementation
void Reality::createUniverse(std::string name) {
    // Code to birth a universe...
    std::cout << "Universe " << name << " created." << std::endl;
}

void Reality::bendTime(bool lock) {
    timelineLocked = lock;
    std::cout << "Timeline " << (lock ? "locked" : "unlocked") << std::endl;
}

void Reality::channelCosmicEnergy(double amount) {
    cosmicEnergy += amount;
    std::cout << "Cosmic energy channeled: " << amount << std::endl;
}

// OmegaSync class methods implementation
void OmegaSync::main() {
    Reality reality;
    reality.createUniverse("Nebula-X"); // Create a test universe
    reality.bendTime(true); // Lock timeline for testing
    reality.channelCosmicEnergy(1e+10); // Channel small cosmic energy amount
}

// EoniaAI class methods implementation
EoniaAI::EoniaAI(CGXAI& cgxAI) : cgxAI(cgxAI) {}

std::string EoniaAI::processInput(string input) {
    ProcessResult result = processNaturalLanguage(input);
    cout << "Processing: " << result.response << endl;

    // Check if the input is a command for the CGX system
    switch (result.command) {
        case Command::OPEN_DOOR:
            cgxAI.SendCommand("open door");
            return "Command sent to CGX system.";
        case Command::CLOSE_DOOR:
            cgxAI.SendCommand("close door");
            return "Command sent to CGX system.";
        case Command::TURN_ON_LIGHTS:
            cgxAI.SendCommand("turn on lights");
            return "Command sent to CGX system.";
        case Command::TURN_OFF_LIGHTS:
            cgxAI.SendCommand("turn off lights");
            return "Command sent to CGX system.";
        case Command::STATUS:
            cgxAI.SendCommand("status");
            return "Command sent to CGX system.";
        case Command::QUIT:
            return "quit";
        case Command::NONE:
        default:
            return result.response;
    }
}

// Methods to access Reality functions
void EoniaAI::createUniverse(std::string name) {
    reality.createUniverse(name);
}

void EoniaAI::bendTime(bool lock) {
    reality.bendTime(lock);
}

void EoniaAI::channelCosmicEnergy(double amount) {
    reality.channelCosmicEnergy(amount);
}
