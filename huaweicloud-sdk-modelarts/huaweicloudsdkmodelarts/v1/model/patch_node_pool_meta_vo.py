# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PatchNodePoolMetaVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'annotations': 'PatchNodePoolAnnotations'
    }

    attribute_map = {
        'annotations': 'annotations'
    }

    def __init__(self, annotations=None):
        r"""PatchNodePoolMetaVO

        The model defined in huaweicloud sdk

        :param annotations: 
        :type annotations: :class:`huaweicloudsdkmodelarts.v1.PatchNodePoolAnnotations`
        """
        
        

        self._annotations = None
        self.discriminator = None

        if annotations is not None:
            self.annotations = annotations

    @property
    def annotations(self):
        r"""Gets the annotations of this PatchNodePoolMetaVO.

        :return: The annotations of this PatchNodePoolMetaVO.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.PatchNodePoolAnnotations`
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        r"""Sets the annotations of this PatchNodePoolMetaVO.

        :param annotations: The annotations of this PatchNodePoolMetaVO.
        :type annotations: :class:`huaweicloudsdkmodelarts.v1.PatchNodePoolAnnotations`
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
        if not isinstance(other, PatchNodePoolMetaVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
