# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchDeletePublicRecordsetsTaskRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'zone_names': 'list[str]',
        'recordset_name_prefixes': 'list[str]'
    }

    attribute_map = {
        'zone_names': 'zone_names',
        'recordset_name_prefixes': 'recordset_name_prefixes'
    }

    def __init__(self, zone_names=None, recordset_name_prefixes=None):
        r"""BatchDeletePublicRecordsetsTaskRequestBody

        The model defined in huaweicloud sdk

        :param zone_names: **参数解释：** 托管该记录的域名。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type zone_names: list[str]
        :param recordset_name_prefixes: **参数解释：** 主机记录。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type recordset_name_prefixes: list[str]
        """
        
        

        self._zone_names = None
        self._recordset_name_prefixes = None
        self.discriminator = None

        self.zone_names = zone_names
        self.recordset_name_prefixes = recordset_name_prefixes

    @property
    def zone_names(self):
        r"""Gets the zone_names of this BatchDeletePublicRecordsetsTaskRequestBody.

        **参数解释：** 托管该记录的域名。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The zone_names of this BatchDeletePublicRecordsetsTaskRequestBody.
        :rtype: list[str]
        """
        return self._zone_names

    @zone_names.setter
    def zone_names(self, zone_names):
        r"""Sets the zone_names of this BatchDeletePublicRecordsetsTaskRequestBody.

        **参数解释：** 托管该记录的域名。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param zone_names: The zone_names of this BatchDeletePublicRecordsetsTaskRequestBody.
        :type zone_names: list[str]
        """
        self._zone_names = zone_names

    @property
    def recordset_name_prefixes(self):
        r"""Gets the recordset_name_prefixes of this BatchDeletePublicRecordsetsTaskRequestBody.

        **参数解释：** 主机记录。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The recordset_name_prefixes of this BatchDeletePublicRecordsetsTaskRequestBody.
        :rtype: list[str]
        """
        return self._recordset_name_prefixes

    @recordset_name_prefixes.setter
    def recordset_name_prefixes(self, recordset_name_prefixes):
        r"""Sets the recordset_name_prefixes of this BatchDeletePublicRecordsetsTaskRequestBody.

        **参数解释：** 主机记录。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param recordset_name_prefixes: The recordset_name_prefixes of this BatchDeletePublicRecordsetsTaskRequestBody.
        :type recordset_name_prefixes: list[str]
        """
        self._recordset_name_prefixes = recordset_name_prefixes

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
        if not isinstance(other, BatchDeletePublicRecordsetsTaskRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
