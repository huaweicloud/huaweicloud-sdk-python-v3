# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExecuteGetVideosListResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'quota': 'int',
        'total': 'int',
        'offset': 'int',
        'count': 'int',
        'videos': 'list[Video]'
    }

    attribute_map = {
        'quota': 'quota',
        'total': 'total',
        'offset': 'offset',
        'count': 'count',
        'videos': 'videos'
    }

    def __init__(self, quota=None, total=None, offset=None, count=None, videos=None):
        r"""ExecuteGetVideosListResponse

        The model defined in huaweicloud sdk

        :param quota: 配额
        :type quota: int
        :param total: 总数
        :type total: int
        :param offset: 偏移
        :type offset: int
        :param count: 返回数量
        :type count: int
        :param videos: 视频列表
        :type videos: list[:class:`huaweicloudsdkcbs.v1.Video`]
        """
        
        super(ExecuteGetVideosListResponse, self).__init__()

        self._quota = None
        self._total = None
        self._offset = None
        self._count = None
        self._videos = None
        self.discriminator = None

        self.quota = quota
        self.total = total
        self.offset = offset
        self.count = count
        self.videos = videos

    @property
    def quota(self):
        r"""Gets the quota of this ExecuteGetVideosListResponse.

        配额

        :return: The quota of this ExecuteGetVideosListResponse.
        :rtype: int
        """
        return self._quota

    @quota.setter
    def quota(self, quota):
        r"""Sets the quota of this ExecuteGetVideosListResponse.

        配额

        :param quota: The quota of this ExecuteGetVideosListResponse.
        :type quota: int
        """
        self._quota = quota

    @property
    def total(self):
        r"""Gets the total of this ExecuteGetVideosListResponse.

        总数

        :return: The total of this ExecuteGetVideosListResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ExecuteGetVideosListResponse.

        总数

        :param total: The total of this ExecuteGetVideosListResponse.
        :type total: int
        """
        self._total = total

    @property
    def offset(self):
        r"""Gets the offset of this ExecuteGetVideosListResponse.

        偏移

        :return: The offset of this ExecuteGetVideosListResponse.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ExecuteGetVideosListResponse.

        偏移

        :param offset: The offset of this ExecuteGetVideosListResponse.
        :type offset: int
        """
        self._offset = offset

    @property
    def count(self):
        r"""Gets the count of this ExecuteGetVideosListResponse.

        返回数量

        :return: The count of this ExecuteGetVideosListResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ExecuteGetVideosListResponse.

        返回数量

        :param count: The count of this ExecuteGetVideosListResponse.
        :type count: int
        """
        self._count = count

    @property
    def videos(self):
        r"""Gets the videos of this ExecuteGetVideosListResponse.

        视频列表

        :return: The videos of this ExecuteGetVideosListResponse.
        :rtype: list[:class:`huaweicloudsdkcbs.v1.Video`]
        """
        return self._videos

    @videos.setter
    def videos(self, videos):
        r"""Sets the videos of this ExecuteGetVideosListResponse.

        视频列表

        :param videos: The videos of this ExecuteGetVideosListResponse.
        :type videos: list[:class:`huaweicloudsdkcbs.v1.Video`]
        """
        self._videos = videos

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
        if not isinstance(other, ExecuteGetVideosListResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
