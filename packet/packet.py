from packet.packet_constants import *
from packet.err_detection import *

class Packet:
    def __init__(self, type,checksumFunc=None, len=0, seq=0, data=''):
        self._type =type
        self._len = len
        self._seq = seq
        self._data = data
        if (checksumFunc!=None):
            self._checksum = checksumFunc(self)

    def get_type(self):
        return self._type
    def set_type(self, typed):
        self._type = typed
    type = property(get_type, set_type)

    def get_len(self):
        return self._len
    def set_len(self, len):
        self._len = len
    len = property(get_len, set_len)

    def get_seq(self):
        return self._seq
    def set_seq(self, seq):
        self._seq = seq
    seq = property(get_seq, set_seq)

    def get_checksum(self):
        return self._checksum
    def set_checksum(self, checksum):
        self._checksum = checksum
    checksum =property(get_checksum, set_checksum)

    def get_data(self):
        return self._data
    def set_data(self, data):
        self._data = data
    data = property(get_data, set_data)

    def toString(self):
        strPkt = 'r' + str(self.type).zfill(SIZE_OF_BYTE)
        if (self.type == DATA_PACKET):
            strPkt+= str(self.len).zfill(SIZE_OF_BYTE)+str(self.seq)+str(self.checksum).zfill(SIZE_OF_BYTE)+self.data
        elif (self.type == ACK_PACKET):
            strPkt+=  str(self.seq)+ str(self.checksum).zfill(SIZE_OF_BYTE)
        elif (self.type== FIN_PACKET):
            strPkt+= str(self.checksum).zfill(SIZE_OF_BYTE)
        strPkt+= '0'
        return strPkt

    # def dataPacket2Str(self):
    #     packet= 'r'+str(DATA_PACKET)+ str(self.len).zfill(SIZE_OF_BYTE)+str(self.seq)+ str(self.checksum).zfill(SIZE_OF_BYTE)+self.data
    #     packet+='0' #TODO: changeit
    #     return packet

    # def ackPacket2Str(self):
    #     packet = 'r' + str(ACK_PACKET) + str(self.seq)+ str(self.checksum).zfill(SIZE_OF_BYTE)
    #     packet += '0'  # TODO: changeit
    #     return packet

    # def finPacket2Str (self):
    #     packet = 'r' + str(FIN_PACKET)+str(self.checksum).zfill(SIZE_OF_BYTE)
    #     packet += '0'  # TODO: changeit
    #     return packet