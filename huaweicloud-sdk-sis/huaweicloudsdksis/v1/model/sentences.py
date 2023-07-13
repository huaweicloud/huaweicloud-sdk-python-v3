# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Sentences:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'end_time': 'int',
        'result': 'FlashScoreResult',
        'start_time': 'int'
    }

    attribute_map = {
        'end_time': 'end_time',
        'result': 'result',
        'start_time': 'start_time'
    }

    def __init__(self, end_time=None, result=None, start_time=None):
        """Sentences

        The model defined in huaweicloud sdk

        :param end_time: 分句结果信息
        :type end_time: int
        :param result: 
        :type result: :class:`huaweicloudsdksis.v1.FlashScoreResult`
        :param start_time: 一句话开始时间，单位毫秒
        :type start_time: int
        """
        
        

        self._end_time = None
        self._result = None
        self._start_time = None
        self.discriminator = None

        if end_time is not None:
            self.end_time = end_time
        if result is not None:
            self.result = result
        if start_time is not None:
            self.start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this Sentences.

        分句结果信息

        :return: The end_time of this Sentences.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this Sentences.

        分句结果信息

        :param end_time: The end_time of this Sentences.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def result(self):
        """Gets the result of this Sentences.

        :return: The result of this Sentences.
        :rtype: :class:`huaweicloudsdksis.v1.FlashScoreResult`
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this Sentences.

        :param result: The result of this Sentences.
        :type result: :class:`huaweicloudsdksis.v1.FlashScoreResult`
        """
        self._result = result

    @property
    def start_time(self):
        """Gets the start_time of this Sentences.

        一句话开始时间，单位毫秒

        :return: The start_time of this Sentences.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this Sentences.

        一句话开始时间，单位毫秒

        :param start_time: The start_time of this Sentences.
        :type start_time: int
        """
        self._start_time = start_time

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
        if not isinstance(other, Sentences):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
