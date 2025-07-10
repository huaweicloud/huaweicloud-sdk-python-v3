# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SimpleDesktopInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain_id': 'str',
        'project_id': 'str',
        'desktop_id': 'str',
        'computer_name': 'str',
        'os_host_name': 'str',
        'created': 'str',
        'ip_address': 'str',
        'user_name': 'str',
        'attach_user_infos': 'list[AttachInstancesUserInfo]',
        'user_group': 'str',
        'sid': 'str',
        'ou_name': 'str',
        'enterprise_project_id': 'str',
        'tags': 'list[Tag]',
        'in_maintenance_mode': 'bool',
        'share_resource_sku': 'str',
        'desktop_type': 'str',
        'subnet_id': 'str',
        'bill_resource_id': 'str',
        'status': 'str',
        'task_status': 'str'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'project_id': 'project_id',
        'desktop_id': 'desktop_id',
        'computer_name': 'computer_name',
        'os_host_name': 'os_host_name',
        'created': 'created',
        'ip_address': 'ip_address',
        'user_name': 'user_name',
        'attach_user_infos': 'attach_user_infos',
        'user_group': 'user_group',
        'sid': 'sid',
        'ou_name': 'ou_name',
        'enterprise_project_id': 'enterprise_project_id',
        'tags': 'tags',
        'in_maintenance_mode': 'in_maintenance_mode',
        'share_resource_sku': 'share_resource_sku',
        'desktop_type': 'desktop_type',
        'subnet_id': 'subnet_id',
        'bill_resource_id': 'bill_resource_id',
        'status': 'status',
        'task_status': 'task_status'
    }

    def __init__(self, domain_id=None, project_id=None, desktop_id=None, computer_name=None, os_host_name=None, created=None, ip_address=None, user_name=None, attach_user_infos=None, user_group=None, sid=None, ou_name=None, enterprise_project_id=None, tags=None, in_maintenance_mode=None, share_resource_sku=None, desktop_type=None, subnet_id=None, bill_resource_id=None, status=None, task_status=None):
        r"""SimpleDesktopInfo

        The model defined in huaweicloud sdk

        :param domain_id: domainId。
        :type domain_id: str
        :param project_id: 项目id。
        :type project_id: str
        :param desktop_id: 桌面ID。
        :type desktop_id: str
        :param computer_name: 桌面名。
        :type computer_name: str
        :param os_host_name: 系统计算机名。
        :type os_host_name: str
        :param created: 创建时间。
        :type created: str
        :param ip_address: 桌面ip地址。
        :type ip_address: str
        :param user_name: 用户名。
        :type user_name: str
        :param attach_user_infos: 桌面已分配的用户信息列表。
        :type attach_user_infos: list[:class:`huaweicloudsdkworkspace.v2.AttachInstancesUserInfo`]
        :param user_group: 权限组。
        :type user_group: str
        :param sid: 桌面的SID信息。
        :type sid: str
        :param ou_name: ou名称。
        :type ou_name: str
        :param enterprise_project_id: 企业项目ID。
        :type enterprise_project_id: str
        :param tags: 标签列表。
        :type tags: list[:class:`huaweicloudsdkworkspace.v2.Tag`]
        :param in_maintenance_mode: 是否处于管理员维护模式。
        :type in_maintenance_mode: bool
        :param share_resource_sku: 桌面协同资源SKU码。
        :type share_resource_sku: str
        :param desktop_type: 桌面类型。
        :type desktop_type: str
        :param subnet_id: 桌面的子网ID。
        :type subnet_id: str
        :param bill_resource_id: 桌面计费资源ID。
        :type bill_resource_id: str
        :param status: 桌面的运行状态。
        :type status: str
        :param task_status: 桌面的任务状态。
        :type task_status: str
        """
        
        

        self._domain_id = None
        self._project_id = None
        self._desktop_id = None
        self._computer_name = None
        self._os_host_name = None
        self._created = None
        self._ip_address = None
        self._user_name = None
        self._attach_user_infos = None
        self._user_group = None
        self._sid = None
        self._ou_name = None
        self._enterprise_project_id = None
        self._tags = None
        self._in_maintenance_mode = None
        self._share_resource_sku = None
        self._desktop_type = None
        self._subnet_id = None
        self._bill_resource_id = None
        self._status = None
        self._task_status = None
        self.discriminator = None

        if domain_id is not None:
            self.domain_id = domain_id
        if project_id is not None:
            self.project_id = project_id
        if desktop_id is not None:
            self.desktop_id = desktop_id
        if computer_name is not None:
            self.computer_name = computer_name
        if os_host_name is not None:
            self.os_host_name = os_host_name
        if created is not None:
            self.created = created
        if ip_address is not None:
            self.ip_address = ip_address
        if user_name is not None:
            self.user_name = user_name
        if attach_user_infos is not None:
            self.attach_user_infos = attach_user_infos
        if user_group is not None:
            self.user_group = user_group
        if sid is not None:
            self.sid = sid
        if ou_name is not None:
            self.ou_name = ou_name
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if tags is not None:
            self.tags = tags
        if in_maintenance_mode is not None:
            self.in_maintenance_mode = in_maintenance_mode
        if share_resource_sku is not None:
            self.share_resource_sku = share_resource_sku
        if desktop_type is not None:
            self.desktop_type = desktop_type
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if bill_resource_id is not None:
            self.bill_resource_id = bill_resource_id
        if status is not None:
            self.status = status
        if task_status is not None:
            self.task_status = task_status

    @property
    def domain_id(self):
        r"""Gets the domain_id of this SimpleDesktopInfo.

        domainId。

        :return: The domain_id of this SimpleDesktopInfo.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this SimpleDesktopInfo.

        domainId。

        :param domain_id: The domain_id of this SimpleDesktopInfo.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def project_id(self):
        r"""Gets the project_id of this SimpleDesktopInfo.

        项目id。

        :return: The project_id of this SimpleDesktopInfo.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this SimpleDesktopInfo.

        项目id。

        :param project_id: The project_id of this SimpleDesktopInfo.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def desktop_id(self):
        r"""Gets the desktop_id of this SimpleDesktopInfo.

        桌面ID。

        :return: The desktop_id of this SimpleDesktopInfo.
        :rtype: str
        """
        return self._desktop_id

    @desktop_id.setter
    def desktop_id(self, desktop_id):
        r"""Sets the desktop_id of this SimpleDesktopInfo.

        桌面ID。

        :param desktop_id: The desktop_id of this SimpleDesktopInfo.
        :type desktop_id: str
        """
        self._desktop_id = desktop_id

    @property
    def computer_name(self):
        r"""Gets the computer_name of this SimpleDesktopInfo.

        桌面名。

        :return: The computer_name of this SimpleDesktopInfo.
        :rtype: str
        """
        return self._computer_name

    @computer_name.setter
    def computer_name(self, computer_name):
        r"""Sets the computer_name of this SimpleDesktopInfo.

        桌面名。

        :param computer_name: The computer_name of this SimpleDesktopInfo.
        :type computer_name: str
        """
        self._computer_name = computer_name

    @property
    def os_host_name(self):
        r"""Gets the os_host_name of this SimpleDesktopInfo.

        系统计算机名。

        :return: The os_host_name of this SimpleDesktopInfo.
        :rtype: str
        """
        return self._os_host_name

    @os_host_name.setter
    def os_host_name(self, os_host_name):
        r"""Sets the os_host_name of this SimpleDesktopInfo.

        系统计算机名。

        :param os_host_name: The os_host_name of this SimpleDesktopInfo.
        :type os_host_name: str
        """
        self._os_host_name = os_host_name

    @property
    def created(self):
        r"""Gets the created of this SimpleDesktopInfo.

        创建时间。

        :return: The created of this SimpleDesktopInfo.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        r"""Sets the created of this SimpleDesktopInfo.

        创建时间。

        :param created: The created of this SimpleDesktopInfo.
        :type created: str
        """
        self._created = created

    @property
    def ip_address(self):
        r"""Gets the ip_address of this SimpleDesktopInfo.

        桌面ip地址。

        :return: The ip_address of this SimpleDesktopInfo.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        r"""Sets the ip_address of this SimpleDesktopInfo.

        桌面ip地址。

        :param ip_address: The ip_address of this SimpleDesktopInfo.
        :type ip_address: str
        """
        self._ip_address = ip_address

    @property
    def user_name(self):
        r"""Gets the user_name of this SimpleDesktopInfo.

        用户名。

        :return: The user_name of this SimpleDesktopInfo.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this SimpleDesktopInfo.

        用户名。

        :param user_name: The user_name of this SimpleDesktopInfo.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def attach_user_infos(self):
        r"""Gets the attach_user_infos of this SimpleDesktopInfo.

        桌面已分配的用户信息列表。

        :return: The attach_user_infos of this SimpleDesktopInfo.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.AttachInstancesUserInfo`]
        """
        return self._attach_user_infos

    @attach_user_infos.setter
    def attach_user_infos(self, attach_user_infos):
        r"""Sets the attach_user_infos of this SimpleDesktopInfo.

        桌面已分配的用户信息列表。

        :param attach_user_infos: The attach_user_infos of this SimpleDesktopInfo.
        :type attach_user_infos: list[:class:`huaweicloudsdkworkspace.v2.AttachInstancesUserInfo`]
        """
        self._attach_user_infos = attach_user_infos

    @property
    def user_group(self):
        r"""Gets the user_group of this SimpleDesktopInfo.

        权限组。

        :return: The user_group of this SimpleDesktopInfo.
        :rtype: str
        """
        return self._user_group

    @user_group.setter
    def user_group(self, user_group):
        r"""Sets the user_group of this SimpleDesktopInfo.

        权限组。

        :param user_group: The user_group of this SimpleDesktopInfo.
        :type user_group: str
        """
        self._user_group = user_group

    @property
    def sid(self):
        r"""Gets the sid of this SimpleDesktopInfo.

        桌面的SID信息。

        :return: The sid of this SimpleDesktopInfo.
        :rtype: str
        """
        return self._sid

    @sid.setter
    def sid(self, sid):
        r"""Sets the sid of this SimpleDesktopInfo.

        桌面的SID信息。

        :param sid: The sid of this SimpleDesktopInfo.
        :type sid: str
        """
        self._sid = sid

    @property
    def ou_name(self):
        r"""Gets the ou_name of this SimpleDesktopInfo.

        ou名称。

        :return: The ou_name of this SimpleDesktopInfo.
        :rtype: str
        """
        return self._ou_name

    @ou_name.setter
    def ou_name(self, ou_name):
        r"""Sets the ou_name of this SimpleDesktopInfo.

        ou名称。

        :param ou_name: The ou_name of this SimpleDesktopInfo.
        :type ou_name: str
        """
        self._ou_name = ou_name

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this SimpleDesktopInfo.

        企业项目ID。

        :return: The enterprise_project_id of this SimpleDesktopInfo.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this SimpleDesktopInfo.

        企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this SimpleDesktopInfo.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def tags(self):
        r"""Gets the tags of this SimpleDesktopInfo.

        标签列表。

        :return: The tags of this SimpleDesktopInfo.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this SimpleDesktopInfo.

        标签列表。

        :param tags: The tags of this SimpleDesktopInfo.
        :type tags: list[:class:`huaweicloudsdkworkspace.v2.Tag`]
        """
        self._tags = tags

    @property
    def in_maintenance_mode(self):
        r"""Gets the in_maintenance_mode of this SimpleDesktopInfo.

        是否处于管理员维护模式。

        :return: The in_maintenance_mode of this SimpleDesktopInfo.
        :rtype: bool
        """
        return self._in_maintenance_mode

    @in_maintenance_mode.setter
    def in_maintenance_mode(self, in_maintenance_mode):
        r"""Sets the in_maintenance_mode of this SimpleDesktopInfo.

        是否处于管理员维护模式。

        :param in_maintenance_mode: The in_maintenance_mode of this SimpleDesktopInfo.
        :type in_maintenance_mode: bool
        """
        self._in_maintenance_mode = in_maintenance_mode

    @property
    def share_resource_sku(self):
        r"""Gets the share_resource_sku of this SimpleDesktopInfo.

        桌面协同资源SKU码。

        :return: The share_resource_sku of this SimpleDesktopInfo.
        :rtype: str
        """
        return self._share_resource_sku

    @share_resource_sku.setter
    def share_resource_sku(self, share_resource_sku):
        r"""Sets the share_resource_sku of this SimpleDesktopInfo.

        桌面协同资源SKU码。

        :param share_resource_sku: The share_resource_sku of this SimpleDesktopInfo.
        :type share_resource_sku: str
        """
        self._share_resource_sku = share_resource_sku

    @property
    def desktop_type(self):
        r"""Gets the desktop_type of this SimpleDesktopInfo.

        桌面类型。

        :return: The desktop_type of this SimpleDesktopInfo.
        :rtype: str
        """
        return self._desktop_type

    @desktop_type.setter
    def desktop_type(self, desktop_type):
        r"""Sets the desktop_type of this SimpleDesktopInfo.

        桌面类型。

        :param desktop_type: The desktop_type of this SimpleDesktopInfo.
        :type desktop_type: str
        """
        self._desktop_type = desktop_type

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this SimpleDesktopInfo.

        桌面的子网ID。

        :return: The subnet_id of this SimpleDesktopInfo.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this SimpleDesktopInfo.

        桌面的子网ID。

        :param subnet_id: The subnet_id of this SimpleDesktopInfo.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def bill_resource_id(self):
        r"""Gets the bill_resource_id of this SimpleDesktopInfo.

        桌面计费资源ID。

        :return: The bill_resource_id of this SimpleDesktopInfo.
        :rtype: str
        """
        return self._bill_resource_id

    @bill_resource_id.setter
    def bill_resource_id(self, bill_resource_id):
        r"""Sets the bill_resource_id of this SimpleDesktopInfo.

        桌面计费资源ID。

        :param bill_resource_id: The bill_resource_id of this SimpleDesktopInfo.
        :type bill_resource_id: str
        """
        self._bill_resource_id = bill_resource_id

    @property
    def status(self):
        r"""Gets the status of this SimpleDesktopInfo.

        桌面的运行状态。

        :return: The status of this SimpleDesktopInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this SimpleDesktopInfo.

        桌面的运行状态。

        :param status: The status of this SimpleDesktopInfo.
        :type status: str
        """
        self._status = status

    @property
    def task_status(self):
        r"""Gets the task_status of this SimpleDesktopInfo.

        桌面的任务状态。

        :return: The task_status of this SimpleDesktopInfo.
        :rtype: str
        """
        return self._task_status

    @task_status.setter
    def task_status(self, task_status):
        r"""Sets the task_status of this SimpleDesktopInfo.

        桌面的任务状态。

        :param task_status: The task_status of this SimpleDesktopInfo.
        :type task_status: str
        """
        self._task_status = task_status

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
        if not isinstance(other, SimpleDesktopInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
