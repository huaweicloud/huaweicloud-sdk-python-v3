# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClusterCertDuration:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'duration': 'int',
        'expire_at': 'str'
    }

    attribute_map = {
        'duration': 'duration',
        'expire_at': 'expire_at'
    }

    def __init__(self, duration=None, expire_at=None):
        r"""ClusterCertDuration

        The model defined in huaweicloud sdk

        :param duration: **参数解释：** 集群证书有效时间。 **约束限制：** duration和expire_at参数至少需要指定一个，若同时指定则以expire_at参数为准。 **取值范围：** 最小值为1天，最大值为5年，因此取值范围为1-1827（以天为单位，实际上限取决于5年内闰年的数量，例如5年内存在一个闰年则上限为1826天）；若填-1则为最大值5年 **默认取值：** 不涉及
        :type duration: int
        :param expire_at: **参数解释：** 集群证书到期时间。 **约束限制：** duration和expire_at参数至少需要指定一个，若同时指定则以expire_at参数为准。 **取值范围：** 证书到期时间须在当前时间后15分钟至5年之间，参数格式为：2025-01-01 16:00:00 +0000 UTC。 **默认取值：** 不涉及
        :type expire_at: str
        """
        
        

        self._duration = None
        self._expire_at = None
        self.discriminator = None

        if duration is not None:
            self.duration = duration
        if expire_at is not None:
            self.expire_at = expire_at

    @property
    def duration(self):
        r"""Gets the duration of this ClusterCertDuration.

        **参数解释：** 集群证书有效时间。 **约束限制：** duration和expire_at参数至少需要指定一个，若同时指定则以expire_at参数为准。 **取值范围：** 最小值为1天，最大值为5年，因此取值范围为1-1827（以天为单位，实际上限取决于5年内闰年的数量，例如5年内存在一个闰年则上限为1826天）；若填-1则为最大值5年 **默认取值：** 不涉及

        :return: The duration of this ClusterCertDuration.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        r"""Sets the duration of this ClusterCertDuration.

        **参数解释：** 集群证书有效时间。 **约束限制：** duration和expire_at参数至少需要指定一个，若同时指定则以expire_at参数为准。 **取值范围：** 最小值为1天，最大值为5年，因此取值范围为1-1827（以天为单位，实际上限取决于5年内闰年的数量，例如5年内存在一个闰年则上限为1826天）；若填-1则为最大值5年 **默认取值：** 不涉及

        :param duration: The duration of this ClusterCertDuration.
        :type duration: int
        """
        self._duration = duration

    @property
    def expire_at(self):
        r"""Gets the expire_at of this ClusterCertDuration.

        **参数解释：** 集群证书到期时间。 **约束限制：** duration和expire_at参数至少需要指定一个，若同时指定则以expire_at参数为准。 **取值范围：** 证书到期时间须在当前时间后15分钟至5年之间，参数格式为：2025-01-01 16:00:00 +0000 UTC。 **默认取值：** 不涉及

        :return: The expire_at of this ClusterCertDuration.
        :rtype: str
        """
        return self._expire_at

    @expire_at.setter
    def expire_at(self, expire_at):
        r"""Sets the expire_at of this ClusterCertDuration.

        **参数解释：** 集群证书到期时间。 **约束限制：** duration和expire_at参数至少需要指定一个，若同时指定则以expire_at参数为准。 **取值范围：** 证书到期时间须在当前时间后15分钟至5年之间，参数格式为：2025-01-01 16:00:00 +0000 UTC。 **默认取值：** 不涉及

        :param expire_at: The expire_at of this ClusterCertDuration.
        :type expire_at: str
        """
        self._expire_at = expire_at

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
        if not isinstance(other, ClusterCertDuration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
