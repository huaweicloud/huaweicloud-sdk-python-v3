# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EncryptDataReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'encrypt_data': 'EncryptDataIn'
    }

    attribute_map = {
        'encrypt_data': 'encrypt_data'
    }

    def __init__(self, encrypt_data=None):
        r"""EncryptDataReq

        The model defined in huaweicloud sdk

        :param encrypt_data: 
        :type encrypt_data: :class:`huaweicloudsdkief.v1.EncryptDataIn`
        """
        
        

        self._encrypt_data = None
        self.discriminator = None

        self.encrypt_data = encrypt_data

    @property
    def encrypt_data(self):
        r"""Gets the encrypt_data of this EncryptDataReq.

        :return: The encrypt_data of this EncryptDataReq.
        :rtype: :class:`huaweicloudsdkief.v1.EncryptDataIn`
        """
        return self._encrypt_data

    @encrypt_data.setter
    def encrypt_data(self, encrypt_data):
        r"""Sets the encrypt_data of this EncryptDataReq.

        :param encrypt_data: The encrypt_data of this EncryptDataReq.
        :type encrypt_data: :class:`huaweicloudsdkief.v1.EncryptDataIn`
        """
        self._encrypt_data = encrypt_data

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
        if not isinstance(other, EncryptDataReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
