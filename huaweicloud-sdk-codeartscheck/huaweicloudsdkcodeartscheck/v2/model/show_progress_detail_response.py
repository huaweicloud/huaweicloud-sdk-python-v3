# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowProgressDetailResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_status': 'int',
        'progress': 'ProgressDetailV2'
    }

    attribute_map = {
        'task_status': 'task_status',
        'progress': 'progress'
    }

    def __init__(self, task_status=None, progress=None):
        """ShowProgressDetailResponse

        The model defined in huaweicloud sdk

        :param task_status: 任务状态,0表示检查中，1表示检查失败，2表示检查成功，3表示任务中止
        :type task_status: int
        :param progress: 
        :type progress: :class:`huaweicloudsdkcodeartscheck.v2.ProgressDetailV2`
        """
        
        super(ShowProgressDetailResponse, self).__init__()

        self._task_status = None
        self._progress = None
        self.discriminator = None

        if task_status is not None:
            self.task_status = task_status
        if progress is not None:
            self.progress = progress

    @property
    def task_status(self):
        """Gets the task_status of this ShowProgressDetailResponse.

        任务状态,0表示检查中，1表示检查失败，2表示检查成功，3表示任务中止

        :return: The task_status of this ShowProgressDetailResponse.
        :rtype: int
        """
        return self._task_status

    @task_status.setter
    def task_status(self, task_status):
        """Sets the task_status of this ShowProgressDetailResponse.

        任务状态,0表示检查中，1表示检查失败，2表示检查成功，3表示任务中止

        :param task_status: The task_status of this ShowProgressDetailResponse.
        :type task_status: int
        """
        self._task_status = task_status

    @property
    def progress(self):
        """Gets the progress of this ShowProgressDetailResponse.

        :return: The progress of this ShowProgressDetailResponse.
        :rtype: :class:`huaweicloudsdkcodeartscheck.v2.ProgressDetailV2`
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this ShowProgressDetailResponse.

        :param progress: The progress of this ShowProgressDetailResponse.
        :type progress: :class:`huaweicloudsdkcodeartscheck.v2.ProgressDetailV2`
        """
        self._progress = progress

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
        if not isinstance(other, ShowProgressDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
