# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AssessProperty:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'expected': 'str',
        'actual': 'str',
        'suggestion': 'str',
        'suggestion_en': 'str',
        'status': 'int'
    }

    attribute_map = {
        'expected': 'expected',
        'actual': 'actual',
        'suggestion': 'suggestion',
        'suggestion_en': 'suggestion_en',
        'status': 'status'
    }

    def __init__(self, expected=None, actual=None, suggestion=None, suggestion_en=None, status=None):
        r"""AssessProperty

        The model defined in huaweicloud sdk

        :param expected: 预期信息
        :type expected: str
        :param actual: 实际信息
        :type actual: str
        :param suggestion: 中文建议
        :type suggestion: str
        :param suggestion_en: 英文建议
        :type suggestion_en: str
        :param status: 是否超出范围
        :type status: int
        """
        
        

        self._expected = None
        self._actual = None
        self._suggestion = None
        self._suggestion_en = None
        self._status = None
        self.discriminator = None

        if expected is not None:
            self.expected = expected
        if actual is not None:
            self.actual = actual
        if suggestion is not None:
            self.suggestion = suggestion
        if suggestion_en is not None:
            self.suggestion_en = suggestion_en
        if status is not None:
            self.status = status

    @property
    def expected(self):
        r"""Gets the expected of this AssessProperty.

        预期信息

        :return: The expected of this AssessProperty.
        :rtype: str
        """
        return self._expected

    @expected.setter
    def expected(self, expected):
        r"""Sets the expected of this AssessProperty.

        预期信息

        :param expected: The expected of this AssessProperty.
        :type expected: str
        """
        self._expected = expected

    @property
    def actual(self):
        r"""Gets the actual of this AssessProperty.

        实际信息

        :return: The actual of this AssessProperty.
        :rtype: str
        """
        return self._actual

    @actual.setter
    def actual(self, actual):
        r"""Sets the actual of this AssessProperty.

        实际信息

        :param actual: The actual of this AssessProperty.
        :type actual: str
        """
        self._actual = actual

    @property
    def suggestion(self):
        r"""Gets the suggestion of this AssessProperty.

        中文建议

        :return: The suggestion of this AssessProperty.
        :rtype: str
        """
        return self._suggestion

    @suggestion.setter
    def suggestion(self, suggestion):
        r"""Sets the suggestion of this AssessProperty.

        中文建议

        :param suggestion: The suggestion of this AssessProperty.
        :type suggestion: str
        """
        self._suggestion = suggestion

    @property
    def suggestion_en(self):
        r"""Gets the suggestion_en of this AssessProperty.

        英文建议

        :return: The suggestion_en of this AssessProperty.
        :rtype: str
        """
        return self._suggestion_en

    @suggestion_en.setter
    def suggestion_en(self, suggestion_en):
        r"""Sets the suggestion_en of this AssessProperty.

        英文建议

        :param suggestion_en: The suggestion_en of this AssessProperty.
        :type suggestion_en: str
        """
        self._suggestion_en = suggestion_en

    @property
    def status(self):
        r"""Gets the status of this AssessProperty.

        是否超出范围

        :return: The status of this AssessProperty.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this AssessProperty.

        是否超出范围

        :param status: The status of this AssessProperty.
        :type status: int
        """
        self._status = status

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
        if not isinstance(other, AssessProperty):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
