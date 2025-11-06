# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HardwareSummary:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sn': 'str',
        'manufacturer': 'str',
        'model': 'str',
        'main_board_manufacturer': 'str',
        'main_board_serial_number': 'str'
    }

    attribute_map = {
        'sn': 'sn',
        'manufacturer': 'manufacturer',
        'model': 'model',
        'main_board_manufacturer': 'main_board_manufacturer',
        'main_board_serial_number': 'main_board_serial_number'
    }

    def __init__(self, sn=None, manufacturer=None, model=None, main_board_manufacturer=None, main_board_serial_number=None):
        r"""HardwareSummary

        The model defined in huaweicloud sdk

        :param sn: serial number
        :type sn: str
        :param manufacturer: 制造商
        :type manufacturer: str
        :param model: 型号
        :type model: str
        :param main_board_manufacturer: 主板厂商
        :type main_board_manufacturer: str
        :param main_board_serial_number: 主板序列号
        :type main_board_serial_number: str
        """
        
        

        self._sn = None
        self._manufacturer = None
        self._model = None
        self._main_board_manufacturer = None
        self._main_board_serial_number = None
        self.discriminator = None

        self.sn = sn
        self.manufacturer = manufacturer
        self.model = model
        if main_board_manufacturer is not None:
            self.main_board_manufacturer = main_board_manufacturer
        if main_board_serial_number is not None:
            self.main_board_serial_number = main_board_serial_number

    @property
    def sn(self):
        r"""Gets the sn of this HardwareSummary.

        serial number

        :return: The sn of this HardwareSummary.
        :rtype: str
        """
        return self._sn

    @sn.setter
    def sn(self, sn):
        r"""Sets the sn of this HardwareSummary.

        serial number

        :param sn: The sn of this HardwareSummary.
        :type sn: str
        """
        self._sn = sn

    @property
    def manufacturer(self):
        r"""Gets the manufacturer of this HardwareSummary.

        制造商

        :return: The manufacturer of this HardwareSummary.
        :rtype: str
        """
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer):
        r"""Sets the manufacturer of this HardwareSummary.

        制造商

        :param manufacturer: The manufacturer of this HardwareSummary.
        :type manufacturer: str
        """
        self._manufacturer = manufacturer

    @property
    def model(self):
        r"""Gets the model of this HardwareSummary.

        型号

        :return: The model of this HardwareSummary.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        r"""Sets the model of this HardwareSummary.

        型号

        :param model: The model of this HardwareSummary.
        :type model: str
        """
        self._model = model

    @property
    def main_board_manufacturer(self):
        r"""Gets the main_board_manufacturer of this HardwareSummary.

        主板厂商

        :return: The main_board_manufacturer of this HardwareSummary.
        :rtype: str
        """
        return self._main_board_manufacturer

    @main_board_manufacturer.setter
    def main_board_manufacturer(self, main_board_manufacturer):
        r"""Sets the main_board_manufacturer of this HardwareSummary.

        主板厂商

        :param main_board_manufacturer: The main_board_manufacturer of this HardwareSummary.
        :type main_board_manufacturer: str
        """
        self._main_board_manufacturer = main_board_manufacturer

    @property
    def main_board_serial_number(self):
        r"""Gets the main_board_serial_number of this HardwareSummary.

        主板序列号

        :return: The main_board_serial_number of this HardwareSummary.
        :rtype: str
        """
        return self._main_board_serial_number

    @main_board_serial_number.setter
    def main_board_serial_number(self, main_board_serial_number):
        r"""Sets the main_board_serial_number of this HardwareSummary.

        主板序列号

        :param main_board_serial_number: The main_board_serial_number of this HardwareSummary.
        :type main_board_serial_number: str
        """
        self._main_board_serial_number = main_board_serial_number

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        import simplejson as json
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, HardwareSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
