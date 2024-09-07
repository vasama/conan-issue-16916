#pragma once

template<typename T>
struct lib_t
{
	using pointer = T*;
	void const* p;
	unsigned long long s;
};
