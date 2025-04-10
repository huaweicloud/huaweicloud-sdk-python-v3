# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExportTopRiskInstancesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'start_at': 'int',
        'end_at': 'int',
        'datastore_type': 'str',
        'num': 'int',
        'x_language': 'str',
        'metric_code': 'str'
    }

    attribute_map = {
        'start_at': 'start_at',
        'end_at': 'end_at',
        'datastore_type': 'datastore_type',
        'num': 'num',
        'x_language': 'X-Language',
        'metric_code': 'metric_code'
    }

    def __init__(self, start_at=None, end_at=None, datastore_type=None, num=None, x_language=None, metric_code=None):
        r"""ExportTopRiskInstancesRequest

        The model defined in huaweicloud sdk

        :param start_at: 开始时间（Unix timestamp），单位：毫秒。
        :type start_at: int
        :param end_at: 结束时间（Unix timestamp），单位：毫秒。
        :type end_at: int
        :param datastore_type: 数据库类型。
        :type datastore_type: str
        :param num: 返回TOP风险实例数量。
        :type num: int
        :param x_language: 请求语言类型。
        :type x_language: str
        :param metric_code: 指标码
        :type metric_code: str
        """
        
        

        self._start_at = None
        self._end_at = None
        self._datastore_type = None
        self._num = None
        self._x_language = None
        self._metric_code = None
        self.discriminator = None

        self.start_at = start_at
        self.end_at = end_at
        self.datastore_type = datastore_type
        if num is not None:
            self.num = num
        if x_language is not None:
            self.x_language = x_language
        if metric_code is not None:
            self.metric_code = metric_code

    @property
    def start_at(self):
        r"""Gets the start_at of this ExportTopRiskInstancesRequest.

        开始时间（Unix timestamp），单位：毫秒。

        :return: The start_at of this ExportTopRiskInstancesRequest.
        :rtype: int
        """
        return self._start_at

    @start_at.setter
    def start_at(self, start_at):
        r"""Sets the start_at of this ExportTopRiskInstancesRequest.

        开始时间（Unix timestamp），单位：毫秒。

        :param start_at: The start_at of this ExportTopRiskInstancesRequest.
        :type start_at: int
        """
        self._start_at = start_at

    @property
    def end_at(self):
        r"""Gets the end_at of this ExportTopRiskInstancesRequest.

        结束时间（Unix timestamp），单位：毫秒。

        :return: The end_at of this ExportTopRiskInstancesRequest.
        :rtype: int
        """
        return self._end_at

    @end_at.setter
    def end_at(self, end_at):
        r"""Sets the end_at of this ExportTopRiskInstancesRequest.

        结束时间（Unix timestamp），单位：毫秒。

        :param end_at: The end_at of this ExportTopRiskInstancesRequest.
        :type end_at: int
        """
        self._end_at = end_at

    @property
    def datastore_type(self):
        r"""Gets the datastore_type of this ExportTopRiskInstancesRequest.

        数据库类型。

        :return: The datastore_type of this ExportTopRiskInstancesRequest.
        :rtype: str
        """
        return self._datastore_type

    @datastore_type.setter
    def datastore_type(self, datastore_type):
        r"""Sets the datastore_type of this ExportTopRiskInstancesRequest.

        数据库类型。

        :param datastore_type: The datastore_type of this ExportTopRiskInstancesRequest.
        :type datastore_type: str
        """
        self._datastore_type = datastore_type

    @property
    def num(self):
        r"""Gets the num of this ExportTopRiskInstancesRequest.

        返回TOP风险实例数量。

        :return: The num of this ExportTopRiskInstancesRequest.
        :rtype: int
        """
        return self._num

    @num.setter
    def num(self, num):
        r"""Sets the num of this ExportTopRiskInstancesRequest.

        返回TOP风险实例数量。

        :param num: The num of this ExportTopRiskInstancesRequest.
        :type num: int
        """
        self._num = num

    @property
    def x_language(self):
        r"""Gets the x_language of this ExportTopRiskInstancesRequest.

        请求语言类型。

        :return: The x_language of this ExportTopRiskInstancesRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ExportTopRiskInstancesRequest.

        请求语言类型。

        :param x_language: The x_language of this ExportTopRiskInstancesRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def metric_code(self):
        r"""Gets the metric_code of this ExportTopRiskInstancesRequest.

        指标码

        :return: The metric_code of this ExportTopRiskInstancesRequest.
        :rtype: str
        """
        return self._metric_code

    @metric_code.setter
    def metric_code(self, metric_code):
        r"""Sets the metric_code of this ExportTopRiskInstancesRequest.

        指标码

        :param metric_code: The metric_code of this ExportTopRiskInstancesRequest.
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
        if not isinstance(other, ExportTopRiskInstancesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
