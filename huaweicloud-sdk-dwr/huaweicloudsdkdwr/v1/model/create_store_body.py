# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateStoreBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'store_name': 'str',
        'region': 'str',
        'availability_zones': 'list[str]',
        'flavor': 'Flavor',
        'charge_info': 'ChargeInfo',
        'description': 'str'
    }

    attribute_map = {
        'store_name': 'store_name',
        'region': 'region',
        'availability_zones': 'availability_zones',
        'flavor': 'flavor',
        'charge_info': 'charge_info',
        'description': 'description'
    }

    def __init__(self, store_name=None, region=None, availability_zones=None, flavor=None, charge_info=None, description=None):
        r"""CreateStoreBody

        The model defined in huaweicloud sdk

        :param store_name: **参数解释：** 知识仓实例名称，region内唯一。 **约束限制：** 长度范围为3到63个字符，支持小写字母、数字、中划线（-），第一个字符只能够是小写字母，中划线(-)不得出现在字符串末尾。 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type store_name: str
        :param region: **参数解释：** 区域ID。 **约束限制**： 不涉及。 **取值范围：** 取值：非空，请参见地区和终端节点。 **默认取值:** 无
        :type region: str
        :param availability_zones: **参数解释：** 可用区ID列表，支持1个，或者多个。 **约束限制：** 不涉及。
        :type availability_zones: list[str]
        :param flavor: 
        :type flavor: :class:`huaweicloudsdkdwr.v1.Flavor`
        :param charge_info: 
        :type charge_info: :class:`huaweicloudsdkdwr.v1.ChargeInfo`
        :param description: **参数解释：** 知识仓实例描述信息。 **约束限制：** 有效长度0-255字节。 **取值范围：** 不涉及。 **默认取值:** 不涉及。
        :type description: str
        """
        
        

        self._store_name = None
        self._region = None
        self._availability_zones = None
        self._flavor = None
        self._charge_info = None
        self._description = None
        self.discriminator = None

        self.store_name = store_name
        self.region = region
        self.availability_zones = availability_zones
        self.flavor = flavor
        if charge_info is not None:
            self.charge_info = charge_info
        if description is not None:
            self.description = description

    @property
    def store_name(self):
        r"""Gets the store_name of this CreateStoreBody.

        **参数解释：** 知识仓实例名称，region内唯一。 **约束限制：** 长度范围为3到63个字符，支持小写字母、数字、中划线（-），第一个字符只能够是小写字母，中划线(-)不得出现在字符串末尾。 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The store_name of this CreateStoreBody.
        :rtype: str
        """
        return self._store_name

    @store_name.setter
    def store_name(self, store_name):
        r"""Sets the store_name of this CreateStoreBody.

        **参数解释：** 知识仓实例名称，region内唯一。 **约束限制：** 长度范围为3到63个字符，支持小写字母、数字、中划线（-），第一个字符只能够是小写字母，中划线(-)不得出现在字符串末尾。 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param store_name: The store_name of this CreateStoreBody.
        :type store_name: str
        """
        self._store_name = store_name

    @property
    def region(self):
        r"""Gets the region of this CreateStoreBody.

        **参数解释：** 区域ID。 **约束限制**： 不涉及。 **取值范围：** 取值：非空，请参见地区和终端节点。 **默认取值:** 无

        :return: The region of this CreateStoreBody.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this CreateStoreBody.

        **参数解释：** 区域ID。 **约束限制**： 不涉及。 **取值范围：** 取值：非空，请参见地区和终端节点。 **默认取值:** 无

        :param region: The region of this CreateStoreBody.
        :type region: str
        """
        self._region = region

    @property
    def availability_zones(self):
        r"""Gets the availability_zones of this CreateStoreBody.

        **参数解释：** 可用区ID列表，支持1个，或者多个。 **约束限制：** 不涉及。

        :return: The availability_zones of this CreateStoreBody.
        :rtype: list[str]
        """
        return self._availability_zones

    @availability_zones.setter
    def availability_zones(self, availability_zones):
        r"""Sets the availability_zones of this CreateStoreBody.

        **参数解释：** 可用区ID列表，支持1个，或者多个。 **约束限制：** 不涉及。

        :param availability_zones: The availability_zones of this CreateStoreBody.
        :type availability_zones: list[str]
        """
        self._availability_zones = availability_zones

    @property
    def flavor(self):
        r"""Gets the flavor of this CreateStoreBody.

        :return: The flavor of this CreateStoreBody.
        :rtype: :class:`huaweicloudsdkdwr.v1.Flavor`
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        r"""Sets the flavor of this CreateStoreBody.

        :param flavor: The flavor of this CreateStoreBody.
        :type flavor: :class:`huaweicloudsdkdwr.v1.Flavor`
        """
        self._flavor = flavor

    @property
    def charge_info(self):
        r"""Gets the charge_info of this CreateStoreBody.

        :return: The charge_info of this CreateStoreBody.
        :rtype: :class:`huaweicloudsdkdwr.v1.ChargeInfo`
        """
        return self._charge_info

    @charge_info.setter
    def charge_info(self, charge_info):
        r"""Sets the charge_info of this CreateStoreBody.

        :param charge_info: The charge_info of this CreateStoreBody.
        :type charge_info: :class:`huaweicloudsdkdwr.v1.ChargeInfo`
        """
        self._charge_info = charge_info

    @property
    def description(self):
        r"""Gets the description of this CreateStoreBody.

        **参数解释：** 知识仓实例描述信息。 **约束限制：** 有效长度0-255字节。 **取值范围：** 不涉及。 **默认取值:** 不涉及。

        :return: The description of this CreateStoreBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateStoreBody.

        **参数解释：** 知识仓实例描述信息。 **约束限制：** 有效长度0-255字节。 **取值范围：** 不涉及。 **默认取值:** 不涉及。

        :param description: The description of this CreateStoreBody.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, CreateStoreBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
