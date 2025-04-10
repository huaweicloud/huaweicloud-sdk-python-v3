# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListComponentsResponse(SdkResponse):

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
        'kind': 'ComponentKindObj',
        'items': 'list[ComponentItem]',
        'total_count': 'int'
    }

    attribute_map = {
        'api_version': 'api_version',
        'kind': 'kind',
        'items': 'items',
        'total_count': 'total_count'
    }

    def __init__(self, api_version=None, kind=None, items=None, total_count=None):
        r"""ListComponentsResponse

        The model defined in huaweicloud sdk

        :param api_version: 
        :type api_version: :class:`huaweicloudsdkcae.v1.ApiVersionObj`
        :param kind: 
        :type kind: :class:`huaweicloudsdkcae.v1.ComponentKindObj`
        :param items: 组件列表。
        :type items: list[:class:`huaweicloudsdkcae.v1.ComponentItem`]
        :param total_count: 分页总数。
        :type total_count: int
        """
        
        super(ListComponentsResponse, self).__init__()

        self._api_version = None
        self._kind = None
        self._items = None
        self._total_count = None
        self.discriminator = None

        if api_version is not None:
            self.api_version = api_version
        if kind is not None:
            self.kind = kind
        if items is not None:
            self.items = items
        if total_count is not None:
            self.total_count = total_count

    @property
    def api_version(self):
        r"""Gets the api_version of this ListComponentsResponse.

        :return: The api_version of this ListComponentsResponse.
        :rtype: :class:`huaweicloudsdkcae.v1.ApiVersionObj`
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        r"""Sets the api_version of this ListComponentsResponse.

        :param api_version: The api_version of this ListComponentsResponse.
        :type api_version: :class:`huaweicloudsdkcae.v1.ApiVersionObj`
        """
        self._api_version = api_version

    @property
    def kind(self):
        r"""Gets the kind of this ListComponentsResponse.

        :return: The kind of this ListComponentsResponse.
        :rtype: :class:`huaweicloudsdkcae.v1.ComponentKindObj`
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        r"""Sets the kind of this ListComponentsResponse.

        :param kind: The kind of this ListComponentsResponse.
        :type kind: :class:`huaweicloudsdkcae.v1.ComponentKindObj`
        """
        self._kind = kind

    @property
    def items(self):
        r"""Gets the items of this ListComponentsResponse.

        组件列表。

        :return: The items of this ListComponentsResponse.
        :rtype: list[:class:`huaweicloudsdkcae.v1.ComponentItem`]
        """
        return self._items

    @items.setter
    def items(self, items):
        r"""Sets the items of this ListComponentsResponse.

        组件列表。

        :param items: The items of this ListComponentsResponse.
        :type items: list[:class:`huaweicloudsdkcae.v1.ComponentItem`]
        """
        self._items = items

    @property
    def total_count(self):
        r"""Gets the total_count of this ListComponentsResponse.

        分页总数。

        :return: The total_count of this ListComponentsResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ListComponentsResponse.

        分页总数。

        :param total_count: The total_count of this ListComponentsResponse.
        :type total_count: int
        """
        self._total_count = total_count

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
        if not isinstance(other, ListComponentsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
