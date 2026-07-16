# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateNodePoolMetaVO:

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
        'annotations': 'CreateNodePoolAnnotations'
    }

    attribute_map = {
        'name': 'name',
        'annotations': 'annotations'
    }

    def __init__(self, name=None, annotations=None):
        r"""CreateNodePoolMetaVO

        The model defined in huaweicloud sdk

        :param name: **参数解释**：节点池名称。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type name: str
        :param annotations: 
        :type annotations: :class:`huaweicloudsdkmodelarts.v1.CreateNodePoolAnnotations`
        """
        
        

        self._name = None
        self._annotations = None
        self.discriminator = None

        self.name = name
        if annotations is not None:
            self.annotations = annotations

    @property
    def name(self):
        r"""Gets the name of this CreateNodePoolMetaVO.

        **参数解释**：节点池名称。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The name of this CreateNodePoolMetaVO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateNodePoolMetaVO.

        **参数解释**：节点池名称。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param name: The name of this CreateNodePoolMetaVO.
        :type name: str
        """
        self._name = name

    @property
    def annotations(self):
        r"""Gets the annotations of this CreateNodePoolMetaVO.

        :return: The annotations of this CreateNodePoolMetaVO.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.CreateNodePoolAnnotations`
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        r"""Sets the annotations of this CreateNodePoolMetaVO.

        :param annotations: The annotations of this CreateNodePoolMetaVO.
        :type annotations: :class:`huaweicloudsdkmodelarts.v1.CreateNodePoolAnnotations`
        """
        self._annotations = annotations

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
        if not isinstance(other, CreateNodePoolMetaVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
