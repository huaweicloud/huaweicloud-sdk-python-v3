# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowKeyRotationStatusResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'key_rotation_enabled': 'bool',
        'rotation_interval': 'int',
        'last_rotation_time': 'str',
        'number_of_rotations': 'int'
    }

    attribute_map = {
        'key_rotation_enabled': 'key_rotation_enabled',
        'rotation_interval': 'rotation_interval',
        'last_rotation_time': 'last_rotation_time',
        'number_of_rotations': 'number_of_rotations'
    }

    def __init__(self, key_rotation_enabled=None, rotation_interval=None, last_rotation_time=None, number_of_rotations=None):
        """ShowKeyRotationStatusResponse

        The model defined in huaweicloud sdk

        :param key_rotation_enabled: 密钥轮换状态，默认为“false”，表示关闭密钥轮换功能。
        :type key_rotation_enabled: bool
        :param rotation_interval: 轮换周期，取值范围为30~365的整数。 周期范围设置根据密钥使用频率进行，若密钥使用频率高，建议设置为短周期；反之，则设置为长周期。
        :type rotation_interval: int
        :param last_rotation_time: 上一次密钥轮换时间。时间戳，即从1970年1月1日至该时间的总秒数。
        :type last_rotation_time: str
        :param number_of_rotations: 密钥轮换次数。
        :type number_of_rotations: int
        """
        
        super(ShowKeyRotationStatusResponse, self).__init__()

        self._key_rotation_enabled = None
        self._rotation_interval = None
        self._last_rotation_time = None
        self._number_of_rotations = None
        self.discriminator = None

        if key_rotation_enabled is not None:
            self.key_rotation_enabled = key_rotation_enabled
        if rotation_interval is not None:
            self.rotation_interval = rotation_interval
        if last_rotation_time is not None:
            self.last_rotation_time = last_rotation_time
        if number_of_rotations is not None:
            self.number_of_rotations = number_of_rotations

    @property
    def key_rotation_enabled(self):
        """Gets the key_rotation_enabled of this ShowKeyRotationStatusResponse.

        密钥轮换状态，默认为“false”，表示关闭密钥轮换功能。

        :return: The key_rotation_enabled of this ShowKeyRotationStatusResponse.
        :rtype: bool
        """
        return self._key_rotation_enabled

    @key_rotation_enabled.setter
    def key_rotation_enabled(self, key_rotation_enabled):
        """Sets the key_rotation_enabled of this ShowKeyRotationStatusResponse.

        密钥轮换状态，默认为“false”，表示关闭密钥轮换功能。

        :param key_rotation_enabled: The key_rotation_enabled of this ShowKeyRotationStatusResponse.
        :type key_rotation_enabled: bool
        """
        self._key_rotation_enabled = key_rotation_enabled

    @property
    def rotation_interval(self):
        """Gets the rotation_interval of this ShowKeyRotationStatusResponse.

        轮换周期，取值范围为30~365的整数。 周期范围设置根据密钥使用频率进行，若密钥使用频率高，建议设置为短周期；反之，则设置为长周期。

        :return: The rotation_interval of this ShowKeyRotationStatusResponse.
        :rtype: int
        """
        return self._rotation_interval

    @rotation_interval.setter
    def rotation_interval(self, rotation_interval):
        """Sets the rotation_interval of this ShowKeyRotationStatusResponse.

        轮换周期，取值范围为30~365的整数。 周期范围设置根据密钥使用频率进行，若密钥使用频率高，建议设置为短周期；反之，则设置为长周期。

        :param rotation_interval: The rotation_interval of this ShowKeyRotationStatusResponse.
        :type rotation_interval: int
        """
        self._rotation_interval = rotation_interval

    @property
    def last_rotation_time(self):
        """Gets the last_rotation_time of this ShowKeyRotationStatusResponse.

        上一次密钥轮换时间。时间戳，即从1970年1月1日至该时间的总秒数。

        :return: The last_rotation_time of this ShowKeyRotationStatusResponse.
        :rtype: str
        """
        return self._last_rotation_time

    @last_rotation_time.setter
    def last_rotation_time(self, last_rotation_time):
        """Sets the last_rotation_time of this ShowKeyRotationStatusResponse.

        上一次密钥轮换时间。时间戳，即从1970年1月1日至该时间的总秒数。

        :param last_rotation_time: The last_rotation_time of this ShowKeyRotationStatusResponse.
        :type last_rotation_time: str
        """
        self._last_rotation_time = last_rotation_time

    @property
    def number_of_rotations(self):
        """Gets the number_of_rotations of this ShowKeyRotationStatusResponse.

        密钥轮换次数。

        :return: The number_of_rotations of this ShowKeyRotationStatusResponse.
        :rtype: int
        """
        return self._number_of_rotations

    @number_of_rotations.setter
    def number_of_rotations(self, number_of_rotations):
        """Sets the number_of_rotations of this ShowKeyRotationStatusResponse.

        密钥轮换次数。

        :param number_of_rotations: The number_of_rotations of this ShowKeyRotationStatusResponse.
        :type number_of_rotations: int
        """
        self._number_of_rotations = number_of_rotations

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
        if not isinstance(other, ShowKeyRotationStatusResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
