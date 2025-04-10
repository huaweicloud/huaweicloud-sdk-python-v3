# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateDomainResponse(SdkResponse):

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
        'items': 'list[DomainItem]',
        'kind': 'str'
    }

    attribute_map = {
        'api_version': 'api_version',
        'items': 'items',
        'kind': 'kind'
    }

    def __init__(self, api_version=None, items=None, kind=None):
        r"""CreateDomainResponse

        The model defined in huaweicloud sdk

        :param api_version: 
        :type api_version: :class:`huaweicloudsdkcae.v1.ApiVersionObj`
        :param items: 域名列表。
        :type items: list[:class:`huaweicloudsdkcae.v1.DomainItem`]
        :param kind: API类型，固定值“Domain”，该值不可修改。
        :type kind: str
        """
        
        super(CreateDomainResponse, self).__init__()

        self._api_version = None
        self._items = None
        self._kind = None
        self.discriminator = None

        if api_version is not None:
            self.api_version = api_version
        if items is not None:
            self.items = items
        if kind is not None:
            self.kind = kind

    @property
    def api_version(self):
        r"""Gets the api_version of this CreateDomainResponse.

        :return: The api_version of this CreateDomainResponse.
        :rtype: :class:`huaweicloudsdkcae.v1.ApiVersionObj`
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        r"""Sets the api_version of this CreateDomainResponse.

        :param api_version: The api_version of this CreateDomainResponse.
        :type api_version: :class:`huaweicloudsdkcae.v1.ApiVersionObj`
        """
        self._api_version = api_version

    @property
    def items(self):
        r"""Gets the items of this CreateDomainResponse.

        域名列表。

        :return: The items of this CreateDomainResponse.
        :rtype: list[:class:`huaweicloudsdkcae.v1.DomainItem`]
        """
        return self._items

    @items.setter
    def items(self, items):
        r"""Sets the items of this CreateDomainResponse.

        域名列表。

        :param items: The items of this CreateDomainResponse.
        :type items: list[:class:`huaweicloudsdkcae.v1.DomainItem`]
        """
        self._items = items

    @property
    def kind(self):
        r"""Gets the kind of this CreateDomainResponse.

        API类型，固定值“Domain”，该值不可修改。

        :return: The kind of this CreateDomainResponse.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        r"""Sets the kind of this CreateDomainResponse.

        API类型，固定值“Domain”，该值不可修改。

        :param kind: The kind of this CreateDomainResponse.
        :type kind: str
        """
        self._kind = kind

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
        if not isinstance(other, CreateDomainResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
