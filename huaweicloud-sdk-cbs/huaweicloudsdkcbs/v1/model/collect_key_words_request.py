# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CollectKeyWordsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'qabot_id': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'top': 'int'
    }

    attribute_map = {
        'qabot_id': 'qabot_id',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'top': 'top'
    }

    def __init__(self, qabot_id=None, start_time=None, end_time=None, top=None):
        """CollectKeyWordsRequest

        The model defined in huaweicloud sdk

        :param qabot_id: qabot编号，UUID格式。
        :type qabot_id: str
        :param start_time: 查询的起始时间，long，UTC时间，默认值为0。
        :type start_time: str
        :param end_time: 查询的结束时间，long，UTC时间，默认值为当前时间的毫秒数。
        :type end_time: str
        :param top: 关键词最多显示的个数，默认值为10，取值范围0-50。
        :type top: int
        """
        
        

        self._qabot_id = None
        self._start_time = None
        self._end_time = None
        self._top = None
        self.discriminator = None

        self.qabot_id = qabot_id
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if top is not None:
            self.top = top

    @property
    def qabot_id(self):
        """Gets the qabot_id of this CollectKeyWordsRequest.

        qabot编号，UUID格式。

        :return: The qabot_id of this CollectKeyWordsRequest.
        :rtype: str
        """
        return self._qabot_id

    @qabot_id.setter
    def qabot_id(self, qabot_id):
        """Sets the qabot_id of this CollectKeyWordsRequest.

        qabot编号，UUID格式。

        :param qabot_id: The qabot_id of this CollectKeyWordsRequest.
        :type qabot_id: str
        """
        self._qabot_id = qabot_id

    @property
    def start_time(self):
        """Gets the start_time of this CollectKeyWordsRequest.

        查询的起始时间，long，UTC时间，默认值为0。

        :return: The start_time of this CollectKeyWordsRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this CollectKeyWordsRequest.

        查询的起始时间，long，UTC时间，默认值为0。

        :param start_time: The start_time of this CollectKeyWordsRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this CollectKeyWordsRequest.

        查询的结束时间，long，UTC时间，默认值为当前时间的毫秒数。

        :return: The end_time of this CollectKeyWordsRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this CollectKeyWordsRequest.

        查询的结束时间，long，UTC时间，默认值为当前时间的毫秒数。

        :param end_time: The end_time of this CollectKeyWordsRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def top(self):
        """Gets the top of this CollectKeyWordsRequest.

        关键词最多显示的个数，默认值为10，取值范围0-50。

        :return: The top of this CollectKeyWordsRequest.
        :rtype: int
        """
        return self._top

    @top.setter
    def top(self, top):
        """Sets the top of this CollectKeyWordsRequest.

        关键词最多显示的个数，默认值为10，取值范围0-50。

        :param top: The top of this CollectKeyWordsRequest.
        :type top: int
        """
        self._top = top

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
        if not isinstance(other, CollectKeyWordsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
