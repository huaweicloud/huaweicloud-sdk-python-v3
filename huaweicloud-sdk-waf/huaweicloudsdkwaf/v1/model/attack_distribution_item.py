# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AttackDistributionItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'key': 'str',
        'num': 'int',
        'items': 'list[AttackSubItem]'
    }

    attribute_map = {
        'key': 'key',
        'num': 'num',
        'items': 'items'
    }

    def __init__(self, key=None, num=None, items=None):
        r"""AttackDistributionItem

        The model defined in huaweicloud sdk

        :param key: 统计指标类型： - compliance_total_matched：内容合规检测命中次数 - injection_total_matched：提示词注入攻击检测命中次数 
        :type key: str
        :param num: 该类型总命中次数
        :type num: int
        :param items: 子类型分布列表
        :type items: list[:class:`huaweicloudsdkwaf.v1.AttackSubItem`]
        """
        
        

        self._key = None
        self._num = None
        self._items = None
        self.discriminator = None

        self.key = key
        self.num = num
        self.items = items

    @property
    def key(self):
        r"""Gets the key of this AttackDistributionItem.

        统计指标类型： - compliance_total_matched：内容合规检测命中次数 - injection_total_matched：提示词注入攻击检测命中次数 

        :return: The key of this AttackDistributionItem.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        r"""Sets the key of this AttackDistributionItem.

        统计指标类型： - compliance_total_matched：内容合规检测命中次数 - injection_total_matched：提示词注入攻击检测命中次数 

        :param key: The key of this AttackDistributionItem.
        :type key: str
        """
        self._key = key

    @property
    def num(self):
        r"""Gets the num of this AttackDistributionItem.

        该类型总命中次数

        :return: The num of this AttackDistributionItem.
        :rtype: int
        """
        return self._num

    @num.setter
    def num(self, num):
        r"""Sets the num of this AttackDistributionItem.

        该类型总命中次数

        :param num: The num of this AttackDistributionItem.
        :type num: int
        """
        self._num = num

    @property
    def items(self):
        r"""Gets the items of this AttackDistributionItem.

        子类型分布列表

        :return: The items of this AttackDistributionItem.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.AttackSubItem`]
        """
        return self._items

    @items.setter
    def items(self, items):
        r"""Sets the items of this AttackDistributionItem.

        子类型分布列表

        :param items: The items of this AttackDistributionItem.
        :type items: list[:class:`huaweicloudsdkwaf.v1.AttackSubItem`]
        """
        self._items = items

    def to_dict(self):
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
        if not isinstance(other, AttackDistributionItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
