The Akai MPX8 uses an SD card to load external samples and save KIT files.

The KIT file format contains the the file information, the kit information, and the information about how the various pads are configured.

The file is broken down as follows:
  File header         - 60 bytes
  Kit header          - 50 bytes
  Pad data (internal) - 704 bytes
  Pad data (external) - 704 bytes
