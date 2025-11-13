# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchCreatePublicRecordsetsTaskItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'zone_name': 'str',
        'name': 'str',
        'type': 'str',
        'line': 'str',
        'ttl': 'int',
        'weight': 'int',
        'records': 'list[str]',
        'status': 'str'
    }

    attribute_map = {
        'zone_name': 'zone_name',
        'name': 'name',
        'type': 'type',
        'line': 'line',
        'ttl': 'ttl',
        'weight': 'weight',
        'records': 'records',
        'status': 'status'
    }

    def __init__(self, zone_name=None, name=None, type=None, line=None, ttl=None, weight=None, records=None, status=None):
        r"""BatchCreatePublicRecordsetsTaskItem

        The model defined in huaweicloud sdk

        :param zone_name: **参数解释：** 托管该记录的域名。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type zone_name: str
        :param name: **参数解释：** 主机记录或域名。 末尾有点则认为是完整域名，如果不包含点，则认为是域名前缀。例如： 输入\&quot;www\&quot;，创建成功后域名显示为\&quot;www.example.com.\&quot; 输入\&quot;www.example.com.\&quot;（注意域名末尾有点），创建成功后域名显示为\&quot;www.example.com.\&quot; 输入\&quot;www.example.com\&quot;（注意域名末尾没有点），创建成功后域名显示为\&quot;www.example.com.example.com.\&quot; **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type name: str
        :param type: **参数解释：** 记录集的类型。 **约束限制：** 不涉及。 **取值范围：** - 公网域名的记录类型: A、CNAME、MX、AAAA、TXT、SRV、NS、CAA。  **默认取值：** 不涉及。
        :type type: str
        :param line: **参数解释：** 解析线路ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** default_view。
        :type line: str
        :param ttl: **参数解释：** 解析记录在本地DNS服务器的缓存时间，缓存时间越长更新生效越慢，以秒为单位。 **约束限制：** 不涉及。 **取值范围：** 1~2147483647。 **默认取值：** 300
        :type ttl: int
        :param weight: **参数解释：** 解析记录的权重。 **约束限制：** MX记录集不支持权重，创建时会忽略权重字段，如果您的MX记录集有多个值，在一条记录集里写多个值即可。(若存在多条同主机记录、同线路类型的MX记录，会自动合并为一条创建) **取值范围：** 0~1000。 **默认取值：** 不涉及。
        :type weight: int
        :param records: **参数解释：** 解析记录的值。不同类型解析记录对应的值的规则不同。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type records: list[str]
        :param status: **参数解释：** 解析记录的状态。 **约束限制：** 不涉及。 **取值范围：** - ENABLE：启用解析 - DISABLE：暂停解析  **默认取值：** ENABLE。
        :type status: str
        """
        
        

        self._zone_name = None
        self._name = None
        self._type = None
        self._line = None
        self._ttl = None
        self._weight = None
        self._records = None
        self._status = None
        self.discriminator = None

        self.zone_name = zone_name
        if name is not None:
            self.name = name
        self.type = type
        if line is not None:
            self.line = line
        if ttl is not None:
            self.ttl = ttl
        if weight is not None:
            self.weight = weight
        self.records = records
        if status is not None:
            self.status = status

    @property
    def zone_name(self):
        r"""Gets the zone_name of this BatchCreatePublicRecordsetsTaskItem.

        **参数解释：** 托管该记录的域名。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The zone_name of this BatchCreatePublicRecordsetsTaskItem.
        :rtype: str
        """
        return self._zone_name

    @zone_name.setter
    def zone_name(self, zone_name):
        r"""Sets the zone_name of this BatchCreatePublicRecordsetsTaskItem.

        **参数解释：** 托管该记录的域名。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param zone_name: The zone_name of this BatchCreatePublicRecordsetsTaskItem.
        :type zone_name: str
        """
        self._zone_name = zone_name

    @property
    def name(self):
        r"""Gets the name of this BatchCreatePublicRecordsetsTaskItem.

        **参数解释：** 主机记录或域名。 末尾有点则认为是完整域名，如果不包含点，则认为是域名前缀。例如： 输入\"www\"，创建成功后域名显示为\"www.example.com.\" 输入\"www.example.com.\"（注意域名末尾有点），创建成功后域名显示为\"www.example.com.\" 输入\"www.example.com\"（注意域名末尾没有点），创建成功后域名显示为\"www.example.com.example.com.\" **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The name of this BatchCreatePublicRecordsetsTaskItem.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this BatchCreatePublicRecordsetsTaskItem.

        **参数解释：** 主机记录或域名。 末尾有点则认为是完整域名，如果不包含点，则认为是域名前缀。例如： 输入\"www\"，创建成功后域名显示为\"www.example.com.\" 输入\"www.example.com.\"（注意域名末尾有点），创建成功后域名显示为\"www.example.com.\" 输入\"www.example.com\"（注意域名末尾没有点），创建成功后域名显示为\"www.example.com.example.com.\" **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param name: The name of this BatchCreatePublicRecordsetsTaskItem.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this BatchCreatePublicRecordsetsTaskItem.

        **参数解释：** 记录集的类型。 **约束限制：** 不涉及。 **取值范围：** - 公网域名的记录类型: A、CNAME、MX、AAAA、TXT、SRV、NS、CAA。  **默认取值：** 不涉及。

        :return: The type of this BatchCreatePublicRecordsetsTaskItem.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this BatchCreatePublicRecordsetsTaskItem.

        **参数解释：** 记录集的类型。 **约束限制：** 不涉及。 **取值范围：** - 公网域名的记录类型: A、CNAME、MX、AAAA、TXT、SRV、NS、CAA。  **默认取值：** 不涉及。

        :param type: The type of this BatchCreatePublicRecordsetsTaskItem.
        :type type: str
        """
        self._type = type

    @property
    def line(self):
        r"""Gets the line of this BatchCreatePublicRecordsetsTaskItem.

        **参数解释：** 解析线路ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** default_view。

        :return: The line of this BatchCreatePublicRecordsetsTaskItem.
        :rtype: str
        """
        return self._line

    @line.setter
    def line(self, line):
        r"""Sets the line of this BatchCreatePublicRecordsetsTaskItem.

        **参数解释：** 解析线路ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** default_view。

        :param line: The line of this BatchCreatePublicRecordsetsTaskItem.
        :type line: str
        """
        self._line = line

    @property
    def ttl(self):
        r"""Gets the ttl of this BatchCreatePublicRecordsetsTaskItem.

        **参数解释：** 解析记录在本地DNS服务器的缓存时间，缓存时间越长更新生效越慢，以秒为单位。 **约束限制：** 不涉及。 **取值范围：** 1~2147483647。 **默认取值：** 300

        :return: The ttl of this BatchCreatePublicRecordsetsTaskItem.
        :rtype: int
        """
        return self._ttl

    @ttl.setter
    def ttl(self, ttl):
        r"""Sets the ttl of this BatchCreatePublicRecordsetsTaskItem.

        **参数解释：** 解析记录在本地DNS服务器的缓存时间，缓存时间越长更新生效越慢，以秒为单位。 **约束限制：** 不涉及。 **取值范围：** 1~2147483647。 **默认取值：** 300

        :param ttl: The ttl of this BatchCreatePublicRecordsetsTaskItem.
        :type ttl: int
        """
        self._ttl = ttl

    @property
    def weight(self):
        r"""Gets the weight of this BatchCreatePublicRecordsetsTaskItem.

        **参数解释：** 解析记录的权重。 **约束限制：** MX记录集不支持权重，创建时会忽略权重字段，如果您的MX记录集有多个值，在一条记录集里写多个值即可。(若存在多条同主机记录、同线路类型的MX记录，会自动合并为一条创建) **取值范围：** 0~1000。 **默认取值：** 不涉及。

        :return: The weight of this BatchCreatePublicRecordsetsTaskItem.
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        r"""Sets the weight of this BatchCreatePublicRecordsetsTaskItem.

        **参数解释：** 解析记录的权重。 **约束限制：** MX记录集不支持权重，创建时会忽略权重字段，如果您的MX记录集有多个值，在一条记录集里写多个值即可。(若存在多条同主机记录、同线路类型的MX记录，会自动合并为一条创建) **取值范围：** 0~1000。 **默认取值：** 不涉及。

        :param weight: The weight of this BatchCreatePublicRecordsetsTaskItem.
        :type weight: int
        """
        self._weight = weight

    @property
    def records(self):
        r"""Gets the records of this BatchCreatePublicRecordsetsTaskItem.

        **参数解释：** 解析记录的值。不同类型解析记录对应的值的规则不同。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The records of this BatchCreatePublicRecordsetsTaskItem.
        :rtype: list[str]
        """
        return self._records

    @records.setter
    def records(self, records):
        r"""Sets the records of this BatchCreatePublicRecordsetsTaskItem.

        **参数解释：** 解析记录的值。不同类型解析记录对应的值的规则不同。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param records: The records of this BatchCreatePublicRecordsetsTaskItem.
        :type records: list[str]
        """
        self._records = records

    @property
    def status(self):
        r"""Gets the status of this BatchCreatePublicRecordsetsTaskItem.

        **参数解释：** 解析记录的状态。 **约束限制：** 不涉及。 **取值范围：** - ENABLE：启用解析 - DISABLE：暂停解析  **默认取值：** ENABLE。

        :return: The status of this BatchCreatePublicRecordsetsTaskItem.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this BatchCreatePublicRecordsetsTaskItem.

        **参数解释：** 解析记录的状态。 **约束限制：** 不涉及。 **取值范围：** - ENABLE：启用解析 - DISABLE：暂停解析  **默认取值：** ENABLE。

        :param status: The status of this BatchCreatePublicRecordsetsTaskItem.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, BatchCreatePublicRecordsetsTaskItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
