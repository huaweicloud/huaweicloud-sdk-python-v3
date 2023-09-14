# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSecretRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'kms_key_id': 'str',
        'description': 'str',
        'secret_binary': 'str',
        'secret_string': 'str',
        'secret_type': 'str',
        'auto_rotation': 'bool',
        'rotation_period': 'str',
        'rotation_config': 'str',
        'event_subscriptions': 'list[str]',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'kms_key_id': 'kms_key_id',
        'description': 'description',
        'secret_binary': 'secret_binary',
        'secret_string': 'secret_string',
        'secret_type': 'secret_type',
        'auto_rotation': 'auto_rotation',
        'rotation_period': 'rotation_period',
        'rotation_config': 'rotation_config',
        'event_subscriptions': 'event_subscriptions',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, name=None, kms_key_id=None, description=None, secret_binary=None, secret_string=None, secret_type=None, auto_rotation=None, rotation_period=None, rotation_config=None, event_subscriptions=None, enterprise_project_id=None):
        """CreateSecretRequestBody

        The model defined in huaweicloud sdk

        :param name: 待创建凭据的名称。  约束：取值范围为1到64个字符，满足正则匹配“^[a-zA-Z0-9_-]{1,64}$”。
        :type name: str
        :param kms_key_id: 用于加密保护凭据值的KMS主密钥ID，如果您未指定此参数，凭据管理服务将默认使用名为csms/default的默认主密钥，用于加密您账号在本项目中创建的凭据值。如果用户账号下不存在该名称的主密钥，则凭据管理服务自动为您创建该名称的密钥。
        :type kms_key_id: str
        :param description: 凭据的描述信息。  约束：2048字节。
        :type description: str
        :param secret_binary: 二进制类型凭据在base64编码后的明文，凭据管理服务将其加密后，存入凭据的初始版本中。  类型：base64编码的二进制数据对象。  约束：secret_binary和secret_string必须且只能设置一个，最大32K。 当secret_type为RDS时。凭据值格式为： \&quot;{&#39;users&#39;:[{&#39;name&#39;:&#39;&#39;,&#39;password&#39;:&#39;&#39;}]}\&quot; 其中name为RDS实例账号名称，password为RDS实例账号口令
        :type secret_binary: str
        :param secret_string: 文本类型凭据的明文，凭据管理服务将其加密后，存入凭据的初始版本中。  约束：secret_binary和secret_string必须且只能设置一个，最大32K。
        :type secret_string: str
        :param secret_type: 凭据类型  取值 ： COMMON ：通用凭据(默认)。用于应用系统中的各种敏感信息储存。         RDS ：RDS凭据 。专门针对RDS的凭据，用于存储RDS的账号信息。
        :type secret_type: str
        :param auto_rotation: 自动轮转  取值：true 开启 ,false 关闭 (默认)
        :type auto_rotation: bool
        :param rotation_period: 轮转周期  约束：6小时-8,760小时 （365天）  类型：Integer[unit] ，Integer表示时间长度 。unit表示时间单位，d（天）、h（小时）、m（分钟）、s（秒）。例如 1d 表示一天，24h也表示一天  说明：当开启自动轮转时，必须填写该值
        :type rotation_period: str
        :param rotation_config: 轮转配置  约束：范围不超过1024个字符。  当secret_type为RDS时，配置为{\&quot;rds_instance_id\&quot;:\&quot;\&quot;,\&quot;Secret_sub_type\&quot;:\&quot;\&quot;}  说明：当secret_type为RDS时，必须填写该值  rds_instance_id为RDS的实例ID,Secret_sub_type为轮转子类型，取值为：SingleUser，MultiUser。  SingleUser：指定轮转类型为单用户模式轮转，每次轮转将指定账号重置为新的口令。  MultiUser：指定轮转类型为双用户模式轮转，SYSCURRENT和SYSPREVIOUS分别引用其中一个账号。凭据轮转时，SYSPREVIOUS引用的账号口令会被重置为新的随机口令，随后凭据交换SYSCURRENT和SYSPREVIOUS对RDS账号的引用。
        :type rotation_config: str
        :param event_subscriptions: 凭据订阅的事件列表，当前最大可订阅一个事件。当事件包含的基础事件触发时，通知消息将发送到事件对应的通知主题。
        :type event_subscriptions: list[str]
        :param enterprise_project_id: 该参数针对企业用户使用。如果您是企业用户，且已创建企业项目，则请从下拉列表中为密钥选择需要绑定的企业项目，默认项目为“default”。 未开通企业管理的用户页面则没有“企业项目”参数项，无需进行配置。
        :type enterprise_project_id: str
        """
        
        

        self._name = None
        self._kms_key_id = None
        self._description = None
        self._secret_binary = None
        self._secret_string = None
        self._secret_type = None
        self._auto_rotation = None
        self._rotation_period = None
        self._rotation_config = None
        self._event_subscriptions = None
        self._enterprise_project_id = None
        self.discriminator = None

        self.name = name
        if kms_key_id is not None:
            self.kms_key_id = kms_key_id
        if description is not None:
            self.description = description
        if secret_binary is not None:
            self.secret_binary = secret_binary
        if secret_string is not None:
            self.secret_string = secret_string
        if secret_type is not None:
            self.secret_type = secret_type
        if auto_rotation is not None:
            self.auto_rotation = auto_rotation
        if rotation_period is not None:
            self.rotation_period = rotation_period
        if rotation_config is not None:
            self.rotation_config = rotation_config
        if event_subscriptions is not None:
            self.event_subscriptions = event_subscriptions
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def name(self):
        """Gets the name of this CreateSecretRequestBody.

        待创建凭据的名称。  约束：取值范围为1到64个字符，满足正则匹配“^[a-zA-Z0-9_-]{1,64}$”。

        :return: The name of this CreateSecretRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateSecretRequestBody.

        待创建凭据的名称。  约束：取值范围为1到64个字符，满足正则匹配“^[a-zA-Z0-9_-]{1,64}$”。

        :param name: The name of this CreateSecretRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def kms_key_id(self):
        """Gets the kms_key_id of this CreateSecretRequestBody.

        用于加密保护凭据值的KMS主密钥ID，如果您未指定此参数，凭据管理服务将默认使用名为csms/default的默认主密钥，用于加密您账号在本项目中创建的凭据值。如果用户账号下不存在该名称的主密钥，则凭据管理服务自动为您创建该名称的密钥。

        :return: The kms_key_id of this CreateSecretRequestBody.
        :rtype: str
        """
        return self._kms_key_id

    @kms_key_id.setter
    def kms_key_id(self, kms_key_id):
        """Sets the kms_key_id of this CreateSecretRequestBody.

        用于加密保护凭据值的KMS主密钥ID，如果您未指定此参数，凭据管理服务将默认使用名为csms/default的默认主密钥，用于加密您账号在本项目中创建的凭据值。如果用户账号下不存在该名称的主密钥，则凭据管理服务自动为您创建该名称的密钥。

        :param kms_key_id: The kms_key_id of this CreateSecretRequestBody.
        :type kms_key_id: str
        """
        self._kms_key_id = kms_key_id

    @property
    def description(self):
        """Gets the description of this CreateSecretRequestBody.

        凭据的描述信息。  约束：2048字节。

        :return: The description of this CreateSecretRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateSecretRequestBody.

        凭据的描述信息。  约束：2048字节。

        :param description: The description of this CreateSecretRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def secret_binary(self):
        """Gets the secret_binary of this CreateSecretRequestBody.

        二进制类型凭据在base64编码后的明文，凭据管理服务将其加密后，存入凭据的初始版本中。  类型：base64编码的二进制数据对象。  约束：secret_binary和secret_string必须且只能设置一个，最大32K。 当secret_type为RDS时。凭据值格式为： \"{'users':[{'name':'','password':''}]}\" 其中name为RDS实例账号名称，password为RDS实例账号口令

        :return: The secret_binary of this CreateSecretRequestBody.
        :rtype: str
        """
        return self._secret_binary

    @secret_binary.setter
    def secret_binary(self, secret_binary):
        """Sets the secret_binary of this CreateSecretRequestBody.

        二进制类型凭据在base64编码后的明文，凭据管理服务将其加密后，存入凭据的初始版本中。  类型：base64编码的二进制数据对象。  约束：secret_binary和secret_string必须且只能设置一个，最大32K。 当secret_type为RDS时。凭据值格式为： \"{'users':[{'name':'','password':''}]}\" 其中name为RDS实例账号名称，password为RDS实例账号口令

        :param secret_binary: The secret_binary of this CreateSecretRequestBody.
        :type secret_binary: str
        """
        self._secret_binary = secret_binary

    @property
    def secret_string(self):
        """Gets the secret_string of this CreateSecretRequestBody.

        文本类型凭据的明文，凭据管理服务将其加密后，存入凭据的初始版本中。  约束：secret_binary和secret_string必须且只能设置一个，最大32K。

        :return: The secret_string of this CreateSecretRequestBody.
        :rtype: str
        """
        return self._secret_string

    @secret_string.setter
    def secret_string(self, secret_string):
        """Sets the secret_string of this CreateSecretRequestBody.

        文本类型凭据的明文，凭据管理服务将其加密后，存入凭据的初始版本中。  约束：secret_binary和secret_string必须且只能设置一个，最大32K。

        :param secret_string: The secret_string of this CreateSecretRequestBody.
        :type secret_string: str
        """
        self._secret_string = secret_string

    @property
    def secret_type(self):
        """Gets the secret_type of this CreateSecretRequestBody.

        凭据类型  取值 ： COMMON ：通用凭据(默认)。用于应用系统中的各种敏感信息储存。         RDS ：RDS凭据 。专门针对RDS的凭据，用于存储RDS的账号信息。

        :return: The secret_type of this CreateSecretRequestBody.
        :rtype: str
        """
        return self._secret_type

    @secret_type.setter
    def secret_type(self, secret_type):
        """Sets the secret_type of this CreateSecretRequestBody.

        凭据类型  取值 ： COMMON ：通用凭据(默认)。用于应用系统中的各种敏感信息储存。         RDS ：RDS凭据 。专门针对RDS的凭据，用于存储RDS的账号信息。

        :param secret_type: The secret_type of this CreateSecretRequestBody.
        :type secret_type: str
        """
        self._secret_type = secret_type

    @property
    def auto_rotation(self):
        """Gets the auto_rotation of this CreateSecretRequestBody.

        自动轮转  取值：true 开启 ,false 关闭 (默认)

        :return: The auto_rotation of this CreateSecretRequestBody.
        :rtype: bool
        """
        return self._auto_rotation

    @auto_rotation.setter
    def auto_rotation(self, auto_rotation):
        """Sets the auto_rotation of this CreateSecretRequestBody.

        自动轮转  取值：true 开启 ,false 关闭 (默认)

        :param auto_rotation: The auto_rotation of this CreateSecretRequestBody.
        :type auto_rotation: bool
        """
        self._auto_rotation = auto_rotation

    @property
    def rotation_period(self):
        """Gets the rotation_period of this CreateSecretRequestBody.

        轮转周期  约束：6小时-8,760小时 （365天）  类型：Integer[unit] ，Integer表示时间长度 。unit表示时间单位，d（天）、h（小时）、m（分钟）、s（秒）。例如 1d 表示一天，24h也表示一天  说明：当开启自动轮转时，必须填写该值

        :return: The rotation_period of this CreateSecretRequestBody.
        :rtype: str
        """
        return self._rotation_period

    @rotation_period.setter
    def rotation_period(self, rotation_period):
        """Sets the rotation_period of this CreateSecretRequestBody.

        轮转周期  约束：6小时-8,760小时 （365天）  类型：Integer[unit] ，Integer表示时间长度 。unit表示时间单位，d（天）、h（小时）、m（分钟）、s（秒）。例如 1d 表示一天，24h也表示一天  说明：当开启自动轮转时，必须填写该值

        :param rotation_period: The rotation_period of this CreateSecretRequestBody.
        :type rotation_period: str
        """
        self._rotation_period = rotation_period

    @property
    def rotation_config(self):
        """Gets the rotation_config of this CreateSecretRequestBody.

        轮转配置  约束：范围不超过1024个字符。  当secret_type为RDS时，配置为{\"rds_instance_id\":\"\",\"Secret_sub_type\":\"\"}  说明：当secret_type为RDS时，必须填写该值  rds_instance_id为RDS的实例ID,Secret_sub_type为轮转子类型，取值为：SingleUser，MultiUser。  SingleUser：指定轮转类型为单用户模式轮转，每次轮转将指定账号重置为新的口令。  MultiUser：指定轮转类型为双用户模式轮转，SYSCURRENT和SYSPREVIOUS分别引用其中一个账号。凭据轮转时，SYSPREVIOUS引用的账号口令会被重置为新的随机口令，随后凭据交换SYSCURRENT和SYSPREVIOUS对RDS账号的引用。

        :return: The rotation_config of this CreateSecretRequestBody.
        :rtype: str
        """
        return self._rotation_config

    @rotation_config.setter
    def rotation_config(self, rotation_config):
        """Sets the rotation_config of this CreateSecretRequestBody.

        轮转配置  约束：范围不超过1024个字符。  当secret_type为RDS时，配置为{\"rds_instance_id\":\"\",\"Secret_sub_type\":\"\"}  说明：当secret_type为RDS时，必须填写该值  rds_instance_id为RDS的实例ID,Secret_sub_type为轮转子类型，取值为：SingleUser，MultiUser。  SingleUser：指定轮转类型为单用户模式轮转，每次轮转将指定账号重置为新的口令。  MultiUser：指定轮转类型为双用户模式轮转，SYSCURRENT和SYSPREVIOUS分别引用其中一个账号。凭据轮转时，SYSPREVIOUS引用的账号口令会被重置为新的随机口令，随后凭据交换SYSCURRENT和SYSPREVIOUS对RDS账号的引用。

        :param rotation_config: The rotation_config of this CreateSecretRequestBody.
        :type rotation_config: str
        """
        self._rotation_config = rotation_config

    @property
    def event_subscriptions(self):
        """Gets the event_subscriptions of this CreateSecretRequestBody.

        凭据订阅的事件列表，当前最大可订阅一个事件。当事件包含的基础事件触发时，通知消息将发送到事件对应的通知主题。

        :return: The event_subscriptions of this CreateSecretRequestBody.
        :rtype: list[str]
        """
        return self._event_subscriptions

    @event_subscriptions.setter
    def event_subscriptions(self, event_subscriptions):
        """Sets the event_subscriptions of this CreateSecretRequestBody.

        凭据订阅的事件列表，当前最大可订阅一个事件。当事件包含的基础事件触发时，通知消息将发送到事件对应的通知主题。

        :param event_subscriptions: The event_subscriptions of this CreateSecretRequestBody.
        :type event_subscriptions: list[str]
        """
        self._event_subscriptions = event_subscriptions

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this CreateSecretRequestBody.

        该参数针对企业用户使用。如果您是企业用户，且已创建企业项目，则请从下拉列表中为密钥选择需要绑定的企业项目，默认项目为“default”。 未开通企业管理的用户页面则没有“企业项目”参数项，无需进行配置。

        :return: The enterprise_project_id of this CreateSecretRequestBody.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this CreateSecretRequestBody.

        该参数针对企业用户使用。如果您是企业用户，且已创建企业项目，则请从下拉列表中为密钥选择需要绑定的企业项目，默认项目为“default”。 未开通企业管理的用户页面则没有“企业项目”参数项，无需进行配置。

        :param enterprise_project_id: The enterprise_project_id of this CreateSecretRequestBody.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, CreateSecretRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
