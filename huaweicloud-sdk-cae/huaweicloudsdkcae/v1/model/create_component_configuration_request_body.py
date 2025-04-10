# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateComponentConfigurationRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'api_version': 'ApiVersionObj',
        'kind': 'ComponentConfigurationKindObj',
        'items': 'list[ConfigurationItem]'
    }

    attribute_map = {
        'api_version': 'api_version',
        'kind': 'kind',
        'items': 'items'
    }

    def __init__(self, api_version=None, kind=None, items=None):
        r"""CreateComponentConfigurationRequestBody

        The model defined in huaweicloud sdk

        :param api_version: 
        :type api_version: :class:`huaweicloudsdkcae.v1.ApiVersionObj`
        :param kind: 
        :type kind: :class:`huaweicloudsdkcae.v1.ComponentConfigurationKindObj`
        :param items: 配置项列表。
        :type items: list[:class:`huaweicloudsdkcae.v1.ConfigurationItem`]
        """
        
        

        self._api_version = None
        self._kind = None
        self._items = None
        self.discriminator = None

        self.api_version = api_version
        self.kind = kind
        self.items = items

    @property
    def api_version(self):
        r"""Gets the api_version of this CreateComponentConfigurationRequestBody.

        :return: The api_version of this CreateComponentConfigurationRequestBody.
        :rtype: :class:`huaweicloudsdkcae.v1.ApiVersionObj`
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        r"""Sets the api_version of this CreateComponentConfigurationRequestBody.

        :param api_version: The api_version of this CreateComponentConfigurationRequestBody.
        :type api_version: :class:`huaweicloudsdkcae.v1.ApiVersionObj`
        """
        self._api_version = api_version

    @property
    def kind(self):
        r"""Gets the kind of this CreateComponentConfigurationRequestBody.

        :return: The kind of this CreateComponentConfigurationRequestBody.
        :rtype: :class:`huaweicloudsdkcae.v1.ComponentConfigurationKindObj`
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        r"""Sets the kind of this CreateComponentConfigurationRequestBody.

        :param kind: The kind of this CreateComponentConfigurationRequestBody.
        :type kind: :class:`huaweicloudsdkcae.v1.ComponentConfigurationKindObj`
        """
        self._kind = kind

    @property
    def items(self):
        r"""Gets the items of this CreateComponentConfigurationRequestBody.

        配置项列表。

        :return: The items of this CreateComponentConfigurationRequestBody.
        :rtype: list[:class:`huaweicloudsdkcae.v1.ConfigurationItem`]
        """
        return self._items

    @items.setter
    def items(self, items):
        r"""Sets the items of this CreateComponentConfigurationRequestBody.

        配置项列表。

        :param items: The items of this CreateComponentConfigurationRequestBody.
        :type items: list[:class:`huaweicloudsdkcae.v1.ConfigurationItem`]
        """
        self._items = items

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
        if not isinstance(other, CreateComponentConfigurationRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
