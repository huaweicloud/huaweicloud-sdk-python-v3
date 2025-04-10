# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CentralNetworkQuota:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'quota_key': 'CentralNetworkQuotaKeyEnum',
        'quota_limit': 'int',
        'used': 'int',
        'unit': 'str'
    }

    attribute_map = {
        'quota_key': 'quota_key',
        'quota_limit': 'quota_limit',
        'used': 'used',
        'unit': 'unit'
    }

    def __init__(self, quota_key=None, quota_limit=None, used=None, unit=None):
        r"""CentralNetworkQuota

        The model defined in huaweicloud sdk

        :param quota_key: 
        :type quota_key: :class:`huaweicloudsdkcc.v3.CentralNetworkQuotaKeyEnum`
        :param quota_limit: 配额大小。
        :type quota_limit: int
        :param used: 已使用配额。
        :type used: int
        :param unit: 配额值的单位。
        :type unit: str
        """
        
        

        self._quota_key = None
        self._quota_limit = None
        self._used = None
        self._unit = None
        self.discriminator = None

        self.quota_key = quota_key
        self.quota_limit = quota_limit
        self.used = used
        self.unit = unit

    @property
    def quota_key(self):
        r"""Gets the quota_key of this CentralNetworkQuota.

        :return: The quota_key of this CentralNetworkQuota.
        :rtype: :class:`huaweicloudsdkcc.v3.CentralNetworkQuotaKeyEnum`
        """
        return self._quota_key

    @quota_key.setter
    def quota_key(self, quota_key):
        r"""Sets the quota_key of this CentralNetworkQuota.

        :param quota_key: The quota_key of this CentralNetworkQuota.
        :type quota_key: :class:`huaweicloudsdkcc.v3.CentralNetworkQuotaKeyEnum`
        """
        self._quota_key = quota_key

    @property
    def quota_limit(self):
        r"""Gets the quota_limit of this CentralNetworkQuota.

        配额大小。

        :return: The quota_limit of this CentralNetworkQuota.
        :rtype: int
        """
        return self._quota_limit

    @quota_limit.setter
    def quota_limit(self, quota_limit):
        r"""Sets the quota_limit of this CentralNetworkQuota.

        配额大小。

        :param quota_limit: The quota_limit of this CentralNetworkQuota.
        :type quota_limit: int
        """
        self._quota_limit = quota_limit

    @property
    def used(self):
        r"""Gets the used of this CentralNetworkQuota.

        已使用配额。

        :return: The used of this CentralNetworkQuota.
        :rtype: int
        """
        return self._used

    @used.setter
    def used(self, used):
        r"""Sets the used of this CentralNetworkQuota.

        已使用配额。

        :param used: The used of this CentralNetworkQuota.
        :type used: int
        """
        self._used = used

    @property
    def unit(self):
        r"""Gets the unit of this CentralNetworkQuota.

        配额值的单位。

        :return: The unit of this CentralNetworkQuota.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        r"""Sets the unit of this CentralNetworkQuota.

        配额值的单位。

        :param unit: The unit of this CentralNetworkQuota.
        :type unit: str
        """
        self._unit = unit

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
        if not isinstance(other, CentralNetworkQuota):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
