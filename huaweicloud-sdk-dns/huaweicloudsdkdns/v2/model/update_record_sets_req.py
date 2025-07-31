# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateRecordSetsReq:

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
        'ttl': 'int',
        'records': 'list[str]',
        'weight': 'int'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'type': 'type',
        'ttl': 'ttl',
        'records': 'records',
        'weight': 'weight'
    }

    def __init__(self, name=None, description=None, type=None, ttl=None, records=None, weight=None):
        r"""UpdateRecordSetsReq

        The model defined in huaweicloud sdk

        :param name: **参数解释：** 域名，后缀需以zone name结束且为FQDN（Fully Qualified Domain Name，全称域名），即以“.”结束的完整主机名。 如“www.example.com.”。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type name: str
        :param description: **参数解释：** 记录集的描述信息。 **约束限制：** 不涉及。 **取值范围：** 长度不超过255个字符。 **默认取值：** 默认为空，表示维持原值。
        :type description: str
        :param type: **参数解释：** 记录集的类型。 **约束限制：** 不涉及。 **取值范围：** - 公网域名的记录类型: A、AAAA、MX、CNAME、TXT、SRV、NS、SOA、CAA。 - 内网域名的记录类型: A、AAAA、MX、CNAME、TXT、PTR、SRV、NS、SOA。  **默认取值：** 不涉及。
        :type type: str
        :param ttl: **参数解释：** 解析记录在本地DNS服务器的缓存时间，缓存时间越长更新生效越慢，以秒为单位。 **约束限制：** 不涉及。 **取值范围：** 1~2147483647。 **默认取值：** 默认为空，表示维持原值。
        :type ttl: int
        :param records: **参数解释：** 解析记录的值。不同类型解析记录对应的值的规则不同。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 默认为空，表示维持原值。
        :type records: list[str]
        :param weight: **参数解释：** 解析记录的权重。 **约束限制：** 不涉及。 **取值范围：** 取值范围：0~1000。 - 当weight为空时，表示该解析记录将保持原有设置的权重。 - 当weight&#x3D;0，表示该解析记录为备用域名解析记录。 - 当weight&gt;0，表示该解析记录为主用域名解析记录。  **默认取值：** 默认为空，表示维持原值。
        :type weight: int
        """
        
        

        self._name = None
        self._description = None
        self._type = None
        self._ttl = None
        self._records = None
        self._weight = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.type = type
        if ttl is not None:
            self.ttl = ttl
        if records is not None:
            self.records = records
        if weight is not None:
            self.weight = weight

    @property
    def name(self):
        r"""Gets the name of this UpdateRecordSetsReq.

        **参数解释：** 域名，后缀需以zone name结束且为FQDN（Fully Qualified Domain Name，全称域名），即以“.”结束的完整主机名。 如“www.example.com.”。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The name of this UpdateRecordSetsReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateRecordSetsReq.

        **参数解释：** 域名，后缀需以zone name结束且为FQDN（Fully Qualified Domain Name，全称域名），即以“.”结束的完整主机名。 如“www.example.com.”。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param name: The name of this UpdateRecordSetsReq.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this UpdateRecordSetsReq.

        **参数解释：** 记录集的描述信息。 **约束限制：** 不涉及。 **取值范围：** 长度不超过255个字符。 **默认取值：** 默认为空，表示维持原值。

        :return: The description of this UpdateRecordSetsReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateRecordSetsReq.

        **参数解释：** 记录集的描述信息。 **约束限制：** 不涉及。 **取值范围：** 长度不超过255个字符。 **默认取值：** 默认为空，表示维持原值。

        :param description: The description of this UpdateRecordSetsReq.
        :type description: str
        """
        self._description = description

    @property
    def type(self):
        r"""Gets the type of this UpdateRecordSetsReq.

        **参数解释：** 记录集的类型。 **约束限制：** 不涉及。 **取值范围：** - 公网域名的记录类型: A、AAAA、MX、CNAME、TXT、SRV、NS、SOA、CAA。 - 内网域名的记录类型: A、AAAA、MX、CNAME、TXT、PTR、SRV、NS、SOA。  **默认取值：** 不涉及。

        :return: The type of this UpdateRecordSetsReq.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this UpdateRecordSetsReq.

        **参数解释：** 记录集的类型。 **约束限制：** 不涉及。 **取值范围：** - 公网域名的记录类型: A、AAAA、MX、CNAME、TXT、SRV、NS、SOA、CAA。 - 内网域名的记录类型: A、AAAA、MX、CNAME、TXT、PTR、SRV、NS、SOA。  **默认取值：** 不涉及。

        :param type: The type of this UpdateRecordSetsReq.
        :type type: str
        """
        self._type = type

    @property
    def ttl(self):
        r"""Gets the ttl of this UpdateRecordSetsReq.

        **参数解释：** 解析记录在本地DNS服务器的缓存时间，缓存时间越长更新生效越慢，以秒为单位。 **约束限制：** 不涉及。 **取值范围：** 1~2147483647。 **默认取值：** 默认为空，表示维持原值。

        :return: The ttl of this UpdateRecordSetsReq.
        :rtype: int
        """
        return self._ttl

    @ttl.setter
    def ttl(self, ttl):
        r"""Sets the ttl of this UpdateRecordSetsReq.

        **参数解释：** 解析记录在本地DNS服务器的缓存时间，缓存时间越长更新生效越慢，以秒为单位。 **约束限制：** 不涉及。 **取值范围：** 1~2147483647。 **默认取值：** 默认为空，表示维持原值。

        :param ttl: The ttl of this UpdateRecordSetsReq.
        :type ttl: int
        """
        self._ttl = ttl

    @property
    def records(self):
        r"""Gets the records of this UpdateRecordSetsReq.

        **参数解释：** 解析记录的值。不同类型解析记录对应的值的规则不同。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 默认为空，表示维持原值。

        :return: The records of this UpdateRecordSetsReq.
        :rtype: list[str]
        """
        return self._records

    @records.setter
    def records(self, records):
        r"""Sets the records of this UpdateRecordSetsReq.

        **参数解释：** 解析记录的值。不同类型解析记录对应的值的规则不同。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 默认为空，表示维持原值。

        :param records: The records of this UpdateRecordSetsReq.
        :type records: list[str]
        """
        self._records = records

    @property
    def weight(self):
        r"""Gets the weight of this UpdateRecordSetsReq.

        **参数解释：** 解析记录的权重。 **约束限制：** 不涉及。 **取值范围：** 取值范围：0~1000。 - 当weight为空时，表示该解析记录将保持原有设置的权重。 - 当weight=0，表示该解析记录为备用域名解析记录。 - 当weight>0，表示该解析记录为主用域名解析记录。  **默认取值：** 默认为空，表示维持原值。

        :return: The weight of this UpdateRecordSetsReq.
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        r"""Sets the weight of this UpdateRecordSetsReq.

        **参数解释：** 解析记录的权重。 **约束限制：** 不涉及。 **取值范围：** 取值范围：0~1000。 - 当weight为空时，表示该解析记录将保持原有设置的权重。 - 当weight=0，表示该解析记录为备用域名解析记录。 - 当weight>0，表示该解析记录为主用域名解析记录。  **默认取值：** 默认为空，表示维持原值。

        :param weight: The weight of this UpdateRecordSetsReq.
        :type weight: int
        """
        self._weight = weight

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
        if not isinstance(other, UpdateRecordSetsReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
