# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QuotaRemainderData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'remainder': 'int',
        'need': 'int'
    }

    attribute_map = {
        'type': 'type',
        'remainder': 'remainder',
        'need': 'need'
    }

    def __init__(self, type=None, remainder=None, need=None):
        r"""QuotaRemainderData

        The model defined in huaweicloud sdk

        :param type: 配额-资源类型： * GPU_INSTANCES：GPU资源实例数，单位个。 * INSTANCES：普通实例数，单位个。 * VOLUME_GIGABYTES：磁盘总容量，单位GB。 * VOLUMES：磁盘数量，单位个。 * CORES：CPU数量，单位个。 * MEMORY：内存容量，单位MB。
        :type type: str
        :param remainder: 剩余配额。
        :type remainder: int
        :param need: 所需配额。
        :type need: int
        """
        
        

        self._type = None
        self._remainder = None
        self._need = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if remainder is not None:
            self.remainder = remainder
        if need is not None:
            self.need = need

    @property
    def type(self):
        r"""Gets the type of this QuotaRemainderData.

        配额-资源类型： * GPU_INSTANCES：GPU资源实例数，单位个。 * INSTANCES：普通实例数，单位个。 * VOLUME_GIGABYTES：磁盘总容量，单位GB。 * VOLUMES：磁盘数量，单位个。 * CORES：CPU数量，单位个。 * MEMORY：内存容量，单位MB。

        :return: The type of this QuotaRemainderData.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this QuotaRemainderData.

        配额-资源类型： * GPU_INSTANCES：GPU资源实例数，单位个。 * INSTANCES：普通实例数，单位个。 * VOLUME_GIGABYTES：磁盘总容量，单位GB。 * VOLUMES：磁盘数量，单位个。 * CORES：CPU数量，单位个。 * MEMORY：内存容量，单位MB。

        :param type: The type of this QuotaRemainderData.
        :type type: str
        """
        self._type = type

    @property
    def remainder(self):
        r"""Gets the remainder of this QuotaRemainderData.

        剩余配额。

        :return: The remainder of this QuotaRemainderData.
        :rtype: int
        """
        return self._remainder

    @remainder.setter
    def remainder(self, remainder):
        r"""Sets the remainder of this QuotaRemainderData.

        剩余配额。

        :param remainder: The remainder of this QuotaRemainderData.
        :type remainder: int
        """
        self._remainder = remainder

    @property
    def need(self):
        r"""Gets the need of this QuotaRemainderData.

        所需配额。

        :return: The need of this QuotaRemainderData.
        :rtype: int
        """
        return self._need

    @need.setter
    def need(self, need):
        r"""Sets the need of this QuotaRemainderData.

        所需配额。

        :param need: The need of this QuotaRemainderData.
        :type need: int
        """
        self._need = need

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
        if not isinstance(other, QuotaRemainderData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
