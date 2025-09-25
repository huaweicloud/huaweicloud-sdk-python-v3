# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EpsRemainingQuotaResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'eps_tag': 'str',
        'instance_eps_quota': 'int',
        'cpu_eps_quota': 'int',
        'mem_eps_quota': 'int',
        'volume_eps_quota': 'int',
        'instance_eps_remaining_quota': 'int',
        'cpu_eps_remaining_quota': 'int',
        'mem_eps_remaining_quota': 'int',
        'volume_eps_remaining_quota': 'int'
    }

    attribute_map = {
        'eps_tag': 'eps_tag',
        'instance_eps_quota': 'instance_eps_quota',
        'cpu_eps_quota': 'cpu_eps_quota',
        'mem_eps_quota': 'mem_eps_quota',
        'volume_eps_quota': 'volume_eps_quota',
        'instance_eps_remaining_quota': 'instance_eps_remaining_quota',
        'cpu_eps_remaining_quota': 'cpu_eps_remaining_quota',
        'mem_eps_remaining_quota': 'mem_eps_remaining_quota',
        'volume_eps_remaining_quota': 'volume_eps_remaining_quota'
    }

    def __init__(self, eps_tag=None, instance_eps_quota=None, cpu_eps_quota=None, mem_eps_quota=None, volume_eps_quota=None, instance_eps_remaining_quota=None, cpu_eps_remaining_quota=None, mem_eps_remaining_quota=None, volume_eps_remaining_quota=None):
        r"""EpsRemainingQuotaResult

        The model defined in huaweicloud sdk

        :param eps_tag: **参数解释**: 企业项目ID。 **取值范围**: 不涉及。
        :type eps_tag: str
        :param instance_eps_quota: **参数解释**: 实例配额。 **取值范围**: 不涉及。
        :type instance_eps_quota: int
        :param cpu_eps_quota: **参数解释**: CPU配额。 **取值范围**: 不涉及。
        :type cpu_eps_quota: int
        :param mem_eps_quota: **参数解释**: 内存配额。 **取值范围**: 不涉及。
        :type mem_eps_quota: int
        :param volume_eps_quota: **参数解释**: 存储空间配额。 **取值范围**: 不涉及。
        :type volume_eps_quota: int
        :param instance_eps_remaining_quota: **参数解释**: 实例剩余配额。 **取值范围**: 不涉及。
        :type instance_eps_remaining_quota: int
        :param cpu_eps_remaining_quota: **参数解释**: CPU剩余配额。 **取值范围**: 不涉及。
        :type cpu_eps_remaining_quota: int
        :param mem_eps_remaining_quota: **参数解释**: 内存剩余配额。 **取值范围**: 不涉及。
        :type mem_eps_remaining_quota: int
        :param volume_eps_remaining_quota: **参数解释**: 存储空间剩余配额。 **取值范围**: 不涉及。
        :type volume_eps_remaining_quota: int
        """
        
        

        self._eps_tag = None
        self._instance_eps_quota = None
        self._cpu_eps_quota = None
        self._mem_eps_quota = None
        self._volume_eps_quota = None
        self._instance_eps_remaining_quota = None
        self._cpu_eps_remaining_quota = None
        self._mem_eps_remaining_quota = None
        self._volume_eps_remaining_quota = None
        self.discriminator = None

        if eps_tag is not None:
            self.eps_tag = eps_tag
        if instance_eps_quota is not None:
            self.instance_eps_quota = instance_eps_quota
        if cpu_eps_quota is not None:
            self.cpu_eps_quota = cpu_eps_quota
        if mem_eps_quota is not None:
            self.mem_eps_quota = mem_eps_quota
        if volume_eps_quota is not None:
            self.volume_eps_quota = volume_eps_quota
        if instance_eps_remaining_quota is not None:
            self.instance_eps_remaining_quota = instance_eps_remaining_quota
        if cpu_eps_remaining_quota is not None:
            self.cpu_eps_remaining_quota = cpu_eps_remaining_quota
        if mem_eps_remaining_quota is not None:
            self.mem_eps_remaining_quota = mem_eps_remaining_quota
        if volume_eps_remaining_quota is not None:
            self.volume_eps_remaining_quota = volume_eps_remaining_quota

    @property
    def eps_tag(self):
        r"""Gets the eps_tag of this EpsRemainingQuotaResult.

        **参数解释**: 企业项目ID。 **取值范围**: 不涉及。

        :return: The eps_tag of this EpsRemainingQuotaResult.
        :rtype: str
        """
        return self._eps_tag

    @eps_tag.setter
    def eps_tag(self, eps_tag):
        r"""Sets the eps_tag of this EpsRemainingQuotaResult.

        **参数解释**: 企业项目ID。 **取值范围**: 不涉及。

        :param eps_tag: The eps_tag of this EpsRemainingQuotaResult.
        :type eps_tag: str
        """
        self._eps_tag = eps_tag

    @property
    def instance_eps_quota(self):
        r"""Gets the instance_eps_quota of this EpsRemainingQuotaResult.

        **参数解释**: 实例配额。 **取值范围**: 不涉及。

        :return: The instance_eps_quota of this EpsRemainingQuotaResult.
        :rtype: int
        """
        return self._instance_eps_quota

    @instance_eps_quota.setter
    def instance_eps_quota(self, instance_eps_quota):
        r"""Sets the instance_eps_quota of this EpsRemainingQuotaResult.

        **参数解释**: 实例配额。 **取值范围**: 不涉及。

        :param instance_eps_quota: The instance_eps_quota of this EpsRemainingQuotaResult.
        :type instance_eps_quota: int
        """
        self._instance_eps_quota = instance_eps_quota

    @property
    def cpu_eps_quota(self):
        r"""Gets the cpu_eps_quota of this EpsRemainingQuotaResult.

        **参数解释**: CPU配额。 **取值范围**: 不涉及。

        :return: The cpu_eps_quota of this EpsRemainingQuotaResult.
        :rtype: int
        """
        return self._cpu_eps_quota

    @cpu_eps_quota.setter
    def cpu_eps_quota(self, cpu_eps_quota):
        r"""Sets the cpu_eps_quota of this EpsRemainingQuotaResult.

        **参数解释**: CPU配额。 **取值范围**: 不涉及。

        :param cpu_eps_quota: The cpu_eps_quota of this EpsRemainingQuotaResult.
        :type cpu_eps_quota: int
        """
        self._cpu_eps_quota = cpu_eps_quota

    @property
    def mem_eps_quota(self):
        r"""Gets the mem_eps_quota of this EpsRemainingQuotaResult.

        **参数解释**: 内存配额。 **取值范围**: 不涉及。

        :return: The mem_eps_quota of this EpsRemainingQuotaResult.
        :rtype: int
        """
        return self._mem_eps_quota

    @mem_eps_quota.setter
    def mem_eps_quota(self, mem_eps_quota):
        r"""Sets the mem_eps_quota of this EpsRemainingQuotaResult.

        **参数解释**: 内存配额。 **取值范围**: 不涉及。

        :param mem_eps_quota: The mem_eps_quota of this EpsRemainingQuotaResult.
        :type mem_eps_quota: int
        """
        self._mem_eps_quota = mem_eps_quota

    @property
    def volume_eps_quota(self):
        r"""Gets the volume_eps_quota of this EpsRemainingQuotaResult.

        **参数解释**: 存储空间配额。 **取值范围**: 不涉及。

        :return: The volume_eps_quota of this EpsRemainingQuotaResult.
        :rtype: int
        """
        return self._volume_eps_quota

    @volume_eps_quota.setter
    def volume_eps_quota(self, volume_eps_quota):
        r"""Sets the volume_eps_quota of this EpsRemainingQuotaResult.

        **参数解释**: 存储空间配额。 **取值范围**: 不涉及。

        :param volume_eps_quota: The volume_eps_quota of this EpsRemainingQuotaResult.
        :type volume_eps_quota: int
        """
        self._volume_eps_quota = volume_eps_quota

    @property
    def instance_eps_remaining_quota(self):
        r"""Gets the instance_eps_remaining_quota of this EpsRemainingQuotaResult.

        **参数解释**: 实例剩余配额。 **取值范围**: 不涉及。

        :return: The instance_eps_remaining_quota of this EpsRemainingQuotaResult.
        :rtype: int
        """
        return self._instance_eps_remaining_quota

    @instance_eps_remaining_quota.setter
    def instance_eps_remaining_quota(self, instance_eps_remaining_quota):
        r"""Sets the instance_eps_remaining_quota of this EpsRemainingQuotaResult.

        **参数解释**: 实例剩余配额。 **取值范围**: 不涉及。

        :param instance_eps_remaining_quota: The instance_eps_remaining_quota of this EpsRemainingQuotaResult.
        :type instance_eps_remaining_quota: int
        """
        self._instance_eps_remaining_quota = instance_eps_remaining_quota

    @property
    def cpu_eps_remaining_quota(self):
        r"""Gets the cpu_eps_remaining_quota of this EpsRemainingQuotaResult.

        **参数解释**: CPU剩余配额。 **取值范围**: 不涉及。

        :return: The cpu_eps_remaining_quota of this EpsRemainingQuotaResult.
        :rtype: int
        """
        return self._cpu_eps_remaining_quota

    @cpu_eps_remaining_quota.setter
    def cpu_eps_remaining_quota(self, cpu_eps_remaining_quota):
        r"""Sets the cpu_eps_remaining_quota of this EpsRemainingQuotaResult.

        **参数解释**: CPU剩余配额。 **取值范围**: 不涉及。

        :param cpu_eps_remaining_quota: The cpu_eps_remaining_quota of this EpsRemainingQuotaResult.
        :type cpu_eps_remaining_quota: int
        """
        self._cpu_eps_remaining_quota = cpu_eps_remaining_quota

    @property
    def mem_eps_remaining_quota(self):
        r"""Gets the mem_eps_remaining_quota of this EpsRemainingQuotaResult.

        **参数解释**: 内存剩余配额。 **取值范围**: 不涉及。

        :return: The mem_eps_remaining_quota of this EpsRemainingQuotaResult.
        :rtype: int
        """
        return self._mem_eps_remaining_quota

    @mem_eps_remaining_quota.setter
    def mem_eps_remaining_quota(self, mem_eps_remaining_quota):
        r"""Sets the mem_eps_remaining_quota of this EpsRemainingQuotaResult.

        **参数解释**: 内存剩余配额。 **取值范围**: 不涉及。

        :param mem_eps_remaining_quota: The mem_eps_remaining_quota of this EpsRemainingQuotaResult.
        :type mem_eps_remaining_quota: int
        """
        self._mem_eps_remaining_quota = mem_eps_remaining_quota

    @property
    def volume_eps_remaining_quota(self):
        r"""Gets the volume_eps_remaining_quota of this EpsRemainingQuotaResult.

        **参数解释**: 存储空间剩余配额。 **取值范围**: 不涉及。

        :return: The volume_eps_remaining_quota of this EpsRemainingQuotaResult.
        :rtype: int
        """
        return self._volume_eps_remaining_quota

    @volume_eps_remaining_quota.setter
    def volume_eps_remaining_quota(self, volume_eps_remaining_quota):
        r"""Sets the volume_eps_remaining_quota of this EpsRemainingQuotaResult.

        **参数解释**: 存储空间剩余配额。 **取值范围**: 不涉及。

        :param volume_eps_remaining_quota: The volume_eps_remaining_quota of this EpsRemainingQuotaResult.
        :type volume_eps_remaining_quota: int
        """
        self._volume_eps_remaining_quota = volume_eps_remaining_quota

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
        if not isinstance(other, EpsRemainingQuotaResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
