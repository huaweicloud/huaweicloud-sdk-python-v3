# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ValidatePolicyFinding:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'finding_details': 'str',
        'finding_type': 'str',
        'issue_code': 'str',
        'learn_more_link': 'str',
        'locations': 'list[Location]'
    }

    attribute_map = {
        'finding_details': 'finding_details',
        'finding_type': 'finding_type',
        'issue_code': 'issue_code',
        'learn_more_link': 'learn_more_link',
        'locations': 'locations'
    }

    def __init__(self, finding_details=None, finding_type=None, issue_code=None, learn_more_link=None, locations=None):
        """ValidatePolicyFinding

        The model defined in huaweicloud sdk

        :param finding_details: 一条本地化消息提供了如何解决该问题的指导。
        :type finding_details: str
        :param finding_type: 影响级别。  安全：策略存在安全风险，可能是允许访问的权限过于宽松等导致。  错误：存在策略无法运行的错误，如语法错误、参数错误等。存在错误的情况下策略无法创建。  警告：存在策略无法运行的警告，如参数取值类型不匹配等。存在警告的情况下策略可以创建。  建议：不影响策略运行，但策略可能不能达到预期的效果。如存在空数组、空对象条件等。 
        :type finding_type: str
        :param issue_code: 问题码提供了与此校验结果关联的问题的标识符。
        :type issue_code: str
        :param learn_more_link: 指向与此校验结果关联的相关文档的链接。
        :type learn_more_link: str
        :param locations: 策略文档中与校验结果相关的位置列表。
        :type locations: list[:class:`huaweicloudsdkiamaccessanalyzer.v1.Location`]
        """
        
        

        self._finding_details = None
        self._finding_type = None
        self._issue_code = None
        self._learn_more_link = None
        self._locations = None
        self.discriminator = None

        self.finding_details = finding_details
        self.finding_type = finding_type
        self.issue_code = issue_code
        self.learn_more_link = learn_more_link
        self.locations = locations

    @property
    def finding_details(self):
        """Gets the finding_details of this ValidatePolicyFinding.

        一条本地化消息提供了如何解决该问题的指导。

        :return: The finding_details of this ValidatePolicyFinding.
        :rtype: str
        """
        return self._finding_details

    @finding_details.setter
    def finding_details(self, finding_details):
        """Sets the finding_details of this ValidatePolicyFinding.

        一条本地化消息提供了如何解决该问题的指导。

        :param finding_details: The finding_details of this ValidatePolicyFinding.
        :type finding_details: str
        """
        self._finding_details = finding_details

    @property
    def finding_type(self):
        """Gets the finding_type of this ValidatePolicyFinding.

        影响级别。  安全：策略存在安全风险，可能是允许访问的权限过于宽松等导致。  错误：存在策略无法运行的错误，如语法错误、参数错误等。存在错误的情况下策略无法创建。  警告：存在策略无法运行的警告，如参数取值类型不匹配等。存在警告的情况下策略可以创建。  建议：不影响策略运行，但策略可能不能达到预期的效果。如存在空数组、空对象条件等。 

        :return: The finding_type of this ValidatePolicyFinding.
        :rtype: str
        """
        return self._finding_type

    @finding_type.setter
    def finding_type(self, finding_type):
        """Sets the finding_type of this ValidatePolicyFinding.

        影响级别。  安全：策略存在安全风险，可能是允许访问的权限过于宽松等导致。  错误：存在策略无法运行的错误，如语法错误、参数错误等。存在错误的情况下策略无法创建。  警告：存在策略无法运行的警告，如参数取值类型不匹配等。存在警告的情况下策略可以创建。  建议：不影响策略运行，但策略可能不能达到预期的效果。如存在空数组、空对象条件等。 

        :param finding_type: The finding_type of this ValidatePolicyFinding.
        :type finding_type: str
        """
        self._finding_type = finding_type

    @property
    def issue_code(self):
        """Gets the issue_code of this ValidatePolicyFinding.

        问题码提供了与此校验结果关联的问题的标识符。

        :return: The issue_code of this ValidatePolicyFinding.
        :rtype: str
        """
        return self._issue_code

    @issue_code.setter
    def issue_code(self, issue_code):
        """Sets the issue_code of this ValidatePolicyFinding.

        问题码提供了与此校验结果关联的问题的标识符。

        :param issue_code: The issue_code of this ValidatePolicyFinding.
        :type issue_code: str
        """
        self._issue_code = issue_code

    @property
    def learn_more_link(self):
        """Gets the learn_more_link of this ValidatePolicyFinding.

        指向与此校验结果关联的相关文档的链接。

        :return: The learn_more_link of this ValidatePolicyFinding.
        :rtype: str
        """
        return self._learn_more_link

    @learn_more_link.setter
    def learn_more_link(self, learn_more_link):
        """Sets the learn_more_link of this ValidatePolicyFinding.

        指向与此校验结果关联的相关文档的链接。

        :param learn_more_link: The learn_more_link of this ValidatePolicyFinding.
        :type learn_more_link: str
        """
        self._learn_more_link = learn_more_link

    @property
    def locations(self):
        """Gets the locations of this ValidatePolicyFinding.

        策略文档中与校验结果相关的位置列表。

        :return: The locations of this ValidatePolicyFinding.
        :rtype: list[:class:`huaweicloudsdkiamaccessanalyzer.v1.Location`]
        """
        return self._locations

    @locations.setter
    def locations(self, locations):
        """Sets the locations of this ValidatePolicyFinding.

        策略文档中与校验结果相关的位置列表。

        :param locations: The locations of this ValidatePolicyFinding.
        :type locations: list[:class:`huaweicloudsdkiamaccessanalyzer.v1.Location`]
        """
        self._locations = locations

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
        if not isinstance(other, ValidatePolicyFinding):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
