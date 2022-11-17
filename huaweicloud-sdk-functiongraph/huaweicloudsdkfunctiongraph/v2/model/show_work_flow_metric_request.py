# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowWorkFlowMetricRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workflow_urn': 'str',
        'period': 'str',
        'start_time': 'str',
        'end_time': 'str'
    }

    attribute_map = {
        'workflow_urn': 'workflow_urn',
        'period': 'period',
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, workflow_urn=None, period=None, start_time=None, end_time=None):
        """ShowWorkFlowMetricRequest

        The model defined in huaweicloud sdk

        :param workflow_urn: 函数工作流URN, 格式为： urn:fss:&lt;region_id&gt;:&lt;project_id&gt;:workflow:\\&lt;package\\&gt;:&lt;workflow_name&gt;:\\&lt;version\\&gt; 注意： package当前只支持default version当前只支持latest
        :type workflow_urn: str
        :param period: 时间段，单位为分钟
        :type period: str
        :param start_time: 开始时间，精确到ms的时间戳
        :type start_time: str
        :param end_time: 结束时间，精确到ms的时间戳
        :type end_time: str
        """
        
        

        self._workflow_urn = None
        self._period = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        self.workflow_urn = workflow_urn
        if period is not None:
            self.period = period
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def workflow_urn(self):
        """Gets the workflow_urn of this ShowWorkFlowMetricRequest.

        函数工作流URN, 格式为： urn:fss:<region_id>:<project_id>:workflow:\\<package\\>:<workflow_name>:\\<version\\> 注意： package当前只支持default version当前只支持latest

        :return: The workflow_urn of this ShowWorkFlowMetricRequest.
        :rtype: str
        """
        return self._workflow_urn

    @workflow_urn.setter
    def workflow_urn(self, workflow_urn):
        """Sets the workflow_urn of this ShowWorkFlowMetricRequest.

        函数工作流URN, 格式为： urn:fss:<region_id>:<project_id>:workflow:\\<package\\>:<workflow_name>:\\<version\\> 注意： package当前只支持default version当前只支持latest

        :param workflow_urn: The workflow_urn of this ShowWorkFlowMetricRequest.
        :type workflow_urn: str
        """
        self._workflow_urn = workflow_urn

    @property
    def period(self):
        """Gets the period of this ShowWorkFlowMetricRequest.

        时间段，单位为分钟

        :return: The period of this ShowWorkFlowMetricRequest.
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this ShowWorkFlowMetricRequest.

        时间段，单位为分钟

        :param period: The period of this ShowWorkFlowMetricRequest.
        :type period: str
        """
        self._period = period

    @property
    def start_time(self):
        """Gets the start_time of this ShowWorkFlowMetricRequest.

        开始时间，精确到ms的时间戳

        :return: The start_time of this ShowWorkFlowMetricRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ShowWorkFlowMetricRequest.

        开始时间，精确到ms的时间戳

        :param start_time: The start_time of this ShowWorkFlowMetricRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ShowWorkFlowMetricRequest.

        结束时间，精确到ms的时间戳

        :return: The end_time of this ShowWorkFlowMetricRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ShowWorkFlowMetricRequest.

        结束时间，精确到ms的时间戳

        :param end_time: The end_time of this ShowWorkFlowMetricRequest.
        :type end_time: str
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
        if not isinstance(other, ShowWorkFlowMetricRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
