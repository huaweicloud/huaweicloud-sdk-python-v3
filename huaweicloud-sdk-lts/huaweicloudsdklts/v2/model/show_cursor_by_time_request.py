# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowCursorByTimeRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_id': 'str',
        'stream_id': 'str',
        'shard_id': 'str',
        '_from': 'str'
    }

    attribute_map = {
        'group_id': 'group_id',
        'stream_id': 'stream_id',
        'shard_id': 'shard_id',
        '_from': 'from'
    }

    def __init__(self, group_id=None, stream_id=None, shard_id=None, _from=None):
        r"""ShowCursorByTimeRequest

        The model defined in huaweicloud sdk

        :param group_id: 日志组ID，获取方式请参见：获取项目ID，获取账号ID，日志组ID、日志流ID。 缺省值：None 最小长度：36 最大长度：36
        :type group_id: str
        :param stream_id: 日志流ID，获取方式请参见：获取项目ID，获取账号ID，日志组ID、日志流ID 缺省值：None 最小长度：36 最大长度：36
        :type stream_id: str
        :param shard_id: Shrad ID
        :type shard_id: str
        :param _from: 起始时间戳，时间单位为纳秒
        :type _from: str
        """
        
        

        self._group_id = None
        self._stream_id = None
        self._shard_id = None
        self.__from = None
        self.discriminator = None

        self.group_id = group_id
        self.stream_id = stream_id
        self.shard_id = shard_id
        self._from = _from

    @property
    def group_id(self):
        r"""Gets the group_id of this ShowCursorByTimeRequest.

        日志组ID，获取方式请参见：获取项目ID，获取账号ID，日志组ID、日志流ID。 缺省值：None 最小长度：36 最大长度：36

        :return: The group_id of this ShowCursorByTimeRequest.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this ShowCursorByTimeRequest.

        日志组ID，获取方式请参见：获取项目ID，获取账号ID，日志组ID、日志流ID。 缺省值：None 最小长度：36 最大长度：36

        :param group_id: The group_id of this ShowCursorByTimeRequest.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def stream_id(self):
        r"""Gets the stream_id of this ShowCursorByTimeRequest.

        日志流ID，获取方式请参见：获取项目ID，获取账号ID，日志组ID、日志流ID 缺省值：None 最小长度：36 最大长度：36

        :return: The stream_id of this ShowCursorByTimeRequest.
        :rtype: str
        """
        return self._stream_id

    @stream_id.setter
    def stream_id(self, stream_id):
        r"""Sets the stream_id of this ShowCursorByTimeRequest.

        日志流ID，获取方式请参见：获取项目ID，获取账号ID，日志组ID、日志流ID 缺省值：None 最小长度：36 最大长度：36

        :param stream_id: The stream_id of this ShowCursorByTimeRequest.
        :type stream_id: str
        """
        self._stream_id = stream_id

    @property
    def shard_id(self):
        r"""Gets the shard_id of this ShowCursorByTimeRequest.

        Shrad ID

        :return: The shard_id of this ShowCursorByTimeRequest.
        :rtype: str
        """
        return self._shard_id

    @shard_id.setter
    def shard_id(self, shard_id):
        r"""Sets the shard_id of this ShowCursorByTimeRequest.

        Shrad ID

        :param shard_id: The shard_id of this ShowCursorByTimeRequest.
        :type shard_id: str
        """
        self._shard_id = shard_id

    @property
    def _from(self):
        r"""Gets the _from of this ShowCursorByTimeRequest.

        起始时间戳，时间单位为纳秒

        :return: The _from of this ShowCursorByTimeRequest.
        :rtype: str
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        r"""Sets the _from of this ShowCursorByTimeRequest.

        起始时间戳，时间单位为纳秒

        :param _from: The _from of this ShowCursorByTimeRequest.
        :type _from: str
        """
        self.__from = _from

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
        if not isinstance(other, ShowCursorByTimeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
