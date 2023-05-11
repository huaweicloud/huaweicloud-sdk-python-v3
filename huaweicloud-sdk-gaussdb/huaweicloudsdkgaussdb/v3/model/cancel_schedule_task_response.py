# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CancelScheduleTaskResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_ids': 'list[str]'
    }

    attribute_map = {
        'job_ids': 'job_ids'
    }

    def __init__(self, job_ids=None):
        """CancelScheduleTaskResponse

        The model defined in huaweicloud sdk

        :param job_ids: 任务ID，表示成功取消定时调度任务的ID。
        :type job_ids: list[str]
        """
        
        super(CancelScheduleTaskResponse, self).__init__()

        self._job_ids = None
        self.discriminator = None

        if job_ids is not None:
            self.job_ids = job_ids

    @property
    def job_ids(self):
        """Gets the job_ids of this CancelScheduleTaskResponse.

        任务ID，表示成功取消定时调度任务的ID。

        :return: The job_ids of this CancelScheduleTaskResponse.
        :rtype: list[str]
        """
        return self._job_ids

    @job_ids.setter
    def job_ids(self, job_ids):
        """Sets the job_ids of this CancelScheduleTaskResponse.

        任务ID，表示成功取消定时调度任务的ID。

        :param job_ids: The job_ids of this CancelScheduleTaskResponse.
        :type job_ids: list[str]
        """
        self._job_ids = job_ids

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
        if not isinstance(other, CancelScheduleTaskResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
