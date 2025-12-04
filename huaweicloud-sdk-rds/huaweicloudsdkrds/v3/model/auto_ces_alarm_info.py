# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AutoCesAlarmInfo:

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
        'domain_id': 'str',
        'domain_name': 'str',
        'user_id': 'str',
        'user_name': 'str',
        'project_id': 'str',
        'project_name': 'str',
        'engine_name': 'str',
        'new_instance_default': 'bool',
        'switch_status': 'str',
        'alarm_id': 'str',
        'topic_urn': 'str',
        'created_at': 'int',
        'updated_at': 'int'
    }

    attribute_map = {
        'id': 'id',
        'domain_id': 'domain_id',
        'domain_name': 'domain_name',
        'user_id': 'user_id',
        'user_name': 'user_name',
        'project_id': 'project_id',
        'project_name': 'project_name',
        'engine_name': 'engine_name',
        'new_instance_default': 'new_instance_default',
        'switch_status': 'switch_status',
        'alarm_id': 'alarm_id',
        'topic_urn': 'topic_urn',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, domain_id=None, domain_name=None, user_id=None, user_name=None, project_id=None, project_name=None, engine_name=None, new_instance_default=None, switch_status=None, alarm_id=None, topic_urn=None, created_at=None, updated_at=None):
        r"""AutoCesAlarmInfo

        The model defined in huaweicloud sdk

        :param id: **参数解释**：  告警记录唯一标识符。  **约束限制**：  不涉及。
        :type id: str
        :param domain_id: **参数解释**：  租户ID。  **约束限制**：  不涉及。
        :type domain_id: str
        :param domain_name: **参数解释**：  租户名称。  **约束限制**：  不涉及。
        :type domain_name: str
        :param user_id: **参数解释**：  用户ID。  **约束限制**：  不涉及。
        :type user_id: str
        :param user_name: **参数解释**：  用户名称。  **约束限制**：  不涉及。
        :type user_name: str
        :param project_id: **参数解释**：  项目ID。  **约束限制**：  不涉及。
        :type project_id: str
        :param project_name: **参数解释**：  项目名称。  **约束限制**：  不涉及。
        :type project_name: str
        :param engine_name: **参数解释**：  数据库引擎名称。  **约束限制**：  不涉及。
        :type engine_name: str
        :param new_instance_default: **参数解释**：  新实例是否默认开启自动告警。  **约束限制**：  不涉及。
        :type new_instance_default: bool
        :param switch_status: **参数解释**：  自动告警状态转换。  **约束限制**：  不涉及。
        :type switch_status: str
        :param alarm_id: **参数解释**：  告警规则唯一标识符。  **约束限制**：  不涉及。
        :type alarm_id: str
        :param topic_urn: **参数解释**：  主题URN。  **约束限制**：  不涉及。
        :type topic_urn: str
        :param created_at: **参数解释**：  记录被创建的时间戳。  **约束限制**：  不涉及。
        :type created_at: int
        :param updated_at: **参数解释**：  记录最后一次被更新的时间戳。  **约束限制**：  不涉及。
        :type updated_at: int
        """
        
        

        self._id = None
        self._domain_id = None
        self._domain_name = None
        self._user_id = None
        self._user_name = None
        self._project_id = None
        self._project_name = None
        self._engine_name = None
        self._new_instance_default = None
        self._switch_status = None
        self._alarm_id = None
        self._topic_urn = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if domain_id is not None:
            self.domain_id = domain_id
        if domain_name is not None:
            self.domain_name = domain_name
        if user_id is not None:
            self.user_id = user_id
        if user_name is not None:
            self.user_name = user_name
        if project_id is not None:
            self.project_id = project_id
        if project_name is not None:
            self.project_name = project_name
        if engine_name is not None:
            self.engine_name = engine_name
        if new_instance_default is not None:
            self.new_instance_default = new_instance_default
        if switch_status is not None:
            self.switch_status = switch_status
        if alarm_id is not None:
            self.alarm_id = alarm_id
        if topic_urn is not None:
            self.topic_urn = topic_urn
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def id(self):
        r"""Gets the id of this AutoCesAlarmInfo.

        **参数解释**：  告警记录唯一标识符。  **约束限制**：  不涉及。

        :return: The id of this AutoCesAlarmInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this AutoCesAlarmInfo.

        **参数解释**：  告警记录唯一标识符。  **约束限制**：  不涉及。

        :param id: The id of this AutoCesAlarmInfo.
        :type id: str
        """
        self._id = id

    @property
    def domain_id(self):
        r"""Gets the domain_id of this AutoCesAlarmInfo.

        **参数解释**：  租户ID。  **约束限制**：  不涉及。

        :return: The domain_id of this AutoCesAlarmInfo.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this AutoCesAlarmInfo.

        **参数解释**：  租户ID。  **约束限制**：  不涉及。

        :param domain_id: The domain_id of this AutoCesAlarmInfo.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def domain_name(self):
        r"""Gets the domain_name of this AutoCesAlarmInfo.

        **参数解释**：  租户名称。  **约束限制**：  不涉及。

        :return: The domain_name of this AutoCesAlarmInfo.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        r"""Sets the domain_name of this AutoCesAlarmInfo.

        **参数解释**：  租户名称。  **约束限制**：  不涉及。

        :param domain_name: The domain_name of this AutoCesAlarmInfo.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def user_id(self):
        r"""Gets the user_id of this AutoCesAlarmInfo.

        **参数解释**：  用户ID。  **约束限制**：  不涉及。

        :return: The user_id of this AutoCesAlarmInfo.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this AutoCesAlarmInfo.

        **参数解释**：  用户ID。  **约束限制**：  不涉及。

        :param user_id: The user_id of this AutoCesAlarmInfo.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def user_name(self):
        r"""Gets the user_name of this AutoCesAlarmInfo.

        **参数解释**：  用户名称。  **约束限制**：  不涉及。

        :return: The user_name of this AutoCesAlarmInfo.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this AutoCesAlarmInfo.

        **参数解释**：  用户名称。  **约束限制**：  不涉及。

        :param user_name: The user_name of this AutoCesAlarmInfo.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def project_id(self):
        r"""Gets the project_id of this AutoCesAlarmInfo.

        **参数解释**：  项目ID。  **约束限制**：  不涉及。

        :return: The project_id of this AutoCesAlarmInfo.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this AutoCesAlarmInfo.

        **参数解释**：  项目ID。  **约束限制**：  不涉及。

        :param project_id: The project_id of this AutoCesAlarmInfo.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def project_name(self):
        r"""Gets the project_name of this AutoCesAlarmInfo.

        **参数解释**：  项目名称。  **约束限制**：  不涉及。

        :return: The project_name of this AutoCesAlarmInfo.
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        r"""Sets the project_name of this AutoCesAlarmInfo.

        **参数解释**：  项目名称。  **约束限制**：  不涉及。

        :param project_name: The project_name of this AutoCesAlarmInfo.
        :type project_name: str
        """
        self._project_name = project_name

    @property
    def engine_name(self):
        r"""Gets the engine_name of this AutoCesAlarmInfo.

        **参数解释**：  数据库引擎名称。  **约束限制**：  不涉及。

        :return: The engine_name of this AutoCesAlarmInfo.
        :rtype: str
        """
        return self._engine_name

    @engine_name.setter
    def engine_name(self, engine_name):
        r"""Sets the engine_name of this AutoCesAlarmInfo.

        **参数解释**：  数据库引擎名称。  **约束限制**：  不涉及。

        :param engine_name: The engine_name of this AutoCesAlarmInfo.
        :type engine_name: str
        """
        self._engine_name = engine_name

    @property
    def new_instance_default(self):
        r"""Gets the new_instance_default of this AutoCesAlarmInfo.

        **参数解释**：  新实例是否默认开启自动告警。  **约束限制**：  不涉及。

        :return: The new_instance_default of this AutoCesAlarmInfo.
        :rtype: bool
        """
        return self._new_instance_default

    @new_instance_default.setter
    def new_instance_default(self, new_instance_default):
        r"""Sets the new_instance_default of this AutoCesAlarmInfo.

        **参数解释**：  新实例是否默认开启自动告警。  **约束限制**：  不涉及。

        :param new_instance_default: The new_instance_default of this AutoCesAlarmInfo.
        :type new_instance_default: bool
        """
        self._new_instance_default = new_instance_default

    @property
    def switch_status(self):
        r"""Gets the switch_status of this AutoCesAlarmInfo.

        **参数解释**：  自动告警状态转换。  **约束限制**：  不涉及。

        :return: The switch_status of this AutoCesAlarmInfo.
        :rtype: str
        """
        return self._switch_status

    @switch_status.setter
    def switch_status(self, switch_status):
        r"""Sets the switch_status of this AutoCesAlarmInfo.

        **参数解释**：  自动告警状态转换。  **约束限制**：  不涉及。

        :param switch_status: The switch_status of this AutoCesAlarmInfo.
        :type switch_status: str
        """
        self._switch_status = switch_status

    @property
    def alarm_id(self):
        r"""Gets the alarm_id of this AutoCesAlarmInfo.

        **参数解释**：  告警规则唯一标识符。  **约束限制**：  不涉及。

        :return: The alarm_id of this AutoCesAlarmInfo.
        :rtype: str
        """
        return self._alarm_id

    @alarm_id.setter
    def alarm_id(self, alarm_id):
        r"""Sets the alarm_id of this AutoCesAlarmInfo.

        **参数解释**：  告警规则唯一标识符。  **约束限制**：  不涉及。

        :param alarm_id: The alarm_id of this AutoCesAlarmInfo.
        :type alarm_id: str
        """
        self._alarm_id = alarm_id

    @property
    def topic_urn(self):
        r"""Gets the topic_urn of this AutoCesAlarmInfo.

        **参数解释**：  主题URN。  **约束限制**：  不涉及。

        :return: The topic_urn of this AutoCesAlarmInfo.
        :rtype: str
        """
        return self._topic_urn

    @topic_urn.setter
    def topic_urn(self, topic_urn):
        r"""Sets the topic_urn of this AutoCesAlarmInfo.

        **参数解释**：  主题URN。  **约束限制**：  不涉及。

        :param topic_urn: The topic_urn of this AutoCesAlarmInfo.
        :type topic_urn: str
        """
        self._topic_urn = topic_urn

    @property
    def created_at(self):
        r"""Gets the created_at of this AutoCesAlarmInfo.

        **参数解释**：  记录被创建的时间戳。  **约束限制**：  不涉及。

        :return: The created_at of this AutoCesAlarmInfo.
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this AutoCesAlarmInfo.

        **参数解释**：  记录被创建的时间戳。  **约束限制**：  不涉及。

        :param created_at: The created_at of this AutoCesAlarmInfo.
        :type created_at: int
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this AutoCesAlarmInfo.

        **参数解释**：  记录最后一次被更新的时间戳。  **约束限制**：  不涉及。

        :return: The updated_at of this AutoCesAlarmInfo.
        :rtype: int
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this AutoCesAlarmInfo.

        **参数解释**：  记录最后一次被更新的时间戳。  **约束限制**：  不涉及。

        :param updated_at: The updated_at of this AutoCesAlarmInfo.
        :type updated_at: int
        """
        self._updated_at = updated_at

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
        if not isinstance(other, AutoCesAlarmInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
