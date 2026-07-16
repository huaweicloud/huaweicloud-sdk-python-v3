# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PoolMetadataCreation:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'labels': 'PoolLabelsCreation',
        'annotations': 'PoolAnnotationsCreation'
    }

    attribute_map = {
        'labels': 'labels',
        'annotations': 'annotations'
    }

    def __init__(self, labels=None, annotations=None):
        r"""PoolMetadataCreation

        The model defined in huaweicloud sdk

        :param labels: 
        :type labels: :class:`huaweicloudsdkmodelarts.v1.PoolLabelsCreation`
        :param annotations: 
        :type annotations: :class:`huaweicloudsdkmodelarts.v1.PoolAnnotationsCreation`
        """
        
        

        self._labels = None
        self._annotations = None
        self.discriminator = None

        self.labels = labels
        if annotations is not None:
            self.annotations = annotations

    @property
    def labels(self):
        r"""Gets the labels of this PoolMetadataCreation.

        :return: The labels of this PoolMetadataCreation.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.PoolLabelsCreation`
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        r"""Sets the labels of this PoolMetadataCreation.

        :param labels: The labels of this PoolMetadataCreation.
        :type labels: :class:`huaweicloudsdkmodelarts.v1.PoolLabelsCreation`
        """
        self._labels = labels

    @property
    def annotations(self):
        r"""Gets the annotations of this PoolMetadataCreation.

        :return: The annotations of this PoolMetadataCreation.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.PoolAnnotationsCreation`
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        r"""Sets the annotations of this PoolMetadataCreation.

        :param annotations: The annotations of this PoolMetadataCreation.
        :type annotations: :class:`huaweicloudsdkmodelarts.v1.PoolAnnotationsCreation`
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
        if not isinstance(other, PoolMetadataCreation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
