# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AllResources:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'used': 'int',
        'quota': 'int',
        'max': 'int',
        'min': 'int'
    }

    attribute_map = {
        'type': 'type',
        'used': 'used',
        'quota': 'quota',
        'max': 'max',
        'min': 'min'
    }

    def __init__(self, type=None, used=None, quota=None, max=None, min=None):
        r"""AllResources

        The model defined in huaweicloud sdk

        :param type: 查询配额的类型。scaling_Group：伸缩组配额。scaling_Config：伸缩配置配额。scaling_Policy：伸缩策略配额。scaling_Instance：伸缩实例配额。bandwidth_scaling_policy：伸缩带宽策略配额。
        :type type: str
        :param used: 已使用的配额数量。当type为scaling_Policy和scaling_Instance时，该字段为保留字段，返回-1。可通过查询弹性伸缩策略和伸缩实例配额查询指定弹性伸缩组下的弹性伸缩策略和伸缩实例已使用的配额数量。
        :type used: int
        :param quota: 配额总数量。
        :type quota: int
        :param max: 配额上限。
        :type max: int
        :param min: 配额下限。
        :type min: int
        """
        
        

        self._type = None
        self._used = None
        self._quota = None
        self._max = None
        self._min = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if used is not None:
            self.used = used
        if quota is not None:
            self.quota = quota
        if max is not None:
            self.max = max
        if min is not None:
            self.min = min

    @property
    def type(self):
        r"""Gets the type of this AllResources.

        查询配额的类型。scaling_Group：伸缩组配额。scaling_Config：伸缩配置配额。scaling_Policy：伸缩策略配额。scaling_Instance：伸缩实例配额。bandwidth_scaling_policy：伸缩带宽策略配额。

        :return: The type of this AllResources.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this AllResources.

        查询配额的类型。scaling_Group：伸缩组配额。scaling_Config：伸缩配置配额。scaling_Policy：伸缩策略配额。scaling_Instance：伸缩实例配额。bandwidth_scaling_policy：伸缩带宽策略配额。

        :param type: The type of this AllResources.
        :type type: str
        """
        self._type = type

    @property
    def used(self):
        r"""Gets the used of this AllResources.

        已使用的配额数量。当type为scaling_Policy和scaling_Instance时，该字段为保留字段，返回-1。可通过查询弹性伸缩策略和伸缩实例配额查询指定弹性伸缩组下的弹性伸缩策略和伸缩实例已使用的配额数量。

        :return: The used of this AllResources.
        :rtype: int
        """
        return self._used

    @used.setter
    def used(self, used):
        r"""Sets the used of this AllResources.

        已使用的配额数量。当type为scaling_Policy和scaling_Instance时，该字段为保留字段，返回-1。可通过查询弹性伸缩策略和伸缩实例配额查询指定弹性伸缩组下的弹性伸缩策略和伸缩实例已使用的配额数量。

        :param used: The used of this AllResources.
        :type used: int
        """
        self._used = used

    @property
    def quota(self):
        r"""Gets the quota of this AllResources.

        配额总数量。

        :return: The quota of this AllResources.
        :rtype: int
        """
        return self._quota

    @quota.setter
    def quota(self, quota):
        r"""Sets the quota of this AllResources.

        配额总数量。

        :param quota: The quota of this AllResources.
        :type quota: int
        """
        self._quota = quota

    @property
    def max(self):
        r"""Gets the max of this AllResources.

        配额上限。

        :return: The max of this AllResources.
        :rtype: int
        """
        return self._max

    @max.setter
    def max(self, max):
        r"""Sets the max of this AllResources.

        配额上限。

        :param max: The max of this AllResources.
        :type max: int
        """
        self._max = max

    @property
    def min(self):
        r"""Gets the min of this AllResources.

        配额下限。

        :return: The min of this AllResources.
        :rtype: int
        """
        return self._min

    @min.setter
    def min(self, min):
        r"""Sets the min of this AllResources.

        配额下限。

        :param min: The min of this AllResources.
        :type min: int
        """
        self._min = min

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
        if not isinstance(other, AllResources):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
