# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LabelSelector:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'match_labels': 'dict(str, str)',
        'match_expressions': 'list[FieldSelector]'
    }

    attribute_map = {
        'match_labels': 'matchLabels',
        'match_expressions': 'matchExpressions'
    }

    def __init__(self, match_labels=None, match_expressions=None):
        """LabelSelector

        The model defined in huaweicloud sdk

        :param match_labels: 
        :type match_labels: dict(str, str)
        :param match_expressions: 
        :type match_expressions: list[:class:`huaweicloudsdkasm.v1.FieldSelector`]
        """
        
        

        self._match_labels = None
        self._match_expressions = None
        self.discriminator = None

        if match_labels is not None:
            self.match_labels = match_labels
        if match_expressions is not None:
            self.match_expressions = match_expressions

    @property
    def match_labels(self):
        """Gets the match_labels of this LabelSelector.

        :return: The match_labels of this LabelSelector.
        :rtype: dict(str, str)
        """
        return self._match_labels

    @match_labels.setter
    def match_labels(self, match_labels):
        """Sets the match_labels of this LabelSelector.

        :param match_labels: The match_labels of this LabelSelector.
        :type match_labels: dict(str, str)
        """
        self._match_labels = match_labels

    @property
    def match_expressions(self):
        """Gets the match_expressions of this LabelSelector.

        :return: The match_expressions of this LabelSelector.
        :rtype: list[:class:`huaweicloudsdkasm.v1.FieldSelector`]
        """
        return self._match_expressions

    @match_expressions.setter
    def match_expressions(self, match_expressions):
        """Sets the match_expressions of this LabelSelector.

        :param match_expressions: The match_expressions of this LabelSelector.
        :type match_expressions: list[:class:`huaweicloudsdkasm.v1.FieldSelector`]
        """
        self._match_expressions = match_expressions

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
        if not isinstance(other, LabelSelector):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
