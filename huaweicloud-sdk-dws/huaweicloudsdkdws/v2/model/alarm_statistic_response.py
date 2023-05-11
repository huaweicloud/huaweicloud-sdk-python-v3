# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AlarmStatisticResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'date': 'str',
        'urgent': 'str',
        'important': 'str',
        'minor': 'str',
        'prompt': 'str'
    }

    attribute_map = {
        'date': 'date',
        'urgent': 'urgent',
        'important': 'important',
        'minor': 'minor',
        'prompt': 'prompt'
    }

    def __init__(self, date=None, urgent=None, important=None, minor=None, prompt=None):
        """AlarmStatisticResponse

        The model defined in huaweicloud sdk

        :param date: 日期
        :type date: str
        :param urgent: 紧急
        :type urgent: str
        :param important: 重要
        :type important: str
        :param minor: 次要
        :type minor: str
        :param prompt: 提示
        :type prompt: str
        """
        
        

        self._date = None
        self._urgent = None
        self._important = None
        self._minor = None
        self._prompt = None
        self.discriminator = None

        if date is not None:
            self.date = date
        if urgent is not None:
            self.urgent = urgent
        if important is not None:
            self.important = important
        if minor is not None:
            self.minor = minor
        if prompt is not None:
            self.prompt = prompt

    @property
    def date(self):
        """Gets the date of this AlarmStatisticResponse.

        日期

        :return: The date of this AlarmStatisticResponse.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this AlarmStatisticResponse.

        日期

        :param date: The date of this AlarmStatisticResponse.
        :type date: str
        """
        self._date = date

    @property
    def urgent(self):
        """Gets the urgent of this AlarmStatisticResponse.

        紧急

        :return: The urgent of this AlarmStatisticResponse.
        :rtype: str
        """
        return self._urgent

    @urgent.setter
    def urgent(self, urgent):
        """Sets the urgent of this AlarmStatisticResponse.

        紧急

        :param urgent: The urgent of this AlarmStatisticResponse.
        :type urgent: str
        """
        self._urgent = urgent

    @property
    def important(self):
        """Gets the important of this AlarmStatisticResponse.

        重要

        :return: The important of this AlarmStatisticResponse.
        :rtype: str
        """
        return self._important

    @important.setter
    def important(self, important):
        """Sets the important of this AlarmStatisticResponse.

        重要

        :param important: The important of this AlarmStatisticResponse.
        :type important: str
        """
        self._important = important

    @property
    def minor(self):
        """Gets the minor of this AlarmStatisticResponse.

        次要

        :return: The minor of this AlarmStatisticResponse.
        :rtype: str
        """
        return self._minor

    @minor.setter
    def minor(self, minor):
        """Sets the minor of this AlarmStatisticResponse.

        次要

        :param minor: The minor of this AlarmStatisticResponse.
        :type minor: str
        """
        self._minor = minor

    @property
    def prompt(self):
        """Gets the prompt of this AlarmStatisticResponse.

        提示

        :return: The prompt of this AlarmStatisticResponse.
        :rtype: str
        """
        return self._prompt

    @prompt.setter
    def prompt(self, prompt):
        """Sets the prompt of this AlarmStatisticResponse.

        提示

        :param prompt: The prompt of this AlarmStatisticResponse.
        :type prompt: str
        """
        self._prompt = prompt

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
        if not isinstance(other, AlarmStatisticResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
