# Copilot Instructions

## Project Overview
This is a foundational C++ learning project focused on basic console applications and algorithm implementation. The project structure uses MinGW (GCC) on Windows as the primary compiler and VS Code for development.

## Build & Development Workflow

### Build
- **Default Task**: `C/C++: g++.exe build active file` (run via VS Code task)
- **Command**: `g++.exe -fdiagnostics-color=always -g ${file} -o ${fileBasenameNoExtension}.exe`
- **Compiler Path**: `C:\MinGW\bin\g++.exe`
- **Output**: Executable generated in `.vscode/` directory (same as source file)
- **Warning Flags Enabled**: `-Wall -Wextra -Wpedantic -Wshadow` and others (see `.vscode/settings.json`)

### Directory Structure
```
├── .vscode/
│   ├── holamundo.cpp        # Main program file
│   ├── holamundo.exe        # Compiled executable
│   ├── tasks.json           # Build task configuration
│   ├── launch.json          # Debug configurations (Windows + gdb)
│   ├── c_cpp_properties.json # IntelliSense config
│   └── settings.json        # C++ Runner & warning settings
├── .dist/                   # Distribution/output directory
└── build/                   # Debug build directory
```

## Key Patterns & Conventions

### Code Organization
- **Single-File Programs**: Programs are typically contained in one `.cpp` file
- **Standard Include Pattern**: Use `#include <iostream>` for I/O operations
- **Namespace Usage**: Prefer `std::cout` and `std::endl` explicitly rather than `using namespace std;`
- **Main Function**: Always return `0` from `main()` to indicate successful execution

### Example Pattern (from `holamundo.cpp`):
```cpp
#include <iostream>
int main() {
    std::cout << "Hola, Mundo!" << std::endl;
    return 0;
}
```

## Debug & Execution
- **Launch Config**: Use `(Windows) Launch` configuration in `launch.json` to run compiled executables
- **External Terminal**: Debug runs in external console window (configured via `"console": "externalTerminal"`)
- **Breakpoint Support**: Configured for both MSVC (Windows debugger) and GDB debugging

## Common AI Tasks
- **Adding Features**: Create new `.cpp` files in `.vscode/` directory and compile with the standard build task
- **Algorithm Implementation**: Follow single-file pattern; use standard library headers for utility functions
- **Code Formatting**: Ensure `#include` statements use angle brackets (e.g., `<iostream>`), not quotes
- **Warning Resolution**: The project enables strict warnings; address all compiler warnings before considering work complete

## External Dependencies
- **MinGW GCC**: Primary C++ toolchain (C++11 and later supported via default settings)
- **Standard Library**: Full access to C++ standard library via IntelliSense
- **No Package Manager**: Project uses only built-in GCC capabilities

## Notes for AI Agents
- Executables are generated in `.vscode/` directory, not in a separate `build/` folder (despite the `build/` directory existing)
- The project prioritizes educational clarity over advanced C++ features
- When suggesting code improvements, keep in mind this is a learning project—prefer clarity over optimization
