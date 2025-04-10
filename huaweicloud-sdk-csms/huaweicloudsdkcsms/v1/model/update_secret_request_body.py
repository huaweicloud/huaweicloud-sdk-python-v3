# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateSecretRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'kms_key_id': 'str',
        'description': 'str',
        'auto_rotation': 'bool',
        'rotation_period': 'str',
        'event_subscriptions': 'list[str]',
        'rotation_func_urn': 'str'
    }

    attribute_map = {
        'kms_key_id': 'kms_key_id',
        'description': 'description',
        'auto_rotation': 'auto_rotation',
        'rotation_period': 'rotation_period',
        'event_subscriptions': 'event_subscriptions',
        'rotation_func_urn': 'rotation_func_urn'
    }

    def __init__(self, kms_key_id=None, description=None, auto_rotation=None, rotation_period=None, event_subscriptions=None, rotation_func_urn=None):
        r"""UpdateSecretRequestBody

        The model defined in huaweicloud sdk

        :param kms_key_id: 用于加密保护凭据值的KMS主密钥ID。更新凭据的主密钥后，仅新创建的凭据版本使用更新后的主密钥ID加密，之前的凭据版本依旧使用之前的主密钥ID解密。
        :type kms_key_id: str
        :param description: 凭据的描述信息。 约束：2048字节。
        :type description: str
        :param auto_rotation: 自动轮转  取值：true 开启 false 关
        :type auto_rotation: bool
        :param rotation_period: 轮转周期  约束：6小时-8,760小时 （365天）  类型：Integer[unit] ，Integer表示时间长度 。unit表示时间单位，d（天）、h（小时）、m（分钟）、s（秒）。例如 1d 表示一天，24h也表示一天  说明：当开启自动轮转时，必须填写该值
        :type rotation_period: str
        :param event_subscriptions: 凭据订阅的事件列表，当前最大可订阅一个事件。当事件包含的基础事件触发时，通知消息将发送到事件对应的通知主题。
        :type event_subscriptions: list[str]
        :param rotation_func_urn: FunctionGraph函数的urn。
        :type rotation_func_urn: str
        """
        
        

        self._kms_key_id = None
        self._description = None
        self._auto_rotation = None
        self._rotation_period = None
        self._event_subscriptions = None
        self._rotation_func_urn = None
        self.discriminator = None

        if kms_key_id is not None:
            self.kms_key_id = kms_key_id
        if description is not None:
            self.description = description
        if auto_rotation is not None:
            self.auto_rotation = auto_rotation
        if rotation_period is not None:
            self.rotation_period = rotation_period
        if event_subscriptions is not None:
            self.event_subscriptions = event_subscriptions
        if rotation_func_urn is not None:
            self.rotation_func_urn = rotation_func_urn

    @property
    def kms_key_id(self):
        r"""Gets the kms_key_id of this UpdateSecretRequestBody.

        用于加密保护凭据值的KMS主密钥ID。更新凭据的主密钥后，仅新创建的凭据版本使用更新后的主密钥ID加密，之前的凭据版本依旧使用之前的主密钥ID解密。

        :return: The kms_key_id of this UpdateSecretRequestBody.
        :rtype: str
        """
        return self._kms_key_id

    @kms_key_id.setter
    def kms_key_id(self, kms_key_id):
        r"""Sets the kms_key_id of this UpdateSecretRequestBody.

        用于加密保护凭据值的KMS主密钥ID。更新凭据的主密钥后，仅新创建的凭据版本使用更新后的主密钥ID加密，之前的凭据版本依旧使用之前的主密钥ID解密。

        :param kms_key_id: The kms_key_id of this UpdateSecretRequestBody.
        :type kms_key_id: str
        """
        self._kms_key_id = kms_key_id

    @property
    def description(self):
        r"""Gets the description of this UpdateSecretRequestBody.

        凭据的描述信息。 约束：2048字节。

        :return: The description of this UpdateSecretRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateSecretRequestBody.

        凭据的描述信息。 约束：2048字节。

        :param description: The description of this UpdateSecretRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def auto_rotation(self):
        r"""Gets the auto_rotation of this UpdateSecretRequestBody.

        自动轮转  取值：true 开启 false 关

        :return: The auto_rotation of this UpdateSecretRequestBody.
        :rtype: bool
        """
        return self._auto_rotation

    @auto_rotation.setter
    def auto_rotation(self, auto_rotation):
        r"""Sets the auto_rotation of this UpdateSecretRequestBody.

        自动轮转  取值：true 开启 false 关

        :param auto_rotation: The auto_rotation of this UpdateSecretRequestBody.
        :type auto_rotation: bool
        """
        self._auto_rotation = auto_rotation

    @property
    def rotation_period(self):
        r"""Gets the rotation_period of this UpdateSecretRequestBody.

        轮转周期  约束：6小时-8,760小时 （365天）  类型：Integer[unit] ，Integer表示时间长度 。unit表示时间单位，d（天）、h（小时）、m（分钟）、s（秒）。例如 1d 表示一天，24h也表示一天  说明：当开启自动轮转时，必须填写该值

        :return: The rotation_period of this UpdateSecretRequestBody.
        :rtype: str
        """
        return self._rotation_period

    @rotation_period.setter
    def rotation_period(self, rotation_period):
        r"""Sets the rotation_period of this UpdateSecretRequestBody.

        轮转周期  约束：6小时-8,760小时 （365天）  类型：Integer[unit] ，Integer表示时间长度 。unit表示时间单位，d（天）、h（小时）、m（分钟）、s（秒）。例如 1d 表示一天，24h也表示一天  说明：当开启自动轮转时，必须填写该值

        :param rotation_period: The rotation_period of this UpdateSecretRequestBody.
        :type rotation_period: str
        """
        self._rotation_period = rotation_period

    @property
    def event_subscriptions(self):
        r"""Gets the event_subscriptions of this UpdateSecretRequestBody.

        凭据订阅的事件列表，当前最大可订阅一个事件。当事件包含的基础事件触发时，通知消息将发送到事件对应的通知主题。

        :return: The event_subscriptions of this UpdateSecretRequestBody.
        :rtype: list[str]
        """
        return self._event_subscriptions

    @event_subscriptions.setter
    def event_subscriptions(self, event_subscriptions):
        r"""Sets the event_subscriptions of this UpdateSecretRequestBody.

        凭据订阅的事件列表，当前最大可订阅一个事件。当事件包含的基础事件触发时，通知消息将发送到事件对应的通知主题。

        :param event_subscriptions: The event_subscriptions of this UpdateSecretRequestBody.
        :type event_subscriptions: list[str]
        """
        self._event_subscriptions = event_subscriptions

    @property
    def rotation_func_urn(self):
        r"""Gets the rotation_func_urn of this UpdateSecretRequestBody.

        FunctionGraph函数的urn。

        :return: The rotation_func_urn of this UpdateSecretRequestBody.
        :rtype: str
        """
        return self._rotation_func_urn

    @rotation_func_urn.setter
    def rotation_func_urn(self, rotation_func_urn):
        r"""Sets the rotation_func_urn of this UpdateSecretRequestBody.

        FunctionGraph函数的urn。

        :param rotation_func_urn: The rotation_func_urn of this UpdateSecretRequestBody.
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
        if not isinstance(other, UpdateSecretRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
