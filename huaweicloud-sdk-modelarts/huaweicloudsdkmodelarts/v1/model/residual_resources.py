# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResidualResources:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'elb_listener_id': 'str',
        'elb_pool_id': 'str',
        'vpcep_id': 'str'
    }

    attribute_map = {
        'elb_listener_id': 'elb_listener_id',
        'elb_pool_id': 'elb_pool_id',
        'vpcep_id': 'vpcep_id'
    }

    def __init__(self, elb_listener_id=None, elb_pool_id=None, vpcep_id=None):
        r"""ResidualResources

        The model defined in huaweicloud sdk

        :param elb_listener_id: **参数解释：** 负载均衡器监听器ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type elb_listener_id: str
        :param elb_pool_id: **参数解释：** 后端服务器组ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type elb_pool_id: str
        :param vpcep_id: **参数解释：** 终端节点ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type vpcep_id: str
        """
        
        

        self._elb_listener_id = None
        self._elb_pool_id = None
        self._vpcep_id = None
        self.discriminator = None

        if elb_listener_id is not None:
            self.elb_listener_id = elb_listener_id
        if elb_pool_id is not None:
            self.elb_pool_id = elb_pool_id
        if vpcep_id is not None:
            self.vpcep_id = vpcep_id

    @property
    def elb_listener_id(self):
        r"""Gets the elb_listener_id of this ResidualResources.

        **参数解释：** 负载均衡器监听器ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The elb_listener_id of this ResidualResources.
        :rtype: str
        """
        return self._elb_listener_id

    @elb_listener_id.setter
    def elb_listener_id(self, elb_listener_id):
        r"""Sets the elb_listener_id of this ResidualResources.

        **参数解释：** 负载均衡器监听器ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param elb_listener_id: The elb_listener_id of this ResidualResources.
        :type elb_listener_id: str
        """
        self._elb_listener_id = elb_listener_id

    @property
    def elb_pool_id(self):
        r"""Gets the elb_pool_id of this ResidualResources.

        **参数解释：** 后端服务器组ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The elb_pool_id of this ResidualResources.
        :rtype: str
        """
        return self._elb_pool_id

    @elb_pool_id.setter
    def elb_pool_id(self, elb_pool_id):
        r"""Sets the elb_pool_id of this ResidualResources.

        **参数解释：** 后端服务器组ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param elb_pool_id: The elb_pool_id of this ResidualResources.
        :type elb_pool_id: str
        """
        self._elb_pool_id = elb_pool_id

    @property
    def vpcep_id(self):
        r"""Gets the vpcep_id of this ResidualResources.

        **参数解释：** 终端节点ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The vpcep_id of this ResidualResources.
        :rtype: str
        """
        return self._vpcep_id

    @vpcep_id.setter
    def vpcep_id(self, vpcep_id):
        r"""Sets the vpcep_id of this ResidualResources.

        **参数解释：** 终端节点ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param vpcep_id: The vpcep_id of this ResidualResources.
        :type vpcep_id: str
        """
        self._vpcep_id = vpcep_id

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
        if not isinstance(other, ResidualResources):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
