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
        'eps_id': 'str',
        'eps_name': 'str',
        'log_stream_id': 'str',
        'log_stream_name': 'str',
        'log_group_id': 'str',
        'log_group_name': 'str',
        'keywords': 'str',
        'condition': 'str',
        'number': 'int',
        'search_time_range': 'int',
        'search_time_range_unit': 'str',
        'is_time_range_relative': 'bool'
    }

    attribute_map = {
        'eps_id': 'eps_id',
        'eps_name': 'eps_name',
        'log_stream_id': 'log_stream_id',
        'log_stream_name': 'log_stream_name',
        'log_group_id': 'log_group_id',
        'log_group_name': 'log_group_name',
        'keywords': 'keywords',
        'condition': 'condition',
        'number': 'number',
        'search_time_range': 'search_time_range',
        'search_time_range_unit': 'search_time_range_unit',
        'is_time_range_relative': 'is_time_range_relative'
    }

    def __init__(self, eps_id=None, eps_name=None, log_stream_id=None, log_stream_name=None, log_group_id=None, log_group_name=None, keywords=None, condition=None, number=None, search_time_range=None, search_time_range_unit=None, is_time_range_relative=None):
        """KeywordsRequest - a model defined in huaweicloud sdk"""
        
        

        self._eps_id = None
        self._eps_name = None
        self._log_stream_id = None
        self._log_stream_name = None
        self._log_group_id = None
        self._log_group_name = None
        self._keywords = None
        self._condition = None
        self._number = None
        self._search_time_range = None
        self._search_time_range_unit = None
        self._is_time_range_relative = None
        self.discriminator = None

        if eps_id is not None:
            self.eps_id = eps_id
        if eps_name is not None:
            self.eps_name = eps_name
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
        if is_time_range_relative is not None:
            self.is_time_range_relative = is_time_range_relative

    @property
    def eps_id(self):
        """Gets the eps_id of this KeywordsRequest.

        企业项目id

        :return: The eps_id of this KeywordsRequest.
        :rtype: str
        """
        return self._eps_id

    @eps_id.setter
    def eps_id(self, eps_id):
        """Sets the eps_id of this KeywordsRequest.

        企业项目id

        :param eps_id: The eps_id of this KeywordsRequest.
        :type: str
        """
        self._eps_id = eps_id

    @property
    def eps_name(self):
        """Gets the eps_name of this KeywordsRequest.

        企业项目名称

        :return: The eps_name of this KeywordsRequest.
        :rtype: str
        """
        return self._eps_name

    @eps_name.setter
    def eps_name(self, eps_name):
        """Sets the eps_name of this KeywordsRequest.

        企业项目名称

        :param eps_name: The eps_name of this KeywordsRequest.
        :type: str
        """
        self._eps_name = eps_name

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
        :type: str
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
        :type: str
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
        :type: str
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
        :type: str
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
        :type: str
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
        :type: str
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
        :type: int
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
        :type: int
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
        :type: str
        """
        self._search_time_range_unit = search_time_range_unit

    @property
    def is_time_range_relative(self):
        """Gets the is_time_range_relative of this KeywordsRequest.

        是否发送

        :return: The is_time_range_relative of this KeywordsRequest.
        :rtype: bool
        """
        return self._is_time_range_relative

    @is_time_range_relative.setter
    def is_time_range_relative(self, is_time_range_relative):
        """Sets the is_time_range_relative of this KeywordsRequest.

        是否发送

        :param is_time_range_relative: The is_time_range_relative of this KeywordsRequest.
        :type: bool
        """
        self._is_time_range_relative = is_time_range_relative

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