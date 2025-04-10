# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRiskTrendRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_language': 'str',
        'datastore_type': 'str',
        'start_at': 'int',
        'end_at': 'int',
        'metric_code': 'str'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'datastore_type': 'datastore_type',
        'start_at': 'start_at',
        'end_at': 'end_at',
        'metric_code': 'metric_code'
    }

    def __init__(self, x_language=None, datastore_type=None, start_at=None, end_at=None, metric_code=None):
        r"""ListRiskTrendRequest

        The model defined in huaweicloud sdk

        :param x_language: 语言
        :type x_language: str
        :param datastore_type: 数据库类型
        :type datastore_type: str
        :param start_at: 开始时间
        :type start_at: int
        :param end_at: 结束时间
        :type end_at: int
        :param metric_code: 指标码
        :type metric_code: str
        """
        
        

        self._x_language = None
        self._datastore_type = None
        self._start_at = None
        self._end_at = None
        self._metric_code = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        self.datastore_type = datastore_type
        self.start_at = start_at
        self.end_at = end_at
        self.metric_code = metric_code

    @property
    def x_language(self):
        r"""Gets the x_language of this ListRiskTrendRequest.

        语言

        :return: The x_language of this ListRiskTrendRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ListRiskTrendRequest.

        语言

        :param x_language: The x_language of this ListRiskTrendRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def datastore_type(self):
        r"""Gets the datastore_type of this ListRiskTrendRequest.

        数据库类型

        :return: The datastore_type of this ListRiskTrendRequest.
        :rtype: str
        """
        return self._datastore_type

    @datastore_type.setter
    def datastore_type(self, datastore_type):
        r"""Sets the datastore_type of this ListRiskTrendRequest.

        数据库类型

        :param datastore_type: The datastore_type of this ListRiskTrendRequest.
        :type datastore_type: str
        """
        self._datastore_type = datastore_type

    @property
    def start_at(self):
        r"""Gets the start_at of this ListRiskTrendRequest.

        开始时间

        :return: The start_at of this ListRiskTrendRequest.
        :rtype: int
        """
        return self._start_at

    @start_at.setter
    def start_at(self, start_at):
        r"""Sets the start_at of this ListRiskTrendRequest.

        开始时间

        :param start_at: The start_at of this ListRiskTrendRequest.
        :type start_at: int
        """
        self._start_at = start_at

    @property
    def end_at(self):
        r"""Gets the end_at of this ListRiskTrendRequest.

        结束时间

        :return: The end_at of this ListRiskTrendRequest.
        :rtype: int
        """
        return self._end_at

    @end_at.setter
    def end_at(self, end_at):
        r"""Sets the end_at of this ListRiskTrendRequest.

        结束时间

        :param end_at: The end_at of this ListRiskTrendRequest.
        :type end_at: int
        """
        self._end_at = end_at

    @property
    def metric_code(self):
        r"""Gets the metric_code of this ListRiskTrendRequest.

        指标码

        :return: The metric_code of this ListRiskTrendRequest.
        :rtype: str
        """
        return self._metric_code

    @metric_code.setter
    def metric_code(self, metric_code):
        r"""Sets the metric_code of this ListRiskTrendRequest.

        指标码

        :param metric_code: The metric_code of this ListRiskTrendRequest.
        :type metric_code: str
        """
        self._metric_code = metric_code

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
        if not isinstance(other, ListRiskTrendRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
