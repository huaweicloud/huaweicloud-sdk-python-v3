# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SubscriptionOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'independent_agent': 'bool',
        'snapshot_always_available': 'bool',
        'replicate_ddl': 'bool',
        'allow_initialize_from_backup': 'bool'
    }

    attribute_map = {
        'independent_agent': 'independent_agent',
        'snapshot_always_available': 'snapshot_always_available',
        'replicate_ddl': 'replicate_ddl',
        'allow_initialize_from_backup': 'allow_initialize_from_backup'
    }

    def __init__(self, independent_agent=None, snapshot_always_available=None, replicate_ddl=None, allow_initialize_from_backup=None):
        r"""SubscriptionOption

        The model defined in huaweicloud sdk

        :param independent_agent: 独立的分发代理。  true：使用。 false：不使用。
        :type independent_agent: bool
        :param snapshot_always_available: 快照始终可用。需要“独立的分发代理”。  true：可用。 false：不可用。
        :type snapshot_always_available: bool
        :param replicate_ddl: 复制架构更改。  true：可更改。 false：不可更改。
        :type replicate_ddl: bool
        :param allow_initialize_from_backup: 允许使用备份文件初始化。  true：允许。 false：不允许。
        :type allow_initialize_from_backup: bool
        """
        
        

        self._independent_agent = None
        self._snapshot_always_available = None
        self._replicate_ddl = None
        self._allow_initialize_from_backup = None
        self.discriminator = None

        if independent_agent is not None:
            self.independent_agent = independent_agent
        if snapshot_always_available is not None:
            self.snapshot_always_available = snapshot_always_available
        if replicate_ddl is not None:
            self.replicate_ddl = replicate_ddl
        if allow_initialize_from_backup is not None:
            self.allow_initialize_from_backup = allow_initialize_from_backup

    @property
    def independent_agent(self):
        r"""Gets the independent_agent of this SubscriptionOption.

        独立的分发代理。  true：使用。 false：不使用。

        :return: The independent_agent of this SubscriptionOption.
        :rtype: bool
        """
        return self._independent_agent

    @independent_agent.setter
    def independent_agent(self, independent_agent):
        r"""Sets the independent_agent of this SubscriptionOption.

        独立的分发代理。  true：使用。 false：不使用。

        :param independent_agent: The independent_agent of this SubscriptionOption.
        :type independent_agent: bool
        """
        self._independent_agent = independent_agent

    @property
    def snapshot_always_available(self):
        r"""Gets the snapshot_always_available of this SubscriptionOption.

        快照始终可用。需要“独立的分发代理”。  true：可用。 false：不可用。

        :return: The snapshot_always_available of this SubscriptionOption.
        :rtype: bool
        """
        return self._snapshot_always_available

    @snapshot_always_available.setter
    def snapshot_always_available(self, snapshot_always_available):
        r"""Sets the snapshot_always_available of this SubscriptionOption.

        快照始终可用。需要“独立的分发代理”。  true：可用。 false：不可用。

        :param snapshot_always_available: The snapshot_always_available of this SubscriptionOption.
        :type snapshot_always_available: bool
        """
        self._snapshot_always_available = snapshot_always_available

    @property
    def replicate_ddl(self):
        r"""Gets the replicate_ddl of this SubscriptionOption.

        复制架构更改。  true：可更改。 false：不可更改。

        :return: The replicate_ddl of this SubscriptionOption.
        :rtype: bool
        """
        return self._replicate_ddl

    @replicate_ddl.setter
    def replicate_ddl(self, replicate_ddl):
        r"""Sets the replicate_ddl of this SubscriptionOption.

        复制架构更改。  true：可更改。 false：不可更改。

        :param replicate_ddl: The replicate_ddl of this SubscriptionOption.
        :type replicate_ddl: bool
        """
        self._replicate_ddl = replicate_ddl

    @property
    def allow_initialize_from_backup(self):
        r"""Gets the allow_initialize_from_backup of this SubscriptionOption.

        允许使用备份文件初始化。  true：允许。 false：不允许。

        :return: The allow_initialize_from_backup of this SubscriptionOption.
        :rtype: bool
        """
        return self._allow_initialize_from_backup

    @allow_initialize_from_backup.setter
    def allow_initialize_from_backup(self, allow_initialize_from_backup):
        r"""Sets the allow_initialize_from_backup of this SubscriptionOption.

        允许使用备份文件初始化。  true：允许。 false：不允许。

        :param allow_initialize_from_backup: The allow_initialize_from_backup of this SubscriptionOption.
        :type allow_initialize_from_backup: bool
        """
        self._allow_initialize_from_backup = allow_initialize_from_backup

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
        if not isinstance(other, SubscriptionOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
