# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateArchiveRuleReqBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []
    sensitive_list.append('name')

    openapi_types = {
        'filters': 'list[FindingFilter]',
        'name': 'str'
    }

    attribute_map = {
        'filters': 'filters',
        'name': 'name'
    }

    def __init__(self, filters=None, name=None):
        """CreateArchiveRuleReqBody

        The model defined in huaweicloud sdk

        :param filters: 匹配要返回的访问分析结果的筛选器。
        :type filters: list[:class:`huaweicloudsdkiamaccessanalyzer.v1.FindingFilter`]
        :param name: 创建存档规则的名称。
        :type name: str
        """
        
        

        self._filters = None
        self._name = None
        self.discriminator = None

        self.filters = filters
        self.name = name

    @property
    def filters(self):
        """Gets the filters of this CreateArchiveRuleReqBody.

        匹配要返回的访问分析结果的筛选器。

        :return: The filters of this CreateArchiveRuleReqBody.
        :rtype: list[:class:`huaweicloudsdkiamaccessanalyzer.v1.FindingFilter`]
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        """Sets the filters of this CreateArchiveRuleReqBody.

        匹配要返回的访问分析结果的筛选器。

        :param filters: The filters of this CreateArchiveRuleReqBody.
        :type filters: list[:class:`huaweicloudsdkiamaccessanalyzer.v1.FindingFilter`]
        """
        self._filters = filters

    @property
    def name(self):
        """Gets the name of this CreateArchiveRuleReqBody.

        创建存档规则的名称。

        :return: The name of this CreateArchiveRuleReqBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateArchiveRuleReqBody.

        创建存档规则的名称。

        :param name: The name of this CreateArchiveRuleReqBody.
        :type name: str
        """
        self._name = name

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
        if not isinstance(other, CreateArchiveRuleReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
