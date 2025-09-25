# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExecutionTimeDetailsInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_time': 'ResourceTime',
        'kernel_time': 'KernelTime',
        'kernel_execution_time': 'KernelExecutionTime',
        'wait_event_time': 'WaitEventTime'
    }

    attribute_map = {
        'resource_time': 'resource_time',
        'kernel_time': 'kernel_time',
        'kernel_execution_time': 'kernel_execution_time',
        'wait_event_time': 'wait_event_time'
    }

    def __init__(self, resource_time=None, kernel_time=None, kernel_execution_time=None, wait_event_time=None):
        r"""ExecutionTimeDetailsInfo

        The model defined in huaweicloud sdk

        :param resource_time: 
        :type resource_time: :class:`huaweicloudsdkgaussdbforopengauss.v3.ResourceTime`
        :param kernel_time: 
        :type kernel_time: :class:`huaweicloudsdkgaussdbforopengauss.v3.KernelTime`
        :param kernel_execution_time: 
        :type kernel_execution_time: :class:`huaweicloudsdkgaussdbforopengauss.v3.KernelExecutionTime`
        :param wait_event_time: 
        :type wait_event_time: :class:`huaweicloudsdkgaussdbforopengauss.v3.WaitEventTime`
        """
        
        

        self._resource_time = None
        self._kernel_time = None
        self._kernel_execution_time = None
        self._wait_event_time = None
        self.discriminator = None

        self.resource_time = resource_time
        self.kernel_time = kernel_time
        if kernel_execution_time is not None:
            self.kernel_execution_time = kernel_execution_time
        self.wait_event_time = wait_event_time

    @property
    def resource_time(self):
        r"""Gets the resource_time of this ExecutionTimeDetailsInfo.

        :return: The resource_time of this ExecutionTimeDetailsInfo.
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.ResourceTime`
        """
        return self._resource_time

    @resource_time.setter
    def resource_time(self, resource_time):
        r"""Sets the resource_time of this ExecutionTimeDetailsInfo.

        :param resource_time: The resource_time of this ExecutionTimeDetailsInfo.
        :type resource_time: :class:`huaweicloudsdkgaussdbforopengauss.v3.ResourceTime`
        """
        self._resource_time = resource_time

    @property
    def kernel_time(self):
        r"""Gets the kernel_time of this ExecutionTimeDetailsInfo.

        :return: The kernel_time of this ExecutionTimeDetailsInfo.
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.KernelTime`
        """
        return self._kernel_time

    @kernel_time.setter
    def kernel_time(self, kernel_time):
        r"""Sets the kernel_time of this ExecutionTimeDetailsInfo.

        :param kernel_time: The kernel_time of this ExecutionTimeDetailsInfo.
        :type kernel_time: :class:`huaweicloudsdkgaussdbforopengauss.v3.KernelTime`
        """
        self._kernel_time = kernel_time

    @property
    def kernel_execution_time(self):
        r"""Gets the kernel_execution_time of this ExecutionTimeDetailsInfo.

        :return: The kernel_execution_time of this ExecutionTimeDetailsInfo.
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.KernelExecutionTime`
        """
        return self._kernel_execution_time

    @kernel_execution_time.setter
    def kernel_execution_time(self, kernel_execution_time):
        r"""Sets the kernel_execution_time of this ExecutionTimeDetailsInfo.

        :param kernel_execution_time: The kernel_execution_time of this ExecutionTimeDetailsInfo.
        :type kernel_execution_time: :class:`huaweicloudsdkgaussdbforopengauss.v3.KernelExecutionTime`
        """
        self._kernel_execution_time = kernel_execution_time

    @property
    def wait_event_time(self):
        r"""Gets the wait_event_time of this ExecutionTimeDetailsInfo.

        :return: The wait_event_time of this ExecutionTimeDetailsInfo.
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.WaitEventTime`
        """
        return self._wait_event_time

    @wait_event_time.setter
    def wait_event_time(self, wait_event_time):
        r"""Sets the wait_event_time of this ExecutionTimeDetailsInfo.

        :param wait_event_time: The wait_event_time of this ExecutionTimeDetailsInfo.
        :type wait_event_time: :class:`huaweicloudsdkgaussdbforopengauss.v3.WaitEventTime`
        """
        self._wait_event_time = wait_event_time

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
        if not isinstance(other, ExecutionTimeDetailsInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
