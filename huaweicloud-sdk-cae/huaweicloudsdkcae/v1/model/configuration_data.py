# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConfigurationData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'spec': 'ConfigurationRequestDataSpec',
        'metadata': 'ConfigurationDataMetadata'
    }

    attribute_map = {
        'spec': 'spec',
        'metadata': 'metadata'
    }

    def __init__(self, spec=None, metadata=None):
        r"""ConfigurationData

        The model defined in huaweicloud sdk

        :param spec: 
        :type spec: :class:`huaweicloudsdkcae.v1.ConfigurationRequestDataSpec`
        :param metadata: 
        :type metadata: :class:`huaweicloudsdkcae.v1.ConfigurationDataMetadata`
        """
        
        

        self._spec = None
        self._metadata = None
        self.discriminator = None

        if spec is not None:
            self.spec = spec
        if metadata is not None:
            self.metadata = metadata

    @property
    def spec(self):
        r"""Gets the spec of this ConfigurationData.

        :return: The spec of this ConfigurationData.
        :rtype: :class:`huaweicloudsdkcae.v1.ConfigurationRequestDataSpec`
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        r"""Sets the spec of this ConfigurationData.

        :param spec: The spec of this ConfigurationData.
        :type spec: :class:`huaweicloudsdkcae.v1.ConfigurationRequestDataSpec`
        """
        self._spec = spec

    @property
    def metadata(self):
        r"""Gets the metadata of this ConfigurationData.

        :return: The metadata of this ConfigurationData.
        :rtype: :class:`huaweicloudsdkcae.v1.ConfigurationDataMetadata`
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        r"""Sets the metadata of this ConfigurationData.

        :param metadata: The metadata of this ConfigurationData.
        :type metadata: :class:`huaweicloudsdkcae.v1.ConfigurationDataMetadata`
        """
        self._metadata = metadata

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
        if not isinstance(other, ConfigurationData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
