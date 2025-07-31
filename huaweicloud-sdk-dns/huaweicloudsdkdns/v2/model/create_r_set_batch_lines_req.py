# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateRSetBatchLinesReq:

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
        'lines': 'list[BatchCreateRecordSetWithLine]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'type': 'type',
        'lines': 'lines'
    }

    def __init__(self, name=None, description=None, type=None, lines=None):
        r"""CreateRSetBatchLinesReq

        The model defined in huaweicloud sdk

        :param name: **参数解释：** 域名，后缀需以zone name结束且为FQDN（Fully Qualified Domain Name，全称域名），即以“.”结束的完整主机名。 如“www.example.com.”。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type name: str
        :param description: **参数解释：** 记录集的描述信息。 **约束限制：** 不涉及。 **取值范围：** 长度不超过255个字符。 **默认取值：** 不涉及。
        :type description: str
        :param type: **参数解释：** 记录集的类型。 **约束限制：** 不涉及。 **取值范围：** A、AAAA、MX、CNAME、TXT、SRV、NS、SOA、CAA。 **默认取值：** 不涉及。
        :type type: str
        :param lines: **参数解释：** 解析线路域名参数。 **约束限制：** 最多支持50个。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type lines: list[:class:`huaweicloudsdkdns.v2.BatchCreateRecordSetWithLine`]
        """
        
        

        self._name = None
        self._description = None
        self._type = None
        self._lines = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.type = type
        self.lines = lines

    @property
    def name(self):
        r"""Gets the name of this CreateRSetBatchLinesReq.

        **参数解释：** 域名，后缀需以zone name结束且为FQDN（Fully Qualified Domain Name，全称域名），即以“.”结束的完整主机名。 如“www.example.com.”。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The name of this CreateRSetBatchLinesReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateRSetBatchLinesReq.

        **参数解释：** 域名，后缀需以zone name结束且为FQDN（Fully Qualified Domain Name，全称域名），即以“.”结束的完整主机名。 如“www.example.com.”。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param name: The name of this CreateRSetBatchLinesReq.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this CreateRSetBatchLinesReq.

        **参数解释：** 记录集的描述信息。 **约束限制：** 不涉及。 **取值范围：** 长度不超过255个字符。 **默认取值：** 不涉及。

        :return: The description of this CreateRSetBatchLinesReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateRSetBatchLinesReq.

        **参数解释：** 记录集的描述信息。 **约束限制：** 不涉及。 **取值范围：** 长度不超过255个字符。 **默认取值：** 不涉及。

        :param description: The description of this CreateRSetBatchLinesReq.
        :type description: str
        """
        self._description = description

    @property
    def type(self):
        r"""Gets the type of this CreateRSetBatchLinesReq.

        **参数解释：** 记录集的类型。 **约束限制：** 不涉及。 **取值范围：** A、AAAA、MX、CNAME、TXT、SRV、NS、SOA、CAA。 **默认取值：** 不涉及。

        :return: The type of this CreateRSetBatchLinesReq.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CreateRSetBatchLinesReq.

        **参数解释：** 记录集的类型。 **约束限制：** 不涉及。 **取值范围：** A、AAAA、MX、CNAME、TXT、SRV、NS、SOA、CAA。 **默认取值：** 不涉及。

        :param type: The type of this CreateRSetBatchLinesReq.
        :type type: str
        """
        self._type = type

    @property
    def lines(self):
        r"""Gets the lines of this CreateRSetBatchLinesReq.

        **参数解释：** 解析线路域名参数。 **约束限制：** 最多支持50个。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The lines of this CreateRSetBatchLinesReq.
        :rtype: list[:class:`huaweicloudsdkdns.v2.BatchCreateRecordSetWithLine`]
        """
        return self._lines

    @lines.setter
    def lines(self, lines):
        r"""Sets the lines of this CreateRSetBatchLinesReq.

        **参数解释：** 解析线路域名参数。 **约束限制：** 最多支持50个。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param lines: The lines of this CreateRSetBatchLinesReq.
        :type lines: list[:class:`huaweicloudsdkdns.v2.BatchCreateRecordSetWithLine`]
        """
        self._lines = lines

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
        if not isinstance(other, CreateRSetBatchLinesReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
