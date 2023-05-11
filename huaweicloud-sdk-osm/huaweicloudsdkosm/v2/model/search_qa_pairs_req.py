# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SearchQaPairsReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain': 'str',
        'top': 'int'
    }

    attribute_map = {
        'domain': 'domain',
        'top': 'top'
    }

    def __init__(self, domain=None, top=None):
        """SearchQaPairsReq

        The model defined in huaweicloud sdk

        :param domain: 主题名称
        :type domain: str
        :param top: 返回匹配度最高的数据条数
        :type top: int
        """
        
        

        self._domain = None
        self._top = None
        self.discriminator = None

        if domain is not None:
            self.domain = domain
        if top is not None:
            self.top = top

    @property
    def domain(self):
        """Gets the domain of this SearchQaPairsReq.

        主题名称

        :return: The domain of this SearchQaPairsReq.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this SearchQaPairsReq.

        主题名称

        :param domain: The domain of this SearchQaPairsReq.
        :type domain: str
        """
        self._domain = domain

    @property
    def top(self):
        """Gets the top of this SearchQaPairsReq.

        返回匹配度最高的数据条数

        :return: The top of this SearchQaPairsReq.
        :rtype: int
        """
        return self._top

    @top.setter
    def top(self, top):
        """Sets the top of this SearchQaPairsReq.

        返回匹配度最高的数据条数

        :param top: The top of this SearchQaPairsReq.
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
        if not isinstance(other, SearchQaPairsReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
