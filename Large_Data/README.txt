
Some information about the two files:


* General format (binary):
  
  - There is a small header at the beginning of each file:

    n -> number of particles in file (32 bit integer)

    time of snapshot (double precision floating point, 64 bits)

  - Then there are n rows of particle data:  m, x, y, z, vx, vy, vz, each of which is written in single precision floating point (32 bits each).  m is the mass of the particle, x, y, z, physical space coords, and vx, vy, vz, velocities.

  - These were written in C, not fortran, so nothing funny going on in terms of how the bytes are packed.


  
* The file "snapshot_10.dat" is a little over 2 million particles and is supposed to be a large sample of the universe (dark matter only).  It should make a pretty image.


* The file "halo.dat" is one smaller dark matter halo (i.e., a small clump of particles) within the larger snapshot.  It was constructed using friends-of-friends techniques.  You should be able to find a fairly good power-law density profile by binning the number of particles by radius.


