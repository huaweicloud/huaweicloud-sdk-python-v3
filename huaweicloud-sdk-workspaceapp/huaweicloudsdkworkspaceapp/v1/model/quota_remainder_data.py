# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QuotaRemainderData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'QuotaResourceTypeEnum',
        'remainder': 'int',
        'need': 'int'
    }

    attribute_map = {
        'type': 'type',
        'remainder': 'remainder',
        'need': 'need'
    }

    def __init__(self, type=None, remainder=None, need=None):
        """QuotaRemainderData

        The model defined in huaweicloud sdk

        :param type: 
        :type type: :class:`huaweicloudsdkworkspaceapp.v1.QuotaResourceTypeEnum`
        :param remainder: 剩余配额
        :type remainder: int
        :param need: 所需配额
        :type need: int
        """
        
        

        self._type = None
        self._remainder = None
        self._need = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if remainder is not None:
            self.remainder = remainder
        if need is not None:
            self.need = need

    @property
    def type(self):
        """Gets the type of this QuotaRemainderData.

        :return: The type of this QuotaRemainderData.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.QuotaResourceTypeEnum`
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this QuotaRemainderData.

        :param type: The type of this QuotaRemainderData.
        :type type: :class:`huaweicloudsdkworkspaceapp.v1.QuotaResourceTypeEnum`
        """
        self._type = type

    @property
    def remainder(self):
        """Gets the remainder of this QuotaRemainderData.

        剩余配额

        :return: The remainder of this QuotaRemainderData.
        :rtype: int
        """
        return self._remainder

    @remainder.setter
    def remainder(self, remainder):
        """Sets the remainder of this QuotaRemainderData.

        剩余配额

        :param remainder: The remainder of this QuotaRemainderData.
        :type remainder: int
        """
        self._remainder = remainder

    @property
    def need(self):
        """Gets the need of this QuotaRemainderData.

        所需配额

        :return: The need of this QuotaRemainderData.
        :rtype: int
        """
        return self._need

    @need.setter
    def need(self, need):
        """Sets the need of this QuotaRemainderData.

        所需配额

        :param need: The need of this QuotaRemainderData.
        :type need: int
        """
        self._need = need

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
        if not isinstance(other, QuotaRemainderData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
