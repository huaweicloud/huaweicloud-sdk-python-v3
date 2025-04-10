# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowMetricResultResponseBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'metric_id': 'str',
        'result': 'ShowMetricResultResponseBodyResult',
        'metric_format': 'list[MetricFormat]',
        'log_msg': 'str',
        'status': 'str'
    }

    attribute_map = {
        'metric_id': 'metric_id',
        'result': 'result',
        'metric_format': 'metric_format',
        'log_msg': 'log_msg',
        'status': 'status'
    }

    def __init__(self, metric_id=None, result=None, metric_format=None, log_msg=None, status=None):
        r"""ShowMetricResultResponseBody

        The model defined in huaweicloud sdk

        :param metric_id: 指标ID
        :type metric_id: str
        :param result: 
        :type result: :class:`huaweicloudsdksecmaster.v2.ShowMetricResultResponseBodyResult`
        :param metric_format: 指标显示格式，根据不同指标固定返回。
        :type metric_format: list[:class:`huaweicloudsdksecmaster.v2.MetricFormat`]
        :param log_msg: 结果日志信息
        :type log_msg: str
        :param status: 查询结果状态，SUCCESS：查询成功，FAILED：查询失败，FALLBACK：使用默认值
        :type status: str
        """
        
        

        self._metric_id = None
        self._result = None
        self._metric_format = None
        self._log_msg = None
        self._status = None
        self.discriminator = None

        self.metric_id = metric_id
        self.result = result
        if metric_format is not None:
            self.metric_format = metric_format
        if log_msg is not None:
            self.log_msg = log_msg
        if status is not None:
            self.status = status

    @property
    def metric_id(self):
        r"""Gets the metric_id of this ShowMetricResultResponseBody.

        指标ID

        :return: The metric_id of this ShowMetricResultResponseBody.
        :rtype: str
        """
        return self._metric_id

    @metric_id.setter
    def metric_id(self, metric_id):
        r"""Sets the metric_id of this ShowMetricResultResponseBody.

        指标ID

        :param metric_id: The metric_id of this ShowMetricResultResponseBody.
        :type metric_id: str
        """
        self._metric_id = metric_id

    @property
    def result(self):
        r"""Gets the result of this ShowMetricResultResponseBody.

        :return: The result of this ShowMetricResultResponseBody.
        :rtype: :class:`huaweicloudsdksecmaster.v2.ShowMetricResultResponseBodyResult`
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this ShowMetricResultResponseBody.

        :param result: The result of this ShowMetricResultResponseBody.
        :type result: :class:`huaweicloudsdksecmaster.v2.ShowMetricResultResponseBodyResult`
        """
        self._result = result

    @property
    def metric_format(self):
        r"""Gets the metric_format of this ShowMetricResultResponseBody.

        指标显示格式，根据不同指标固定返回。

        :return: The metric_format of this ShowMetricResultResponseBody.
        :rtype: list[:class:`huaweicloudsdksecmaster.v2.MetricFormat`]
        """
        return self._metric_format

    @metric_format.setter
    def metric_format(self, metric_format):
        r"""Sets the metric_format of this ShowMetricResultResponseBody.

        指标显示格式，根据不同指标固定返回。

        :param metric_format: The metric_format of this ShowMetricResultResponseBody.
        :type metric_format: list[:class:`huaweicloudsdksecmaster.v2.MetricFormat`]
        """
        self._metric_format = metric_format

    @property
    def log_msg(self):
        r"""Gets the log_msg of this ShowMetricResultResponseBody.

        结果日志信息

        :return: The log_msg of this ShowMetricResultResponseBody.
        :rtype: str
        """
        return self._log_msg

    @log_msg.setter
    def log_msg(self, log_msg):
        r"""Sets the log_msg of this ShowMetricResultResponseBody.

        结果日志信息

        :param log_msg: The log_msg of this ShowMetricResultResponseBody.
        :type log_msg: str
        """
        self._log_msg = log_msg

    @property
    def status(self):
        r"""Gets the status of this ShowMetricResultResponseBody.

        查询结果状态，SUCCESS：查询成功，FAILED：查询失败，FALLBACK：使用默认值

        :return: The status of this ShowMetricResultResponseBody.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowMetricResultResponseBody.

        查询结果状态，SUCCESS：查询成功，FAILED：查询失败，FALLBACK：使用默认值

        :param status: The status of this ShowMetricResultResponseBody.
        :type status: str
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
        if not isinstance(other, ShowMetricResultResponseBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
