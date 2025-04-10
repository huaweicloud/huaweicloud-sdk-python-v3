# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListImagesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'imagetype': 'str',
        'isregistered': 'str',
        'os_bit': 'str',
        'os_type': 'str',
        'platform': 'str',
        'support_diskintensive': 'str',
        'support_highperformance': 'str',
        'support_kvm': 'str',
        'support_kvm_gpu_type': 'str',
        'support_kvm_infiniband': 'str',
        'support_largememory': 'str',
        'support_xen': 'str',
        'support_xen_gpu_type': 'str',
        'support_xen_hana': 'str',
        'container_format': 'str',
        'disk_format': 'str',
        'enterprise_project_id': 'str',
        'id': 'str',
        'limit': 'int',
        'marker': 'str',
        'member_status': 'str',
        'min_disk': 'int',
        'min_ram': 'int',
        'name': 'str',
        'owner': 'str',
        'protected': 'bool',
        'sort_dir': 'str',
        'sort_key': 'str',
        'status': 'str',
        'tag': 'str',
        'virtual_env_type': 'str',
        'visibility': 'str',
        'x_sdk_date': 'str',
        'flavor_id': 'str',
        'created_at': 'str',
        'updated_at': 'str',
        'architecture': 'str'
    }

    attribute_map = {
        'imagetype': '__imagetype',
        'isregistered': '__isregistered',
        'os_bit': '__os_bit',
        'os_type': '__os_type',
        'platform': '__platform',
        'support_diskintensive': '__support_diskintensive',
        'support_highperformance': '__support_highperformance',
        'support_kvm': '__support_kvm',
        'support_kvm_gpu_type': '__support_kvm_gpu_type',
        'support_kvm_infiniband': '__support_kvm_infiniband',
        'support_largememory': '__support_largememory',
        'support_xen': '__support_xen',
        'support_xen_gpu_type': '__support_xen_gpu_type',
        'support_xen_hana': '__support_xen_hana',
        'container_format': 'container_format',
        'disk_format': 'disk_format',
        'enterprise_project_id': 'enterprise_project_id',
        'id': 'id',
        'limit': 'limit',
        'marker': 'marker',
        'member_status': 'member_status',
        'min_disk': 'min_disk',
        'min_ram': 'min_ram',
        'name': 'name',
        'owner': 'owner',
        'protected': 'protected',
        'sort_dir': 'sort_dir',
        'sort_key': 'sort_key',
        'status': 'status',
        'tag': 'tag',
        'virtual_env_type': 'virtual_env_type',
        'visibility': 'visibility',
        'x_sdk_date': 'X-Sdk-Date',
        'flavor_id': 'flavor_id',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'architecture': 'architecture'
    }

    def __init__(self, imagetype=None, isregistered=None, os_bit=None, os_type=None, platform=None, support_diskintensive=None, support_highperformance=None, support_kvm=None, support_kvm_gpu_type=None, support_kvm_infiniband=None, support_largememory=None, support_xen=None, support_xen_gpu_type=None, support_xen_hana=None, container_format=None, disk_format=None, enterprise_project_id=None, id=None, limit=None, marker=None, member_status=None, min_disk=None, min_ram=None, name=None, owner=None, protected=None, sort_dir=None, sort_key=None, status=None, tag=None, virtual_env_type=None, visibility=None, x_sdk_date=None, flavor_id=None, created_at=None, updated_at=None, architecture=None):
        r"""ListImagesRequest

        The model defined in huaweicloud sdk

        :param imagetype: 镜像类型，目前支持以下类型： 公共镜像：gold 私有镜像：private 共享镜像：shared 市场镜像：market
        :type imagetype: str
        :param isregistered: 镜像是否可用，取值为true，扩展接口会默认为true，普通用户只能查询取值为true的镜像。
        :type isregistered: str
        :param os_bit: 操作系统位数，一般取值为32或者64。
        :type os_bit: str
        :param os_type: 镜像系统类型，取值为Linux，Windows，Other。
        :type os_type: str
        :param platform: 镜像平台分类
        :type platform: str
        :param support_diskintensive: 表示该镜像支持密集存储。如果镜像支持密集存储性能，则值为true，否则无需增加该属性。
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
        :param support_xen_gpu_type: 表示该镜像是支持XEN虚拟化平台下的GPU优化类型，如果不支持XEN虚拟化下GPU类型，无需添加该属性 。该属性与“__support_xen”和“__support_kvm”属性不共存。
        :type support_xen_gpu_type: str
        :param support_xen_hana: 如果镜像支持XEN虚拟化下HANA类型，取值为true。否则，无需添加该属性。该属性与“__support_xen”和“__support_kvm”属性不共存。
        :type support_xen_hana: str
        :param container_format: 容器类型
        :type container_format: str
        :param disk_format: 镜像格式，目前支持vhd，zvhd、raw，qcow2,zvhd2。默认值是vhd。
        :type disk_format: str
        :param enterprise_project_id: 表示查询某个企业项目下的镜像。 取值为0，表示查询属于default企业项目下的镜像。 取值为UUID，表示查询属于该UUID对应的企业项目下的镜像。取值为all_granted_eps，表示查询当前用户所有企业项目下的镜像。 关于企业项目ID的获取及企业项目特性的详细信息，请参考《企业管理用户指南》。
        :type enterprise_project_id: str
        :param id: 镜像ID
        :type id: str
        :param limit: 用于分页，表示查询几条镜像记录，取值为整数，默认取值为500。
        :type limit: int
        :param marker: 用于分页，表示从哪个镜像开始查询，取值为镜像ID。
        :type marker: str
        :param member_status: 成员状态。目前取值有accepted、rejected、pending。accepted表示已经接受共享的镜像，rejected表示已经拒绝了其他用户共享的镜像，pending表示需要确认的其他用户的共享镜像。需要在查询时设置“visibility”参数为“shared”。
        :type member_status: str
        :param min_disk: 镜像运行需要的最小磁盘，单位为GB 。取值为40～1024GB。
        :type min_disk: int
        :param min_ram: 镜像运行需要的最小内存，单位为MB。参数取值依据弹性云服务器的规格限制，一般设置为0。
        :type min_ram: int
        :param name: 镜像名称
        :type name: str
        :param owner: 镜像属于哪个租户
        :type owner: str
        :param protected: 镜像是否是受保护，取值为true/false，一般查询公共镜像时候取值为true，查询私有镜像可以不指定。
        :type protected: bool
        :param sort_dir: 用于排序，表示升序还是降序，取值为asc和desc。与sort_key一起组合使用，默认为降序desc。
        :type sort_dir: str
        :param sort_key: 用于排序，表示按照哪个字段排序。取值为镜像属性name，container_format，disk_format，status ，id，size字段，默认为创建时间。
        :type sort_key: str
        :param status: 镜像状态。取值如下： queued：表示镜像元数据已经创建成功，等待上传镜像文件。 saving：表示镜像正在上传文件到后端存储。 deleted：表示镜像已经删除。 killed：表示镜像上传错误。 active：表示镜像可以正常使用。
        :type status: str
        :param tag: 标签，用户为镜像增加自定义标签后可以通过该参数过滤查询。
        :type tag: str
        :param virtual_env_type: 镜像使用环境类型：FusionCompute，Ironic，DataImage。如果弹性云服务器镜像，则取值为FusionCompute，如果是数据卷镜像则取值是DataImage，如果是裸金属服务器镜像，则取值是Ironic。
        :type virtual_env_type: str
        :param visibility: 是否被其他租户可见，取值为public、private或shared
        :type visibility: str
        :param x_sdk_date: 请求的发生时间,格式为YYYYMMDDTHHMMSSZ。取值为当前系统的GMT时间。使用AK/SK认证时该字段必选
        :type x_sdk_date: str
        :param flavor_id: 用于通过云服务器规格过滤出可用公共镜像，取值为规格ID。 当前仅支持通过单个规格进行过滤。
        :type flavor_id: str
        :param created_at: 镜像创建时间。支持按照时间点过滤查询，取值格式为“操作符:UTC时间”。 其中操作符支持如下几种： gt：大于 gte：大于等于 lt：小于 lte：小于等于 eq：等于 neq：不等于 时间格式支持：yyyy-MM-ddThh:mm:ssZ或者yyyy-MM-dd hh:mm:ss 例如，查询创建时间在2018-10-28 10:00:00之前的镜像，可以通过如下条件过滤： created_at&#x3D;gt:2018-10-28T10:00:00Z
        :type created_at: str
        :param updated_at: 镜像修改时间。支持按照时间点过滤查询，取值格式为“ 操作符:UTC时间”。 其中操作符支持如下几种： gt：大于 gte：大于等于 lt：小于 lte：小于等于 eq：等于 neq：不等于 时间格式支持：yyyy-MM-ddThh:mm:ssZ或者yyyy-MM-dd hh:mm:ss 例如，查询修改时间在2018-10-28 10:00:00之前的镜像，可以通过如下条件过滤： updated_at&#x3D;gt:2018-10-28T10:00:00Z
        :type updated_at: str
        :param architecture: 镜像架构类型。取值包括： x86 arm
        :type architecture: str
        """
        
        

        self._imagetype = None
        self._isregistered = None
        self._os_bit = None
        self._os_type = None
        self._platform = None
        self._support_diskintensive = None
        self._support_highperformance = None
        self._support_kvm = None
        self._support_kvm_gpu_type = None
        self._support_kvm_infiniband = None
        self._support_largememory = None
        self._support_xen = None
        self._support_xen_gpu_type = None
        self._support_xen_hana = None
        self._container_format = None
        self._disk_format = None
        self._enterprise_project_id = None
        self._id = None
        self._limit = None
        self._marker = None
        self._member_status = None
        self._min_disk = None
        self._min_ram = None
        self._name = None
        self._owner = None
        self._protected = None
        self._sort_dir = None
        self._sort_key = None
        self._status = None
        self._tag = None
        self._virtual_env_type = None
        self._visibility = None
        self._x_sdk_date = None
        self._flavor_id = None
        self._created_at = None
        self._updated_at = None
        self._architecture = None
        self.discriminator = None

        if imagetype is not None:
            self.imagetype = imagetype
        if isregistered is not None:
            self.isregistered = isregistered
        if os_bit is not None:
            self.os_bit = os_bit
        if os_type is not None:
            self.os_type = os_type
        if platform is not None:
            self.platform = platform
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
        if container_format is not None:
            self.container_format = container_format
        if disk_format is not None:
            self.disk_format = disk_format
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if id is not None:
            self.id = id
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if member_status is not None:
            self.member_status = member_status
        if min_disk is not None:
            self.min_disk = min_disk
        if min_ram is not None:
            self.min_ram = min_ram
        if name is not None:
            self.name = name
        if owner is not None:
            self.owner = owner
        if protected is not None:
            self.protected = protected
        if sort_dir is not None:
            self.sort_dir = sort_dir
        if sort_key is not None:
            self.sort_key = sort_key
        if status is not None:
            self.status = status
        if tag is not None:
            self.tag = tag
        if virtual_env_type is not None:
            self.virtual_env_type = virtual_env_type
        if visibility is not None:
            self.visibility = visibility
        if x_sdk_date is not None:
            self.x_sdk_date = x_sdk_date
        if flavor_id is not None:
            self.flavor_id = flavor_id
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if architecture is not None:
            self.architecture = architecture

    @property
    def imagetype(self):
        r"""Gets the imagetype of this ListImagesRequest.

        镜像类型，目前支持以下类型： 公共镜像：gold 私有镜像：private 共享镜像：shared 市场镜像：market

        :return: The imagetype of this ListImagesRequest.
        :rtype: str
        """
        return self._imagetype

    @imagetype.setter
    def imagetype(self, imagetype):
        r"""Sets the imagetype of this ListImagesRequest.

        镜像类型，目前支持以下类型： 公共镜像：gold 私有镜像：private 共享镜像：shared 市场镜像：market

        :param imagetype: The imagetype of this ListImagesRequest.
        :type imagetype: str
        """
        self._imagetype = imagetype

    @property
    def isregistered(self):
        r"""Gets the isregistered of this ListImagesRequest.

        镜像是否可用，取值为true，扩展接口会默认为true，普通用户只能查询取值为true的镜像。

        :return: The isregistered of this ListImagesRequest.
        :rtype: str
        """
        return self._isregistered

    @isregistered.setter
    def isregistered(self, isregistered):
        r"""Sets the isregistered of this ListImagesRequest.

        镜像是否可用，取值为true，扩展接口会默认为true，普通用户只能查询取值为true的镜像。

        :param isregistered: The isregistered of this ListImagesRequest.
        :type isregistered: str
        """
        self._isregistered = isregistered

    @property
    def os_bit(self):
        r"""Gets the os_bit of this ListImagesRequest.

        操作系统位数，一般取值为32或者64。

        :return: The os_bit of this ListImagesRequest.
        :rtype: str
        """
        return self._os_bit

    @os_bit.setter
    def os_bit(self, os_bit):
        r"""Sets the os_bit of this ListImagesRequest.

        操作系统位数，一般取值为32或者64。

        :param os_bit: The os_bit of this ListImagesRequest.
        :type os_bit: str
        """
        self._os_bit = os_bit

    @property
    def os_type(self):
        r"""Gets the os_type of this ListImagesRequest.

        镜像系统类型，取值为Linux，Windows，Other。

        :return: The os_type of this ListImagesRequest.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        r"""Sets the os_type of this ListImagesRequest.

        镜像系统类型，取值为Linux，Windows，Other。

        :param os_type: The os_type of this ListImagesRequest.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def platform(self):
        r"""Gets the platform of this ListImagesRequest.

        镜像平台分类

        :return: The platform of this ListImagesRequest.
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        r"""Sets the platform of this ListImagesRequest.

        镜像平台分类

        :param platform: The platform of this ListImagesRequest.
        :type platform: str
        """
        self._platform = platform

    @property
    def support_diskintensive(self):
        r"""Gets the support_diskintensive of this ListImagesRequest.

        表示该镜像支持密集存储。如果镜像支持密集存储性能，则值为true，否则无需增加该属性。

        :return: The support_diskintensive of this ListImagesRequest.
        :rtype: str
        """
        return self._support_diskintensive

    @support_diskintensive.setter
    def support_diskintensive(self, support_diskintensive):
        r"""Sets the support_diskintensive of this ListImagesRequest.

        表示该镜像支持密集存储。如果镜像支持密集存储性能，则值为true，否则无需增加该属性。

        :param support_diskintensive: The support_diskintensive of this ListImagesRequest.
        :type support_diskintensive: str
        """
        self._support_diskintensive = support_diskintensive

    @property
    def support_highperformance(self):
        r"""Gets the support_highperformance of this ListImagesRequest.

        表示该镜像支持高计算性能。如果镜像支持高计算性能，则值为true，否则无需增加该属性。

        :return: The support_highperformance of this ListImagesRequest.
        :rtype: str
        """
        return self._support_highperformance

    @support_highperformance.setter
    def support_highperformance(self, support_highperformance):
        r"""Sets the support_highperformance of this ListImagesRequest.

        表示该镜像支持高计算性能。如果镜像支持高计算性能，则值为true，否则无需增加该属性。

        :param support_highperformance: The support_highperformance of this ListImagesRequest.
        :type support_highperformance: str
        """
        self._support_highperformance = support_highperformance

    @property
    def support_kvm(self):
        r"""Gets the support_kvm of this ListImagesRequest.

        如果镜像支持KVM，取值为true，否则无需增加该属性。

        :return: The support_kvm of this ListImagesRequest.
        :rtype: str
        """
        return self._support_kvm

    @support_kvm.setter
    def support_kvm(self, support_kvm):
        r"""Sets the support_kvm of this ListImagesRequest.

        如果镜像支持KVM，取值为true，否则无需增加该属性。

        :param support_kvm: The support_kvm of this ListImagesRequest.
        :type support_kvm: str
        """
        self._support_kvm = support_kvm

    @property
    def support_kvm_gpu_type(self):
        r"""Gets the support_kvm_gpu_type of this ListImagesRequest.

        表示该镜像是支持KVM虚拟化平台下的GPU类型，如果不支持KVM虚拟机下GPU类型，无需添加该属性。该属性与“__support_xen”和“__support_kvm”属性不共存。

        :return: The support_kvm_gpu_type of this ListImagesRequest.
        :rtype: str
        """
        return self._support_kvm_gpu_type

    @support_kvm_gpu_type.setter
    def support_kvm_gpu_type(self, support_kvm_gpu_type):
        r"""Sets the support_kvm_gpu_type of this ListImagesRequest.

        表示该镜像是支持KVM虚拟化平台下的GPU类型，如果不支持KVM虚拟机下GPU类型，无需添加该属性。该属性与“__support_xen”和“__support_kvm”属性不共存。

        :param support_kvm_gpu_type: The support_kvm_gpu_type of this ListImagesRequest.
        :type support_kvm_gpu_type: str
        """
        self._support_kvm_gpu_type = support_kvm_gpu_type

    @property
    def support_kvm_infiniband(self):
        r"""Gets the support_kvm_infiniband of this ListImagesRequest.

        如果镜像支持KVM虚拟化下Infiniband网卡类型，取值为true。否则，无需添加该属性。该属性与“__support_xen”属性不共存。

        :return: The support_kvm_infiniband of this ListImagesRequest.
        :rtype: str
        """
        return self._support_kvm_infiniband

    @support_kvm_infiniband.setter
    def support_kvm_infiniband(self, support_kvm_infiniband):
        r"""Sets the support_kvm_infiniband of this ListImagesRequest.

        如果镜像支持KVM虚拟化下Infiniband网卡类型，取值为true。否则，无需添加该属性。该属性与“__support_xen”属性不共存。

        :param support_kvm_infiniband: The support_kvm_infiniband of this ListImagesRequest.
        :type support_kvm_infiniband: str
        """
        self._support_kvm_infiniband = support_kvm_infiniband

    @property
    def support_largememory(self):
        r"""Gets the support_largememory of this ListImagesRequest.

        表示该镜像支持超大内存。如果镜像支持超大内存，取值为true，否则无需增加该属性。

        :return: The support_largememory of this ListImagesRequest.
        :rtype: str
        """
        return self._support_largememory

    @support_largememory.setter
    def support_largememory(self, support_largememory):
        r"""Sets the support_largememory of this ListImagesRequest.

        表示该镜像支持超大内存。如果镜像支持超大内存，取值为true，否则无需增加该属性。

        :param support_largememory: The support_largememory of this ListImagesRequest.
        :type support_largememory: str
        """
        self._support_largememory = support_largememory

    @property
    def support_xen(self):
        r"""Gets the support_xen of this ListImagesRequest.

        如果镜像支持XEN，取值为true，否则无需增加该属性。

        :return: The support_xen of this ListImagesRequest.
        :rtype: str
        """
        return self._support_xen

    @support_xen.setter
    def support_xen(self, support_xen):
        r"""Sets the support_xen of this ListImagesRequest.

        如果镜像支持XEN，取值为true，否则无需增加该属性。

        :param support_xen: The support_xen of this ListImagesRequest.
        :type support_xen: str
        """
        self._support_xen = support_xen

    @property
    def support_xen_gpu_type(self):
        r"""Gets the support_xen_gpu_type of this ListImagesRequest.

        表示该镜像是支持XEN虚拟化平台下的GPU优化类型，如果不支持XEN虚拟化下GPU类型，无需添加该属性 。该属性与“__support_xen”和“__support_kvm”属性不共存。

        :return: The support_xen_gpu_type of this ListImagesRequest.
        :rtype: str
        """
        return self._support_xen_gpu_type

    @support_xen_gpu_type.setter
    def support_xen_gpu_type(self, support_xen_gpu_type):
        r"""Sets the support_xen_gpu_type of this ListImagesRequest.

        表示该镜像是支持XEN虚拟化平台下的GPU优化类型，如果不支持XEN虚拟化下GPU类型，无需添加该属性 。该属性与“__support_xen”和“__support_kvm”属性不共存。

        :param support_xen_gpu_type: The support_xen_gpu_type of this ListImagesRequest.
        :type support_xen_gpu_type: str
        """
        self._support_xen_gpu_type = support_xen_gpu_type

    @property
    def support_xen_hana(self):
        r"""Gets the support_xen_hana of this ListImagesRequest.

        如果镜像支持XEN虚拟化下HANA类型，取值为true。否则，无需添加该属性。该属性与“__support_xen”和“__support_kvm”属性不共存。

        :return: The support_xen_hana of this ListImagesRequest.
        :rtype: str
        """
        return self._support_xen_hana

    @support_xen_hana.setter
    def support_xen_hana(self, support_xen_hana):
        r"""Sets the support_xen_hana of this ListImagesRequest.

        如果镜像支持XEN虚拟化下HANA类型，取值为true。否则，无需添加该属性。该属性与“__support_xen”和“__support_kvm”属性不共存。

        :param support_xen_hana: The support_xen_hana of this ListImagesRequest.
        :type support_xen_hana: str
        """
        self._support_xen_hana = support_xen_hana

    @property
    def container_format(self):
        r"""Gets the container_format of this ListImagesRequest.

        容器类型

        :return: The container_format of this ListImagesRequest.
        :rtype: str
        """
        return self._container_format

    @container_format.setter
    def container_format(self, container_format):
        r"""Sets the container_format of this ListImagesRequest.

        容器类型

        :param container_format: The container_format of this ListImagesRequest.
        :type container_format: str
        """
        self._container_format = container_format

    @property
    def disk_format(self):
        r"""Gets the disk_format of this ListImagesRequest.

        镜像格式，目前支持vhd，zvhd、raw，qcow2,zvhd2。默认值是vhd。

        :return: The disk_format of this ListImagesRequest.
        :rtype: str
        """
        return self._disk_format

    @disk_format.setter
    def disk_format(self, disk_format):
        r"""Sets the disk_format of this ListImagesRequest.

        镜像格式，目前支持vhd，zvhd、raw，qcow2,zvhd2。默认值是vhd。

        :param disk_format: The disk_format of this ListImagesRequest.
        :type disk_format: str
        """
        self._disk_format = disk_format

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListImagesRequest.

        表示查询某个企业项目下的镜像。 取值为0，表示查询属于default企业项目下的镜像。 取值为UUID，表示查询属于该UUID对应的企业项目下的镜像。取值为all_granted_eps，表示查询当前用户所有企业项目下的镜像。 关于企业项目ID的获取及企业项目特性的详细信息，请参考《企业管理用户指南》。

        :return: The enterprise_project_id of this ListImagesRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListImagesRequest.

        表示查询某个企业项目下的镜像。 取值为0，表示查询属于default企业项目下的镜像。 取值为UUID，表示查询属于该UUID对应的企业项目下的镜像。取值为all_granted_eps，表示查询当前用户所有企业项目下的镜像。 关于企业项目ID的获取及企业项目特性的详细信息，请参考《企业管理用户指南》。

        :param enterprise_project_id: The enterprise_project_id of this ListImagesRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def id(self):
        r"""Gets the id of this ListImagesRequest.

        镜像ID

        :return: The id of this ListImagesRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListImagesRequest.

        镜像ID

        :param id: The id of this ListImagesRequest.
        :type id: str
        """
        self._id = id

    @property
    def limit(self):
        r"""Gets the limit of this ListImagesRequest.

        用于分页，表示查询几条镜像记录，取值为整数，默认取值为500。

        :return: The limit of this ListImagesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListImagesRequest.

        用于分页，表示查询几条镜像记录，取值为整数，默认取值为500。

        :param limit: The limit of this ListImagesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListImagesRequest.

        用于分页，表示从哪个镜像开始查询，取值为镜像ID。

        :return: The marker of this ListImagesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListImagesRequest.

        用于分页，表示从哪个镜像开始查询，取值为镜像ID。

        :param marker: The marker of this ListImagesRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def member_status(self):
        r"""Gets the member_status of this ListImagesRequest.

        成员状态。目前取值有accepted、rejected、pending。accepted表示已经接受共享的镜像，rejected表示已经拒绝了其他用户共享的镜像，pending表示需要确认的其他用户的共享镜像。需要在查询时设置“visibility”参数为“shared”。

        :return: The member_status of this ListImagesRequest.
        :rtype: str
        """
        return self._member_status

    @member_status.setter
    def member_status(self, member_status):
        r"""Sets the member_status of this ListImagesRequest.

        成员状态。目前取值有accepted、rejected、pending。accepted表示已经接受共享的镜像，rejected表示已经拒绝了其他用户共享的镜像，pending表示需要确认的其他用户的共享镜像。需要在查询时设置“visibility”参数为“shared”。

        :param member_status: The member_status of this ListImagesRequest.
        :type member_status: str
        """
        self._member_status = member_status

    @property
    def min_disk(self):
        r"""Gets the min_disk of this ListImagesRequest.

        镜像运行需要的最小磁盘，单位为GB 。取值为40～1024GB。

        :return: The min_disk of this ListImagesRequest.
        :rtype: int
        """
        return self._min_disk

    @min_disk.setter
    def min_disk(self, min_disk):
        r"""Sets the min_disk of this ListImagesRequest.

        镜像运行需要的最小磁盘，单位为GB 。取值为40～1024GB。

        :param min_disk: The min_disk of this ListImagesRequest.
        :type min_disk: int
        """
        self._min_disk = min_disk

    @property
    def min_ram(self):
        r"""Gets the min_ram of this ListImagesRequest.

        镜像运行需要的最小内存，单位为MB。参数取值依据弹性云服务器的规格限制，一般设置为0。

        :return: The min_ram of this ListImagesRequest.
        :rtype: int
        """
        return self._min_ram

    @min_ram.setter
    def min_ram(self, min_ram):
        r"""Sets the min_ram of this ListImagesRequest.

        镜像运行需要的最小内存，单位为MB。参数取值依据弹性云服务器的规格限制，一般设置为0。

        :param min_ram: The min_ram of this ListImagesRequest.
        :type min_ram: int
        """
        self._min_ram = min_ram

    @property
    def name(self):
        r"""Gets the name of this ListImagesRequest.

        镜像名称

        :return: The name of this ListImagesRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListImagesRequest.

        镜像名称

        :param name: The name of this ListImagesRequest.
        :type name: str
        """
        self._name = name

    @property
    def owner(self):
        r"""Gets the owner of this ListImagesRequest.

        镜像属于哪个租户

        :return: The owner of this ListImagesRequest.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        r"""Sets the owner of this ListImagesRequest.

        镜像属于哪个租户

        :param owner: The owner of this ListImagesRequest.
        :type owner: str
        """
        self._owner = owner

    @property
    def protected(self):
        r"""Gets the protected of this ListImagesRequest.

        镜像是否是受保护，取值为true/false，一般查询公共镜像时候取值为true，查询私有镜像可以不指定。

        :return: The protected of this ListImagesRequest.
        :rtype: bool
        """
        return self._protected

    @protected.setter
    def protected(self, protected):
        r"""Sets the protected of this ListImagesRequest.

        镜像是否是受保护，取值为true/false，一般查询公共镜像时候取值为true，查询私有镜像可以不指定。

        :param protected: The protected of this ListImagesRequest.
        :type protected: bool
        """
        self._protected = protected

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this ListImagesRequest.

        用于排序，表示升序还是降序，取值为asc和desc。与sort_key一起组合使用，默认为降序desc。

        :return: The sort_dir of this ListImagesRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this ListImagesRequest.

        用于排序，表示升序还是降序，取值为asc和desc。与sort_key一起组合使用，默认为降序desc。

        :param sort_dir: The sort_dir of this ListImagesRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

    @property
    def sort_key(self):
        r"""Gets the sort_key of this ListImagesRequest.

        用于排序，表示按照哪个字段排序。取值为镜像属性name，container_format，disk_format，status ，id，size字段，默认为创建时间。

        :return: The sort_key of this ListImagesRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        r"""Sets the sort_key of this ListImagesRequest.

        用于排序，表示按照哪个字段排序。取值为镜像属性name，container_format，disk_format，status ，id，size字段，默认为创建时间。

        :param sort_key: The sort_key of this ListImagesRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def status(self):
        r"""Gets the status of this ListImagesRequest.

        镜像状态。取值如下： queued：表示镜像元数据已经创建成功，等待上传镜像文件。 saving：表示镜像正在上传文件到后端存储。 deleted：表示镜像已经删除。 killed：表示镜像上传错误。 active：表示镜像可以正常使用。

        :return: The status of this ListImagesRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListImagesRequest.

        镜像状态。取值如下： queued：表示镜像元数据已经创建成功，等待上传镜像文件。 saving：表示镜像正在上传文件到后端存储。 deleted：表示镜像已经删除。 killed：表示镜像上传错误。 active：表示镜像可以正常使用。

        :param status: The status of this ListImagesRequest.
        :type status: str
        """
        self._status = status

    @property
    def tag(self):
        r"""Gets the tag of this ListImagesRequest.

        标签，用户为镜像增加自定义标签后可以通过该参数过滤查询。

        :return: The tag of this ListImagesRequest.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        r"""Sets the tag of this ListImagesRequest.

        标签，用户为镜像增加自定义标签后可以通过该参数过滤查询。

        :param tag: The tag of this ListImagesRequest.
        :type tag: str
        """
        self._tag = tag

    @property
    def virtual_env_type(self):
        r"""Gets the virtual_env_type of this ListImagesRequest.

        镜像使用环境类型：FusionCompute，Ironic，DataImage。如果弹性云服务器镜像，则取值为FusionCompute，如果是数据卷镜像则取值是DataImage，如果是裸金属服务器镜像，则取值是Ironic。

        :return: The virtual_env_type of this ListImagesRequest.
        :rtype: str
        """
        return self._virtual_env_type

    @virtual_env_type.setter
    def virtual_env_type(self, virtual_env_type):
        r"""Sets the virtual_env_type of this ListImagesRequest.

        镜像使用环境类型：FusionCompute，Ironic，DataImage。如果弹性云服务器镜像，则取值为FusionCompute，如果是数据卷镜像则取值是DataImage，如果是裸金属服务器镜像，则取值是Ironic。

        :param virtual_env_type: The virtual_env_type of this ListImagesRequest.
        :type virtual_env_type: str
        """
        self._virtual_env_type = virtual_env_type

    @property
    def visibility(self):
        r"""Gets the visibility of this ListImagesRequest.

        是否被其他租户可见，取值为public、private或shared

        :return: The visibility of this ListImagesRequest.
        :rtype: str
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        r"""Sets the visibility of this ListImagesRequest.

        是否被其他租户可见，取值为public、private或shared

        :param visibility: The visibility of this ListImagesRequest.
        :type visibility: str
        """
        self._visibility = visibility

    @property
    def x_sdk_date(self):
        r"""Gets the x_sdk_date of this ListImagesRequest.

        请求的发生时间,格式为YYYYMMDDTHHMMSSZ。取值为当前系统的GMT时间。使用AK/SK认证时该字段必选

        :return: The x_sdk_date of this ListImagesRequest.
        :rtype: str
        """
        return self._x_sdk_date

    @x_sdk_date.setter
    def x_sdk_date(self, x_sdk_date):
        r"""Sets the x_sdk_date of this ListImagesRequest.

        请求的发生时间,格式为YYYYMMDDTHHMMSSZ。取值为当前系统的GMT时间。使用AK/SK认证时该字段必选

        :param x_sdk_date: The x_sdk_date of this ListImagesRequest.
        :type x_sdk_date: str
        """
        self._x_sdk_date = x_sdk_date

    @property
    def flavor_id(self):
        r"""Gets the flavor_id of this ListImagesRequest.

        用于通过云服务器规格过滤出可用公共镜像，取值为规格ID。 当前仅支持通过单个规格进行过滤。

        :return: The flavor_id of this ListImagesRequest.
        :rtype: str
        """
        return self._flavor_id

    @flavor_id.setter
    def flavor_id(self, flavor_id):
        r"""Sets the flavor_id of this ListImagesRequest.

        用于通过云服务器规格过滤出可用公共镜像，取值为规格ID。 当前仅支持通过单个规格进行过滤。

        :param flavor_id: The flavor_id of this ListImagesRequest.
        :type flavor_id: str
        """
        self._flavor_id = flavor_id

    @property
    def created_at(self):
        r"""Gets the created_at of this ListImagesRequest.

        镜像创建时间。支持按照时间点过滤查询，取值格式为“操作符:UTC时间”。 其中操作符支持如下几种： gt：大于 gte：大于等于 lt：小于 lte：小于等于 eq：等于 neq：不等于 时间格式支持：yyyy-MM-ddThh:mm:ssZ或者yyyy-MM-dd hh:mm:ss 例如，查询创建时间在2018-10-28 10:00:00之前的镜像，可以通过如下条件过滤： created_at=gt:2018-10-28T10:00:00Z

        :return: The created_at of this ListImagesRequest.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this ListImagesRequest.

        镜像创建时间。支持按照时间点过滤查询，取值格式为“操作符:UTC时间”。 其中操作符支持如下几种： gt：大于 gte：大于等于 lt：小于 lte：小于等于 eq：等于 neq：不等于 时间格式支持：yyyy-MM-ddThh:mm:ssZ或者yyyy-MM-dd hh:mm:ss 例如，查询创建时间在2018-10-28 10:00:00之前的镜像，可以通过如下条件过滤： created_at=gt:2018-10-28T10:00:00Z

        :param created_at: The created_at of this ListImagesRequest.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this ListImagesRequest.

        镜像修改时间。支持按照时间点过滤查询，取值格式为“ 操作符:UTC时间”。 其中操作符支持如下几种： gt：大于 gte：大于等于 lt：小于 lte：小于等于 eq：等于 neq：不等于 时间格式支持：yyyy-MM-ddThh:mm:ssZ或者yyyy-MM-dd hh:mm:ss 例如，查询修改时间在2018-10-28 10:00:00之前的镜像，可以通过如下条件过滤： updated_at=gt:2018-10-28T10:00:00Z

        :return: The updated_at of this ListImagesRequest.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this ListImagesRequest.

        镜像修改时间。支持按照时间点过滤查询，取值格式为“ 操作符:UTC时间”。 其中操作符支持如下几种： gt：大于 gte：大于等于 lt：小于 lte：小于等于 eq：等于 neq：不等于 时间格式支持：yyyy-MM-ddThh:mm:ssZ或者yyyy-MM-dd hh:mm:ss 例如，查询修改时间在2018-10-28 10:00:00之前的镜像，可以通过如下条件过滤： updated_at=gt:2018-10-28T10:00:00Z

        :param updated_at: The updated_at of this ListImagesRequest.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def architecture(self):
        r"""Gets the architecture of this ListImagesRequest.

        镜像架构类型。取值包括： x86 arm

        :return: The architecture of this ListImagesRequest.
        :rtype: str
        """
        return self._architecture

    @architecture.setter
    def architecture(self, architecture):
        r"""Sets the architecture of this ListImagesRequest.

        镜像架构类型。取值包括： x86 arm

        :param architecture: The architecture of this ListImagesRequest.
        :type architecture: str
        """
        self._architecture = architecture

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
        if not isinstance(other, ListImagesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
