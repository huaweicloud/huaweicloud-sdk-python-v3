# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListVideoMotionCaptureJobsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'video_motion_capture_jobs': 'list[VideoMotionCaptureInfo]',
        'x_request_id': 'str'
    }

    attribute_map = {
        'total': 'total',
        'video_motion_capture_jobs': 'video_motion_capture_jobs',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, total=None, video_motion_capture_jobs=None, x_request_id=None):
        r"""ListVideoMotionCaptureJobsResponse

        The model defined in huaweicloud sdk

        :param total: 视频驱动任务总数。
        :type total: int
        :param video_motion_capture_jobs: 视频驱动任务列表。
        :type video_motion_capture_jobs: list[:class:`huaweicloudsdkmetastudio.v1.VideoMotionCaptureInfo`]
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ListVideoMotionCaptureJobsResponse, self).__init__()

        self._total = None
        self._video_motion_capture_jobs = None
        self._x_request_id = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if video_motion_capture_jobs is not None:
            self.video_motion_capture_jobs = video_motion_capture_jobs
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def total(self):
        r"""Gets the total of this ListVideoMotionCaptureJobsResponse.

        视频驱动任务总数。

        :return: The total of this ListVideoMotionCaptureJobsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListVideoMotionCaptureJobsResponse.

        视频驱动任务总数。

        :param total: The total of this ListVideoMotionCaptureJobsResponse.
        :type total: int
        """
        self._total = total

    @property
    def video_motion_capture_jobs(self):
        r"""Gets the video_motion_capture_jobs of this ListVideoMotionCaptureJobsResponse.

        视频驱动任务列表。

        :return: The video_motion_capture_jobs of this ListVideoMotionCaptureJobsResponse.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.VideoMotionCaptureInfo`]
        """
        return self._video_motion_capture_jobs

    @video_motion_capture_jobs.setter
    def video_motion_capture_jobs(self, video_motion_capture_jobs):
        r"""Sets the video_motion_capture_jobs of this ListVideoMotionCaptureJobsResponse.

        视频驱动任务列表。

        :param video_motion_capture_jobs: The video_motion_capture_jobs of this ListVideoMotionCaptureJobsResponse.
        :type video_motion_capture_jobs: list[:class:`huaweicloudsdkmetastudio.v1.VideoMotionCaptureInfo`]
        """
        self._video_motion_capture_jobs = video_motion_capture_jobs

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ListVideoMotionCaptureJobsResponse.

        :return: The x_request_id of this ListVideoMotionCaptureJobsResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ListVideoMotionCaptureJobsResponse.

        :param x_request_id: The x_request_id of this ListVideoMotionCaptureJobsResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, ListVideoMotionCaptureJobsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
