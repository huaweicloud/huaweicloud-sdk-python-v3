# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AccessScope:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'namespaces': 'list[str]'
    }

    attribute_map = {
        'namespaces': 'namespaces'
    }

    def __init__(self, namespaces=None):
        r"""AccessScope

        The model defined in huaweicloud sdk

        :param namespaces: **参数解释：** 集群命名空间的列表，允许使用通配符（“\\*”），表示所有命名空间。当选择了不同集群时，命名空间的列表可以为多个集群的集合，在转化成RBAC策略时，会自动判断集群下的命名空间是否存在。 **约束限制：** 当前最多支持同时授权500个命名空间。 **取值范围：** \\[\&quot;\\*\&quot;\\]或者集群命名空间列表。 **默认取值：** 不涉及
        :type namespaces: list[str]
        """
        
        

        self._namespaces = None
        self.discriminator = None

        self.namespaces = namespaces

    @property
    def namespaces(self):
        r"""Gets the namespaces of this AccessScope.

        **参数解释：** 集群命名空间的列表，允许使用通配符（“\\*”），表示所有命名空间。当选择了不同集群时，命名空间的列表可以为多个集群的集合，在转化成RBAC策略时，会自动判断集群下的命名空间是否存在。 **约束限制：** 当前最多支持同时授权500个命名空间。 **取值范围：** \\[\"\\*\"\\]或者集群命名空间列表。 **默认取值：** 不涉及

        :return: The namespaces of this AccessScope.
        :rtype: list[str]
        """
        return self._namespaces

    @namespaces.setter
    def namespaces(self, namespaces):
        r"""Sets the namespaces of this AccessScope.

        **参数解释：** 集群命名空间的列表，允许使用通配符（“\\*”），表示所有命名空间。当选择了不同集群时，命名空间的列表可以为多个集群的集合，在转化成RBAC策略时，会自动判断集群下的命名空间是否存在。 **约束限制：** 当前最多支持同时授权500个命名空间。 **取值范围：** \\[\"\\*\"\\]或者集群命名空间列表。 **默认取值：** 不涉及

        :param namespaces: The namespaces of this AccessScope.
        :type namespaces: list[str]
        """
        self._namespaces = namespaces

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
        if not isinstance(other, AccessScope):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
