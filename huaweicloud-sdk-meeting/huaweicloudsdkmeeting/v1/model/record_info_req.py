# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RecordInfoReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'conf_uuid': 'str',
        'segment_offset': 'int',
        'segment_limit': 'int'
    }

    attribute_map = {
        'conf_uuid': 'confUUID',
        'segment_offset': 'segmentOffset',
        'segment_limit': 'segmentLimit'
    }

    def __init__(self, conf_uuid=None, segment_offset=None, segment_limit=None):
        r"""RecordInfoReq

        The model defined in huaweicloud sdk

        :param conf_uuid: 会议uuid
        :type conf_uuid: str
        :param segment_offset: 录制段落查询偏移量
        :type segment_offset: int
        :param segment_limit: 录制段落查询数量
        :type segment_limit: int
        """
        
        

        self._conf_uuid = None
        self._segment_offset = None
        self._segment_limit = None
        self.discriminator = None

        self.conf_uuid = conf_uuid
        if segment_offset is not None:
            self.segment_offset = segment_offset
        if segment_limit is not None:
            self.segment_limit = segment_limit

    @property
    def conf_uuid(self):
        r"""Gets the conf_uuid of this RecordInfoReq.

        会议uuid

        :return: The conf_uuid of this RecordInfoReq.
        :rtype: str
        """
        return self._conf_uuid

    @conf_uuid.setter
    def conf_uuid(self, conf_uuid):
        r"""Sets the conf_uuid of this RecordInfoReq.

        会议uuid

        :param conf_uuid: The conf_uuid of this RecordInfoReq.
        :type conf_uuid: str
        """
        self._conf_uuid = conf_uuid

    @property
    def segment_offset(self):
        r"""Gets the segment_offset of this RecordInfoReq.

        录制段落查询偏移量

        :return: The segment_offset of this RecordInfoReq.
        :rtype: int
        """
        return self._segment_offset

    @segment_offset.setter
    def segment_offset(self, segment_offset):
        r"""Sets the segment_offset of this RecordInfoReq.

        录制段落查询偏移量

        :param segment_offset: The segment_offset of this RecordInfoReq.
        :type segment_offset: int
        """
        self._segment_offset = segment_offset

    @property
    def segment_limit(self):
        r"""Gets the segment_limit of this RecordInfoReq.

        录制段落查询数量

        :return: The segment_limit of this RecordInfoReq.
        :rtype: int
        """
        return self._segment_limit

    @segment_limit.setter
    def segment_limit(self, segment_limit):
        r"""Sets the segment_limit of this RecordInfoReq.

        录制段落查询数量

        :param segment_limit: The segment_limit of this RecordInfoReq.
        :type segment_limit: int
        """
        self._segment_limit = segment_limit

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
        if not isinstance(other, RecordInfoReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
