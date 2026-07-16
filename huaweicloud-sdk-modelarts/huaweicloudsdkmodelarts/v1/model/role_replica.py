# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RoleReplica:

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
        'max_replicas': 'int',
        'min_replicas': 'int'
    }

    attribute_map = {
        'name': 'name',
        'max_replicas': 'max_replicas',
        'min_replicas': 'min_replicas'
    }

    def __init__(self, name=None, max_replicas=None, min_replicas=None):
        r"""RoleReplica

        The model defined in huaweicloud sdk

        :param name: **参数解释：** 角色名称。 **取值范围：** 不涉及。
        :type name: str
        :param max_replicas: **参数解释：** 最大副本数。 **取值范围：** 1~128。
        :type max_replicas: int
        :param min_replicas: **参数解释：** 最小副本数。 **取值范围：** 1~128。
        :type min_replicas: int
        """
        
        

        self._name = None
        self._max_replicas = None
        self._min_replicas = None
        self.discriminator = None

        self.name = name
        if max_replicas is not None:
            self.max_replicas = max_replicas
        if min_replicas is not None:
            self.min_replicas = min_replicas

    @property
    def name(self):
        r"""Gets the name of this RoleReplica.

        **参数解释：** 角色名称。 **取值范围：** 不涉及。

        :return: The name of this RoleReplica.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this RoleReplica.

        **参数解释：** 角色名称。 **取值范围：** 不涉及。

        :param name: The name of this RoleReplica.
        :type name: str
        """
        self._name = name

    @property
    def max_replicas(self):
        r"""Gets the max_replicas of this RoleReplica.

        **参数解释：** 最大副本数。 **取值范围：** 1~128。

        :return: The max_replicas of this RoleReplica.
        :rtype: int
        """
        return self._max_replicas

    @max_replicas.setter
    def max_replicas(self, max_replicas):
        r"""Sets the max_replicas of this RoleReplica.

        **参数解释：** 最大副本数。 **取值范围：** 1~128。

        :param max_replicas: The max_replicas of this RoleReplica.
        :type max_replicas: int
        """
        self._max_replicas = max_replicas

    @property
    def min_replicas(self):
        r"""Gets the min_replicas of this RoleReplica.

        **参数解释：** 最小副本数。 **取值范围：** 1~128。

        :return: The min_replicas of this RoleReplica.
        :rtype: int
        """
        return self._min_replicas

    @min_replicas.setter
    def min_replicas(self, min_replicas):
        r"""Sets the min_replicas of this RoleReplica.

        **参数解释：** 最小副本数。 **取值范围：** 1~128。

        :param min_replicas: The min_replicas of this RoleReplica.
        :type min_replicas: int
        """
        self._min_replicas = min_replicas

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
        if not isinstance(other, RoleReplica):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
