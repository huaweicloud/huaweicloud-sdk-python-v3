# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowMessageReceiveConfigResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'scope': 'str',
        'resource_types': 'list[str]',
        'language': 'LanguageEnum'
    }

    attribute_map = {
        'scope': 'scope',
        'resource_types': 'resource_types',
        'language': 'language'
    }

    def __init__(self, scope=None, resource_types=None, language=None):
        r"""ShowMessageReceiveConfigResponse

        The model defined in huaweicloud sdk

        :param scope: 接收范围（不接收消息(none)、仅接收自己操作的消息(mine)、接收全部消息(all)）
        :type scope: str
        :param resource_types: 资源类型
        :type resource_types: list[str]
        :param language: 
        :type language: :class:`huaweicloudsdkeihealth.v1.LanguageEnum`
        """
        
        super(ShowMessageReceiveConfigResponse, self).__init__()

        self._scope = None
        self._resource_types = None
        self._language = None
        self.discriminator = None

        if scope is not None:
            self.scope = scope
        if resource_types is not None:
            self.resource_types = resource_types
        if language is not None:
            self.language = language

    @property
    def scope(self):
        r"""Gets the scope of this ShowMessageReceiveConfigResponse.

        接收范围（不接收消息(none)、仅接收自己操作的消息(mine)、接收全部消息(all)）

        :return: The scope of this ShowMessageReceiveConfigResponse.
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        r"""Sets the scope of this ShowMessageReceiveConfigResponse.

        接收范围（不接收消息(none)、仅接收自己操作的消息(mine)、接收全部消息(all)）

        :param scope: The scope of this ShowMessageReceiveConfigResponse.
        :type scope: str
        """
        self._scope = scope

    @property
    def resource_types(self):
        r"""Gets the resource_types of this ShowMessageReceiveConfigResponse.

        资源类型

        :return: The resource_types of this ShowMessageReceiveConfigResponse.
        :rtype: list[str]
        """
        return self._resource_types

    @resource_types.setter
    def resource_types(self, resource_types):
        r"""Sets the resource_types of this ShowMessageReceiveConfigResponse.

        资源类型

        :param resource_types: The resource_types of this ShowMessageReceiveConfigResponse.
        :type resource_types: list[str]
        """
        self._resource_types = resource_types

    @property
    def language(self):
        r"""Gets the language of this ShowMessageReceiveConfigResponse.

        :return: The language of this ShowMessageReceiveConfigResponse.
        :rtype: :class:`huaweicloudsdkeihealth.v1.LanguageEnum`
        """
        return self._language

    @language.setter
    def language(self, language):
        r"""Sets the language of this ShowMessageReceiveConfigResponse.

        :param language: The language of this ShowMessageReceiveConfigResponse.
        :type language: :class:`huaweicloudsdkeihealth.v1.LanguageEnum`
        """
        self._language = language

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
        if not isinstance(other, ShowMessageReceiveConfigResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
