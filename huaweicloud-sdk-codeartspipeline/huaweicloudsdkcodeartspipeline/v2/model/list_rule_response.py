# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRuleResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'data': 'list[Rule]',
        'total': 'int'
    }

    attribute_map = {
        'data': 'data',
        'total': 'total'
    }

    def __init__(self, data=None, total=None):
        r"""ListRuleResponse

        The model defined in huaweicloud sdk

        :param data: 静态规则列表
        :type data: list[:class:`huaweicloudsdkcodeartspipeline.v2.Rule`]
        :param total: 总数
        :type total: int
        """
        
        super(ListRuleResponse, self).__init__()

        self._data = None
        self._total = None
        self.discriminator = None

        if data is not None:
            self.data = data
        if total is not None:
            self.total = total

    @property
    def data(self):
        r"""Gets the data of this ListRuleResponse.

        静态规则列表

        :return: The data of this ListRuleResponse.
        :rtype: list[:class:`huaweicloudsdkcodeartspipeline.v2.Rule`]
        """
        return self._data

    @data.setter
    def data(self, data):
        r"""Sets the data of this ListRuleResponse.

        静态规则列表

        :param data: The data of this ListRuleResponse.
        :type data: list[:class:`huaweicloudsdkcodeartspipeline.v2.Rule`]
        """
        self._data = data

    @property
    def total(self):
        r"""Gets the total of this ListRuleResponse.

        总数

        :return: The total of this ListRuleResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListRuleResponse.

        总数

        :param total: The total of this ListRuleResponse.
        :type total: int
        """
        self._total = total

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
        if not isinstance(other, ListRuleResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
