# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PutTaskReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'type': 'str',
        'region_id': 'str',
        'region_name': 'str',
        'exist_server': 'bool',
        'migration_ip': 'str',
        'use_ipv6': 'bool',
        'use_public_ip': 'bool',
        'speed_limit': 'int',
        'project_name': 'str',
        'project_id': 'str',
        'enterprise_project': 'str',
        'image_disk_id': 'str',
        'vm_template_id': 'str',
        'target_disk_ids': 'str',
        'snapshot_ids': 'str',
        'cutovered_snapshot_ids': 'str',
        'target_server': 'TargetServer',
        'clone_server': 'CloneServer'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'region_id': 'region_id',
        'region_name': 'region_name',
        'exist_server': 'exist_server',
        'migration_ip': 'migration_ip',
        'use_ipv6': 'use_ipv6',
        'use_public_ip': 'use_public_ip',
        'speed_limit': 'speed_limit',
        'project_name': 'project_name',
        'project_id': 'project_id',
        'enterprise_project': 'enterprise_project',
        'image_disk_id': 'image_disk_id',
        'vm_template_id': 'vm_template_id',
        'target_disk_ids': 'target_disk_ids',
        'snapshot_ids': 'snapshot_ids',
        'cutovered_snapshot_ids': 'cutovered_snapshot_ids',
        'target_server': 'target_server',
        'clone_server': 'clone_server'
    }

    def __init__(self, name=None, type=None, region_id=None, region_name=None, exist_server=None, migration_ip=None, use_ipv6=None, use_public_ip=None, speed_limit=None, project_name=None, project_id=None, enterprise_project=None, image_disk_id=None, vm_template_id=None, target_disk_ids=None, snapshot_ids=None, cutovered_snapshot_ids=None, target_server=None, clone_server=None):
        r"""PutTaskReq

        The model defined in huaweicloud sdk

        :param name: 任务名称（用户自定义） 仅由中文字符、下划线、短横线、数字、英文大小写字母组成
        :type name: str
        :param type: 任务类型，创建时必选，更新时可选 MIGRATE_FILE:文件级迁移 MIGRATE_BLOCK:块级迁移
        :type type: str
        :param region_id: 目的端服务器的区域ID
        :type region_id: str
        :param region_name: 目的端服务器的区域名称
        :type region_name: str
        :param exist_server: 目的端服务器是否存在。true代表已有目的端服务器，false代表需要新建目的端服务器
        :type exist_server: bool
        :param migration_ip: 目的端服务器的IP地址。 公网迁移时请填写弹性IP地址 专线迁移时请填写私有IP地址 如果use_ipv6是true，则需要满足ipv6的格式，如果use_ipv6是false，则需要满足ipv4的格式
        :type migration_ip: str
        :param use_ipv6: 目的端服务器的IP地址是否使用ipv6
        :type use_ipv6: bool
        :param use_public_ip: 是否为公网
        :type use_public_ip: bool
        :param speed_limit: 限制迁移速率，单位：Mbps
        :type speed_limit: int
        :param project_name: 目的端服务器所在项目名称
        :type project_name: str
        :param project_id: 目的端服务器所在项目ID
        :type project_id: str
        :param enterprise_project: 企业项目ID
        :type enterprise_project: str
        :param image_disk_id: 目的端服务器镜像代理磁盘ID
        :type image_disk_id: str
        :param vm_template_id: 模板ID
        :type vm_template_id: str
        :param target_disk_ids: 目的端服务器磁盘ID数组，用空格分隔，单个id长度不超过255
        :type target_disk_ids: str
        :param snapshot_ids: 目的端的快照ID，id之间\&quot;;\&quot;分隔
        :type snapshot_ids: str
        :param cutovered_snapshot_ids: 割接的快照ID
        :type cutovered_snapshot_ids: str
        :param target_server: 
        :type target_server: :class:`huaweicloudsdksms.v3.TargetServer`
        :param clone_server: 
        :type clone_server: :class:`huaweicloudsdksms.v3.CloneServer`
        """
        
        

        self._name = None
        self._type = None
        self._region_id = None
        self._region_name = None
        self._exist_server = None
        self._migration_ip = None
        self._use_ipv6 = None
        self._use_public_ip = None
        self._speed_limit = None
        self._project_name = None
        self._project_id = None
        self._enterprise_project = None
        self._image_disk_id = None
        self._vm_template_id = None
        self._target_disk_ids = None
        self._snapshot_ids = None
        self._cutovered_snapshot_ids = None
        self._target_server = None
        self._clone_server = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if region_id is not None:
            self.region_id = region_id
        if region_name is not None:
            self.region_name = region_name
        if exist_server is not None:
            self.exist_server = exist_server
        if migration_ip is not None:
            self.migration_ip = migration_ip
        if use_ipv6 is not None:
            self.use_ipv6 = use_ipv6
        if use_public_ip is not None:
            self.use_public_ip = use_public_ip
        if speed_limit is not None:
            self.speed_limit = speed_limit
        if project_name is not None:
            self.project_name = project_name
        if project_id is not None:
            self.project_id = project_id
        if enterprise_project is not None:
            self.enterprise_project = enterprise_project
        if image_disk_id is not None:
            self.image_disk_id = image_disk_id
        if vm_template_id is not None:
            self.vm_template_id = vm_template_id
        if target_disk_ids is not None:
            self.target_disk_ids = target_disk_ids
        if snapshot_ids is not None:
            self.snapshot_ids = snapshot_ids
        if cutovered_snapshot_ids is not None:
            self.cutovered_snapshot_ids = cutovered_snapshot_ids
        if target_server is not None:
            self.target_server = target_server
        if clone_server is not None:
            self.clone_server = clone_server

    @property
    def name(self):
        r"""Gets the name of this PutTaskReq.

        任务名称（用户自定义） 仅由中文字符、下划线、短横线、数字、英文大小写字母组成

        :return: The name of this PutTaskReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this PutTaskReq.

        任务名称（用户自定义） 仅由中文字符、下划线、短横线、数字、英文大小写字母组成

        :param name: The name of this PutTaskReq.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this PutTaskReq.

        任务类型，创建时必选，更新时可选 MIGRATE_FILE:文件级迁移 MIGRATE_BLOCK:块级迁移

        :return: The type of this PutTaskReq.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this PutTaskReq.

        任务类型，创建时必选，更新时可选 MIGRATE_FILE:文件级迁移 MIGRATE_BLOCK:块级迁移

        :param type: The type of this PutTaskReq.
        :type type: str
        """
        self._type = type

    @property
    def region_id(self):
        r"""Gets the region_id of this PutTaskReq.

        目的端服务器的区域ID

        :return: The region_id of this PutTaskReq.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this PutTaskReq.

        目的端服务器的区域ID

        :param region_id: The region_id of this PutTaskReq.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def region_name(self):
        r"""Gets the region_name of this PutTaskReq.

        目的端服务器的区域名称

        :return: The region_name of this PutTaskReq.
        :rtype: str
        """
        return self._region_name

    @region_name.setter
    def region_name(self, region_name):
        r"""Sets the region_name of this PutTaskReq.

        目的端服务器的区域名称

        :param region_name: The region_name of this PutTaskReq.
        :type region_name: str
        """
        self._region_name = region_name

    @property
    def exist_server(self):
        r"""Gets the exist_server of this PutTaskReq.

        目的端服务器是否存在。true代表已有目的端服务器，false代表需要新建目的端服务器

        :return: The exist_server of this PutTaskReq.
        :rtype: bool
        """
        return self._exist_server

    @exist_server.setter
    def exist_server(self, exist_server):
        r"""Sets the exist_server of this PutTaskReq.

        目的端服务器是否存在。true代表已有目的端服务器，false代表需要新建目的端服务器

        :param exist_server: The exist_server of this PutTaskReq.
        :type exist_server: bool
        """
        self._exist_server = exist_server

    @property
    def migration_ip(self):
        r"""Gets the migration_ip of this PutTaskReq.

        目的端服务器的IP地址。 公网迁移时请填写弹性IP地址 专线迁移时请填写私有IP地址 如果use_ipv6是true，则需要满足ipv6的格式，如果use_ipv6是false，则需要满足ipv4的格式

        :return: The migration_ip of this PutTaskReq.
        :rtype: str
        """
        return self._migration_ip

    @migration_ip.setter
    def migration_ip(self, migration_ip):
        r"""Sets the migration_ip of this PutTaskReq.

        目的端服务器的IP地址。 公网迁移时请填写弹性IP地址 专线迁移时请填写私有IP地址 如果use_ipv6是true，则需要满足ipv6的格式，如果use_ipv6是false，则需要满足ipv4的格式

        :param migration_ip: The migration_ip of this PutTaskReq.
        :type migration_ip: str
        """
        self._migration_ip = migration_ip

    @property
    def use_ipv6(self):
        r"""Gets the use_ipv6 of this PutTaskReq.

        目的端服务器的IP地址是否使用ipv6

        :return: The use_ipv6 of this PutTaskReq.
        :rtype: bool
        """
        return self._use_ipv6

    @use_ipv6.setter
    def use_ipv6(self, use_ipv6):
        r"""Sets the use_ipv6 of this PutTaskReq.

        目的端服务器的IP地址是否使用ipv6

        :param use_ipv6: The use_ipv6 of this PutTaskReq.
        :type use_ipv6: bool
        """
        self._use_ipv6 = use_ipv6

    @property
    def use_public_ip(self):
        r"""Gets the use_public_ip of this PutTaskReq.

        是否为公网

        :return: The use_public_ip of this PutTaskReq.
        :rtype: bool
        """
        return self._use_public_ip

    @use_public_ip.setter
    def use_public_ip(self, use_public_ip):
        r"""Sets the use_public_ip of this PutTaskReq.

        是否为公网

        :param use_public_ip: The use_public_ip of this PutTaskReq.
        :type use_public_ip: bool
        """
        self._use_public_ip = use_public_ip

    @property
    def speed_limit(self):
        r"""Gets the speed_limit of this PutTaskReq.

        限制迁移速率，单位：Mbps

        :return: The speed_limit of this PutTaskReq.
        :rtype: int
        """
        return self._speed_limit

    @speed_limit.setter
    def speed_limit(self, speed_limit):
        r"""Sets the speed_limit of this PutTaskReq.

        限制迁移速率，单位：Mbps

        :param speed_limit: The speed_limit of this PutTaskReq.
        :type speed_limit: int
        """
        self._speed_limit = speed_limit

    @property
    def project_name(self):
        r"""Gets the project_name of this PutTaskReq.

        目的端服务器所在项目名称

        :return: The project_name of this PutTaskReq.
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        r"""Sets the project_name of this PutTaskReq.

        目的端服务器所在项目名称

        :param project_name: The project_name of this PutTaskReq.
        :type project_name: str
        """
        self._project_name = project_name

    @property
    def project_id(self):
        r"""Gets the project_id of this PutTaskReq.

        目的端服务器所在项目ID

        :return: The project_id of this PutTaskReq.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this PutTaskReq.

        目的端服务器所在项目ID

        :param project_id: The project_id of this PutTaskReq.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def enterprise_project(self):
        r"""Gets the enterprise_project of this PutTaskReq.

        企业项目ID

        :return: The enterprise_project of this PutTaskReq.
        :rtype: str
        """
        return self._enterprise_project

    @enterprise_project.setter
    def enterprise_project(self, enterprise_project):
        r"""Sets the enterprise_project of this PutTaskReq.

        企业项目ID

        :param enterprise_project: The enterprise_project of this PutTaskReq.
        :type enterprise_project: str
        """
        self._enterprise_project = enterprise_project

    @property
    def image_disk_id(self):
        r"""Gets the image_disk_id of this PutTaskReq.

        目的端服务器镜像代理磁盘ID

        :return: The image_disk_id of this PutTaskReq.
        :rtype: str
        """
        return self._image_disk_id

    @image_disk_id.setter
    def image_disk_id(self, image_disk_id):
        r"""Sets the image_disk_id of this PutTaskReq.

        目的端服务器镜像代理磁盘ID

        :param image_disk_id: The image_disk_id of this PutTaskReq.
        :type image_disk_id: str
        """
        self._image_disk_id = image_disk_id

    @property
    def vm_template_id(self):
        r"""Gets the vm_template_id of this PutTaskReq.

        模板ID

        :return: The vm_template_id of this PutTaskReq.
        :rtype: str
        """
        return self._vm_template_id

    @vm_template_id.setter
    def vm_template_id(self, vm_template_id):
        r"""Sets the vm_template_id of this PutTaskReq.

        模板ID

        :param vm_template_id: The vm_template_id of this PutTaskReq.
        :type vm_template_id: str
        """
        self._vm_template_id = vm_template_id

    @property
    def target_disk_ids(self):
        r"""Gets the target_disk_ids of this PutTaskReq.

        目的端服务器磁盘ID数组，用空格分隔，单个id长度不超过255

        :return: The target_disk_ids of this PutTaskReq.
        :rtype: str
        """
        return self._target_disk_ids

    @target_disk_ids.setter
    def target_disk_ids(self, target_disk_ids):
        r"""Sets the target_disk_ids of this PutTaskReq.

        目的端服务器磁盘ID数组，用空格分隔，单个id长度不超过255

        :param target_disk_ids: The target_disk_ids of this PutTaskReq.
        :type target_disk_ids: str
        """
        self._target_disk_ids = target_disk_ids

    @property
    def snapshot_ids(self):
        r"""Gets the snapshot_ids of this PutTaskReq.

        目的端的快照ID，id之间\";\"分隔

        :return: The snapshot_ids of this PutTaskReq.
        :rtype: str
        """
        return self._snapshot_ids

    @snapshot_ids.setter
    def snapshot_ids(self, snapshot_ids):
        r"""Sets the snapshot_ids of this PutTaskReq.

        目的端的快照ID，id之间\";\"分隔

        :param snapshot_ids: The snapshot_ids of this PutTaskReq.
        :type snapshot_ids: str
        """
        self._snapshot_ids = snapshot_ids

    @property
    def cutovered_snapshot_ids(self):
        r"""Gets the cutovered_snapshot_ids of this PutTaskReq.

        割接的快照ID

        :return: The cutovered_snapshot_ids of this PutTaskReq.
        :rtype: str
        """
        return self._cutovered_snapshot_ids

    @cutovered_snapshot_ids.setter
    def cutovered_snapshot_ids(self, cutovered_snapshot_ids):
        r"""Sets the cutovered_snapshot_ids of this PutTaskReq.

        割接的快照ID

        :param cutovered_snapshot_ids: The cutovered_snapshot_ids of this PutTaskReq.
        :type cutovered_snapshot_ids: str
        """
        self._cutovered_snapshot_ids = cutovered_snapshot_ids

    @property
    def target_server(self):
        r"""Gets the target_server of this PutTaskReq.

        :return: The target_server of this PutTaskReq.
        :rtype: :class:`huaweicloudsdksms.v3.TargetServer`
        """
        return self._target_server

    @target_server.setter
    def target_server(self, target_server):
        r"""Sets the target_server of this PutTaskReq.

        :param target_server: The target_server of this PutTaskReq.
        :type target_server: :class:`huaweicloudsdksms.v3.TargetServer`
        """
        self._target_server = target_server

    @property
    def clone_server(self):
        r"""Gets the clone_server of this PutTaskReq.

        :return: The clone_server of this PutTaskReq.
        :rtype: :class:`huaweicloudsdksms.v3.CloneServer`
        """
        return self._clone_server

    @clone_server.setter
    def clone_server(self, clone_server):
        r"""Sets the clone_server of this PutTaskReq.

        :param clone_server: The clone_server of this PutTaskReq.
        :type clone_server: :class:`huaweicloudsdksms.v3.CloneServer`
        """
        self._clone_server = clone_server

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
        if not isinstance(other, PutTaskReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
