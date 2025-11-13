# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchCreateCombinedPublicRecordsetsTaskRequestBody:

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
        'recordset_name_prefixes': 'list[str]',
        'records': 'list[str]',
        'type': 'str',
        'line': 'str',
        'ttl': 'int'
    }

    attribute_map = {
        'zone_names': 'zone_names',
        'recordset_name_prefixes': 'recordset_name_prefixes',
        'records': 'records',
        'type': 'type',
        'line': 'line',
        'ttl': 'ttl'
    }

    def __init__(self, zone_names=None, recordset_name_prefixes=None, records=None, type=None, line=None, ttl=None):
        r"""BatchCreateCombinedPublicRecordsetsTaskRequestBody

        The model defined in huaweicloud sdk

        :param zone_names: **参数解释：** 托管该记录的域名。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type zone_names: list[str]
        :param recordset_name_prefixes: **参数解释：** 主机记录。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type recordset_name_prefixes: list[str]
        :param records: **参数解释：** 解析记录的值。不同类型解析记录对应的值的规则不同。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type records: list[str]
        :param type: **参数解释：** 记录集的类型。 **约束限制：** 不涉及。 **取值范围：** - 公网域名的记录类型: A、CNAME、MX、AAAA、TXT、SRV、NS、CAA。  **默认取值：** 不涉及。
        :type type: str
        :param line: **参数解释：** 解析线路ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** default_view。
        :type line: str
        :param ttl: **参数解释：** 解析记录在本地DNS服务器的缓存时间，缓存时间越长更新生效越慢，以秒为单位。 **约束限制：** 不涉及。 **取值范围：** 1~2147483647。 **默认取值：** 300
        :type ttl: int
        """
        
        

        self._zone_names = None
        self._recordset_name_prefixes = None
        self._records = None
        self._type = None
        self._line = None
        self._ttl = None
        self.discriminator = None

        self.zone_names = zone_names
        self.recordset_name_prefixes = recordset_name_prefixes
        self.records = records
        self.type = type
        if line is not None:
            self.line = line
        if ttl is not None:
            self.ttl = ttl

    @property
    def zone_names(self):
        r"""Gets the zone_names of this BatchCreateCombinedPublicRecordsetsTaskRequestBody.

        **参数解释：** 托管该记录的域名。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The zone_names of this BatchCreateCombinedPublicRecordsetsTaskRequestBody.
        :rtype: list[str]
        """
        return self._zone_names

    @zone_names.setter
    def zone_names(self, zone_names):
        r"""Sets the zone_names of this BatchCreateCombinedPublicRecordsetsTaskRequestBody.

        **参数解释：** 托管该记录的域名。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param zone_names: The zone_names of this BatchCreateCombinedPublicRecordsetsTaskRequestBody.
        :type zone_names: list[str]
        """
        self._zone_names = zone_names

    @property
    def recordset_name_prefixes(self):
        r"""Gets the recordset_name_prefixes of this BatchCreateCombinedPublicRecordsetsTaskRequestBody.

        **参数解释：** 主机记录。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The recordset_name_prefixes of this BatchCreateCombinedPublicRecordsetsTaskRequestBody.
        :rtype: list[str]
        """
        return self._recordset_name_prefixes

    @recordset_name_prefixes.setter
    def recordset_name_prefixes(self, recordset_name_prefixes):
        r"""Sets the recordset_name_prefixes of this BatchCreateCombinedPublicRecordsetsTaskRequestBody.

        **参数解释：** 主机记录。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param recordset_name_prefixes: The recordset_name_prefixes of this BatchCreateCombinedPublicRecordsetsTaskRequestBody.
        :type recordset_name_prefixes: list[str]
        """
        self._recordset_name_prefixes = recordset_name_prefixes

    @property
    def records(self):
        r"""Gets the records of this BatchCreateCombinedPublicRecordsetsTaskRequestBody.

        **参数解释：** 解析记录的值。不同类型解析记录对应的值的规则不同。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The records of this BatchCreateCombinedPublicRecordsetsTaskRequestBody.
        :rtype: list[str]
        """
        return self._records

    @records.setter
    def records(self, records):
        r"""Sets the records of this BatchCreateCombinedPublicRecordsetsTaskRequestBody.

        **参数解释：** 解析记录的值。不同类型解析记录对应的值的规则不同。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param records: The records of this BatchCreateCombinedPublicRecordsetsTaskRequestBody.
        :type records: list[str]
        """
        self._records = records

    @property
    def type(self):
        r"""Gets the type of this BatchCreateCombinedPublicRecordsetsTaskRequestBody.

        **参数解释：** 记录集的类型。 **约束限制：** 不涉及。 **取值范围：** - 公网域名的记录类型: A、CNAME、MX、AAAA、TXT、SRV、NS、CAA。  **默认取值：** 不涉及。

        :return: The type of this BatchCreateCombinedPublicRecordsetsTaskRequestBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this BatchCreateCombinedPublicRecordsetsTaskRequestBody.

        **参数解释：** 记录集的类型。 **约束限制：** 不涉及。 **取值范围：** - 公网域名的记录类型: A、CNAME、MX、AAAA、TXT、SRV、NS、CAA。  **默认取值：** 不涉及。

        :param type: The type of this BatchCreateCombinedPublicRecordsetsTaskRequestBody.
        :type type: str
        """
        self._type = type

    @property
    def line(self):
        r"""Gets the line of this BatchCreateCombinedPublicRecordsetsTaskRequestBody.

        **参数解释：** 解析线路ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** default_view。

        :return: The line of this BatchCreateCombinedPublicRecordsetsTaskRequestBody.
        :rtype: str
        """
        return self._line

    @line.setter
    def line(self, line):
        r"""Sets the line of this BatchCreateCombinedPublicRecordsetsTaskRequestBody.

        **参数解释：** 解析线路ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** default_view。

        :param line: The line of this BatchCreateCombinedPublicRecordsetsTaskRequestBody.
        :type line: str
        """
        self._line = line

    @property
    def ttl(self):
        r"""Gets the ttl of this BatchCreateCombinedPublicRecordsetsTaskRequestBody.

        **参数解释：** 解析记录在本地DNS服务器的缓存时间，缓存时间越长更新生效越慢，以秒为单位。 **约束限制：** 不涉及。 **取值范围：** 1~2147483647。 **默认取值：** 300

        :return: The ttl of this BatchCreateCombinedPublicRecordsetsTaskRequestBody.
        :rtype: int
        """
        return self._ttl

    @ttl.setter
    def ttl(self, ttl):
        r"""Sets the ttl of this BatchCreateCombinedPublicRecordsetsTaskRequestBody.

        **参数解释：** 解析记录在本地DNS服务器的缓存时间，缓存时间越长更新生效越慢，以秒为单位。 **约束限制：** 不涉及。 **取值范围：** 1~2147483647。 **默认取值：** 300

        :param ttl: The ttl of this BatchCreateCombinedPublicRecordsetsTaskRequestBody.
        :type ttl: int
        """
        self._ttl = ttl

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
        if not isinstance(other, BatchCreateCombinedPublicRecordsetsTaskRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
