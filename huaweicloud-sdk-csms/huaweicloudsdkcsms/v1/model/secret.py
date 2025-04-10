# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Secret:

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
        'name': 'str',
        'state': 'str',
        'kms_key_id': 'str',
        'description': 'str',
        'create_time': 'int',
        'update_time': 'int',
        'scheduled_delete_time': 'int',
        'secret_type': 'str',
        'auto_rotation': 'bool',
        'rotation_period': 'str',
        'rotation_config': 'str',
        'rotation_time': 'int',
        'next_rotation_time': 'int',
        'event_subscriptions': 'list[str]',
        'enterprise_project_id': 'str',
        'rotation_func_urn': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'state': 'state',
        'kms_key_id': 'kms_key_id',
        'description': 'description',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'scheduled_delete_time': 'scheduled_delete_time',
        'secret_type': 'secret_type',
        'auto_rotation': 'auto_rotation',
        'rotation_period': 'rotation_period',
        'rotation_config': 'rotation_config',
        'rotation_time': 'rotation_time',
        'next_rotation_time': 'next_rotation_time',
        'event_subscriptions': 'event_subscriptions',
        'enterprise_project_id': 'enterprise_project_id',
        'rotation_func_urn': 'rotation_func_urn'
    }

    def __init__(self, id=None, name=None, state=None, kms_key_id=None, description=None, create_time=None, update_time=None, scheduled_delete_time=None, secret_type=None, auto_rotation=None, rotation_period=None, rotation_config=None, rotation_time=None, next_rotation_time=None, event_subscriptions=None, enterprise_project_id=None, rotation_func_urn=None):
        r"""Secret

        The model defined in huaweicloud sdk

        :param id: 凭据的资源标识符。
        :type id: str
        :param name: 凭据名称。
        :type name: str
        :param state: 凭据状态，取值如下：  ENABLED：表示启用状态  DISABLED：表示禁用状态  PENDING_DELETE：表示待删除状态  FROZEN：表示冻结状态
        :type state: str
        :param kms_key_id: 用于加密凭据值的KMS主密钥的ID值。
        :type kms_key_id: str
        :param description: 凭据的描述信息。
        :type description: str
        :param create_time: 凭据创建时间，时间戳，即从1970年1月1日至该时间的总秒数。
        :type create_time: int
        :param update_time: 凭据上次更新时间，时间戳，即从1970年1月1日至该时间的总秒数。
        :type update_time: int
        :param scheduled_delete_time: 凭据计划删除时间，时间戳，即从1970年1月1日至该时间的总秒数。  凭据不在删除计划中时，本项值为null。
        :type scheduled_delete_time: int
        :param secret_type: 凭据类型  - COMMON：通用凭据(默认)。用于应用系统中的各种敏感信息储存。 - RDS：RDS凭据 。专门针对RDS的凭据，用于存储RDS的账号信息。（已不支持，使用RDS-FG替代） - RDS-FG：RDS凭据 。专门针对RDS的凭据，用于存储RDS的账号信息。 - GaussDB-FG：TaurusDB凭据。专门针对TaurusDB的凭据，用于存储TaurusDB的账号信息。
        :type secret_type: str
        :param auto_rotation: 自动轮转  取值：true 开启, false 关闭(默认)
        :type auto_rotation: bool
        :param rotation_period: 轮转周期  约束：6小时-8,760小时 （365天）  类型：Integer[unit] ，Integer表示时间长度 。unit表示时间单位，d（天）、h（小时）、m（分钟）、s（秒）。例如 1d 表示一天，24h也表示一天  说明：当开启自动轮转时，必须填写该值
        :type rotation_period: str
        :param rotation_config: 轮转配置  约束：范围不超过1024个字符。  当secret_type为RDS-FG、GaussDB-FG时，配置为{\&quot;InstanceId\&quot;:\&quot;\&quot;,\&quot;SecretSubType\&quot;:\&quot;\&quot;}  说明：当secret_type为RDS-FG、GaussDB-FG时，必须填写该值  InstanceId为实例ID,SecretSubType为轮转子类型，取值为：SingleUser，MultiUser。  SingleUser：指定轮转类型为单用户模式轮转，每次轮转将指定账号重置为新的口令。  MultiUser：指定轮转类型为双用户模式轮转，SYSCURRENT和SYSPREVIOUS分别引用其中一个账号。凭据轮转时，SYSPREVIOUS引用的账号口令会被重置为新的随机口令，随后凭据交换SYSCURRENT和SYSPREVIOUS对账号的引用。
        :type rotation_config: str
        :param rotation_time: 轮转时间戳
        :type rotation_time: int
        :param next_rotation_time: 下一次轮转时间戳
        :type next_rotation_time: int
        :param event_subscriptions: 凭据订阅的事件列表，当前最大可订阅一个事件。当事件包含的基础事件触发时，通知消息将发送到事件对应的通知主题。
        :type event_subscriptions: list[str]
        :param enterprise_project_id: 企业项目ID
        :type enterprise_project_id: str
        :param rotation_func_urn: FunctionGraph函数的urn。
        :type rotation_func_urn: str
        """
        
        

        self._id = None
        self._name = None
        self._state = None
        self._kms_key_id = None
        self._description = None
        self._create_time = None
        self._update_time = None
        self._scheduled_delete_time = None
        self._secret_type = None
        self._auto_rotation = None
        self._rotation_period = None
        self._rotation_config = None
        self._rotation_time = None
        self._next_rotation_time = None
        self._event_subscriptions = None
        self._enterprise_project_id = None
        self._rotation_func_urn = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if state is not None:
            self.state = state
        if kms_key_id is not None:
            self.kms_key_id = kms_key_id
        if description is not None:
            self.description = description
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if scheduled_delete_time is not None:
            self.scheduled_delete_time = scheduled_delete_time
        if secret_type is not None:
            self.secret_type = secret_type
        if auto_rotation is not None:
            self.auto_rotation = auto_rotation
        if rotation_period is not None:
            self.rotation_period = rotation_period
        if rotation_config is not None:
            self.rotation_config = rotation_config
        if rotation_time is not None:
            self.rotation_time = rotation_time
        if next_rotation_time is not None:
            self.next_rotation_time = next_rotation_time
        if event_subscriptions is not None:
            self.event_subscriptions = event_subscriptions
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if rotation_func_urn is not None:
            self.rotation_func_urn = rotation_func_urn

    @property
    def id(self):
        r"""Gets the id of this Secret.

        凭据的资源标识符。

        :return: The id of this Secret.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this Secret.

        凭据的资源标识符。

        :param id: The id of this Secret.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this Secret.

        凭据名称。

        :return: The name of this Secret.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Secret.

        凭据名称。

        :param name: The name of this Secret.
        :type name: str
        """
        self._name = name

    @property
    def state(self):
        r"""Gets the state of this Secret.

        凭据状态，取值如下：  ENABLED：表示启用状态  DISABLED：表示禁用状态  PENDING_DELETE：表示待删除状态  FROZEN：表示冻结状态

        :return: The state of this Secret.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this Secret.

        凭据状态，取值如下：  ENABLED：表示启用状态  DISABLED：表示禁用状态  PENDING_DELETE：表示待删除状态  FROZEN：表示冻结状态

        :param state: The state of this Secret.
        :type state: str
        """
        self._state = state

    @property
    def kms_key_id(self):
        r"""Gets the kms_key_id of this Secret.

        用于加密凭据值的KMS主密钥的ID值。

        :return: The kms_key_id of this Secret.
        :rtype: str
        """
        return self._kms_key_id

    @kms_key_id.setter
    def kms_key_id(self, kms_key_id):
        r"""Sets the kms_key_id of this Secret.

        用于加密凭据值的KMS主密钥的ID值。

        :param kms_key_id: The kms_key_id of this Secret.
        :type kms_key_id: str
        """
        self._kms_key_id = kms_key_id

    @property
    def description(self):
        r"""Gets the description of this Secret.

        凭据的描述信息。

        :return: The description of this Secret.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this Secret.

        凭据的描述信息。

        :param description: The description of this Secret.
        :type description: str
        """
        self._description = description

    @property
    def create_time(self):
        r"""Gets the create_time of this Secret.

        凭据创建时间，时间戳，即从1970年1月1日至该时间的总秒数。

        :return: The create_time of this Secret.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this Secret.

        凭据创建时间，时间戳，即从1970年1月1日至该时间的总秒数。

        :param create_time: The create_time of this Secret.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this Secret.

        凭据上次更新时间，时间戳，即从1970年1月1日至该时间的总秒数。

        :return: The update_time of this Secret.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this Secret.

        凭据上次更新时间，时间戳，即从1970年1月1日至该时间的总秒数。

        :param update_time: The update_time of this Secret.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def scheduled_delete_time(self):
        r"""Gets the scheduled_delete_time of this Secret.

        凭据计划删除时间，时间戳，即从1970年1月1日至该时间的总秒数。  凭据不在删除计划中时，本项值为null。

        :return: The scheduled_delete_time of this Secret.
        :rtype: int
        """
        return self._scheduled_delete_time

    @scheduled_delete_time.setter
    def scheduled_delete_time(self, scheduled_delete_time):
        r"""Sets the scheduled_delete_time of this Secret.

        凭据计划删除时间，时间戳，即从1970年1月1日至该时间的总秒数。  凭据不在删除计划中时，本项值为null。

        :param scheduled_delete_time: The scheduled_delete_time of this Secret.
        :type scheduled_delete_time: int
        """
        self._scheduled_delete_time = scheduled_delete_time

    @property
    def secret_type(self):
        r"""Gets the secret_type of this Secret.

        凭据类型  - COMMON：通用凭据(默认)。用于应用系统中的各种敏感信息储存。 - RDS：RDS凭据 。专门针对RDS的凭据，用于存储RDS的账号信息。（已不支持，使用RDS-FG替代） - RDS-FG：RDS凭据 。专门针对RDS的凭据，用于存储RDS的账号信息。 - GaussDB-FG：TaurusDB凭据。专门针对TaurusDB的凭据，用于存储TaurusDB的账号信息。

        :return: The secret_type of this Secret.
        :rtype: str
        """
        return self._secret_type

    @secret_type.setter
    def secret_type(self, secret_type):
        r"""Sets the secret_type of this Secret.

        凭据类型  - COMMON：通用凭据(默认)。用于应用系统中的各种敏感信息储存。 - RDS：RDS凭据 。专门针对RDS的凭据，用于存储RDS的账号信息。（已不支持，使用RDS-FG替代） - RDS-FG：RDS凭据 。专门针对RDS的凭据，用于存储RDS的账号信息。 - GaussDB-FG：TaurusDB凭据。专门针对TaurusDB的凭据，用于存储TaurusDB的账号信息。

        :param secret_type: The secret_type of this Secret.
        :type secret_type: str
        """
        self._secret_type = secret_type

    @property
    def auto_rotation(self):
        r"""Gets the auto_rotation of this Secret.

        自动轮转  取值：true 开启, false 关闭(默认)

        :return: The auto_rotation of this Secret.
        :rtype: bool
        """
        return self._auto_rotation

    @auto_rotation.setter
    def auto_rotation(self, auto_rotation):
        r"""Sets the auto_rotation of this Secret.

        自动轮转  取值：true 开启, false 关闭(默认)

        :param auto_rotation: The auto_rotation of this Secret.
        :type auto_rotation: bool
        """
        self._auto_rotation = auto_rotation

    @property
    def rotation_period(self):
        r"""Gets the rotation_period of this Secret.

        轮转周期  约束：6小时-8,760小时 （365天）  类型：Integer[unit] ，Integer表示时间长度 。unit表示时间单位，d（天）、h（小时）、m（分钟）、s（秒）。例如 1d 表示一天，24h也表示一天  说明：当开启自动轮转时，必须填写该值

        :return: The rotation_period of this Secret.
        :rtype: str
        """
        return self._rotation_period

    @rotation_period.setter
    def rotation_period(self, rotation_period):
        r"""Sets the rotation_period of this Secret.

        轮转周期  约束：6小时-8,760小时 （365天）  类型：Integer[unit] ，Integer表示时间长度 。unit表示时间单位，d（天）、h（小时）、m（分钟）、s（秒）。例如 1d 表示一天，24h也表示一天  说明：当开启自动轮转时，必须填写该值

        :param rotation_period: The rotation_period of this Secret.
        :type rotation_period: str
        """
        self._rotation_period = rotation_period

    @property
    def rotation_config(self):
        r"""Gets the rotation_config of this Secret.

        轮转配置  约束：范围不超过1024个字符。  当secret_type为RDS-FG、GaussDB-FG时，配置为{\"InstanceId\":\"\",\"SecretSubType\":\"\"}  说明：当secret_type为RDS-FG、GaussDB-FG时，必须填写该值  InstanceId为实例ID,SecretSubType为轮转子类型，取值为：SingleUser，MultiUser。  SingleUser：指定轮转类型为单用户模式轮转，每次轮转将指定账号重置为新的口令。  MultiUser：指定轮转类型为双用户模式轮转，SYSCURRENT和SYSPREVIOUS分别引用其中一个账号。凭据轮转时，SYSPREVIOUS引用的账号口令会被重置为新的随机口令，随后凭据交换SYSCURRENT和SYSPREVIOUS对账号的引用。

        :return: The rotation_config of this Secret.
        :rtype: str
        """
        return self._rotation_config

    @rotation_config.setter
    def rotation_config(self, rotation_config):
        r"""Sets the rotation_config of this Secret.

        轮转配置  约束：范围不超过1024个字符。  当secret_type为RDS-FG、GaussDB-FG时，配置为{\"InstanceId\":\"\",\"SecretSubType\":\"\"}  说明：当secret_type为RDS-FG、GaussDB-FG时，必须填写该值  InstanceId为实例ID,SecretSubType为轮转子类型，取值为：SingleUser，MultiUser。  SingleUser：指定轮转类型为单用户模式轮转，每次轮转将指定账号重置为新的口令。  MultiUser：指定轮转类型为双用户模式轮转，SYSCURRENT和SYSPREVIOUS分别引用其中一个账号。凭据轮转时，SYSPREVIOUS引用的账号口令会被重置为新的随机口令，随后凭据交换SYSCURRENT和SYSPREVIOUS对账号的引用。

        :param rotation_config: The rotation_config of this Secret.
        :type rotation_config: str
        """
        self._rotation_config = rotation_config

    @property
    def rotation_time(self):
        r"""Gets the rotation_time of this Secret.

        轮转时间戳

        :return: The rotation_time of this Secret.
        :rtype: int
        """
        return self._rotation_time

    @rotation_time.setter
    def rotation_time(self, rotation_time):
        r"""Sets the rotation_time of this Secret.

        轮转时间戳

        :param rotation_time: The rotation_time of this Secret.
        :type rotation_time: int
        """
        self._rotation_time = rotation_time

    @property
    def next_rotation_time(self):
        r"""Gets the next_rotation_time of this Secret.

        下一次轮转时间戳

        :return: The next_rotation_time of this Secret.
        :rtype: int
        """
        return self._next_rotation_time

    @next_rotation_time.setter
    def next_rotation_time(self, next_rotation_time):
        r"""Sets the next_rotation_time of this Secret.

        下一次轮转时间戳

        :param next_rotation_time: The next_rotation_time of this Secret.
        :type next_rotation_time: int
        """
        self._next_rotation_time = next_rotation_time

    @property
    def event_subscriptions(self):
        r"""Gets the event_subscriptions of this Secret.

        凭据订阅的事件列表，当前最大可订阅一个事件。当事件包含的基础事件触发时，通知消息将发送到事件对应的通知主题。

        :return: The event_subscriptions of this Secret.
        :rtype: list[str]
        """
        return self._event_subscriptions

    @event_subscriptions.setter
    def event_subscriptions(self, event_subscriptions):
        r"""Sets the event_subscriptions of this Secret.

        凭据订阅的事件列表，当前最大可订阅一个事件。当事件包含的基础事件触发时，通知消息将发送到事件对应的通知主题。

        :param event_subscriptions: The event_subscriptions of this Secret.
        :type event_subscriptions: list[str]
        """
        self._event_subscriptions = event_subscriptions

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this Secret.

        企业项目ID

        :return: The enterprise_project_id of this Secret.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this Secret.

        企业项目ID

        :param enterprise_project_id: The enterprise_project_id of this Secret.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def rotation_func_urn(self):
        r"""Gets the rotation_func_urn of this Secret.

        FunctionGraph函数的urn。

        :return: The rotation_func_urn of this Secret.
        :rtype: str
        """
        return self._rotation_func_urn

    @rotation_func_urn.setter
    def rotation_func_urn(self, rotation_func_urn):
        r"""Sets the rotation_func_urn of this Secret.

        FunctionGraph函数的urn。

        :param rotation_func_urn: The rotation_func_urn of this Secret.
        :type rotation_func_urn: str
        """
        self._rotation_func_urn = rotation_func_urn

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
        if not isinstance(other, Secret):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
