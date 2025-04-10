# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BwListIps:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ip': 'str',
        'desc': 'str'
    }

    attribute_map = {
        'ip': 'ip',
        'desc': 'desc'
    }

    def __init__(self, ip=None, desc=None):
        r"""BwListIps

        The model defined in huaweicloud sdk

        :param ip: 黑白名单ip
        :type ip: str
        :param desc: 描述
        :type desc: str
        """
        
        

        self._ip = None
        self._desc = None
        self.discriminator = None

        if ip is not None:
            self.ip = ip
        if desc is not None:
            self.desc = desc

    @property
    def ip(self):
        r"""Gets the ip of this BwListIps.

        黑白名单ip

        :return: The ip of this BwListIps.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        r"""Sets the ip of this BwListIps.

        黑白名单ip

        :param ip: The ip of this BwListIps.
        :type ip: str
        """
        self._ip = ip

    @property
    def desc(self):
        r"""Gets the desc of this BwListIps.

        描述

        :return: The desc of this BwListIps.
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        r"""Sets the desc of this BwListIps.

        描述

        :param desc: The desc of this BwListIps.
        :type desc: str
        """
        self._desc = desc

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
        if not isinstance(other, BwListIps):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
