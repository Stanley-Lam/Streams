import unittest
import bitstreams
from queue import *

class TestBitstreams(unittest.TestCase):
    def test01_density(self):
        msg = "Testing the density of a trivial stream"

        bits = [0]
        stream = (bit for bit in bits)
        density = bitstreams.find_density(stream, 1)

        self.assertAlmostEqual(density, 0.0, 7, msg)

    def test02_density(self):
        msg = "Testing the density of a stream"

        bits = [0, 1, 1, 0, 1, 1, 0, 0]
        stream = (bit for bit in bits)
        density = bitstreams.find_density(stream, 4)

        self.assertAlmostEqual(density, 2.4, 7, msg)

    def test03_pattern(self):
        msg = "Testing patterns within a trivial stream"

        bits = [0]
        stream = (bit for bit in bits)
        indices = bitstreams.find_pattern(stream, 1, [0])

        self.assertEqual(size(indices), 1, msg)
        self.assertEqual(dequeue(indices), 0, msg)

    def test04_pattern(self):
        msg = "Testing patterns within a stream"

        bits = [0, 1, 1, 0, 1, 1, 0, 0]
        stream = (bit for bit in bits)
        indices = bitstreams.find_pattern(stream, 4, [0, 1, 1, 0])

        self.assertEqual(size(indices), 2, msg)
        self.assertEqual(dequeue(indices), 0, msg)
        self.assertEqual(dequeue(indices), 3, msg)

    def test05_density(self):
        msg = "Testing width greater than stream"

        bits = [0]
        stream = (bit for bit in bits)

        with self.assertRaises(ZeroDivisionError): (bitstreams.find_density(stream, 4), msg)


    def test06_pattern(self):
        msg = "Testing patterns within a stream"

        bits = [0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1]
        stream = (bit for bit in bits)
        indices = bitstreams.find_pattern(stream, 5, [0, 1, 1, 1, 0])

        self.assertEqual(size(indices), 2, msg)
        self.assertEqual(dequeue(indices), 0, msg)
        self.assertEqual(dequeue(indices), 5, msg)

if __name__ == "__main__":
    unittest.main()
