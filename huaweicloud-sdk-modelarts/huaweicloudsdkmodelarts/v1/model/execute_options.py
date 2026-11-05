# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExecuteOptions:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'serial_number': 'str'
    }

    attribute_map = {
        'serial_number': 'serialNumber'
    }

    def __init__(self, serial_number=None):
        r"""ExecuteOptions

        The model defined in huaweicloud sdk

        :param serial_number: **参数解释**：序列号。
        :type serial_number: str
        """
        
        

        self._serial_number = None
        self.discriminator = None

        if serial_number is not None:
            self.serial_number = serial_number

    @property
    def serial_number(self):
        r"""Gets the serial_number of this ExecuteOptions.

        **参数解释**：序列号。

        :return: The serial_number of this ExecuteOptions.
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        r"""Sets the serial_number of this ExecuteOptions.

        **参数解释**：序列号。

        :param serial_number: The serial_number of this ExecuteOptions.
        :type serial_number: str
        """
        self._serial_number = serial_number

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
        if not isinstance(other, ExecuteOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
