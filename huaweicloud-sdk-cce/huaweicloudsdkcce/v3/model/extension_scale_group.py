# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExtensionScaleGroup:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'metadata': 'ExtensionScaleGroupMetadata',
        'spec': 'ExtensionScaleGroupSpec'
    }

    attribute_map = {
        'metadata': 'metadata',
        'spec': 'spec'
    }

    def __init__(self, metadata=None, spec=None):
        r"""ExtensionScaleGroup

        The model defined in huaweicloud sdk

        :param metadata: 
        :type metadata: :class:`huaweicloudsdkcce.v3.ExtensionScaleGroupMetadata`
        :param spec: 
        :type spec: :class:`huaweicloudsdkcce.v3.ExtensionScaleGroupSpec`
        """
        
        

        self._metadata = None
        self._spec = None
        self.discriminator = None

        if metadata is not None:
            self.metadata = metadata
        if spec is not None:
            self.spec = spec

    @property
    def metadata(self):
        r"""Gets the metadata of this ExtensionScaleGroup.

        :return: The metadata of this ExtensionScaleGroup.
        :rtype: :class:`huaweicloudsdkcce.v3.ExtensionScaleGroupMetadata`
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        r"""Sets the metadata of this ExtensionScaleGroup.

        :param metadata: The metadata of this ExtensionScaleGroup.
        :type metadata: :class:`huaweicloudsdkcce.v3.ExtensionScaleGroupMetadata`
        """
        self._metadata = metadata

    @property
    def spec(self):
        r"""Gets the spec of this ExtensionScaleGroup.

        :return: The spec of this ExtensionScaleGroup.
        :rtype: :class:`huaweicloudsdkcce.v3.ExtensionScaleGroupSpec`
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        r"""Sets the spec of this ExtensionScaleGroup.

        :param spec: The spec of this ExtensionScaleGroup.
        :type spec: :class:`huaweicloudsdkcce.v3.ExtensionScaleGroupSpec`
        """
        self._spec = spec

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ExtensionScaleGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
