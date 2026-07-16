# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowLeaseResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'create_at': 'int',
        'duration': 'int',
        'enable': 'bool',
        'type': 'str',
        'update_at': 'int'
    }

    attribute_map = {
        'create_at': 'create_at',
        'duration': 'duration',
        'enable': 'enable',
        'type': 'type',
        'update_at': 'update_at'
    }

    def __init__(self, create_at=None, duration=None, enable=None, type=None, update_at=None):
        r"""ShowLeaseResponse

        The model defined in huaweicloud sdk

        :param create_at: **参数解释**：实例创建的时间，UTC毫秒。 **取值范围**：不涉及。
        :type create_at: int
        :param duration: **参数解释**：实例运行时长，以创建时间为起点计算，即“创建时间+duration &gt; 当前时刻”时，系统会自动停止实例。 **取值范围**：不涉及。
        :type duration: int
        :param enable: **参数解释**：是否启用自动停止功能。 **取值范围**：布尔类型： - true：启动自动停止功能。 - false：关闭自动停止功能。
        :type enable: bool
        :param type: **参数解释**：自动停止类别。 **取值范围**：枚举类型，取值如下： - TIMING：自动停止。 - IDLE：空闲停止。
        :type type: str
        :param update_at: **参数解释**：实例最后更新（不包括探活心跳）的时间，UTC毫秒。 **取值范围**：不涉及。
        :type update_at: int
        """
        
        super().__init__()

        self._create_at = None
        self._duration = None
        self._enable = None
        self._type = None
        self._update_at = None
        self.discriminator = None

        if create_at is not None:
            self.create_at = create_at
        if duration is not None:
            self.duration = duration
        if enable is not None:
            self.enable = enable
        if type is not None:
            self.type = type
        if update_at is not None:
            self.update_at = update_at

    @property
    def create_at(self):
        r"""Gets the create_at of this ShowLeaseResponse.

        **参数解释**：实例创建的时间，UTC毫秒。 **取值范围**：不涉及。

        :return: The create_at of this ShowLeaseResponse.
        :rtype: int
        """
        return self._create_at

    @create_at.setter
    def create_at(self, create_at):
        r"""Sets the create_at of this ShowLeaseResponse.

        **参数解释**：实例创建的时间，UTC毫秒。 **取值范围**：不涉及。

        :param create_at: The create_at of this ShowLeaseResponse.
        :type create_at: int
        """
        self._create_at = create_at

    @property
    def duration(self):
        r"""Gets the duration of this ShowLeaseResponse.

        **参数解释**：实例运行时长，以创建时间为起点计算，即“创建时间+duration > 当前时刻”时，系统会自动停止实例。 **取值范围**：不涉及。

        :return: The duration of this ShowLeaseResponse.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        r"""Sets the duration of this ShowLeaseResponse.

        **参数解释**：实例运行时长，以创建时间为起点计算，即“创建时间+duration > 当前时刻”时，系统会自动停止实例。 **取值范围**：不涉及。

        :param duration: The duration of this ShowLeaseResponse.
        :type duration: int
        """
        self._duration = duration

    @property
    def enable(self):
        r"""Gets the enable of this ShowLeaseResponse.

        **参数解释**：是否启用自动停止功能。 **取值范围**：布尔类型： - true：启动自动停止功能。 - false：关闭自动停止功能。

        :return: The enable of this ShowLeaseResponse.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        r"""Sets the enable of this ShowLeaseResponse.

        **参数解释**：是否启用自动停止功能。 **取值范围**：布尔类型： - true：启动自动停止功能。 - false：关闭自动停止功能。

        :param enable: The enable of this ShowLeaseResponse.
        :type enable: bool
        """
        self._enable = enable

    @property
    def type(self):
        r"""Gets the type of this ShowLeaseResponse.

        **参数解释**：自动停止类别。 **取值范围**：枚举类型，取值如下： - TIMING：自动停止。 - IDLE：空闲停止。

        :return: The type of this ShowLeaseResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ShowLeaseResponse.

        **参数解释**：自动停止类别。 **取值范围**：枚举类型，取值如下： - TIMING：自动停止。 - IDLE：空闲停止。

        :param type: The type of this ShowLeaseResponse.
        :type type: str
        """
        self._type = type

    @property
    def update_at(self):
        r"""Gets the update_at of this ShowLeaseResponse.

        **参数解释**：实例最后更新（不包括探活心跳）的时间，UTC毫秒。 **取值范围**：不涉及。

        :return: The update_at of this ShowLeaseResponse.
        :rtype: int
        """
        return self._update_at

    @update_at.setter
    def update_at(self, update_at):
        r"""Sets the update_at of this ShowLeaseResponse.

        **参数解释**：实例最后更新（不包括探活心跳）的时间，UTC毫秒。 **取值范围**：不涉及。

        :param update_at: The update_at of this ShowLeaseResponse.
        :type update_at: int
        """
        self._update_at = update_at

    def to_dict(self):
        import warnings
        warnings.warn("ShowLeaseResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ShowLeaseResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
