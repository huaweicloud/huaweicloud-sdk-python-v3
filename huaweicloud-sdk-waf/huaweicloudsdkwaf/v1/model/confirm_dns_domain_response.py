# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConfirmDnsDomainResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'next_marker': 'str',
        'items': 'list[DnsDomain]'
    }

    attribute_map = {
        'next_marker': 'next_marker',
        'items': 'items'
    }

    def __init__(self, next_marker=None, items=None):
        r"""ConfirmDnsDomainResponse

        The model defined in huaweicloud sdk

        :param next_marker: dns标识
        :type next_marker: str
        :param items: dns域名列表
        :type items: list[:class:`huaweicloudsdkwaf.v1.DnsDomain`]
        """
        
        super().__init__()

        self._next_marker = None
        self._items = None
        self.discriminator = None

        if next_marker is not None:
            self.next_marker = next_marker
        if items is not None:
            self.items = items

    @property
    def next_marker(self):
        r"""Gets the next_marker of this ConfirmDnsDomainResponse.

        dns标识

        :return: The next_marker of this ConfirmDnsDomainResponse.
        :rtype: str
        """
        return self._next_marker

    @next_marker.setter
    def next_marker(self, next_marker):
        r"""Sets the next_marker of this ConfirmDnsDomainResponse.

        dns标识

        :param next_marker: The next_marker of this ConfirmDnsDomainResponse.
        :type next_marker: str
        """
        self._next_marker = next_marker

    @property
    def items(self):
        r"""Gets the items of this ConfirmDnsDomainResponse.

        dns域名列表

        :return: The items of this ConfirmDnsDomainResponse.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.DnsDomain`]
        """
        return self._items

    @items.setter
    def items(self, items):
        r"""Sets the items of this ConfirmDnsDomainResponse.

        dns域名列表

        :param items: The items of this ConfirmDnsDomainResponse.
        :type items: list[:class:`huaweicloudsdkwaf.v1.DnsDomain`]
        """
        self._items = items

    def to_dict(self):
        import warnings
        warnings.warn("ConfirmDnsDomainResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ConfirmDnsDomainResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
