# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GradedCount:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'complete_match': 'int',
        'partial_match': 'int',
        'no_match': 'int'
    }

    attribute_map = {
        'total': 'total',
        'complete_match': 'complete_match',
        'partial_match': 'partial_match',
        'no_match': 'no_match'
    }

    def __init__(self, total=None, complete_match=None, partial_match=None, no_match=None):
        r"""GradedCount

        The model defined in huaweicloud sdk

        :param total: 总数
        :type total: int
        :param complete_match: 合规资源数
        :type complete_match: int
        :param partial_match: 部分合规资源数
        :type partial_match: int
        :param no_match: 不合规资源数
        :type no_match: int
        """
        
        

        self._total = None
        self._complete_match = None
        self._partial_match = None
        self._no_match = None
        self.discriminator = None

        self.total = total
        if complete_match is not None:
            self.complete_match = complete_match
        if partial_match is not None:
            self.partial_match = partial_match
        if no_match is not None:
            self.no_match = no_match

    @property
    def total(self):
        r"""Gets the total of this GradedCount.

        总数

        :return: The total of this GradedCount.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this GradedCount.

        总数

        :param total: The total of this GradedCount.
        :type total: int
        """
        self._total = total

    @property
    def complete_match(self):
        r"""Gets the complete_match of this GradedCount.

        合规资源数

        :return: The complete_match of this GradedCount.
        :rtype: int
        """
        return self._complete_match

    @complete_match.setter
    def complete_match(self, complete_match):
        r"""Sets the complete_match of this GradedCount.

        合规资源数

        :param complete_match: The complete_match of this GradedCount.
        :type complete_match: int
        """
        self._complete_match = complete_match

    @property
    def partial_match(self):
        r"""Gets the partial_match of this GradedCount.

        部分合规资源数

        :return: The partial_match of this GradedCount.
        :rtype: int
        """
        return self._partial_match

    @partial_match.setter
    def partial_match(self, partial_match):
        r"""Sets the partial_match of this GradedCount.

        部分合规资源数

        :param partial_match: The partial_match of this GradedCount.
        :type partial_match: int
        """
        self._partial_match = partial_match

    @property
    def no_match(self):
        r"""Gets the no_match of this GradedCount.

        不合规资源数

        :return: The no_match of this GradedCount.
        :rtype: int
        """
        return self._no_match

    @no_match.setter
    def no_match(self, no_match):
        r"""Sets the no_match of this GradedCount.

        不合规资源数

        :param no_match: The no_match of this GradedCount.
        :type no_match: int
        """
        self._no_match = no_match

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
        if not isinstance(other, GradedCount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
