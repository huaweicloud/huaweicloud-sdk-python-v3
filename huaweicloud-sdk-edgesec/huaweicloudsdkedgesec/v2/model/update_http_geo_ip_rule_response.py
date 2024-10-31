# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateHttpGeoIpRuleResponse(SdkResponse):

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
        'name': 'str',
        'policyid': 'str',
        'policy_name': 'str',
        'timestamp': 'int',
        'description': 'str',
        'status': 'int',
        'geo_ip': 'str',
        'geo_tag_list': 'list[str]',
        'white': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'policyid': 'policyid',
        'policy_name': 'policy_name',
        'timestamp': 'timestamp',
        'description': 'description',
        'status': 'status',
        'geo_ip': 'geo_ip',
        'geo_tag_list': 'geo_tag_list',
        'white': 'white'
    }

    def __init__(self, id=None, name=None, policyid=None, policy_name=None, timestamp=None, description=None, status=None, geo_ip=None, geo_tag_list=None, white=None):
        """UpdateHttpGeoIpRuleResponse

        The model defined in huaweicloud sdk

        :param id: 规则id
        :type id: str
        :param name: 规则名称
        :type name: str
        :param policyid: 规则所在策略id
        :type policyid: str
        :param policy_name: 规则所在策略名称
        :type policy_name: str
        :param timestamp: 创建规则时间戳
        :type timestamp: int
        :param description: 规则描述
        :type description: str
        :param status: 规则开关状态
        :type status: int
        :param geo_ip: 地理位置
        :type geo_ip: str
        :param geo_tag_list: 地理位置列表
        :type geo_tag_list: list[str]
        :param white: 拦截/放行/仅记录
        :type white: int
        """
        
        super(UpdateHttpGeoIpRuleResponse, self).__init__()

        self._id = None
        self._name = None
        self._policyid = None
        self._policy_name = None
        self._timestamp = None
        self._description = None
        self._status = None
        self._geo_ip = None
        self._geo_tag_list = None
        self._white = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if policyid is not None:
            self.policyid = policyid
        if policy_name is not None:
            self.policy_name = policy_name
        if timestamp is not None:
            self.timestamp = timestamp
        if description is not None:
            self.description = description
        if status is not None:
            self.status = status
        if geo_ip is not None:
            self.geo_ip = geo_ip
        if geo_tag_list is not None:
            self.geo_tag_list = geo_tag_list
        if white is not None:
            self.white = white

    @property
    def id(self):
        """Gets the id of this UpdateHttpGeoIpRuleResponse.

        规则id

        :return: The id of this UpdateHttpGeoIpRuleResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UpdateHttpGeoIpRuleResponse.

        规则id

        :param id: The id of this UpdateHttpGeoIpRuleResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this UpdateHttpGeoIpRuleResponse.

        规则名称

        :return: The name of this UpdateHttpGeoIpRuleResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateHttpGeoIpRuleResponse.

        规则名称

        :param name: The name of this UpdateHttpGeoIpRuleResponse.
        :type name: str
        """
        self._name = name

    @property
    def policyid(self):
        """Gets the policyid of this UpdateHttpGeoIpRuleResponse.

        规则所在策略id

        :return: The policyid of this UpdateHttpGeoIpRuleResponse.
        :rtype: str
        """
        return self._policyid

    @policyid.setter
    def policyid(self, policyid):
        """Sets the policyid of this UpdateHttpGeoIpRuleResponse.

        规则所在策略id

        :param policyid: The policyid of this UpdateHttpGeoIpRuleResponse.
        :type policyid: str
        """
        self._policyid = policyid

    @property
    def policy_name(self):
        """Gets the policy_name of this UpdateHttpGeoIpRuleResponse.

        规则所在策略名称

        :return: The policy_name of this UpdateHttpGeoIpRuleResponse.
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        """Sets the policy_name of this UpdateHttpGeoIpRuleResponse.

        规则所在策略名称

        :param policy_name: The policy_name of this UpdateHttpGeoIpRuleResponse.
        :type policy_name: str
        """
        self._policy_name = policy_name

    @property
    def timestamp(self):
        """Gets the timestamp of this UpdateHttpGeoIpRuleResponse.

        创建规则时间戳

        :return: The timestamp of this UpdateHttpGeoIpRuleResponse.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this UpdateHttpGeoIpRuleResponse.

        创建规则时间戳

        :param timestamp: The timestamp of this UpdateHttpGeoIpRuleResponse.
        :type timestamp: int
        """
        self._timestamp = timestamp

    @property
    def description(self):
        """Gets the description of this UpdateHttpGeoIpRuleResponse.

        规则描述

        :return: The description of this UpdateHttpGeoIpRuleResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateHttpGeoIpRuleResponse.

        规则描述

        :param description: The description of this UpdateHttpGeoIpRuleResponse.
        :type description: str
        """
        self._description = description

    @property
    def status(self):
        """Gets the status of this UpdateHttpGeoIpRuleResponse.

        规则开关状态

        :return: The status of this UpdateHttpGeoIpRuleResponse.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UpdateHttpGeoIpRuleResponse.

        规则开关状态

        :param status: The status of this UpdateHttpGeoIpRuleResponse.
        :type status: int
        """
        self._status = status

    @property
    def geo_ip(self):
        """Gets the geo_ip of this UpdateHttpGeoIpRuleResponse.

        地理位置

        :return: The geo_ip of this UpdateHttpGeoIpRuleResponse.
        :rtype: str
        """
        return self._geo_ip

    @geo_ip.setter
    def geo_ip(self, geo_ip):
        """Sets the geo_ip of this UpdateHttpGeoIpRuleResponse.

        地理位置

        :param geo_ip: The geo_ip of this UpdateHttpGeoIpRuleResponse.
        :type geo_ip: str
        """
        self._geo_ip = geo_ip

    @property
    def geo_tag_list(self):
        """Gets the geo_tag_list of this UpdateHttpGeoIpRuleResponse.

        地理位置列表

        :return: The geo_tag_list of this UpdateHttpGeoIpRuleResponse.
        :rtype: list[str]
        """
        return self._geo_tag_list

    @geo_tag_list.setter
    def geo_tag_list(self, geo_tag_list):
        """Sets the geo_tag_list of this UpdateHttpGeoIpRuleResponse.

        地理位置列表

        :param geo_tag_list: The geo_tag_list of this UpdateHttpGeoIpRuleResponse.
        :type geo_tag_list: list[str]
        """
        self._geo_tag_list = geo_tag_list

    @property
    def white(self):
        """Gets the white of this UpdateHttpGeoIpRuleResponse.

        拦截/放行/仅记录

        :return: The white of this UpdateHttpGeoIpRuleResponse.
        :rtype: int
        """
        return self._white

    @white.setter
    def white(self, white):
        """Sets the white of this UpdateHttpGeoIpRuleResponse.

        拦截/放行/仅记录

        :param white: The white of this UpdateHttpGeoIpRuleResponse.
        :type white: int
        """
        self._white = white

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
        if not isinstance(other, UpdateHttpGeoIpRuleResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
