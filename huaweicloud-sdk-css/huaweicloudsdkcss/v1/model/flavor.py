# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Flavor:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cpu': 'int',
        'ram': 'int',
        'name': 'str',
        'region': 'str',
        'typename': 'str',
        'diskrange': 'str',
        'cond_operation_status': 'str',
        'cond_operation_az': 'str',
        'localdisk': 'str',
        'flavor_type_cn': 'str',
        'flavor_type_en': 'str',
        'edge': 'bool',
        'str_id': 'str',
        'is_allow_https': 'bool'
    }

    attribute_map = {
        'cpu': 'cpu',
        'ram': 'ram',
        'name': 'name',
        'region': 'region',
        'typename': 'typename',
        'diskrange': 'diskrange',
        'cond_operation_status': 'condOperationStatus',
        'cond_operation_az': 'condOperationAz',
        'localdisk': 'localdisk',
        'flavor_type_cn': 'flavorTypeCn',
        'flavor_type_en': 'flavorTypeEn',
        'edge': 'edge',
        'str_id': 'str_id',
        'is_allow_https': 'isAllowHttps'
    }

    def __init__(self, cpu=None, ram=None, name=None, region=None, typename=None, diskrange=None, cond_operation_status=None, cond_operation_az=None, localdisk=None, flavor_type_cn=None, flavor_type_en=None, edge=None, str_id=None, is_allow_https=None):
        r"""Flavor

        The model defined in huaweicloud sdk

        :param cpu: **参数解释**： 实例的CPU核数。 **取值范围**： 不涉及
        :type cpu: int
        :param ram: **参数解释**： 实例的内存大小。单位GB。 **取值范围**： 不涉及
        :type ram: int
        :param name: **参数解释**： 规格名称。 **取值范围**： 不涉及
        :type name: str
        :param region: **参数解释**： 节点规格支持的Region。 **取值范围**： 不涉及
        :type region: str
        :param typename: **参数解释**： 节点类型名称。 **取值范围**： 不涉及
        :type typename: str
        :param diskrange: **参数解释**： 实例的硬盘容量范围，单位GB。 **取值范围**： 不涉及
        :type diskrange: str
        :param cond_operation_status: **参数解释**： 此参数是Region级配置，某个AZ没有在condOperationAz参数中配置时默认使用此参数的取值。 **取值范围**：   - normal：正常商用。   - sellout：售罄。
        :type cond_operation_status: str
        :param cond_operation_az: **参数解释**： 此参数是AZ级配置，某个AZ没有在此参数中配置时默认使用condOperationAz参数的取值。此参数的配置格式“az(xx)”。()内为某个AZ的flavor状态，()内必须要填有状态，不填为无效配置。状态的取值范围与condOperationStatus参数相同。 **取值范围**： 不涉及
        :type cond_operation_az: str
        :param localdisk: **参数解释**： 是否本地盘。 **取值范围**： - true：本地盘。 - false：非本地盘。
        :type localdisk: str
        :param flavor_type_cn: **参数解释**： 中文规格分类。 **取值范围**： 不涉及
        :type flavor_type_cn: str
        :param flavor_type_en: **参数解释**： 英文规格分类。 **取值范围**： 不涉及
        :type flavor_type_en: str
        :param edge: **参数解释**： 是否边缘区规格。 **取值范围**： - true：边缘区专属规格。 - false：通用规格。
        :type edge: bool
        :param str_id: **参数解释**： 规格id。 **取值范围**： 不涉及
        :type str_id: str
        :param is_allow_https: **参数解释**： 节点类型是否支持HTTPS协议访问。 **取值范围**： 不涉及
        :type is_allow_https: bool
        """
        
        

        self._cpu = None
        self._ram = None
        self._name = None
        self._region = None
        self._typename = None
        self._diskrange = None
        self._cond_operation_status = None
        self._cond_operation_az = None
        self._localdisk = None
        self._flavor_type_cn = None
        self._flavor_type_en = None
        self._edge = None
        self._str_id = None
        self._is_allow_https = None
        self.discriminator = None

        if cpu is not None:
            self.cpu = cpu
        if ram is not None:
            self.ram = ram
        if name is not None:
            self.name = name
        if region is not None:
            self.region = region
        if typename is not None:
            self.typename = typename
        if diskrange is not None:
            self.diskrange = diskrange
        if cond_operation_status is not None:
            self.cond_operation_status = cond_operation_status
        if cond_operation_az is not None:
            self.cond_operation_az = cond_operation_az
        if localdisk is not None:
            self.localdisk = localdisk
        if flavor_type_cn is not None:
            self.flavor_type_cn = flavor_type_cn
        if flavor_type_en is not None:
            self.flavor_type_en = flavor_type_en
        if edge is not None:
            self.edge = edge
        if str_id is not None:
            self.str_id = str_id
        if is_allow_https is not None:
            self.is_allow_https = is_allow_https

    @property
    def cpu(self):
        r"""Gets the cpu of this Flavor.

        **参数解释**： 实例的CPU核数。 **取值范围**： 不涉及

        :return: The cpu of this Flavor.
        :rtype: int
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        r"""Sets the cpu of this Flavor.

        **参数解释**： 实例的CPU核数。 **取值范围**： 不涉及

        :param cpu: The cpu of this Flavor.
        :type cpu: int
        """
        self._cpu = cpu

    @property
    def ram(self):
        r"""Gets the ram of this Flavor.

        **参数解释**： 实例的内存大小。单位GB。 **取值范围**： 不涉及

        :return: The ram of this Flavor.
        :rtype: int
        """
        return self._ram

    @ram.setter
    def ram(self, ram):
        r"""Sets the ram of this Flavor.

        **参数解释**： 实例的内存大小。单位GB。 **取值范围**： 不涉及

        :param ram: The ram of this Flavor.
        :type ram: int
        """
        self._ram = ram

    @property
    def name(self):
        r"""Gets the name of this Flavor.

        **参数解释**： 规格名称。 **取值范围**： 不涉及

        :return: The name of this Flavor.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Flavor.

        **参数解释**： 规格名称。 **取值范围**： 不涉及

        :param name: The name of this Flavor.
        :type name: str
        """
        self._name = name

    @property
    def region(self):
        r"""Gets the region of this Flavor.

        **参数解释**： 节点规格支持的Region。 **取值范围**： 不涉及

        :return: The region of this Flavor.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this Flavor.

        **参数解释**： 节点规格支持的Region。 **取值范围**： 不涉及

        :param region: The region of this Flavor.
        :type region: str
        """
        self._region = region

    @property
    def typename(self):
        r"""Gets the typename of this Flavor.

        **参数解释**： 节点类型名称。 **取值范围**： 不涉及

        :return: The typename of this Flavor.
        :rtype: str
        """
        return self._typename

    @typename.setter
    def typename(self, typename):
        r"""Sets the typename of this Flavor.

        **参数解释**： 节点类型名称。 **取值范围**： 不涉及

        :param typename: The typename of this Flavor.
        :type typename: str
        """
        self._typename = typename

    @property
    def diskrange(self):
        r"""Gets the diskrange of this Flavor.

        **参数解释**： 实例的硬盘容量范围，单位GB。 **取值范围**： 不涉及

        :return: The diskrange of this Flavor.
        :rtype: str
        """
        return self._diskrange

    @diskrange.setter
    def diskrange(self, diskrange):
        r"""Sets the diskrange of this Flavor.

        **参数解释**： 实例的硬盘容量范围，单位GB。 **取值范围**： 不涉及

        :param diskrange: The diskrange of this Flavor.
        :type diskrange: str
        """
        self._diskrange = diskrange

    @property
    def cond_operation_status(self):
        r"""Gets the cond_operation_status of this Flavor.

        **参数解释**： 此参数是Region级配置，某个AZ没有在condOperationAz参数中配置时默认使用此参数的取值。 **取值范围**：   - normal：正常商用。   - sellout：售罄。

        :return: The cond_operation_status of this Flavor.
        :rtype: str
        """
        return self._cond_operation_status

    @cond_operation_status.setter
    def cond_operation_status(self, cond_operation_status):
        r"""Sets the cond_operation_status of this Flavor.

        **参数解释**： 此参数是Region级配置，某个AZ没有在condOperationAz参数中配置时默认使用此参数的取值。 **取值范围**：   - normal：正常商用。   - sellout：售罄。

        :param cond_operation_status: The cond_operation_status of this Flavor.
        :type cond_operation_status: str
        """
        self._cond_operation_status = cond_operation_status

    @property
    def cond_operation_az(self):
        r"""Gets the cond_operation_az of this Flavor.

        **参数解释**： 此参数是AZ级配置，某个AZ没有在此参数中配置时默认使用condOperationAz参数的取值。此参数的配置格式“az(xx)”。()内为某个AZ的flavor状态，()内必须要填有状态，不填为无效配置。状态的取值范围与condOperationStatus参数相同。 **取值范围**： 不涉及

        :return: The cond_operation_az of this Flavor.
        :rtype: str
        """
        return self._cond_operation_az

    @cond_operation_az.setter
    def cond_operation_az(self, cond_operation_az):
        r"""Sets the cond_operation_az of this Flavor.

        **参数解释**： 此参数是AZ级配置，某个AZ没有在此参数中配置时默认使用condOperationAz参数的取值。此参数的配置格式“az(xx)”。()内为某个AZ的flavor状态，()内必须要填有状态，不填为无效配置。状态的取值范围与condOperationStatus参数相同。 **取值范围**： 不涉及

        :param cond_operation_az: The cond_operation_az of this Flavor.
        :type cond_operation_az: str
        """
        self._cond_operation_az = cond_operation_az

    @property
    def localdisk(self):
        r"""Gets the localdisk of this Flavor.

        **参数解释**： 是否本地盘。 **取值范围**： - true：本地盘。 - false：非本地盘。

        :return: The localdisk of this Flavor.
        :rtype: str
        """
        return self._localdisk

    @localdisk.setter
    def localdisk(self, localdisk):
        r"""Sets the localdisk of this Flavor.

        **参数解释**： 是否本地盘。 **取值范围**： - true：本地盘。 - false：非本地盘。

        :param localdisk: The localdisk of this Flavor.
        :type localdisk: str
        """
        self._localdisk = localdisk

    @property
    def flavor_type_cn(self):
        r"""Gets the flavor_type_cn of this Flavor.

        **参数解释**： 中文规格分类。 **取值范围**： 不涉及

        :return: The flavor_type_cn of this Flavor.
        :rtype: str
        """
        return self._flavor_type_cn

    @flavor_type_cn.setter
    def flavor_type_cn(self, flavor_type_cn):
        r"""Sets the flavor_type_cn of this Flavor.

        **参数解释**： 中文规格分类。 **取值范围**： 不涉及

        :param flavor_type_cn: The flavor_type_cn of this Flavor.
        :type flavor_type_cn: str
        """
        self._flavor_type_cn = flavor_type_cn

    @property
    def flavor_type_en(self):
        r"""Gets the flavor_type_en of this Flavor.

        **参数解释**： 英文规格分类。 **取值范围**： 不涉及

        :return: The flavor_type_en of this Flavor.
        :rtype: str
        """
        return self._flavor_type_en

    @flavor_type_en.setter
    def flavor_type_en(self, flavor_type_en):
        r"""Sets the flavor_type_en of this Flavor.

        **参数解释**： 英文规格分类。 **取值范围**： 不涉及

        :param flavor_type_en: The flavor_type_en of this Flavor.
        :type flavor_type_en: str
        """
        self._flavor_type_en = flavor_type_en

    @property
    def edge(self):
        r"""Gets the edge of this Flavor.

        **参数解释**： 是否边缘区规格。 **取值范围**： - true：边缘区专属规格。 - false：通用规格。

        :return: The edge of this Flavor.
        :rtype: bool
        """
        return self._edge

    @edge.setter
    def edge(self, edge):
        r"""Sets the edge of this Flavor.

        **参数解释**： 是否边缘区规格。 **取值范围**： - true：边缘区专属规格。 - false：通用规格。

        :param edge: The edge of this Flavor.
        :type edge: bool
        """
        self._edge = edge

    @property
    def str_id(self):
        r"""Gets the str_id of this Flavor.

        **参数解释**： 规格id。 **取值范围**： 不涉及

        :return: The str_id of this Flavor.
        :rtype: str
        """
        return self._str_id

    @str_id.setter
    def str_id(self, str_id):
        r"""Sets the str_id of this Flavor.

        **参数解释**： 规格id。 **取值范围**： 不涉及

        :param str_id: The str_id of this Flavor.
        :type str_id: str
        """
        self._str_id = str_id

    @property
    def is_allow_https(self):
        r"""Gets the is_allow_https of this Flavor.

        **参数解释**： 节点类型是否支持HTTPS协议访问。 **取值范围**： 不涉及

        :return: The is_allow_https of this Flavor.
        :rtype: bool
        """
        return self._is_allow_https

    @is_allow_https.setter
    def is_allow_https(self, is_allow_https):
        r"""Sets the is_allow_https of this Flavor.

        **参数解释**： 节点类型是否支持HTTPS协议访问。 **取值范围**： 不涉及

        :param is_allow_https: The is_allow_https of this Flavor.
        :type is_allow_https: bool
        """
        self._is_allow_https = is_allow_https

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
        if not isinstance(other, Flavor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
