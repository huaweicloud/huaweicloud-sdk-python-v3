# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CinderUpdateSnapshotOptionV5:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'description': 'str',
        'instant_access': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'instant_access': 'instant_access'
    }

    def __init__(self, name=None, description=None, instant_access=None):
        r"""CinderUpdateSnapshotOptionV5

        The model defined in huaweicloud sdk

        :param name: **参数解释** 云硬盘快照名称。最大支持64个字符。 **约束限制** 对云硬盘创建备份时，同时会创建以autobk_snapshot_为名称前缀的快照，云硬盘控制台对此类快照会有操作限制。因此建议不要创建以autobk_snapshot_为名称前缀的快照，避免影响快照的正常使用。 **取值范围** 不涉及。 **默认取值** 不涉及。
        :type name: str
        :param description: **参数解释** 云硬盘快照描述。 **约束限制** 不涉及。 **取值范围** 最大支持85个字符。 **默认取值** 不涉及。
        :type description: str
        :param instant_access: **参数解释** 云硬盘快照极速可用标识。 **约束限制** 不涉及。 **取值范围** - true：开启快照极速可用功能。 - false：关闭快照极速可用功能。 **默认取值** 不涉及。
        :type instant_access: bool
        """
        
        

        self._name = None
        self._description = None
        self._instant_access = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if instant_access is not None:
            self.instant_access = instant_access

    @property
    def name(self):
        r"""Gets the name of this CinderUpdateSnapshotOptionV5.

        **参数解释** 云硬盘快照名称。最大支持64个字符。 **约束限制** 对云硬盘创建备份时，同时会创建以autobk_snapshot_为名称前缀的快照，云硬盘控制台对此类快照会有操作限制。因此建议不要创建以autobk_snapshot_为名称前缀的快照，避免影响快照的正常使用。 **取值范围** 不涉及。 **默认取值** 不涉及。

        :return: The name of this CinderUpdateSnapshotOptionV5.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CinderUpdateSnapshotOptionV5.

        **参数解释** 云硬盘快照名称。最大支持64个字符。 **约束限制** 对云硬盘创建备份时，同时会创建以autobk_snapshot_为名称前缀的快照，云硬盘控制台对此类快照会有操作限制。因此建议不要创建以autobk_snapshot_为名称前缀的快照，避免影响快照的正常使用。 **取值范围** 不涉及。 **默认取值** 不涉及。

        :param name: The name of this CinderUpdateSnapshotOptionV5.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this CinderUpdateSnapshotOptionV5.

        **参数解释** 云硬盘快照描述。 **约束限制** 不涉及。 **取值范围** 最大支持85个字符。 **默认取值** 不涉及。

        :return: The description of this CinderUpdateSnapshotOptionV5.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CinderUpdateSnapshotOptionV5.

        **参数解释** 云硬盘快照描述。 **约束限制** 不涉及。 **取值范围** 最大支持85个字符。 **默认取值** 不涉及。

        :param description: The description of this CinderUpdateSnapshotOptionV5.
        :type description: str
        """
        self._description = description

    @property
    def instant_access(self):
        r"""Gets the instant_access of this CinderUpdateSnapshotOptionV5.

        **参数解释** 云硬盘快照极速可用标识。 **约束限制** 不涉及。 **取值范围** - true：开启快照极速可用功能。 - false：关闭快照极速可用功能。 **默认取值** 不涉及。

        :return: The instant_access of this CinderUpdateSnapshotOptionV5.
        :rtype: bool
        """
        return self._instant_access

    @instant_access.setter
    def instant_access(self, instant_access):
        r"""Sets the instant_access of this CinderUpdateSnapshotOptionV5.

        **参数解释** 云硬盘快照极速可用标识。 **约束限制** 不涉及。 **取值范围** - true：开启快照极速可用功能。 - false：关闭快照极速可用功能。 **默认取值** 不涉及。

        :param instant_access: The instant_access of this CinderUpdateSnapshotOptionV5.
        :type instant_access: bool
        """
        self._instant_access = instant_access

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
        if not isinstance(other, CinderUpdateSnapshotOptionV5):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
