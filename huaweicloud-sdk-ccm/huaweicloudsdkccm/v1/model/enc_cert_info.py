# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EncCertInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enc_serial_number': 'str'
    }

    attribute_map = {
        'enc_serial_number': 'enc_serial_number'
    }

    def __init__(self, enc_serial_number=None):
        r"""EncCertInfo

        The model defined in huaweicloud sdk

        :param enc_serial_number: 加密证书序列号。
        :type enc_serial_number: str
        """
        
        

        self._enc_serial_number = None
        self.discriminator = None

        self.enc_serial_number = enc_serial_number

    @property
    def enc_serial_number(self):
        r"""Gets the enc_serial_number of this EncCertInfo.

        加密证书序列号。

        :return: The enc_serial_number of this EncCertInfo.
        :rtype: str
        """
        return self._enc_serial_number

    @enc_serial_number.setter
    def enc_serial_number(self, enc_serial_number):
        r"""Sets the enc_serial_number of this EncCertInfo.

        加密证书序列号。

        :param enc_serial_number: The enc_serial_number of this EncCertInfo.
        :type enc_serial_number: str
        """
        self._enc_serial_number = enc_serial_number

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
        if not isinstance(other, EncCertInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
