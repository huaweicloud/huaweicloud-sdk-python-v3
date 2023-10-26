# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowBackgroundTaskProgressResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'progress': 'int',
        'remain_time': 'int',
        'step_details': 'list[StepDetail]'
    }

    attribute_map = {
        'progress': 'progress',
        'remain_time': 'remain_time',
        'step_details': 'step_details'
    }

    def __init__(self, progress=None, remain_time=None, step_details=None):
        """ShowBackgroundTaskProgressResponse

        The model defined in huaweicloud sdk

        :param progress: 总体进度,百分比
        :type progress: int
        :param remain_time: 剩余时间(单位秒)
        :type remain_time: int
        :param step_details: 任务详情列表
        :type step_details: list[:class:`huaweicloudsdkdcs.v2.StepDetail`]
        """
        
        super(ShowBackgroundTaskProgressResponse, self).__init__()

        self._progress = None
        self._remain_time = None
        self._step_details = None
        self.discriminator = None

        if progress is not None:
            self.progress = progress
        if remain_time is not None:
            self.remain_time = remain_time
        if step_details is not None:
            self.step_details = step_details

    @property
    def progress(self):
        """Gets the progress of this ShowBackgroundTaskProgressResponse.

        总体进度,百分比

        :return: The progress of this ShowBackgroundTaskProgressResponse.
        :rtype: int
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this ShowBackgroundTaskProgressResponse.

        总体进度,百分比

        :param progress: The progress of this ShowBackgroundTaskProgressResponse.
        :type progress: int
        """
        self._progress = progress

    @property
    def remain_time(self):
        """Gets the remain_time of this ShowBackgroundTaskProgressResponse.

        剩余时间(单位秒)

        :return: The remain_time of this ShowBackgroundTaskProgressResponse.
        :rtype: int
        """
        return self._remain_time

    @remain_time.setter
    def remain_time(self, remain_time):
        """Sets the remain_time of this ShowBackgroundTaskProgressResponse.

        剩余时间(单位秒)

        :param remain_time: The remain_time of this ShowBackgroundTaskProgressResponse.
        :type remain_time: int
        """
        self._remain_time = remain_time

    @property
    def step_details(self):
        """Gets the step_details of this ShowBackgroundTaskProgressResponse.

        任务详情列表

        :return: The step_details of this ShowBackgroundTaskProgressResponse.
        :rtype: list[:class:`huaweicloudsdkdcs.v2.StepDetail`]
        """
        return self._step_details

    @step_details.setter
    def step_details(self, step_details):
        """Sets the step_details of this ShowBackgroundTaskProgressResponse.

        任务详情列表

        :param step_details: The step_details of this ShowBackgroundTaskProgressResponse.
        :type step_details: list[:class:`huaweicloudsdkdcs.v2.StepDetail`]
        """
        self._step_details = step_details

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
        if not isinstance(other, ShowBackgroundTaskProgressResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
