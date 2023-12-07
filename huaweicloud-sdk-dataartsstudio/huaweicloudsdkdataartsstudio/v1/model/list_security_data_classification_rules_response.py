# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSecurityDataClassificationRulesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'content': 'list[DataClassificationRuleQueryDTO]',
        'total': 'int'
    }

    attribute_map = {
        'content': 'content',
        'total': 'total'
    }

    def __init__(self, content=None, total=None):
        """ListSecurityDataClassificationRulesResponse

        The model defined in huaweicloud sdk

        :param content: 查询到的所有数据识别规则
        :type content: list[:class:`huaweicloudsdkdataartsstudio.v1.DataClassificationRuleQueryDTO`]
        :param total: 数据识别规则总数
        :type total: int
        """
        
        super(ListSecurityDataClassificationRulesResponse, self).__init__()

        self._content = None
        self._total = None
        self.discriminator = None

        if content is not None:
            self.content = content
        if total is not None:
            self.total = total

    @property
    def content(self):
        """Gets the content of this ListSecurityDataClassificationRulesResponse.

        查询到的所有数据识别规则

        :return: The content of this ListSecurityDataClassificationRulesResponse.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.DataClassificationRuleQueryDTO`]
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this ListSecurityDataClassificationRulesResponse.

        查询到的所有数据识别规则

        :param content: The content of this ListSecurityDataClassificationRulesResponse.
        :type content: list[:class:`huaweicloudsdkdataartsstudio.v1.DataClassificationRuleQueryDTO`]
        """
        self._content = content

    @property
    def total(self):
        """Gets the total of this ListSecurityDataClassificationRulesResponse.

        数据识别规则总数

        :return: The total of this ListSecurityDataClassificationRulesResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListSecurityDataClassificationRulesResponse.

        数据识别规则总数

        :param total: The total of this ListSecurityDataClassificationRulesResponse.
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
        if not isinstance(other, ListSecurityDataClassificationRulesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
