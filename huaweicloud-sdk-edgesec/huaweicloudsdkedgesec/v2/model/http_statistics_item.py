# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HttpStatisticsItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'attack_category': 'str',
        'stat_num': 'int'
    }

    attribute_map = {
        'attack_category': 'attack_category',
        'stat_num': 'stat_num'
    }

    def __init__(self, attack_category=None, stat_num=None):
        r"""HttpStatisticsItem

        The model defined in huaweicloud sdk

        :param attack_category: 攻击类别
        :type attack_category: str
        :param stat_num: 统计数量
        :type stat_num: int
        """
        
        

        self._attack_category = None
        self._stat_num = None
        self.discriminator = None

        if attack_category is not None:
            self.attack_category = attack_category
        if stat_num is not None:
            self.stat_num = stat_num

    @property
    def attack_category(self):
        r"""Gets the attack_category of this HttpStatisticsItem.

        攻击类别

        :return: The attack_category of this HttpStatisticsItem.
        :rtype: str
        """
        return self._attack_category

    @attack_category.setter
    def attack_category(self, attack_category):
        r"""Sets the attack_category of this HttpStatisticsItem.

        攻击类别

        :param attack_category: The attack_category of this HttpStatisticsItem.
        :type attack_category: str
        """
        self._attack_category = attack_category

    @property
    def stat_num(self):
        r"""Gets the stat_num of this HttpStatisticsItem.

        统计数量

        :return: The stat_num of this HttpStatisticsItem.
        :rtype: int
        """
        return self._stat_num

    @stat_num.setter
    def stat_num(self, stat_num):
        r"""Sets the stat_num of this HttpStatisticsItem.

        统计数量

        :param stat_num: The stat_num of this HttpStatisticsItem.
        :type stat_num: int
        """
        self._stat_num = stat_num

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
        if not isinstance(other, HttpStatisticsItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
