import os
import tempfile
import pytest
from unittest.mock import Mock, patch
from qrcode import QRCode
from segno import DataOverflowError
from qrdata.data_check import DataChecker
from qrdata.enums import QrCodeMode
from qrdata.logger import CUILogger
from qrdata.qrcode_generator import QRCodeGenerator

class TestNumeric:
    @pytest.fixture
    def qrcode_generator(self):
        # Create a mock logger
        logger = CUILogger()
        # Create an instance of QRCodeGenerator
        generator = QRCodeGenerator(logger)
        return generator

    def test_1_l_41(self, qrcode_generator):
        output_dir = tempfile.mkdtemp()
        # Set up the mock objects
        with open("tests/data/i_41.txt", "rb") as file:
            data = file.read()

        # Call the method to test
        qrcode_generator.generate_qrcodes(1, "L", QrCodeMode.Numeric, data, "ascii", output_dir)

        #判断output_dir中文件个数为1
        assert len(os.listdir(output_dir)) == 1

        checker = DataChecker(data, "ascii", output_dir, qrcode_generator.logger)
        res1 = checker.check_data('pyzbar')
        res2 = checker.check_data('zxing')
        assert res1 == True or res2 == True

    def test_1_h_41(self, qrcode_generator):
        output_dir = tempfile.mkdtemp()
        # Set up the mock objects
        with open("tests/data/i_41.txt", "rb") as file:
            data = file.read()

        # Call the method to test
        qrcode_generator.generate_qrcodes(1, "H", QrCodeMode.Numeric, data, "ascii", output_dir)

        #判断output_dir中文件个数为1
        assert len(os.listdir(output_dir)) == 3

        checker = DataChecker(data, "ascii", output_dir, qrcode_generator.logger)
        res1 = checker.check_data('pyzbar')
        res2 = checker.check_data('zxing')
        assert res1 == True or res2 == True

    def test_1_l_42(self, qrcode_generator):
        output_dir = tempfile.mkdtemp()
        # Set up the mock objects
        with open("tests/data/i_42.txt", "rb") as file:
            data = file.read()

        # Call the method to test
        qrcode_generator.generate_qrcodes(1, "L", QrCodeMode.Numeric, data, "ascii", output_dir)

        #判断output_dir中文件个数为1
        assert len(os.listdir(output_dir)) == 2

        checker = DataChecker(data, "ascii", output_dir, qrcode_generator.logger)
        res1 = checker.check_data('pyzbar')
        res2 = checker.check_data('zxing')
        assert res1 == True or res2 == True

    def test_40_l_7089(self, qrcode_generator):
        output_dir = tempfile.mkdtemp()
        # Set up the mock objects
        with open("tests/data/i_7089.txt", "rb") as file:
            data = file.read()

        # Call the method to test
        qrcode_generator.generate_qrcodes(40, "L", QrCodeMode.Numeric, data, "ascii", output_dir)

        #判断output_dir中文件个数为1
        assert len(os.listdir(output_dir)) == 1

        checker = DataChecker(data, "ascii", output_dir, qrcode_generator.logger)
        res1 = checker.check_data('pyzbar')
        res2 = checker.check_data('zxing')
        assert res1 == True or res2 == True

    def test_1_h_40_lf(self, qrcode_generator):
        output_dir = tempfile.mkdtemp()
        # Set up the mock objects
        with open("tests/data/i_40_lf.txt", "rb") as file:
            data = file.read()

        # Call the method to test
        try:
            qrcode_generator.generate_qrcodes(1, "L", QrCodeMode.Numeric, data, "ascii", output_dir)
        except Exception as e:
            assert isinstance(e,ValueError)
            assert "Proposal: byte" in str(e)

class TestAlphanumeric:
    @pytest.fixture
    def qrcode_generator(self):
        # Create a mock logger
        logger = CUILogger()
        # Create an instance of QRCodeGenerator
        generator = QRCodeGenerator(logger)
        return generator

    def test_1_l_25(self, qrcode_generator):
        output_dir = tempfile.mkdtemp()
        # Set up the mock objects
        with open("tests/data/A_25.txt", "rb") as file:
            data = file.read()

        # Call the method to test
        qrcode_generator.generate_qrcodes(1, "L", QrCodeMode.Alphanumeric, data, "ascii", output_dir)

        #判断output_dir中文件个数为1
        assert len(os.listdir(output_dir)) == 1

        checker = DataChecker(data, "ascii", output_dir, qrcode_generator.logger)
        res1 = checker.check_data('pyzbar')
        res2 = checker.check_data('zxing')
        assert res1 == True or res2 == True

    def test_40_l_4296(self, qrcode_generator):
        output_dir = tempfile.mkdtemp()
        # Set up the mock objects
        with open("tests/data/A_4296.txt", "rb") as file:
            data = file.read()

        # Call the method to test
        qrcode_generator.generate_qrcodes(40, "L", QrCodeMode.Alphanumeric, data, "ascii", output_dir)

        #判断output_dir中文件个数为1
        assert len(os.listdir(output_dir)) == 1

        checker = DataChecker(data, "ascii", output_dir, qrcode_generator.logger)
        res1 = checker.check_data('pyzbar')
        res2 = checker.check_data('zxing')
        assert res1 == True or res2 == True

class TestEnText:
    @pytest.fixture
    def qrcode_generator(self):
        # Create a mock logger
        logger = CUILogger()
        # Create an instance of QRCodeGenerator
        generator = QRCodeGenerator(logger)
        return generator

    def test_1_l_17(self, qrcode_generator):
        output_dir = tempfile.mkdtemp()
        # Set up the mock objects
        with open("tests/data/a_17.txt", "rb") as file:
            data = file.read()

        # Call the method to test
        qrcode_generator.generate_qrcodes(1, "L", QrCodeMode.Byte, data, "ascii", output_dir)

        #判断output_dir中文件个数为1
        assert len(os.listdir(output_dir)) == 1

        checker = DataChecker(data, "ascii", output_dir, qrcode_generator.logger)
        res1 = checker.check_data('pyzbar')
        res2 = checker.check_data('zxing')
        assert res1 == True or res2 == True

    def test_40_l_2953(self, qrcode_generator):
        output_dir = tempfile.mkdtemp()
        # Set up the mock objects
        with open("tests/data/a_2953.txt", "rb") as file:
            data = file.read()

        # Call the method to test
        qrcode_generator.generate_qrcodes(40, "L", QrCodeMode.Byte, data, "ascii", output_dir)
        
        #判断output_dir中文件个数为1
        assert len(os.listdir(output_dir)) == 1

        checker = DataChecker(data, "ascii", output_dir, qrcode_generator.logger)
        res1 = checker.check_data('pyzbar')
        res2 = checker.check_data('zxing')
        assert res1 == True or res2 == True

    def test_40_l_2954(self, qrcode_generator):
        output_dir = tempfile.mkdtemp()
        # Set up the mock objects
        with open("tests/data/a_2954.txt", "rb") as file:
            data = file.read()
            data_len = len(data)
            print(data_len)

        # Call the method to test
        qrcode_generator.generate_qrcodes(40, "L", QrCodeMode.Byte, data, "ascii", output_dir)
        
        #判断output_dir中文件个数为1
        assert len(os.listdir(output_dir)) == 2

        checker = DataChecker(data, "ascii", output_dir, qrcode_generator.logger)
        res1 = checker.check_data('pyzbar')
        res2 = checker.check_data('zxing')
        assert res1 == True or res2 == True

class TestZhText:
    @pytest.fixture
    def qrcode_generator(self):
        # Create a mock logger
        logger = CUILogger()
        # Create an instance of QRCodeGenerator
        generator = QRCodeGenerator(logger)
        return generator

    def test_1_l_5_utf8(self, qrcode_generator):
        output_dir = tempfile.mkdtemp()
        # Set up the mock objects
        with open("tests/data/c_5_utf8.txt", "rb") as file:
            data = file.read()

        # Call the method to test
        qrcode_generator.generate_qrcodes(1, "L", QrCodeMode.Byte, data, "utf-8", output_dir)

        #判断output_dir中文件个数为1
        assert len(os.listdir(output_dir)) == 1

        checker = DataChecker(data, "utf-8", output_dir, qrcode_generator.logger)
        res1 = checker.check_data('pyzbar')
        res2 = checker.check_data('zxing')
        assert res1 == True or res2 == True

    def test_1_l_6_utf8(self, qrcode_generator):
        output_dir = tempfile.mkdtemp()
        # Set up the mock objects
        with open("tests/data/c_6_utf8.txt", "rb") as file:
            data = file.read()

        # Call the method to test
        try:
            qrcode_generator.generate_qrcodes(1, "L", QrCodeMode.Byte, data, "utf-8", output_dir)
        except Exception as e:
            assert isinstance(e,DataOverflowError)

    def test_40_l_984_utf8(self, qrcode_generator):
        output_dir = tempfile.mkdtemp()
        # Set up the mock objects
        with open("tests/data/c_984_utf8.txt", "rb") as file:
            data = file.read()

        # Call the method to test
        qrcode_generator.generate_qrcodes(40, "L", QrCodeMode.Byte, data, "utf-8", output_dir)

        #判断output_dir中文件个数为1
        assert len(os.listdir(output_dir)) == 1

        checker = DataChecker(data, "utf-8", output_dir, qrcode_generator.logger)
        res1 = checker.check_data('pyzbar')
        res2 = checker.check_data('zxing')
        assert res1 == True or res2 == True
    
    def test_40_l_985_utf8(self, qrcode_generator):
        output_dir = tempfile.mkdtemp()
        # Set up the mock objects
        with open("tests/data/c_985_utf8.txt", "rb") as file:
            data = file.read()

        # Call the method to test
        qrcode_generator.generate_qrcodes(40, "L", QrCodeMode.Byte, data, "utf-8", output_dir)

        #判断output_dir中文件个数为1
        assert len(os.listdir(output_dir)) == 2

        checker = DataChecker(data, "utf-8", output_dir, qrcode_generator.logger)
        res1 = checker.check_data('pyzbar')
        res2 = checker.check_data('zxing')
        assert res1 == True or res2 == True

    def test_1_l_6_gbk(self, qrcode_generator):
        output_dir = tempfile.mkdtemp()
        # Set up the mock objects
        with open("tests/data/c_6_gbk.txt", "rb") as file:
            data = file.read()

        # Call the method to test
        qrcode_generator.generate_qrcodes(1, "L", QrCodeMode.Byte, data, "gbk", output_dir)

        #判断output_dir中文件个数为1
        assert len(os.listdir(output_dir)) == 1

        checker = DataChecker(data, "gbk", output_dir, qrcode_generator.logger)
        res1 = checker.check_data('pyzbar')
        res2 = checker.check_data('zxing')
        assert res1 == True or res2 == True

    def test_1_l_7_gbk(self, qrcode_generator):
        output_dir = tempfile.mkdtemp()
        # Set up the mock objects
        with open("tests/data/c_7_gbk.txt", "rb") as file:
            data = file.read()

        # Call the method to test
        qrcode_generator.generate_qrcodes(1, "L", QrCodeMode.Byte, data, "gbk", output_dir)

        #判断output_dir中文件个数为1
        assert len(os.listdir(output_dir)) == 2

        checker = DataChecker(data, "gbk", output_dir, qrcode_generator.logger)
        res1 = checker.check_data('pyzbar')
        res2 = checker.check_data('zxing')
        assert res1 == True or res2 == True

    def test_40_l_1107_gbk(self, qrcode_generator):
        output_dir = tempfile.mkdtemp()
        # Set up the mock objects
        with open("tests/data/c_1107_gbk.txt", "rb") as file:
            data = file.read()

        # Call the method to test
        qrcode_generator.generate_qrcodes(40, "L", QrCodeMode.Byte, data, "gbk", output_dir)

        #判断output_dir中文件个数为1
        assert len(os.listdir(output_dir)) == 1

        checker = DataChecker(data, "gbk", output_dir, qrcode_generator.logger)
        res1 = checker.check_data('pyzbar')
        res2 = checker.check_data('zxing')
        assert res1 == True or res2 == True

    def test_40_l_1108_gbk(self, qrcode_generator):
        output_dir = tempfile.mkdtemp()
        # Set up the mock objects
        with open("tests/data/c_1108_gbk.txt", "rb") as file:
            data = file.read()

        # Call the method to test
        qrcode_generator.generate_qrcodes(40, "L", QrCodeMode.Byte, data, "gbk", output_dir)

        #判断output_dir中文件个数为1
        assert len(os.listdir(output_dir)) == 2

        checker = DataChecker(data, "gbk", output_dir, qrcode_generator.logger)
        res1 = checker.check_data('pyzbar')
        res2 = checker.check_data('zxing')
        assert res1 == True or res2 == True

class TestByte:
    @pytest.fixture
    def qrcode_generator(self):
        # Create a mock logger
        logger = CUILogger()
        # Create an instance of QRCodeGenerator
        generator = QRCodeGenerator(logger)
        return generator

    def test_40_l_2214(self, qrcode_generator):
        output_dir = tempfile.mkdtemp()
        # Set up the mock objects
        with open("tests/data/b_2214.txt", "rb") as file:
            data = file.read()

        # Call the method to test
        qrcode_generator.generate_qrcodes(40, "L", QrCodeMode.Byte, data, "binary", output_dir)

        #判断output_dir中文件个数为1
        assert len(os.listdir(output_dir)) == 1

        checker = DataChecker(data, "binary", output_dir, qrcode_generator.logger)
        res1 = checker.check_data('pyzbar')
        res2 = checker.check_data('zxing')
        assert res1 == True or res2 == True

    def test_40_l_2215(self, qrcode_generator):
        output_dir = tempfile.mkdtemp()
        # Set up the mock objects
        with open("tests/data/b_2215.txt", "rb") as file:
            data = file.read()

        # Call the method to test
        qrcode_generator.generate_qrcodes(40, "L", QrCodeMode.Byte, data, "binary", output_dir)

        #判断output_dir中文件个数为1
        assert len(os.listdir(output_dir)) == 2

        checker = DataChecker(data, "binary", output_dir, qrcode_generator.logger)
        res1 = checker.check_data('pyzbar')
        res2 = checker.check_data('zxing')
        assert res1 == True or res2 == True