padInternal = ["4B", "49", "54", "49", \
               "50", "00", "00", "00", \
               "00", "00", "00", "00", \
               "00", "00", "00", "00", \
               "00", "00", "00", "00", \
               "00", "00", "00", "00", \
               "00", "00", "00", "00", \
               "00", "00", "00", "00", \
               "00", "00", "00", "15", \
               "00", "06", "00", "00", \
               "00", "05", "00", "20", \
               "01", "04", "08", "10", \
               "02", "04", "08", "10", \
               "03", "00", "00", "20", \
               "08", "00", "00", "7F", \
               "09", "00", "00", "03", \
               "00", "00", "00", "00", \
               "00", "00", "00", "00", \
               "00", "00", "00", "00", \
               "00", "00", "00", "00", \
               "00", "00", "00", "00", \
               "00", "00", "00", "00"]

samplesInternal = ["808 Kick", \
                   "808 SNR", \
                   "Hat", \
                   "Clap", \
                   "Pluck8Bt", \
                   "Bass1 C2", \
                   "UH", \
                   "Yea", \
                   "909 Kick", \
                   "S-Ressy", \
                   "808 HH O", \
                   "808 HH C", \
                   "808 Tom", \
                   "SynthStb", \
                   "Trans FX", \
                   "Gunshot", \
                   "K-Harder", \
                   "Rimshot", \
                   "Airhorn", \
                   "ABass C2", \
                   "NoSample"]

print padInternal

sample = samplesInternal[1]
padInternal[15] = format(len(sample), '#04x').split('x')[-1].upper()

for index in range(len(sample)):
    padInternal[index+16] = hex(ord(sample[index])).split('x')[-1].upper()

print padInternal
