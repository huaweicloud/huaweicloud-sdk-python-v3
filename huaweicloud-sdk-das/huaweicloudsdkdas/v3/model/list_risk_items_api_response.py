# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRiskItemsApiResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'engine_type': 'str',
        'items': 'list[RiskItemInfo]'
    }

    attribute_map = {
        'engine_type': 'engine_type',
        'items': 'items'
    }

    def __init__(self, engine_type=None, items=None):
        r"""ListRiskItemsApiResponse

        The model defined in huaweicloud sdk

        :param engine_type: 数据库类型
        :type engine_type: str
        :param items: 指标阈值列表
        :type items: list[:class:`huaweicloudsdkdas.v3.RiskItemInfo`]
        """
        
        super().__init__()

        self._engine_type = None
        self._items = None
        self.discriminator = None

        if engine_type is not None:
            self.engine_type = engine_type
        if items is not None:
            self.items = items

    @property
    def engine_type(self):
        r"""Gets the engine_type of this ListRiskItemsApiResponse.

        数据库类型

        :return: The engine_type of this ListRiskItemsApiResponse.
        :rtype: str
        """
        return self._engine_type

    @engine_type.setter
    def engine_type(self, engine_type):
        r"""Sets the engine_type of this ListRiskItemsApiResponse.

        数据库类型

        :param engine_type: The engine_type of this ListRiskItemsApiResponse.
        :type engine_type: str
        """
        self._engine_type = engine_type

    @property
    def items(self):
        r"""Gets the items of this ListRiskItemsApiResponse.

        指标阈值列表

        :return: The items of this ListRiskItemsApiResponse.
        :rtype: list[:class:`huaweicloudsdkdas.v3.RiskItemInfo`]
        """
        return self._items

    @items.setter
    def items(self, items):
        r"""Sets the items of this ListRiskItemsApiResponse.

        指标阈值列表

        :param items: The items of this ListRiskItemsApiResponse.
        :type items: list[:class:`huaweicloudsdkdas.v3.RiskItemInfo`]
        """
        self._items = items

    def to_dict(self):
        import warnings
        warnings.warn("ListRiskItemsApiResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListRiskItemsApiResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
