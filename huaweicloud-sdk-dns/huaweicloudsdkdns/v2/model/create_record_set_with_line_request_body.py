# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateRecordSetWithLineRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'description': 'str',
        'type': 'str',
        'status': 'str',
        'ttl': 'int',
        'records': 'list[str]',
        'line': 'str',
        'tags': 'list[Tag]',
        'weight': 'int',
        'alias_target': 'AliasTarget'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'type': 'type',
        'status': 'status',
        'ttl': 'ttl',
        'records': 'records',
        'line': 'line',
        'tags': 'tags',
        'weight': 'weight',
        'alias_target': 'alias_target'
    }

    def __init__(self, name=None, description=None, type=None, status=None, ttl=None, records=None, line=None, tags=None, weight=None, alias_target=None):
        r"""CreateRecordSetWithLineRequestBody

        The model defined in huaweicloud sdk

        :param name: **参数解释：** 域名，后缀需以zone name结束且为FQDN（Fully Qualified Domain Name，全称域名），即以“.”结束的完整主机名。 如“www.example.com.”。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type name: str
        :param description: **参数解释：** 记录集的描述信息。 **约束限制：** 不涉及。 **取值范围：** 长度不超过255个字符。 **默认取值：** 不涉及。
        :type description: str
        :param type: **参数解释：** 记录集的类型。 **约束限制：** 不涉及。 **取值范围：** - 公网域名的记录类型: A、AAAA、MX、CNAME、TXT、SRV、NS、SOA、CAA。 - 内网域名的记录类型: A、AAAA、MX、CNAME、TXT、PTR、SRV、NS、SOA。  **默认取值：** 不涉及。
        :type type: str
        :param status: **参数解释：** 解析记录的状态。 **约束限制：** 不涉及。 **取值范围：** - ENABLE：启用解析 - DISABLE：暂停解析  **默认取值：** ENABLE。
        :type status: str
        :param ttl: **参数解释：** 解析记录在本地DNS服务器的缓存时间，缓存时间越长更新生效越慢，以秒为单位。 **约束限制：** 不涉及。 **取值范围：** 1~2147483647。 **默认取值：** 300
        :type ttl: int
        :param records: **参数解释：** 解析记录的值。不同类型解析记录对应的值的规则不同。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type records: list[str]
        :param line: **参数解释：** 解析线路ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type line: str
        :param tags: **参数解释：** 资源标签。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type tags: list[:class:`huaweicloudsdkdns.v2.Tag`]
        :param weight: **参数解释：** 解析记录的权重。 **约束限制：** 别名记录不支持权重。 **取值范围：** 0~1000。 **默认取值：** - 公网记录集默认为1。 - 内网记录集默认为null。
        :type weight: int
        :param alias_target: 
        :type alias_target: :class:`huaweicloudsdkdns.v2.AliasTarget`
        """
        
        

        self._name = None
        self._description = None
        self._type = None
        self._status = None
        self._ttl = None
        self._records = None
        self._line = None
        self._tags = None
        self._weight = None
        self._alias_target = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.type = type
        if status is not None:
            self.status = status
        if ttl is not None:
            self.ttl = ttl
        if records is not None:
            self.records = records
        if line is not None:
            self.line = line
        if tags is not None:
            self.tags = tags
        if weight is not None:
            self.weight = weight
        if alias_target is not None:
            self.alias_target = alias_target

    @property
    def name(self):
        r"""Gets the name of this CreateRecordSetWithLineRequestBody.

        **参数解释：** 域名，后缀需以zone name结束且为FQDN（Fully Qualified Domain Name，全称域名），即以“.”结束的完整主机名。 如“www.example.com.”。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The name of this CreateRecordSetWithLineRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateRecordSetWithLineRequestBody.

        **参数解释：** 域名，后缀需以zone name结束且为FQDN（Fully Qualified Domain Name，全称域名），即以“.”结束的完整主机名。 如“www.example.com.”。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param name: The name of this CreateRecordSetWithLineRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this CreateRecordSetWithLineRequestBody.

        **参数解释：** 记录集的描述信息。 **约束限制：** 不涉及。 **取值范围：** 长度不超过255个字符。 **默认取值：** 不涉及。

        :return: The description of this CreateRecordSetWithLineRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateRecordSetWithLineRequestBody.

        **参数解释：** 记录集的描述信息。 **约束限制：** 不涉及。 **取值范围：** 长度不超过255个字符。 **默认取值：** 不涉及。

        :param description: The description of this CreateRecordSetWithLineRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def type(self):
        r"""Gets the type of this CreateRecordSetWithLineRequestBody.

        **参数解释：** 记录集的类型。 **约束限制：** 不涉及。 **取值范围：** - 公网域名的记录类型: A、AAAA、MX、CNAME、TXT、SRV、NS、SOA、CAA。 - 内网域名的记录类型: A、AAAA、MX、CNAME、TXT、PTR、SRV、NS、SOA。  **默认取值：** 不涉及。

        :return: The type of this CreateRecordSetWithLineRequestBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CreateRecordSetWithLineRequestBody.

        **参数解释：** 记录集的类型。 **约束限制：** 不涉及。 **取值范围：** - 公网域名的记录类型: A、AAAA、MX、CNAME、TXT、SRV、NS、SOA、CAA。 - 内网域名的记录类型: A、AAAA、MX、CNAME、TXT、PTR、SRV、NS、SOA。  **默认取值：** 不涉及。

        :param type: The type of this CreateRecordSetWithLineRequestBody.
        :type type: str
        """
        self._type = type

    @property
    def status(self):
        r"""Gets the status of this CreateRecordSetWithLineRequestBody.

        **参数解释：** 解析记录的状态。 **约束限制：** 不涉及。 **取值范围：** - ENABLE：启用解析 - DISABLE：暂停解析  **默认取值：** ENABLE。

        :return: The status of this CreateRecordSetWithLineRequestBody.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CreateRecordSetWithLineRequestBody.

        **参数解释：** 解析记录的状态。 **约束限制：** 不涉及。 **取值范围：** - ENABLE：启用解析 - DISABLE：暂停解析  **默认取值：** ENABLE。

        :param status: The status of this CreateRecordSetWithLineRequestBody.
        :type status: str
        """
        self._status = status

    @property
    def ttl(self):
        r"""Gets the ttl of this CreateRecordSetWithLineRequestBody.

        **参数解释：** 解析记录在本地DNS服务器的缓存时间，缓存时间越长更新生效越慢，以秒为单位。 **约束限制：** 不涉及。 **取值范围：** 1~2147483647。 **默认取值：** 300

        :return: The ttl of this CreateRecordSetWithLineRequestBody.
        :rtype: int
        """
        return self._ttl

    @ttl.setter
    def ttl(self, ttl):
        r"""Sets the ttl of this CreateRecordSetWithLineRequestBody.

        **参数解释：** 解析记录在本地DNS服务器的缓存时间，缓存时间越长更新生效越慢，以秒为单位。 **约束限制：** 不涉及。 **取值范围：** 1~2147483647。 **默认取值：** 300

        :param ttl: The ttl of this CreateRecordSetWithLineRequestBody.
        :type ttl: int
        """
        self._ttl = ttl

    @property
    def records(self):
        r"""Gets the records of this CreateRecordSetWithLineRequestBody.

        **参数解释：** 解析记录的值。不同类型解析记录对应的值的规则不同。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The records of this CreateRecordSetWithLineRequestBody.
        :rtype: list[str]
        """
        return self._records

    @records.setter
    def records(self, records):
        r"""Sets the records of this CreateRecordSetWithLineRequestBody.

        **参数解释：** 解析记录的值。不同类型解析记录对应的值的规则不同。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param records: The records of this CreateRecordSetWithLineRequestBody.
        :type records: list[str]
        """
        self._records = records

    @property
    def line(self):
        r"""Gets the line of this CreateRecordSetWithLineRequestBody.

        **参数解释：** 解析线路ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The line of this CreateRecordSetWithLineRequestBody.
        :rtype: str
        """
        return self._line

    @line.setter
    def line(self, line):
        r"""Sets the line of this CreateRecordSetWithLineRequestBody.

        **参数解释：** 解析线路ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param line: The line of this CreateRecordSetWithLineRequestBody.
        :type line: str
        """
        self._line = line

    @property
    def tags(self):
        r"""Gets the tags of this CreateRecordSetWithLineRequestBody.

        **参数解释：** 资源标签。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The tags of this CreateRecordSetWithLineRequestBody.
        :rtype: list[:class:`huaweicloudsdkdns.v2.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this CreateRecordSetWithLineRequestBody.

        **参数解释：** 资源标签。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param tags: The tags of this CreateRecordSetWithLineRequestBody.
        :type tags: list[:class:`huaweicloudsdkdns.v2.Tag`]
        """
        self._tags = tags

    @property
    def weight(self):
        r"""Gets the weight of this CreateRecordSetWithLineRequestBody.

        **参数解释：** 解析记录的权重。 **约束限制：** 别名记录不支持权重。 **取值范围：** 0~1000。 **默认取值：** - 公网记录集默认为1。 - 内网记录集默认为null。

        :return: The weight of this CreateRecordSetWithLineRequestBody.
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        r"""Sets the weight of this CreateRecordSetWithLineRequestBody.

        **参数解释：** 解析记录的权重。 **约束限制：** 别名记录不支持权重。 **取值范围：** 0~1000。 **默认取值：** - 公网记录集默认为1。 - 内网记录集默认为null。

        :param weight: The weight of this CreateRecordSetWithLineRequestBody.
        :type weight: int
        """
        self._weight = weight

    @property
    def alias_target(self):
        r"""Gets the alias_target of this CreateRecordSetWithLineRequestBody.

        :return: The alias_target of this CreateRecordSetWithLineRequestBody.
        :rtype: :class:`huaweicloudsdkdns.v2.AliasTarget`
        """
        return self._alias_target

    @alias_target.setter
    def alias_target(self, alias_target):
        r"""Sets the alias_target of this CreateRecordSetWithLineRequestBody.

        :param alias_target: The alias_target of this CreateRecordSetWithLineRequestBody.
        :type alias_target: :class:`huaweicloudsdkdns.v2.AliasTarget`
        """
        self._alias_target = alias_target

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
        if not isinstance(other, CreateRecordSetWithLineRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
