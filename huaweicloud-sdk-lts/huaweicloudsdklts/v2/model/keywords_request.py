# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class KeywordsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'log_stream_id': 'str',
        'log_stream_name': 'str',
        'log_group_id': 'str',
        'log_group_name': 'str',
        'keywords': 'str',
        'condition': 'str',
        'number': 'int',
        'search_time_range': 'int',
        'search_time_range_unit': 'str'
    }

    attribute_map = {
        'log_stream_id': 'log_stream_id',
        'log_stream_name': 'log_stream_name',
        'log_group_id': 'log_group_id',
        'log_group_name': 'log_group_name',
        'keywords': 'keywords',
        'condition': 'condition',
        'number': 'number',
        'search_time_range': 'search_time_range',
        'search_time_range_unit': 'search_time_range_unit'
    }

    def __init__(self, log_stream_id=None, log_stream_name=None, log_group_id=None, log_group_name=None, keywords=None, condition=None, number=None, search_time_range=None, search_time_range_unit=None):
        """KeywordsRequest

        The model defined in huaweicloud sdk

        :param log_stream_id: 日志流id
        :type log_stream_id: str
        :param log_stream_name: 日志流名称
        :type log_stream_name: str
        :param log_group_id: 日志组id
        :type log_group_id: str
        :param log_group_name: 日志组名称
        :type log_group_name: str
        :param keywords: 关键词
        :type keywords: str
        :param condition: 条件
        :type condition: str
        :param number: 行数
        :type number: int
        :param search_time_range: 查询执行任务时最近数据的时间范围，最大值为60
        :type search_time_range: int
        :param search_time_range_unit: 查询时间单位
        :type search_time_range_unit: str
        """
        
        

        self._log_stream_id = None
        self._log_stream_name = None
        self._log_group_id = None
        self._log_group_name = None
        self._keywords = None
        self._condition = None
        self._number = None
        self._search_time_range = None
        self._search_time_range_unit = None
        self.discriminator = None

        self.log_stream_id = log_stream_id
        if log_stream_name is not None:
            self.log_stream_name = log_stream_name
        self.log_group_id = log_group_id
        if log_group_name is not None:
            self.log_group_name = log_group_name
        self.keywords = keywords
        self.condition = condition
        self.number = number
        self.search_time_range = search_time_range
        self.search_time_range_unit = search_time_range_unit

    @property
    def log_stream_id(self):
        """Gets the log_stream_id of this KeywordsRequest.

        日志流id

        :return: The log_stream_id of this KeywordsRequest.
        :rtype: str
        """
        return self._log_stream_id

    @log_stream_id.setter
    def log_stream_id(self, log_stream_id):
        """Sets the log_stream_id of this KeywordsRequest.

        日志流id

        :param log_stream_id: The log_stream_id of this KeywordsRequest.
        :type log_stream_id: str
        """
        self._log_stream_id = log_stream_id

    @property
    def log_stream_name(self):
        """Gets the log_stream_name of this KeywordsRequest.

        日志流名称

        :return: The log_stream_name of this KeywordsRequest.
        :rtype: str
        """
        return self._log_stream_name

    @log_stream_name.setter
    def log_stream_name(self, log_stream_name):
        """Sets the log_stream_name of this KeywordsRequest.

        日志流名称

        :param log_stream_name: The log_stream_name of this KeywordsRequest.
        :type log_stream_name: str
        """
        self._log_stream_name = log_stream_name

    @property
    def log_group_id(self):
        """Gets the log_group_id of this KeywordsRequest.

        日志组id

        :return: The log_group_id of this KeywordsRequest.
        :rtype: str
        """
        return self._log_group_id

    @log_group_id.setter
    def log_group_id(self, log_group_id):
        """Sets the log_group_id of this KeywordsRequest.

        日志组id

        :param log_group_id: The log_group_id of this KeywordsRequest.
        :type log_group_id: str
        """
        self._log_group_id = log_group_id

    @property
    def log_group_name(self):
        """Gets the log_group_name of this KeywordsRequest.

        日志组名称

        :return: The log_group_name of this KeywordsRequest.
        :rtype: str
        """
        return self._log_group_name

    @log_group_name.setter
    def log_group_name(self, log_group_name):
        """Sets the log_group_name of this KeywordsRequest.

        日志组名称

        :param log_group_name: The log_group_name of this KeywordsRequest.
        :type log_group_name: str
        """
        self._log_group_name = log_group_name

    @property
    def keywords(self):
        """Gets the keywords of this KeywordsRequest.

        关键词

        :return: The keywords of this KeywordsRequest.
        :rtype: str
        """
        return self._keywords

    @keywords.setter
    def keywords(self, keywords):
        """Sets the keywords of this KeywordsRequest.

        关键词

        :param keywords: The keywords of this KeywordsRequest.
        :type keywords: str
        """
        self._keywords = keywords

    @property
    def condition(self):
        """Gets the condition of this KeywordsRequest.

        条件

        :return: The condition of this KeywordsRequest.
        :rtype: str
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """Sets the condition of this KeywordsRequest.

        条件

        :param condition: The condition of this KeywordsRequest.
        :type condition: str
        """
        self._condition = condition

    @property
    def number(self):
        """Gets the number of this KeywordsRequest.

        行数

        :return: The number of this KeywordsRequest.
        :rtype: int
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this KeywordsRequest.

        行数

        :param number: The number of this KeywordsRequest.
        :type number: int
        """
        self._number = number

    @property
    def search_time_range(self):
        """Gets the search_time_range of this KeywordsRequest.

        查询执行任务时最近数据的时间范围，最大值为60

        :return: The search_time_range of this KeywordsRequest.
        :rtype: int
        """
        return self._search_time_range

    @search_time_range.setter
    def search_time_range(self, search_time_range):
        """Sets the search_time_range of this KeywordsRequest.

        查询执行任务时最近数据的时间范围，最大值为60

        :param search_time_range: The search_time_range of this KeywordsRequest.
        :type search_time_range: int
        """
        self._search_time_range = search_time_range

    @property
    def search_time_range_unit(self):
        """Gets the search_time_range_unit of this KeywordsRequest.

        查询时间单位

        :return: The search_time_range_unit of this KeywordsRequest.
        :rtype: str
        """
        return self._search_time_range_unit

    @search_time_range_unit.setter
    def search_time_range_unit(self, search_time_range_unit):
        """Sets the search_time_range_unit of this KeywordsRequest.

        查询时间单位

        :param search_time_range_unit: The search_time_range_unit of this KeywordsRequest.
        :type search_time_range_unit: str
        """
        self._search_time_range_unit = search_time_range_unit

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
        if not isinstance(other, KeywordsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
