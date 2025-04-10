# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPartitionsResponse(SdkResponse):

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
        'items': 'list[Partition]'
    }

    attribute_map = {
        'kind': 'kind',
        'api_version': 'apiVersion',
        'items': 'items'
    }

    def __init__(self, kind=None, api_version=None, items=None):
        r"""ListPartitionsResponse

        The model defined in huaweicloud sdk

        :param kind: 资源类型
        :type kind: str
        :param api_version: API版本
        :type api_version: str
        :param items: 
        :type items: list[:class:`huaweicloudsdkcce.v3.Partition`]
        """
        
        super(ListPartitionsResponse, self).__init__()

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
        r"""Gets the kind of this ListPartitionsResponse.

        资源类型

        :return: The kind of this ListPartitionsResponse.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        r"""Sets the kind of this ListPartitionsResponse.

        资源类型

        :param kind: The kind of this ListPartitionsResponse.
        :type kind: str
        """
        self._kind = kind

    @property
    def api_version(self):
        r"""Gets the api_version of this ListPartitionsResponse.

        API版本

        :return: The api_version of this ListPartitionsResponse.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        r"""Sets the api_version of this ListPartitionsResponse.

        API版本

        :param api_version: The api_version of this ListPartitionsResponse.
        :type api_version: str
        """
        self._api_version = api_version

    @property
    def items(self):
        r"""Gets the items of this ListPartitionsResponse.

        :return: The items of this ListPartitionsResponse.
        :rtype: list[:class:`huaweicloudsdkcce.v3.Partition`]
        """
        return self._items

    @items.setter
    def items(self, items):
        r"""Sets the items of this ListPartitionsResponse.

        :param items: The items of this ListPartitionsResponse.
        :type items: list[:class:`huaweicloudsdkcce.v3.Partition`]
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
        if not isinstance(other, ListPartitionsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
