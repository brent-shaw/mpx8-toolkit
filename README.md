The Akai MPX8 uses an SD card to load external samples and save KIT files.

The KIT file format contains the the file information, the kit information, and the information about how the various pads are configured.

The file is broken down as follows:
  File header         - 60 bytes
  Kit header          - 50 bytes
  Pad data (internal) - 704 bytes
  Pad data (external) - 704 bytes

The file header is comprised as follows:

  # 4B 49 54 48 // File header
  # 80 00 00 00
  # E4 00 08 08 // Checksum or something
  # 00 20 00 20
  # 00 00 00 03
  # 00 10 00 20
  # 00 00 00 00
  # 00 00 0C 18
  # 00 00 0C 18
  # 00 00 0C 18
  # 00 00 0C 18
  # 00 00 0C 18
  # 00 00 0C 18
  # 00 00 0C 18
  # 00 00 00 00
  # 00 00 00 00
  # 00 00 00 00
  # 00 00 00 00

The kit header is comprised as follows:

  # 4B 49 54 30 // Kit name
  # 30 33 00 00
  # 00 00 00 00
  # 00 00 00 00
  # 00 00 00 00
  # 00 00 00 00
  # 00 00 00 00
  # 00 00 00 00
  # 00 00 00 00
  # 00 00 00 00
  # 00 00 00 00
  # 00 00 00 00
  # 00 00 00 00
  # 00 00 00 00
  
Each pad has data for both interal and external samples.
The internal pad data layout for each pad is as follows:

  # 4B 49 54 49 // Sample
  # 50 00 00 00 // Holder
  # 00 00 00 00 // Sample location (internal)
  # 00 00 00 08 // Name length
  # 38 30 38 20 // Name (808 Kick)
  # 4B 69 63 6B
  # 00 00 00 00
  # 00 00 00 00
  # 00 00 00 15 // Holder
  # 00 06 00 00 // Holder
  # 00 01 00 20 // Level     00 XX 00 20 (00 to 20)
  # 01 05 08 10 // Tune      01 XX 08 10 (00 to 08)
  # 02 04 08 10 // Panning   02 XX 08 10 (00 to 08)
  # 03 01 00 0A // Reverb    03 XX 00 20 (00 to 0A)
  # 08 01 00 7F // Midi      08 XX 00 7F (00 to 7F)
  # 09 00 00 03 // Trigger   09 XX 00 03 (00 to 03)
  # 00 00 00 00
  # 00 00 00 00
  # 00 00 00 00
  # 00 00 00 00
  # 00 00 00 00
  # 00 00 00 00

The external sample pad data for each pad is as follows:

  # 4B 49 54 49 // Sample
  # 50 00 00 00 // Holder
  # FF AA 00 00 // Sample location (card)
  # 00 00 00 08 // Name length
  # 3C 45 6D 70 // Name (<Empty> )
  # 74 79 3E 20
  # 00 00 00 00
  # 00 00 00 00
  # 00 00 01 00 //Holder card
  # 00 06 00 00 // Holder
  # 00 01 00 20 // Level     00 XX 00 20 (00 to 0A)
  # 01 05 08 10 // Tune      01 XX 08 10 (00 to 08)
  # 02 04 08 10 // Panning   02 XX 08 10 (00 to 08)
  # 03 01 00 20 // Reverb    03 XX 00 20 (00 to 0A)
  # 08 01 00 7F // Midi      08 XX 00 7F (00 to 7F)
  # 09 00 00 03 // Trigger   09 XX 00 03 (00 to 03)
  # 00 00 00 00
  # 00 00 00 00
  # 00 00 00 00
  # 00 00 00 00
  # 00 00 00 00
  # 00 00 00 00
 
