from src.data_processors.interfaces.ifile_manager import IFileManager
import numpy as np
import struct

class FileManager(IFileManager):

    @staticmethod
    def read(file_name):
        try:
            f = open(file_name, "rb")
            id_surfer = f.read(4).decode("utf-8")
            amount_x = int.from_bytes(f.read(2), "little")  # кол-во ячеек по Х
            amount_y = int.from_bytes(f.read(2), "little")  # кол-во ячеек по Y
            region_bound = struct.unpack('6d', f.read(6 * 8))

            dem = np.zeros((amount_x, amount_y))
            for x in range(amount_x):
                for y in range(amount_y):
                    temp = struct.unpack('f', f.read(4))
                    dem[x][y] = temp[0]
        except IOError:
            print("An IOError has occurred!")
        finally:
            f.close()
        return dem, region_bound[:4], amount_x, amount_y

    @staticmethod
    def write(file_name, dem, region_bound, amount_x, amount_y):
        id_surfer = "DSBB"
        try:
            f = open(file_name, "wb")
            f.write(id_surfer.encode("utf-8"))
            f.write(struct.pack('h', amount_x))
            f.write(struct.pack('h', amount_y))
            f.write(struct.pack('6d',
                                region_bound[0], region_bound[1], region_bound[2], region_bound[3],
                                np.min(dem), np.max(dem)))
            for x in range(amount_x):
                for y in range(amount_y):
                    f.write(struct.pack('f', dem[x][y]))
        except IOError:
            print("An IOError has occurred!")
        finally:
            f.close()