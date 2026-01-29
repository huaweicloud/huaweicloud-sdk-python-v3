# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowGroupResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enabled': 'bool',
        'broadcast': 'bool',
        'brokers': 'list[str]',
        'name': 'str',
        'group_desc': 'str',
        'created_at': 'int',
        'retry_max_time': 'int',
        'permissions': 'list[str]',
        'consume_orderly': 'bool',
        'group_online': 'bool'
    }

    attribute_map = {
        'enabled': 'enabled',
        'broadcast': 'broadcast',
        'brokers': 'brokers',
        'name': 'name',
        'group_desc': 'group_desc',
        'created_at': 'created_at',
        'retry_max_time': 'retry_max_time',
        'permissions': 'permissions',
        'consume_orderly': 'consume_orderly',
        'group_online': 'group_online'
    }

    def __init__(self, enabled=None, broadcast=None, brokers=None, name=None, group_desc=None, created_at=None, retry_max_time=None, permissions=None, consume_orderly=None, group_online=None):
        r"""ShowGroupResponse

        The model defined in huaweicloud sdk

        :param enabled: **参数解释**： 是否可以消费。 **约束限制**： 不涉及。 **取值范围**： - true：可以消费。 - false：不可以消费。 **默认取值**： 不涉及。
        :type enabled: bool
        :param broadcast: **参数解释**： 是否广播。 **约束限制**： 不涉及。 **取值范围**： - true：开启广播消费。 - false：不开启广播消费。 **默认取值**： 不涉及。
        :type broadcast: bool
        :param brokers: **参数解释**： 关联的代理列表。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type brokers: list[str]
        :param name: **参数解释**： 消费组名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type name: str
        :param group_desc: **参数解释**： 消费组描述。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type group_desc: str
        :param created_at: **参数解释**： 创建时间。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type created_at: int
        :param retry_max_time: **参数解释**： 最大重试次数。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type retry_max_time: int
        :param permissions: **参数解释**： 权限。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type permissions: list[str]
        :param consume_orderly: **参数解释**： 是否顺序消费。 **约束限制**： 不涉及。 **取值范围**： - true：开启顺序消费。 - false：不开启顺序消费。 **默认取值**： 不涉及。
        :type consume_orderly: bool
        :param group_online: **参数解释**： 消费组是否在线。 **约束限制**： 不涉及。 **取值范围**： - true：消费组在线。 - false：消费组不在线。 **默认取值**： 不涉及。
        :type group_online: bool
        """
        
        super().__init__()

        self._enabled = None
        self._broadcast = None
        self._brokers = None
        self._name = None
        self._group_desc = None
        self._created_at = None
        self._retry_max_time = None
        self._permissions = None
        self._consume_orderly = None
        self._group_online = None
        self.discriminator = None

        if enabled is not None:
            self.enabled = enabled
        if broadcast is not None:
            self.broadcast = broadcast
        if brokers is not None:
            self.brokers = brokers
        if name is not None:
            self.name = name
        if group_desc is not None:
            self.group_desc = group_desc
        if created_at is not None:
            self.created_at = created_at
        if retry_max_time is not None:
            self.retry_max_time = retry_max_time
        if permissions is not None:
            self.permissions = permissions
        if consume_orderly is not None:
            self.consume_orderly = consume_orderly
        if group_online is not None:
            self.group_online = group_online

    @property
    def enabled(self):
        r"""Gets the enabled of this ShowGroupResponse.

        **参数解释**： 是否可以消费。 **约束限制**： 不涉及。 **取值范围**： - true：可以消费。 - false：不可以消费。 **默认取值**： 不涉及。

        :return: The enabled of this ShowGroupResponse.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this ShowGroupResponse.

        **参数解释**： 是否可以消费。 **约束限制**： 不涉及。 **取值范围**： - true：可以消费。 - false：不可以消费。 **默认取值**： 不涉及。

        :param enabled: The enabled of this ShowGroupResponse.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def broadcast(self):
        r"""Gets the broadcast of this ShowGroupResponse.

        **参数解释**： 是否广播。 **约束限制**： 不涉及。 **取值范围**： - true：开启广播消费。 - false：不开启广播消费。 **默认取值**： 不涉及。

        :return: The broadcast of this ShowGroupResponse.
        :rtype: bool
        """
        return self._broadcast

    @broadcast.setter
    def broadcast(self, broadcast):
        r"""Sets the broadcast of this ShowGroupResponse.

        **参数解释**： 是否广播。 **约束限制**： 不涉及。 **取值范围**： - true：开启广播消费。 - false：不开启广播消费。 **默认取值**： 不涉及。

        :param broadcast: The broadcast of this ShowGroupResponse.
        :type broadcast: bool
        """
        self._broadcast = broadcast

    @property
    def brokers(self):
        r"""Gets the brokers of this ShowGroupResponse.

        **参数解释**： 关联的代理列表。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The brokers of this ShowGroupResponse.
        :rtype: list[str]
        """
        return self._brokers

    @brokers.setter
    def brokers(self, brokers):
        r"""Sets the brokers of this ShowGroupResponse.

        **参数解释**： 关联的代理列表。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param brokers: The brokers of this ShowGroupResponse.
        :type brokers: list[str]
        """
        self._brokers = brokers

    @property
    def name(self):
        r"""Gets the name of this ShowGroupResponse.

        **参数解释**： 消费组名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The name of this ShowGroupResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowGroupResponse.

        **参数解释**： 消费组名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param name: The name of this ShowGroupResponse.
        :type name: str
        """
        self._name = name

    @property
    def group_desc(self):
        r"""Gets the group_desc of this ShowGroupResponse.

        **参数解释**： 消费组描述。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The group_desc of this ShowGroupResponse.
        :rtype: str
        """
        return self._group_desc

    @group_desc.setter
    def group_desc(self, group_desc):
        r"""Sets the group_desc of this ShowGroupResponse.

        **参数解释**： 消费组描述。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param group_desc: The group_desc of this ShowGroupResponse.
        :type group_desc: str
        """
        self._group_desc = group_desc

    @property
    def created_at(self):
        r"""Gets the created_at of this ShowGroupResponse.

        **参数解释**： 创建时间。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The created_at of this ShowGroupResponse.
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this ShowGroupResponse.

        **参数解释**： 创建时间。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param created_at: The created_at of this ShowGroupResponse.
        :type created_at: int
        """
        self._created_at = created_at

    @property
    def retry_max_time(self):
        r"""Gets the retry_max_time of this ShowGroupResponse.

        **参数解释**： 最大重试次数。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The retry_max_time of this ShowGroupResponse.
        :rtype: int
        """
        return self._retry_max_time

    @retry_max_time.setter
    def retry_max_time(self, retry_max_time):
        r"""Sets the retry_max_time of this ShowGroupResponse.

        **参数解释**： 最大重试次数。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param retry_max_time: The retry_max_time of this ShowGroupResponse.
        :type retry_max_time: int
        """
        self._retry_max_time = retry_max_time

    @property
    def permissions(self):
        r"""Gets the permissions of this ShowGroupResponse.

        **参数解释**： 权限。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The permissions of this ShowGroupResponse.
        :rtype: list[str]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        r"""Sets the permissions of this ShowGroupResponse.

        **参数解释**： 权限。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param permissions: The permissions of this ShowGroupResponse.
        :type permissions: list[str]
        """
        self._permissions = permissions

    @property
    def consume_orderly(self):
        r"""Gets the consume_orderly of this ShowGroupResponse.

        **参数解释**： 是否顺序消费。 **约束限制**： 不涉及。 **取值范围**： - true：开启顺序消费。 - false：不开启顺序消费。 **默认取值**： 不涉及。

        :return: The consume_orderly of this ShowGroupResponse.
        :rtype: bool
        """
        return self._consume_orderly

    @consume_orderly.setter
    def consume_orderly(self, consume_orderly):
        r"""Sets the consume_orderly of this ShowGroupResponse.

        **参数解释**： 是否顺序消费。 **约束限制**： 不涉及。 **取值范围**： - true：开启顺序消费。 - false：不开启顺序消费。 **默认取值**： 不涉及。

        :param consume_orderly: The consume_orderly of this ShowGroupResponse.
        :type consume_orderly: bool
        """
        self._consume_orderly = consume_orderly

    @property
    def group_online(self):
        r"""Gets the group_online of this ShowGroupResponse.

        **参数解释**： 消费组是否在线。 **约束限制**： 不涉及。 **取值范围**： - true：消费组在线。 - false：消费组不在线。 **默认取值**： 不涉及。

        :return: The group_online of this ShowGroupResponse.
        :rtype: bool
        """
        return self._group_online

    @group_online.setter
    def group_online(self, group_online):
        r"""Sets the group_online of this ShowGroupResponse.

        **参数解释**： 消费组是否在线。 **约束限制**： 不涉及。 **取值范围**： - true：消费组在线。 - false：消费组不在线。 **默认取值**： 不涉及。

        :param group_online: The group_online of this ShowGroupResponse.
        :type group_online: bool
        """
        self._group_online = group_online

    def to_dict(self):
        import warnings
        warnings.warn("ShowGroupResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ShowGroupResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
