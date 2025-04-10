# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RecordInfoDO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'subject': 'str',
        'begin_time': 'str',
        'segment_offset': 'int',
        'segment_limit': 'int',
        'segment_count': 'int',
        'segment_list': 'list[SegmentDO]'
    }

    attribute_map = {
        'subject': 'subject',
        'begin_time': 'beginTime',
        'segment_offset': 'segmentOffset',
        'segment_limit': 'segmentLimit',
        'segment_count': 'segmentCount',
        'segment_list': 'segmentList'
    }

    def __init__(self, subject=None, begin_time=None, segment_offset=None, segment_limit=None, segment_count=None, segment_list=None):
        r"""RecordInfoDO

        The model defined in huaweicloud sdk

        :param subject: 会议主题
        :type subject: str
        :param begin_time: 会议录制开始时间
        :type begin_time: str
        :param segment_offset: 录制段落查询偏移量
        :type segment_offset: int
        :param segment_limit: 录制段落查询数量
        :type segment_limit: int
        :param segment_count: 录制段落总数
        :type segment_count: int
        :param segment_list: 录制人工启动/停止分段列表
        :type segment_list: list[:class:`huaweicloudsdkmeeting.v1.SegmentDO`]
        """
        
        

        self._subject = None
        self._begin_time = None
        self._segment_offset = None
        self._segment_limit = None
        self._segment_count = None
        self._segment_list = None
        self.discriminator = None

        if subject is not None:
            self.subject = subject
        if begin_time is not None:
            self.begin_time = begin_time
        if segment_offset is not None:
            self.segment_offset = segment_offset
        if segment_limit is not None:
            self.segment_limit = segment_limit
        if segment_count is not None:
            self.segment_count = segment_count
        if segment_list is not None:
            self.segment_list = segment_list

    @property
    def subject(self):
        r"""Gets the subject of this RecordInfoDO.

        会议主题

        :return: The subject of this RecordInfoDO.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        r"""Sets the subject of this RecordInfoDO.

        会议主题

        :param subject: The subject of this RecordInfoDO.
        :type subject: str
        """
        self._subject = subject

    @property
    def begin_time(self):
        r"""Gets the begin_time of this RecordInfoDO.

        会议录制开始时间

        :return: The begin_time of this RecordInfoDO.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        r"""Sets the begin_time of this RecordInfoDO.

        会议录制开始时间

        :param begin_time: The begin_time of this RecordInfoDO.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def segment_offset(self):
        r"""Gets the segment_offset of this RecordInfoDO.

        录制段落查询偏移量

        :return: The segment_offset of this RecordInfoDO.
        :rtype: int
        """
        return self._segment_offset

    @segment_offset.setter
    def segment_offset(self, segment_offset):
        r"""Sets the segment_offset of this RecordInfoDO.

        录制段落查询偏移量

        :param segment_offset: The segment_offset of this RecordInfoDO.
        :type segment_offset: int
        """
        self._segment_offset = segment_offset

    @property
    def segment_limit(self):
        r"""Gets the segment_limit of this RecordInfoDO.

        录制段落查询数量

        :return: The segment_limit of this RecordInfoDO.
        :rtype: int
        """
        return self._segment_limit

    @segment_limit.setter
    def segment_limit(self, segment_limit):
        r"""Sets the segment_limit of this RecordInfoDO.

        录制段落查询数量

        :param segment_limit: The segment_limit of this RecordInfoDO.
        :type segment_limit: int
        """
        self._segment_limit = segment_limit

    @property
    def segment_count(self):
        r"""Gets the segment_count of this RecordInfoDO.

        录制段落总数

        :return: The segment_count of this RecordInfoDO.
        :rtype: int
        """
        return self._segment_count

    @segment_count.setter
    def segment_count(self, segment_count):
        r"""Sets the segment_count of this RecordInfoDO.

        录制段落总数

        :param segment_count: The segment_count of this RecordInfoDO.
        :type segment_count: int
        """
        self._segment_count = segment_count

    @property
    def segment_list(self):
        r"""Gets the segment_list of this RecordInfoDO.

        录制人工启动/停止分段列表

        :return: The segment_list of this RecordInfoDO.
        :rtype: list[:class:`huaweicloudsdkmeeting.v1.SegmentDO`]
        """
        return self._segment_list

    @segment_list.setter
    def segment_list(self, segment_list):
        r"""Sets the segment_list of this RecordInfoDO.

        录制人工启动/停止分段列表

        :param segment_list: The segment_list of this RecordInfoDO.
        :type segment_list: list[:class:`huaweicloudsdkmeeting.v1.SegmentDO`]
        """
        self._segment_list = segment_list

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
        if not isinstance(other, RecordInfoDO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
