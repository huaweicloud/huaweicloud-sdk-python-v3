# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDomainDetectionRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'zone_id': 'str',
        'type': 'str',
        'domain_name': 'str'
    }

    attribute_map = {
        'zone_id': 'zone_id',
        'type': 'type',
        'domain_name': 'domain_name'
    }

    def __init__(self, zone_id=None, type=None, domain_name=None):
        r"""ShowDomainDetectionRequest

        The model defined in huaweicloud sdk

        :param zone_id: **参数解释：** 域名ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type zone_id: str
        :param type: 待诊断记录集的类型。 取值范围：CNAME、TXT、MX。
        :type type: str
        :param domain_name: 待诊断记录集的名称。
        :type domain_name: str
        """
        
        

        self._zone_id = None
        self._type = None
        self._domain_name = None
        self.discriminator = None

        self.zone_id = zone_id
        if type is not None:
            self.type = type
        self.domain_name = domain_name

    @property
    def zone_id(self):
        r"""Gets the zone_id of this ShowDomainDetectionRequest.

        **参数解释：** 域名ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The zone_id of this ShowDomainDetectionRequest.
        :rtype: str
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, zone_id):
        r"""Sets the zone_id of this ShowDomainDetectionRequest.

        **参数解释：** 域名ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param zone_id: The zone_id of this ShowDomainDetectionRequest.
        :type zone_id: str
        """
        self._zone_id = zone_id

    @property
    def type(self):
        r"""Gets the type of this ShowDomainDetectionRequest.

        待诊断记录集的类型。 取值范围：CNAME、TXT、MX。

        :return: The type of this ShowDomainDetectionRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ShowDomainDetectionRequest.

        待诊断记录集的类型。 取值范围：CNAME、TXT、MX。

        :param type: The type of this ShowDomainDetectionRequest.
        :type type: str
        """
        self._type = type

    @property
    def domain_name(self):
        r"""Gets the domain_name of this ShowDomainDetectionRequest.

        待诊断记录集的名称。

        :return: The domain_name of this ShowDomainDetectionRequest.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        r"""Sets the domain_name of this ShowDomainDetectionRequest.

        待诊断记录集的名称。

        :param domain_name: The domain_name of this ShowDomainDetectionRequest.
        :type domain_name: str
        """
        self._domain_name = domain_name

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
        if not isinstance(other, ShowDomainDetectionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
