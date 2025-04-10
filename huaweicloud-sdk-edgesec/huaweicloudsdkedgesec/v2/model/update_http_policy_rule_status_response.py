# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateHttpPolicyRuleStatusResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'category': 'str',
        'description': 'str',
        'id': 'str',
        'policyid': 'str',
        'status': 'int',
        'timestamp': 'float'
    }

    attribute_map = {
        'category': 'category',
        'description': 'description',
        'id': 'id',
        'policyid': 'policyid',
        'status': 'status',
        'timestamp': 'timestamp'
    }

    def __init__(self, category=None, description=None, id=None, policyid=None, status=None, timestamp=None):
        r"""UpdateHttpPolicyRuleStatusResponse

        The model defined in huaweicloud sdk

        :param category: 规则类别
        :type category: str
        :param description: 描述
        :type description: str
        :param id: 规则id
        :type id: str
        :param policyid: 策略id
        :type policyid: str
        :param status: 规则状态
        :type status: int
        :param timestamp: 规则添加时间
        :type timestamp: float
        """
        
        super(UpdateHttpPolicyRuleStatusResponse, self).__init__()

        self._category = None
        self._description = None
        self._id = None
        self._policyid = None
        self._status = None
        self._timestamp = None
        self.discriminator = None

        if category is not None:
            self.category = category
        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        if policyid is not None:
            self.policyid = policyid
        if status is not None:
            self.status = status
        if timestamp is not None:
            self.timestamp = timestamp

    @property
    def category(self):
        r"""Gets the category of this UpdateHttpPolicyRuleStatusResponse.

        规则类别

        :return: The category of this UpdateHttpPolicyRuleStatusResponse.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this UpdateHttpPolicyRuleStatusResponse.

        规则类别

        :param category: The category of this UpdateHttpPolicyRuleStatusResponse.
        :type category: str
        """
        self._category = category

    @property
    def description(self):
        r"""Gets the description of this UpdateHttpPolicyRuleStatusResponse.

        描述

        :return: The description of this UpdateHttpPolicyRuleStatusResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateHttpPolicyRuleStatusResponse.

        描述

        :param description: The description of this UpdateHttpPolicyRuleStatusResponse.
        :type description: str
        """
        self._description = description

    @property
    def id(self):
        r"""Gets the id of this UpdateHttpPolicyRuleStatusResponse.

        规则id

        :return: The id of this UpdateHttpPolicyRuleStatusResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this UpdateHttpPolicyRuleStatusResponse.

        规则id

        :param id: The id of this UpdateHttpPolicyRuleStatusResponse.
        :type id: str
        """
        self._id = id

    @property
    def policyid(self):
        r"""Gets the policyid of this UpdateHttpPolicyRuleStatusResponse.

        策略id

        :return: The policyid of this UpdateHttpPolicyRuleStatusResponse.
        :rtype: str
        """
        return self._policyid

    @policyid.setter
    def policyid(self, policyid):
        r"""Sets the policyid of this UpdateHttpPolicyRuleStatusResponse.

        策略id

        :param policyid: The policyid of this UpdateHttpPolicyRuleStatusResponse.
        :type policyid: str
        """
        self._policyid = policyid

    @property
    def status(self):
        r"""Gets the status of this UpdateHttpPolicyRuleStatusResponse.

        规则状态

        :return: The status of this UpdateHttpPolicyRuleStatusResponse.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this UpdateHttpPolicyRuleStatusResponse.

        规则状态

        :param status: The status of this UpdateHttpPolicyRuleStatusResponse.
        :type status: int
        """
        self._status = status

    @property
    def timestamp(self):
        r"""Gets the timestamp of this UpdateHttpPolicyRuleStatusResponse.

        规则添加时间

        :return: The timestamp of this UpdateHttpPolicyRuleStatusResponse.
        :rtype: float
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        r"""Sets the timestamp of this UpdateHttpPolicyRuleStatusResponse.

        规则添加时间

        :param timestamp: The timestamp of this UpdateHttpPolicyRuleStatusResponse.
        :type timestamp: float
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
        if not isinstance(other, UpdateHttpPolicyRuleStatusResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
