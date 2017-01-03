#pragma once

/**
\brief Executes a python script.
\param szFileName Path to the file (UTF-8).
\return true if it succeeds, false if it fails.
*/
extern "C" __declspec(dllimport) bool ExecutePythonScriptA(const char* szFileName);

/**
\brief Executes a python script.
\param szFileName Path to the file (UTF-8).
\param argc Number of arguments to pass to the python script.
\param argv Array of arguments to pass to the python script (UTF-8).
\return true if it succeeds, false if it fails.
*/
extern "C" __declspec(dllimport) bool ExecutePythonScriptExA(const char* szFileName, int argc, char* argv[]);

/**
\brief Executes a python script.
\param szFileName Path to the file (UTF-16).
\return true if it succeeds, false if it fails.
*/
extern "C" __declspec(dllimport) bool ExecutePythonScriptW(const wchar_t* szFileName);

/**
\brief Executes a python script.
\param szFileName Path to the file (UTF-16).
\param argc Number of arguments to pass to the python script.
\param argv Array of arguments to pass to the python script (UTF-16).
\return true if it succeeds, false if it fails.
*/
extern "C" __declspec(dllimport) bool ExecutePythonScriptExW(const wchar_t* szFileName, int argc, wchar_t* argv[]);
