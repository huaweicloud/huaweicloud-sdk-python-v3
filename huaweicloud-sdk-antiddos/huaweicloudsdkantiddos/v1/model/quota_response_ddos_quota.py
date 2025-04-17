# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QuotaResponseDdosQuota:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'current': 'int',
        'quota': 'int'
    }

    attribute_map = {
        'current': 'current',
        'quota': 'quota'
    }

    def __init__(self, current=None, quota=None):
        r"""QuotaResponseDdosQuota

        The model defined in huaweicloud sdk

        :param current: 当前用户已使用配额
        :type current: int
        :param quota: 最大配额
        :type quota: int
        """
        
        

        self._current = None
        self._quota = None
        self.discriminator = None

        if current is not None:
            self.current = current
        if quota is not None:
            self.quota = quota

    @property
    def current(self):
        r"""Gets the current of this QuotaResponseDdosQuota.

        当前用户已使用配额

        :return: The current of this QuotaResponseDdosQuota.
        :rtype: int
        """
        return self._current

    @current.setter
    def current(self, current):
        r"""Sets the current of this QuotaResponseDdosQuota.

        当前用户已使用配额

        :param current: The current of this QuotaResponseDdosQuota.
        :type current: int
        """
        self._current = current

    @property
    def quota(self):
        r"""Gets the quota of this QuotaResponseDdosQuota.

        最大配额

        :return: The quota of this QuotaResponseDdosQuota.
        :rtype: int
        """
        return self._quota

    @quota.setter
    def quota(self, quota):
        r"""Sets the quota of this QuotaResponseDdosQuota.

        最大配额

        :param quota: The quota of this QuotaResponseDdosQuota.
        :type quota: int
        """
        self._quota = quota

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
        if not isinstance(other, QuotaResponseDdosQuota):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
