# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAntiTamperRuleResponse(SdkResponse):

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
        'status': 'int'
    }

    attribute_map = {
        'id': 'id',
        'policyid': 'policyid',
        'hostname': 'hostname',
        'url': 'url',
        'description': 'description',
        'status': 'status'
    }

    def __init__(self, id=None, policyid=None, hostname=None, url=None, description=None, status=None):
        r"""CreateAntiTamperRuleResponse

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
        """
        
        super(CreateAntiTamperRuleResponse, self).__init__()

        self._id = None
        self._policyid = None
        self._hostname = None
        self._url = None
        self._description = None
        self._status = None
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

    @property
    def id(self):
        r"""Gets the id of this CreateAntiTamperRuleResponse.

        规则id

        :return: The id of this CreateAntiTamperRuleResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CreateAntiTamperRuleResponse.

        规则id

        :param id: The id of this CreateAntiTamperRuleResponse.
        :type id: str
        """
        self._id = id

    @property
    def policyid(self):
        r"""Gets the policyid of this CreateAntiTamperRuleResponse.

        策略id

        :return: The policyid of this CreateAntiTamperRuleResponse.
        :rtype: str
        """
        return self._policyid

    @policyid.setter
    def policyid(self, policyid):
        r"""Sets the policyid of this CreateAntiTamperRuleResponse.

        策略id

        :param policyid: The policyid of this CreateAntiTamperRuleResponse.
        :type policyid: str
        """
        self._policyid = policyid

    @property
    def hostname(self):
        r"""Gets the hostname of this CreateAntiTamperRuleResponse.

        防篡改的域名

        :return: The hostname of this CreateAntiTamperRuleResponse.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        r"""Sets the hostname of this CreateAntiTamperRuleResponse.

        防篡改的域名

        :param hostname: The hostname of this CreateAntiTamperRuleResponse.
        :type hostname: str
        """
        self._hostname = hostname

    @property
    def url(self):
        r"""Gets the url of this CreateAntiTamperRuleResponse.

        防篡改的url，

        :return: The url of this CreateAntiTamperRuleResponse.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this CreateAntiTamperRuleResponse.

        防篡改的url，

        :param url: The url of this CreateAntiTamperRuleResponse.
        :type url: str
        """
        self._url = url

    @property
    def description(self):
        r"""Gets the description of this CreateAntiTamperRuleResponse.

        创建规则的时间戳

        :return: The description of this CreateAntiTamperRuleResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateAntiTamperRuleResponse.

        创建规则的时间戳

        :param description: The description of this CreateAntiTamperRuleResponse.
        :type description: str
        """
        self._description = description

    @property
    def status(self):
        r"""Gets the status of this CreateAntiTamperRuleResponse.

        规则状态，0：关闭，1：开启

        :return: The status of this CreateAntiTamperRuleResponse.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CreateAntiTamperRuleResponse.

        规则状态，0：关闭，1：开启

        :param status: The status of this CreateAntiTamperRuleResponse.
        :type status: int
        """
        self._status = status

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
        if not isinstance(other, CreateAntiTamperRuleResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
