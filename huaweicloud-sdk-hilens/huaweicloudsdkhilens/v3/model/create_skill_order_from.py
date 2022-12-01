# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSkillOrderFrom:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'data': 'list[SkillInfo]',
        'total': 'int',
        'skill_id': 'str',
        'amount': 'int',
        'commission_flag': 'int'
    }

    attribute_map = {
        'data': 'data',
        'total': 'total',
        'skill_id': 'skill_id',
        'amount': 'amount',
        'commission_flag': 'commission_flag'
    }

    def __init__(self, data=None, total=None, skill_id=None, amount=None, commission_flag=None):
        """CreateSkillOrderFrom

        The model defined in huaweicloud sdk

        :param data: 技能列表
        :type data: list[:class:`huaweicloudsdkhilens.v3.SkillInfo`]
        :param total: 总数量
        :type total: int
        :param skill_id: 技能ID
        :type skill_id: str
        :param amount: 购买个数
        :type amount: int
        :param commission_flag: 定制技能标识
        :type commission_flag: int
        """
        
        

        self._data = None
        self._total = None
        self._skill_id = None
        self._amount = None
        self._commission_flag = None
        self.discriminator = None

        if data is not None:
            self.data = data
        if total is not None:
            self.total = total
        self.skill_id = skill_id
        self.amount = amount
        self.commission_flag = commission_flag

    @property
    def data(self):
        """Gets the data of this CreateSkillOrderFrom.

        技能列表

        :return: The data of this CreateSkillOrderFrom.
        :rtype: list[:class:`huaweicloudsdkhilens.v3.SkillInfo`]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this CreateSkillOrderFrom.

        技能列表

        :param data: The data of this CreateSkillOrderFrom.
        :type data: list[:class:`huaweicloudsdkhilens.v3.SkillInfo`]
        """
        self._data = data

    @property
    def total(self):
        """Gets the total of this CreateSkillOrderFrom.

        总数量

        :return: The total of this CreateSkillOrderFrom.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this CreateSkillOrderFrom.

        总数量

        :param total: The total of this CreateSkillOrderFrom.
        :type total: int
        """
        self._total = total

    @property
    def skill_id(self):
        """Gets the skill_id of this CreateSkillOrderFrom.

        技能ID

        :return: The skill_id of this CreateSkillOrderFrom.
        :rtype: str
        """
        return self._skill_id

    @skill_id.setter
    def skill_id(self, skill_id):
        """Sets the skill_id of this CreateSkillOrderFrom.

        技能ID

        :param skill_id: The skill_id of this CreateSkillOrderFrom.
        :type skill_id: str
        """
        self._skill_id = skill_id

    @property
    def amount(self):
        """Gets the amount of this CreateSkillOrderFrom.

        购买个数

        :return: The amount of this CreateSkillOrderFrom.
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this CreateSkillOrderFrom.

        购买个数

        :param amount: The amount of this CreateSkillOrderFrom.
        :type amount: int
        """
        self._amount = amount

    @property
    def commission_flag(self):
        """Gets the commission_flag of this CreateSkillOrderFrom.

        定制技能标识

        :return: The commission_flag of this CreateSkillOrderFrom.
        :rtype: int
        """
        return self._commission_flag

    @commission_flag.setter
    def commission_flag(self, commission_flag):
        """Sets the commission_flag of this CreateSkillOrderFrom.

        定制技能标识

        :param commission_flag: The commission_flag of this CreateSkillOrderFrom.
        :type commission_flag: int
        """
        self._commission_flag = commission_flag

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
        if not isinstance(other, CreateSkillOrderFrom):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
