# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PoolStatisticsStatisticsStatus:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'creating': 'int',
        'created': 'int',
        'failed': 'int',
        'pending': 'int'
    }

    attribute_map = {
        'creating': 'creating',
        'created': 'created',
        'failed': 'failed',
        'pending': 'pending'
    }

    def __init__(self, creating=None, created=None, failed=None, pending=None):
        r"""PoolStatisticsStatisticsStatus

        The model defined in huaweicloud sdk

        :param creating: **参数描述**： 正在创建中的资源池统计信息。 **取值范围**： 不涉及。
        :type creating: int
        :param created: **参数描述**： 创建成功的资源池数量。 **取值范围**： 不涉及。
        :type created: int
        :param failed: **参数描述**： 最近三天内创建失败的资源池数量，最大值为500。 **取值范围**： 不涉及。
        :type failed: int
        :param pending: **参数描述**： 等待中的资源池数量，通常是未支付的包周期资源池。 **取值范围**： 不涉及。
        :type pending: int
        """
        
        

        self._creating = None
        self._created = None
        self._failed = None
        self._pending = None
        self.discriminator = None

        if creating is not None:
            self.creating = creating
        if created is not None:
            self.created = created
        if failed is not None:
            self.failed = failed
        if pending is not None:
            self.pending = pending

    @property
    def creating(self):
        r"""Gets the creating of this PoolStatisticsStatisticsStatus.

        **参数描述**： 正在创建中的资源池统计信息。 **取值范围**： 不涉及。

        :return: The creating of this PoolStatisticsStatisticsStatus.
        :rtype: int
        """
        return self._creating

    @creating.setter
    def creating(self, creating):
        r"""Sets the creating of this PoolStatisticsStatisticsStatus.

        **参数描述**： 正在创建中的资源池统计信息。 **取值范围**： 不涉及。

        :param creating: The creating of this PoolStatisticsStatisticsStatus.
        :type creating: int
        """
        self._creating = creating

    @property
    def created(self):
        r"""Gets the created of this PoolStatisticsStatisticsStatus.

        **参数描述**： 创建成功的资源池数量。 **取值范围**： 不涉及。

        :return: The created of this PoolStatisticsStatisticsStatus.
        :rtype: int
        """
        return self._created

    @created.setter
    def created(self, created):
        r"""Sets the created of this PoolStatisticsStatisticsStatus.

        **参数描述**： 创建成功的资源池数量。 **取值范围**： 不涉及。

        :param created: The created of this PoolStatisticsStatisticsStatus.
        :type created: int
        """
        self._created = created

    @property
    def failed(self):
        r"""Gets the failed of this PoolStatisticsStatisticsStatus.

        **参数描述**： 最近三天内创建失败的资源池数量，最大值为500。 **取值范围**： 不涉及。

        :return: The failed of this PoolStatisticsStatisticsStatus.
        :rtype: int
        """
        return self._failed

    @failed.setter
    def failed(self, failed):
        r"""Sets the failed of this PoolStatisticsStatisticsStatus.

        **参数描述**： 最近三天内创建失败的资源池数量，最大值为500。 **取值范围**： 不涉及。

        :param failed: The failed of this PoolStatisticsStatisticsStatus.
        :type failed: int
        """
        self._failed = failed

    @property
    def pending(self):
        r"""Gets the pending of this PoolStatisticsStatisticsStatus.

        **参数描述**： 等待中的资源池数量，通常是未支付的包周期资源池。 **取值范围**： 不涉及。

        :return: The pending of this PoolStatisticsStatisticsStatus.
        :rtype: int
        """
        return self._pending

    @pending.setter
    def pending(self, pending):
        r"""Sets the pending of this PoolStatisticsStatisticsStatus.

        **参数描述**： 等待中的资源池数量，通常是未支付的包周期资源池。 **取值范围**： 不涉及。

        :param pending: The pending of this PoolStatisticsStatisticsStatus.
        :type pending: int
        """
        self._pending = pending

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
        if not isinstance(other, PoolStatisticsStatisticsStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
