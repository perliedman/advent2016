def bitParity(x):
   x ^= x >> 16
   x ^= x >> 8
   x ^= x >> 4
   x &= 0xf

   return (0x6996 >> x) & 1;