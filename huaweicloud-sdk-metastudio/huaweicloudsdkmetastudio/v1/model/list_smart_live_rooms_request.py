# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSmartLiveRoomsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_app_user_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'room_name': 'str',
        'dh_id': 'str',
        'model_name': 'str',
        'live_state': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'room_type': 'str',
        'template_own_type': 'str',
        'confirm_state': 'str'
    }

    attribute_map = {
        'x_app_user_id': 'X-App-UserId',
        'offset': 'offset',
        'limit': 'limit',
        'room_name': 'room_name',
        'dh_id': 'dh_id',
        'model_name': 'model_name',
        'live_state': 'live_state',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'room_type': 'room_type',
        'template_own_type': 'template_own_type',
        'confirm_state': 'confirm_state'
    }

    def __init__(self, x_app_user_id=None, offset=None, limit=None, room_name=None, dh_id=None, model_name=None, live_state=None, start_time=None, end_time=None, room_type=None, template_own_type=None, confirm_state=None):
        r"""ListSmartLiveRoomsRequest

        The model defined in huaweicloud sdk

        :param x_app_user_id: 第三方用户ID。不允许输入中文。
        :type x_app_user_id: str
        :param offset: 偏移量，表示从此偏移量开始查询。
        :type offset: int
        :param limit: 每页显示的条目数量。
        :type limit: int
        :param room_name: 按直播间名称模糊查询。
        :type room_name: str
        :param dh_id: 按数字人形象ID查询。
        :type dh_id: str
        :param model_name: 按形象名称模糊查询。
        :type model_name: str
        :param live_state: 当前直播间直播状态。 WAITING，PROCESSING，SUCCESS，FAILED，CANCELED对应直播任务状态 NULL 对应没有直播任务 可多个状态查询，使用英文逗号分隔。
        :type live_state: str
        :param start_time: 最近直播任务起始时间。格式遵循：RFC 3339 如“2021-01-10T08:43:17Z”。
        :type start_time: str
        :param end_time: 结束时间。格式遵循：RFC 3339 如\&quot;2021-01-10T10:43:17Z\&quot;。
        :type end_time: str
        :param room_type: 按直播间类型查询。直播间类型。 * NORMAL：普通直播间，直播间一直存在，可以反复开播 * TEMP：临时直播间，直播任务结束后自动清理直播间。 * TEMPLATE：直播间模板。
        :type room_type: str
        :param template_own_type: 按照自己拥有的和别人分享以及公共的模板进行查询 * OWNED 自己拥有且暂未共享的 * SHARED_TO_OHTERS 分享给别人的 * SHARED_FROM_OHTERS 别人分享给我的 * PUBLIC 公共模板
        :type template_own_type: str
        :param confirm_state: 直播间确认状态。此状态仅用于特定用户需要人工确认场景。 - unconfirm: 未确认 - confirmed：已确认 - reject： 拒绝
        :type confirm_state: str
        """
        
        

        self._x_app_user_id = None
        self._offset = None
        self._limit = None
        self._room_name = None
        self._dh_id = None
        self._model_name = None
        self._live_state = None
        self._start_time = None
        self._end_time = None
        self._room_type = None
        self._template_own_type = None
        self._confirm_state = None
        self.discriminator = None

        if x_app_user_id is not None:
            self.x_app_user_id = x_app_user_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if room_name is not None:
            self.room_name = room_name
        if dh_id is not None:
            self.dh_id = dh_id
        if model_name is not None:
            self.model_name = model_name
        if live_state is not None:
            self.live_state = live_state
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if room_type is not None:
            self.room_type = room_type
        if template_own_type is not None:
            self.template_own_type = template_own_type
        if confirm_state is not None:
            self.confirm_state = confirm_state

    @property
    def x_app_user_id(self):
        r"""Gets the x_app_user_id of this ListSmartLiveRoomsRequest.

        第三方用户ID。不允许输入中文。

        :return: The x_app_user_id of this ListSmartLiveRoomsRequest.
        :rtype: str
        """
        return self._x_app_user_id

    @x_app_user_id.setter
    def x_app_user_id(self, x_app_user_id):
        r"""Sets the x_app_user_id of this ListSmartLiveRoomsRequest.

        第三方用户ID。不允许输入中文。

        :param x_app_user_id: The x_app_user_id of this ListSmartLiveRoomsRequest.
        :type x_app_user_id: str
        """
        self._x_app_user_id = x_app_user_id

    @property
    def offset(self):
        r"""Gets the offset of this ListSmartLiveRoomsRequest.

        偏移量，表示从此偏移量开始查询。

        :return: The offset of this ListSmartLiveRoomsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListSmartLiveRoomsRequest.

        偏移量，表示从此偏移量开始查询。

        :param offset: The offset of this ListSmartLiveRoomsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListSmartLiveRoomsRequest.

        每页显示的条目数量。

        :return: The limit of this ListSmartLiveRoomsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListSmartLiveRoomsRequest.

        每页显示的条目数量。

        :param limit: The limit of this ListSmartLiveRoomsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def room_name(self):
        r"""Gets the room_name of this ListSmartLiveRoomsRequest.

        按直播间名称模糊查询。

        :return: The room_name of this ListSmartLiveRoomsRequest.
        :rtype: str
        """
        return self._room_name

    @room_name.setter
    def room_name(self, room_name):
        r"""Sets the room_name of this ListSmartLiveRoomsRequest.

        按直播间名称模糊查询。

        :param room_name: The room_name of this ListSmartLiveRoomsRequest.
        :type room_name: str
        """
        self._room_name = room_name

    @property
    def dh_id(self):
        r"""Gets the dh_id of this ListSmartLiveRoomsRequest.

        按数字人形象ID查询。

        :return: The dh_id of this ListSmartLiveRoomsRequest.
        :rtype: str
        """
        return self._dh_id

    @dh_id.setter
    def dh_id(self, dh_id):
        r"""Sets the dh_id of this ListSmartLiveRoomsRequest.

        按数字人形象ID查询。

        :param dh_id: The dh_id of this ListSmartLiveRoomsRequest.
        :type dh_id: str
        """
        self._dh_id = dh_id

    @property
    def model_name(self):
        r"""Gets the model_name of this ListSmartLiveRoomsRequest.

        按形象名称模糊查询。

        :return: The model_name of this ListSmartLiveRoomsRequest.
        :rtype: str
        """
        return self._model_name

    @model_name.setter
    def model_name(self, model_name):
        r"""Sets the model_name of this ListSmartLiveRoomsRequest.

        按形象名称模糊查询。

        :param model_name: The model_name of this ListSmartLiveRoomsRequest.
        :type model_name: str
        """
        self._model_name = model_name

    @property
    def live_state(self):
        r"""Gets the live_state of this ListSmartLiveRoomsRequest.

        当前直播间直播状态。 WAITING，PROCESSING，SUCCESS，FAILED，CANCELED对应直播任务状态 NULL 对应没有直播任务 可多个状态查询，使用英文逗号分隔。

        :return: The live_state of this ListSmartLiveRoomsRequest.
        :rtype: str
        """
        return self._live_state

    @live_state.setter
    def live_state(self, live_state):
        r"""Sets the live_state of this ListSmartLiveRoomsRequest.

        当前直播间直播状态。 WAITING，PROCESSING，SUCCESS，FAILED，CANCELED对应直播任务状态 NULL 对应没有直播任务 可多个状态查询，使用英文逗号分隔。

        :param live_state: The live_state of this ListSmartLiveRoomsRequest.
        :type live_state: str
        """
        self._live_state = live_state

    @property
    def start_time(self):
        r"""Gets the start_time of this ListSmartLiveRoomsRequest.

        最近直播任务起始时间。格式遵循：RFC 3339 如“2021-01-10T08:43:17Z”。

        :return: The start_time of this ListSmartLiveRoomsRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListSmartLiveRoomsRequest.

        最近直播任务起始时间。格式遵循：RFC 3339 如“2021-01-10T08:43:17Z”。

        :param start_time: The start_time of this ListSmartLiveRoomsRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListSmartLiveRoomsRequest.

        结束时间。格式遵循：RFC 3339 如\"2021-01-10T10:43:17Z\"。

        :return: The end_time of this ListSmartLiveRoomsRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListSmartLiveRoomsRequest.

        结束时间。格式遵循：RFC 3339 如\"2021-01-10T10:43:17Z\"。

        :param end_time: The end_time of this ListSmartLiveRoomsRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def room_type(self):
        r"""Gets the room_type of this ListSmartLiveRoomsRequest.

        按直播间类型查询。直播间类型。 * NORMAL：普通直播间，直播间一直存在，可以反复开播 * TEMP：临时直播间，直播任务结束后自动清理直播间。 * TEMPLATE：直播间模板。

        :return: The room_type of this ListSmartLiveRoomsRequest.
        :rtype: str
        """
        return self._room_type

    @room_type.setter
    def room_type(self, room_type):
        r"""Sets the room_type of this ListSmartLiveRoomsRequest.

        按直播间类型查询。直播间类型。 * NORMAL：普通直播间，直播间一直存在，可以反复开播 * TEMP：临时直播间，直播任务结束后自动清理直播间。 * TEMPLATE：直播间模板。

        :param room_type: The room_type of this ListSmartLiveRoomsRequest.
        :type room_type: str
        """
        self._room_type = room_type

    @property
    def template_own_type(self):
        r"""Gets the template_own_type of this ListSmartLiveRoomsRequest.

        按照自己拥有的和别人分享以及公共的模板进行查询 * OWNED 自己拥有且暂未共享的 * SHARED_TO_OHTERS 分享给别人的 * SHARED_FROM_OHTERS 别人分享给我的 * PUBLIC 公共模板

        :return: The template_own_type of this ListSmartLiveRoomsRequest.
        :rtype: str
        """
        return self._template_own_type

    @template_own_type.setter
    def template_own_type(self, template_own_type):
        r"""Sets the template_own_type of this ListSmartLiveRoomsRequest.

        按照自己拥有的和别人分享以及公共的模板进行查询 * OWNED 自己拥有且暂未共享的 * SHARED_TO_OHTERS 分享给别人的 * SHARED_FROM_OHTERS 别人分享给我的 * PUBLIC 公共模板

        :param template_own_type: The template_own_type of this ListSmartLiveRoomsRequest.
        :type template_own_type: str
        """
        self._template_own_type = template_own_type

    @property
    def confirm_state(self):
        r"""Gets the confirm_state of this ListSmartLiveRoomsRequest.

        直播间确认状态。此状态仅用于特定用户需要人工确认场景。 - unconfirm: 未确认 - confirmed：已确认 - reject： 拒绝

        :return: The confirm_state of this ListSmartLiveRoomsRequest.
        :rtype: str
        """
        return self._confirm_state

    @confirm_state.setter
    def confirm_state(self, confirm_state):
        r"""Sets the confirm_state of this ListSmartLiveRoomsRequest.

        直播间确认状态。此状态仅用于特定用户需要人工确认场景。 - unconfirm: 未确认 - confirmed：已确认 - reject： 拒绝

        :param confirm_state: The confirm_state of this ListSmartLiveRoomsRequest.
        :type confirm_state: str
        """
        self._confirm_state = confirm_state

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
        if not isinstance(other, ListSmartLiveRoomsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
