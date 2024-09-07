#include <my/lib.hpp>

#include <iostream>

int main()
{
	lib_t<char> x;
	x.p = "hello";
	x.s = 5;

	// put breakpoint here for debugging:
	[[maybe_unused]] int y = 0;
}
