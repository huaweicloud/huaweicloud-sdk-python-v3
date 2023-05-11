# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DivergingCommitCounts:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ahead': 'float',
        'behind': 'float'
    }

    attribute_map = {
        'ahead': 'ahead',
        'behind': 'behind'
    }

    def __init__(self, ahead=None, behind=None):
        """DivergingCommitCounts

        The model defined in huaweicloud sdk

        :param ahead: 领先提交数
        :type ahead: float
        :param behind: 滞后提交数
        :type behind: float
        """
        
        

        self._ahead = None
        self._behind = None
        self.discriminator = None

        if ahead is not None:
            self.ahead = ahead
        if behind is not None:
            self.behind = behind

    @property
    def ahead(self):
        """Gets the ahead of this DivergingCommitCounts.

        领先提交数

        :return: The ahead of this DivergingCommitCounts.
        :rtype: float
        """
        return self._ahead

    @ahead.setter
    def ahead(self, ahead):
        """Sets the ahead of this DivergingCommitCounts.

        领先提交数

        :param ahead: The ahead of this DivergingCommitCounts.
        :type ahead: float
        """
        self._ahead = ahead

    @property
    def behind(self):
        """Gets the behind of this DivergingCommitCounts.

        滞后提交数

        :return: The behind of this DivergingCommitCounts.
        :rtype: float
        """
        return self._behind

    @behind.setter
    def behind(self, behind):
        """Sets the behind of this DivergingCommitCounts.

        滞后提交数

        :param behind: The behind of this DivergingCommitCounts.
        :type behind: float
        """
        self._behind = behind

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
        if not isinstance(other, DivergingCommitCounts):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
