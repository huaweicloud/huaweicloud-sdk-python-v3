# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImageInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'backup_id': 'str',
        'data_origin': 'str',
        'description': 'str',
        'image_size': 'str',
        'image_source_type': 'str',
        'imagetype': 'str',
        'isregistered': 'str',
        'originalimagename': 'str',
        'os_bit': 'str',
        'os_type': 'str',
        'os_version': 'str',
        'platform': 'str',
        'productcode': 'str',
        'support_diskintensive': 'str',
        'support_highperformance': 'str',
        'support_kvm': 'str',
        'support_kvm_gpu_type': 'str',
        'support_kvm_infiniband': 'str',
        'support_largememory': 'str',
        'support_xen': 'str',
        'support_xen_gpu_type': 'str',
        'support_xen_hana': 'str',
        'system_support_market': 'bool',
        'checksum': 'str',
        'container_format': 'str',
        'created_at': 'str',
        'disk_format': 'str',
        'enterprise_project_id': 'str',
        'file': 'str',
        'id': 'str',
        'min_disk': 'int',
        'min_ram': 'int',
        'name': 'str',
        'owner': 'str',
        'protected': 'bool',
        'schema': 'str',
        '_self': 'str',
        'size': 'int',
        'status': 'str',
        'tags': 'list[str]',
        'updated_at': 'str',
        'virtual_env_type': 'str',
        'virtual_size': 'int',
        'visibility': 'str',
        'support_fc_inject': 'str',
        'hw_firmware_type': 'str',
        'support_arm': 'str',
        'max_ram': 'str',
        'system__cmkid': 'str',
        'os_feature_list': 'str',
        'account_code': 'str',
        'hw_vif_multiqueue_enabled': 'str',
        'is_offshelved': 'str',
        'lazyloading': 'str',
        'root_origin': 'str',
        'sequence_num': 'str',
        'active_at': 'str',
        'support_agent_list': 'str',
        'image_displayname': 'str',
        'support_amd': 'str',
        'support_kvm_hi1822_hisriov': 'str',
        'support_kvm_hi1822_hivirtionet': 'str',
        'os_shutdown_timeout': 'str'
    }

    attribute_map = {
        'backup_id': '__backup_id',
        'data_origin': '__data_origin',
        'description': '__description',
        'image_size': '__image_size',
        'image_source_type': '__image_source_type',
        'imagetype': '__imagetype',
        'isregistered': '__isregistered',
        'originalimagename': '__originalimagename',
        'os_bit': '__os_bit',
        'os_type': '__os_type',
        'os_version': '__os_version',
        'platform': '__platform',
        'productcode': '__productcode',
        'support_diskintensive': '__support_diskintensive',
        'support_highperformance': '__support_highperformance',
        'support_kvm': '__support_kvm',
        'support_kvm_gpu_type': '__support_kvm_gpu_type',
        'support_kvm_infiniband': '__support_kvm_infiniband',
        'support_largememory': '__support_largememory',
        'support_xen': '__support_xen',
        'support_xen_gpu_type': '__support_xen_gpu_type',
        'support_xen_hana': '__support_xen_hana',
        'system_support_market': '__system_support_market',
        'checksum': 'checksum',
        'container_format': 'container_format',
        'created_at': 'created_at',
        'disk_format': 'disk_format',
        'enterprise_project_id': 'enterprise_project_id',
        'file': 'file',
        'id': 'id',
        'min_disk': 'min_disk',
        'min_ram': 'min_ram',
        'name': 'name',
        'owner': 'owner',
        'protected': 'protected',
        'schema': 'schema',
        '_self': 'self',
        'size': 'size',
        'status': 'status',
        'tags': 'tags',
        'updated_at': 'updated_at',
        'virtual_env_type': 'virtual_env_type',
        'virtual_size': 'virtual_size',
        'visibility': 'visibility',
        'support_fc_inject': '__support_fc_inject',
        'hw_firmware_type': 'hw_firmware_type',
        'support_arm': '__support_arm',
        'max_ram': 'max_ram',
        'system__cmkid': '__system__cmkid',
        'os_feature_list': '__os_feature_list',
        'account_code': '__account_code',
        'hw_vif_multiqueue_enabled': 'hw_vif_multiqueue_enabled',
        'is_offshelved': '__is_offshelved',
        'lazyloading': '__lazyloading',
        'root_origin': '__root_origin',
        'sequence_num': '__sequence_num',
        'active_at': 'active_at',
        'support_agent_list': '__support_agent_list',
        'image_displayname': '__image_displayname',
        'support_amd': '__support_amd',
        'support_kvm_hi1822_hisriov': '__support_kvm_hi1822_hisriov',
        'support_kvm_hi1822_hivirtionet': '__support_kvm_hi1822_hivirtionet',
        'os_shutdown_timeout': 'os_shutdown_timeout'
    }

    def __init__(self, backup_id=None, data_origin=None, description=None, image_size=None, image_source_type=None, imagetype=None, isregistered=None, originalimagename=None, os_bit=None, os_type=None, os_version=None, platform=None, productcode=None, support_diskintensive=None, support_highperformance=None, support_kvm=None, support_kvm_gpu_type=None, support_kvm_infiniband=None, support_largememory=None, support_xen=None, support_xen_gpu_type=None, support_xen_hana=None, system_support_market=None, checksum=None, container_format=None, created_at=None, disk_format=None, enterprise_project_id=None, file=None, id=None, min_disk=None, min_ram=None, name=None, owner=None, protected=None, schema=None, _self=None, size=None, status=None, tags=None, updated_at=None, virtual_env_type=None, virtual_size=None, visibility=None, support_fc_inject=None, hw_firmware_type=None, support_arm=None, max_ram=None, system__cmkid=None, os_feature_list=None, account_code=None, hw_vif_multiqueue_enabled=None, is_offshelved=None, lazyloading=None, root_origin=None, sequence_num=None, active_at=None, support_agent_list=None, image_displayname=None, support_amd=None, support_kvm_hi1822_hisriov=None, support_kvm_hi1822_hivirtionet=None, os_shutdown_timeout=None):
        r"""ImageInfo

        The model defined in huaweicloud sdk

        :param backup_id: 备份ID。如果是备份创建的镜像，则填写为备份的ID，否则为空
        :type backup_id: str
        :param data_origin: 镜像来源。公共镜像为空
        :type data_origin: str
        :param description: 镜像描述信息。 支持字母、数字、中文等，不支持回车、&lt;、 &gt;，长度不能超过1024个字符。
        :type description: str
        :param image_size: 镜像文件的大小，单位为字节
        :type image_size: str
        :param image_source_type: 镜像后端存储类型，目前只支持uds
        :type image_source_type: str
        :param imagetype: 镜像类型，目前支持以下类型： 公共镜像：gold 私有镜像：private 共享镜像：shared 市场镜像：market
        :type imagetype: str
        :param isregistered: 是否是注册过的镜像，取值为“true”或者“false”
        :type isregistered: str
        :param originalimagename: 父镜像ID。公共镜像或通过文件创建的私有镜像，取值为空
        :type originalimagename: str
        :param os_bit: 操作系统位数，一般取值为“32”或者“64”
        :type os_bit: str
        :param os_type: 操作系统类型，目前取值Linux， Windows，Other
        :type os_type: str
        :param os_version: 操作系统具体版本
        :type os_version: str
        :param platform: 镜像平台分类
        :type platform: str
        :param productcode: 市场镜像的产品ID
        :type productcode: str
        :param support_diskintensive: 镜像来源表示该镜像支持密集存储。如果镜像支持密集存储性能，则值为true，否则无需增加该属性。
        :type support_diskintensive: str
        :param support_highperformance: 表示该镜像支持高计算性能。如果镜像支持高计算性能，则值为true，否则无需增加该属性。
        :type support_highperformance: str
        :param support_kvm: 如果镜像支持KVM，取值为true，否则无需增加该属性。
        :type support_kvm: str
        :param support_kvm_gpu_type: 表示该镜像是支持KVM虚拟化平台下的GPU类型，如果不支持KVM虚拟机下GPU类型，无需添加该属性。该属性与“__support_xen”和“__support_kvm”属性不共存。
        :type support_kvm_gpu_type: str
        :param support_kvm_infiniband: 如果镜像支持KVM虚拟化下Infiniband网卡类型，取值为true。否则，无需添加该属性。该属性与“__support_xen”属性不共存。
        :type support_kvm_infiniband: str
        :param support_largememory: 表示该镜像支持超大内存。如果镜像支持超大内存，取值为true，否则无需增加该属性。
        :type support_largememory: str
        :param support_xen: 如果镜像支持XEN，取值为true，否则无需增加该属性。
        :type support_xen: str
        :param support_xen_gpu_type: 表示该镜像是支持XEN虚拟化平台下的GPU优化类型，如果不支持XEN虚拟化下GPU类型，无需添加该属性            。该属性与“__support_xen”和“__support_kvm”属性不共存。
        :type support_xen_gpu_type: str
        :param support_xen_hana: 如果镜像支持XEN虚拟化下HANA类型，取值为true。否则，无需添加该属性。该属性与“__support_xen”             和“__support_kvm”属性不共存。
        :type support_xen_hana: str
        :param system_support_market: 表示当前镜像是否支持发布为市场镜像,true表示支持,false 表示不支持
        :type system_support_market: bool
        :param checksum: 目前暂时不使用
        :type checksum: str
        :param container_format: 容器类型
        :type container_format: str
        :param created_at: 创建时间。格式为UTC时间
        :type created_at: str
        :param disk_format: 镜像的格式，目前支持vhd，zvhd、raw，qcow2。默认值是vhd
        :type disk_format: str
        :param enterprise_project_id: 表示当前镜像所属的企业项目。取值为0或无该值，表示属于default企业项目，取值为UUID，表示属于该UUID对应的企业项目。
        :type enterprise_project_id: str
        :param file: 镜像文件下载和上传链接
        :type file: str
        :param id: 镜像ID
        :type id: str
        :param min_disk: 镜像运行需要的最小磁盘容量，单位为GB。取值为40～1024GB。
        :type min_disk: int
        :param min_ram: 镜像运行需要的最小内存，单位为MB。参数取值依据弹性云服务器的规格限制，默认设置为0
        :type min_ram: int
        :param name: 镜像名称。 名称的首尾字母不能为空格。 名称的长度至为1～128位。 名称包含以下4种字符： 大写字母 小写字母 数字 特殊字符包含-、.、_、空格和中文。
        :type name: str
        :param owner: 镜像属于哪个租户
        :type owner: str
        :param protected: 是否是受保护的，受保护的镜像不允许删除。取值为true或false
        :type protected: bool
        :param schema: 镜像视图
        :type schema: str
        :param _self: 镜像链接信息
        :type _self: str
        :param size: 目前暂时不使用
        :type size: int
        :param status: 镜像状态。取值如下：queued：表示镜像元数据已经创建成功，等待 上传镜像文件。saving：表示镜像 正在上传文件到后端存储。deleted：表示镜像已经删除。killed：表示镜像上传错误。active：表示镜像可以正常使用
        :type status: str
        :param tags: 镜像标签列表
        :type tags: list[str]
        :param updated_at: 更新时间。格式为UTC时间
        :type updated_at: str
        :param virtual_env_type: 镜像使用环境类型：FusionCompute，Ironic，DataImage。如果弹性云服务器镜像，则取值为FusionCompute，如果是数据卷镜像则取Dat            aImage，如果是裸金属服务器镜像，则取值是Ironic
        :type virtual_env_type: str
        :param virtual_size: 目前暂时不使用
        :type virtual_size: int
        :param visibility: 是否被其他租户可见，取值为private、public或shared
        :type visibility: str
        :param support_fc_inject: 表示当前镜像支持CloudInit密码/密钥注入方式，建议设置为\&quot;true\&quot;或者\&quot;false\&quot;。 如果取值为\&quot;true\&quot;，表示该镜像不支持CloudInit注入密码/密钥，其他取值时表示支持CloudInit注入密钥/密码。
        :type support_fc_inject: str
        :param hw_firmware_type: 云服务器的启动方式。目前支持： bios：表示bios引导启动。 uefi：表示uefi引导启动。
        :type hw_firmware_type: str
        :param support_arm: 是否是ARM架构类型的镜像，取值为“true”或者“false”。
        :type support_arm: str
        :param max_ram: 镜像支持的最大内存，单位为MB。取值可以参考云服务器规格限制，一般不设置。
        :type max_ram: str
        :param system__cmkid: 加密镜像所使用的密钥ID。
        :type system__cmkid: str
        :param os_feature_list: 镜像附加属性。该属性采用JSON格式来标识镜像支持的高级特性清单。
        :type os_feature_list: str
        :param account_code: 收费镜像标识。
        :type account_code: str
        :param hw_vif_multiqueue_enabled: 镜像是否支持网卡多队列。取值为“true”或者“false”。
        :type hw_vif_multiqueue_enabled: str
        :param is_offshelved: 表示当前市场镜像是否下架。true：已下架 false：未下架
        :type is_offshelved: str
        :param lazyloading: 镜像是否支持延迟加载。取值为“True”或“False”。
        :type lazyloading: str
        :param root_origin: 表示当前镜像来源是从外部导入。取值：file。
        :type root_origin: str
        :param sequence_num: 表示当前镜像对应云服务器的系统盘插槽位置。目前暂时不用
        :type sequence_num: str
        :param active_at: 镜像状态变为正常的时间。
        :type active_at: str
        :param support_agent_list: 镜像是否支持企业主机安全或主机监控。 hss：企业主机安全 ces：主机监控
        :type support_agent_list: str
        :param image_displayname: 对外展示名称。
        :type image_displayname: str
        :param support_amd: 是否是AMD架构类型的镜像。取值为“true”或者“false”。
        :type support_amd: str
        :param support_kvm_hi1822_hisriov: 如果镜像支持sriov直通，取值为true，否则无需增加该属性。
        :type support_kvm_hi1822_hisriov: str
        :param support_kvm_hi1822_hivirtionet: 如果镜像支持Virtio-net直通规格，取值为true，否则无需增加该属性。
        :type support_kvm_hi1822_hivirtionet: str
        :param os_shutdown_timeout: 设置虚拟机的优雅关机超时时间，设置范围为60-300，默认为60（取值为整数，单位为秒）。 云服务器在优雅关机超时后会触发强制关机，避免实例长时间处于关机状态中。 当您的云服务器关机过程中由于特定软件的状态、保存等原因导致优雅关机时间过长，会触发超时强制关机。 您可以通过设置镜像该字段，使得发放的云服务器优雅关机超时时间变长。 该字段当前只影响弹性云服务器，不影响裸金属服务器。
        :type os_shutdown_timeout: str
        """
        
        

        self._backup_id = None
        self._data_origin = None
        self._description = None
        self._image_size = None
        self._image_source_type = None
        self._imagetype = None
        self._isregistered = None
        self._originalimagename = None
        self._os_bit = None
        self._os_type = None
        self._os_version = None
        self._platform = None
        self._productcode = None
        self._support_diskintensive = None
        self._support_highperformance = None
        self._support_kvm = None
        self._support_kvm_gpu_type = None
        self._support_kvm_infiniband = None
        self._support_largememory = None
        self._support_xen = None
        self._support_xen_gpu_type = None
        self._support_xen_hana = None
        self._system_support_market = None
        self._checksum = None
        self._container_format = None
        self._created_at = None
        self._disk_format = None
        self._enterprise_project_id = None
        self._file = None
        self._id = None
        self._min_disk = None
        self._min_ram = None
        self._name = None
        self._owner = None
        self._protected = None
        self._schema = None
        self.__self = None
        self._size = None
        self._status = None
        self._tags = None
        self._updated_at = None
        self._virtual_env_type = None
        self._virtual_size = None
        self._visibility = None
        self._support_fc_inject = None
        self._hw_firmware_type = None
        self._support_arm = None
        self._max_ram = None
        self._system__cmkid = None
        self._os_feature_list = None
        self._account_code = None
        self._hw_vif_multiqueue_enabled = None
        self._is_offshelved = None
        self._lazyloading = None
        self._root_origin = None
        self._sequence_num = None
        self._active_at = None
        self._support_agent_list = None
        self._image_displayname = None
        self._support_amd = None
        self._support_kvm_hi1822_hisriov = None
        self._support_kvm_hi1822_hivirtionet = None
        self._os_shutdown_timeout = None
        self.discriminator = None

        if backup_id is not None:
            self.backup_id = backup_id
        if data_origin is not None:
            self.data_origin = data_origin
        if description is not None:
            self.description = description
        self.image_size = image_size
        self.image_source_type = image_source_type
        self.imagetype = imagetype
        self.isregistered = isregistered
        if originalimagename is not None:
            self.originalimagename = originalimagename
        if os_bit is not None:
            self.os_bit = os_bit
        self.os_type = os_type
        if os_version is not None:
            self.os_version = os_version
        if platform is not None:
            self.platform = platform
        if productcode is not None:
            self.productcode = productcode
        if support_diskintensive is not None:
            self.support_diskintensive = support_diskintensive
        if support_highperformance is not None:
            self.support_highperformance = support_highperformance
        if support_kvm is not None:
            self.support_kvm = support_kvm
        if support_kvm_gpu_type is not None:
            self.support_kvm_gpu_type = support_kvm_gpu_type
        if support_kvm_infiniband is not None:
            self.support_kvm_infiniband = support_kvm_infiniband
        if support_largememory is not None:
            self.support_largememory = support_largememory
        if support_xen is not None:
            self.support_xen = support_xen
        if support_xen_gpu_type is not None:
            self.support_xen_gpu_type = support_xen_gpu_type
        if support_xen_hana is not None:
            self.support_xen_hana = support_xen_hana
        if system_support_market is not None:
            self.system_support_market = system_support_market
        if checksum is not None:
            self.checksum = checksum
        self.container_format = container_format
        self.created_at = created_at
        if disk_format is not None:
            self.disk_format = disk_format
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if file is not None:
            self.file = file
        self.id = id
        self.min_disk = min_disk
        self.min_ram = min_ram
        self.name = name
        self.owner = owner
        self.protected = protected
        if schema is not None:
            self.schema = schema
        self._self = _self
        if size is not None:
            self.size = size
        self.status = status
        self.tags = tags
        self.updated_at = updated_at
        self.virtual_env_type = virtual_env_type
        if virtual_size is not None:
            self.virtual_size = virtual_size
        self.visibility = visibility
        if support_fc_inject is not None:
            self.support_fc_inject = support_fc_inject
        if hw_firmware_type is not None:
            self.hw_firmware_type = hw_firmware_type
        if support_arm is not None:
            self.support_arm = support_arm
        if max_ram is not None:
            self.max_ram = max_ram
        if system__cmkid is not None:
            self.system__cmkid = system__cmkid
        if os_feature_list is not None:
            self.os_feature_list = os_feature_list
        if account_code is not None:
            self.account_code = account_code
        if hw_vif_multiqueue_enabled is not None:
            self.hw_vif_multiqueue_enabled = hw_vif_multiqueue_enabled
        if is_offshelved is not None:
            self.is_offshelved = is_offshelved
        if lazyloading is not None:
            self.lazyloading = lazyloading
        if root_origin is not None:
            self.root_origin = root_origin
        if sequence_num is not None:
            self.sequence_num = sequence_num
        self.active_at = active_at
        if support_agent_list is not None:
            self.support_agent_list = support_agent_list
        if image_displayname is not None:
            self.image_displayname = image_displayname
        if support_amd is not None:
            self.support_amd = support_amd
        if support_kvm_hi1822_hisriov is not None:
            self.support_kvm_hi1822_hisriov = support_kvm_hi1822_hisriov
        if support_kvm_hi1822_hivirtionet is not None:
            self.support_kvm_hi1822_hivirtionet = support_kvm_hi1822_hivirtionet
        if os_shutdown_timeout is not None:
            self.os_shutdown_timeout = os_shutdown_timeout

    @property
    def backup_id(self):
        r"""Gets the backup_id of this ImageInfo.

        备份ID。如果是备份创建的镜像，则填写为备份的ID，否则为空

        :return: The backup_id of this ImageInfo.
        :rtype: str
        """
        return self._backup_id

    @backup_id.setter
    def backup_id(self, backup_id):
        r"""Sets the backup_id of this ImageInfo.

        备份ID。如果是备份创建的镜像，则填写为备份的ID，否则为空

        :param backup_id: The backup_id of this ImageInfo.
        :type backup_id: str
        """
        self._backup_id = backup_id

    @property
    def data_origin(self):
        r"""Gets the data_origin of this ImageInfo.

        镜像来源。公共镜像为空

        :return: The data_origin of this ImageInfo.
        :rtype: str
        """
        return self._data_origin

    @data_origin.setter
    def data_origin(self, data_origin):
        r"""Sets the data_origin of this ImageInfo.

        镜像来源。公共镜像为空

        :param data_origin: The data_origin of this ImageInfo.
        :type data_origin: str
        """
        self._data_origin = data_origin

    @property
    def description(self):
        r"""Gets the description of this ImageInfo.

        镜像描述信息。 支持字母、数字、中文等，不支持回车、<、 >，长度不能超过1024个字符。

        :return: The description of this ImageInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ImageInfo.

        镜像描述信息。 支持字母、数字、中文等，不支持回车、<、 >，长度不能超过1024个字符。

        :param description: The description of this ImageInfo.
        :type description: str
        """
        self._description = description

    @property
    def image_size(self):
        r"""Gets the image_size of this ImageInfo.

        镜像文件的大小，单位为字节

        :return: The image_size of this ImageInfo.
        :rtype: str
        """
        return self._image_size

    @image_size.setter
    def image_size(self, image_size):
        r"""Sets the image_size of this ImageInfo.

        镜像文件的大小，单位为字节

        :param image_size: The image_size of this ImageInfo.
        :type image_size: str
        """
        self._image_size = image_size

    @property
    def image_source_type(self):
        r"""Gets the image_source_type of this ImageInfo.

        镜像后端存储类型，目前只支持uds

        :return: The image_source_type of this ImageInfo.
        :rtype: str
        """
        return self._image_source_type

    @image_source_type.setter
    def image_source_type(self, image_source_type):
        r"""Sets the image_source_type of this ImageInfo.

        镜像后端存储类型，目前只支持uds

        :param image_source_type: The image_source_type of this ImageInfo.
        :type image_source_type: str
        """
        self._image_source_type = image_source_type

    @property
    def imagetype(self):
        r"""Gets the imagetype of this ImageInfo.

        镜像类型，目前支持以下类型： 公共镜像：gold 私有镜像：private 共享镜像：shared 市场镜像：market

        :return: The imagetype of this ImageInfo.
        :rtype: str
        """
        return self._imagetype

    @imagetype.setter
    def imagetype(self, imagetype):
        r"""Sets the imagetype of this ImageInfo.

        镜像类型，目前支持以下类型： 公共镜像：gold 私有镜像：private 共享镜像：shared 市场镜像：market

        :param imagetype: The imagetype of this ImageInfo.
        :type imagetype: str
        """
        self._imagetype = imagetype

    @property
    def isregistered(self):
        r"""Gets the isregistered of this ImageInfo.

        是否是注册过的镜像，取值为“true”或者“false”

        :return: The isregistered of this ImageInfo.
        :rtype: str
        """
        return self._isregistered

    @isregistered.setter
    def isregistered(self, isregistered):
        r"""Sets the isregistered of this ImageInfo.

        是否是注册过的镜像，取值为“true”或者“false”

        :param isregistered: The isregistered of this ImageInfo.
        :type isregistered: str
        """
        self._isregistered = isregistered

    @property
    def originalimagename(self):
        r"""Gets the originalimagename of this ImageInfo.

        父镜像ID。公共镜像或通过文件创建的私有镜像，取值为空

        :return: The originalimagename of this ImageInfo.
        :rtype: str
        """
        return self._originalimagename

    @originalimagename.setter
    def originalimagename(self, originalimagename):
        r"""Sets the originalimagename of this ImageInfo.

        父镜像ID。公共镜像或通过文件创建的私有镜像，取值为空

        :param originalimagename: The originalimagename of this ImageInfo.
        :type originalimagename: str
        """
        self._originalimagename = originalimagename

    @property
    def os_bit(self):
        r"""Gets the os_bit of this ImageInfo.

        操作系统位数，一般取值为“32”或者“64”

        :return: The os_bit of this ImageInfo.
        :rtype: str
        """
        return self._os_bit

    @os_bit.setter
    def os_bit(self, os_bit):
        r"""Sets the os_bit of this ImageInfo.

        操作系统位数，一般取值为“32”或者“64”

        :param os_bit: The os_bit of this ImageInfo.
        :type os_bit: str
        """
        self._os_bit = os_bit

    @property
    def os_type(self):
        r"""Gets the os_type of this ImageInfo.

        操作系统类型，目前取值Linux， Windows，Other

        :return: The os_type of this ImageInfo.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        r"""Sets the os_type of this ImageInfo.

        操作系统类型，目前取值Linux， Windows，Other

        :param os_type: The os_type of this ImageInfo.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def os_version(self):
        r"""Gets the os_version of this ImageInfo.

        操作系统具体版本

        :return: The os_version of this ImageInfo.
        :rtype: str
        """
        return self._os_version

    @os_version.setter
    def os_version(self, os_version):
        r"""Sets the os_version of this ImageInfo.

        操作系统具体版本

        :param os_version: The os_version of this ImageInfo.
        :type os_version: str
        """
        self._os_version = os_version

    @property
    def platform(self):
        r"""Gets the platform of this ImageInfo.

        镜像平台分类

        :return: The platform of this ImageInfo.
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        r"""Sets the platform of this ImageInfo.

        镜像平台分类

        :param platform: The platform of this ImageInfo.
        :type platform: str
        """
        self._platform = platform

    @property
    def productcode(self):
        r"""Gets the productcode of this ImageInfo.

        市场镜像的产品ID

        :return: The productcode of this ImageInfo.
        :rtype: str
        """
        return self._productcode

    @productcode.setter
    def productcode(self, productcode):
        r"""Sets the productcode of this ImageInfo.

        市场镜像的产品ID

        :param productcode: The productcode of this ImageInfo.
        :type productcode: str
        """
        self._productcode = productcode

    @property
    def support_diskintensive(self):
        r"""Gets the support_diskintensive of this ImageInfo.

        镜像来源表示该镜像支持密集存储。如果镜像支持密集存储性能，则值为true，否则无需增加该属性。

        :return: The support_diskintensive of this ImageInfo.
        :rtype: str
        """
        return self._support_diskintensive

    @support_diskintensive.setter
    def support_diskintensive(self, support_diskintensive):
        r"""Sets the support_diskintensive of this ImageInfo.

        镜像来源表示该镜像支持密集存储。如果镜像支持密集存储性能，则值为true，否则无需增加该属性。

        :param support_diskintensive: The support_diskintensive of this ImageInfo.
        :type support_diskintensive: str
        """
        self._support_diskintensive = support_diskintensive

    @property
    def support_highperformance(self):
        r"""Gets the support_highperformance of this ImageInfo.

        表示该镜像支持高计算性能。如果镜像支持高计算性能，则值为true，否则无需增加该属性。

        :return: The support_highperformance of this ImageInfo.
        :rtype: str
        """
        return self._support_highperformance

    @support_highperformance.setter
    def support_highperformance(self, support_highperformance):
        r"""Sets the support_highperformance of this ImageInfo.

        表示该镜像支持高计算性能。如果镜像支持高计算性能，则值为true，否则无需增加该属性。

        :param support_highperformance: The support_highperformance of this ImageInfo.
        :type support_highperformance: str
        """
        self._support_highperformance = support_highperformance

    @property
    def support_kvm(self):
        r"""Gets the support_kvm of this ImageInfo.

        如果镜像支持KVM，取值为true，否则无需增加该属性。

        :return: The support_kvm of this ImageInfo.
        :rtype: str
        """
        return self._support_kvm

    @support_kvm.setter
    def support_kvm(self, support_kvm):
        r"""Sets the support_kvm of this ImageInfo.

        如果镜像支持KVM，取值为true，否则无需增加该属性。

        :param support_kvm: The support_kvm of this ImageInfo.
        :type support_kvm: str
        """
        self._support_kvm = support_kvm

    @property
    def support_kvm_gpu_type(self):
        r"""Gets the support_kvm_gpu_type of this ImageInfo.

        表示该镜像是支持KVM虚拟化平台下的GPU类型，如果不支持KVM虚拟机下GPU类型，无需添加该属性。该属性与“__support_xen”和“__support_kvm”属性不共存。

        :return: The support_kvm_gpu_type of this ImageInfo.
        :rtype: str
        """
        return self._support_kvm_gpu_type

    @support_kvm_gpu_type.setter
    def support_kvm_gpu_type(self, support_kvm_gpu_type):
        r"""Sets the support_kvm_gpu_type of this ImageInfo.

        表示该镜像是支持KVM虚拟化平台下的GPU类型，如果不支持KVM虚拟机下GPU类型，无需添加该属性。该属性与“__support_xen”和“__support_kvm”属性不共存。

        :param support_kvm_gpu_type: The support_kvm_gpu_type of this ImageInfo.
        :type support_kvm_gpu_type: str
        """
        self._support_kvm_gpu_type = support_kvm_gpu_type

    @property
    def support_kvm_infiniband(self):
        r"""Gets the support_kvm_infiniband of this ImageInfo.

        如果镜像支持KVM虚拟化下Infiniband网卡类型，取值为true。否则，无需添加该属性。该属性与“__support_xen”属性不共存。

        :return: The support_kvm_infiniband of this ImageInfo.
        :rtype: str
        """
        return self._support_kvm_infiniband

    @support_kvm_infiniband.setter
    def support_kvm_infiniband(self, support_kvm_infiniband):
        r"""Sets the support_kvm_infiniband of this ImageInfo.

        如果镜像支持KVM虚拟化下Infiniband网卡类型，取值为true。否则，无需添加该属性。该属性与“__support_xen”属性不共存。

        :param support_kvm_infiniband: The support_kvm_infiniband of this ImageInfo.
        :type support_kvm_infiniband: str
        """
        self._support_kvm_infiniband = support_kvm_infiniband

    @property
    def support_largememory(self):
        r"""Gets the support_largememory of this ImageInfo.

        表示该镜像支持超大内存。如果镜像支持超大内存，取值为true，否则无需增加该属性。

        :return: The support_largememory of this ImageInfo.
        :rtype: str
        """
        return self._support_largememory

    @support_largememory.setter
    def support_largememory(self, support_largememory):
        r"""Sets the support_largememory of this ImageInfo.

        表示该镜像支持超大内存。如果镜像支持超大内存，取值为true，否则无需增加该属性。

        :param support_largememory: The support_largememory of this ImageInfo.
        :type support_largememory: str
        """
        self._support_largememory = support_largememory

    @property
    def support_xen(self):
        r"""Gets the support_xen of this ImageInfo.

        如果镜像支持XEN，取值为true，否则无需增加该属性。

        :return: The support_xen of this ImageInfo.
        :rtype: str
        """
        return self._support_xen

    @support_xen.setter
    def support_xen(self, support_xen):
        r"""Sets the support_xen of this ImageInfo.

        如果镜像支持XEN，取值为true，否则无需增加该属性。

        :param support_xen: The support_xen of this ImageInfo.
        :type support_xen: str
        """
        self._support_xen = support_xen

    @property
    def support_xen_gpu_type(self):
        r"""Gets the support_xen_gpu_type of this ImageInfo.

        表示该镜像是支持XEN虚拟化平台下的GPU优化类型，如果不支持XEN虚拟化下GPU类型，无需添加该属性            。该属性与“__support_xen”和“__support_kvm”属性不共存。

        :return: The support_xen_gpu_type of this ImageInfo.
        :rtype: str
        """
        return self._support_xen_gpu_type

    @support_xen_gpu_type.setter
    def support_xen_gpu_type(self, support_xen_gpu_type):
        r"""Sets the support_xen_gpu_type of this ImageInfo.

        表示该镜像是支持XEN虚拟化平台下的GPU优化类型，如果不支持XEN虚拟化下GPU类型，无需添加该属性            。该属性与“__support_xen”和“__support_kvm”属性不共存。

        :param support_xen_gpu_type: The support_xen_gpu_type of this ImageInfo.
        :type support_xen_gpu_type: str
        """
        self._support_xen_gpu_type = support_xen_gpu_type

    @property
    def support_xen_hana(self):
        r"""Gets the support_xen_hana of this ImageInfo.

        如果镜像支持XEN虚拟化下HANA类型，取值为true。否则，无需添加该属性。该属性与“__support_xen”             和“__support_kvm”属性不共存。

        :return: The support_xen_hana of this ImageInfo.
        :rtype: str
        """
        return self._support_xen_hana

    @support_xen_hana.setter
    def support_xen_hana(self, support_xen_hana):
        r"""Sets the support_xen_hana of this ImageInfo.

        如果镜像支持XEN虚拟化下HANA类型，取值为true。否则，无需添加该属性。该属性与“__support_xen”             和“__support_kvm”属性不共存。

        :param support_xen_hana: The support_xen_hana of this ImageInfo.
        :type support_xen_hana: str
        """
        self._support_xen_hana = support_xen_hana

    @property
    def system_support_market(self):
        r"""Gets the system_support_market of this ImageInfo.

        表示当前镜像是否支持发布为市场镜像,true表示支持,false 表示不支持

        :return: The system_support_market of this ImageInfo.
        :rtype: bool
        """
        return self._system_support_market

    @system_support_market.setter
    def system_support_market(self, system_support_market):
        r"""Sets the system_support_market of this ImageInfo.

        表示当前镜像是否支持发布为市场镜像,true表示支持,false 表示不支持

        :param system_support_market: The system_support_market of this ImageInfo.
        :type system_support_market: bool
        """
        self._system_support_market = system_support_market

    @property
    def checksum(self):
        r"""Gets the checksum of this ImageInfo.

        目前暂时不使用

        :return: The checksum of this ImageInfo.
        :rtype: str
        """
        return self._checksum

    @checksum.setter
    def checksum(self, checksum):
        r"""Sets the checksum of this ImageInfo.

        目前暂时不使用

        :param checksum: The checksum of this ImageInfo.
        :type checksum: str
        """
        self._checksum = checksum

    @property
    def container_format(self):
        r"""Gets the container_format of this ImageInfo.

        容器类型

        :return: The container_format of this ImageInfo.
        :rtype: str
        """
        return self._container_format

    @container_format.setter
    def container_format(self, container_format):
        r"""Sets the container_format of this ImageInfo.

        容器类型

        :param container_format: The container_format of this ImageInfo.
        :type container_format: str
        """
        self._container_format = container_format

    @property
    def created_at(self):
        r"""Gets the created_at of this ImageInfo.

        创建时间。格式为UTC时间

        :return: The created_at of this ImageInfo.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this ImageInfo.

        创建时间。格式为UTC时间

        :param created_at: The created_at of this ImageInfo.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def disk_format(self):
        r"""Gets the disk_format of this ImageInfo.

        镜像的格式，目前支持vhd，zvhd、raw，qcow2。默认值是vhd

        :return: The disk_format of this ImageInfo.
        :rtype: str
        """
        return self._disk_format

    @disk_format.setter
    def disk_format(self, disk_format):
        r"""Sets the disk_format of this ImageInfo.

        镜像的格式，目前支持vhd，zvhd、raw，qcow2。默认值是vhd

        :param disk_format: The disk_format of this ImageInfo.
        :type disk_format: str
        """
        self._disk_format = disk_format

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ImageInfo.

        表示当前镜像所属的企业项目。取值为0或无该值，表示属于default企业项目，取值为UUID，表示属于该UUID对应的企业项目。

        :return: The enterprise_project_id of this ImageInfo.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ImageInfo.

        表示当前镜像所属的企业项目。取值为0或无该值，表示属于default企业项目，取值为UUID，表示属于该UUID对应的企业项目。

        :param enterprise_project_id: The enterprise_project_id of this ImageInfo.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def file(self):
        r"""Gets the file of this ImageInfo.

        镜像文件下载和上传链接

        :return: The file of this ImageInfo.
        :rtype: str
        """
        return self._file

    @file.setter
    def file(self, file):
        r"""Sets the file of this ImageInfo.

        镜像文件下载和上传链接

        :param file: The file of this ImageInfo.
        :type file: str
        """
        self._file = file

    @property
    def id(self):
        r"""Gets the id of this ImageInfo.

        镜像ID

        :return: The id of this ImageInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ImageInfo.

        镜像ID

        :param id: The id of this ImageInfo.
        :type id: str
        """
        self._id = id

    @property
    def min_disk(self):
        r"""Gets the min_disk of this ImageInfo.

        镜像运行需要的最小磁盘容量，单位为GB。取值为40～1024GB。

        :return: The min_disk of this ImageInfo.
        :rtype: int
        """
        return self._min_disk

    @min_disk.setter
    def min_disk(self, min_disk):
        r"""Sets the min_disk of this ImageInfo.

        镜像运行需要的最小磁盘容量，单位为GB。取值为40～1024GB。

        :param min_disk: The min_disk of this ImageInfo.
        :type min_disk: int
        """
        self._min_disk = min_disk

    @property
    def min_ram(self):
        r"""Gets the min_ram of this ImageInfo.

        镜像运行需要的最小内存，单位为MB。参数取值依据弹性云服务器的规格限制，默认设置为0

        :return: The min_ram of this ImageInfo.
        :rtype: int
        """
        return self._min_ram

    @min_ram.setter
    def min_ram(self, min_ram):
        r"""Sets the min_ram of this ImageInfo.

        镜像运行需要的最小内存，单位为MB。参数取值依据弹性云服务器的规格限制，默认设置为0

        :param min_ram: The min_ram of this ImageInfo.
        :type min_ram: int
        """
        self._min_ram = min_ram

    @property
    def name(self):
        r"""Gets the name of this ImageInfo.

        镜像名称。 名称的首尾字母不能为空格。 名称的长度至为1～128位。 名称包含以下4种字符： 大写字母 小写字母 数字 特殊字符包含-、.、_、空格和中文。

        :return: The name of this ImageInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ImageInfo.

        镜像名称。 名称的首尾字母不能为空格。 名称的长度至为1～128位。 名称包含以下4种字符： 大写字母 小写字母 数字 特殊字符包含-、.、_、空格和中文。

        :param name: The name of this ImageInfo.
        :type name: str
        """
        self._name = name

    @property
    def owner(self):
        r"""Gets the owner of this ImageInfo.

        镜像属于哪个租户

        :return: The owner of this ImageInfo.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        r"""Sets the owner of this ImageInfo.

        镜像属于哪个租户

        :param owner: The owner of this ImageInfo.
        :type owner: str
        """
        self._owner = owner

    @property
    def protected(self):
        r"""Gets the protected of this ImageInfo.

        是否是受保护的，受保护的镜像不允许删除。取值为true或false

        :return: The protected of this ImageInfo.
        :rtype: bool
        """
        return self._protected

    @protected.setter
    def protected(self, protected):
        r"""Sets the protected of this ImageInfo.

        是否是受保护的，受保护的镜像不允许删除。取值为true或false

        :param protected: The protected of this ImageInfo.
        :type protected: bool
        """
        self._protected = protected

    @property
    def schema(self):
        r"""Gets the schema of this ImageInfo.

        镜像视图

        :return: The schema of this ImageInfo.
        :rtype: str
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        r"""Sets the schema of this ImageInfo.

        镜像视图

        :param schema: The schema of this ImageInfo.
        :type schema: str
        """
        self._schema = schema

    @property
    def _self(self):
        r"""Gets the _self of this ImageInfo.

        镜像链接信息

        :return: The _self of this ImageInfo.
        :rtype: str
        """
        return self.__self

    @_self.setter
    def _self(self, _self):
        r"""Sets the _self of this ImageInfo.

        镜像链接信息

        :param _self: The _self of this ImageInfo.
        :type _self: str
        """
        self.__self = _self

    @property
    def size(self):
        r"""Gets the size of this ImageInfo.

        目前暂时不使用

        :return: The size of this ImageInfo.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this ImageInfo.

        目前暂时不使用

        :param size: The size of this ImageInfo.
        :type size: int
        """
        self._size = size

    @property
    def status(self):
        r"""Gets the status of this ImageInfo.

        镜像状态。取值如下：queued：表示镜像元数据已经创建成功，等待 上传镜像文件。saving：表示镜像 正在上传文件到后端存储。deleted：表示镜像已经删除。killed：表示镜像上传错误。active：表示镜像可以正常使用

        :return: The status of this ImageInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ImageInfo.

        镜像状态。取值如下：queued：表示镜像元数据已经创建成功，等待 上传镜像文件。saving：表示镜像 正在上传文件到后端存储。deleted：表示镜像已经删除。killed：表示镜像上传错误。active：表示镜像可以正常使用

        :param status: The status of this ImageInfo.
        :type status: str
        """
        self._status = status

    @property
    def tags(self):
        r"""Gets the tags of this ImageInfo.

        镜像标签列表

        :return: The tags of this ImageInfo.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ImageInfo.

        镜像标签列表

        :param tags: The tags of this ImageInfo.
        :type tags: list[str]
        """
        self._tags = tags

    @property
    def updated_at(self):
        r"""Gets the updated_at of this ImageInfo.

        更新时间。格式为UTC时间

        :return: The updated_at of this ImageInfo.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this ImageInfo.

        更新时间。格式为UTC时间

        :param updated_at: The updated_at of this ImageInfo.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def virtual_env_type(self):
        r"""Gets the virtual_env_type of this ImageInfo.

        镜像使用环境类型：FusionCompute，Ironic，DataImage。如果弹性云服务器镜像，则取值为FusionCompute，如果是数据卷镜像则取Dat            aImage，如果是裸金属服务器镜像，则取值是Ironic

        :return: The virtual_env_type of this ImageInfo.
        :rtype: str
        """
        return self._virtual_env_type

    @virtual_env_type.setter
    def virtual_env_type(self, virtual_env_type):
        r"""Sets the virtual_env_type of this ImageInfo.

        镜像使用环境类型：FusionCompute，Ironic，DataImage。如果弹性云服务器镜像，则取值为FusionCompute，如果是数据卷镜像则取Dat            aImage，如果是裸金属服务器镜像，则取值是Ironic

        :param virtual_env_type: The virtual_env_type of this ImageInfo.
        :type virtual_env_type: str
        """
        self._virtual_env_type = virtual_env_type

    @property
    def virtual_size(self):
        r"""Gets the virtual_size of this ImageInfo.

        目前暂时不使用

        :return: The virtual_size of this ImageInfo.
        :rtype: int
        """
        return self._virtual_size

    @virtual_size.setter
    def virtual_size(self, virtual_size):
        r"""Sets the virtual_size of this ImageInfo.

        目前暂时不使用

        :param virtual_size: The virtual_size of this ImageInfo.
        :type virtual_size: int
        """
        self._virtual_size = virtual_size

    @property
    def visibility(self):
        r"""Gets the visibility of this ImageInfo.

        是否被其他租户可见，取值为private、public或shared

        :return: The visibility of this ImageInfo.
        :rtype: str
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        r"""Sets the visibility of this ImageInfo.

        是否被其他租户可见，取值为private、public或shared

        :param visibility: The visibility of this ImageInfo.
        :type visibility: str
        """
        self._visibility = visibility

    @property
    def support_fc_inject(self):
        r"""Gets the support_fc_inject of this ImageInfo.

        表示当前镜像支持CloudInit密码/密钥注入方式，建议设置为\"true\"或者\"false\"。 如果取值为\"true\"，表示该镜像不支持CloudInit注入密码/密钥，其他取值时表示支持CloudInit注入密钥/密码。

        :return: The support_fc_inject of this ImageInfo.
        :rtype: str
        """
        return self._support_fc_inject

    @support_fc_inject.setter
    def support_fc_inject(self, support_fc_inject):
        r"""Sets the support_fc_inject of this ImageInfo.

        表示当前镜像支持CloudInit密码/密钥注入方式，建议设置为\"true\"或者\"false\"。 如果取值为\"true\"，表示该镜像不支持CloudInit注入密码/密钥，其他取值时表示支持CloudInit注入密钥/密码。

        :param support_fc_inject: The support_fc_inject of this ImageInfo.
        :type support_fc_inject: str
        """
        self._support_fc_inject = support_fc_inject

    @property
    def hw_firmware_type(self):
        r"""Gets the hw_firmware_type of this ImageInfo.

        云服务器的启动方式。目前支持： bios：表示bios引导启动。 uefi：表示uefi引导启动。

        :return: The hw_firmware_type of this ImageInfo.
        :rtype: str
        """
        return self._hw_firmware_type

    @hw_firmware_type.setter
    def hw_firmware_type(self, hw_firmware_type):
        r"""Sets the hw_firmware_type of this ImageInfo.

        云服务器的启动方式。目前支持： bios：表示bios引导启动。 uefi：表示uefi引导启动。

        :param hw_firmware_type: The hw_firmware_type of this ImageInfo.
        :type hw_firmware_type: str
        """
        self._hw_firmware_type = hw_firmware_type

    @property
    def support_arm(self):
        r"""Gets the support_arm of this ImageInfo.

        是否是ARM架构类型的镜像，取值为“true”或者“false”。

        :return: The support_arm of this ImageInfo.
        :rtype: str
        """
        return self._support_arm

    @support_arm.setter
    def support_arm(self, support_arm):
        r"""Sets the support_arm of this ImageInfo.

        是否是ARM架构类型的镜像，取值为“true”或者“false”。

        :param support_arm: The support_arm of this ImageInfo.
        :type support_arm: str
        """
        self._support_arm = support_arm

    @property
    def max_ram(self):
        r"""Gets the max_ram of this ImageInfo.

        镜像支持的最大内存，单位为MB。取值可以参考云服务器规格限制，一般不设置。

        :return: The max_ram of this ImageInfo.
        :rtype: str
        """
        return self._max_ram

    @max_ram.setter
    def max_ram(self, max_ram):
        r"""Sets the max_ram of this ImageInfo.

        镜像支持的最大内存，单位为MB。取值可以参考云服务器规格限制，一般不设置。

        :param max_ram: The max_ram of this ImageInfo.
        :type max_ram: str
        """
        self._max_ram = max_ram

    @property
    def system__cmkid(self):
        r"""Gets the system__cmkid of this ImageInfo.

        加密镜像所使用的密钥ID。

        :return: The system__cmkid of this ImageInfo.
        :rtype: str
        """
        return self._system__cmkid

    @system__cmkid.setter
    def system__cmkid(self, system__cmkid):
        r"""Sets the system__cmkid of this ImageInfo.

        加密镜像所使用的密钥ID。

        :param system__cmkid: The system__cmkid of this ImageInfo.
        :type system__cmkid: str
        """
        self._system__cmkid = system__cmkid

    @property
    def os_feature_list(self):
        r"""Gets the os_feature_list of this ImageInfo.

        镜像附加属性。该属性采用JSON格式来标识镜像支持的高级特性清单。

        :return: The os_feature_list of this ImageInfo.
        :rtype: str
        """
        return self._os_feature_list

    @os_feature_list.setter
    def os_feature_list(self, os_feature_list):
        r"""Sets the os_feature_list of this ImageInfo.

        镜像附加属性。该属性采用JSON格式来标识镜像支持的高级特性清单。

        :param os_feature_list: The os_feature_list of this ImageInfo.
        :type os_feature_list: str
        """
        self._os_feature_list = os_feature_list

    @property
    def account_code(self):
        r"""Gets the account_code of this ImageInfo.

        收费镜像标识。

        :return: The account_code of this ImageInfo.
        :rtype: str
        """
        return self._account_code

    @account_code.setter
    def account_code(self, account_code):
        r"""Sets the account_code of this ImageInfo.

        收费镜像标识。

        :param account_code: The account_code of this ImageInfo.
        :type account_code: str
        """
        self._account_code = account_code

    @property
    def hw_vif_multiqueue_enabled(self):
        r"""Gets the hw_vif_multiqueue_enabled of this ImageInfo.

        镜像是否支持网卡多队列。取值为“true”或者“false”。

        :return: The hw_vif_multiqueue_enabled of this ImageInfo.
        :rtype: str
        """
        return self._hw_vif_multiqueue_enabled

    @hw_vif_multiqueue_enabled.setter
    def hw_vif_multiqueue_enabled(self, hw_vif_multiqueue_enabled):
        r"""Sets the hw_vif_multiqueue_enabled of this ImageInfo.

        镜像是否支持网卡多队列。取值为“true”或者“false”。

        :param hw_vif_multiqueue_enabled: The hw_vif_multiqueue_enabled of this ImageInfo.
        :type hw_vif_multiqueue_enabled: str
        """
        self._hw_vif_multiqueue_enabled = hw_vif_multiqueue_enabled

    @property
    def is_offshelved(self):
        r"""Gets the is_offshelved of this ImageInfo.

        表示当前市场镜像是否下架。true：已下架 false：未下架

        :return: The is_offshelved of this ImageInfo.
        :rtype: str
        """
        return self._is_offshelved

    @is_offshelved.setter
    def is_offshelved(self, is_offshelved):
        r"""Sets the is_offshelved of this ImageInfo.

        表示当前市场镜像是否下架。true：已下架 false：未下架

        :param is_offshelved: The is_offshelved of this ImageInfo.
        :type is_offshelved: str
        """
        self._is_offshelved = is_offshelved

    @property
    def lazyloading(self):
        r"""Gets the lazyloading of this ImageInfo.

        镜像是否支持延迟加载。取值为“True”或“False”。

        :return: The lazyloading of this ImageInfo.
        :rtype: str
        """
        return self._lazyloading

    @lazyloading.setter
    def lazyloading(self, lazyloading):
        r"""Sets the lazyloading of this ImageInfo.

        镜像是否支持延迟加载。取值为“True”或“False”。

        :param lazyloading: The lazyloading of this ImageInfo.
        :type lazyloading: str
        """
        self._lazyloading = lazyloading

    @property
    def root_origin(self):
        r"""Gets the root_origin of this ImageInfo.

        表示当前镜像来源是从外部导入。取值：file。

        :return: The root_origin of this ImageInfo.
        :rtype: str
        """
        return self._root_origin

    @root_origin.setter
    def root_origin(self, root_origin):
        r"""Sets the root_origin of this ImageInfo.

        表示当前镜像来源是从外部导入。取值：file。

        :param root_origin: The root_origin of this ImageInfo.
        :type root_origin: str
        """
        self._root_origin = root_origin

    @property
    def sequence_num(self):
        r"""Gets the sequence_num of this ImageInfo.

        表示当前镜像对应云服务器的系统盘插槽位置。目前暂时不用

        :return: The sequence_num of this ImageInfo.
        :rtype: str
        """
        return self._sequence_num

    @sequence_num.setter
    def sequence_num(self, sequence_num):
        r"""Sets the sequence_num of this ImageInfo.

        表示当前镜像对应云服务器的系统盘插槽位置。目前暂时不用

        :param sequence_num: The sequence_num of this ImageInfo.
        :type sequence_num: str
        """
        self._sequence_num = sequence_num

    @property
    def active_at(self):
        r"""Gets the active_at of this ImageInfo.

        镜像状态变为正常的时间。

        :return: The active_at of this ImageInfo.
        :rtype: str
        """
        return self._active_at

    @active_at.setter
    def active_at(self, active_at):
        r"""Sets the active_at of this ImageInfo.

        镜像状态变为正常的时间。

        :param active_at: The active_at of this ImageInfo.
        :type active_at: str
        """
        self._active_at = active_at

    @property
    def support_agent_list(self):
        r"""Gets the support_agent_list of this ImageInfo.

        镜像是否支持企业主机安全或主机监控。 hss：企业主机安全 ces：主机监控

        :return: The support_agent_list of this ImageInfo.
        :rtype: str
        """
        return self._support_agent_list

    @support_agent_list.setter
    def support_agent_list(self, support_agent_list):
        r"""Sets the support_agent_list of this ImageInfo.

        镜像是否支持企业主机安全或主机监控。 hss：企业主机安全 ces：主机监控

        :param support_agent_list: The support_agent_list of this ImageInfo.
        :type support_agent_list: str
        """
        self._support_agent_list = support_agent_list

    @property
    def image_displayname(self):
        r"""Gets the image_displayname of this ImageInfo.

        对外展示名称。

        :return: The image_displayname of this ImageInfo.
        :rtype: str
        """
        return self._image_displayname

    @image_displayname.setter
    def image_displayname(self, image_displayname):
        r"""Sets the image_displayname of this ImageInfo.

        对外展示名称。

        :param image_displayname: The image_displayname of this ImageInfo.
        :type image_displayname: str
        """
        self._image_displayname = image_displayname

    @property
    def support_amd(self):
        r"""Gets the support_amd of this ImageInfo.

        是否是AMD架构类型的镜像。取值为“true”或者“false”。

        :return: The support_amd of this ImageInfo.
        :rtype: str
        """
        return self._support_amd

    @support_amd.setter
    def support_amd(self, support_amd):
        r"""Sets the support_amd of this ImageInfo.

        是否是AMD架构类型的镜像。取值为“true”或者“false”。

        :param support_amd: The support_amd of this ImageInfo.
        :type support_amd: str
        """
        self._support_amd = support_amd

    @property
    def support_kvm_hi1822_hisriov(self):
        r"""Gets the support_kvm_hi1822_hisriov of this ImageInfo.

        如果镜像支持sriov直通，取值为true，否则无需增加该属性。

        :return: The support_kvm_hi1822_hisriov of this ImageInfo.
        :rtype: str
        """
        return self._support_kvm_hi1822_hisriov

    @support_kvm_hi1822_hisriov.setter
    def support_kvm_hi1822_hisriov(self, support_kvm_hi1822_hisriov):
        r"""Sets the support_kvm_hi1822_hisriov of this ImageInfo.

        如果镜像支持sriov直通，取值为true，否则无需增加该属性。

        :param support_kvm_hi1822_hisriov: The support_kvm_hi1822_hisriov of this ImageInfo.
        :type support_kvm_hi1822_hisriov: str
        """
        self._support_kvm_hi1822_hisriov = support_kvm_hi1822_hisriov

    @property
    def support_kvm_hi1822_hivirtionet(self):
        r"""Gets the support_kvm_hi1822_hivirtionet of this ImageInfo.

        如果镜像支持Virtio-net直通规格，取值为true，否则无需增加该属性。

        :return: The support_kvm_hi1822_hivirtionet of this ImageInfo.
        :rtype: str
        """
        return self._support_kvm_hi1822_hivirtionet

    @support_kvm_hi1822_hivirtionet.setter
    def support_kvm_hi1822_hivirtionet(self, support_kvm_hi1822_hivirtionet):
        r"""Sets the support_kvm_hi1822_hivirtionet of this ImageInfo.

        如果镜像支持Virtio-net直通规格，取值为true，否则无需增加该属性。

        :param support_kvm_hi1822_hivirtionet: The support_kvm_hi1822_hivirtionet of this ImageInfo.
        :type support_kvm_hi1822_hivirtionet: str
        """
        self._support_kvm_hi1822_hivirtionet = support_kvm_hi1822_hivirtionet

    @property
    def os_shutdown_timeout(self):
        r"""Gets the os_shutdown_timeout of this ImageInfo.

        设置虚拟机的优雅关机超时时间，设置范围为60-300，默认为60（取值为整数，单位为秒）。 云服务器在优雅关机超时后会触发强制关机，避免实例长时间处于关机状态中。 当您的云服务器关机过程中由于特定软件的状态、保存等原因导致优雅关机时间过长，会触发超时强制关机。 您可以通过设置镜像该字段，使得发放的云服务器优雅关机超时时间变长。 该字段当前只影响弹性云服务器，不影响裸金属服务器。

        :return: The os_shutdown_timeout of this ImageInfo.
        :rtype: str
        """
        return self._os_shutdown_timeout

    @os_shutdown_timeout.setter
    def os_shutdown_timeout(self, os_shutdown_timeout):
        r"""Sets the os_shutdown_timeout of this ImageInfo.

        设置虚拟机的优雅关机超时时间，设置范围为60-300，默认为60（取值为整数，单位为秒）。 云服务器在优雅关机超时后会触发强制关机，避免实例长时间处于关机状态中。 当您的云服务器关机过程中由于特定软件的状态、保存等原因导致优雅关机时间过长，会触发超时强制关机。 您可以通过设置镜像该字段，使得发放的云服务器优雅关机超时时间变长。 该字段当前只影响弹性云服务器，不影响裸金属服务器。

        :param os_shutdown_timeout: The os_shutdown_timeout of this ImageInfo.
        :type os_shutdown_timeout: str
        """
        self._os_shutdown_timeout = os_shutdown_timeout

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
        if not isinstance(other, ImageInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
