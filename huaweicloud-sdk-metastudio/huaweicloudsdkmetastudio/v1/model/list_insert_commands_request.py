# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInsertCommandsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'room_id': 'str',
        'job_id': 'str',
        'x_app_user_id': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'room_id': 'room_id',
        'job_id': 'job_id',
        'x_app_user_id': 'X-App-UserId',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, room_id=None, job_id=None, x_app_user_id=None, offset=None, limit=None):
        r"""ListInsertCommandsRequest

        The model defined in huaweicloud sdk

        :param room_id: 直播间ID。
        :type room_id: str
        :param job_id: 任务ID。
        :type job_id: str
        :param x_app_user_id: 第三方用户ID。不允许输入中文。
        :type x_app_user_id: str
        :param offset: 偏移量，表示从此偏移量开始查询。
        :type offset: int
        :param limit: 每页显示的条目数量。
        :type limit: int
        """
        
        

        self._room_id = None
        self._job_id = None
        self._x_app_user_id = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.room_id = room_id
        self.job_id = job_id
        if x_app_user_id is not None:
            self.x_app_user_id = x_app_user_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def room_id(self):
        r"""Gets the room_id of this ListInsertCommandsRequest.

        直播间ID。

        :return: The room_id of this ListInsertCommandsRequest.
        :rtype: str
        """
        return self._room_id

    @room_id.setter
    def room_id(self, room_id):
        r"""Sets the room_id of this ListInsertCommandsRequest.

        直播间ID。

        :param room_id: The room_id of this ListInsertCommandsRequest.
        :type room_id: str
        """
        self._room_id = room_id

    @property
    def job_id(self):
        r"""Gets the job_id of this ListInsertCommandsRequest.

        任务ID。

        :return: The job_id of this ListInsertCommandsRequest.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this ListInsertCommandsRequest.

        任务ID。

        :param job_id: The job_id of this ListInsertCommandsRequest.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def x_app_user_id(self):
        r"""Gets the x_app_user_id of this ListInsertCommandsRequest.

        第三方用户ID。不允许输入中文。

        :return: The x_app_user_id of this ListInsertCommandsRequest.
        :rtype: str
        """
        return self._x_app_user_id

    @x_app_user_id.setter
    def x_app_user_id(self, x_app_user_id):
        r"""Sets the x_app_user_id of this ListInsertCommandsRequest.

        第三方用户ID。不允许输入中文。

        :param x_app_user_id: The x_app_user_id of this ListInsertCommandsRequest.
        :type x_app_user_id: str
        """
        self._x_app_user_id = x_app_user_id

    @property
    def offset(self):
        r"""Gets the offset of this ListInsertCommandsRequest.

        偏移量，表示从此偏移量开始查询。

        :return: The offset of this ListInsertCommandsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListInsertCommandsRequest.

        偏移量，表示从此偏移量开始查询。

        :param offset: The offset of this ListInsertCommandsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListInsertCommandsRequest.

        每页显示的条目数量。

        :return: The limit of this ListInsertCommandsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListInsertCommandsRequest.

        每页显示的条目数量。

        :param limit: The limit of this ListInsertCommandsRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListInsertCommandsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
