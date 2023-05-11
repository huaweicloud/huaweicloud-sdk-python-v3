# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAntitamperRuleResponse(SdkResponse):

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
        'hostname': 'str',
        'url': 'str',
        'description': 'str',
        'status': 'int',
        'timestamp': 'int'
    }

    attribute_map = {
        'id': 'id',
        'policyid': 'policyid',
        'hostname': 'hostname',
        'url': 'url',
        'description': 'description',
        'status': 'status',
        'timestamp': 'timestamp'
    }

    def __init__(self, id=None, policyid=None, hostname=None, url=None, description=None, status=None, timestamp=None):
        """ShowAntitamperRuleResponse

        The model defined in huaweicloud sdk

        :param id: 规则id
        :type id: str
        :param policyid: 策略id
        :type policyid: str
        :param hostname: 防篡改的域名
        :type hostname: str
        :param url: 防篡改的url，
        :type url: str
        :param description: 创建规则的时间戳
        :type description: str
        :param status: 规则状态，0：关闭，1：开启
        :type status: int
        :param timestamp: 创建规则的时间，格式为13位毫秒时间戳
        :type timestamp: int
        """
        
        super(ShowAntitamperRuleResponse, self).__init__()

        self._id = None
        self._policyid = None
        self._hostname = None
        self._url = None
        self._description = None
        self._status = None
        self._timestamp = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if policyid is not None:
            self.policyid = policyid
        if hostname is not None:
            self.hostname = hostname
        if url is not None:
            self.url = url
        if description is not None:
            self.description = description
        if status is not None:
            self.status = status
        if timestamp is not None:
            self.timestamp = timestamp

    @property
    def id(self):
        """Gets the id of this ShowAntitamperRuleResponse.

        规则id

        :return: The id of this ShowAntitamperRuleResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowAntitamperRuleResponse.

        规则id

        :param id: The id of this ShowAntitamperRuleResponse.
        :type id: str
        """
        self._id = id

    @property
    def policyid(self):
        """Gets the policyid of this ShowAntitamperRuleResponse.

        策略id

        :return: The policyid of this ShowAntitamperRuleResponse.
        :rtype: str
        """
        return self._policyid

    @policyid.setter
    def policyid(self, policyid):
        """Sets the policyid of this ShowAntitamperRuleResponse.

        策略id

        :param policyid: The policyid of this ShowAntitamperRuleResponse.
        :type policyid: str
        """
        self._policyid = policyid

    @property
    def hostname(self):
        """Gets the hostname of this ShowAntitamperRuleResponse.

        防篡改的域名

        :return: The hostname of this ShowAntitamperRuleResponse.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this ShowAntitamperRuleResponse.

        防篡改的域名

        :param hostname: The hostname of this ShowAntitamperRuleResponse.
        :type hostname: str
        """
        self._hostname = hostname

    @property
    def url(self):
        """Gets the url of this ShowAntitamperRuleResponse.

        防篡改的url，

        :return: The url of this ShowAntitamperRuleResponse.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this ShowAntitamperRuleResponse.

        防篡改的url，

        :param url: The url of this ShowAntitamperRuleResponse.
        :type url: str
        """
        self._url = url

    @property
    def description(self):
        """Gets the description of this ShowAntitamperRuleResponse.

        创建规则的时间戳

        :return: The description of this ShowAntitamperRuleResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ShowAntitamperRuleResponse.

        创建规则的时间戳

        :param description: The description of this ShowAntitamperRuleResponse.
        :type description: str
        """
        self._description = description

    @property
    def status(self):
        """Gets the status of this ShowAntitamperRuleResponse.

        规则状态，0：关闭，1：开启

        :return: The status of this ShowAntitamperRuleResponse.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowAntitamperRuleResponse.

        规则状态，0：关闭，1：开启

        :param status: The status of this ShowAntitamperRuleResponse.
        :type status: int
        """
        self._status = status

    @property
    def timestamp(self):
        """Gets the timestamp of this ShowAntitamperRuleResponse.

        创建规则的时间，格式为13位毫秒时间戳

        :return: The timestamp of this ShowAntitamperRuleResponse.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this ShowAntitamperRuleResponse.

        创建规则的时间，格式为13位毫秒时间戳

        :param timestamp: The timestamp of this ShowAntitamperRuleResponse.
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
        if not isinstance(other, ShowAntitamperRuleResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
