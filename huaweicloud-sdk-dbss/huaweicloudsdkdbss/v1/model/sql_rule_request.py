# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SqlRuleRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'page': 'int',
        'size': 'int',
        'risk_levels': 'str'
    }

    attribute_map = {
        'page': 'page',
        'size': 'size',
        'risk_levels': 'risk_levels'
    }

    def __init__(self, page=None, size=None, risk_levels=None):
        r"""SqlRuleRequest

        The model defined in huaweicloud sdk

        :param page: 当前页
        :type page: int
        :param size: 每页大小
        :type size: int
        :param risk_levels: 风险级别 - HIGH - MEDIUM - LOW - NO_RISK
        :type risk_levels: str
        """
        
        

        self._page = None
        self._size = None
        self._risk_levels = None
        self.discriminator = None

        if page is not None:
            self.page = page
        if size is not None:
            self.size = size
        if risk_levels is not None:
            self.risk_levels = risk_levels

    @property
    def page(self):
        r"""Gets the page of this SqlRuleRequest.

        当前页

        :return: The page of this SqlRuleRequest.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        r"""Sets the page of this SqlRuleRequest.

        当前页

        :param page: The page of this SqlRuleRequest.
        :type page: int
        """
        self._page = page

    @property
    def size(self):
        r"""Gets the size of this SqlRuleRequest.

        每页大小

        :return: The size of this SqlRuleRequest.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this SqlRuleRequest.

        每页大小

        :param size: The size of this SqlRuleRequest.
        :type size: int
        """
        self._size = size

    @property
    def risk_levels(self):
        r"""Gets the risk_levels of this SqlRuleRequest.

        风险级别 - HIGH - MEDIUM - LOW - NO_RISK

        :return: The risk_levels of this SqlRuleRequest.
        :rtype: str
        """
        return self._risk_levels

    @risk_levels.setter
    def risk_levels(self, risk_levels):
        r"""Sets the risk_levels of this SqlRuleRequest.

        风险级别 - HIGH - MEDIUM - LOW - NO_RISK

        :param risk_levels: The risk_levels of this SqlRuleRequest.
        :type risk_levels: str
        """
        self._risk_levels = risk_levels

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
        if not isinstance(other, SqlRuleRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
