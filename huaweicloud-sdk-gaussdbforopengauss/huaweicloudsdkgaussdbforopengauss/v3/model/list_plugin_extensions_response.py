# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPluginExtensionsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'body': 'list[PluginExtensions]'
    }

    attribute_map = {
        'body': 'body'
    }

    def __init__(self, body=None):
        """ListPluginExtensionsResponse

        The model defined in huaweicloud sdk

        :param body: 实例插件拓展信息
        :type body: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.PluginExtensions`]
        """
        
        super(ListPluginExtensionsResponse, self).__init__()

        self._body = None
        self.discriminator = None

        if body is not None:
            self.body = body

    @property
    def body(self):
        """Gets the body of this ListPluginExtensionsResponse.

        实例插件拓展信息

        :return: The body of this ListPluginExtensionsResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.PluginExtensions`]
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this ListPluginExtensionsResponse.

        实例插件拓展信息

        :param body: The body of this ListPluginExtensionsResponse.
        :type body: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.PluginExtensions`]
        """
        self._body = body

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
        if not isinstance(other, ListPluginExtensionsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
