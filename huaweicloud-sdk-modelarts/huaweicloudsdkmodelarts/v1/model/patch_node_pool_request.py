# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PatchNodePoolRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'pool_name': 'str',
        'nodepool_name': 'str',
        'body': 'PatchNodePoolRequestBody'
    }

    attribute_map = {
        'pool_name': 'pool_name',
        'nodepool_name': 'nodepool_name',
        'body': 'body'
    }

    def __init__(self, pool_name=None, nodepool_name=None, body=None):
        r"""PatchNodePoolRequest

        The model defined in huaweicloud sdk

        :param pool_name: **参数解释**：资源池名称。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type pool_name: str
        :param nodepool_name: **参数解释**：节点池名称。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type nodepool_name: str
        :param body: Body of the PatchNodePoolRequest
        :type body: :class:`huaweicloudsdkmodelarts.v1.PatchNodePoolRequestBody`
        """
        
        

        self._pool_name = None
        self._nodepool_name = None
        self._body = None
        self.discriminator = None

        self.pool_name = pool_name
        self.nodepool_name = nodepool_name
        if body is not None:
            self.body = body

    @property
    def pool_name(self):
        r"""Gets the pool_name of this PatchNodePoolRequest.

        **参数解释**：资源池名称。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The pool_name of this PatchNodePoolRequest.
        :rtype: str
        """
        return self._pool_name

    @pool_name.setter
    def pool_name(self, pool_name):
        r"""Sets the pool_name of this PatchNodePoolRequest.

        **参数解释**：资源池名称。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param pool_name: The pool_name of this PatchNodePoolRequest.
        :type pool_name: str
        """
        self._pool_name = pool_name

    @property
    def nodepool_name(self):
        r"""Gets the nodepool_name of this PatchNodePoolRequest.

        **参数解释**：节点池名称。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The nodepool_name of this PatchNodePoolRequest.
        :rtype: str
        """
        return self._nodepool_name

    @nodepool_name.setter
    def nodepool_name(self, nodepool_name):
        r"""Sets the nodepool_name of this PatchNodePoolRequest.

        **参数解释**：节点池名称。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param nodepool_name: The nodepool_name of this PatchNodePoolRequest.
        :type nodepool_name: str
        """
        self._nodepool_name = nodepool_name

    @property
    def body(self):
        r"""Gets the body of this PatchNodePoolRequest.

        :return: The body of this PatchNodePoolRequest.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.PatchNodePoolRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this PatchNodePoolRequest.

        :param body: The body of this PatchNodePoolRequest.
        :type body: :class:`huaweicloudsdkmodelarts.v1.PatchNodePoolRequestBody`
        """
        self._body = body

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
        if not isinstance(other, PatchNodePoolRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
