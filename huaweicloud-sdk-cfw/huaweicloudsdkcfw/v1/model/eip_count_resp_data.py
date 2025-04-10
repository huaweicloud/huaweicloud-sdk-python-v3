# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EipCountRespData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'eip_total': 'int',
        'eip_protected': 'int',
        'eip_protected_self': 'int'
    }

    attribute_map = {
        'eip_total': 'eip_total',
        'eip_protected': 'eip_protected',
        'eip_protected_self': 'eip_protected_self'
    }

    def __init__(self, eip_total=None, eip_protected=None, eip_protected_self=None):
        r"""EipCountRespData

        The model defined in huaweicloud sdk

        :param eip_total: 总体EIP数
        :type eip_total: int
        :param eip_protected: 该账号下所有墙防护EIP总数量
        :type eip_protected: int
        :param eip_protected_self: 当前防火墙防护EIP数量
        :type eip_protected_self: int
        """
        
        

        self._eip_total = None
        self._eip_protected = None
        self._eip_protected_self = None
        self.discriminator = None

        if eip_total is not None:
            self.eip_total = eip_total
        if eip_protected is not None:
            self.eip_protected = eip_protected
        if eip_protected_self is not None:
            self.eip_protected_self = eip_protected_self

    @property
    def eip_total(self):
        r"""Gets the eip_total of this EipCountRespData.

        总体EIP数

        :return: The eip_total of this EipCountRespData.
        :rtype: int
        """
        return self._eip_total

    @eip_total.setter
    def eip_total(self, eip_total):
        r"""Sets the eip_total of this EipCountRespData.

        总体EIP数

        :param eip_total: The eip_total of this EipCountRespData.
        :type eip_total: int
        """
        self._eip_total = eip_total

    @property
    def eip_protected(self):
        r"""Gets the eip_protected of this EipCountRespData.

        该账号下所有墙防护EIP总数量

        :return: The eip_protected of this EipCountRespData.
        :rtype: int
        """
        return self._eip_protected

    @eip_protected.setter
    def eip_protected(self, eip_protected):
        r"""Sets the eip_protected of this EipCountRespData.

        该账号下所有墙防护EIP总数量

        :param eip_protected: The eip_protected of this EipCountRespData.
        :type eip_protected: int
        """
        self._eip_protected = eip_protected

    @property
    def eip_protected_self(self):
        r"""Gets the eip_protected_self of this EipCountRespData.

        当前防火墙防护EIP数量

        :return: The eip_protected_self of this EipCountRespData.
        :rtype: int
        """
        return self._eip_protected_self

    @eip_protected_self.setter
    def eip_protected_self(self, eip_protected_self):
        r"""Sets the eip_protected_self of this EipCountRespData.

        当前防火墙防护EIP数量

        :param eip_protected_self: The eip_protected_self of this EipCountRespData.
        :type eip_protected_self: int
        """
        self._eip_protected_self = eip_protected_self

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
        if not isinstance(other, EipCountRespData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
