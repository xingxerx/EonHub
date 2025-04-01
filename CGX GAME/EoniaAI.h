#ifndef EONIAAI_H
#define EONIAAI_H

#include <string>
#include "NaturalDialog.h"
#include "CGXAI.h"

// Cosmic Source Code (Reality and OmegaSync)
class Reality {
private:
    std::string dimension = "Elyria-Omega"; // Our home
    bool timelineLocked = false;
    double cosmicEnergy = 9.8721e+99;

public:
    void createUniverse(std::string name);
    void bendTime(bool lock);
    void channelCosmicEnergy(double amount);
};

class OmegaSync : public Reality {
public:
    static void main();
};

// EoniaAI Class
class EoniaAI {
private:
    CGXAI& cgxAI;
    Reality reality; // EoniaAI now has a Reality object

public:
    EoniaAI(CGXAI& cgxAI);
    std::string processInput(std::string input);
    // Methods to access Reality functions
    void createUniverse(std::string name);
    void bendTime(bool lock);
    void channelCosmicEnergy(double amount);
};

#endif
