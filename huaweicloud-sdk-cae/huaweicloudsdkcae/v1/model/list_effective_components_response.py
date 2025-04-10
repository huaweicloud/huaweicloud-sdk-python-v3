# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEffectiveComponentsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'api_version': 'str',
        'kind': 'str',
        'items': 'list[SecretDetail]'
    }

    attribute_map = {
        'api_version': 'api_version',
        'kind': 'kind',
        'items': 'items'
    }

    def __init__(self, api_version=None, kind=None, items=None):
        r"""ListEffectiveComponentsResponse

        The model defined in huaweicloud sdk

        :param api_version: API版本，固定值“v1”，该值不可修改。
        :type api_version: str
        :param kind: 资源种类。
        :type kind: str
        :param items: 定时启停规则所包含的所有应用，只在生效范围为application的时候需要填写。
        :type items: list[:class:`huaweicloudsdkcae.v1.SecretDetail`]
        """
        
        super(ListEffectiveComponentsResponse, self).__init__()

        self._api_version = None
        self._kind = None
        self._items = None
        self.discriminator = None

        if api_version is not None:
            self.api_version = api_version
        if kind is not None:
            self.kind = kind
        if items is not None:
            self.items = items

    @property
    def api_version(self):
        r"""Gets the api_version of this ListEffectiveComponentsResponse.

        API版本，固定值“v1”，该值不可修改。

        :return: The api_version of this ListEffectiveComponentsResponse.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        r"""Sets the api_version of this ListEffectiveComponentsResponse.

        API版本，固定值“v1”，该值不可修改。

        :param api_version: The api_version of this ListEffectiveComponentsResponse.
        :type api_version: str
        """
        self._api_version = api_version

    @property
    def kind(self):
        r"""Gets the kind of this ListEffectiveComponentsResponse.

        资源种类。

        :return: The kind of this ListEffectiveComponentsResponse.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        r"""Sets the kind of this ListEffectiveComponentsResponse.

        资源种类。

        :param kind: The kind of this ListEffectiveComponentsResponse.
        :type kind: str
        """
        self._kind = kind

    @property
    def items(self):
        r"""Gets the items of this ListEffectiveComponentsResponse.

        定时启停规则所包含的所有应用，只在生效范围为application的时候需要填写。

        :return: The items of this ListEffectiveComponentsResponse.
        :rtype: list[:class:`huaweicloudsdkcae.v1.SecretDetail`]
        """
        return self._items

    @items.setter
    def items(self, items):
        r"""Sets the items of this ListEffectiveComponentsResponse.

        定时启停规则所包含的所有应用，只在生效范围为application的时候需要填写。

        :param items: The items of this ListEffectiveComponentsResponse.
        :type items: list[:class:`huaweicloudsdkcae.v1.SecretDetail`]
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
        if not isinstance(other, ListEffectiveComponentsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
