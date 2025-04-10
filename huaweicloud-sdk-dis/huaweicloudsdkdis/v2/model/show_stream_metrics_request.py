# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowStreamMetricsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'stream_name': 'str',
        'label': 'str',
        'label_list': 'str',
        'start_time': 'int',
        'end_time': 'int'
    }

    attribute_map = {
        'stream_name': 'stream_name',
        'label': 'label',
        'label_list': 'label_list',
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, stream_name=None, label=None, label_list=None, start_time=None, end_time=None):
        r"""ShowStreamMetricsRequest

        The model defined in huaweicloud sdk

        :param stream_name: 通道名称。
        :type stream_name: str
        :param label: 通道监控指标。（label与label_list必须二选一，label_list与label同时存在时，以label_list为准）  - total_put_bytes_per_stream：总输入流量（Byte） - total_get_bytes_per_stream：总输出流量（Byte） - total_put_records_per_stream：总输入记录数（个） - total_get_records_per_stream：总输出记录数（个） - total_put_req_latency：上传请求平均处理时间（毫秒） - total_get_req_latency：下载请求平均处理时间（毫秒） - total_put_req_suc_per_stream：上传请求成功次数（个） - total_get_req_suc_per_stream：下载请求成功次数（个） - traffic_control_put：因流控拒绝的上传请求次数 （个） - traffic_control_get：因流控拒绝的下载请求次数 （个）
        :type label: str
        :param label_list: 使用label用逗号拼接组成，用于批量查询多个label的指标。（label与label_list必须二选一，label_list与label同时存在时，以label_list为准）
        :type label_list: str
        :param start_time: 监控开始时间点，10位时间戳。
        :type start_time: int
        :param end_time: 监控结束时间点，10位时间戳。
        :type end_time: int
        """
        
        

        self._stream_name = None
        self._label = None
        self._label_list = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        self.stream_name = stream_name
        if label is not None:
            self.label = label
        if label_list is not None:
            self.label_list = label_list
        self.start_time = start_time
        self.end_time = end_time

    @property
    def stream_name(self):
        r"""Gets the stream_name of this ShowStreamMetricsRequest.

        通道名称。

        :return: The stream_name of this ShowStreamMetricsRequest.
        :rtype: str
        """
        return self._stream_name

    @stream_name.setter
    def stream_name(self, stream_name):
        r"""Sets the stream_name of this ShowStreamMetricsRequest.

        通道名称。

        :param stream_name: The stream_name of this ShowStreamMetricsRequest.
        :type stream_name: str
        """
        self._stream_name = stream_name

    @property
    def label(self):
        r"""Gets the label of this ShowStreamMetricsRequest.

        通道监控指标。（label与label_list必须二选一，label_list与label同时存在时，以label_list为准）  - total_put_bytes_per_stream：总输入流量（Byte） - total_get_bytes_per_stream：总输出流量（Byte） - total_put_records_per_stream：总输入记录数（个） - total_get_records_per_stream：总输出记录数（个） - total_put_req_latency：上传请求平均处理时间（毫秒） - total_get_req_latency：下载请求平均处理时间（毫秒） - total_put_req_suc_per_stream：上传请求成功次数（个） - total_get_req_suc_per_stream：下载请求成功次数（个） - traffic_control_put：因流控拒绝的上传请求次数 （个） - traffic_control_get：因流控拒绝的下载请求次数 （个）

        :return: The label of this ShowStreamMetricsRequest.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        r"""Sets the label of this ShowStreamMetricsRequest.

        通道监控指标。（label与label_list必须二选一，label_list与label同时存在时，以label_list为准）  - total_put_bytes_per_stream：总输入流量（Byte） - total_get_bytes_per_stream：总输出流量（Byte） - total_put_records_per_stream：总输入记录数（个） - total_get_records_per_stream：总输出记录数（个） - total_put_req_latency：上传请求平均处理时间（毫秒） - total_get_req_latency：下载请求平均处理时间（毫秒） - total_put_req_suc_per_stream：上传请求成功次数（个） - total_get_req_suc_per_stream：下载请求成功次数（个） - traffic_control_put：因流控拒绝的上传请求次数 （个） - traffic_control_get：因流控拒绝的下载请求次数 （个）

        :param label: The label of this ShowStreamMetricsRequest.
        :type label: str
        """
        self._label = label

    @property
    def label_list(self):
        r"""Gets the label_list of this ShowStreamMetricsRequest.

        使用label用逗号拼接组成，用于批量查询多个label的指标。（label与label_list必须二选一，label_list与label同时存在时，以label_list为准）

        :return: The label_list of this ShowStreamMetricsRequest.
        :rtype: str
        """
        return self._label_list

    @label_list.setter
    def label_list(self, label_list):
        r"""Sets the label_list of this ShowStreamMetricsRequest.

        使用label用逗号拼接组成，用于批量查询多个label的指标。（label与label_list必须二选一，label_list与label同时存在时，以label_list为准）

        :param label_list: The label_list of this ShowStreamMetricsRequest.
        :type label_list: str
        """
        self._label_list = label_list

    @property
    def start_time(self):
        r"""Gets the start_time of this ShowStreamMetricsRequest.

        监控开始时间点，10位时间戳。

        :return: The start_time of this ShowStreamMetricsRequest.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ShowStreamMetricsRequest.

        监控开始时间点，10位时间戳。

        :param start_time: The start_time of this ShowStreamMetricsRequest.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ShowStreamMetricsRequest.

        监控结束时间点，10位时间戳。

        :return: The end_time of this ShowStreamMetricsRequest.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ShowStreamMetricsRequest.

        监控结束时间点，10位时间戳。

        :param end_time: The end_time of this ShowStreamMetricsRequest.
        :type end_time: int
        """
        self._end_time = end_time

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
        if not isinstance(other, ShowStreamMetricsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
