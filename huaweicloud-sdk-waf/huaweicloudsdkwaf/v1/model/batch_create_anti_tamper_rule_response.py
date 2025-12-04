# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchCreateAntiTamperRuleResponse(SdkResponse):

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
        r"""BatchCreateAntiTamperRuleResponse

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
        :param status: **参数解释：** 规则状态标识，用于指定规则的启用或关闭状态 **约束限制：** 不涉及 **取值范围：**  - 0：关闭  - 1：开启 **默认取值：** 不涉及
        :type status: int
        """
        
        super().__init__()

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
        r"""Gets the id of this BatchCreateAntiTamperRuleResponse.

        规则id

        :return: The id of this BatchCreateAntiTamperRuleResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this BatchCreateAntiTamperRuleResponse.

        规则id

        :param id: The id of this BatchCreateAntiTamperRuleResponse.
        :type id: str
        """
        self._id = id

    @property
    def policyid(self):
        r"""Gets the policyid of this BatchCreateAntiTamperRuleResponse.

        策略id

        :return: The policyid of this BatchCreateAntiTamperRuleResponse.
        :rtype: str
        """
        return self._policyid

    @policyid.setter
    def policyid(self, policyid):
        r"""Sets the policyid of this BatchCreateAntiTamperRuleResponse.

        策略id

        :param policyid: The policyid of this BatchCreateAntiTamperRuleResponse.
        :type policyid: str
        """
        self._policyid = policyid

    @property
    def hostname(self):
        r"""Gets the hostname of this BatchCreateAntiTamperRuleResponse.

        防篡改的域名

        :return: The hostname of this BatchCreateAntiTamperRuleResponse.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        r"""Sets the hostname of this BatchCreateAntiTamperRuleResponse.

        防篡改的域名

        :param hostname: The hostname of this BatchCreateAntiTamperRuleResponse.
        :type hostname: str
        """
        self._hostname = hostname

    @property
    def url(self):
        r"""Gets the url of this BatchCreateAntiTamperRuleResponse.

        防篡改的url，

        :return: The url of this BatchCreateAntiTamperRuleResponse.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this BatchCreateAntiTamperRuleResponse.

        防篡改的url，

        :param url: The url of this BatchCreateAntiTamperRuleResponse.
        :type url: str
        """
        self._url = url

    @property
    def description(self):
        r"""Gets the description of this BatchCreateAntiTamperRuleResponse.

        创建规则的时间戳

        :return: The description of this BatchCreateAntiTamperRuleResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this BatchCreateAntiTamperRuleResponse.

        创建规则的时间戳

        :param description: The description of this BatchCreateAntiTamperRuleResponse.
        :type description: str
        """
        self._description = description

    @property
    def status(self):
        r"""Gets the status of this BatchCreateAntiTamperRuleResponse.

        **参数解释：** 规则状态标识，用于指定规则的启用或关闭状态 **约束限制：** 不涉及 **取值范围：**  - 0：关闭  - 1：开启 **默认取值：** 不涉及

        :return: The status of this BatchCreateAntiTamperRuleResponse.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this BatchCreateAntiTamperRuleResponse.

        **参数解释：** 规则状态标识，用于指定规则的启用或关闭状态 **约束限制：** 不涉及 **取值范围：**  - 0：关闭  - 1：开启 **默认取值：** 不涉及

        :param status: The status of this BatchCreateAntiTamperRuleResponse.
        :type status: int
        """
        self._status = status

    def to_dict(self):
        import warnings
        warnings.warn("BatchCreateAntiTamperRuleResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BatchCreateAntiTamperRuleResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
