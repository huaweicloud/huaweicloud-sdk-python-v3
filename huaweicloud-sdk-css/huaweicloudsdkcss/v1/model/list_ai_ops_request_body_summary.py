# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAiOpsRequestBodySummary:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'high': 'int',
        'medium': 'int',
        'suggestion': 'int'
    }

    attribute_map = {
        'high': 'high',
        'medium': 'medium',
        'suggestion': 'suggestion'
    }

    def __init__(self, high=None, medium=None, suggestion=None):
        """ListAiOpsRequestBodySummary

        The model defined in huaweicloud sdk

        :param high: 检测项判定为高风险的数量。
        :type high: int
        :param medium: 检测项判定为中风险的数量。
        :type medium: int
        :param suggestion: 检测项判定为建议的数量。
        :type suggestion: int
        """
        
        

        self._high = None
        self._medium = None
        self._suggestion = None
        self.discriminator = None

        if high is not None:
            self.high = high
        if medium is not None:
            self.medium = medium
        if suggestion is not None:
            self.suggestion = suggestion

    @property
    def high(self):
        """Gets the high of this ListAiOpsRequestBodySummary.

        检测项判定为高风险的数量。

        :return: The high of this ListAiOpsRequestBodySummary.
        :rtype: int
        """
        return self._high

    @high.setter
    def high(self, high):
        """Sets the high of this ListAiOpsRequestBodySummary.

        检测项判定为高风险的数量。

        :param high: The high of this ListAiOpsRequestBodySummary.
        :type high: int
        """
        self._high = high

    @property
    def medium(self):
        """Gets the medium of this ListAiOpsRequestBodySummary.

        检测项判定为中风险的数量。

        :return: The medium of this ListAiOpsRequestBodySummary.
        :rtype: int
        """
        return self._medium

    @medium.setter
    def medium(self, medium):
        """Sets the medium of this ListAiOpsRequestBodySummary.

        检测项判定为中风险的数量。

        :param medium: The medium of this ListAiOpsRequestBodySummary.
        :type medium: int
        """
        self._medium = medium

    @property
    def suggestion(self):
        """Gets the suggestion of this ListAiOpsRequestBodySummary.

        检测项判定为建议的数量。

        :return: The suggestion of this ListAiOpsRequestBodySummary.
        :rtype: int
        """
        return self._suggestion

    @suggestion.setter
    def suggestion(self, suggestion):
        """Sets the suggestion of this ListAiOpsRequestBodySummary.

        检测项判定为建议的数量。

        :param suggestion: The suggestion of this ListAiOpsRequestBodySummary.
        :type suggestion: int
        """
        self._suggestion = suggestion

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
        if not isinstance(other, ListAiOpsRequestBodySummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
