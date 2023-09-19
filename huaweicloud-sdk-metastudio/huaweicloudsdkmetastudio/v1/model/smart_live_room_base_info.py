# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SmartLiveRoomBaseInfo:

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
        'room_name': 'str',
        'room_description': 'str',
        'cover_url': 'str',
        'model_infos': 'list[ModelInfo]',
        'create_time': 'str',
        'update_time': 'str',
        'last_job_start_time': 'str',
        'last_job_end_time': 'str',
        'last_job_status': 'str'
    }

    attribute_map = {
        'room_id': 'room_id',
        'room_name': 'room_name',
        'room_description': 'room_description',
        'cover_url': 'cover_url',
        'model_infos': 'model_infos',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'last_job_start_time': 'last_job_start_time',
        'last_job_end_time': 'last_job_end_time',
        'last_job_status': 'last_job_status'
    }

    def __init__(self, room_id=None, room_name=None, room_description=None, cover_url=None, model_infos=None, create_time=None, update_time=None, last_job_start_time=None, last_job_end_time=None, last_job_status=None):
        """SmartLiveRoomBaseInfo

        The model defined in huaweicloud sdk

        :param room_id: 直播间ID
        :type room_id: str
        :param room_name: 直播间名称
        :type room_name: str
        :param room_description: 直播间描述。
        :type room_description: str
        :param cover_url: 直播间封面图URL
        :type cover_url: str
        :param model_infos: 数字人模型信息
        :type model_infos: list[:class:`huaweicloudsdkmetastudio.v1.ModelInfo`]
        :param create_time: 创建时间，格式遵循：RFC 3339 如\&quot;2021-01-10T08:43:17Z\&quot;。
        :type create_time: str
        :param update_time: 更新时间，格式遵循：RFC 3339 如\&quot;2021-01-10T08:43:17Z\&quot;。
        :type update_time: str
        :param last_job_start_time: 开始直播时间，格式遵循：RFC 3339 如\&quot;2021-01-10T08:43:17Z\&quot;。
        :type last_job_start_time: str
        :param last_job_end_time: 结束直播时间，格式遵循：RFC 3339 如\&quot;2021-01-10T08:43:17Z\&quot;。
        :type last_job_end_time: str
        :param last_job_status: 当前直播状态 - WAITING：任务等待执行 - PROCESSING：任务执行中 - SUCCEED：任务处理成功 - FAILED：任务处理时变 - CANCELED：任务取消
        :type last_job_status: str
        """
        
        

        self._room_id = None
        self._room_name = None
        self._room_description = None
        self._cover_url = None
        self._model_infos = None
        self._create_time = None
        self._update_time = None
        self._last_job_start_time = None
        self._last_job_end_time = None
        self._last_job_status = None
        self.discriminator = None

        if room_id is not None:
            self.room_id = room_id
        if room_name is not None:
            self.room_name = room_name
        if room_description is not None:
            self.room_description = room_description
        if cover_url is not None:
            self.cover_url = cover_url
        if model_infos is not None:
            self.model_infos = model_infos
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if last_job_start_time is not None:
            self.last_job_start_time = last_job_start_time
        if last_job_end_time is not None:
            self.last_job_end_time = last_job_end_time
        if last_job_status is not None:
            self.last_job_status = last_job_status

    @property
    def room_id(self):
        """Gets the room_id of this SmartLiveRoomBaseInfo.

        直播间ID

        :return: The room_id of this SmartLiveRoomBaseInfo.
        :rtype: str
        """
        return self._room_id

    @room_id.setter
    def room_id(self, room_id):
        """Sets the room_id of this SmartLiveRoomBaseInfo.

        直播间ID

        :param room_id: The room_id of this SmartLiveRoomBaseInfo.
        :type room_id: str
        """
        self._room_id = room_id

    @property
    def room_name(self):
        """Gets the room_name of this SmartLiveRoomBaseInfo.

        直播间名称

        :return: The room_name of this SmartLiveRoomBaseInfo.
        :rtype: str
        """
        return self._room_name

    @room_name.setter
    def room_name(self, room_name):
        """Sets the room_name of this SmartLiveRoomBaseInfo.

        直播间名称

        :param room_name: The room_name of this SmartLiveRoomBaseInfo.
        :type room_name: str
        """
        self._room_name = room_name

    @property
    def room_description(self):
        """Gets the room_description of this SmartLiveRoomBaseInfo.

        直播间描述。

        :return: The room_description of this SmartLiveRoomBaseInfo.
        :rtype: str
        """
        return self._room_description

    @room_description.setter
    def room_description(self, room_description):
        """Sets the room_description of this SmartLiveRoomBaseInfo.

        直播间描述。

        :param room_description: The room_description of this SmartLiveRoomBaseInfo.
        :type room_description: str
        """
        self._room_description = room_description

    @property
    def cover_url(self):
        """Gets the cover_url of this SmartLiveRoomBaseInfo.

        直播间封面图URL

        :return: The cover_url of this SmartLiveRoomBaseInfo.
        :rtype: str
        """
        return self._cover_url

    @cover_url.setter
    def cover_url(self, cover_url):
        """Sets the cover_url of this SmartLiveRoomBaseInfo.

        直播间封面图URL

        :param cover_url: The cover_url of this SmartLiveRoomBaseInfo.
        :type cover_url: str
        """
        self._cover_url = cover_url

    @property
    def model_infos(self):
        """Gets the model_infos of this SmartLiveRoomBaseInfo.

        数字人模型信息

        :return: The model_infos of this SmartLiveRoomBaseInfo.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.ModelInfo`]
        """
        return self._model_infos

    @model_infos.setter
    def model_infos(self, model_infos):
        """Sets the model_infos of this SmartLiveRoomBaseInfo.

        数字人模型信息

        :param model_infos: The model_infos of this SmartLiveRoomBaseInfo.
        :type model_infos: list[:class:`huaweicloudsdkmetastudio.v1.ModelInfo`]
        """
        self._model_infos = model_infos

    @property
    def create_time(self):
        """Gets the create_time of this SmartLiveRoomBaseInfo.

        创建时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :return: The create_time of this SmartLiveRoomBaseInfo.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this SmartLiveRoomBaseInfo.

        创建时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :param create_time: The create_time of this SmartLiveRoomBaseInfo.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this SmartLiveRoomBaseInfo.

        更新时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :return: The update_time of this SmartLiveRoomBaseInfo.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this SmartLiveRoomBaseInfo.

        更新时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :param update_time: The update_time of this SmartLiveRoomBaseInfo.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def last_job_start_time(self):
        """Gets the last_job_start_time of this SmartLiveRoomBaseInfo.

        开始直播时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :return: The last_job_start_time of this SmartLiveRoomBaseInfo.
        :rtype: str
        """
        return self._last_job_start_time

    @last_job_start_time.setter
    def last_job_start_time(self, last_job_start_time):
        """Sets the last_job_start_time of this SmartLiveRoomBaseInfo.

        开始直播时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :param last_job_start_time: The last_job_start_time of this SmartLiveRoomBaseInfo.
        :type last_job_start_time: str
        """
        self._last_job_start_time = last_job_start_time

    @property
    def last_job_end_time(self):
        """Gets the last_job_end_time of this SmartLiveRoomBaseInfo.

        结束直播时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :return: The last_job_end_time of this SmartLiveRoomBaseInfo.
        :rtype: str
        """
        return self._last_job_end_time

    @last_job_end_time.setter
    def last_job_end_time(self, last_job_end_time):
        """Sets the last_job_end_time of this SmartLiveRoomBaseInfo.

        结束直播时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :param last_job_end_time: The last_job_end_time of this SmartLiveRoomBaseInfo.
        :type last_job_end_time: str
        """
        self._last_job_end_time = last_job_end_time

    @property
    def last_job_status(self):
        """Gets the last_job_status of this SmartLiveRoomBaseInfo.

        当前直播状态 - WAITING：任务等待执行 - PROCESSING：任务执行中 - SUCCEED：任务处理成功 - FAILED：任务处理时变 - CANCELED：任务取消

        :return: The last_job_status of this SmartLiveRoomBaseInfo.
        :rtype: str
        """
        return self._last_job_status

    @last_job_status.setter
    def last_job_status(self, last_job_status):
        """Sets the last_job_status of this SmartLiveRoomBaseInfo.

        当前直播状态 - WAITING：任务等待执行 - PROCESSING：任务执行中 - SUCCEED：任务处理成功 - FAILED：任务处理时变 - CANCELED：任务取消

        :param last_job_status: The last_job_status of this SmartLiveRoomBaseInfo.
        :type last_job_status: str
        """
        self._last_job_status = last_job_status

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
        if not isinstance(other, SmartLiveRoomBaseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
