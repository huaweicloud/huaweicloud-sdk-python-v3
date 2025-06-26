# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateInstanceNamespaceRequestBody:

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
        r"""CreateInstanceNamespaceRequestBody

        The model defined in huaweicloud sdk

        :param namespace_name: 命名空间名称，小写字母或数字开头，后面跟小写字母、数字、点、下划线或中划线（其中点、下划线、中划线不能直接连续），小写字母或数字结尾，1-64个字符。
        :type namespace_name: str
        :param metadata: 
        :type metadata: :class:`huaweicloudsdkswr.v2.NamespaceMetadata`
        """
        
        

        self._namespace_name = None
        self._metadata = None
        self.discriminator = None

        self.namespace_name = namespace_name
        self.metadata = metadata

    @property
    def namespace_name(self):
        r"""Gets the namespace_name of this CreateInstanceNamespaceRequestBody.

        命名空间名称，小写字母或数字开头，后面跟小写字母、数字、点、下划线或中划线（其中点、下划线、中划线不能直接连续），小写字母或数字结尾，1-64个字符。

        :return: The namespace_name of this CreateInstanceNamespaceRequestBody.
        :rtype: str
        """
        return self._namespace_name

    @namespace_name.setter
    def namespace_name(self, namespace_name):
        r"""Sets the namespace_name of this CreateInstanceNamespaceRequestBody.

        命名空间名称，小写字母或数字开头，后面跟小写字母、数字、点、下划线或中划线（其中点、下划线、中划线不能直接连续），小写字母或数字结尾，1-64个字符。

        :param namespace_name: The namespace_name of this CreateInstanceNamespaceRequestBody.
        :type namespace_name: str
        """
        self._namespace_name = namespace_name

    @property
    def metadata(self):
        r"""Gets the metadata of this CreateInstanceNamespaceRequestBody.

        :return: The metadata of this CreateInstanceNamespaceRequestBody.
        :rtype: :class:`huaweicloudsdkswr.v2.NamespaceMetadata`
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        r"""Sets the metadata of this CreateInstanceNamespaceRequestBody.

        :param metadata: The metadata of this CreateInstanceNamespaceRequestBody.
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
        if not isinstance(other, CreateInstanceNamespaceRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
