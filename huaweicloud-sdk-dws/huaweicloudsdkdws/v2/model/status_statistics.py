# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StatusStatistics:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'active': 'int',
        'total': 'int'
    }

    attribute_map = {
        'active': 'active',
        'total': 'total'
    }

    def __init__(self, active=None, total=None):
        r"""StatusStatistics

        The model defined in huaweicloud sdk

        :param active: **参数解释**： 活跃资源。 **取值范围**： 不涉及。
        :type active: int
        :param total: **参数解释**： 总资源。 **取值范围**： 不涉及。
        :type total: int
        """
        
        

        self._active = None
        self._total = None
        self.discriminator = None

        if active is not None:
            self.active = active
        if total is not None:
            self.total = total

    @property
    def active(self):
        r"""Gets the active of this StatusStatistics.

        **参数解释**： 活跃资源。 **取值范围**： 不涉及。

        :return: The active of this StatusStatistics.
        :rtype: int
        """
        return self._active

    @active.setter
    def active(self, active):
        r"""Sets the active of this StatusStatistics.

        **参数解释**： 活跃资源。 **取值范围**： 不涉及。

        :param active: The active of this StatusStatistics.
        :type active: int
        """
        self._active = active

    @property
    def total(self):
        r"""Gets the total of this StatusStatistics.

        **参数解释**： 总资源。 **取值范围**： 不涉及。

        :return: The total of this StatusStatistics.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this StatusStatistics.

        **参数解释**： 总资源。 **取值范围**： 不涉及。

        :param total: The total of this StatusStatistics.
        :type total: int
        """
        self._total = total

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
        if not isinstance(other, StatusStatistics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
