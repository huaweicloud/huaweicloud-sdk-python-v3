# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateHttpPunishmentRuleRequestBody:

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
        'category': 'str',
        'block_time': 'int'
    }

    attribute_map = {
        'description': 'description',
        'category': 'category',
        'block_time': 'block_time'
    }

    def __init__(self, description=None, category=None, block_time=None):
        r"""CreateHttpPunishmentRuleRequestBody

        The model defined in huaweicloud sdk

        :param description: 规则描述，最长512字符
        :type description: str
        :param category: 拦截类型，可选值为：long_ip_block（长时间IP拦截）、long_cookie_block（长时间Cookie拦截）、long_params_block（长时间Params拦截）、short_ip_block（短时间IP拦截）、short_cookie_block（短时间Cookie拦截）、short_params_block（短时间Params拦截）
        :type category: str
        :param block_time: 拦截时间，如果选择前缀为long的攻击惩罚类别，则block_time时长范围设置为301-1800;选择前缀为short的攻击惩罚类别，则block_time时长范围为0-300之间
        :type block_time: int
        """
        
        

        self._description = None
        self._category = None
        self._block_time = None
        self.discriminator = None

        if description is not None:
            self.description = description
        self.category = category
        self.block_time = block_time

    @property
    def description(self):
        r"""Gets the description of this CreateHttpPunishmentRuleRequestBody.

        规则描述，最长512字符

        :return: The description of this CreateHttpPunishmentRuleRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateHttpPunishmentRuleRequestBody.

        规则描述，最长512字符

        :param description: The description of this CreateHttpPunishmentRuleRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def category(self):
        r"""Gets the category of this CreateHttpPunishmentRuleRequestBody.

        拦截类型，可选值为：long_ip_block（长时间IP拦截）、long_cookie_block（长时间Cookie拦截）、long_params_block（长时间Params拦截）、short_ip_block（短时间IP拦截）、short_cookie_block（短时间Cookie拦截）、short_params_block（短时间Params拦截）

        :return: The category of this CreateHttpPunishmentRuleRequestBody.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this CreateHttpPunishmentRuleRequestBody.

        拦截类型，可选值为：long_ip_block（长时间IP拦截）、long_cookie_block（长时间Cookie拦截）、long_params_block（长时间Params拦截）、short_ip_block（短时间IP拦截）、short_cookie_block（短时间Cookie拦截）、short_params_block（短时间Params拦截）

        :param category: The category of this CreateHttpPunishmentRuleRequestBody.
        :type category: str
        """
        self._category = category

    @property
    def block_time(self):
        r"""Gets the block_time of this CreateHttpPunishmentRuleRequestBody.

        拦截时间，如果选择前缀为long的攻击惩罚类别，则block_time时长范围设置为301-1800;选择前缀为short的攻击惩罚类别，则block_time时长范围为0-300之间

        :return: The block_time of this CreateHttpPunishmentRuleRequestBody.
        :rtype: int
        """
        return self._block_time

    @block_time.setter
    def block_time(self, block_time):
        r"""Sets the block_time of this CreateHttpPunishmentRuleRequestBody.

        拦截时间，如果选择前缀为long的攻击惩罚类别，则block_time时长范围设置为301-1800;选择前缀为short的攻击惩罚类别，则block_time时长范围为0-300之间

        :param block_time: The block_time of this CreateHttpPunishmentRuleRequestBody.
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
        if not isinstance(other, CreateHttpPunishmentRuleRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
