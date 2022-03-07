# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IngnoreItem:


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
        'timestamp': 'int',
        'description': 'str',
        'status': 'int',
        'url': 'str',
        'rule': 'str',
        'domain': 'list[str]',
        'url_logic': 'str',
        'advanced': 'Advance'
    }

    attribute_map = {
        'id': 'id',
        'policyid': 'policyid',
        'timestamp': 'timestamp',
        'description': 'description',
        'status': 'status',
        'url': 'url',
        'rule': 'rule',
        'domain': 'domain',
        'url_logic': 'url_logic',
        'advanced': 'advanced'
    }

    def __init__(self, id=None, policyid=None, timestamp=None, description=None, status=None, url=None, rule=None, domain=None, url_logic=None, advanced=None):
        """IngnoreItem - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._policyid = None
        self._timestamp = None
        self._description = None
        self._status = None
        self._url = None
        self._rule = None
        self._domain = None
        self._url_logic = None
        self._advanced = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if policyid is not None:
            self.policyid = policyid
        if timestamp is not None:
            self.timestamp = timestamp
        if description is not None:
            self.description = description
        if status is not None:
            self.status = status
        if url is not None:
            self.url = url
        if rule is not None:
            self.rule = rule
        if domain is not None:
            self.domain = domain
        if url_logic is not None:
            self.url_logic = url_logic
        if advanced is not None:
            self.advanced = advanced

    @property
    def id(self):
        """Gets the id of this IngnoreItem.

        规则id

        :return: The id of this IngnoreItem.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IngnoreItem.

        规则id

        :param id: The id of this IngnoreItem.
        :type: str
        """
        self._id = id

    @property
    def policyid(self):
        """Gets the policyid of this IngnoreItem.

        策略id

        :return: The policyid of this IngnoreItem.
        :rtype: str
        """
        return self._policyid

    @policyid.setter
    def policyid(self, policyid):
        """Sets the policyid of this IngnoreItem.

        策略id

        :param policyid: The policyid of this IngnoreItem.
        :type: str
        """
        self._policyid = policyid

    @property
    def timestamp(self):
        """Gets the timestamp of this IngnoreItem.

        创建规则的时间戳

        :return: The timestamp of this IngnoreItem.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this IngnoreItem.

        创建规则的时间戳

        :param timestamp: The timestamp of this IngnoreItem.
        :type: int
        """
        self._timestamp = timestamp

    @property
    def description(self):
        """Gets the description of this IngnoreItem.

        规则描述

        :return: The description of this IngnoreItem.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this IngnoreItem.

        规则描述

        :param description: The description of this IngnoreItem.
        :type: str
        """
        self._description = description

    @property
    def status(self):
        """Gets the status of this IngnoreItem.

        规则状态，0：关闭，1：开启

        :return: The status of this IngnoreItem.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this IngnoreItem.

        规则状态，0：关闭，1：开启

        :param status: The status of this IngnoreItem.
        :type: int
        """
        self._status = status

    @property
    def url(self):
        """Gets the url of this IngnoreItem.

        防篡改规则防护的url，需要填写标准的url格式，例如/admin/xxx或者/admin/*,以\"*\"号结尾代表路径前缀

        :return: The url of this IngnoreItem.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this IngnoreItem.

        防篡改规则防护的url，需要填写标准的url格式，例如/admin/xxx或者/admin/*,以\"*\"号结尾代表路径前缀

        :param url: The url of this IngnoreItem.
        :type: str
        """
        self._url = url

    @property
    def rule(self):
        """Gets the rule of this IngnoreItem.

        屏蔽的规则，可以是命中规则id，对应防护事件的命中规则；或者所有规则（所有规则：all）；或者攻击类型枚举（XSS攻击：xss，sqli，命令注入：cmdi，恶意爬虫：robot，本地文件包含：lfi，远程文件包含：rfi，网站木马：webshell，cc攻击：cc，精准防护：custom_custom，IP黑白名单：custom_whiteblackip，地理位置访问控制：custom_geoip，防篡改：antitamper，反爬虫：anticrawler，网站信息防泄漏：leakage，非法请求：illegal，其它类型攻击：vuln）

        :return: The rule of this IngnoreItem.
        :rtype: str
        """
        return self._rule

    @rule.setter
    def rule(self, rule):
        """Sets the rule of this IngnoreItem.

        屏蔽的规则，可以是命中规则id，对应防护事件的命中规则；或者所有规则（所有规则：all）；或者攻击类型枚举（XSS攻击：xss，sqli，命令注入：cmdi，恶意爬虫：robot，本地文件包含：lfi，远程文件包含：rfi，网站木马：webshell，cc攻击：cc，精准防护：custom_custom，IP黑白名单：custom_whiteblackip，地理位置访问控制：custom_geoip，防篡改：antitamper，反爬虫：anticrawler，网站信息防泄漏：leakage，非法请求：illegal，其它类型攻击：vuln）

        :param rule: The rule of this IngnoreItem.
        :type: str
        """
        self._rule = rule

    @property
    def domain(self):
        """Gets the domain of this IngnoreItem.

        防护的域名

        :return: The domain of this IngnoreItem.
        :rtype: list[str]
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this IngnoreItem.

        防护的域名

        :param domain: The domain of this IngnoreItem.
        :type: list[str]
        """
        self._domain = domain

    @property
    def url_logic(self):
        """Gets the url_logic of this IngnoreItem.

        url匹配逻辑（prefix：前缀匹配，equal：全等）

        :return: The url_logic of this IngnoreItem.
        :rtype: str
        """
        return self._url_logic

    @url_logic.setter
    def url_logic(self, url_logic):
        """Sets the url_logic of this IngnoreItem.

        url匹配逻辑（prefix：前缀匹配，equal：全等）

        :param url_logic: The url_logic of this IngnoreItem.
        :type: str
        """
        self._url_logic = url_logic

    @property
    def advanced(self):
        """Gets the advanced of this IngnoreItem.


        :return: The advanced of this IngnoreItem.
        :rtype: Advance
        """
        return self._advanced

    @advanced.setter
    def advanced(self, advanced):
        """Sets the advanced of this IngnoreItem.


        :param advanced: The advanced of this IngnoreItem.
        :type: Advance
        """
        self._advanced = advanced

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
        if not isinstance(other, IngnoreItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
