# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SwitchoverReplicaSetRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_id': 'str'
    }

    attribute_map = {
        'group_id': 'group_id'
    }

    def __init__(self, group_id=None):
        r"""SwitchoverReplicaSetRequestBody

        The model defined in huaweicloud sdk

        :param group_id: **参数解释** 组ID。 **约束限制** 不涉及。 **取值范围** - 对于集群实例，该参数为shard组ID或config组ID。可以调用“查询实例列表和详情”接口获取。 - 对于副本集实例，不传该参数。 **默认取值** 不涉及。
        :type group_id: str
        """
        
        

        self._group_id = None
        self.discriminator = None

        if group_id is not None:
            self.group_id = group_id

    @property
    def group_id(self):
        r"""Gets the group_id of this SwitchoverReplicaSetRequestBody.

        **参数解释** 组ID。 **约束限制** 不涉及。 **取值范围** - 对于集群实例，该参数为shard组ID或config组ID。可以调用“查询实例列表和详情”接口获取。 - 对于副本集实例，不传该参数。 **默认取值** 不涉及。

        :return: The group_id of this SwitchoverReplicaSetRequestBody.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this SwitchoverReplicaSetRequestBody.

        **参数解释** 组ID。 **约束限制** 不涉及。 **取值范围** - 对于集群实例，该参数为shard组ID或config组ID。可以调用“查询实例列表和详情”接口获取。 - 对于副本集实例，不传该参数。 **默认取值** 不涉及。

        :param group_id: The group_id of this SwitchoverReplicaSetRequestBody.
        :type group_id: str
        """
        self._group_id = group_id

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
        if not isinstance(other, SwitchoverReplicaSetRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
