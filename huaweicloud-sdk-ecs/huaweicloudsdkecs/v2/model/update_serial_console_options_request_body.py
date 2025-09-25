# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateSerialConsoleOptionsRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'serial_console_options': 'UpdateSerialConsoleOptionsOption'
    }

    attribute_map = {
        'serial_console_options': 'serial_console_options'
    }

    def __init__(self, serial_console_options=None):
        r"""UpdateSerialConsoleOptionsRequestBody

        The model defined in huaweicloud sdk

        :param serial_console_options: 
        :type serial_console_options: :class:`huaweicloudsdkecs.v2.UpdateSerialConsoleOptionsOption`
        """
        
        

        self._serial_console_options = None
        self.discriminator = None

        if serial_console_options is not None:
            self.serial_console_options = serial_console_options

    @property
    def serial_console_options(self):
        r"""Gets the serial_console_options of this UpdateSerialConsoleOptionsRequestBody.

        :return: The serial_console_options of this UpdateSerialConsoleOptionsRequestBody.
        :rtype: :class:`huaweicloudsdkecs.v2.UpdateSerialConsoleOptionsOption`
        """
        return self._serial_console_options

    @serial_console_options.setter
    def serial_console_options(self, serial_console_options):
        r"""Sets the serial_console_options of this UpdateSerialConsoleOptionsRequestBody.

        :param serial_console_options: The serial_console_options of this UpdateSerialConsoleOptionsRequestBody.
        :type serial_console_options: :class:`huaweicloudsdkecs.v2.UpdateSerialConsoleOptionsOption`
        """
        self._serial_console_options = serial_console_options

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpdateSerialConsoleOptionsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
