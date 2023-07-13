# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PreviewJobResultRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_id': 'str',
        'queue_name': 'str'
    }

    attribute_map = {
        'job_id': 'job_id',
        'queue_name': 'queue-name'
    }

    def __init__(self, job_id=None, queue_name=None):
        """PreviewJobResultRequest

        The model defined in huaweicloud sdk

        :param job_id: 作业ID。
        :type job_id: str
        :param queue_name: 指定获取作业结果的执行队列名称。若不指定则使用默认的系统队列
        :type queue_name: str
        """
        
        

        self._job_id = None
        self._queue_name = None
        self.discriminator = None

        self.job_id = job_id
        if queue_name is not None:
            self.queue_name = queue_name

    @property
    def job_id(self):
        """Gets the job_id of this PreviewJobResultRequest.

        作业ID。

        :return: The job_id of this PreviewJobResultRequest.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this PreviewJobResultRequest.

        作业ID。

        :param job_id: The job_id of this PreviewJobResultRequest.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def queue_name(self):
        """Gets the queue_name of this PreviewJobResultRequest.

        指定获取作业结果的执行队列名称。若不指定则使用默认的系统队列

        :return: The queue_name of this PreviewJobResultRequest.
        :rtype: str
        """
        return self._queue_name

    @queue_name.setter
    def queue_name(self, queue_name):
        """Sets the queue_name of this PreviewJobResultRequest.

        指定获取作业结果的执行队列名称。若不指定则使用默认的系统队列

        :param queue_name: The queue_name of this PreviewJobResultRequest.
        :type queue_name: str
        """
        self._queue_name = queue_name

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
        if not isinstance(other, PreviewJobResultRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
