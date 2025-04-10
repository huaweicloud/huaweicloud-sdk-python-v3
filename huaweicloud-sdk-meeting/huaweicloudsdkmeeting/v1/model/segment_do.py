# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SegmentDO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'manual_order': 'int',
        'segment_order': 'int',
        'segment_size': 'str',
        'file_list': 'list[SegmentFileDO]'
    }

    attribute_map = {
        'manual_order': 'manualOrder',
        'segment_order': 'segmentOrder',
        'segment_size': 'segmentSize',
        'file_list': 'fileList'
    }

    def __init__(self, manual_order=None, segment_order=None, segment_size=None, file_list=None):
        r"""SegmentDO

        The model defined in huaweicloud sdk

        :param manual_order: 录制人工分段序号，每次启动录制，生成一个分段
        :type manual_order: int
        :param segment_order: 录制片段内的文件自动切片序号（每次启动录制后，每三小时一个分片文件，多次人工启动重新从1开始）
        :type segment_order: int
        :param segment_size: 录制分段总文件大小（字节）
        :type segment_size: str
        :param file_list: 录制文件自动切片列表，每3小时文件切片一次
        :type file_list: list[:class:`huaweicloudsdkmeeting.v1.SegmentFileDO`]
        """
        
        

        self._manual_order = None
        self._segment_order = None
        self._segment_size = None
        self._file_list = None
        self.discriminator = None

        if manual_order is not None:
            self.manual_order = manual_order
        if segment_order is not None:
            self.segment_order = segment_order
        if segment_size is not None:
            self.segment_size = segment_size
        if file_list is not None:
            self.file_list = file_list

    @property
    def manual_order(self):
        r"""Gets the manual_order of this SegmentDO.

        录制人工分段序号，每次启动录制，生成一个分段

        :return: The manual_order of this SegmentDO.
        :rtype: int
        """
        return self._manual_order

    @manual_order.setter
    def manual_order(self, manual_order):
        r"""Sets the manual_order of this SegmentDO.

        录制人工分段序号，每次启动录制，生成一个分段

        :param manual_order: The manual_order of this SegmentDO.
        :type manual_order: int
        """
        self._manual_order = manual_order

    @property
    def segment_order(self):
        r"""Gets the segment_order of this SegmentDO.

        录制片段内的文件自动切片序号（每次启动录制后，每三小时一个分片文件，多次人工启动重新从1开始）

        :return: The segment_order of this SegmentDO.
        :rtype: int
        """
        return self._segment_order

    @segment_order.setter
    def segment_order(self, segment_order):
        r"""Sets the segment_order of this SegmentDO.

        录制片段内的文件自动切片序号（每次启动录制后，每三小时一个分片文件，多次人工启动重新从1开始）

        :param segment_order: The segment_order of this SegmentDO.
        :type segment_order: int
        """
        self._segment_order = segment_order

    @property
    def segment_size(self):
        r"""Gets the segment_size of this SegmentDO.

        录制分段总文件大小（字节）

        :return: The segment_size of this SegmentDO.
        :rtype: str
        """
        return self._segment_size

    @segment_size.setter
    def segment_size(self, segment_size):
        r"""Sets the segment_size of this SegmentDO.

        录制分段总文件大小（字节）

        :param segment_size: The segment_size of this SegmentDO.
        :type segment_size: str
        """
        self._segment_size = segment_size

    @property
    def file_list(self):
        r"""Gets the file_list of this SegmentDO.

        录制文件自动切片列表，每3小时文件切片一次

        :return: The file_list of this SegmentDO.
        :rtype: list[:class:`huaweicloudsdkmeeting.v1.SegmentFileDO`]
        """
        return self._file_list

    @file_list.setter
    def file_list(self, file_list):
        r"""Sets the file_list of this SegmentDO.

        录制文件自动切片列表，每3小时文件切片一次

        :param file_list: The file_list of this SegmentDO.
        :type file_list: list[:class:`huaweicloudsdkmeeting.v1.SegmentFileDO`]
        """
        self._file_list = file_list

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
        if not isinstance(other, SegmentDO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
