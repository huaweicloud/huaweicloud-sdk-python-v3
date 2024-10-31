# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateHttpPunishmentRuleRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'description': 'str',
        'block_time': 'int'
    }

    attribute_map = {
        'description': 'description',
        'block_time': 'block_time'
    }

    def __init__(self, description=None, block_time=None):
        """UpdateHttpPunishmentRuleRequestBody

        The model defined in huaweicloud sdk

        :param description: 规则描述，最长512字符
        :type description: str
        :param block_time: 拦截时间，如果选择前缀为long的攻击惩罚类别，则block_time时长范围设置为301-1800;选择前缀为short的攻击惩罚类别，则block_time时长范围为1-300之间
        :type block_time: int
        """
        
        

        self._description = None
        self._block_time = None
        self.discriminator = None

        if description is not None:
            self.description = description
        self.block_time = block_time

    @property
    def description(self):
        """Gets the description of this UpdateHttpPunishmentRuleRequestBody.

        规则描述，最长512字符

        :return: The description of this UpdateHttpPunishmentRuleRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateHttpPunishmentRuleRequestBody.

        规则描述，最长512字符

        :param description: The description of this UpdateHttpPunishmentRuleRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def block_time(self):
        """Gets the block_time of this UpdateHttpPunishmentRuleRequestBody.

        拦截时间，如果选择前缀为long的攻击惩罚类别，则block_time时长范围设置为301-1800;选择前缀为short的攻击惩罚类别，则block_time时长范围为1-300之间

        :return: The block_time of this UpdateHttpPunishmentRuleRequestBody.
        :rtype: int
        """
        return self._block_time

    @block_time.setter
    def block_time(self, block_time):
        """Sets the block_time of this UpdateHttpPunishmentRuleRequestBody.

        拦截时间，如果选择前缀为long的攻击惩罚类别，则block_time时长范围设置为301-1800;选择前缀为short的攻击惩罚类别，则block_time时长范围为1-300之间

        :param block_time: The block_time of this UpdateHttpPunishmentRuleRequestBody.
        :type block_time: int
        """
        self._block_time = block_time

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
        if not isinstance(other, UpdateHttpPunishmentRuleRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
