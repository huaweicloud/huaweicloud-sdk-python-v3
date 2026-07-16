# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceFlavorMetadata:

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
        'labels': 'ResourceFlavorLabel',
        'annotations': 'ResourceFlavorAnnotation'
    }

    attribute_map = {
        'name': 'name',
        'labels': 'labels',
        'annotations': 'annotations'
    }

    def __init__(self, name=None, labels=None, annotations=None):
        r"""ResourceFlavorMetadata

        The model defined in huaweicloud sdk

        :param name: **参数解释**：资源规格的ID。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type name: str
        :param labels: 
        :type labels: :class:`huaweicloudsdkmodelarts.v1.ResourceFlavorLabel`
        :param annotations: 
        :type annotations: :class:`huaweicloudsdkmodelarts.v1.ResourceFlavorAnnotation`
        """
        
        

        self._name = None
        self._labels = None
        self._annotations = None
        self.discriminator = None

        self.name = name
        self.labels = labels
        if annotations is not None:
            self.annotations = annotations

    @property
    def name(self):
        r"""Gets the name of this ResourceFlavorMetadata.

        **参数解释**：资源规格的ID。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The name of this ResourceFlavorMetadata.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ResourceFlavorMetadata.

        **参数解释**：资源规格的ID。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param name: The name of this ResourceFlavorMetadata.
        :type name: str
        """
        self._name = name

    @property
    def labels(self):
        r"""Gets the labels of this ResourceFlavorMetadata.

        :return: The labels of this ResourceFlavorMetadata.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ResourceFlavorLabel`
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        r"""Sets the labels of this ResourceFlavorMetadata.

        :param labels: The labels of this ResourceFlavorMetadata.
        :type labels: :class:`huaweicloudsdkmodelarts.v1.ResourceFlavorLabel`
        """
        self._labels = labels

    @property
    def annotations(self):
        r"""Gets the annotations of this ResourceFlavorMetadata.

        :return: The annotations of this ResourceFlavorMetadata.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ResourceFlavorAnnotation`
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        r"""Sets the annotations of this ResourceFlavorMetadata.

        :param annotations: The annotations of this ResourceFlavorMetadata.
        :type annotations: :class:`huaweicloudsdkmodelarts.v1.ResourceFlavorAnnotation`
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
        if not isinstance(other, ResourceFlavorMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
