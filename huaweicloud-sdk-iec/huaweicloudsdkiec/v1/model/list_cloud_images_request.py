# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCloudImagesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'region_id': 'str',
        'imagetype': 'str',
        'isregistered': 'str',
        'os_type': 'str',
        'support_diskintensive': 'str',
        'support_highperformance': 'str',
        'support_kvm': 'str',
        'support_kvm_gpu_type': 'str',
        'support_kvm_infiniband': 'str',
        'support_largememory': 'str',
        'support_xen': 'str',
        'support_xen_gpu_type': 'str',
        'support_xen_hana': 'str',
        'id': 'str',
        'limit': 'int',
        'marker': 'str',
        'name': 'str',
        'owner': 'str',
        'protected': 'str',
        'sort_dir': 'str',
        'sort_key': 'str',
        'status': 'str',
        'virtual_env_type': 'str',
        'visibility': 'str'
    }

    attribute_map = {
        'region_id': 'region_id',
        'imagetype': '__imagetype',
        'isregistered': '__isregistered',
        'os_type': '__os_type',
        'support_diskintensive': '__support_diskintensive',
        'support_highperformance': '__support_highperformance',
        'support_kvm': '__support_kvm',
        'support_kvm_gpu_type': '__support_kvm_gpu_type',
        'support_kvm_infiniband': '__support_kvm_infiniband',
        'support_largememory': '__support_largememory',
        'support_xen': '__support_xen',
        'support_xen_gpu_type': '__support_xen_gpu_type',
        'support_xen_hana': '__support_xen_hana',
        'id': 'id',
        'limit': 'limit',
        'marker': 'marker',
        'name': 'name',
        'owner': 'owner',
        'protected': 'protected',
        'sort_dir': 'sort_dir',
        'sort_key': 'sort_key',
        'status': 'status',
        'virtual_env_type': 'virtual_env_type',
        'visibility': 'visibility'
    }

    def __init__(self, region_id=None, imagetype=None, isregistered=None, os_type=None, support_diskintensive=None, support_highperformance=None, support_kvm=None, support_kvm_gpu_type=None, support_kvm_infiniband=None, support_largememory=None, support_xen=None, support_xen_gpu_type=None, support_xen_hana=None, id=None, limit=None, marker=None, name=None, owner=None, protected=None, sort_dir=None, sort_key=None, status=None, virtual_env_type=None, visibility=None):
        """ListCloudImagesRequest

        The model defined in huaweicloud sdk

        :param region_id: 华为云区域ID
        :type region_id: str
        :param imagetype: 镜像类型，目前支持以下类型：  - 公共镜像：gold  - 私有镜像：private
        :type imagetype: str
        :param isregistered: 镜像是否可用，取值为true/false。 &gt; 查询公共镜像时，该参数无效。
        :type isregistered: str
        :param os_type: 镜像系统类型，取值如下：  - Linux - Windows - Other
        :type os_type: str
        :param support_diskintensive: 表示该镜像支持密集存储。如果镜像支持密集存储性能，则值为true，否则无需增加该属性。
        :type support_diskintensive: str
        :param support_highperformance: 表示该镜像支持高计算性能。如果镜像支持高计算性能，则值为true，否则无需增加该属性。
        :type support_highperformance: str
        :param support_kvm: 如果镜像支持KVM，取值为true，否则无该属性。
        :type support_kvm: str
        :param support_kvm_gpu_type: 如果镜像是支持KVM虚拟化平台下的GPU类型，取值为“V100_vGPU”或者“RTX5000”，否则无该属性。
        :type support_kvm_gpu_type: str
        :param support_kvm_infiniband: 如果镜像支持KVM虚拟化下Infiniband网卡类型，取值为true。否则，无需添加该属性。  该属性与“__support_xen”属性不共存。
        :type support_kvm_infiniband: str
        :param support_largememory: 表示该镜像支持超大内存。如果镜像支持超大内存，取值为true，否则无需增加该属性。
        :type support_largememory: str
        :param support_xen: 如果镜像支持XEN，取值为true，否则无需增加该属性。
        :type support_xen: str
        :param support_xen_gpu_type: 表示该镜像是支持XEN虚拟化平台下的GPU优化类型。如果不支持XEN虚拟化下GPU类型，无需添加该属性。该属性与“__support_xen”和“__support_kvm”属性不共存。
        :type support_xen_gpu_type: str
        :param support_xen_hana: 如果镜像支持XEN虚拟化下HANA类型，取值为true。否则，无需添加该属性。  该属性与“__support_xen”和“__support_kvm”属性不共存。
        :type support_xen_hana: str
        :param id: 镜像ID，精确匹配。
        :type id: str
        :param limit: 用于分页，表示查询几条镜像记录，取值为正整数，最大（默认）取值为500
        :type limit: int
        :param marker: 用于分页，表示从哪个镜像开始查询，取值为镜像ID。
        :type marker: str
        :param name: 镜像名称，匹配规则为精确匹配。
        :type name: str
        :param owner: 镜像属于哪个租户。
        :type owner: str
        :param protected: 镜像是否是受保护，取值为true/false，一般查询公共镜像时候取值为true，查询私有镜像可以不指定。
        :type protected: str
        :param sort_dir: 用于排序，表示升序还是降序，取值为asc和desc，与sort_key一起组合使用，默认为降序desc。
        :type sort_dir: str
        :param sort_key: 用于排序，表示按照哪个字段排序，取值为镜像属性name、status、disk_format、created_at，默认取值为created_at。
        :type sort_key: str
        :param status: 镜像状态。取值如下：  - saving：表示镜像正在上传文件到后端存储  - deleted：表示镜像已经删除  - killed：表示镜像上传错误  - active：表示镜像可以正常使用
        :type status: str
        :param virtual_env_type: 镜像使用环境类型。  目前仅支持系统盘镜像，取值为：FusionCompute
        :type virtual_env_type: str
        :param visibility: 是否被其他租户可见，取值如下：  - public：公共镜像  - private：私有镜像
        :type visibility: str
        """
        
        

        self._region_id = None
        self._imagetype = None
        self._isregistered = None
        self._os_type = None
        self._support_diskintensive = None
        self._support_highperformance = None
        self._support_kvm = None
        self._support_kvm_gpu_type = None
        self._support_kvm_infiniband = None
        self._support_largememory = None
        self._support_xen = None
        self._support_xen_gpu_type = None
        self._support_xen_hana = None
        self._id = None
        self._limit = None
        self._marker = None
        self._name = None
        self._owner = None
        self._protected = None
        self._sort_dir = None
        self._sort_key = None
        self._status = None
        self._virtual_env_type = None
        self._visibility = None
        self.discriminator = None

        self.region_id = region_id
        if imagetype is not None:
            self.imagetype = imagetype
        if isregistered is not None:
            self.isregistered = isregistered
        if os_type is not None:
            self.os_type = os_type
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
        if id is not None:
            self.id = id
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
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
        if virtual_env_type is not None:
            self.virtual_env_type = virtual_env_type
        if visibility is not None:
            self.visibility = visibility

    @property
    def region_id(self):
        """Gets the region_id of this ListCloudImagesRequest.

        华为云区域ID

        :return: The region_id of this ListCloudImagesRequest.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this ListCloudImagesRequest.

        华为云区域ID

        :param region_id: The region_id of this ListCloudImagesRequest.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def imagetype(self):
        """Gets the imagetype of this ListCloudImagesRequest.

        镜像类型，目前支持以下类型：  - 公共镜像：gold  - 私有镜像：private

        :return: The imagetype of this ListCloudImagesRequest.
        :rtype: str
        """
        return self._imagetype

    @imagetype.setter
    def imagetype(self, imagetype):
        """Sets the imagetype of this ListCloudImagesRequest.

        镜像类型，目前支持以下类型：  - 公共镜像：gold  - 私有镜像：private

        :param imagetype: The imagetype of this ListCloudImagesRequest.
        :type imagetype: str
        """
        self._imagetype = imagetype

    @property
    def isregistered(self):
        """Gets the isregistered of this ListCloudImagesRequest.

        镜像是否可用，取值为true/false。 > 查询公共镜像时，该参数无效。

        :return: The isregistered of this ListCloudImagesRequest.
        :rtype: str
        """
        return self._isregistered

    @isregistered.setter
    def isregistered(self, isregistered):
        """Sets the isregistered of this ListCloudImagesRequest.

        镜像是否可用，取值为true/false。 > 查询公共镜像时，该参数无效。

        :param isregistered: The isregistered of this ListCloudImagesRequest.
        :type isregistered: str
        """
        self._isregistered = isregistered

    @property
    def os_type(self):
        """Gets the os_type of this ListCloudImagesRequest.

        镜像系统类型，取值如下：  - Linux - Windows - Other

        :return: The os_type of this ListCloudImagesRequest.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        """Sets the os_type of this ListCloudImagesRequest.

        镜像系统类型，取值如下：  - Linux - Windows - Other

        :param os_type: The os_type of this ListCloudImagesRequest.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def support_diskintensive(self):
        """Gets the support_diskintensive of this ListCloudImagesRequest.

        表示该镜像支持密集存储。如果镜像支持密集存储性能，则值为true，否则无需增加该属性。

        :return: The support_diskintensive of this ListCloudImagesRequest.
        :rtype: str
        """
        return self._support_diskintensive

    @support_diskintensive.setter
    def support_diskintensive(self, support_diskintensive):
        """Sets the support_diskintensive of this ListCloudImagesRequest.

        表示该镜像支持密集存储。如果镜像支持密集存储性能，则值为true，否则无需增加该属性。

        :param support_diskintensive: The support_diskintensive of this ListCloudImagesRequest.
        :type support_diskintensive: str
        """
        self._support_diskintensive = support_diskintensive

    @property
    def support_highperformance(self):
        """Gets the support_highperformance of this ListCloudImagesRequest.

        表示该镜像支持高计算性能。如果镜像支持高计算性能，则值为true，否则无需增加该属性。

        :return: The support_highperformance of this ListCloudImagesRequest.
        :rtype: str
        """
        return self._support_highperformance

    @support_highperformance.setter
    def support_highperformance(self, support_highperformance):
        """Sets the support_highperformance of this ListCloudImagesRequest.

        表示该镜像支持高计算性能。如果镜像支持高计算性能，则值为true，否则无需增加该属性。

        :param support_highperformance: The support_highperformance of this ListCloudImagesRequest.
        :type support_highperformance: str
        """
        self._support_highperformance = support_highperformance

    @property
    def support_kvm(self):
        """Gets the support_kvm of this ListCloudImagesRequest.

        如果镜像支持KVM，取值为true，否则无该属性。

        :return: The support_kvm of this ListCloudImagesRequest.
        :rtype: str
        """
        return self._support_kvm

    @support_kvm.setter
    def support_kvm(self, support_kvm):
        """Sets the support_kvm of this ListCloudImagesRequest.

        如果镜像支持KVM，取值为true，否则无该属性。

        :param support_kvm: The support_kvm of this ListCloudImagesRequest.
        :type support_kvm: str
        """
        self._support_kvm = support_kvm

    @property
    def support_kvm_gpu_type(self):
        """Gets the support_kvm_gpu_type of this ListCloudImagesRequest.

        如果镜像是支持KVM虚拟化平台下的GPU类型，取值为“V100_vGPU”或者“RTX5000”，否则无该属性。

        :return: The support_kvm_gpu_type of this ListCloudImagesRequest.
        :rtype: str
        """
        return self._support_kvm_gpu_type

    @support_kvm_gpu_type.setter
    def support_kvm_gpu_type(self, support_kvm_gpu_type):
        """Sets the support_kvm_gpu_type of this ListCloudImagesRequest.

        如果镜像是支持KVM虚拟化平台下的GPU类型，取值为“V100_vGPU”或者“RTX5000”，否则无该属性。

        :param support_kvm_gpu_type: The support_kvm_gpu_type of this ListCloudImagesRequest.
        :type support_kvm_gpu_type: str
        """
        self._support_kvm_gpu_type = support_kvm_gpu_type

    @property
    def support_kvm_infiniband(self):
        """Gets the support_kvm_infiniband of this ListCloudImagesRequest.

        如果镜像支持KVM虚拟化下Infiniband网卡类型，取值为true。否则，无需添加该属性。  该属性与“__support_xen”属性不共存。

        :return: The support_kvm_infiniband of this ListCloudImagesRequest.
        :rtype: str
        """
        return self._support_kvm_infiniband

    @support_kvm_infiniband.setter
    def support_kvm_infiniband(self, support_kvm_infiniband):
        """Sets the support_kvm_infiniband of this ListCloudImagesRequest.

        如果镜像支持KVM虚拟化下Infiniband网卡类型，取值为true。否则，无需添加该属性。  该属性与“__support_xen”属性不共存。

        :param support_kvm_infiniband: The support_kvm_infiniband of this ListCloudImagesRequest.
        :type support_kvm_infiniband: str
        """
        self._support_kvm_infiniband = support_kvm_infiniband

    @property
    def support_largememory(self):
        """Gets the support_largememory of this ListCloudImagesRequest.

        表示该镜像支持超大内存。如果镜像支持超大内存，取值为true，否则无需增加该属性。

        :return: The support_largememory of this ListCloudImagesRequest.
        :rtype: str
        """
        return self._support_largememory

    @support_largememory.setter
    def support_largememory(self, support_largememory):
        """Sets the support_largememory of this ListCloudImagesRequest.

        表示该镜像支持超大内存。如果镜像支持超大内存，取值为true，否则无需增加该属性。

        :param support_largememory: The support_largememory of this ListCloudImagesRequest.
        :type support_largememory: str
        """
        self._support_largememory = support_largememory

    @property
    def support_xen(self):
        """Gets the support_xen of this ListCloudImagesRequest.

        如果镜像支持XEN，取值为true，否则无需增加该属性。

        :return: The support_xen of this ListCloudImagesRequest.
        :rtype: str
        """
        return self._support_xen

    @support_xen.setter
    def support_xen(self, support_xen):
        """Sets the support_xen of this ListCloudImagesRequest.

        如果镜像支持XEN，取值为true，否则无需增加该属性。

        :param support_xen: The support_xen of this ListCloudImagesRequest.
        :type support_xen: str
        """
        self._support_xen = support_xen

    @property
    def support_xen_gpu_type(self):
        """Gets the support_xen_gpu_type of this ListCloudImagesRequest.

        表示该镜像是支持XEN虚拟化平台下的GPU优化类型。如果不支持XEN虚拟化下GPU类型，无需添加该属性。该属性与“__support_xen”和“__support_kvm”属性不共存。

        :return: The support_xen_gpu_type of this ListCloudImagesRequest.
        :rtype: str
        """
        return self._support_xen_gpu_type

    @support_xen_gpu_type.setter
    def support_xen_gpu_type(self, support_xen_gpu_type):
        """Sets the support_xen_gpu_type of this ListCloudImagesRequest.

        表示该镜像是支持XEN虚拟化平台下的GPU优化类型。如果不支持XEN虚拟化下GPU类型，无需添加该属性。该属性与“__support_xen”和“__support_kvm”属性不共存。

        :param support_xen_gpu_type: The support_xen_gpu_type of this ListCloudImagesRequest.
        :type support_xen_gpu_type: str
        """
        self._support_xen_gpu_type = support_xen_gpu_type

    @property
    def support_xen_hana(self):
        """Gets the support_xen_hana of this ListCloudImagesRequest.

        如果镜像支持XEN虚拟化下HANA类型，取值为true。否则，无需添加该属性。  该属性与“__support_xen”和“__support_kvm”属性不共存。

        :return: The support_xen_hana of this ListCloudImagesRequest.
        :rtype: str
        """
        return self._support_xen_hana

    @support_xen_hana.setter
    def support_xen_hana(self, support_xen_hana):
        """Sets the support_xen_hana of this ListCloudImagesRequest.

        如果镜像支持XEN虚拟化下HANA类型，取值为true。否则，无需添加该属性。  该属性与“__support_xen”和“__support_kvm”属性不共存。

        :param support_xen_hana: The support_xen_hana of this ListCloudImagesRequest.
        :type support_xen_hana: str
        """
        self._support_xen_hana = support_xen_hana

    @property
    def id(self):
        """Gets the id of this ListCloudImagesRequest.

        镜像ID，精确匹配。

        :return: The id of this ListCloudImagesRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListCloudImagesRequest.

        镜像ID，精确匹配。

        :param id: The id of this ListCloudImagesRequest.
        :type id: str
        """
        self._id = id

    @property
    def limit(self):
        """Gets the limit of this ListCloudImagesRequest.

        用于分页，表示查询几条镜像记录，取值为正整数，最大（默认）取值为500

        :return: The limit of this ListCloudImagesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListCloudImagesRequest.

        用于分页，表示查询几条镜像记录，取值为正整数，最大（默认）取值为500

        :param limit: The limit of this ListCloudImagesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListCloudImagesRequest.

        用于分页，表示从哪个镜像开始查询，取值为镜像ID。

        :return: The marker of this ListCloudImagesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListCloudImagesRequest.

        用于分页，表示从哪个镜像开始查询，取值为镜像ID。

        :param marker: The marker of this ListCloudImagesRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def name(self):
        """Gets the name of this ListCloudImagesRequest.

        镜像名称，匹配规则为精确匹配。

        :return: The name of this ListCloudImagesRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListCloudImagesRequest.

        镜像名称，匹配规则为精确匹配。

        :param name: The name of this ListCloudImagesRequest.
        :type name: str
        """
        self._name = name

    @property
    def owner(self):
        """Gets the owner of this ListCloudImagesRequest.

        镜像属于哪个租户。

        :return: The owner of this ListCloudImagesRequest.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this ListCloudImagesRequest.

        镜像属于哪个租户。

        :param owner: The owner of this ListCloudImagesRequest.
        :type owner: str
        """
        self._owner = owner

    @property
    def protected(self):
        """Gets the protected of this ListCloudImagesRequest.

        镜像是否是受保护，取值为true/false，一般查询公共镜像时候取值为true，查询私有镜像可以不指定。

        :return: The protected of this ListCloudImagesRequest.
        :rtype: str
        """
        return self._protected

    @protected.setter
    def protected(self, protected):
        """Sets the protected of this ListCloudImagesRequest.

        镜像是否是受保护，取值为true/false，一般查询公共镜像时候取值为true，查询私有镜像可以不指定。

        :param protected: The protected of this ListCloudImagesRequest.
        :type protected: str
        """
        self._protected = protected

    @property
    def sort_dir(self):
        """Gets the sort_dir of this ListCloudImagesRequest.

        用于排序，表示升序还是降序，取值为asc和desc，与sort_key一起组合使用，默认为降序desc。

        :return: The sort_dir of this ListCloudImagesRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        """Sets the sort_dir of this ListCloudImagesRequest.

        用于排序，表示升序还是降序，取值为asc和desc，与sort_key一起组合使用，默认为降序desc。

        :param sort_dir: The sort_dir of this ListCloudImagesRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

    @property
    def sort_key(self):
        """Gets the sort_key of this ListCloudImagesRequest.

        用于排序，表示按照哪个字段排序，取值为镜像属性name、status、disk_format、created_at，默认取值为created_at。

        :return: The sort_key of this ListCloudImagesRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        """Sets the sort_key of this ListCloudImagesRequest.

        用于排序，表示按照哪个字段排序，取值为镜像属性name、status、disk_format、created_at，默认取值为created_at。

        :param sort_key: The sort_key of this ListCloudImagesRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def status(self):
        """Gets the status of this ListCloudImagesRequest.

        镜像状态。取值如下：  - saving：表示镜像正在上传文件到后端存储  - deleted：表示镜像已经删除  - killed：表示镜像上传错误  - active：表示镜像可以正常使用

        :return: The status of this ListCloudImagesRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListCloudImagesRequest.

        镜像状态。取值如下：  - saving：表示镜像正在上传文件到后端存储  - deleted：表示镜像已经删除  - killed：表示镜像上传错误  - active：表示镜像可以正常使用

        :param status: The status of this ListCloudImagesRequest.
        :type status: str
        """
        self._status = status

    @property
    def virtual_env_type(self):
        """Gets the virtual_env_type of this ListCloudImagesRequest.

        镜像使用环境类型。  目前仅支持系统盘镜像，取值为：FusionCompute

        :return: The virtual_env_type of this ListCloudImagesRequest.
        :rtype: str
        """
        return self._virtual_env_type

    @virtual_env_type.setter
    def virtual_env_type(self, virtual_env_type):
        """Sets the virtual_env_type of this ListCloudImagesRequest.

        镜像使用环境类型。  目前仅支持系统盘镜像，取值为：FusionCompute

        :param virtual_env_type: The virtual_env_type of this ListCloudImagesRequest.
        :type virtual_env_type: str
        """
        self._virtual_env_type = virtual_env_type

    @property
    def visibility(self):
        """Gets the visibility of this ListCloudImagesRequest.

        是否被其他租户可见，取值如下：  - public：公共镜像  - private：私有镜像

        :return: The visibility of this ListCloudImagesRequest.
        :rtype: str
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        """Sets the visibility of this ListCloudImagesRequest.

        是否被其他租户可见，取值如下：  - public：公共镜像  - private：私有镜像

        :param visibility: The visibility of this ListCloudImagesRequest.
        :type visibility: str
        """
        self._visibility = visibility

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
        if not isinstance(other, ListCloudImagesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
