# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProductInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'product_id': 'str',
        'flavor_id': 'str',
        'type': 'str',
        'architecture': 'str',
        'cpu': 'str',
        'cpu_desc': 'str',
        'memory': 'str',
        'is_gpu': 'bool',
        'system_disk_type': 'str',
        'system_disk_size': 'str',
        'gpu_desc': 'str',
        'descriptions': 'str',
        'charge_mode': 'str',
        'contain_data_disk': 'bool',
        'resource_type': 'str',
        'cloud_service_type': 'str',
        'volume_product_type': 'str',
        'sessions': 'int',
        'status': 'str',
        'cond_operation_az': 'str',
        'sub_product_list': 'list[str]',
        'domain_ids': 'list[str]',
        'package_type': 'str',
        'expire_time': 'datetime',
        'support_gpu_type': 'str'
    }

    attribute_map = {
        'product_id': 'product_id',
        'flavor_id': 'flavor_id',
        'type': 'type',
        'architecture': 'architecture',
        'cpu': 'cpu',
        'cpu_desc': 'cpu_desc',
        'memory': 'memory',
        'is_gpu': 'is_gpu',
        'system_disk_type': 'system_disk_type',
        'system_disk_size': 'system_disk_size',
        'gpu_desc': 'gpu_desc',
        'descriptions': 'descriptions',
        'charge_mode': 'charge_mode',
        'contain_data_disk': 'contain_data_disk',
        'resource_type': 'resource_type',
        'cloud_service_type': 'cloud_service_type',
        'volume_product_type': 'volume_product_type',
        'sessions': 'sessions',
        'status': 'status',
        'cond_operation_az': 'cond_operation_az',
        'sub_product_list': 'sub_product_list',
        'domain_ids': 'domain_ids',
        'package_type': 'package_type',
        'expire_time': 'expire_time',
        'support_gpu_type': 'support_gpu_type'
    }

    def __init__(self, product_id=None, flavor_id=None, type=None, architecture=None, cpu=None, cpu_desc=None, memory=None, is_gpu=None, system_disk_type=None, system_disk_size=None, gpu_desc=None, descriptions=None, charge_mode=None, contain_data_disk=None, resource_type=None, cloud_service_type=None, volume_product_type=None, sessions=None, status=None, cond_operation_az=None, sub_product_list=None, domain_ids=None, package_type=None, expire_time=None, support_gpu_type=None):
        """ProductInfo

        The model defined in huaweicloud sdk

        :param product_id: 产品id
        :type product_id: str
        :param flavor_id: 规格ID
        :type flavor_id: str
        :param type: 产品类型。 - BASE：表示产品基础套餐，套餐镜像中不包括除操作系统之外的其他商业软件，私有镜像场景只能使用此类套餐。 - ADVANCED：表示产品高级套餐，套餐镜像中包括了一些商业软件。
        :type type: str
        :param architecture: 产品架构，当前仅支持x86 - x86 - arm
        :type architecture: str
        :param cpu: CPU
        :type cpu: str
        :param cpu_desc: CPU描述
        :type cpu_desc: str
        :param memory: 内存大小，单位兆：MB
        :type memory: str
        :param is_gpu: 是否是GPU类型的规格
        :type is_gpu: bool
        :param system_disk_type: 系统盘类型
        :type system_disk_type: str
        :param system_disk_size: 系统盘大小
        :type system_disk_size: str
        :param gpu_desc: GPU描述
        :type gpu_desc: str
        :param descriptions: 产品描述
        :type descriptions: str
        :param charge_mode: 套餐标识。 - 1：表示包周期。 - 0：表示按需。
        :type charge_mode: str
        :param contain_data_disk: 套餐计费是否包含了数据盘
        :type contain_data_disk: bool
        :param resource_type: 资源类型
        :type resource_type: str
        :param cloud_service_type: 云服务类型
        :type cloud_service_type: str
        :param volume_product_type: 磁盘产品类型
        :type volume_product_type: str
        :param sessions: 套餐默认支持的最大会话数
        :type sessions: int
        :param status: 产品套餐在销售模式下的状态，取值自ECS的cond:operation:status。 不配置时等同于normal在售状态。 * &#x60;normal&#x60; - 正常商用 * &#x60;abandon&#x60; - 下线（即不显示） * &#x60;sellout&#x60; - 售罄 * &#x60;obt&#x60; - 公测 * &#x60;obt_sellout&#x60; - 公测售罄 * &#x60;promotion&#x60; - 推荐(等同normal，也是商用)
        :type status: str
        :param cond_operation_az: 产品套餐在可用区的状态，配套status使用。 &gt; - 此参数是AZ级配置，优选取此参数的值，某个AZ没有在此参数中配置时默认使用status参数的取值。 &gt; - 配置格式“az(xx)”。()内为某个AZ的flavor状态，()内必须要填有状态，不填为无效配置。 &gt; - 例如：套餐在某个region的az0正常商用，az1售罄，az2公测，az3正常商用，其他az显示下线，可配置为： &gt;   - “status”设置为：“abandon”  &gt;   - “cond_operation_az”设置为：“az0(normal), az1(sellout), az2(obt), az3(normal)”  &gt; -  说明：如果flavor在某个AZ下的状态与status配置状态不同，必须配置该参数。
        :type cond_operation_az: str
        :param sub_product_list: 专属主机的子产品
        :type sub_product_list: list[str]
        :param domain_ids: 产品属于专有的domainId
        :type domain_ids: list[str]
        :param package_type: 套餐类型。 - general：表示产品通用套餐。 - dedicated：表示产品专属主机套餐。
        :type package_type: str
        :param expire_time: 产品套餐过期时间,产品将在改时间点后逐步下架
        :type expire_time: datetime
        :param support_gpu_type: 产品套餐支持的GPU类型
        :type support_gpu_type: str
        """
        
        

        self._product_id = None
        self._flavor_id = None
        self._type = None
        self._architecture = None
        self._cpu = None
        self._cpu_desc = None
        self._memory = None
        self._is_gpu = None
        self._system_disk_type = None
        self._system_disk_size = None
        self._gpu_desc = None
        self._descriptions = None
        self._charge_mode = None
        self._contain_data_disk = None
        self._resource_type = None
        self._cloud_service_type = None
        self._volume_product_type = None
        self._sessions = None
        self._status = None
        self._cond_operation_az = None
        self._sub_product_list = None
        self._domain_ids = None
        self._package_type = None
        self._expire_time = None
        self._support_gpu_type = None
        self.discriminator = None

        if product_id is not None:
            self.product_id = product_id
        if flavor_id is not None:
            self.flavor_id = flavor_id
        if type is not None:
            self.type = type
        if architecture is not None:
            self.architecture = architecture
        if cpu is not None:
            self.cpu = cpu
        if cpu_desc is not None:
            self.cpu_desc = cpu_desc
        if memory is not None:
            self.memory = memory
        if is_gpu is not None:
            self.is_gpu = is_gpu
        if system_disk_type is not None:
            self.system_disk_type = system_disk_type
        if system_disk_size is not None:
            self.system_disk_size = system_disk_size
        if gpu_desc is not None:
            self.gpu_desc = gpu_desc
        if descriptions is not None:
            self.descriptions = descriptions
        if charge_mode is not None:
            self.charge_mode = charge_mode
        if contain_data_disk is not None:
            self.contain_data_disk = contain_data_disk
        if resource_type is not None:
            self.resource_type = resource_type
        if cloud_service_type is not None:
            self.cloud_service_type = cloud_service_type
        if volume_product_type is not None:
            self.volume_product_type = volume_product_type
        if sessions is not None:
            self.sessions = sessions
        if status is not None:
            self.status = status
        if cond_operation_az is not None:
            self.cond_operation_az = cond_operation_az
        if sub_product_list is not None:
            self.sub_product_list = sub_product_list
        if domain_ids is not None:
            self.domain_ids = domain_ids
        if package_type is not None:
            self.package_type = package_type
        if expire_time is not None:
            self.expire_time = expire_time
        if support_gpu_type is not None:
            self.support_gpu_type = support_gpu_type

    @property
    def product_id(self):
        """Gets the product_id of this ProductInfo.

        产品id

        :return: The product_id of this ProductInfo.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this ProductInfo.

        产品id

        :param product_id: The product_id of this ProductInfo.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def flavor_id(self):
        """Gets the flavor_id of this ProductInfo.

        规格ID

        :return: The flavor_id of this ProductInfo.
        :rtype: str
        """
        return self._flavor_id

    @flavor_id.setter
    def flavor_id(self, flavor_id):
        """Sets the flavor_id of this ProductInfo.

        规格ID

        :param flavor_id: The flavor_id of this ProductInfo.
        :type flavor_id: str
        """
        self._flavor_id = flavor_id

    @property
    def type(self):
        """Gets the type of this ProductInfo.

        产品类型。 - BASE：表示产品基础套餐，套餐镜像中不包括除操作系统之外的其他商业软件，私有镜像场景只能使用此类套餐。 - ADVANCED：表示产品高级套餐，套餐镜像中包括了一些商业软件。

        :return: The type of this ProductInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ProductInfo.

        产品类型。 - BASE：表示产品基础套餐，套餐镜像中不包括除操作系统之外的其他商业软件，私有镜像场景只能使用此类套餐。 - ADVANCED：表示产品高级套餐，套餐镜像中包括了一些商业软件。

        :param type: The type of this ProductInfo.
        :type type: str
        """
        self._type = type

    @property
    def architecture(self):
        """Gets the architecture of this ProductInfo.

        产品架构，当前仅支持x86 - x86 - arm

        :return: The architecture of this ProductInfo.
        :rtype: str
        """
        return self._architecture

    @architecture.setter
    def architecture(self, architecture):
        """Sets the architecture of this ProductInfo.

        产品架构，当前仅支持x86 - x86 - arm

        :param architecture: The architecture of this ProductInfo.
        :type architecture: str
        """
        self._architecture = architecture

    @property
    def cpu(self):
        """Gets the cpu of this ProductInfo.

        CPU

        :return: The cpu of this ProductInfo.
        :rtype: str
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        """Sets the cpu of this ProductInfo.

        CPU

        :param cpu: The cpu of this ProductInfo.
        :type cpu: str
        """
        self._cpu = cpu

    @property
    def cpu_desc(self):
        """Gets the cpu_desc of this ProductInfo.

        CPU描述

        :return: The cpu_desc of this ProductInfo.
        :rtype: str
        """
        return self._cpu_desc

    @cpu_desc.setter
    def cpu_desc(self, cpu_desc):
        """Sets the cpu_desc of this ProductInfo.

        CPU描述

        :param cpu_desc: The cpu_desc of this ProductInfo.
        :type cpu_desc: str
        """
        self._cpu_desc = cpu_desc

    @property
    def memory(self):
        """Gets the memory of this ProductInfo.

        内存大小，单位兆：MB

        :return: The memory of this ProductInfo.
        :rtype: str
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        """Sets the memory of this ProductInfo.

        内存大小，单位兆：MB

        :param memory: The memory of this ProductInfo.
        :type memory: str
        """
        self._memory = memory

    @property
    def is_gpu(self):
        """Gets the is_gpu of this ProductInfo.

        是否是GPU类型的规格

        :return: The is_gpu of this ProductInfo.
        :rtype: bool
        """
        return self._is_gpu

    @is_gpu.setter
    def is_gpu(self, is_gpu):
        """Sets the is_gpu of this ProductInfo.

        是否是GPU类型的规格

        :param is_gpu: The is_gpu of this ProductInfo.
        :type is_gpu: bool
        """
        self._is_gpu = is_gpu

    @property
    def system_disk_type(self):
        """Gets the system_disk_type of this ProductInfo.

        系统盘类型

        :return: The system_disk_type of this ProductInfo.
        :rtype: str
        """
        return self._system_disk_type

    @system_disk_type.setter
    def system_disk_type(self, system_disk_type):
        """Sets the system_disk_type of this ProductInfo.

        系统盘类型

        :param system_disk_type: The system_disk_type of this ProductInfo.
        :type system_disk_type: str
        """
        self._system_disk_type = system_disk_type

    @property
    def system_disk_size(self):
        """Gets the system_disk_size of this ProductInfo.

        系统盘大小

        :return: The system_disk_size of this ProductInfo.
        :rtype: str
        """
        return self._system_disk_size

    @system_disk_size.setter
    def system_disk_size(self, system_disk_size):
        """Sets the system_disk_size of this ProductInfo.

        系统盘大小

        :param system_disk_size: The system_disk_size of this ProductInfo.
        :type system_disk_size: str
        """
        self._system_disk_size = system_disk_size

    @property
    def gpu_desc(self):
        """Gets the gpu_desc of this ProductInfo.

        GPU描述

        :return: The gpu_desc of this ProductInfo.
        :rtype: str
        """
        return self._gpu_desc

    @gpu_desc.setter
    def gpu_desc(self, gpu_desc):
        """Sets the gpu_desc of this ProductInfo.

        GPU描述

        :param gpu_desc: The gpu_desc of this ProductInfo.
        :type gpu_desc: str
        """
        self._gpu_desc = gpu_desc

    @property
    def descriptions(self):
        """Gets the descriptions of this ProductInfo.

        产品描述

        :return: The descriptions of this ProductInfo.
        :rtype: str
        """
        return self._descriptions

    @descriptions.setter
    def descriptions(self, descriptions):
        """Sets the descriptions of this ProductInfo.

        产品描述

        :param descriptions: The descriptions of this ProductInfo.
        :type descriptions: str
        """
        self._descriptions = descriptions

    @property
    def charge_mode(self):
        """Gets the charge_mode of this ProductInfo.

        套餐标识。 - 1：表示包周期。 - 0：表示按需。

        :return: The charge_mode of this ProductInfo.
        :rtype: str
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        """Sets the charge_mode of this ProductInfo.

        套餐标识。 - 1：表示包周期。 - 0：表示按需。

        :param charge_mode: The charge_mode of this ProductInfo.
        :type charge_mode: str
        """
        self._charge_mode = charge_mode

    @property
    def contain_data_disk(self):
        """Gets the contain_data_disk of this ProductInfo.

        套餐计费是否包含了数据盘

        :return: The contain_data_disk of this ProductInfo.
        :rtype: bool
        """
        return self._contain_data_disk

    @contain_data_disk.setter
    def contain_data_disk(self, contain_data_disk):
        """Sets the contain_data_disk of this ProductInfo.

        套餐计费是否包含了数据盘

        :param contain_data_disk: The contain_data_disk of this ProductInfo.
        :type contain_data_disk: bool
        """
        self._contain_data_disk = contain_data_disk

    @property
    def resource_type(self):
        """Gets the resource_type of this ProductInfo.

        资源类型

        :return: The resource_type of this ProductInfo.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this ProductInfo.

        资源类型

        :param resource_type: The resource_type of this ProductInfo.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def cloud_service_type(self):
        """Gets the cloud_service_type of this ProductInfo.

        云服务类型

        :return: The cloud_service_type of this ProductInfo.
        :rtype: str
        """
        return self._cloud_service_type

    @cloud_service_type.setter
    def cloud_service_type(self, cloud_service_type):
        """Sets the cloud_service_type of this ProductInfo.

        云服务类型

        :param cloud_service_type: The cloud_service_type of this ProductInfo.
        :type cloud_service_type: str
        """
        self._cloud_service_type = cloud_service_type

    @property
    def volume_product_type(self):
        """Gets the volume_product_type of this ProductInfo.

        磁盘产品类型

        :return: The volume_product_type of this ProductInfo.
        :rtype: str
        """
        return self._volume_product_type

    @volume_product_type.setter
    def volume_product_type(self, volume_product_type):
        """Sets the volume_product_type of this ProductInfo.

        磁盘产品类型

        :param volume_product_type: The volume_product_type of this ProductInfo.
        :type volume_product_type: str
        """
        self._volume_product_type = volume_product_type

    @property
    def sessions(self):
        """Gets the sessions of this ProductInfo.

        套餐默认支持的最大会话数

        :return: The sessions of this ProductInfo.
        :rtype: int
        """
        return self._sessions

    @sessions.setter
    def sessions(self, sessions):
        """Sets the sessions of this ProductInfo.

        套餐默认支持的最大会话数

        :param sessions: The sessions of this ProductInfo.
        :type sessions: int
        """
        self._sessions = sessions

    @property
    def status(self):
        """Gets the status of this ProductInfo.

        产品套餐在销售模式下的状态，取值自ECS的cond:operation:status。 不配置时等同于normal在售状态。 * `normal` - 正常商用 * `abandon` - 下线（即不显示） * `sellout` - 售罄 * `obt` - 公测 * `obt_sellout` - 公测售罄 * `promotion` - 推荐(等同normal，也是商用)

        :return: The status of this ProductInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ProductInfo.

        产品套餐在销售模式下的状态，取值自ECS的cond:operation:status。 不配置时等同于normal在售状态。 * `normal` - 正常商用 * `abandon` - 下线（即不显示） * `sellout` - 售罄 * `obt` - 公测 * `obt_sellout` - 公测售罄 * `promotion` - 推荐(等同normal，也是商用)

        :param status: The status of this ProductInfo.
        :type status: str
        """
        self._status = status

    @property
    def cond_operation_az(self):
        """Gets the cond_operation_az of this ProductInfo.

        产品套餐在可用区的状态，配套status使用。 > - 此参数是AZ级配置，优选取此参数的值，某个AZ没有在此参数中配置时默认使用status参数的取值。 > - 配置格式“az(xx)”。()内为某个AZ的flavor状态，()内必须要填有状态，不填为无效配置。 > - 例如：套餐在某个region的az0正常商用，az1售罄，az2公测，az3正常商用，其他az显示下线，可配置为： >   - “status”设置为：“abandon”  >   - “cond_operation_az”设置为：“az0(normal), az1(sellout), az2(obt), az3(normal)”  > -  说明：如果flavor在某个AZ下的状态与status配置状态不同，必须配置该参数。

        :return: The cond_operation_az of this ProductInfo.
        :rtype: str
        """
        return self._cond_operation_az

    @cond_operation_az.setter
    def cond_operation_az(self, cond_operation_az):
        """Sets the cond_operation_az of this ProductInfo.

        产品套餐在可用区的状态，配套status使用。 > - 此参数是AZ级配置，优选取此参数的值，某个AZ没有在此参数中配置时默认使用status参数的取值。 > - 配置格式“az(xx)”。()内为某个AZ的flavor状态，()内必须要填有状态，不填为无效配置。 > - 例如：套餐在某个region的az0正常商用，az1售罄，az2公测，az3正常商用，其他az显示下线，可配置为： >   - “status”设置为：“abandon”  >   - “cond_operation_az”设置为：“az0(normal), az1(sellout), az2(obt), az3(normal)”  > -  说明：如果flavor在某个AZ下的状态与status配置状态不同，必须配置该参数。

        :param cond_operation_az: The cond_operation_az of this ProductInfo.
        :type cond_operation_az: str
        """
        self._cond_operation_az = cond_operation_az

    @property
    def sub_product_list(self):
        """Gets the sub_product_list of this ProductInfo.

        专属主机的子产品

        :return: The sub_product_list of this ProductInfo.
        :rtype: list[str]
        """
        return self._sub_product_list

    @sub_product_list.setter
    def sub_product_list(self, sub_product_list):
        """Sets the sub_product_list of this ProductInfo.

        专属主机的子产品

        :param sub_product_list: The sub_product_list of this ProductInfo.
        :type sub_product_list: list[str]
        """
        self._sub_product_list = sub_product_list

    @property
    def domain_ids(self):
        """Gets the domain_ids of this ProductInfo.

        产品属于专有的domainId

        :return: The domain_ids of this ProductInfo.
        :rtype: list[str]
        """
        return self._domain_ids

    @domain_ids.setter
    def domain_ids(self, domain_ids):
        """Sets the domain_ids of this ProductInfo.

        产品属于专有的domainId

        :param domain_ids: The domain_ids of this ProductInfo.
        :type domain_ids: list[str]
        """
        self._domain_ids = domain_ids

    @property
    def package_type(self):
        """Gets the package_type of this ProductInfo.

        套餐类型。 - general：表示产品通用套餐。 - dedicated：表示产品专属主机套餐。

        :return: The package_type of this ProductInfo.
        :rtype: str
        """
        return self._package_type

    @package_type.setter
    def package_type(self, package_type):
        """Sets the package_type of this ProductInfo.

        套餐类型。 - general：表示产品通用套餐。 - dedicated：表示产品专属主机套餐。

        :param package_type: The package_type of this ProductInfo.
        :type package_type: str
        """
        self._package_type = package_type

    @property
    def expire_time(self):
        """Gets the expire_time of this ProductInfo.

        产品套餐过期时间,产品将在改时间点后逐步下架

        :return: The expire_time of this ProductInfo.
        :rtype: datetime
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        """Sets the expire_time of this ProductInfo.

        产品套餐过期时间,产品将在改时间点后逐步下架

        :param expire_time: The expire_time of this ProductInfo.
        :type expire_time: datetime
        """
        self._expire_time = expire_time

    @property
    def support_gpu_type(self):
        """Gets the support_gpu_type of this ProductInfo.

        产品套餐支持的GPU类型

        :return: The support_gpu_type of this ProductInfo.
        :rtype: str
        """
        return self._support_gpu_type

    @support_gpu_type.setter
    def support_gpu_type(self, support_gpu_type):
        """Sets the support_gpu_type of this ProductInfo.

        产品套餐支持的GPU类型

        :param support_gpu_type: The support_gpu_type of this ProductInfo.
        :type support_gpu_type: str
        """
        self._support_gpu_type = support_gpu_type

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
        if not isinstance(other, ProductInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
