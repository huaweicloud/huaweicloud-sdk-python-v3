# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListServersRspServers:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'created': 'str',
        'desktop_id': 'str',
        'desktop_product_id': 'str',
        'computer_name': 'str',
        'status': 'str',
        'tenant_id': 'str',
        'updated': 'str',
        'task_state': 'str',
        'image_id': 'str',
        'image_name': 'str',
        'vcpu': 'int',
        'memory': 'int',
        'ip_addresses': 'list[str]',
        'availability_zone': 'str',
        'process': 'int'
    }

    attribute_map = {
        'type': 'type',
        'created': 'created',
        'desktop_id': 'desktop_id',
        'desktop_product_id': 'desktop_product_id',
        'computer_name': 'computer_name',
        'status': 'status',
        'tenant_id': 'tenant_id',
        'updated': 'updated',
        'task_state': 'task_state',
        'image_id': 'image_id',
        'image_name': 'image_name',
        'vcpu': 'vcpu',
        'memory': 'memory',
        'ip_addresses': 'ip_addresses',
        'availability_zone': 'availability_zone',
        'process': 'process'
    }

    def __init__(self, type=None, created=None, desktop_id=None, desktop_product_id=None, computer_name=None, status=None, tenant_id=None, updated=None, task_state=None, image_id=None, image_name=None, vcpu=None, memory=None, ip_addresses=None, availability_zone=None, process=None):
        r"""ListServersRspServers

        The model defined in huaweicloud sdk

        :param type: 类型，render-desktop表示渲染桌面，wdh-desktop表示专属主机桌面。
        :type type: str
        :param created: 创建时间。
        :type created: str
        :param desktop_id: 桌面id。
        :type desktop_id: str
        :param desktop_product_id: 桌面套餐ID。
        :type desktop_product_id: str
        :param computer_name: 机器名称。
        :type computer_name: str
        :param status: 机器状态。
        :type status: str
        :param tenant_id: 租户id。
        :type tenant_id: str
        :param updated: 更新时间。
        :type updated: str
        :param task_state: 任务状态。
        :type task_state: str
        :param image_id: 镜像id。
        :type image_id: str
        :param image_name: 镜像名称。
        :type image_name: str
        :param vcpu: CPU核数。
        :type vcpu: int
        :param memory: 内存大小, 单位MB。
        :type memory: int
        :param ip_addresses: ip地址。
        :type ip_addresses: list[str]
        :param availability_zone: 区域。
        :type availability_zone: str
        :param process: 桌面任务进度， 取值范围0-100以及null，null表示该桌面无任务，0-100表明该任务进度的百分比。
        :type process: int
        """
        
        

        self._type = None
        self._created = None
        self._desktop_id = None
        self._desktop_product_id = None
        self._computer_name = None
        self._status = None
        self._tenant_id = None
        self._updated = None
        self._task_state = None
        self._image_id = None
        self._image_name = None
        self._vcpu = None
        self._memory = None
        self._ip_addresses = None
        self._availability_zone = None
        self._process = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if created is not None:
            self.created = created
        if desktop_id is not None:
            self.desktop_id = desktop_id
        if desktop_product_id is not None:
            self.desktop_product_id = desktop_product_id
        if computer_name is not None:
            self.computer_name = computer_name
        if status is not None:
            self.status = status
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if updated is not None:
            self.updated = updated
        if task_state is not None:
            self.task_state = task_state
        if image_id is not None:
            self.image_id = image_id
        if image_name is not None:
            self.image_name = image_name
        if vcpu is not None:
            self.vcpu = vcpu
        if memory is not None:
            self.memory = memory
        if ip_addresses is not None:
            self.ip_addresses = ip_addresses
        if availability_zone is not None:
            self.availability_zone = availability_zone
        if process is not None:
            self.process = process

    @property
    def type(self):
        r"""Gets the type of this ListServersRspServers.

        类型，render-desktop表示渲染桌面，wdh-desktop表示专属主机桌面。

        :return: The type of this ListServersRspServers.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListServersRspServers.

        类型，render-desktop表示渲染桌面，wdh-desktop表示专属主机桌面。

        :param type: The type of this ListServersRspServers.
        :type type: str
        """
        self._type = type

    @property
    def created(self):
        r"""Gets the created of this ListServersRspServers.

        创建时间。

        :return: The created of this ListServersRspServers.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        r"""Sets the created of this ListServersRspServers.

        创建时间。

        :param created: The created of this ListServersRspServers.
        :type created: str
        """
        self._created = created

    @property
    def desktop_id(self):
        r"""Gets the desktop_id of this ListServersRspServers.

        桌面id。

        :return: The desktop_id of this ListServersRspServers.
        :rtype: str
        """
        return self._desktop_id

    @desktop_id.setter
    def desktop_id(self, desktop_id):
        r"""Sets the desktop_id of this ListServersRspServers.

        桌面id。

        :param desktop_id: The desktop_id of this ListServersRspServers.
        :type desktop_id: str
        """
        self._desktop_id = desktop_id

    @property
    def desktop_product_id(self):
        r"""Gets the desktop_product_id of this ListServersRspServers.

        桌面套餐ID。

        :return: The desktop_product_id of this ListServersRspServers.
        :rtype: str
        """
        return self._desktop_product_id

    @desktop_product_id.setter
    def desktop_product_id(self, desktop_product_id):
        r"""Sets the desktop_product_id of this ListServersRspServers.

        桌面套餐ID。

        :param desktop_product_id: The desktop_product_id of this ListServersRspServers.
        :type desktop_product_id: str
        """
        self._desktop_product_id = desktop_product_id

    @property
    def computer_name(self):
        r"""Gets the computer_name of this ListServersRspServers.

        机器名称。

        :return: The computer_name of this ListServersRspServers.
        :rtype: str
        """
        return self._computer_name

    @computer_name.setter
    def computer_name(self, computer_name):
        r"""Sets the computer_name of this ListServersRspServers.

        机器名称。

        :param computer_name: The computer_name of this ListServersRspServers.
        :type computer_name: str
        """
        self._computer_name = computer_name

    @property
    def status(self):
        r"""Gets the status of this ListServersRspServers.

        机器状态。

        :return: The status of this ListServersRspServers.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListServersRspServers.

        机器状态。

        :param status: The status of this ListServersRspServers.
        :type status: str
        """
        self._status = status

    @property
    def tenant_id(self):
        r"""Gets the tenant_id of this ListServersRspServers.

        租户id。

        :return: The tenant_id of this ListServersRspServers.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        r"""Sets the tenant_id of this ListServersRspServers.

        租户id。

        :param tenant_id: The tenant_id of this ListServersRspServers.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def updated(self):
        r"""Gets the updated of this ListServersRspServers.

        更新时间。

        :return: The updated of this ListServersRspServers.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        r"""Sets the updated of this ListServersRspServers.

        更新时间。

        :param updated: The updated of this ListServersRspServers.
        :type updated: str
        """
        self._updated = updated

    @property
    def task_state(self):
        r"""Gets the task_state of this ListServersRspServers.

        任务状态。

        :return: The task_state of this ListServersRspServers.
        :rtype: str
        """
        return self._task_state

    @task_state.setter
    def task_state(self, task_state):
        r"""Sets the task_state of this ListServersRspServers.

        任务状态。

        :param task_state: The task_state of this ListServersRspServers.
        :type task_state: str
        """
        self._task_state = task_state

    @property
    def image_id(self):
        r"""Gets the image_id of this ListServersRspServers.

        镜像id。

        :return: The image_id of this ListServersRspServers.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this ListServersRspServers.

        镜像id。

        :param image_id: The image_id of this ListServersRspServers.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def image_name(self):
        r"""Gets the image_name of this ListServersRspServers.

        镜像名称。

        :return: The image_name of this ListServersRspServers.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        r"""Sets the image_name of this ListServersRspServers.

        镜像名称。

        :param image_name: The image_name of this ListServersRspServers.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def vcpu(self):
        r"""Gets the vcpu of this ListServersRspServers.

        CPU核数。

        :return: The vcpu of this ListServersRspServers.
        :rtype: int
        """
        return self._vcpu

    @vcpu.setter
    def vcpu(self, vcpu):
        r"""Sets the vcpu of this ListServersRspServers.

        CPU核数。

        :param vcpu: The vcpu of this ListServersRspServers.
        :type vcpu: int
        """
        self._vcpu = vcpu

    @property
    def memory(self):
        r"""Gets the memory of this ListServersRspServers.

        内存大小, 单位MB。

        :return: The memory of this ListServersRspServers.
        :rtype: int
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        r"""Sets the memory of this ListServersRspServers.

        内存大小, 单位MB。

        :param memory: The memory of this ListServersRspServers.
        :type memory: int
        """
        self._memory = memory

    @property
    def ip_addresses(self):
        r"""Gets the ip_addresses of this ListServersRspServers.

        ip地址。

        :return: The ip_addresses of this ListServersRspServers.
        :rtype: list[str]
        """
        return self._ip_addresses

    @ip_addresses.setter
    def ip_addresses(self, ip_addresses):
        r"""Sets the ip_addresses of this ListServersRspServers.

        ip地址。

        :param ip_addresses: The ip_addresses of this ListServersRspServers.
        :type ip_addresses: list[str]
        """
        self._ip_addresses = ip_addresses

    @property
    def availability_zone(self):
        r"""Gets the availability_zone of this ListServersRspServers.

        区域。

        :return: The availability_zone of this ListServersRspServers.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        r"""Sets the availability_zone of this ListServersRspServers.

        区域。

        :param availability_zone: The availability_zone of this ListServersRspServers.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def process(self):
        r"""Gets the process of this ListServersRspServers.

        桌面任务进度， 取值范围0-100以及null，null表示该桌面无任务，0-100表明该任务进度的百分比。

        :return: The process of this ListServersRspServers.
        :rtype: int
        """
        return self._process

    @process.setter
    def process(self, process):
        r"""Sets the process of this ListServersRspServers.

        桌面任务进度， 取值范围0-100以及null，null表示该桌面无任务，0-100表明该任务进度的百分比。

        :param process: The process of this ListServersRspServers.
        :type process: int
        """
        self._process = process

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
        if not isinstance(other, ListServersRspServers):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
