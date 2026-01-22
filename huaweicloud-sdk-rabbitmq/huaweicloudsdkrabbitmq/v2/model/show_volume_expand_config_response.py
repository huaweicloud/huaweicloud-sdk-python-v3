# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowVolumeExpandConfigResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'auto_volume_expand_enable': 'bool',
        'expand_threshold': 'int',
        'max_volume_size': 'int',
        'expand_increment': 'int'
    }

    attribute_map = {
        'auto_volume_expand_enable': 'auto_volume_expand_enable',
        'expand_threshold': 'expand_threshold',
        'max_volume_size': 'max_volume_size',
        'expand_increment': 'expand_increment'
    }

    def __init__(self, auto_volume_expand_enable=None, expand_threshold=None, max_volume_size=None, expand_increment=None):
        r"""ShowVolumeExpandConfigResponse

        The model defined in huaweicloud sdk

        :param auto_volume_expand_enable: **参数解释**： 是否开启磁盘自动扩容。 **取值范围**： - true：开启。 - false：关闭。
        :type auto_volume_expand_enable: bool
        :param expand_threshold: **参数解释**： 触发磁盘自动扩容的阈值。 **取值范围**： 20%-80%。
        :type expand_threshold: int
        :param max_volume_size: **参数解释**： 磁盘自动扩容的上限值。 **取值范围**： 不涉及。
        :type max_volume_size: int
        :param expand_increment: **参数解释**： 每次磁盘自动扩容的比例。 **取值范围**： 10%-100%。
        :type expand_increment: int
        """
        
        super().__init__()

        self._auto_volume_expand_enable = None
        self._expand_threshold = None
        self._max_volume_size = None
        self._expand_increment = None
        self.discriminator = None

        if auto_volume_expand_enable is not None:
            self.auto_volume_expand_enable = auto_volume_expand_enable
        if expand_threshold is not None:
            self.expand_threshold = expand_threshold
        if max_volume_size is not None:
            self.max_volume_size = max_volume_size
        if expand_increment is not None:
            self.expand_increment = expand_increment

    @property
    def auto_volume_expand_enable(self):
        r"""Gets the auto_volume_expand_enable of this ShowVolumeExpandConfigResponse.

        **参数解释**： 是否开启磁盘自动扩容。 **取值范围**： - true：开启。 - false：关闭。

        :return: The auto_volume_expand_enable of this ShowVolumeExpandConfigResponse.
        :rtype: bool
        """
        return self._auto_volume_expand_enable

    @auto_volume_expand_enable.setter
    def auto_volume_expand_enable(self, auto_volume_expand_enable):
        r"""Sets the auto_volume_expand_enable of this ShowVolumeExpandConfigResponse.

        **参数解释**： 是否开启磁盘自动扩容。 **取值范围**： - true：开启。 - false：关闭。

        :param auto_volume_expand_enable: The auto_volume_expand_enable of this ShowVolumeExpandConfigResponse.
        :type auto_volume_expand_enable: bool
        """
        self._auto_volume_expand_enable = auto_volume_expand_enable

    @property
    def expand_threshold(self):
        r"""Gets the expand_threshold of this ShowVolumeExpandConfigResponse.

        **参数解释**： 触发磁盘自动扩容的阈值。 **取值范围**： 20%-80%。

        :return: The expand_threshold of this ShowVolumeExpandConfigResponse.
        :rtype: int
        """
        return self._expand_threshold

    @expand_threshold.setter
    def expand_threshold(self, expand_threshold):
        r"""Sets the expand_threshold of this ShowVolumeExpandConfigResponse.

        **参数解释**： 触发磁盘自动扩容的阈值。 **取值范围**： 20%-80%。

        :param expand_threshold: The expand_threshold of this ShowVolumeExpandConfigResponse.
        :type expand_threshold: int
        """
        self._expand_threshold = expand_threshold

    @property
    def max_volume_size(self):
        r"""Gets the max_volume_size of this ShowVolumeExpandConfigResponse.

        **参数解释**： 磁盘自动扩容的上限值。 **取值范围**： 不涉及。

        :return: The max_volume_size of this ShowVolumeExpandConfigResponse.
        :rtype: int
        """
        return self._max_volume_size

    @max_volume_size.setter
    def max_volume_size(self, max_volume_size):
        r"""Sets the max_volume_size of this ShowVolumeExpandConfigResponse.

        **参数解释**： 磁盘自动扩容的上限值。 **取值范围**： 不涉及。

        :param max_volume_size: The max_volume_size of this ShowVolumeExpandConfigResponse.
        :type max_volume_size: int
        """
        self._max_volume_size = max_volume_size

    @property
    def expand_increment(self):
        r"""Gets the expand_increment of this ShowVolumeExpandConfigResponse.

        **参数解释**： 每次磁盘自动扩容的比例。 **取值范围**： 10%-100%。

        :return: The expand_increment of this ShowVolumeExpandConfigResponse.
        :rtype: int
        """
        return self._expand_increment

    @expand_increment.setter
    def expand_increment(self, expand_increment):
        r"""Sets the expand_increment of this ShowVolumeExpandConfigResponse.

        **参数解释**： 每次磁盘自动扩容的比例。 **取值范围**： 10%-100%。

        :param expand_increment: The expand_increment of this ShowVolumeExpandConfigResponse.
        :type expand_increment: int
        """
        self._expand_increment = expand_increment

    def to_dict(self):
        import warnings
        warnings.warn("ShowVolumeExpandConfigResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowVolumeExpandConfigResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
