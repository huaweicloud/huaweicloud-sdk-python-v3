# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAddonInstancesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'kind': 'str',
        'api_version': 'str',
        'items': 'list[AddonInstance]'
    }

    attribute_map = {
        'kind': 'kind',
        'api_version': 'apiVersion',
        'items': 'items'
    }

    def __init__(self, kind=None, api_version=None, items=None):
        """ListAddonInstancesResponse

        The model defined in huaweicloud sdk

        :param kind: API类型，固定值“Addon”，该值不可修改。
        :type kind: str
        :param api_version: API版本，固定值“v3”，该值不可修改。
        :type api_version: str
        :param items: 插件实例列表
        :type items: list[:class:`huaweicloudsdkcce.v3.AddonInstance`]
        """
        
        super(ListAddonInstancesResponse, self).__init__()

        self._kind = None
        self._api_version = None
        self._items = None
        self.discriminator = None

        if kind is not None:
            self.kind = kind
        if api_version is not None:
            self.api_version = api_version
        if items is not None:
            self.items = items

    @property
    def kind(self):
        """Gets the kind of this ListAddonInstancesResponse.

        API类型，固定值“Addon”，该值不可修改。

        :return: The kind of this ListAddonInstancesResponse.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this ListAddonInstancesResponse.

        API类型，固定值“Addon”，该值不可修改。

        :param kind: The kind of this ListAddonInstancesResponse.
        :type kind: str
        """
        self._kind = kind

    @property
    def api_version(self):
        """Gets the api_version of this ListAddonInstancesResponse.

        API版本，固定值“v3”，该值不可修改。

        :return: The api_version of this ListAddonInstancesResponse.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """Sets the api_version of this ListAddonInstancesResponse.

        API版本，固定值“v3”，该值不可修改。

        :param api_version: The api_version of this ListAddonInstancesResponse.
        :type api_version: str
        """
        self._api_version = api_version

    @property
    def items(self):
        """Gets the items of this ListAddonInstancesResponse.

        插件实例列表

        :return: The items of this ListAddonInstancesResponse.
        :rtype: list[:class:`huaweicloudsdkcce.v3.AddonInstance`]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this ListAddonInstancesResponse.

        插件实例列表

        :param items: The items of this ListAddonInstancesResponse.
        :type items: list[:class:`huaweicloudsdkcce.v3.AddonInstance`]
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
        if not isinstance(other, ListAddonInstancesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
