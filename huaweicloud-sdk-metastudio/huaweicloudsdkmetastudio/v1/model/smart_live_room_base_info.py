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
        'project_id': 'str',
        'room_name': 'str',
        'room_type': 'str',
        'room_state': 'str',
        'view_mode': 'str',
        'error_info': 'ErrorResponse',
        'shared_config': 'SharedConfig',
        'room_description': 'str',
        'cover_url': 'str',
        'thumbnail': 'str',
        'model_infos': 'list[ModelInfo]',
        'create_time': 'str',
        'update_time': 'str',
        'last_job_start_time': 'str',
        'last_job_end_time': 'str',
        'last_job_status': 'str',
        'priv_data': 'str',
        'confirm_state': 'str'
    }

    attribute_map = {
        'room_id': 'room_id',
        'project_id': 'project_id',
        'room_name': 'room_name',
        'room_type': 'room_type',
        'room_state': 'room_state',
        'view_mode': 'view_mode',
        'error_info': 'error_info',
        'shared_config': 'shared_config',
        'room_description': 'room_description',
        'cover_url': 'cover_url',
        'thumbnail': 'thumbnail',
        'model_infos': 'model_infos',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'last_job_start_time': 'last_job_start_time',
        'last_job_end_time': 'last_job_end_time',
        'last_job_status': 'last_job_status',
        'priv_data': 'priv_data',
        'confirm_state': 'confirm_state'
    }

    def __init__(self, room_id=None, project_id=None, room_name=None, room_type=None, room_state=None, view_mode=None, error_info=None, shared_config=None, room_description=None, cover_url=None, thumbnail=None, model_infos=None, create_time=None, update_time=None, last_job_start_time=None, last_job_end_time=None, last_job_status=None, priv_data=None, confirm_state=None):
        r"""SmartLiveRoomBaseInfo

        The model defined in huaweicloud sdk

        :param room_id: 直播间ID
        :type room_id: str
        :param project_id: 租户id
        :type project_id: str
        :param room_name: 直播间名称
        :type room_name: str
        :param room_type: 直播间类型。 * NORMAL：普通直播间，直播间一直存在，可以反复开播 * TEMP：临时直播间，直播任务结束后自动清理直播间。 * TEMPLATE：直播间模板。
        :type room_type: str
        :param room_state: 直播间配置状态。 - ENABLE: 直播间正常可用。 - DISABLE： 直播间不可用。不可用原因在error_info中说明。 - BLOCKED：直播间被冻结。冻结原因在error_info中说明。
        :type room_state: str
        :param view_mode: 横竖屏类型。默认值为：VERTICAL。 * LANDSCAPE：横屏。 * VERTICAL： 竖屏。
        :type view_mode: str
        :param error_info: 
        :type error_info: :class:`huaweicloudsdkmetastudio.v1.ErrorResponse`
        :param shared_config: 
        :type shared_config: :class:`huaweicloudsdkmetastudio.v1.SharedConfig`
        :param room_description: 直播间描述。
        :type room_description: str
        :param cover_url: 直播间封面图URL
        :type cover_url: str
        :param thumbnail: 直播间封面图URL
        :type thumbnail: str
        :param model_infos: 数字人模型信息
        :type model_infos: list[:class:`huaweicloudsdkmetastudio.v1.ModelInfo`]
        :param create_time: 创建时间，格式遵循：RFC 3339 如“2021-01-10T08:43:17Z”。
        :type create_time: str
        :param update_time: 更新时间，格式遵循：RFC 3339 如“2021-01-10T08:43:17Z”。
        :type update_time: str
        :param last_job_start_time: 开始直播时间，格式遵循：RFC 3339 如“2021-01-10T08:43:17Z”。
        :type last_job_start_time: str
        :param last_job_end_time: 结束直播时间，格式遵循：RFC 3339 如“2021-01-10T08:43:17Z”。
        :type last_job_end_time: str
        :param last_job_status: 当前直播状态 - WAITING：任务等待执行 - PROCESSING：任务执行中 - SUCCEED：任务处理成功 - FAILED：任务处理时变 - CANCELED：任务取消 - BLOCKED：任务被冻结
        :type last_job_status: str
        :param priv_data: 私有数据，用户填写，原样带回。
        :type priv_data: str
        :param confirm_state: 直播间确认状态。此状态仅用于特定用户需要人工确认场景。 - UNCONFIRM: 未确认 - CONFIRMED：已确认 - REJECT： 拒绝
        :type confirm_state: str
        """
        
        

        self._room_id = None
        self._project_id = None
        self._room_name = None
        self._room_type = None
        self._room_state = None
        self._view_mode = None
        self._error_info = None
        self._shared_config = None
        self._room_description = None
        self._cover_url = None
        self._thumbnail = None
        self._model_infos = None
        self._create_time = None
        self._update_time = None
        self._last_job_start_time = None
        self._last_job_end_time = None
        self._last_job_status = None
        self._priv_data = None
        self._confirm_state = None
        self.discriminator = None

        if room_id is not None:
            self.room_id = room_id
        if project_id is not None:
            self.project_id = project_id
        if room_name is not None:
            self.room_name = room_name
        if room_type is not None:
            self.room_type = room_type
        if room_state is not None:
            self.room_state = room_state
        if view_mode is not None:
            self.view_mode = view_mode
        if error_info is not None:
            self.error_info = error_info
        if shared_config is not None:
            self.shared_config = shared_config
        if room_description is not None:
            self.room_description = room_description
        if cover_url is not None:
            self.cover_url = cover_url
        if thumbnail is not None:
            self.thumbnail = thumbnail
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
        if priv_data is not None:
            self.priv_data = priv_data
        if confirm_state is not None:
            self.confirm_state = confirm_state

    @property
    def room_id(self):
        r"""Gets the room_id of this SmartLiveRoomBaseInfo.

        直播间ID

        :return: The room_id of this SmartLiveRoomBaseInfo.
        :rtype: str
        """
        return self._room_id

    @room_id.setter
    def room_id(self, room_id):
        r"""Sets the room_id of this SmartLiveRoomBaseInfo.

        直播间ID

        :param room_id: The room_id of this SmartLiveRoomBaseInfo.
        :type room_id: str
        """
        self._room_id = room_id

    @property
    def project_id(self):
        r"""Gets the project_id of this SmartLiveRoomBaseInfo.

        租户id

        :return: The project_id of this SmartLiveRoomBaseInfo.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this SmartLiveRoomBaseInfo.

        租户id

        :param project_id: The project_id of this SmartLiveRoomBaseInfo.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def room_name(self):
        r"""Gets the room_name of this SmartLiveRoomBaseInfo.

        直播间名称

        :return: The room_name of this SmartLiveRoomBaseInfo.
        :rtype: str
        """
        return self._room_name

    @room_name.setter
    def room_name(self, room_name):
        r"""Sets the room_name of this SmartLiveRoomBaseInfo.

        直播间名称

        :param room_name: The room_name of this SmartLiveRoomBaseInfo.
        :type room_name: str
        """
        self._room_name = room_name

    @property
    def room_type(self):
        r"""Gets the room_type of this SmartLiveRoomBaseInfo.

        直播间类型。 * NORMAL：普通直播间，直播间一直存在，可以反复开播 * TEMP：临时直播间，直播任务结束后自动清理直播间。 * TEMPLATE：直播间模板。

        :return: The room_type of this SmartLiveRoomBaseInfo.
        :rtype: str
        """
        return self._room_type

    @room_type.setter
    def room_type(self, room_type):
        r"""Sets the room_type of this SmartLiveRoomBaseInfo.

        直播间类型。 * NORMAL：普通直播间，直播间一直存在，可以反复开播 * TEMP：临时直播间，直播任务结束后自动清理直播间。 * TEMPLATE：直播间模板。

        :param room_type: The room_type of this SmartLiveRoomBaseInfo.
        :type room_type: str
        """
        self._room_type = room_type

    @property
    def room_state(self):
        r"""Gets the room_state of this SmartLiveRoomBaseInfo.

        直播间配置状态。 - ENABLE: 直播间正常可用。 - DISABLE： 直播间不可用。不可用原因在error_info中说明。 - BLOCKED：直播间被冻结。冻结原因在error_info中说明。

        :return: The room_state of this SmartLiveRoomBaseInfo.
        :rtype: str
        """
        return self._room_state

    @room_state.setter
    def room_state(self, room_state):
        r"""Sets the room_state of this SmartLiveRoomBaseInfo.

        直播间配置状态。 - ENABLE: 直播间正常可用。 - DISABLE： 直播间不可用。不可用原因在error_info中说明。 - BLOCKED：直播间被冻结。冻结原因在error_info中说明。

        :param room_state: The room_state of this SmartLiveRoomBaseInfo.
        :type room_state: str
        """
        self._room_state = room_state

    @property
    def view_mode(self):
        r"""Gets the view_mode of this SmartLiveRoomBaseInfo.

        横竖屏类型。默认值为：VERTICAL。 * LANDSCAPE：横屏。 * VERTICAL： 竖屏。

        :return: The view_mode of this SmartLiveRoomBaseInfo.
        :rtype: str
        """
        return self._view_mode

    @view_mode.setter
    def view_mode(self, view_mode):
        r"""Sets the view_mode of this SmartLiveRoomBaseInfo.

        横竖屏类型。默认值为：VERTICAL。 * LANDSCAPE：横屏。 * VERTICAL： 竖屏。

        :param view_mode: The view_mode of this SmartLiveRoomBaseInfo.
        :type view_mode: str
        """
        self._view_mode = view_mode

    @property
    def error_info(self):
        r"""Gets the error_info of this SmartLiveRoomBaseInfo.

        :return: The error_info of this SmartLiveRoomBaseInfo.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ErrorResponse`
        """
        return self._error_info

    @error_info.setter
    def error_info(self, error_info):
        r"""Sets the error_info of this SmartLiveRoomBaseInfo.

        :param error_info: The error_info of this SmartLiveRoomBaseInfo.
        :type error_info: :class:`huaweicloudsdkmetastudio.v1.ErrorResponse`
        """
        self._error_info = error_info

    @property
    def shared_config(self):
        r"""Gets the shared_config of this SmartLiveRoomBaseInfo.

        :return: The shared_config of this SmartLiveRoomBaseInfo.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.SharedConfig`
        """
        return self._shared_config

    @shared_config.setter
    def shared_config(self, shared_config):
        r"""Sets the shared_config of this SmartLiveRoomBaseInfo.

        :param shared_config: The shared_config of this SmartLiveRoomBaseInfo.
        :type shared_config: :class:`huaweicloudsdkmetastudio.v1.SharedConfig`
        """
        self._shared_config = shared_config

    @property
    def room_description(self):
        r"""Gets the room_description of this SmartLiveRoomBaseInfo.

        直播间描述。

        :return: The room_description of this SmartLiveRoomBaseInfo.
        :rtype: str
        """
        return self._room_description

    @room_description.setter
    def room_description(self, room_description):
        r"""Sets the room_description of this SmartLiveRoomBaseInfo.

        直播间描述。

        :param room_description: The room_description of this SmartLiveRoomBaseInfo.
        :type room_description: str
        """
        self._room_description = room_description

    @property
    def cover_url(self):
        r"""Gets the cover_url of this SmartLiveRoomBaseInfo.

        直播间封面图URL

        :return: The cover_url of this SmartLiveRoomBaseInfo.
        :rtype: str
        """
        return self._cover_url

    @cover_url.setter
    def cover_url(self, cover_url):
        r"""Sets the cover_url of this SmartLiveRoomBaseInfo.

        直播间封面图URL

        :param cover_url: The cover_url of this SmartLiveRoomBaseInfo.
        :type cover_url: str
        """
        self._cover_url = cover_url

    @property
    def thumbnail(self):
        r"""Gets the thumbnail of this SmartLiveRoomBaseInfo.

        直播间封面图URL

        :return: The thumbnail of this SmartLiveRoomBaseInfo.
        :rtype: str
        """
        return self._thumbnail

    @thumbnail.setter
    def thumbnail(self, thumbnail):
        r"""Sets the thumbnail of this SmartLiveRoomBaseInfo.

        直播间封面图URL

        :param thumbnail: The thumbnail of this SmartLiveRoomBaseInfo.
        :type thumbnail: str
        """
        self._thumbnail = thumbnail

    @property
    def model_infos(self):
        r"""Gets the model_infos of this SmartLiveRoomBaseInfo.

        数字人模型信息

        :return: The model_infos of this SmartLiveRoomBaseInfo.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.ModelInfo`]
        """
        return self._model_infos

    @model_infos.setter
    def model_infos(self, model_infos):
        r"""Sets the model_infos of this SmartLiveRoomBaseInfo.

        数字人模型信息

        :param model_infos: The model_infos of this SmartLiveRoomBaseInfo.
        :type model_infos: list[:class:`huaweicloudsdkmetastudio.v1.ModelInfo`]
        """
        self._model_infos = model_infos

    @property
    def create_time(self):
        r"""Gets the create_time of this SmartLiveRoomBaseInfo.

        创建时间，格式遵循：RFC 3339 如“2021-01-10T08:43:17Z”。

        :return: The create_time of this SmartLiveRoomBaseInfo.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this SmartLiveRoomBaseInfo.

        创建时间，格式遵循：RFC 3339 如“2021-01-10T08:43:17Z”。

        :param create_time: The create_time of this SmartLiveRoomBaseInfo.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this SmartLiveRoomBaseInfo.

        更新时间，格式遵循：RFC 3339 如“2021-01-10T08:43:17Z”。

        :return: The update_time of this SmartLiveRoomBaseInfo.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this SmartLiveRoomBaseInfo.

        更新时间，格式遵循：RFC 3339 如“2021-01-10T08:43:17Z”。

        :param update_time: The update_time of this SmartLiveRoomBaseInfo.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def last_job_start_time(self):
        r"""Gets the last_job_start_time of this SmartLiveRoomBaseInfo.

        开始直播时间，格式遵循：RFC 3339 如“2021-01-10T08:43:17Z”。

        :return: The last_job_start_time of this SmartLiveRoomBaseInfo.
        :rtype: str
        """
        return self._last_job_start_time

    @last_job_start_time.setter
    def last_job_start_time(self, last_job_start_time):
        r"""Sets the last_job_start_time of this SmartLiveRoomBaseInfo.

        开始直播时间，格式遵循：RFC 3339 如“2021-01-10T08:43:17Z”。

        :param last_job_start_time: The last_job_start_time of this SmartLiveRoomBaseInfo.
        :type last_job_start_time: str
        """
        self._last_job_start_time = last_job_start_time

    @property
    def last_job_end_time(self):
        r"""Gets the last_job_end_time of this SmartLiveRoomBaseInfo.

        结束直播时间，格式遵循：RFC 3339 如“2021-01-10T08:43:17Z”。

        :return: The last_job_end_time of this SmartLiveRoomBaseInfo.
        :rtype: str
        """
        return self._last_job_end_time

    @last_job_end_time.setter
    def last_job_end_time(self, last_job_end_time):
        r"""Sets the last_job_end_time of this SmartLiveRoomBaseInfo.

        结束直播时间，格式遵循：RFC 3339 如“2021-01-10T08:43:17Z”。

        :param last_job_end_time: The last_job_end_time of this SmartLiveRoomBaseInfo.
        :type last_job_end_time: str
        """
        self._last_job_end_time = last_job_end_time

    @property
    def last_job_status(self):
        r"""Gets the last_job_status of this SmartLiveRoomBaseInfo.

        当前直播状态 - WAITING：任务等待执行 - PROCESSING：任务执行中 - SUCCEED：任务处理成功 - FAILED：任务处理时变 - CANCELED：任务取消 - BLOCKED：任务被冻结

        :return: The last_job_status of this SmartLiveRoomBaseInfo.
        :rtype: str
        """
        return self._last_job_status

    @last_job_status.setter
    def last_job_status(self, last_job_status):
        r"""Sets the last_job_status of this SmartLiveRoomBaseInfo.

        当前直播状态 - WAITING：任务等待执行 - PROCESSING：任务执行中 - SUCCEED：任务处理成功 - FAILED：任务处理时变 - CANCELED：任务取消 - BLOCKED：任务被冻结

        :param last_job_status: The last_job_status of this SmartLiveRoomBaseInfo.
        :type last_job_status: str
        """
        self._last_job_status = last_job_status

    @property
    def priv_data(self):
        r"""Gets the priv_data of this SmartLiveRoomBaseInfo.

        私有数据，用户填写，原样带回。

        :return: The priv_data of this SmartLiveRoomBaseInfo.
        :rtype: str
        """
        return self._priv_data

    @priv_data.setter
    def priv_data(self, priv_data):
        r"""Sets the priv_data of this SmartLiveRoomBaseInfo.

        私有数据，用户填写，原样带回。

        :param priv_data: The priv_data of this SmartLiveRoomBaseInfo.
        :type priv_data: str
        """
        self._priv_data = priv_data

    @property
    def confirm_state(self):
        r"""Gets the confirm_state of this SmartLiveRoomBaseInfo.

        直播间确认状态。此状态仅用于特定用户需要人工确认场景。 - UNCONFIRM: 未确认 - CONFIRMED：已确认 - REJECT： 拒绝

        :return: The confirm_state of this SmartLiveRoomBaseInfo.
        :rtype: str
        """
        return self._confirm_state

    @confirm_state.setter
    def confirm_state(self, confirm_state):
        r"""Sets the confirm_state of this SmartLiveRoomBaseInfo.

        直播间确认状态。此状态仅用于特定用户需要人工确认场景。 - UNCONFIRM: 未确认 - CONFIRMED：已确认 - REJECT： 拒绝

        :param confirm_state: The confirm_state of this SmartLiveRoomBaseInfo.
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
        if not isinstance(other, SmartLiveRoomBaseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
