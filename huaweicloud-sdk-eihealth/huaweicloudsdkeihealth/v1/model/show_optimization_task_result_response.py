# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowOptimizationTaskResultResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'AsyncTaskStatus',
        'task_data': 'OptimizationTaskData',
        'result': 'OptimizationResult'
    }

    attribute_map = {
        'status': 'status',
        'task_data': 'task_data',
        'result': 'result'
    }

    def __init__(self, status=None, task_data=None, result=None):
        r"""ShowOptimizationTaskResultResponse

        The model defined in huaweicloud sdk

        :param status: 
        :type status: :class:`huaweicloudsdkeihealth.v1.AsyncTaskStatus`
        :param task_data: 
        :type task_data: :class:`huaweicloudsdkeihealth.v1.OptimizationTaskData`
        :param result: 
        :type result: :class:`huaweicloudsdkeihealth.v1.OptimizationResult`
        """
        
        super(ShowOptimizationTaskResultResponse, self).__init__()

        self._status = None
        self._task_data = None
        self._result = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if task_data is not None:
            self.task_data = task_data
        if result is not None:
            self.result = result

    @property
    def status(self):
        r"""Gets the status of this ShowOptimizationTaskResultResponse.

        :return: The status of this ShowOptimizationTaskResultResponse.
        :rtype: :class:`huaweicloudsdkeihealth.v1.AsyncTaskStatus`
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowOptimizationTaskResultResponse.

        :param status: The status of this ShowOptimizationTaskResultResponse.
        :type status: :class:`huaweicloudsdkeihealth.v1.AsyncTaskStatus`
        """
        self._status = status

    @property
    def task_data(self):
        r"""Gets the task_data of this ShowOptimizationTaskResultResponse.

        :return: The task_data of this ShowOptimizationTaskResultResponse.
        :rtype: :class:`huaweicloudsdkeihealth.v1.OptimizationTaskData`
        """
        return self._task_data

    @task_data.setter
    def task_data(self, task_data):
        r"""Sets the task_data of this ShowOptimizationTaskResultResponse.

        :param task_data: The task_data of this ShowOptimizationTaskResultResponse.
        :type task_data: :class:`huaweicloudsdkeihealth.v1.OptimizationTaskData`
        """
        self._task_data = task_data

    @property
    def result(self):
        r"""Gets the result of this ShowOptimizationTaskResultResponse.

        :return: The result of this ShowOptimizationTaskResultResponse.
        :rtype: :class:`huaweicloudsdkeihealth.v1.OptimizationResult`
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this ShowOptimizationTaskResultResponse.

        :param result: The result of this ShowOptimizationTaskResultResponse.
        :type result: :class:`huaweicloudsdkeihealth.v1.OptimizationResult`
        """
        self._result = result

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
        if not isinstance(other, ShowOptimizationTaskResultResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
