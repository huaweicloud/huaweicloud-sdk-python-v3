# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VulnItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vuln_id': 'str',
        'domain_id': 'str',
        'url': 'str',
        'severity': 'str',
        'vuln_status': 'str',
        'vuln_class': 'str',
        'vuln_type': 'str',
        'description': 'str',
        'advice': 'str',
        'hit_details': 'str',
        'request': 'str',
        'response': 'str',
        'provider': 'str',
        'reason': 'str',
        'find_time': 'str'
    }

    attribute_map = {
        'vuln_id': 'vuln_id',
        'domain_id': 'domain_id',
        'url': 'url',
        'severity': 'severity',
        'vuln_status': 'vuln_status',
        'vuln_class': 'vuln_class',
        'vuln_type': 'vuln_type',
        'description': 'description',
        'advice': 'advice',
        'hit_details': 'hit_details',
        'request': 'request',
        'response': 'response',
        'provider': 'provider',
        'reason': 'reason',
        'find_time': 'find_time'
    }

    def __init__(self, vuln_id=None, domain_id=None, url=None, severity=None, vuln_status=None, vuln_class=None, vuln_type=None, description=None, advice=None, hit_details=None, request=None, response=None, provider=None, reason=None, find_time=None):
        """VulnItem

        The model defined in huaweicloud sdk

        :param vuln_id: 漏洞ID
        :type vuln_id: str
        :param domain_id: 网站域名ID
        :type domain_id: str
        :param url: 目标网址
        :type url: str
        :param severity: 漏洞风险等级:   * high - 高风险   * middle - 中风险   * low - 低风险   * hint - 提示 
        :type severity: str
        :param vuln_status: 漏洞状态:   * repairing - 未修复   * repaired - 已修复   * false_report - 误报，已忽略 
        :type vuln_status: str
        :param vuln_class: 漏洞类别
        :type vuln_class: str
        :param vuln_type: 漏洞名称
        :type vuln_type: str
        :param description: 漏洞描述
        :type description: str
        :param advice: 修复建议
        :type advice: str
        :param hit_details: 命中详情
        :type hit_details: str
        :param request: 请求详情
        :type request: str
        :param response: 响应详情
        :type response: str
        :param provider: 漏洞确认人
        :type provider: str
        :param reason: 漏洞忽略理由
        :type reason: str
        :param find_time: 漏洞发现时间
        :type find_time: str
        """
        
        

        self._vuln_id = None
        self._domain_id = None
        self._url = None
        self._severity = None
        self._vuln_status = None
        self._vuln_class = None
        self._vuln_type = None
        self._description = None
        self._advice = None
        self._hit_details = None
        self._request = None
        self._response = None
        self._provider = None
        self._reason = None
        self._find_time = None
        self.discriminator = None

        if vuln_id is not None:
            self.vuln_id = vuln_id
        if domain_id is not None:
            self.domain_id = domain_id
        if url is not None:
            self.url = url
        if severity is not None:
            self.severity = severity
        if vuln_status is not None:
            self.vuln_status = vuln_status
        if vuln_class is not None:
            self.vuln_class = vuln_class
        if vuln_type is not None:
            self.vuln_type = vuln_type
        if description is not None:
            self.description = description
        if advice is not None:
            self.advice = advice
        if hit_details is not None:
            self.hit_details = hit_details
        if request is not None:
            self.request = request
        if response is not None:
            self.response = response
        if provider is not None:
            self.provider = provider
        if reason is not None:
            self.reason = reason
        if find_time is not None:
            self.find_time = find_time

    @property
    def vuln_id(self):
        """Gets the vuln_id of this VulnItem.

        漏洞ID

        :return: The vuln_id of this VulnItem.
        :rtype: str
        """
        return self._vuln_id

    @vuln_id.setter
    def vuln_id(self, vuln_id):
        """Sets the vuln_id of this VulnItem.

        漏洞ID

        :param vuln_id: The vuln_id of this VulnItem.
        :type vuln_id: str
        """
        self._vuln_id = vuln_id

    @property
    def domain_id(self):
        """Gets the domain_id of this VulnItem.

        网站域名ID

        :return: The domain_id of this VulnItem.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this VulnItem.

        网站域名ID

        :param domain_id: The domain_id of this VulnItem.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def url(self):
        """Gets the url of this VulnItem.

        目标网址

        :return: The url of this VulnItem.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this VulnItem.

        目标网址

        :param url: The url of this VulnItem.
        :type url: str
        """
        self._url = url

    @property
    def severity(self):
        """Gets the severity of this VulnItem.

        漏洞风险等级:   * high - 高风险   * middle - 中风险   * low - 低风险   * hint - 提示 

        :return: The severity of this VulnItem.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this VulnItem.

        漏洞风险等级:   * high - 高风险   * middle - 中风险   * low - 低风险   * hint - 提示 

        :param severity: The severity of this VulnItem.
        :type severity: str
        """
        self._severity = severity

    @property
    def vuln_status(self):
        """Gets the vuln_status of this VulnItem.

        漏洞状态:   * repairing - 未修复   * repaired - 已修复   * false_report - 误报，已忽略 

        :return: The vuln_status of this VulnItem.
        :rtype: str
        """
        return self._vuln_status

    @vuln_status.setter
    def vuln_status(self, vuln_status):
        """Sets the vuln_status of this VulnItem.

        漏洞状态:   * repairing - 未修复   * repaired - 已修复   * false_report - 误报，已忽略 

        :param vuln_status: The vuln_status of this VulnItem.
        :type vuln_status: str
        """
        self._vuln_status = vuln_status

    @property
    def vuln_class(self):
        """Gets the vuln_class of this VulnItem.

        漏洞类别

        :return: The vuln_class of this VulnItem.
        :rtype: str
        """
        return self._vuln_class

    @vuln_class.setter
    def vuln_class(self, vuln_class):
        """Sets the vuln_class of this VulnItem.

        漏洞类别

        :param vuln_class: The vuln_class of this VulnItem.
        :type vuln_class: str
        """
        self._vuln_class = vuln_class

    @property
    def vuln_type(self):
        """Gets the vuln_type of this VulnItem.

        漏洞名称

        :return: The vuln_type of this VulnItem.
        :rtype: str
        """
        return self._vuln_type

    @vuln_type.setter
    def vuln_type(self, vuln_type):
        """Sets the vuln_type of this VulnItem.

        漏洞名称

        :param vuln_type: The vuln_type of this VulnItem.
        :type vuln_type: str
        """
        self._vuln_type = vuln_type

    @property
    def description(self):
        """Gets the description of this VulnItem.

        漏洞描述

        :return: The description of this VulnItem.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this VulnItem.

        漏洞描述

        :param description: The description of this VulnItem.
        :type description: str
        """
        self._description = description

    @property
    def advice(self):
        """Gets the advice of this VulnItem.

        修复建议

        :return: The advice of this VulnItem.
        :rtype: str
        """
        return self._advice

    @advice.setter
    def advice(self, advice):
        """Sets the advice of this VulnItem.

        修复建议

        :param advice: The advice of this VulnItem.
        :type advice: str
        """
        self._advice = advice

    @property
    def hit_details(self):
        """Gets the hit_details of this VulnItem.

        命中详情

        :return: The hit_details of this VulnItem.
        :rtype: str
        """
        return self._hit_details

    @hit_details.setter
    def hit_details(self, hit_details):
        """Sets the hit_details of this VulnItem.

        命中详情

        :param hit_details: The hit_details of this VulnItem.
        :type hit_details: str
        """
        self._hit_details = hit_details

    @property
    def request(self):
        """Gets the request of this VulnItem.

        请求详情

        :return: The request of this VulnItem.
        :rtype: str
        """
        return self._request

    @request.setter
    def request(self, request):
        """Sets the request of this VulnItem.

        请求详情

        :param request: The request of this VulnItem.
        :type request: str
        """
        self._request = request

    @property
    def response(self):
        """Gets the response of this VulnItem.

        响应详情

        :return: The response of this VulnItem.
        :rtype: str
        """
        return self._response

    @response.setter
    def response(self, response):
        """Sets the response of this VulnItem.

        响应详情

        :param response: The response of this VulnItem.
        :type response: str
        """
        self._response = response

    @property
    def provider(self):
        """Gets the provider of this VulnItem.

        漏洞确认人

        :return: The provider of this VulnItem.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this VulnItem.

        漏洞确认人

        :param provider: The provider of this VulnItem.
        :type provider: str
        """
        self._provider = provider

    @property
    def reason(self):
        """Gets the reason of this VulnItem.

        漏洞忽略理由

        :return: The reason of this VulnItem.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this VulnItem.

        漏洞忽略理由

        :param reason: The reason of this VulnItem.
        :type reason: str
        """
        self._reason = reason

    @property
    def find_time(self):
        """Gets the find_time of this VulnItem.

        漏洞发现时间

        :return: The find_time of this VulnItem.
        :rtype: str
        """
        return self._find_time

    @find_time.setter
    def find_time(self, find_time):
        """Sets the find_time of this VulnItem.

        漏洞发现时间

        :param find_time: The find_time of this VulnItem.
        :type find_time: str
        """
        self._find_time = find_time

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
        if not isinstance(other, VulnItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
