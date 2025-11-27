# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPolicyInstancesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'items': 'list[UCSConstraint]',
        'kind': 'str',
        'api_version': 'str'
    }

    attribute_map = {
        'items': 'items',
        'kind': 'kind',
        'api_version': 'apiVersion'
    }

    def __init__(self, items=None, kind=None, api_version=None):
        r"""ListPolicyInstancesResponse

        The model defined in huaweicloud sdk

        :param items: 策略实例列表
        :type items: list[:class:`huaweicloudsdkucs.v1.UCSConstraint`]
        :param kind: API类型
        :type kind: str
        :param api_version: API版本
        :type api_version: str
        """
        
        super().__init__()

        self._items = None
        self._kind = None
        self._api_version = None
        self.discriminator = None

        if items is not None:
            self.items = items
        if kind is not None:
            self.kind = kind
        if api_version is not None:
            self.api_version = api_version

    @property
    def items(self):
        r"""Gets the items of this ListPolicyInstancesResponse.

        策略实例列表

        :return: The items of this ListPolicyInstancesResponse.
        :rtype: list[:class:`huaweicloudsdkucs.v1.UCSConstraint`]
        """
        return self._items

    @items.setter
    def items(self, items):
        r"""Sets the items of this ListPolicyInstancesResponse.

        策略实例列表

        :param items: The items of this ListPolicyInstancesResponse.
        :type items: list[:class:`huaweicloudsdkucs.v1.UCSConstraint`]
        """
        self._items = items

    @property
    def kind(self):
        r"""Gets the kind of this ListPolicyInstancesResponse.

        API类型

        :return: The kind of this ListPolicyInstancesResponse.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        r"""Sets the kind of this ListPolicyInstancesResponse.

        API类型

        :param kind: The kind of this ListPolicyInstancesResponse.
        :type kind: str
        """
        self._kind = kind

    @property
    def api_version(self):
        r"""Gets the api_version of this ListPolicyInstancesResponse.

        API版本

        :return: The api_version of this ListPolicyInstancesResponse.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        r"""Sets the api_version of this ListPolicyInstancesResponse.

        API版本

        :param api_version: The api_version of this ListPolicyInstancesResponse.
        :type api_version: str
        """
        self._api_version = api_version

    def to_dict(self):
        import warnings
        warnings.warn("ListPolicyInstancesResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListPolicyInstancesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
