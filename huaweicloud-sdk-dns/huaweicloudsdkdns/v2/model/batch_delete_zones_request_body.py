# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchDeleteZonesRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'zone_type': 'str',
        'zone_ids': 'list[str]'
    }

    attribute_map = {
        'zone_type': 'zone_type',
        'zone_ids': 'zone_ids'
    }

    def __init__(self, zone_type=None, zone_ids=None):
        r"""BatchDeleteZonesRequestBody

        The model defined in huaweicloud sdk

        :param zone_type: **参数解释：** 待删除域名的类型。 **约束限制：** 不涉及。 **取值范围：** - public：公网域名 - private：内网域名  **默认取值：** 不涉及。
        :type zone_type: str
        :param zone_ids: **参数解释：** 待删除域名ID列表。 **约束限制：** 最多支持50个。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type zone_ids: list[str]
        """
        
        

        self._zone_type = None
        self._zone_ids = None
        self.discriminator = None

        self.zone_type = zone_type
        self.zone_ids = zone_ids

    @property
    def zone_type(self):
        r"""Gets the zone_type of this BatchDeleteZonesRequestBody.

        **参数解释：** 待删除域名的类型。 **约束限制：** 不涉及。 **取值范围：** - public：公网域名 - private：内网域名  **默认取值：** 不涉及。

        :return: The zone_type of this BatchDeleteZonesRequestBody.
        :rtype: str
        """
        return self._zone_type

    @zone_type.setter
    def zone_type(self, zone_type):
        r"""Sets the zone_type of this BatchDeleteZonesRequestBody.

        **参数解释：** 待删除域名的类型。 **约束限制：** 不涉及。 **取值范围：** - public：公网域名 - private：内网域名  **默认取值：** 不涉及。

        :param zone_type: The zone_type of this BatchDeleteZonesRequestBody.
        :type zone_type: str
        """
        self._zone_type = zone_type

    @property
    def zone_ids(self):
        r"""Gets the zone_ids of this BatchDeleteZonesRequestBody.

        **参数解释：** 待删除域名ID列表。 **约束限制：** 最多支持50个。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The zone_ids of this BatchDeleteZonesRequestBody.
        :rtype: list[str]
        """
        return self._zone_ids

    @zone_ids.setter
    def zone_ids(self, zone_ids):
        r"""Sets the zone_ids of this BatchDeleteZonesRequestBody.

        **参数解释：** 待删除域名ID列表。 **约束限制：** 最多支持50个。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param zone_ids: The zone_ids of this BatchDeleteZonesRequestBody.
        :type zone_ids: list[str]
        """
        self._zone_ids = zone_ids

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
        if not isinstance(other, BatchDeleteZonesRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
