# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ServerFlavorinstanceResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'arch': 'str',
        'availability_zone': 'str',
        'charging_mode': 'str',
        'count': 'int',
        'flavor': 'str',
        'flavor_type': 'str',
        'roce_num': 'int',
        'server_type': 'str',
        'sku_code': 'str',
        'specification': 'str',
        'status': 'str',
        'is_sold_out': 'bool'
    }

    attribute_map = {
        'arch': 'arch',
        'availability_zone': 'availability_zone',
        'charging_mode': 'charging_mode',
        'count': 'count',
        'flavor': 'flavor',
        'flavor_type': 'flavor_type',
        'roce_num': 'roce_num',
        'server_type': 'server_type',
        'sku_code': 'sku_code',
        'specification': 'specification',
        'status': 'status',
        'is_sold_out': 'is_sold_out'
    }

    def __init__(self, arch=None, availability_zone=None, charging_mode=None, count=None, flavor=None, flavor_type=None, roce_num=None, server_type=None, sku_code=None, specification=None, status=None, is_sold_out=None):
        r"""ServerFlavorinstanceResponse

        The model defined in huaweicloud sdk

        :param arch: **参数解释**：CPU架构。 **约束限制**：不涉及。 **取值范围**： - X86：CPU架构为X86 - ARM：CPU架构为ARM  **默认取值**：不涉及。
        :type arch: str
        :param availability_zone: **参数解释**：分区名。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type availability_zone: str
        :param charging_mode: **参数解释**：计费模式。 **约束限制**：不涉及。 **取值范围**： - PRE_PAID：计费模式为包年/包月 - POST_PAID：计费模式为按需计费 **默认取值**：不涉及。
        :type charging_mode: str
        :param count: **参数解释**：数量。 **约束限制**：不涉及。 **默认取值**：不涉及。
        :type count: int
        :param flavor: **参数解释**：规格名称。 **约束限制**：不涉及。 **默认取值**：不涉及。
        :type flavor: str
        :param flavor_type: **参数解释**：规格类型。 **约束限制**：不涉及。 **默认取值**：不涉及。
        :type flavor_type: str
        :param roce_num: **参数解释**：roce数量。 **约束限制**：不涉及。 **默认取值**：不涉及。
        :type roce_num: int
        :param server_type: **参数解释**：服务类型。 **约束限制**：不涉及。 **取值范围**： - BMS：资源类型为裸金属服务器 - ECS：资源类型为弹性云服务器 - HPS：资源类型为超节点服务器  **默认取值**：不涉及。
        :type server_type: str
        :param sku_code: **参数解释**：计费码。 **约束限制**：不涉及。 **默认取值**：不涉及。
        :type sku_code: str
        :param specification: **参数解释**：规格详情。 **约束限制**：不涉及。 **默认取值**：不涉及。
        :type specification: str
        :param status: **参数解释**：状态。 **约束限制**：不涉及。 **默认取值**：不涉及。
        :type status: str
        :param is_sold_out: **参数解释**：是否售罄。 **约束限制**：不涉及。 **取值范围**： - true：已售罄 - false：未售罄  **默认取值**：false。
        :type is_sold_out: bool
        """
        
        

        self._arch = None
        self._availability_zone = None
        self._charging_mode = None
        self._count = None
        self._flavor = None
        self._flavor_type = None
        self._roce_num = None
        self._server_type = None
        self._sku_code = None
        self._specification = None
        self._status = None
        self._is_sold_out = None
        self.discriminator = None

        if arch is not None:
            self.arch = arch
        if availability_zone is not None:
            self.availability_zone = availability_zone
        if charging_mode is not None:
            self.charging_mode = charging_mode
        if count is not None:
            self.count = count
        if flavor is not None:
            self.flavor = flavor
        if flavor_type is not None:
            self.flavor_type = flavor_type
        if roce_num is not None:
            self.roce_num = roce_num
        if server_type is not None:
            self.server_type = server_type
        if sku_code is not None:
            self.sku_code = sku_code
        if specification is not None:
            self.specification = specification
        if status is not None:
            self.status = status
        if is_sold_out is not None:
            self.is_sold_out = is_sold_out

    @property
    def arch(self):
        r"""Gets the arch of this ServerFlavorinstanceResponse.

        **参数解释**：CPU架构。 **约束限制**：不涉及。 **取值范围**： - X86：CPU架构为X86 - ARM：CPU架构为ARM  **默认取值**：不涉及。

        :return: The arch of this ServerFlavorinstanceResponse.
        :rtype: str
        """
        return self._arch

    @arch.setter
    def arch(self, arch):
        r"""Sets the arch of this ServerFlavorinstanceResponse.

        **参数解释**：CPU架构。 **约束限制**：不涉及。 **取值范围**： - X86：CPU架构为X86 - ARM：CPU架构为ARM  **默认取值**：不涉及。

        :param arch: The arch of this ServerFlavorinstanceResponse.
        :type arch: str
        """
        self._arch = arch

    @property
    def availability_zone(self):
        r"""Gets the availability_zone of this ServerFlavorinstanceResponse.

        **参数解释**：分区名。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The availability_zone of this ServerFlavorinstanceResponse.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        r"""Sets the availability_zone of this ServerFlavorinstanceResponse.

        **参数解释**：分区名。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param availability_zone: The availability_zone of this ServerFlavorinstanceResponse.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def charging_mode(self):
        r"""Gets the charging_mode of this ServerFlavorinstanceResponse.

        **参数解释**：计费模式。 **约束限制**：不涉及。 **取值范围**： - PRE_PAID：计费模式为包年/包月 - POST_PAID：计费模式为按需计费 **默认取值**：不涉及。

        :return: The charging_mode of this ServerFlavorinstanceResponse.
        :rtype: str
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        r"""Sets the charging_mode of this ServerFlavorinstanceResponse.

        **参数解释**：计费模式。 **约束限制**：不涉及。 **取值范围**： - PRE_PAID：计费模式为包年/包月 - POST_PAID：计费模式为按需计费 **默认取值**：不涉及。

        :param charging_mode: The charging_mode of this ServerFlavorinstanceResponse.
        :type charging_mode: str
        """
        self._charging_mode = charging_mode

    @property
    def count(self):
        r"""Gets the count of this ServerFlavorinstanceResponse.

        **参数解释**：数量。 **约束限制**：不涉及。 **默认取值**：不涉及。

        :return: The count of this ServerFlavorinstanceResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ServerFlavorinstanceResponse.

        **参数解释**：数量。 **约束限制**：不涉及。 **默认取值**：不涉及。

        :param count: The count of this ServerFlavorinstanceResponse.
        :type count: int
        """
        self._count = count

    @property
    def flavor(self):
        r"""Gets the flavor of this ServerFlavorinstanceResponse.

        **参数解释**：规格名称。 **约束限制**：不涉及。 **默认取值**：不涉及。

        :return: The flavor of this ServerFlavorinstanceResponse.
        :rtype: str
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        r"""Sets the flavor of this ServerFlavorinstanceResponse.

        **参数解释**：规格名称。 **约束限制**：不涉及。 **默认取值**：不涉及。

        :param flavor: The flavor of this ServerFlavorinstanceResponse.
        :type flavor: str
        """
        self._flavor = flavor

    @property
    def flavor_type(self):
        r"""Gets the flavor_type of this ServerFlavorinstanceResponse.

        **参数解释**：规格类型。 **约束限制**：不涉及。 **默认取值**：不涉及。

        :return: The flavor_type of this ServerFlavorinstanceResponse.
        :rtype: str
        """
        return self._flavor_type

    @flavor_type.setter
    def flavor_type(self, flavor_type):
        r"""Sets the flavor_type of this ServerFlavorinstanceResponse.

        **参数解释**：规格类型。 **约束限制**：不涉及。 **默认取值**：不涉及。

        :param flavor_type: The flavor_type of this ServerFlavorinstanceResponse.
        :type flavor_type: str
        """
        self._flavor_type = flavor_type

    @property
    def roce_num(self):
        r"""Gets the roce_num of this ServerFlavorinstanceResponse.

        **参数解释**：roce数量。 **约束限制**：不涉及。 **默认取值**：不涉及。

        :return: The roce_num of this ServerFlavorinstanceResponse.
        :rtype: int
        """
        return self._roce_num

    @roce_num.setter
    def roce_num(self, roce_num):
        r"""Sets the roce_num of this ServerFlavorinstanceResponse.

        **参数解释**：roce数量。 **约束限制**：不涉及。 **默认取值**：不涉及。

        :param roce_num: The roce_num of this ServerFlavorinstanceResponse.
        :type roce_num: int
        """
        self._roce_num = roce_num

    @property
    def server_type(self):
        r"""Gets the server_type of this ServerFlavorinstanceResponse.

        **参数解释**：服务类型。 **约束限制**：不涉及。 **取值范围**： - BMS：资源类型为裸金属服务器 - ECS：资源类型为弹性云服务器 - HPS：资源类型为超节点服务器  **默认取值**：不涉及。

        :return: The server_type of this ServerFlavorinstanceResponse.
        :rtype: str
        """
        return self._server_type

    @server_type.setter
    def server_type(self, server_type):
        r"""Sets the server_type of this ServerFlavorinstanceResponse.

        **参数解释**：服务类型。 **约束限制**：不涉及。 **取值范围**： - BMS：资源类型为裸金属服务器 - ECS：资源类型为弹性云服务器 - HPS：资源类型为超节点服务器  **默认取值**：不涉及。

        :param server_type: The server_type of this ServerFlavorinstanceResponse.
        :type server_type: str
        """
        self._server_type = server_type

    @property
    def sku_code(self):
        r"""Gets the sku_code of this ServerFlavorinstanceResponse.

        **参数解释**：计费码。 **约束限制**：不涉及。 **默认取值**：不涉及。

        :return: The sku_code of this ServerFlavorinstanceResponse.
        :rtype: str
        """
        return self._sku_code

    @sku_code.setter
    def sku_code(self, sku_code):
        r"""Sets the sku_code of this ServerFlavorinstanceResponse.

        **参数解释**：计费码。 **约束限制**：不涉及。 **默认取值**：不涉及。

        :param sku_code: The sku_code of this ServerFlavorinstanceResponse.
        :type sku_code: str
        """
        self._sku_code = sku_code

    @property
    def specification(self):
        r"""Gets the specification of this ServerFlavorinstanceResponse.

        **参数解释**：规格详情。 **约束限制**：不涉及。 **默认取值**：不涉及。

        :return: The specification of this ServerFlavorinstanceResponse.
        :rtype: str
        """
        return self._specification

    @specification.setter
    def specification(self, specification):
        r"""Sets the specification of this ServerFlavorinstanceResponse.

        **参数解释**：规格详情。 **约束限制**：不涉及。 **默认取值**：不涉及。

        :param specification: The specification of this ServerFlavorinstanceResponse.
        :type specification: str
        """
        self._specification = specification

    @property
    def status(self):
        r"""Gets the status of this ServerFlavorinstanceResponse.

        **参数解释**：状态。 **约束限制**：不涉及。 **默认取值**：不涉及。

        :return: The status of this ServerFlavorinstanceResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ServerFlavorinstanceResponse.

        **参数解释**：状态。 **约束限制**：不涉及。 **默认取值**：不涉及。

        :param status: The status of this ServerFlavorinstanceResponse.
        :type status: str
        """
        self._status = status

    @property
    def is_sold_out(self):
        r"""Gets the is_sold_out of this ServerFlavorinstanceResponse.

        **参数解释**：是否售罄。 **约束限制**：不涉及。 **取值范围**： - true：已售罄 - false：未售罄  **默认取值**：false。

        :return: The is_sold_out of this ServerFlavorinstanceResponse.
        :rtype: bool
        """
        return self._is_sold_out

    @is_sold_out.setter
    def is_sold_out(self, is_sold_out):
        r"""Sets the is_sold_out of this ServerFlavorinstanceResponse.

        **参数解释**：是否售罄。 **约束限制**：不涉及。 **取值范围**： - true：已售罄 - false：未售罄  **默认取值**：false。

        :param is_sold_out: The is_sold_out of this ServerFlavorinstanceResponse.
        :type is_sold_out: bool
        """
        self._is_sold_out = is_sold_out

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
        if not isinstance(other, ServerFlavorinstanceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
