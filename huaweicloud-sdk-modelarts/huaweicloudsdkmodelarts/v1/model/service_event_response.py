# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ServiceEventResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'service_id': 'str',
        'service_version_id': 'str',
        'event_count': 'int',
        'event_type': 'str',
        'event_info': 'str',
        'event_info_cn': 'str',
        'create_at': 'int',
        'update_at': 'int'
    }

    attribute_map = {
        'id': 'id',
        'service_id': 'service_id',
        'service_version_id': 'service_version_id',
        'event_count': 'event_count',
        'event_type': 'event_type',
        'event_info': 'event_info',
        'event_info_cn': 'event_info_cn',
        'create_at': 'create_at',
        'update_at': 'update_at'
    }

    def __init__(self, id=None, service_id=None, service_version_id=None, event_count=None, event_type=None, event_info=None, event_info_cn=None, create_at=None, update_at=None):
        r"""ServiceEventResponse

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 服务事件ID。 **取值范围：** 不涉及。
        :type id: str
        :param service_id: **参数解释：** 服务ID。 **取值范围：** 不涉及。
        :type service_id: str
        :param service_version_id: **参数解释：** 服务版本ID。 **取值范围：** 不涉及。
        :type service_version_id: str
        :param event_count: **参数解释：** 服务事件发生计数 **取值范围：** 不涉及。
        :type event_count: int
        :param event_type: **参数解释：** 服务事件类型：NORMAL/ABNORMAL/WARNING **取值范围：** 不涉及。
        :type event_type: str
        :param event_info: **参数解释：** 服务事件信息（英文） **取值范围：** 不涉及。
        :type event_info: str
        :param event_info_cn: **参数解释：** 服务事件信息（中文） **取值范围：** 不涉及。
        :type event_info_cn: str
        :param create_at: **参数解释：** 服务事件第一次发生时间 **取值范围：** 不涉及。
        :type create_at: int
        :param update_at: **参数解释：** 服务事件最后发生时间 **取值范围：** 不涉及。
        :type update_at: int
        """
        
        

        self._id = None
        self._service_id = None
        self._service_version_id = None
        self._event_count = None
        self._event_type = None
        self._event_info = None
        self._event_info_cn = None
        self._create_at = None
        self._update_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if service_id is not None:
            self.service_id = service_id
        if service_version_id is not None:
            self.service_version_id = service_version_id
        if event_count is not None:
            self.event_count = event_count
        if event_type is not None:
            self.event_type = event_type
        if event_info is not None:
            self.event_info = event_info
        if event_info_cn is not None:
            self.event_info_cn = event_info_cn
        if create_at is not None:
            self.create_at = create_at
        if update_at is not None:
            self.update_at = update_at

    @property
    def id(self):
        r"""Gets the id of this ServiceEventResponse.

        **参数解释：** 服务事件ID。 **取值范围：** 不涉及。

        :return: The id of this ServiceEventResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ServiceEventResponse.

        **参数解释：** 服务事件ID。 **取值范围：** 不涉及。

        :param id: The id of this ServiceEventResponse.
        :type id: str
        """
        self._id = id

    @property
    def service_id(self):
        r"""Gets the service_id of this ServiceEventResponse.

        **参数解释：** 服务ID。 **取值范围：** 不涉及。

        :return: The service_id of this ServiceEventResponse.
        :rtype: str
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        r"""Sets the service_id of this ServiceEventResponse.

        **参数解释：** 服务ID。 **取值范围：** 不涉及。

        :param service_id: The service_id of this ServiceEventResponse.
        :type service_id: str
        """
        self._service_id = service_id

    @property
    def service_version_id(self):
        r"""Gets the service_version_id of this ServiceEventResponse.

        **参数解释：** 服务版本ID。 **取值范围：** 不涉及。

        :return: The service_version_id of this ServiceEventResponse.
        :rtype: str
        """
        return self._service_version_id

    @service_version_id.setter
    def service_version_id(self, service_version_id):
        r"""Sets the service_version_id of this ServiceEventResponse.

        **参数解释：** 服务版本ID。 **取值范围：** 不涉及。

        :param service_version_id: The service_version_id of this ServiceEventResponse.
        :type service_version_id: str
        """
        self._service_version_id = service_version_id

    @property
    def event_count(self):
        r"""Gets the event_count of this ServiceEventResponse.

        **参数解释：** 服务事件发生计数 **取值范围：** 不涉及。

        :return: The event_count of this ServiceEventResponse.
        :rtype: int
        """
        return self._event_count

    @event_count.setter
    def event_count(self, event_count):
        r"""Sets the event_count of this ServiceEventResponse.

        **参数解释：** 服务事件发生计数 **取值范围：** 不涉及。

        :param event_count: The event_count of this ServiceEventResponse.
        :type event_count: int
        """
        self._event_count = event_count

    @property
    def event_type(self):
        r"""Gets the event_type of this ServiceEventResponse.

        **参数解释：** 服务事件类型：NORMAL/ABNORMAL/WARNING **取值范围：** 不涉及。

        :return: The event_type of this ServiceEventResponse.
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        r"""Sets the event_type of this ServiceEventResponse.

        **参数解释：** 服务事件类型：NORMAL/ABNORMAL/WARNING **取值范围：** 不涉及。

        :param event_type: The event_type of this ServiceEventResponse.
        :type event_type: str
        """
        self._event_type = event_type

    @property
    def event_info(self):
        r"""Gets the event_info of this ServiceEventResponse.

        **参数解释：** 服务事件信息（英文） **取值范围：** 不涉及。

        :return: The event_info of this ServiceEventResponse.
        :rtype: str
        """
        return self._event_info

    @event_info.setter
    def event_info(self, event_info):
        r"""Sets the event_info of this ServiceEventResponse.

        **参数解释：** 服务事件信息（英文） **取值范围：** 不涉及。

        :param event_info: The event_info of this ServiceEventResponse.
        :type event_info: str
        """
        self._event_info = event_info

    @property
    def event_info_cn(self):
        r"""Gets the event_info_cn of this ServiceEventResponse.

        **参数解释：** 服务事件信息（中文） **取值范围：** 不涉及。

        :return: The event_info_cn of this ServiceEventResponse.
        :rtype: str
        """
        return self._event_info_cn

    @event_info_cn.setter
    def event_info_cn(self, event_info_cn):
        r"""Sets the event_info_cn of this ServiceEventResponse.

        **参数解释：** 服务事件信息（中文） **取值范围：** 不涉及。

        :param event_info_cn: The event_info_cn of this ServiceEventResponse.
        :type event_info_cn: str
        """
        self._event_info_cn = event_info_cn

    @property
    def create_at(self):
        r"""Gets the create_at of this ServiceEventResponse.

        **参数解释：** 服务事件第一次发生时间 **取值范围：** 不涉及。

        :return: The create_at of this ServiceEventResponse.
        :rtype: int
        """
        return self._create_at

    @create_at.setter
    def create_at(self, create_at):
        r"""Sets the create_at of this ServiceEventResponse.

        **参数解释：** 服务事件第一次发生时间 **取值范围：** 不涉及。

        :param create_at: The create_at of this ServiceEventResponse.
        :type create_at: int
        """
        self._create_at = create_at

    @property
    def update_at(self):
        r"""Gets the update_at of this ServiceEventResponse.

        **参数解释：** 服务事件最后发生时间 **取值范围：** 不涉及。

        :return: The update_at of this ServiceEventResponse.
        :rtype: int
        """
        return self._update_at

    @update_at.setter
    def update_at(self, update_at):
        r"""Sets the update_at of this ServiceEventResponse.

        **参数解释：** 服务事件最后发生时间 **取值范围：** 不涉及。

        :param update_at: The update_at of this ServiceEventResponse.
        :type update_at: int
        """
        self._update_at = update_at

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
        if not isinstance(other, ServiceEventResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
