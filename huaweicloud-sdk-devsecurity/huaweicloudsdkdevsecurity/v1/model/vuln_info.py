# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VulnInfo:

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
        'principle': 'str',
        'solution': 'str',
        'vuln_items': 'list[VulnItem]'
    }

    attribute_map = {
        'category': 'category',
        'principle': 'principle',
        'solution': 'solution',
        'vuln_items': 'vuln_items'
    }

    def __init__(self, category=None, principle=None, solution=None, vuln_items=None):
        """VulnInfo

        The model defined in huaweicloud sdk

        :param category: 漏洞类型
        :type category: str
        :param principle: 漏洞原理
        :type principle: str
        :param solution: 解决方案
        :type solution: str
        :param vuln_items: 漏洞项列表
        :type vuln_items: list[:class:`huaweicloudsdkdevsecurity.v1.VulnItem`]
        """
        
        

        self._category = None
        self._principle = None
        self._solution = None
        self._vuln_items = None
        self.discriminator = None

        if category is not None:
            self.category = category
        if principle is not None:
            self.principle = principle
        if solution is not None:
            self.solution = solution
        if vuln_items is not None:
            self.vuln_items = vuln_items

    @property
    def category(self):
        """Gets the category of this VulnInfo.

        漏洞类型

        :return: The category of this VulnInfo.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this VulnInfo.

        漏洞类型

        :param category: The category of this VulnInfo.
        :type category: str
        """
        self._category = category

    @property
    def principle(self):
        """Gets the principle of this VulnInfo.

        漏洞原理

        :return: The principle of this VulnInfo.
        :rtype: str
        """
        return self._principle

    @principle.setter
    def principle(self, principle):
        """Sets the principle of this VulnInfo.

        漏洞原理

        :param principle: The principle of this VulnInfo.
        :type principle: str
        """
        self._principle = principle

    @property
    def solution(self):
        """Gets the solution of this VulnInfo.

        解决方案

        :return: The solution of this VulnInfo.
        :rtype: str
        """
        return self._solution

    @solution.setter
    def solution(self, solution):
        """Sets the solution of this VulnInfo.

        解决方案

        :param solution: The solution of this VulnInfo.
        :type solution: str
        """
        self._solution = solution

    @property
    def vuln_items(self):
        """Gets the vuln_items of this VulnInfo.

        漏洞项列表

        :return: The vuln_items of this VulnInfo.
        :rtype: list[:class:`huaweicloudsdkdevsecurity.v1.VulnItem`]
        """
        return self._vuln_items

    @vuln_items.setter
    def vuln_items(self, vuln_items):
        """Sets the vuln_items of this VulnInfo.

        漏洞项列表

        :param vuln_items: The vuln_items of this VulnInfo.
        :type vuln_items: list[:class:`huaweicloudsdkdevsecurity.v1.VulnItem`]
        """
        self._vuln_items = vuln_items

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
        if not isinstance(other, VulnInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
