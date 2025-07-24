# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowShareResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'action_progress': 'ActionProgress',
        'version': 'str',
        'avail_capacity': 'str',
        'availability_zone': 'str',
        'az_name': 'str',
        'created_at': 'datetime',
        'crypt_key_id': 'str',
        'expand_type': 'str',
        'export_location': 'str',
        'id': 'str',
        'name': 'str',
        'pay_model': 'str',
        'region': 'str',
        'security_group_id': 'str',
        'share_proto': 'str',
        'share_type': 'str',
        'size': 'str',
        'status': 'str',
        'sub_status': 'str',
        'subnet_id': 'str',
        'vpc_id': 'str',
        'enterprise_project_id': 'str',
        'tags': 'list[ResourceTag]',
        'optional_endpoint': 'str',
        'hpc_bw': 'str',
        'instance_id': 'str',
        'instance_type': 'str',
        'status_detail': 'str',
        'features': 'ShareInfoFeatures'
    }

    attribute_map = {
        'action_progress': 'action_progress',
        'version': 'version',
        'avail_capacity': 'avail_capacity',
        'availability_zone': 'availability_zone',
        'az_name': 'az_name',
        'created_at': 'created_at',
        'crypt_key_id': 'crypt_key_id',
        'expand_type': 'expand_type',
        'export_location': 'export_location',
        'id': 'id',
        'name': 'name',
        'pay_model': 'pay_model',
        'region': 'region',
        'security_group_id': 'security_group_id',
        'share_proto': 'share_proto',
        'share_type': 'share_type',
        'size': 'size',
        'status': 'status',
        'sub_status': 'sub_status',
        'subnet_id': 'subnet_id',
        'vpc_id': 'vpc_id',
        'enterprise_project_id': 'enterprise_project_id',
        'tags': 'tags',
        'optional_endpoint': 'optional_endpoint',
        'hpc_bw': 'hpc_bw',
        'instance_id': 'instanceId',
        'instance_type': 'instanceType',
        'status_detail': 'statusDetail',
        'features': 'features'
    }

    def __init__(self, action_progress=None, version=None, avail_capacity=None, availability_zone=None, az_name=None, created_at=None, crypt_key_id=None, expand_type=None, export_location=None, id=None, name=None, pay_model=None, region=None, security_group_id=None, share_proto=None, share_type=None, size=None, status=None, sub_status=None, subnet_id=None, vpc_id=None, enterprise_project_id=None, tags=None, optional_endpoint=None, hpc_bw=None, instance_id=None, instance_type=None, status_detail=None, features=None):
        r"""ShowShareResponse

        The model defined in huaweicloud sdk

        :param action_progress: 
        :type action_progress: :class:`huaweicloudsdksfsturbo.v1.ActionProgress`
        :param version: SFS Turbo文件系统的版本号。
        :type version: str
        :param avail_capacity: SFS Turbo文件系统剩余容量，单位GB。
        :type avail_capacity: str
        :param availability_zone: SFS Turbo文件系统所在可用区编码。
        :type availability_zone: str
        :param az_name: SFS Turbo文件系统所在可用区名称。
        :type az_name: str
        :param created_at: 创建时间。UTC时间，例如：2018-11-19T04:02:03
        :type created_at: datetime
        :param crypt_key_id: 用户指定的加密密钥ID，非加密盘时不返回。
        :type crypt_key_id: str
        :param expand_type: 如果是增强版文件系统，该字段返回bandwidth；如果是20MB/s/TiB、40MB/s/TiB、125MB/s/TiB、250MB/s/TiB、500MB/s/TiB、1000MB/s/TiB，该字段返回hpc；否则不返回。
        :type expand_type: str
        :param export_location: SFS Turbo文件系统的挂载端点。例如\&quot;192.168.0.90:/\&quot;。如果文件系统正在创建，该字段不返回。
        :type export_location: str
        :param id: SFS Turbo的文件系统ID。
        :type id: str
        :param name: 创建时指定的SFS Turbo文件系统名称。
        :type name: str
        :param pay_model: SFS Turbo文件系统的计费模式。&#39;0&#39;代表按需付费，&#39;1&#39;代表包周期计费。如果文件系统正在创建，该字段不返回。
        :type pay_model: str
        :param region: SFS Turbo文件系统所在区域。
        :type region: str
        :param security_group_id: 用户指定的安全组ID。
        :type security_group_id: str
        :param share_proto: SFS Turbo文件系统的协议类型，当前为NFS或 CIFS。
        :type share_proto: str
        :param share_type: SFS Turbo文件系统性能类型，包括“STANDARD”标准型和“PERFORMANCE”性能型。
        :type share_type: str
        :param size: SFS Turbo文件系统总容量，单位GB。
        :type size: str
        :param status: SFS Turbo文件系统的状态。&#39;100&#39;表示创建中，&#39;200&#39;表示可用，&#39;303&#39;表示创建失败，&#39;800&#39;表示实例被冻结。
        :type status: str
        :param sub_status: SFS Turbo文件系统的子状态。当用户未对文件系统有修改类操作时，该字段不返回。 &#39;121&#39;表示扩容中；&#39;132&#39;表示修改安全组中；&#39;137&#39;表示添加VPC中；&#39;138&#39;表示删除VPC中；&#39;150&#39;表示配置联动后端中；&#39;151&#39;表示删除联动后端配置中。 &#39;221&#39;表示扩容成功；&#39;232&#39;表示修改安全组成功；&#39;237&#39;表示添加VPC成功；&#39;238&#39;表示删除VPC成功；&#39;250&#39;表示配置联动后端成功；&#39;251&#39;表示删除联动后端配置成功。 &#39;321&#39;表示扩容失败；&#39;332&#39;表示修改安全组失败；&#39;337&#39;表示添加VPC失败；&#39;338&#39;表示删除VPC失败；&#39;350&#39;表示配置联动后端失败；&#39;351&#39;表示删除联动后端配置失败。
        :type sub_status: str
        :param subnet_id: 用户指定的子网的网络ID。
        :type subnet_id: str
        :param vpc_id: 用户指定的VPC ID。
        :type vpc_id: str
        :param enterprise_project_id: SFS Turbo文件系统绑定的企业项目ID。
        :type enterprise_project_id: str
        :param tags: tag标签的列表。
        :type tags: list[:class:`huaweicloudsdksfsturbo.v1.ResourceTag`]
        :param optional_endpoint: 可选的挂载IP地址。上一代文件系统规格类型不返回该字段。
        :type optional_endpoint: str
        :param hpc_bw: 文件系统的带宽规格。 - \&quot;20M\&quot;表示20MB/s/TiB - \&quot;40M\&quot;表示40MB/s/TiB - \&quot;125M\&quot;表示125MB/s/TiB - \&quot;250M\&quot;表示250MB/s/TiB - \&quot;500M\&quot;表示500MB/s/TiB  - \&quot;1000M\&quot;表示1000MB/s/TiB  - \&quot;2G\&quot;、\&quot;4G\&quot;、\&quot;8G\&quot;、\&quot;16G\&quot;、\&quot;24G\&quot;、\&quot;32G\&quot;或\&quot;48G\&quot;表示HPC缓存型的带宽规格。 
        :type hpc_bw: str
        :param instance_id: 文件系统规格的节点id，为预留字段，不具备实际含义。
        :type instance_id: str
        :param instance_type: 文件系统规格的节点类型，为预留字段，不具备实际含义。
        :type instance_type: str
        :param status_detail: 文件系统的请求ID，为预留字段，不具备实际含义。
        :type status_detail: str
        :param features: 
        :type features: :class:`huaweicloudsdksfsturbo.v1.ShareInfoFeatures`
        """
        
        super(ShowShareResponse, self).__init__()

        self._action_progress = None
        self._version = None
        self._avail_capacity = None
        self._availability_zone = None
        self._az_name = None
        self._created_at = None
        self._crypt_key_id = None
        self._expand_type = None
        self._export_location = None
        self._id = None
        self._name = None
        self._pay_model = None
        self._region = None
        self._security_group_id = None
        self._share_proto = None
        self._share_type = None
        self._size = None
        self._status = None
        self._sub_status = None
        self._subnet_id = None
        self._vpc_id = None
        self._enterprise_project_id = None
        self._tags = None
        self._optional_endpoint = None
        self._hpc_bw = None
        self._instance_id = None
        self._instance_type = None
        self._status_detail = None
        self._features = None
        self.discriminator = None

        if action_progress is not None:
            self.action_progress = action_progress
        if version is not None:
            self.version = version
        if avail_capacity is not None:
            self.avail_capacity = avail_capacity
        if availability_zone is not None:
            self.availability_zone = availability_zone
        if az_name is not None:
            self.az_name = az_name
        if created_at is not None:
            self.created_at = created_at
        if crypt_key_id is not None:
            self.crypt_key_id = crypt_key_id
        if expand_type is not None:
            self.expand_type = expand_type
        if export_location is not None:
            self.export_location = export_location
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if pay_model is not None:
            self.pay_model = pay_model
        if region is not None:
            self.region = region
        if security_group_id is not None:
            self.security_group_id = security_group_id
        if share_proto is not None:
            self.share_proto = share_proto
        if share_type is not None:
            self.share_type = share_type
        if size is not None:
            self.size = size
        if status is not None:
            self.status = status
        if sub_status is not None:
            self.sub_status = sub_status
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if tags is not None:
            self.tags = tags
        if optional_endpoint is not None:
            self.optional_endpoint = optional_endpoint
        if hpc_bw is not None:
            self.hpc_bw = hpc_bw
        if instance_id is not None:
            self.instance_id = instance_id
        if instance_type is not None:
            self.instance_type = instance_type
        if status_detail is not None:
            self.status_detail = status_detail
        if features is not None:
            self.features = features

    @property
    def action_progress(self):
        r"""Gets the action_progress of this ShowShareResponse.

        :return: The action_progress of this ShowShareResponse.
        :rtype: :class:`huaweicloudsdksfsturbo.v1.ActionProgress`
        """
        return self._action_progress

    @action_progress.setter
    def action_progress(self, action_progress):
        r"""Sets the action_progress of this ShowShareResponse.

        :param action_progress: The action_progress of this ShowShareResponse.
        :type action_progress: :class:`huaweicloudsdksfsturbo.v1.ActionProgress`
        """
        self._action_progress = action_progress

    @property
    def version(self):
        r"""Gets the version of this ShowShareResponse.

        SFS Turbo文件系统的版本号。

        :return: The version of this ShowShareResponse.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ShowShareResponse.

        SFS Turbo文件系统的版本号。

        :param version: The version of this ShowShareResponse.
        :type version: str
        """
        self._version = version

    @property
    def avail_capacity(self):
        r"""Gets the avail_capacity of this ShowShareResponse.

        SFS Turbo文件系统剩余容量，单位GB。

        :return: The avail_capacity of this ShowShareResponse.
        :rtype: str
        """
        return self._avail_capacity

    @avail_capacity.setter
    def avail_capacity(self, avail_capacity):
        r"""Sets the avail_capacity of this ShowShareResponse.

        SFS Turbo文件系统剩余容量，单位GB。

        :param avail_capacity: The avail_capacity of this ShowShareResponse.
        :type avail_capacity: str
        """
        self._avail_capacity = avail_capacity

    @property
    def availability_zone(self):
        r"""Gets the availability_zone of this ShowShareResponse.

        SFS Turbo文件系统所在可用区编码。

        :return: The availability_zone of this ShowShareResponse.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        r"""Sets the availability_zone of this ShowShareResponse.

        SFS Turbo文件系统所在可用区编码。

        :param availability_zone: The availability_zone of this ShowShareResponse.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def az_name(self):
        r"""Gets the az_name of this ShowShareResponse.

        SFS Turbo文件系统所在可用区名称。

        :return: The az_name of this ShowShareResponse.
        :rtype: str
        """
        return self._az_name

    @az_name.setter
    def az_name(self, az_name):
        r"""Sets the az_name of this ShowShareResponse.

        SFS Turbo文件系统所在可用区名称。

        :param az_name: The az_name of this ShowShareResponse.
        :type az_name: str
        """
        self._az_name = az_name

    @property
    def created_at(self):
        r"""Gets the created_at of this ShowShareResponse.

        创建时间。UTC时间，例如：2018-11-19T04:02:03

        :return: The created_at of this ShowShareResponse.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this ShowShareResponse.

        创建时间。UTC时间，例如：2018-11-19T04:02:03

        :param created_at: The created_at of this ShowShareResponse.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def crypt_key_id(self):
        r"""Gets the crypt_key_id of this ShowShareResponse.

        用户指定的加密密钥ID，非加密盘时不返回。

        :return: The crypt_key_id of this ShowShareResponse.
        :rtype: str
        """
        return self._crypt_key_id

    @crypt_key_id.setter
    def crypt_key_id(self, crypt_key_id):
        r"""Sets the crypt_key_id of this ShowShareResponse.

        用户指定的加密密钥ID，非加密盘时不返回。

        :param crypt_key_id: The crypt_key_id of this ShowShareResponse.
        :type crypt_key_id: str
        """
        self._crypt_key_id = crypt_key_id

    @property
    def expand_type(self):
        r"""Gets the expand_type of this ShowShareResponse.

        如果是增强版文件系统，该字段返回bandwidth；如果是20MB/s/TiB、40MB/s/TiB、125MB/s/TiB、250MB/s/TiB、500MB/s/TiB、1000MB/s/TiB，该字段返回hpc；否则不返回。

        :return: The expand_type of this ShowShareResponse.
        :rtype: str
        """
        return self._expand_type

    @expand_type.setter
    def expand_type(self, expand_type):
        r"""Sets the expand_type of this ShowShareResponse.

        如果是增强版文件系统，该字段返回bandwidth；如果是20MB/s/TiB、40MB/s/TiB、125MB/s/TiB、250MB/s/TiB、500MB/s/TiB、1000MB/s/TiB，该字段返回hpc；否则不返回。

        :param expand_type: The expand_type of this ShowShareResponse.
        :type expand_type: str
        """
        self._expand_type = expand_type

    @property
    def export_location(self):
        r"""Gets the export_location of this ShowShareResponse.

        SFS Turbo文件系统的挂载端点。例如\"192.168.0.90:/\"。如果文件系统正在创建，该字段不返回。

        :return: The export_location of this ShowShareResponse.
        :rtype: str
        """
        return self._export_location

    @export_location.setter
    def export_location(self, export_location):
        r"""Sets the export_location of this ShowShareResponse.

        SFS Turbo文件系统的挂载端点。例如\"192.168.0.90:/\"。如果文件系统正在创建，该字段不返回。

        :param export_location: The export_location of this ShowShareResponse.
        :type export_location: str
        """
        self._export_location = export_location

    @property
    def id(self):
        r"""Gets the id of this ShowShareResponse.

        SFS Turbo的文件系统ID。

        :return: The id of this ShowShareResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowShareResponse.

        SFS Turbo的文件系统ID。

        :param id: The id of this ShowShareResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ShowShareResponse.

        创建时指定的SFS Turbo文件系统名称。

        :return: The name of this ShowShareResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowShareResponse.

        创建时指定的SFS Turbo文件系统名称。

        :param name: The name of this ShowShareResponse.
        :type name: str
        """
        self._name = name

    @property
    def pay_model(self):
        r"""Gets the pay_model of this ShowShareResponse.

        SFS Turbo文件系统的计费模式。'0'代表按需付费，'1'代表包周期计费。如果文件系统正在创建，该字段不返回。

        :return: The pay_model of this ShowShareResponse.
        :rtype: str
        """
        return self._pay_model

    @pay_model.setter
    def pay_model(self, pay_model):
        r"""Sets the pay_model of this ShowShareResponse.

        SFS Turbo文件系统的计费模式。'0'代表按需付费，'1'代表包周期计费。如果文件系统正在创建，该字段不返回。

        :param pay_model: The pay_model of this ShowShareResponse.
        :type pay_model: str
        """
        self._pay_model = pay_model

    @property
    def region(self):
        r"""Gets the region of this ShowShareResponse.

        SFS Turbo文件系统所在区域。

        :return: The region of this ShowShareResponse.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this ShowShareResponse.

        SFS Turbo文件系统所在区域。

        :param region: The region of this ShowShareResponse.
        :type region: str
        """
        self._region = region

    @property
    def security_group_id(self):
        r"""Gets the security_group_id of this ShowShareResponse.

        用户指定的安全组ID。

        :return: The security_group_id of this ShowShareResponse.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        r"""Sets the security_group_id of this ShowShareResponse.

        用户指定的安全组ID。

        :param security_group_id: The security_group_id of this ShowShareResponse.
        :type security_group_id: str
        """
        self._security_group_id = security_group_id

    @property
    def share_proto(self):
        r"""Gets the share_proto of this ShowShareResponse.

        SFS Turbo文件系统的协议类型，当前为NFS或 CIFS。

        :return: The share_proto of this ShowShareResponse.
        :rtype: str
        """
        return self._share_proto

    @share_proto.setter
    def share_proto(self, share_proto):
        r"""Sets the share_proto of this ShowShareResponse.

        SFS Turbo文件系统的协议类型，当前为NFS或 CIFS。

        :param share_proto: The share_proto of this ShowShareResponse.
        :type share_proto: str
        """
        self._share_proto = share_proto

    @property
    def share_type(self):
        r"""Gets the share_type of this ShowShareResponse.

        SFS Turbo文件系统性能类型，包括“STANDARD”标准型和“PERFORMANCE”性能型。

        :return: The share_type of this ShowShareResponse.
        :rtype: str
        """
        return self._share_type

    @share_type.setter
    def share_type(self, share_type):
        r"""Sets the share_type of this ShowShareResponse.

        SFS Turbo文件系统性能类型，包括“STANDARD”标准型和“PERFORMANCE”性能型。

        :param share_type: The share_type of this ShowShareResponse.
        :type share_type: str
        """
        self._share_type = share_type

    @property
    def size(self):
        r"""Gets the size of this ShowShareResponse.

        SFS Turbo文件系统总容量，单位GB。

        :return: The size of this ShowShareResponse.
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this ShowShareResponse.

        SFS Turbo文件系统总容量，单位GB。

        :param size: The size of this ShowShareResponse.
        :type size: str
        """
        self._size = size

    @property
    def status(self):
        r"""Gets the status of this ShowShareResponse.

        SFS Turbo文件系统的状态。'100'表示创建中，'200'表示可用，'303'表示创建失败，'800'表示实例被冻结。

        :return: The status of this ShowShareResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowShareResponse.

        SFS Turbo文件系统的状态。'100'表示创建中，'200'表示可用，'303'表示创建失败，'800'表示实例被冻结。

        :param status: The status of this ShowShareResponse.
        :type status: str
        """
        self._status = status

    @property
    def sub_status(self):
        r"""Gets the sub_status of this ShowShareResponse.

        SFS Turbo文件系统的子状态。当用户未对文件系统有修改类操作时，该字段不返回。 '121'表示扩容中；'132'表示修改安全组中；'137'表示添加VPC中；'138'表示删除VPC中；'150'表示配置联动后端中；'151'表示删除联动后端配置中。 '221'表示扩容成功；'232'表示修改安全组成功；'237'表示添加VPC成功；'238'表示删除VPC成功；'250'表示配置联动后端成功；'251'表示删除联动后端配置成功。 '321'表示扩容失败；'332'表示修改安全组失败；'337'表示添加VPC失败；'338'表示删除VPC失败；'350'表示配置联动后端失败；'351'表示删除联动后端配置失败。

        :return: The sub_status of this ShowShareResponse.
        :rtype: str
        """
        return self._sub_status

    @sub_status.setter
    def sub_status(self, sub_status):
        r"""Sets the sub_status of this ShowShareResponse.

        SFS Turbo文件系统的子状态。当用户未对文件系统有修改类操作时，该字段不返回。 '121'表示扩容中；'132'表示修改安全组中；'137'表示添加VPC中；'138'表示删除VPC中；'150'表示配置联动后端中；'151'表示删除联动后端配置中。 '221'表示扩容成功；'232'表示修改安全组成功；'237'表示添加VPC成功；'238'表示删除VPC成功；'250'表示配置联动后端成功；'251'表示删除联动后端配置成功。 '321'表示扩容失败；'332'表示修改安全组失败；'337'表示添加VPC失败；'338'表示删除VPC失败；'350'表示配置联动后端失败；'351'表示删除联动后端配置失败。

        :param sub_status: The sub_status of this ShowShareResponse.
        :type sub_status: str
        """
        self._sub_status = sub_status

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this ShowShareResponse.

        用户指定的子网的网络ID。

        :return: The subnet_id of this ShowShareResponse.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this ShowShareResponse.

        用户指定的子网的网络ID。

        :param subnet_id: The subnet_id of this ShowShareResponse.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this ShowShareResponse.

        用户指定的VPC ID。

        :return: The vpc_id of this ShowShareResponse.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this ShowShareResponse.

        用户指定的VPC ID。

        :param vpc_id: The vpc_id of this ShowShareResponse.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ShowShareResponse.

        SFS Turbo文件系统绑定的企业项目ID。

        :return: The enterprise_project_id of this ShowShareResponse.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ShowShareResponse.

        SFS Turbo文件系统绑定的企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this ShowShareResponse.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def tags(self):
        r"""Gets the tags of this ShowShareResponse.

        tag标签的列表。

        :return: The tags of this ShowShareResponse.
        :rtype: list[:class:`huaweicloudsdksfsturbo.v1.ResourceTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ShowShareResponse.

        tag标签的列表。

        :param tags: The tags of this ShowShareResponse.
        :type tags: list[:class:`huaweicloudsdksfsturbo.v1.ResourceTag`]
        """
        self._tags = tags

    @property
    def optional_endpoint(self):
        r"""Gets the optional_endpoint of this ShowShareResponse.

        可选的挂载IP地址。上一代文件系统规格类型不返回该字段。

        :return: The optional_endpoint of this ShowShareResponse.
        :rtype: str
        """
        return self._optional_endpoint

    @optional_endpoint.setter
    def optional_endpoint(self, optional_endpoint):
        r"""Sets the optional_endpoint of this ShowShareResponse.

        可选的挂载IP地址。上一代文件系统规格类型不返回该字段。

        :param optional_endpoint: The optional_endpoint of this ShowShareResponse.
        :type optional_endpoint: str
        """
        self._optional_endpoint = optional_endpoint

    @property
    def hpc_bw(self):
        r"""Gets the hpc_bw of this ShowShareResponse.

        文件系统的带宽规格。 - \"20M\"表示20MB/s/TiB - \"40M\"表示40MB/s/TiB - \"125M\"表示125MB/s/TiB - \"250M\"表示250MB/s/TiB - \"500M\"表示500MB/s/TiB  - \"1000M\"表示1000MB/s/TiB  - \"2G\"、\"4G\"、\"8G\"、\"16G\"、\"24G\"、\"32G\"或\"48G\"表示HPC缓存型的带宽规格。 

        :return: The hpc_bw of this ShowShareResponse.
        :rtype: str
        """
        return self._hpc_bw

    @hpc_bw.setter
    def hpc_bw(self, hpc_bw):
        r"""Sets the hpc_bw of this ShowShareResponse.

        文件系统的带宽规格。 - \"20M\"表示20MB/s/TiB - \"40M\"表示40MB/s/TiB - \"125M\"表示125MB/s/TiB - \"250M\"表示250MB/s/TiB - \"500M\"表示500MB/s/TiB  - \"1000M\"表示1000MB/s/TiB  - \"2G\"、\"4G\"、\"8G\"、\"16G\"、\"24G\"、\"32G\"或\"48G\"表示HPC缓存型的带宽规格。 

        :param hpc_bw: The hpc_bw of this ShowShareResponse.
        :type hpc_bw: str
        """
        self._hpc_bw = hpc_bw

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ShowShareResponse.

        文件系统规格的节点id，为预留字段，不具备实际含义。

        :return: The instance_id of this ShowShareResponse.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ShowShareResponse.

        文件系统规格的节点id，为预留字段，不具备实际含义。

        :param instance_id: The instance_id of this ShowShareResponse.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def instance_type(self):
        r"""Gets the instance_type of this ShowShareResponse.

        文件系统规格的节点类型，为预留字段，不具备实际含义。

        :return: The instance_type of this ShowShareResponse.
        :rtype: str
        """
        return self._instance_type

    @instance_type.setter
    def instance_type(self, instance_type):
        r"""Sets the instance_type of this ShowShareResponse.

        文件系统规格的节点类型，为预留字段，不具备实际含义。

        :param instance_type: The instance_type of this ShowShareResponse.
        :type instance_type: str
        """
        self._instance_type = instance_type

    @property
    def status_detail(self):
        r"""Gets the status_detail of this ShowShareResponse.

        文件系统的请求ID，为预留字段，不具备实际含义。

        :return: The status_detail of this ShowShareResponse.
        :rtype: str
        """
        return self._status_detail

    @status_detail.setter
    def status_detail(self, status_detail):
        r"""Sets the status_detail of this ShowShareResponse.

        文件系统的请求ID，为预留字段，不具备实际含义。

        :param status_detail: The status_detail of this ShowShareResponse.
        :type status_detail: str
        """
        self._status_detail = status_detail

    @property
    def features(self):
        r"""Gets the features of this ShowShareResponse.

        :return: The features of this ShowShareResponse.
        :rtype: :class:`huaweicloudsdksfsturbo.v1.ShareInfoFeatures`
        """
        return self._features

    @features.setter
    def features(self, features):
        r"""Sets the features of this ShowShareResponse.

        :param features: The features of this ShowShareResponse.
        :type features: :class:`huaweicloudsdksfsturbo.v1.ShareInfoFeatures`
        """
        self._features = features

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
        if not isinstance(other, ShowShareResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
