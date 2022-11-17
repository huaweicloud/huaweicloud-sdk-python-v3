# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OsExtraSpecs:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_type': 'str',
        'capabilitiescpu_arch': 'str',
        'baremetaldisk_detail': 'str',
        'capabilitieshypervisor_type': 'str',
        'baremetal__support_evs': 'str',
        'baremetalext_boot_type': 'str',
        'capabilitiesboard_type': 'str',
        'baremetalnet_num': 'str',
        'baremetalnetcard_detail': 'str',
        'baremetalcpu_detail': 'str',
        'baremetalmemory_detail': 'str',
        'condoperationstatus': 'str',
        'condoperationaz': 'str'
    }

    attribute_map = {
        'resource_type': 'resource_type',
        'capabilitiescpu_arch': 'capabilities:cpu_arch',
        'baremetaldisk_detail': 'baremetal:disk_detail',
        'capabilitieshypervisor_type': 'capabilities:hypervisor_type',
        'baremetal__support_evs': 'baremetal:__support_evs',
        'baremetalext_boot_type': 'baremetal:extBootType',
        'capabilitiesboard_type': 'capabilities:board_type',
        'baremetalnet_num': 'baremetal:net_num',
        'baremetalnetcard_detail': 'baremetal:netcard_detail',
        'baremetalcpu_detail': 'baremetal:cpu_detail',
        'baremetalmemory_detail': 'baremetal:memory_detail',
        'condoperationstatus': 'cond:operation:status',
        'condoperationaz': 'cond:operation:az'
    }

    def __init__(self, resource_type=None, capabilitiescpu_arch=None, baremetaldisk_detail=None, capabilitieshypervisor_type=None, baremetal__support_evs=None, baremetalext_boot_type=None, capabilitiesboard_type=None, baremetalnet_num=None, baremetalnetcard_detail=None, baremetalcpu_detail=None, baremetalmemory_detail=None, condoperationstatus=None, condoperationaz=None):
        """OsExtraSpecs

        The model defined in huaweicloud sdk

        :param resource_type: 识该规格对应的资源类型，取值范围为“ironic”。
        :type resource_type: str
        :param capabilitiescpu_arch: 裸金属服务器的CPU架构类型，取值为：x86_64（适用于x86机型）aarch64（适用于ARM机型）
        :type capabilitiescpu_arch: str
        :param baremetaldisk_detail: 磁盘物理规格描述信息。
        :type baremetaldisk_detail: str
        :param capabilitieshypervisor_type: 标示ironic类型的规格。
        :type capabilitieshypervisor_type: str
        :param baremetal__support_evs: 标识当前的规格是否支持挂载EVS卷。truefalse
        :type baremetal__support_evs: str
        :param baremetalext_boot_type: 裸金属服务器启动源。LocalDisk：本地盘Volume：云硬盘（快速发放）
        :type baremetalext_boot_type: str
        :param capabilitiesboard_type: 裸金属服务器的规格类型。格式为规格的缩写，例如规格名称为“physical.o2.medium”，则规格类型为“o2m”。
        :type capabilitiesboard_type: str
        :param baremetalnet_num: 实际可挂载网络数量。
        :type baremetalnet_num: str
        :param baremetalnetcard_detail: 网卡物理规格描述信息。
        :type baremetalnetcard_detail: str
        :param baremetalcpu_detail: CPU物理规格描述信息。
        :type baremetalcpu_detail: str
        :param baremetalmemory_detail: 内存物理规格描述信息
        :type baremetalmemory_detail: str
        :param condoperationstatus: 裸金属服务器规格状态。不配置时等同于normal。normal：正常商用abandon：下线（即不显示）sellout：售罄obt：公测promotion：推荐（等同normal，也是商用）
        :type condoperationstatus: str
        :param condoperationaz: 在某个AZ的裸金属服务器规格状态。此参数是AZ级配置，某个AZ没有在此参数中配置时默认使用cond:operation:status参数的取值。格式：az(xx)。()内为某个AZ下的裸金属服务器规格状态，()内必须填写状态，不填为无效配置。例如：规格在某个区域的az0正常商用，az1售罄，az2公测，az3正常商用，其他az显示下线，可配置为：“cond:operation:status”设置为“abandon”“cond:operation:az”设置为“az0(normal), az1(sellout), az2(obt), az3(promotion)” 说明：如果规格在某个AZ下的状态与cond:operation:status配置状态不同，必须配置该参数。
        :type condoperationaz: str
        """
        
        

        self._resource_type = None
        self._capabilitiescpu_arch = None
        self._baremetaldisk_detail = None
        self._capabilitieshypervisor_type = None
        self._baremetal__support_evs = None
        self._baremetalext_boot_type = None
        self._capabilitiesboard_type = None
        self._baremetalnet_num = None
        self._baremetalnetcard_detail = None
        self._baremetalcpu_detail = None
        self._baremetalmemory_detail = None
        self._condoperationstatus = None
        self._condoperationaz = None
        self.discriminator = None

        self.resource_type = resource_type
        self.capabilitiescpu_arch = capabilitiescpu_arch
        self.baremetaldisk_detail = baremetaldisk_detail
        self.capabilitieshypervisor_type = capabilitieshypervisor_type
        if baremetal__support_evs is not None:
            self.baremetal__support_evs = baremetal__support_evs
        if baremetalext_boot_type is not None:
            self.baremetalext_boot_type = baremetalext_boot_type
        self.capabilitiesboard_type = capabilitiesboard_type
        self.baremetalnet_num = baremetalnet_num
        self.baremetalnetcard_detail = baremetalnetcard_detail
        self.baremetalcpu_detail = baremetalcpu_detail
        self.baremetalmemory_detail = baremetalmemory_detail
        if condoperationstatus is not None:
            self.condoperationstatus = condoperationstatus
        if condoperationaz is not None:
            self.condoperationaz = condoperationaz

    @property
    def resource_type(self):
        """Gets the resource_type of this OsExtraSpecs.

        识该规格对应的资源类型，取值范围为“ironic”。

        :return: The resource_type of this OsExtraSpecs.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this OsExtraSpecs.

        识该规格对应的资源类型，取值范围为“ironic”。

        :param resource_type: The resource_type of this OsExtraSpecs.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def capabilitiescpu_arch(self):
        """Gets the capabilitiescpu_arch of this OsExtraSpecs.

        裸金属服务器的CPU架构类型，取值为：x86_64（适用于x86机型）aarch64（适用于ARM机型）

        :return: The capabilitiescpu_arch of this OsExtraSpecs.
        :rtype: str
        """
        return self._capabilitiescpu_arch

    @capabilitiescpu_arch.setter
    def capabilitiescpu_arch(self, capabilitiescpu_arch):
        """Sets the capabilitiescpu_arch of this OsExtraSpecs.

        裸金属服务器的CPU架构类型，取值为：x86_64（适用于x86机型）aarch64（适用于ARM机型）

        :param capabilitiescpu_arch: The capabilitiescpu_arch of this OsExtraSpecs.
        :type capabilitiescpu_arch: str
        """
        self._capabilitiescpu_arch = capabilitiescpu_arch

    @property
    def baremetaldisk_detail(self):
        """Gets the baremetaldisk_detail of this OsExtraSpecs.

        磁盘物理规格描述信息。

        :return: The baremetaldisk_detail of this OsExtraSpecs.
        :rtype: str
        """
        return self._baremetaldisk_detail

    @baremetaldisk_detail.setter
    def baremetaldisk_detail(self, baremetaldisk_detail):
        """Sets the baremetaldisk_detail of this OsExtraSpecs.

        磁盘物理规格描述信息。

        :param baremetaldisk_detail: The baremetaldisk_detail of this OsExtraSpecs.
        :type baremetaldisk_detail: str
        """
        self._baremetaldisk_detail = baremetaldisk_detail

    @property
    def capabilitieshypervisor_type(self):
        """Gets the capabilitieshypervisor_type of this OsExtraSpecs.

        标示ironic类型的规格。

        :return: The capabilitieshypervisor_type of this OsExtraSpecs.
        :rtype: str
        """
        return self._capabilitieshypervisor_type

    @capabilitieshypervisor_type.setter
    def capabilitieshypervisor_type(self, capabilitieshypervisor_type):
        """Sets the capabilitieshypervisor_type of this OsExtraSpecs.

        标示ironic类型的规格。

        :param capabilitieshypervisor_type: The capabilitieshypervisor_type of this OsExtraSpecs.
        :type capabilitieshypervisor_type: str
        """
        self._capabilitieshypervisor_type = capabilitieshypervisor_type

    @property
    def baremetal__support_evs(self):
        """Gets the baremetal__support_evs of this OsExtraSpecs.

        标识当前的规格是否支持挂载EVS卷。truefalse

        :return: The baremetal__support_evs of this OsExtraSpecs.
        :rtype: str
        """
        return self._baremetal__support_evs

    @baremetal__support_evs.setter
    def baremetal__support_evs(self, baremetal__support_evs):
        """Sets the baremetal__support_evs of this OsExtraSpecs.

        标识当前的规格是否支持挂载EVS卷。truefalse

        :param baremetal__support_evs: The baremetal__support_evs of this OsExtraSpecs.
        :type baremetal__support_evs: str
        """
        self._baremetal__support_evs = baremetal__support_evs

    @property
    def baremetalext_boot_type(self):
        """Gets the baremetalext_boot_type of this OsExtraSpecs.

        裸金属服务器启动源。LocalDisk：本地盘Volume：云硬盘（快速发放）

        :return: The baremetalext_boot_type of this OsExtraSpecs.
        :rtype: str
        """
        return self._baremetalext_boot_type

    @baremetalext_boot_type.setter
    def baremetalext_boot_type(self, baremetalext_boot_type):
        """Sets the baremetalext_boot_type of this OsExtraSpecs.

        裸金属服务器启动源。LocalDisk：本地盘Volume：云硬盘（快速发放）

        :param baremetalext_boot_type: The baremetalext_boot_type of this OsExtraSpecs.
        :type baremetalext_boot_type: str
        """
        self._baremetalext_boot_type = baremetalext_boot_type

    @property
    def capabilitiesboard_type(self):
        """Gets the capabilitiesboard_type of this OsExtraSpecs.

        裸金属服务器的规格类型。格式为规格的缩写，例如规格名称为“physical.o2.medium”，则规格类型为“o2m”。

        :return: The capabilitiesboard_type of this OsExtraSpecs.
        :rtype: str
        """
        return self._capabilitiesboard_type

    @capabilitiesboard_type.setter
    def capabilitiesboard_type(self, capabilitiesboard_type):
        """Sets the capabilitiesboard_type of this OsExtraSpecs.

        裸金属服务器的规格类型。格式为规格的缩写，例如规格名称为“physical.o2.medium”，则规格类型为“o2m”。

        :param capabilitiesboard_type: The capabilitiesboard_type of this OsExtraSpecs.
        :type capabilitiesboard_type: str
        """
        self._capabilitiesboard_type = capabilitiesboard_type

    @property
    def baremetalnet_num(self):
        """Gets the baremetalnet_num of this OsExtraSpecs.

        实际可挂载网络数量。

        :return: The baremetalnet_num of this OsExtraSpecs.
        :rtype: str
        """
        return self._baremetalnet_num

    @baremetalnet_num.setter
    def baremetalnet_num(self, baremetalnet_num):
        """Sets the baremetalnet_num of this OsExtraSpecs.

        实际可挂载网络数量。

        :param baremetalnet_num: The baremetalnet_num of this OsExtraSpecs.
        :type baremetalnet_num: str
        """
        self._baremetalnet_num = baremetalnet_num

    @property
    def baremetalnetcard_detail(self):
        """Gets the baremetalnetcard_detail of this OsExtraSpecs.

        网卡物理规格描述信息。

        :return: The baremetalnetcard_detail of this OsExtraSpecs.
        :rtype: str
        """
        return self._baremetalnetcard_detail

    @baremetalnetcard_detail.setter
    def baremetalnetcard_detail(self, baremetalnetcard_detail):
        """Sets the baremetalnetcard_detail of this OsExtraSpecs.

        网卡物理规格描述信息。

        :param baremetalnetcard_detail: The baremetalnetcard_detail of this OsExtraSpecs.
        :type baremetalnetcard_detail: str
        """
        self._baremetalnetcard_detail = baremetalnetcard_detail

    @property
    def baremetalcpu_detail(self):
        """Gets the baremetalcpu_detail of this OsExtraSpecs.

        CPU物理规格描述信息。

        :return: The baremetalcpu_detail of this OsExtraSpecs.
        :rtype: str
        """
        return self._baremetalcpu_detail

    @baremetalcpu_detail.setter
    def baremetalcpu_detail(self, baremetalcpu_detail):
        """Sets the baremetalcpu_detail of this OsExtraSpecs.

        CPU物理规格描述信息。

        :param baremetalcpu_detail: The baremetalcpu_detail of this OsExtraSpecs.
        :type baremetalcpu_detail: str
        """
        self._baremetalcpu_detail = baremetalcpu_detail

    @property
    def baremetalmemory_detail(self):
        """Gets the baremetalmemory_detail of this OsExtraSpecs.

        内存物理规格描述信息

        :return: The baremetalmemory_detail of this OsExtraSpecs.
        :rtype: str
        """
        return self._baremetalmemory_detail

    @baremetalmemory_detail.setter
    def baremetalmemory_detail(self, baremetalmemory_detail):
        """Sets the baremetalmemory_detail of this OsExtraSpecs.

        内存物理规格描述信息

        :param baremetalmemory_detail: The baremetalmemory_detail of this OsExtraSpecs.
        :type baremetalmemory_detail: str
        """
        self._baremetalmemory_detail = baremetalmemory_detail

    @property
    def condoperationstatus(self):
        """Gets the condoperationstatus of this OsExtraSpecs.

        裸金属服务器规格状态。不配置时等同于normal。normal：正常商用abandon：下线（即不显示）sellout：售罄obt：公测promotion：推荐（等同normal，也是商用）

        :return: The condoperationstatus of this OsExtraSpecs.
        :rtype: str
        """
        return self._condoperationstatus

    @condoperationstatus.setter
    def condoperationstatus(self, condoperationstatus):
        """Sets the condoperationstatus of this OsExtraSpecs.

        裸金属服务器规格状态。不配置时等同于normal。normal：正常商用abandon：下线（即不显示）sellout：售罄obt：公测promotion：推荐（等同normal，也是商用）

        :param condoperationstatus: The condoperationstatus of this OsExtraSpecs.
        :type condoperationstatus: str
        """
        self._condoperationstatus = condoperationstatus

    @property
    def condoperationaz(self):
        """Gets the condoperationaz of this OsExtraSpecs.

        在某个AZ的裸金属服务器规格状态。此参数是AZ级配置，某个AZ没有在此参数中配置时默认使用cond:operation:status参数的取值。格式：az(xx)。()内为某个AZ下的裸金属服务器规格状态，()内必须填写状态，不填为无效配置。例如：规格在某个区域的az0正常商用，az1售罄，az2公测，az3正常商用，其他az显示下线，可配置为：“cond:operation:status”设置为“abandon”“cond:operation:az”设置为“az0(normal), az1(sellout), az2(obt), az3(promotion)” 说明：如果规格在某个AZ下的状态与cond:operation:status配置状态不同，必须配置该参数。

        :return: The condoperationaz of this OsExtraSpecs.
        :rtype: str
        """
        return self._condoperationaz

    @condoperationaz.setter
    def condoperationaz(self, condoperationaz):
        """Sets the condoperationaz of this OsExtraSpecs.

        在某个AZ的裸金属服务器规格状态。此参数是AZ级配置，某个AZ没有在此参数中配置时默认使用cond:operation:status参数的取值。格式：az(xx)。()内为某个AZ下的裸金属服务器规格状态，()内必须填写状态，不填为无效配置。例如：规格在某个区域的az0正常商用，az1售罄，az2公测，az3正常商用，其他az显示下线，可配置为：“cond:operation:status”设置为“abandon”“cond:operation:az”设置为“az0(normal), az1(sellout), az2(obt), az3(promotion)” 说明：如果规格在某个AZ下的状态与cond:operation:status配置状态不同，必须配置该参数。

        :param condoperationaz: The condoperationaz of this OsExtraSpecs.
        :type condoperationaz: str
        """
        self._condoperationaz = condoperationaz

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
        if not isinstance(other, OsExtraSpecs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
