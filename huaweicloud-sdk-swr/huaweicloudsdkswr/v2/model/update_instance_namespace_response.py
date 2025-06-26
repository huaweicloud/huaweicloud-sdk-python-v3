# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateInstanceNamespaceResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'namespace_name': 'str',
        'metadata': 'NamespaceMetadata'
    }

    attribute_map = {
        'namespace_name': 'namespace_name',
        'metadata': 'metadata'
    }

    def __init__(self, namespace_name=None, metadata=None):
        r"""UpdateInstanceNamespaceResponse

        The model defined in huaweicloud sdk

        :param namespace_name: 命名空间名称
        :type namespace_name: str
        :param metadata: 
        :type metadata: :class:`huaweicloudsdkswr.v2.NamespaceMetadata`
        """
        
        super(UpdateInstanceNamespaceResponse, self).__init__()

        self._namespace_name = None
        self._metadata = None
        self.discriminator = None

        if namespace_name is not None:
            self.namespace_name = namespace_name
        if metadata is not None:
            self.metadata = metadata

    @property
    def namespace_name(self):
        r"""Gets the namespace_name of this UpdateInstanceNamespaceResponse.

        命名空间名称

        :return: The namespace_name of this UpdateInstanceNamespaceResponse.
        :rtype: str
        """
        return self._namespace_name

    @namespace_name.setter
    def namespace_name(self, namespace_name):
        r"""Sets the namespace_name of this UpdateInstanceNamespaceResponse.

        命名空间名称

        :param namespace_name: The namespace_name of this UpdateInstanceNamespaceResponse.
        :type namespace_name: str
        """
        self._namespace_name = namespace_name

    @property
    def metadata(self):
        r"""Gets the metadata of this UpdateInstanceNamespaceResponse.

        :return: The metadata of this UpdateInstanceNamespaceResponse.
        :rtype: :class:`huaweicloudsdkswr.v2.NamespaceMetadata`
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        r"""Sets the metadata of this UpdateInstanceNamespaceResponse.

        :param metadata: The metadata of this UpdateInstanceNamespaceResponse.
        :type metadata: :class:`huaweicloudsdkswr.v2.NamespaceMetadata`
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
        if not isinstance(other, UpdateInstanceNamespaceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
