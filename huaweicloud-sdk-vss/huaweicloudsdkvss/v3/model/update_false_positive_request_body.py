# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateFalsePositiveRequestBody:

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
        'provider': 'str',
        'reason': 'str',
        'vuln_status': 'str'
    }

    attribute_map = {
        'vuln_id': 'vuln_id',
        'provider': 'provider',
        'reason': 'reason',
        'vuln_status': 'vuln_status'
    }

    def __init__(self, vuln_id=None, provider=None, reason=None, vuln_status=None):
        """UpdateFalsePositiveRequestBody

        The model defined in huaweicloud sdk

        :param vuln_id: 漏洞ID
        :type vuln_id: str
        :param provider: 误报确认人
        :type provider: str
        :param reason: 误报确认理由
        :type reason: str
        :param vuln_status: 对漏洞的操作:   * false_report - 更新漏洞状态为误报，并忽略   * repairing - 更新漏洞状态未修复 
        :type vuln_status: str
        """
        
        

        self._vuln_id = None
        self._provider = None
        self._reason = None
        self._vuln_status = None
        self.discriminator = None

        self.vuln_id = vuln_id
        if provider is not None:
            self.provider = provider
        if reason is not None:
            self.reason = reason
        if vuln_status is not None:
            self.vuln_status = vuln_status

    @property
    def vuln_id(self):
        """Gets the vuln_id of this UpdateFalsePositiveRequestBody.

        漏洞ID

        :return: The vuln_id of this UpdateFalsePositiveRequestBody.
        :rtype: str
        """
        return self._vuln_id

    @vuln_id.setter
    def vuln_id(self, vuln_id):
        """Sets the vuln_id of this UpdateFalsePositiveRequestBody.

        漏洞ID

        :param vuln_id: The vuln_id of this UpdateFalsePositiveRequestBody.
        :type vuln_id: str
        """
        self._vuln_id = vuln_id

    @property
    def provider(self):
        """Gets the provider of this UpdateFalsePositiveRequestBody.

        误报确认人

        :return: The provider of this UpdateFalsePositiveRequestBody.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this UpdateFalsePositiveRequestBody.

        误报确认人

        :param provider: The provider of this UpdateFalsePositiveRequestBody.
        :type provider: str
        """
        self._provider = provider

    @property
    def reason(self):
        """Gets the reason of this UpdateFalsePositiveRequestBody.

        误报确认理由

        :return: The reason of this UpdateFalsePositiveRequestBody.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this UpdateFalsePositiveRequestBody.

        误报确认理由

        :param reason: The reason of this UpdateFalsePositiveRequestBody.
        :type reason: str
        """
        self._reason = reason

    @property
    def vuln_status(self):
        """Gets the vuln_status of this UpdateFalsePositiveRequestBody.

        对漏洞的操作:   * false_report - 更新漏洞状态为误报，并忽略   * repairing - 更新漏洞状态未修复 

        :return: The vuln_status of this UpdateFalsePositiveRequestBody.
        :rtype: str
        """
        return self._vuln_status

    @vuln_status.setter
    def vuln_status(self, vuln_status):
        """Sets the vuln_status of this UpdateFalsePositiveRequestBody.

        对漏洞的操作:   * false_report - 更新漏洞状态为误报，并忽略   * repairing - 更新漏洞状态未修复 

        :param vuln_status: The vuln_status of this UpdateFalsePositiveRequestBody.
        :type vuln_status: str
        """
        self._vuln_status = vuln_status

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
        if not isinstance(other, UpdateFalsePositiveRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
