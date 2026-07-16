# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceFlavorAnnotation:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'os_modelarts_flavor_image_filter': 'str'
    }

    attribute_map = {
        'os_modelarts_flavor_image_filter': 'os.modelarts.flavor/image.filter'
    }

    def __init__(self, os_modelarts_flavor_image_filter=None):
        r"""ResourceFlavorAnnotation

        The model defined in huaweicloud sdk

        :param os_modelarts_flavor_image_filter: **参数解释**：资源规格支持的私有镜像的过滤条件。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type os_modelarts_flavor_image_filter: str
        """
        
        

        self._os_modelarts_flavor_image_filter = None
        self.discriminator = None

        if os_modelarts_flavor_image_filter is not None:
            self.os_modelarts_flavor_image_filter = os_modelarts_flavor_image_filter

    @property
    def os_modelarts_flavor_image_filter(self):
        r"""Gets the os_modelarts_flavor_image_filter of this ResourceFlavorAnnotation.

        **参数解释**：资源规格支持的私有镜像的过滤条件。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The os_modelarts_flavor_image_filter of this ResourceFlavorAnnotation.
        :rtype: str
        """
        return self._os_modelarts_flavor_image_filter

    @os_modelarts_flavor_image_filter.setter
    def os_modelarts_flavor_image_filter(self, os_modelarts_flavor_image_filter):
        r"""Sets the os_modelarts_flavor_image_filter of this ResourceFlavorAnnotation.

        **参数解释**：资源规格支持的私有镜像的过滤条件。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param os_modelarts_flavor_image_filter: The os_modelarts_flavor_image_filter of this ResourceFlavorAnnotation.
        :type os_modelarts_flavor_image_filter: str
        """
        self._os_modelarts_flavor_image_filter = os_modelarts_flavor_image_filter

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
        if not isinstance(other, ResourceFlavorAnnotation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
