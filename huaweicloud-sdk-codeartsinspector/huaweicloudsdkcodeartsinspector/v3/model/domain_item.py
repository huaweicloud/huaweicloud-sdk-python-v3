# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DomainItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'high': 'int',
        'middle': 'int',
        'low': 'int',
        'hint': 'int',
        'domain_id': 'str',
        'top_level_domain_id': 'str',
        'domain_name': 'str',
        'alias': 'str',
        'create_time': 'str',
        'auth_status': 'str',
        'protocol_type': 'str'
    }

    attribute_map = {
        'high': 'high',
        'middle': 'middle',
        'low': 'low',
        'hint': 'hint',
        'domain_id': 'domain_id',
        'top_level_domain_id': 'top_level_domain_id',
        'domain_name': 'domain_name',
        'alias': 'alias',
        'create_time': 'create_time',
        'auth_status': 'auth_status',
        'protocol_type': 'protocol_type'
    }

    def __init__(self, high=None, middle=None, low=None, hint=None, domain_id=None, top_level_domain_id=None, domain_name=None, alias=None, create_time=None, auth_status=None, protocol_type=None):
        """DomainItem

        The model defined in huaweicloud sdk

        :param high: 高危漏洞数
        :type high: int
        :param middle: 中危漏洞数
        :type middle: int
        :param low: 低危漏洞数
        :type low: int
        :param hint: 提示危漏洞数
        :type hint: int
        :param domain_id: 网站域名ID
        :type domain_id: str
        :param top_level_domain_id: 一级域名ID
        :type top_level_domain_id: str
        :param domain_name: 网站域名
        :type domain_name: str
        :param alias: 网站域名的别名
        :type alias: str
        :param create_time: 创建网站域名资产的时间
        :type create_time: str
        :param auth_status: 网站域名的认证状态:   * unauth - 未认证   * auth - 已认证   * invalid - 认证文件无效   * manual - 人工认证   * skip - 免认证 
        :type auth_status: str
        :param protocol_type: 协议类型:   * http:// - HTTP   * https:// - HTTPS 
        :type protocol_type: str
        """
        
        

        self._high = None
        self._middle = None
        self._low = None
        self._hint = None
        self._domain_id = None
        self._top_level_domain_id = None
        self._domain_name = None
        self._alias = None
        self._create_time = None
        self._auth_status = None
        self._protocol_type = None
        self.discriminator = None

        if high is not None:
            self.high = high
        if middle is not None:
            self.middle = middle
        if low is not None:
            self.low = low
        if hint is not None:
            self.hint = hint
        if domain_id is not None:
            self.domain_id = domain_id
        if top_level_domain_id is not None:
            self.top_level_domain_id = top_level_domain_id
        if domain_name is not None:
            self.domain_name = domain_name
        if alias is not None:
            self.alias = alias
        if create_time is not None:
            self.create_time = create_time
        if auth_status is not None:
            self.auth_status = auth_status
        if protocol_type is not None:
            self.protocol_type = protocol_type

    @property
    def high(self):
        """Gets the high of this DomainItem.

        高危漏洞数

        :return: The high of this DomainItem.
        :rtype: int
        """
        return self._high

    @high.setter
    def high(self, high):
        """Sets the high of this DomainItem.

        高危漏洞数

        :param high: The high of this DomainItem.
        :type high: int
        """
        self._high = high

    @property
    def middle(self):
        """Gets the middle of this DomainItem.

        中危漏洞数

        :return: The middle of this DomainItem.
        :rtype: int
        """
        return self._middle

    @middle.setter
    def middle(self, middle):
        """Sets the middle of this DomainItem.

        中危漏洞数

        :param middle: The middle of this DomainItem.
        :type middle: int
        """
        self._middle = middle

    @property
    def low(self):
        """Gets the low of this DomainItem.

        低危漏洞数

        :return: The low of this DomainItem.
        :rtype: int
        """
        return self._low

    @low.setter
    def low(self, low):
        """Sets the low of this DomainItem.

        低危漏洞数

        :param low: The low of this DomainItem.
        :type low: int
        """
        self._low = low

    @property
    def hint(self):
        """Gets the hint of this DomainItem.

        提示危漏洞数

        :return: The hint of this DomainItem.
        :rtype: int
        """
        return self._hint

    @hint.setter
    def hint(self, hint):
        """Sets the hint of this DomainItem.

        提示危漏洞数

        :param hint: The hint of this DomainItem.
        :type hint: int
        """
        self._hint = hint

    @property
    def domain_id(self):
        """Gets the domain_id of this DomainItem.

        网站域名ID

        :return: The domain_id of this DomainItem.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this DomainItem.

        网站域名ID

        :param domain_id: The domain_id of this DomainItem.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def top_level_domain_id(self):
        """Gets the top_level_domain_id of this DomainItem.

        一级域名ID

        :return: The top_level_domain_id of this DomainItem.
        :rtype: str
        """
        return self._top_level_domain_id

    @top_level_domain_id.setter
    def top_level_domain_id(self, top_level_domain_id):
        """Sets the top_level_domain_id of this DomainItem.

        一级域名ID

        :param top_level_domain_id: The top_level_domain_id of this DomainItem.
        :type top_level_domain_id: str
        """
        self._top_level_domain_id = top_level_domain_id

    @property
    def domain_name(self):
        """Gets the domain_name of this DomainItem.

        网站域名

        :return: The domain_name of this DomainItem.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this DomainItem.

        网站域名

        :param domain_name: The domain_name of this DomainItem.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def alias(self):
        """Gets the alias of this DomainItem.

        网站域名的别名

        :return: The alias of this DomainItem.
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this DomainItem.

        网站域名的别名

        :param alias: The alias of this DomainItem.
        :type alias: str
        """
        self._alias = alias

    @property
    def create_time(self):
        """Gets the create_time of this DomainItem.

        创建网站域名资产的时间

        :return: The create_time of this DomainItem.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this DomainItem.

        创建网站域名资产的时间

        :param create_time: The create_time of this DomainItem.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def auth_status(self):
        """Gets the auth_status of this DomainItem.

        网站域名的认证状态:   * unauth - 未认证   * auth - 已认证   * invalid - 认证文件无效   * manual - 人工认证   * skip - 免认证 

        :return: The auth_status of this DomainItem.
        :rtype: str
        """
        return self._auth_status

    @auth_status.setter
    def auth_status(self, auth_status):
        """Sets the auth_status of this DomainItem.

        网站域名的认证状态:   * unauth - 未认证   * auth - 已认证   * invalid - 认证文件无效   * manual - 人工认证   * skip - 免认证 

        :param auth_status: The auth_status of this DomainItem.
        :type auth_status: str
        """
        self._auth_status = auth_status

    @property
    def protocol_type(self):
        """Gets the protocol_type of this DomainItem.

        协议类型:   * http:// - HTTP   * https:// - HTTPS 

        :return: The protocol_type of this DomainItem.
        :rtype: str
        """
        return self._protocol_type

    @protocol_type.setter
    def protocol_type(self, protocol_type):
        """Sets the protocol_type of this DomainItem.

        协议类型:   * http:// - HTTP   * https:// - HTTPS 

        :param protocol_type: The protocol_type of this DomainItem.
        :type protocol_type: str
        """
        self._protocol_type = protocol_type

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
        if not isinstance(other, DomainItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
