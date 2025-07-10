# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListScreenRecordsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'offset': 'int',
        'desktop_id': 'str',
        'username': 'str',
        'status': 'str',
        'type': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'sort_field': 'str',
        'sort_type': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'desktop_id': 'desktop_id',
        'username': 'username',
        'status': 'status',
        'type': 'type',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'sort_field': 'sort_field',
        'sort_type': 'sort_type'
    }

    def __init__(self, limit=None, offset=None, desktop_id=None, username=None, status=None, type=None, start_time=None, end_time=None, sort_field=None, sort_type=None):
        r"""ListScreenRecordsRequest

        The model defined in huaweicloud sdk

        :param limit: 用于分页查询，返回录屏记录数量的限制。默认100。范围0~1000。
        :type limit: int
        :param offset: 用于分页查询，查询的起始记录序号，从0开始。
        :type offset: int
        :param desktop_id: 根据桌面ID过滤结果。
        :type desktop_id: str
        :param username: 根据用户名称过滤结果。
        :type username: str
        :param status: 录屏状态。 - RECORDING：录制中。 - REC_COMPLETED：录制完成。 - UPLOADING：上传中。 - UPLOAD_COMPLETED：上传完成。
        :type status: str
        :param type: 录屏类型。 - FULL：全程录屏。 - INTERVAL：间隔录屏。 - OPERATION：用户操作录屏。 - SESSION：监听会话生命周期录屏。
        :type type: str
        :param start_time: 开始时间，格式为yyyy-MM-dd HH:mm:ss（UTC时间，不传查默认最近15天）。
        :type start_time: str
        :param end_time: 结束时间，格式为yyyy-MM-dd HH:mm:ss（UTC时间，不传查默认最近15天）。
        :type end_time: str
        :param sort_field: 用于排序，表示按照哪个字段排序。取值为录屏属性start_time字段。
        :type sort_field: str
        :param sort_type: 用于排序，表示升序还是降序，取值为asc和desc。与sort_field一起组合使用。
        :type sort_type: str
        """
        
        

        self._limit = None
        self._offset = None
        self._desktop_id = None
        self._username = None
        self._status = None
        self._type = None
        self._start_time = None
        self._end_time = None
        self._sort_field = None
        self._sort_type = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if desktop_id is not None:
            self.desktop_id = desktop_id
        if username is not None:
            self.username = username
        if status is not None:
            self.status = status
        if type is not None:
            self.type = type
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if sort_field is not None:
            self.sort_field = sort_field
        if sort_type is not None:
            self.sort_type = sort_type

    @property
    def limit(self):
        r"""Gets the limit of this ListScreenRecordsRequest.

        用于分页查询，返回录屏记录数量的限制。默认100。范围0~1000。

        :return: The limit of this ListScreenRecordsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListScreenRecordsRequest.

        用于分页查询，返回录屏记录数量的限制。默认100。范围0~1000。

        :param limit: The limit of this ListScreenRecordsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListScreenRecordsRequest.

        用于分页查询，查询的起始记录序号，从0开始。

        :return: The offset of this ListScreenRecordsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListScreenRecordsRequest.

        用于分页查询，查询的起始记录序号，从0开始。

        :param offset: The offset of this ListScreenRecordsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def desktop_id(self):
        r"""Gets the desktop_id of this ListScreenRecordsRequest.

        根据桌面ID过滤结果。

        :return: The desktop_id of this ListScreenRecordsRequest.
        :rtype: str
        """
        return self._desktop_id

    @desktop_id.setter
    def desktop_id(self, desktop_id):
        r"""Sets the desktop_id of this ListScreenRecordsRequest.

        根据桌面ID过滤结果。

        :param desktop_id: The desktop_id of this ListScreenRecordsRequest.
        :type desktop_id: str
        """
        self._desktop_id = desktop_id

    @property
    def username(self):
        r"""Gets the username of this ListScreenRecordsRequest.

        根据用户名称过滤结果。

        :return: The username of this ListScreenRecordsRequest.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        r"""Sets the username of this ListScreenRecordsRequest.

        根据用户名称过滤结果。

        :param username: The username of this ListScreenRecordsRequest.
        :type username: str
        """
        self._username = username

    @property
    def status(self):
        r"""Gets the status of this ListScreenRecordsRequest.

        录屏状态。 - RECORDING：录制中。 - REC_COMPLETED：录制完成。 - UPLOADING：上传中。 - UPLOAD_COMPLETED：上传完成。

        :return: The status of this ListScreenRecordsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListScreenRecordsRequest.

        录屏状态。 - RECORDING：录制中。 - REC_COMPLETED：录制完成。 - UPLOADING：上传中。 - UPLOAD_COMPLETED：上传完成。

        :param status: The status of this ListScreenRecordsRequest.
        :type status: str
        """
        self._status = status

    @property
    def type(self):
        r"""Gets the type of this ListScreenRecordsRequest.

        录屏类型。 - FULL：全程录屏。 - INTERVAL：间隔录屏。 - OPERATION：用户操作录屏。 - SESSION：监听会话生命周期录屏。

        :return: The type of this ListScreenRecordsRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListScreenRecordsRequest.

        录屏类型。 - FULL：全程录屏。 - INTERVAL：间隔录屏。 - OPERATION：用户操作录屏。 - SESSION：监听会话生命周期录屏。

        :param type: The type of this ListScreenRecordsRequest.
        :type type: str
        """
        self._type = type

    @property
    def start_time(self):
        r"""Gets the start_time of this ListScreenRecordsRequest.

        开始时间，格式为yyyy-MM-dd HH:mm:ss（UTC时间，不传查默认最近15天）。

        :return: The start_time of this ListScreenRecordsRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListScreenRecordsRequest.

        开始时间，格式为yyyy-MM-dd HH:mm:ss（UTC时间，不传查默认最近15天）。

        :param start_time: The start_time of this ListScreenRecordsRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListScreenRecordsRequest.

        结束时间，格式为yyyy-MM-dd HH:mm:ss（UTC时间，不传查默认最近15天）。

        :return: The end_time of this ListScreenRecordsRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListScreenRecordsRequest.

        结束时间，格式为yyyy-MM-dd HH:mm:ss（UTC时间，不传查默认最近15天）。

        :param end_time: The end_time of this ListScreenRecordsRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def sort_field(self):
        r"""Gets the sort_field of this ListScreenRecordsRequest.

        用于排序，表示按照哪个字段排序。取值为录屏属性start_time字段。

        :return: The sort_field of this ListScreenRecordsRequest.
        :rtype: str
        """
        return self._sort_field

    @sort_field.setter
    def sort_field(self, sort_field):
        r"""Sets the sort_field of this ListScreenRecordsRequest.

        用于排序，表示按照哪个字段排序。取值为录屏属性start_time字段。

        :param sort_field: The sort_field of this ListScreenRecordsRequest.
        :type sort_field: str
        """
        self._sort_field = sort_field

    @property
    def sort_type(self):
        r"""Gets the sort_type of this ListScreenRecordsRequest.

        用于排序，表示升序还是降序，取值为asc和desc。与sort_field一起组合使用。

        :return: The sort_type of this ListScreenRecordsRequest.
        :rtype: str
        """
        return self._sort_type

    @sort_type.setter
    def sort_type(self, sort_type):
        r"""Sets the sort_type of this ListScreenRecordsRequest.

        用于排序，表示升序还是降序，取值为asc和desc。与sort_field一起组合使用。

        :param sort_type: The sort_type of this ListScreenRecordsRequest.
        :type sort_type: str
        """
        self._sort_type = sort_type

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
        if not isinstance(other, ListScreenRecordsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
