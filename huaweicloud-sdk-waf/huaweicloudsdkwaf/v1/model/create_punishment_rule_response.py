# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreatePunishmentRuleResponse(SdkResponse):

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
        'policyid': 'str',
        'block_time': 'int',
        'category': 'str',
        'description': 'str',
        'timestamp': 'int'
    }

    attribute_map = {
        'id': 'id',
        'policyid': 'policyid',
        'block_time': 'block_time',
        'category': 'category',
        'description': 'description',
        'timestamp': 'timestamp'
    }

    def __init__(self, id=None, policyid=None, block_time=None, category=None, description=None, timestamp=None):
        """CreatePunishmentRuleResponse

        The model defined in huaweicloud sdk

        :param id: 规则id
        :type id: str
        :param policyid: 所属策略id
        :type policyid: str
        :param block_time: 拦截时间
        :type block_time: int
        :param category: 攻击惩罚类别
        :type category: str
        :param description: 规则描述
        :type description: str
        :param timestamp: 创建规则时间戳
        :type timestamp: int
        """
        
        super(CreatePunishmentRuleResponse, self).__init__()

        self._id = None
        self._policyid = None
        self._block_time = None
        self._category = None
        self._description = None
        self._timestamp = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if policyid is not None:
            self.policyid = policyid
        if block_time is not None:
            self.block_time = block_time
        if category is not None:
            self.category = category
        if description is not None:
            self.description = description
        if timestamp is not None:
            self.timestamp = timestamp

    @property
    def id(self):
        """Gets the id of this CreatePunishmentRuleResponse.

        规则id

        :return: The id of this CreatePunishmentRuleResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreatePunishmentRuleResponse.

        规则id

        :param id: The id of this CreatePunishmentRuleResponse.
        :type id: str
        """
        self._id = id

    @property
    def policyid(self):
        """Gets the policyid of this CreatePunishmentRuleResponse.

        所属策略id

        :return: The policyid of this CreatePunishmentRuleResponse.
        :rtype: str
        """
        return self._policyid

    @policyid.setter
    def policyid(self, policyid):
        """Sets the policyid of this CreatePunishmentRuleResponse.

        所属策略id

        :param policyid: The policyid of this CreatePunishmentRuleResponse.
        :type policyid: str
        """
        self._policyid = policyid

    @property
    def block_time(self):
        """Gets the block_time of this CreatePunishmentRuleResponse.

        拦截时间

        :return: The block_time of this CreatePunishmentRuleResponse.
        :rtype: int
        """
        return self._block_time

    @block_time.setter
    def block_time(self, block_time):
        """Sets the block_time of this CreatePunishmentRuleResponse.

        拦截时间

        :param block_time: The block_time of this CreatePunishmentRuleResponse.
        :type block_time: int
        """
        self._block_time = block_time

    @property
    def category(self):
        """Gets the category of this CreatePunishmentRuleResponse.

        攻击惩罚类别

        :return: The category of this CreatePunishmentRuleResponse.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this CreatePunishmentRuleResponse.

        攻击惩罚类别

        :param category: The category of this CreatePunishmentRuleResponse.
        :type category: str
        """
        self._category = category

    @property
    def description(self):
        """Gets the description of this CreatePunishmentRuleResponse.

        规则描述

        :return: The description of this CreatePunishmentRuleResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreatePunishmentRuleResponse.

        规则描述

        :param description: The description of this CreatePunishmentRuleResponse.
        :type description: str
        """
        self._description = description

    @property
    def timestamp(self):
        """Gets the timestamp of this CreatePunishmentRuleResponse.

        创建规则时间戳

        :return: The timestamp of this CreatePunishmentRuleResponse.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this CreatePunishmentRuleResponse.

        创建规则时间戳

        :param timestamp: The timestamp of this CreatePunishmentRuleResponse.
        :type timestamp: int
        """
        self._timestamp = timestamp

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
        if not isinstance(other, CreatePunishmentRuleResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
