#include "EoniaAI.h"
#include "CGXAI.h"
#include <iostream>

int main() {
    CGXAI cgx;
    EoniaAI eonia(cgx);

    // Test EoniaAI's basic commands
    std::cout << eonia.processInput("open door") << std::endl;
    std::cout << eonia.processInput("status") << std::endl;
    std::cout << eonia.processInput("turn off lights") << std::endl;
    std::cout << eonia.processInput("hello") << std::endl;

    // Test the Cosmic Source Code integration
    eonia.createUniverse("Andromeda-Prime");
    eonia.bendTime(false);
    eonia.channelCosmicEnergy(5e+50);

    //Test OmegaSync
    OmegaSync::main();

    return 0;
}
