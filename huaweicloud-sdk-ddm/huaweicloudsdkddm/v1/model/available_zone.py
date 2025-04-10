# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AvailableZone:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'code': 'str',
        'description': 'str',
        'status': 'str',
        'support_ipv6': 'bool'
    }

    attribute_map = {
        'code': 'code',
        'description': 'description',
        'status': 'status',
        'support_ipv6': 'support_ipv6'
    }

    def __init__(self, code=None, description=None, status=None, support_ipv6=None):
        r"""AvailableZone

        The model defined in huaweicloud sdk

        :param code: 可用区CODE
        :type code: str
        :param description: 可用区描述
        :type description: str
        :param status: 可用区状态
        :type status: str
        :param support_ipv6: 是否支持IPV6
        :type support_ipv6: bool
        """
        
        

        self._code = None
        self._description = None
        self._status = None
        self._support_ipv6 = None
        self.discriminator = None

        self.code = code
        self.description = description
        self.status = status
        self.support_ipv6 = support_ipv6

    @property
    def code(self):
        r"""Gets the code of this AvailableZone.

        可用区CODE

        :return: The code of this AvailableZone.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this AvailableZone.

        可用区CODE

        :param code: The code of this AvailableZone.
        :type code: str
        """
        self._code = code

    @property
    def description(self):
        r"""Gets the description of this AvailableZone.

        可用区描述

        :return: The description of this AvailableZone.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this AvailableZone.

        可用区描述

        :param description: The description of this AvailableZone.
        :type description: str
        """
        self._description = description

    @property
    def status(self):
        r"""Gets the status of this AvailableZone.

        可用区状态

        :return: The status of this AvailableZone.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this AvailableZone.

        可用区状态

        :param status: The status of this AvailableZone.
        :type status: str
        """
        self._status = status

    @property
    def support_ipv6(self):
        r"""Gets the support_ipv6 of this AvailableZone.

        是否支持IPV6

        :return: The support_ipv6 of this AvailableZone.
        :rtype: bool
        """
        return self._support_ipv6

    @support_ipv6.setter
    def support_ipv6(self, support_ipv6):
        r"""Sets the support_ipv6 of this AvailableZone.

        是否支持IPV6

        :param support_ipv6: The support_ipv6 of this AvailableZone.
        :type support_ipv6: bool
        """
        self._support_ipv6 = support_ipv6

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
        if not isinstance(other, AvailableZone):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
