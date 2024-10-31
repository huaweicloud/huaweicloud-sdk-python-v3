# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateHttpPunishmentRuleResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'policy_id': 'str',
        'timestamp': 'int',
        'description': 'str',
        'category': 'str',
        'block_time': 'int'
    }

    attribute_map = {
        'id': 'id',
        'policy_id': 'policy_id',
        'timestamp': 'timestamp',
        'description': 'description',
        'category': 'category',
        'block_time': 'block_time'
    }

    def __init__(self, id=None, policy_id=None, timestamp=None, description=None, category=None, block_time=None):
        """UpdateHttpPunishmentRuleResponse

        The model defined in huaweicloud sdk

        :param id: 规则id
        :type id: str
        :param policy_id: 规则所在策略id
        :type policy_id: str
        :param timestamp: 创建规则时间戳
        :type timestamp: int
        :param description: 规则描述
        :type description: str
        :param category: 拦截类型，可选值为：long_ip_block（长时间IP拦截）、long_cookie_block（长时间Cookie拦截）、long_params_block（长时间Params拦截）、short_ip_block（短时间IP拦截）、short_cookie_block（短时间Cookie拦截）、short_params_block（短时间Params拦截）
        :type category: str
        :param block_time: 拦截时长
        :type block_time: int
        """
        
        super(UpdateHttpPunishmentRuleResponse, self).__init__()

        self._id = None
        self._policy_id = None
        self._timestamp = None
        self._description = None
        self._category = None
        self._block_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if policy_id is not None:
            self.policy_id = policy_id
        if timestamp is not None:
            self.timestamp = timestamp
        if description is not None:
            self.description = description
        if category is not None:
            self.category = category
        if block_time is not None:
            self.block_time = block_time

    @property
    def id(self):
        """Gets the id of this UpdateHttpPunishmentRuleResponse.

        规则id

        :return: The id of this UpdateHttpPunishmentRuleResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UpdateHttpPunishmentRuleResponse.

        规则id

        :param id: The id of this UpdateHttpPunishmentRuleResponse.
        :type id: str
        """
        self._id = id

    @property
    def policy_id(self):
        """Gets the policy_id of this UpdateHttpPunishmentRuleResponse.

        规则所在策略id

        :return: The policy_id of this UpdateHttpPunishmentRuleResponse.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        """Sets the policy_id of this UpdateHttpPunishmentRuleResponse.

        规则所在策略id

        :param policy_id: The policy_id of this UpdateHttpPunishmentRuleResponse.
        :type policy_id: str
        """
        self._policy_id = policy_id

    @property
    def timestamp(self):
        """Gets the timestamp of this UpdateHttpPunishmentRuleResponse.

        创建规则时间戳

        :return: The timestamp of this UpdateHttpPunishmentRuleResponse.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this UpdateHttpPunishmentRuleResponse.

        创建规则时间戳

        :param timestamp: The timestamp of this UpdateHttpPunishmentRuleResponse.
        :type timestamp: int
        """
        self._timestamp = timestamp

    @property
    def description(self):
        """Gets the description of this UpdateHttpPunishmentRuleResponse.

        规则描述

        :return: The description of this UpdateHttpPunishmentRuleResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateHttpPunishmentRuleResponse.

        规则描述

        :param description: The description of this UpdateHttpPunishmentRuleResponse.
        :type description: str
        """
        self._description = description

    @property
    def category(self):
        """Gets the category of this UpdateHttpPunishmentRuleResponse.

        拦截类型，可选值为：long_ip_block（长时间IP拦截）、long_cookie_block（长时间Cookie拦截）、long_params_block（长时间Params拦截）、short_ip_block（短时间IP拦截）、short_cookie_block（短时间Cookie拦截）、short_params_block（短时间Params拦截）

        :return: The category of this UpdateHttpPunishmentRuleResponse.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this UpdateHttpPunishmentRuleResponse.

        拦截类型，可选值为：long_ip_block（长时间IP拦截）、long_cookie_block（长时间Cookie拦截）、long_params_block（长时间Params拦截）、short_ip_block（短时间IP拦截）、short_cookie_block（短时间Cookie拦截）、short_params_block（短时间Params拦截）

        :param category: The category of this UpdateHttpPunishmentRuleResponse.
        :type category: str
        """
        self._category = category

    @property
    def block_time(self):
        """Gets the block_time of this UpdateHttpPunishmentRuleResponse.

        拦截时长

        :return: The block_time of this UpdateHttpPunishmentRuleResponse.
        :rtype: int
        """
        return self._block_time

    @block_time.setter
    def block_time(self, block_time):
        """Sets the block_time of this UpdateHttpPunishmentRuleResponse.

        拦截时长

        :param block_time: The block_time of this UpdateHttpPunishmentRuleResponse.
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
        if not isinstance(other, UpdateHttpPunishmentRuleResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
