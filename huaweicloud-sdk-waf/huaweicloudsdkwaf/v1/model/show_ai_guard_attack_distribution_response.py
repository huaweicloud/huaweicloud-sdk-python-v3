# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAiGuardAttackDistributionResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'num': 'int',
        'items': 'list[AttackDistributionItem]',
        'x_request_id': 'str'
    }

    attribute_map = {
        'num': 'num',
        'items': 'items',
        'x_request_id': 'X-request-id'
    }

    def __init__(self, num=None, items=None, x_request_id=None):
        r"""ShowAiGuardAttackDistributionResponse

        The model defined in huaweicloud sdk

        :param num: 总命中数，数量等于下一级items的total的数量
        :type num: int
        :param items: 攻击类型分布列表
        :type items: list[:class:`huaweicloudsdkwaf.v1.AttackDistributionItem`]
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super().__init__()

        self._num = None
        self._items = None
        self._x_request_id = None
        self.discriminator = None

        if num is not None:
            self.num = num
        if items is not None:
            self.items = items
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def num(self):
        r"""Gets the num of this ShowAiGuardAttackDistributionResponse.

        总命中数，数量等于下一级items的total的数量

        :return: The num of this ShowAiGuardAttackDistributionResponse.
        :rtype: int
        """
        return self._num

    @num.setter
    def num(self, num):
        r"""Sets the num of this ShowAiGuardAttackDistributionResponse.

        总命中数，数量等于下一级items的total的数量

        :param num: The num of this ShowAiGuardAttackDistributionResponse.
        :type num: int
        """
        self._num = num

    @property
    def items(self):
        r"""Gets the items of this ShowAiGuardAttackDistributionResponse.

        攻击类型分布列表

        :return: The items of this ShowAiGuardAttackDistributionResponse.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.AttackDistributionItem`]
        """
        return self._items

    @items.setter
    def items(self, items):
        r"""Sets the items of this ShowAiGuardAttackDistributionResponse.

        攻击类型分布列表

        :param items: The items of this ShowAiGuardAttackDistributionResponse.
        :type items: list[:class:`huaweicloudsdkwaf.v1.AttackDistributionItem`]
        """
        self._items = items

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ShowAiGuardAttackDistributionResponse.

        :return: The x_request_id of this ShowAiGuardAttackDistributionResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ShowAiGuardAttackDistributionResponse.

        :param x_request_id: The x_request_id of this ShowAiGuardAttackDistributionResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

    def to_dict(self):
        import warnings
        warnings.warn("ShowAiGuardAttackDistributionResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowAiGuardAttackDistributionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
