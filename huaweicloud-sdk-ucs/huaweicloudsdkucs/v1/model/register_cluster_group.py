# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RegisterClusterGroup:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'metadata': 'RegisterClusterGroupObjectMeta',
        'spec': 'RegisterClusterGroupSpec'
    }

    attribute_map = {
        'metadata': 'metadata',
        'spec': 'spec'
    }

    def __init__(self, metadata=None, spec=None):
        r"""RegisterClusterGroup

        The model defined in huaweicloud sdk

        :param metadata: 
        :type metadata: :class:`huaweicloudsdkucs.v1.RegisterClusterGroupObjectMeta`
        :param spec: 
        :type spec: :class:`huaweicloudsdkucs.v1.RegisterClusterGroupSpec`
        """
        
        

        self._metadata = None
        self._spec = None
        self.discriminator = None

        self.metadata = metadata
        if spec is not None:
            self.spec = spec

    @property
    def metadata(self):
        r"""Gets the metadata of this RegisterClusterGroup.

        :return: The metadata of this RegisterClusterGroup.
        :rtype: :class:`huaweicloudsdkucs.v1.RegisterClusterGroupObjectMeta`
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        r"""Sets the metadata of this RegisterClusterGroup.

        :param metadata: The metadata of this RegisterClusterGroup.
        :type metadata: :class:`huaweicloudsdkucs.v1.RegisterClusterGroupObjectMeta`
        """
        self._metadata = metadata

    @property
    def spec(self):
        r"""Gets the spec of this RegisterClusterGroup.

        :return: The spec of this RegisterClusterGroup.
        :rtype: :class:`huaweicloudsdkucs.v1.RegisterClusterGroupSpec`
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        r"""Sets the spec of this RegisterClusterGroup.

        :param spec: The spec of this RegisterClusterGroup.
        :type spec: :class:`huaweicloudsdkucs.v1.RegisterClusterGroupSpec`
        """
        self._spec = spec

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
        if not isinstance(other, RegisterClusterGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
