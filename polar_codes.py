from helper import *

N,k = DefineParam()
rel_seq = [i for i in reliabiility_sequence32 if i<=N]
rel_msg_channels = rel_seq[-k:]
rel_msg_channels.sort()

raw_msg = input("Enter Message bits: ")
msg = makeProper(raw_msg,N,rel_msg_channels)
codeword = msg.copy()

Encoder(codeword,N,N)
modulated =  ApplyBPSK(codeword)
noise = np.random.normal(0, 0.1, (N))
received = modulated+noise

i = [0]
decoded = [0]*N
orig = Decoder(received,rel_msg_channels,i,decoded)
decoded = finalDecoding(decoded,rel_msg_channels)

print("Reliable Channels: ",rel_msg_channels)
print("msg: ", msg)
print("Polar Code: ", codeword)
print("decoded: ", decoded)