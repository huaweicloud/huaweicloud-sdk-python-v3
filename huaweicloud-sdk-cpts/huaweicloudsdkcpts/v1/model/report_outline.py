# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReportOutline:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'core_index': 'CoreIndex',
        'exception_response_sum': 'ExceptionResponseSum',
        'network_traffic': 'NetworkTraffic',
        'response_code_sum': 'ResponseCodeSum',
        'task_basic_attribute': 'TaskBasicAttribute',
        'task_basic_execution_data': 'TaskBasicExecutionData',
        'response_code_details': 'list[object]',
        'sla_statistic': 'object',
        'streaming_media': 'object'
    }

    attribute_map = {
        'core_index': 'core_index',
        'exception_response_sum': 'exception_response_sum',
        'network_traffic': 'network_traffic',
        'response_code_sum': 'response_code_sum',
        'task_basic_attribute': 'task_basic_attribute',
        'task_basic_execution_data': 'task_basic_execution_data',
        'response_code_details': 'response_code_details',
        'sla_statistic': 'sla_statistic',
        'streaming_media': 'streaming_media'
    }

    def __init__(self, core_index=None, exception_response_sum=None, network_traffic=None, response_code_sum=None, task_basic_attribute=None, task_basic_execution_data=None, response_code_details=None, sla_statistic=None, streaming_media=None):
        r"""ReportOutline

        The model defined in huaweicloud sdk

        :param core_index: 
        :type core_index: :class:`huaweicloudsdkcpts.v1.CoreIndex`
        :param exception_response_sum: 
        :type exception_response_sum: :class:`huaweicloudsdkcpts.v1.ExceptionResponseSum`
        :param network_traffic: 
        :type network_traffic: :class:`huaweicloudsdkcpts.v1.NetworkTraffic`
        :param response_code_sum: 
        :type response_code_sum: :class:`huaweicloudsdkcpts.v1.ResponseCodeSum`
        :param task_basic_attribute: 
        :type task_basic_attribute: :class:`huaweicloudsdkcpts.v1.TaskBasicAttribute`
        :param task_basic_execution_data: 
        :type task_basic_execution_data: :class:`huaweicloudsdkcpts.v1.TaskBasicExecutionData`
        :param response_code_details: 响应码详细信息
        :type response_code_details: list[object]
        :param sla_statistic: SLA数据
        :type sla_statistic: object
        :param streaming_media: 流媒体相关数据
        :type streaming_media: object
        """
        
        

        self._core_index = None
        self._exception_response_sum = None
        self._network_traffic = None
        self._response_code_sum = None
        self._task_basic_attribute = None
        self._task_basic_execution_data = None
        self._response_code_details = None
        self._sla_statistic = None
        self._streaming_media = None
        self.discriminator = None

        if core_index is not None:
            self.core_index = core_index
        if exception_response_sum is not None:
            self.exception_response_sum = exception_response_sum
        if network_traffic is not None:
            self.network_traffic = network_traffic
        if response_code_sum is not None:
            self.response_code_sum = response_code_sum
        if task_basic_attribute is not None:
            self.task_basic_attribute = task_basic_attribute
        if task_basic_execution_data is not None:
            self.task_basic_execution_data = task_basic_execution_data
        if response_code_details is not None:
            self.response_code_details = response_code_details
        if sla_statistic is not None:
            self.sla_statistic = sla_statistic
        if streaming_media is not None:
            self.streaming_media = streaming_media

    @property
    def core_index(self):
        r"""Gets the core_index of this ReportOutline.

        :return: The core_index of this ReportOutline.
        :rtype: :class:`huaweicloudsdkcpts.v1.CoreIndex`
        """
        return self._core_index

    @core_index.setter
    def core_index(self, core_index):
        r"""Sets the core_index of this ReportOutline.

        :param core_index: The core_index of this ReportOutline.
        :type core_index: :class:`huaweicloudsdkcpts.v1.CoreIndex`
        """
        self._core_index = core_index

    @property
    def exception_response_sum(self):
        r"""Gets the exception_response_sum of this ReportOutline.

        :return: The exception_response_sum of this ReportOutline.
        :rtype: :class:`huaweicloudsdkcpts.v1.ExceptionResponseSum`
        """
        return self._exception_response_sum

    @exception_response_sum.setter
    def exception_response_sum(self, exception_response_sum):
        r"""Sets the exception_response_sum of this ReportOutline.

        :param exception_response_sum: The exception_response_sum of this ReportOutline.
        :type exception_response_sum: :class:`huaweicloudsdkcpts.v1.ExceptionResponseSum`
        """
        self._exception_response_sum = exception_response_sum

    @property
    def network_traffic(self):
        r"""Gets the network_traffic of this ReportOutline.

        :return: The network_traffic of this ReportOutline.
        :rtype: :class:`huaweicloudsdkcpts.v1.NetworkTraffic`
        """
        return self._network_traffic

    @network_traffic.setter
    def network_traffic(self, network_traffic):
        r"""Sets the network_traffic of this ReportOutline.

        :param network_traffic: The network_traffic of this ReportOutline.
        :type network_traffic: :class:`huaweicloudsdkcpts.v1.NetworkTraffic`
        """
        self._network_traffic = network_traffic

    @property
    def response_code_sum(self):
        r"""Gets the response_code_sum of this ReportOutline.

        :return: The response_code_sum of this ReportOutline.
        :rtype: :class:`huaweicloudsdkcpts.v1.ResponseCodeSum`
        """
        return self._response_code_sum

    @response_code_sum.setter
    def response_code_sum(self, response_code_sum):
        r"""Sets the response_code_sum of this ReportOutline.

        :param response_code_sum: The response_code_sum of this ReportOutline.
        :type response_code_sum: :class:`huaweicloudsdkcpts.v1.ResponseCodeSum`
        """
        self._response_code_sum = response_code_sum

    @property
    def task_basic_attribute(self):
        r"""Gets the task_basic_attribute of this ReportOutline.

        :return: The task_basic_attribute of this ReportOutline.
        :rtype: :class:`huaweicloudsdkcpts.v1.TaskBasicAttribute`
        """
        return self._task_basic_attribute

    @task_basic_attribute.setter
    def task_basic_attribute(self, task_basic_attribute):
        r"""Sets the task_basic_attribute of this ReportOutline.

        :param task_basic_attribute: The task_basic_attribute of this ReportOutline.
        :type task_basic_attribute: :class:`huaweicloudsdkcpts.v1.TaskBasicAttribute`
        """
        self._task_basic_attribute = task_basic_attribute

    @property
    def task_basic_execution_data(self):
        r"""Gets the task_basic_execution_data of this ReportOutline.

        :return: The task_basic_execution_data of this ReportOutline.
        :rtype: :class:`huaweicloudsdkcpts.v1.TaskBasicExecutionData`
        """
        return self._task_basic_execution_data

    @task_basic_execution_data.setter
    def task_basic_execution_data(self, task_basic_execution_data):
        r"""Sets the task_basic_execution_data of this ReportOutline.

        :param task_basic_execution_data: The task_basic_execution_data of this ReportOutline.
        :type task_basic_execution_data: :class:`huaweicloudsdkcpts.v1.TaskBasicExecutionData`
        """
        self._task_basic_execution_data = task_basic_execution_data

    @property
    def response_code_details(self):
        r"""Gets the response_code_details of this ReportOutline.

        响应码详细信息

        :return: The response_code_details of this ReportOutline.
        :rtype: list[object]
        """
        return self._response_code_details

    @response_code_details.setter
    def response_code_details(self, response_code_details):
        r"""Sets the response_code_details of this ReportOutline.

        响应码详细信息

        :param response_code_details: The response_code_details of this ReportOutline.
        :type response_code_details: list[object]
        """
        self._response_code_details = response_code_details

    @property
    def sla_statistic(self):
        r"""Gets the sla_statistic of this ReportOutline.

        SLA数据

        :return: The sla_statistic of this ReportOutline.
        :rtype: object
        """
        return self._sla_statistic

    @sla_statistic.setter
    def sla_statistic(self, sla_statistic):
        r"""Sets the sla_statistic of this ReportOutline.

        SLA数据

        :param sla_statistic: The sla_statistic of this ReportOutline.
        :type sla_statistic: object
        """
        self._sla_statistic = sla_statistic

    @property
    def streaming_media(self):
        r"""Gets the streaming_media of this ReportOutline.

        流媒体相关数据

        :return: The streaming_media of this ReportOutline.
        :rtype: object
        """
        return self._streaming_media

    @streaming_media.setter
    def streaming_media(self, streaming_media):
        r"""Sets the streaming_media of this ReportOutline.

        流媒体相关数据

        :param streaming_media: The streaming_media of this ReportOutline.
        :type streaming_media: object
        """
        self._streaming_media = streaming_media

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
        if not isinstance(other, ReportOutline):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
