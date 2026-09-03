# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EventEventsDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'log_name': 'str',
        'pos': 'int',
        'event_type': 'str',
        'server_id': 'str',
        'end_log_pos': 'int',
        'info': 'str'
    }

    attribute_map = {
        'log_name': 'log_name',
        'pos': 'pos',
        'event_type': 'event_type',
        'server_id': 'server_id',
        'end_log_pos': 'end_log_pos',
        'info': 'info'
    }

    def __init__(self, log_name=None, pos=None, event_type=None, server_id=None, end_log_pos=None, info=None):
        r"""EventEventsDto

        The model defined in huaweicloud sdk

        :param log_name: 文件名称
        :type log_name: str
        :param pos: 位置
        :type pos: int
        :param event_type: 事件类型
        :type event_type: str
        :param server_id: 服务器ID
        :type server_id: str
        :param end_log_pos: 结束位置
        :type end_log_pos: int
        :param info: 信息
        :type info: str
        """
        
        

        self._log_name = None
        self._pos = None
        self._event_type = None
        self._server_id = None
        self._end_log_pos = None
        self._info = None
        self.discriminator = None

        if log_name is not None:
            self.log_name = log_name
        if pos is not None:
            self.pos = pos
        if event_type is not None:
            self.event_type = event_type
        if server_id is not None:
            self.server_id = server_id
        if end_log_pos is not None:
            self.end_log_pos = end_log_pos
        if info is not None:
            self.info = info

    @property
    def log_name(self):
        r"""Gets the log_name of this EventEventsDto.

        文件名称

        :return: The log_name of this EventEventsDto.
        :rtype: str
        """
        return self._log_name

    @log_name.setter
    def log_name(self, log_name):
        r"""Sets the log_name of this EventEventsDto.

        文件名称

        :param log_name: The log_name of this EventEventsDto.
        :type log_name: str
        """
        self._log_name = log_name

    @property
    def pos(self):
        r"""Gets the pos of this EventEventsDto.

        位置

        :return: The pos of this EventEventsDto.
        :rtype: int
        """
        return self._pos

    @pos.setter
    def pos(self, pos):
        r"""Sets the pos of this EventEventsDto.

        位置

        :param pos: The pos of this EventEventsDto.
        :type pos: int
        """
        self._pos = pos

    @property
    def event_type(self):
        r"""Gets the event_type of this EventEventsDto.

        事件类型

        :return: The event_type of this EventEventsDto.
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        r"""Sets the event_type of this EventEventsDto.

        事件类型

        :param event_type: The event_type of this EventEventsDto.
        :type event_type: str
        """
        self._event_type = event_type

    @property
    def server_id(self):
        r"""Gets the server_id of this EventEventsDto.

        服务器ID

        :return: The server_id of this EventEventsDto.
        :rtype: str
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        r"""Sets the server_id of this EventEventsDto.

        服务器ID

        :param server_id: The server_id of this EventEventsDto.
        :type server_id: str
        """
        self._server_id = server_id

    @property
    def end_log_pos(self):
        r"""Gets the end_log_pos of this EventEventsDto.

        结束位置

        :return: The end_log_pos of this EventEventsDto.
        :rtype: int
        """
        return self._end_log_pos

    @end_log_pos.setter
    def end_log_pos(self, end_log_pos):
        r"""Sets the end_log_pos of this EventEventsDto.

        结束位置

        :param end_log_pos: The end_log_pos of this EventEventsDto.
        :type end_log_pos: int
        """
        self._end_log_pos = end_log_pos

    @property
    def info(self):
        r"""Gets the info of this EventEventsDto.

        信息

        :return: The info of this EventEventsDto.
        :rtype: str
        """
        return self._info

    @info.setter
    def info(self, info):
        r"""Sets the info of this EventEventsDto.

        信息

        :param info: The info of this EventEventsDto.
        :type info: str
        """
        self._info = info

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, EventEventsDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
