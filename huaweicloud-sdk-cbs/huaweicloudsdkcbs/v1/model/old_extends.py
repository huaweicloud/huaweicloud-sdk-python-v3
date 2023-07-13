# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OldExtends:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domains': 'list[str]',
        'top': 'int'
    }

    attribute_map = {
        'domains': 'domains',
        'top': 'top'
    }

    def __init__(self, domains=None, top=None):
        """OldExtends

        The model defined in huaweicloud sdk

        :param domains: 领域列表，多个领域用分号隔开。如果设置了领域且领域不为空，就从这些领域中匹配答案，否则就从该用户的全部知识库匹配答案。  当前最多支持10个领域。 
        :type domains: list[str]
        :param top: 返回答案数量，默认为5，取值范围1~10。
        :type top: int
        """
        
        

        self._domains = None
        self._top = None
        self.discriminator = None

        if domains is not None:
            self.domains = domains
        if top is not None:
            self.top = top

    @property
    def domains(self):
        """Gets the domains of this OldExtends.

        领域列表，多个领域用分号隔开。如果设置了领域且领域不为空，就从这些领域中匹配答案，否则就从该用户的全部知识库匹配答案。  当前最多支持10个领域。 

        :return: The domains of this OldExtends.
        :rtype: list[str]
        """
        return self._domains

    @domains.setter
    def domains(self, domains):
        """Sets the domains of this OldExtends.

        领域列表，多个领域用分号隔开。如果设置了领域且领域不为空，就从这些领域中匹配答案，否则就从该用户的全部知识库匹配答案。  当前最多支持10个领域。 

        :param domains: The domains of this OldExtends.
        :type domains: list[str]
        """
        self._domains = domains

    @property
    def top(self):
        """Gets the top of this OldExtends.

        返回答案数量，默认为5，取值范围1~10。

        :return: The top of this OldExtends.
        :rtype: int
        """
        return self._top

    @top.setter
    def top(self, top):
        """Sets the top of this OldExtends.

        返回答案数量，默认为5，取值范围1~10。

        :param top: The top of this OldExtends.
        :type top: int
        """
        self._top = top

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
        if not isinstance(other, OldExtends):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
