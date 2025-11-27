# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RollingUpdateNodeUpgradeStrategy:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'max_unavailable': 'object',
        'max_surge': 'object',
        'delete_policy': 'str'
    }

    attribute_map = {
        'max_unavailable': 'maxUnavailable',
        'max_surge': 'maxSurge',
        'delete_policy': 'deletePolicy'
    }

    def __init__(self, max_unavailable=None, max_surge=None, delete_policy=None):
        r"""RollingUpdateNodeUpgradeStrategy

        The model defined in huaweicloud sdk

        :param max_unavailable: 最大不可用个数
        :type max_unavailable: object
        :param max_surge: 允许超出期望的最大个数
        :type max_surge: object
        :param delete_policy: 删除策略：Random、Oldest、Newest
        :type delete_policy: str
        """
        
        

        self._max_unavailable = None
        self._max_surge = None
        self._delete_policy = None
        self.discriminator = None

        if max_unavailable is not None:
            self.max_unavailable = max_unavailable
        if max_surge is not None:
            self.max_surge = max_surge
        if delete_policy is not None:
            self.delete_policy = delete_policy

    @property
    def max_unavailable(self):
        r"""Gets the max_unavailable of this RollingUpdateNodeUpgradeStrategy.

        最大不可用个数

        :return: The max_unavailable of this RollingUpdateNodeUpgradeStrategy.
        :rtype: object
        """
        return self._max_unavailable

    @max_unavailable.setter
    def max_unavailable(self, max_unavailable):
        r"""Sets the max_unavailable of this RollingUpdateNodeUpgradeStrategy.

        最大不可用个数

        :param max_unavailable: The max_unavailable of this RollingUpdateNodeUpgradeStrategy.
        :type max_unavailable: object
        """
        self._max_unavailable = max_unavailable

    @property
    def max_surge(self):
        r"""Gets the max_surge of this RollingUpdateNodeUpgradeStrategy.

        允许超出期望的最大个数

        :return: The max_surge of this RollingUpdateNodeUpgradeStrategy.
        :rtype: object
        """
        return self._max_surge

    @max_surge.setter
    def max_surge(self, max_surge):
        r"""Sets the max_surge of this RollingUpdateNodeUpgradeStrategy.

        允许超出期望的最大个数

        :param max_surge: The max_surge of this RollingUpdateNodeUpgradeStrategy.
        :type max_surge: object
        """
        self._max_surge = max_surge

    @property
    def delete_policy(self):
        r"""Gets the delete_policy of this RollingUpdateNodeUpgradeStrategy.

        删除策略：Random、Oldest、Newest

        :return: The delete_policy of this RollingUpdateNodeUpgradeStrategy.
        :rtype: str
        """
        return self._delete_policy

    @delete_policy.setter
    def delete_policy(self, delete_policy):
        r"""Sets the delete_policy of this RollingUpdateNodeUpgradeStrategy.

        删除策略：Random、Oldest、Newest

        :param delete_policy: The delete_policy of this RollingUpdateNodeUpgradeStrategy.
        :type delete_policy: str
        """
        self._delete_policy = delete_policy

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RollingUpdateNodeUpgradeStrategy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
