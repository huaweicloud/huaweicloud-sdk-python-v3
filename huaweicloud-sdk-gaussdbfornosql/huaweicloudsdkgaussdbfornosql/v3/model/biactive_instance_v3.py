# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BiactiveInstanceV3:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'status': 'str',
        'actions': 'list[str]',
        'project_id': 'str',
        'project_name': 'str',
        'region_code': 'str',
        'node_num': 'int',
        'vcpus': 'str',
        'ram': 'str',
        'disk_size': 'str',
        'used_disk_size': 'str',
        'cidr': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'status': 'status',
        'actions': 'actions',
        'project_id': 'project_id',
        'project_name': 'project_name',
        'region_code': 'region_code',
        'node_num': 'node_num',
        'vcpus': 'vcpus',
        'ram': 'ram',
        'disk_size': 'disk_size',
        'used_disk_size': 'used_disk_size',
        'cidr': 'cidr'
    }

    def __init__(self, id=None, name=None, status=None, actions=None, project_id=None, project_name=None, region_code=None, node_num=None, vcpus=None, ram=None, disk_size=None, used_disk_size=None, cidr=None):
        r"""BiactiveInstanceV3

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 实例ID。 **取值范围：** 不涉及。
        :type id: str
        :param name: **参数解释：** 实例名称。 **取值范围：** 不涉及。
        :type name: str
        :param status: **参数解释：** 实例状态。 **取值范围：** 不涉及。
        :type status: str
        :param actions: **参数解释：** 实例当前支持的操作。 **取值范围：** 不涉及。
        :type actions: list[str]
        :param project_id: **参数解释：** 项目ID。 **取值范围：** 不涉及。
        :type project_id: str
        :param project_name: **参数解释：** 项目名称。 **取值范围：** 不涉及。
        :type project_name: str
        :param region_code: **参数解释：** 区域。 **取值范围：** 不涉及。
        :type region_code: str
        :param node_num: **参数解释：** 节点数量。 **取值范围：** 不涉及。
        :type node_num: int
        :param vcpus: **参数解释：** vCPU数量。 **取值范围：** 不涉及。
        :type vcpus: str
        :param ram: **参数解释：** 内存大小，单位GB。 **取值范围：** 不涉及。
        :type ram: str
        :param disk_size: **参数解释：** 磁盘大小，单位GB。 **取值范围：** 不涉及。
        :type disk_size: str
        :param used_disk_size: **参数解释：** 已使用磁盘大小，单位GB。 **取值范围：** 不涉及。
        :type used_disk_size: str
        :param cidr: **参数解释：** VPC CIDR。 **取值范围：** 不涉及。
        :type cidr: str
        """
        
        

        self._id = None
        self._name = None
        self._status = None
        self._actions = None
        self._project_id = None
        self._project_name = None
        self._region_code = None
        self._node_num = None
        self._vcpus = None
        self._ram = None
        self._disk_size = None
        self._used_disk_size = None
        self._cidr = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if actions is not None:
            self.actions = actions
        if project_id is not None:
            self.project_id = project_id
        if project_name is not None:
            self.project_name = project_name
        if region_code is not None:
            self.region_code = region_code
        if node_num is not None:
            self.node_num = node_num
        if vcpus is not None:
            self.vcpus = vcpus
        if ram is not None:
            self.ram = ram
        if disk_size is not None:
            self.disk_size = disk_size
        if used_disk_size is not None:
            self.used_disk_size = used_disk_size
        if cidr is not None:
            self.cidr = cidr

    @property
    def id(self):
        r"""Gets the id of this BiactiveInstanceV3.

        **参数解释：** 实例ID。 **取值范围：** 不涉及。

        :return: The id of this BiactiveInstanceV3.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this BiactiveInstanceV3.

        **参数解释：** 实例ID。 **取值范围：** 不涉及。

        :param id: The id of this BiactiveInstanceV3.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this BiactiveInstanceV3.

        **参数解释：** 实例名称。 **取值范围：** 不涉及。

        :return: The name of this BiactiveInstanceV3.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this BiactiveInstanceV3.

        **参数解释：** 实例名称。 **取值范围：** 不涉及。

        :param name: The name of this BiactiveInstanceV3.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        r"""Gets the status of this BiactiveInstanceV3.

        **参数解释：** 实例状态。 **取值范围：** 不涉及。

        :return: The status of this BiactiveInstanceV3.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this BiactiveInstanceV3.

        **参数解释：** 实例状态。 **取值范围：** 不涉及。

        :param status: The status of this BiactiveInstanceV3.
        :type status: str
        """
        self._status = status

    @property
    def actions(self):
        r"""Gets the actions of this BiactiveInstanceV3.

        **参数解释：** 实例当前支持的操作。 **取值范围：** 不涉及。

        :return: The actions of this BiactiveInstanceV3.
        :rtype: list[str]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        r"""Sets the actions of this BiactiveInstanceV3.

        **参数解释：** 实例当前支持的操作。 **取值范围：** 不涉及。

        :param actions: The actions of this BiactiveInstanceV3.
        :type actions: list[str]
        """
        self._actions = actions

    @property
    def project_id(self):
        r"""Gets the project_id of this BiactiveInstanceV3.

        **参数解释：** 项目ID。 **取值范围：** 不涉及。

        :return: The project_id of this BiactiveInstanceV3.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this BiactiveInstanceV3.

        **参数解释：** 项目ID。 **取值范围：** 不涉及。

        :param project_id: The project_id of this BiactiveInstanceV3.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def project_name(self):
        r"""Gets the project_name of this BiactiveInstanceV3.

        **参数解释：** 项目名称。 **取值范围：** 不涉及。

        :return: The project_name of this BiactiveInstanceV3.
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        r"""Sets the project_name of this BiactiveInstanceV3.

        **参数解释：** 项目名称。 **取值范围：** 不涉及。

        :param project_name: The project_name of this BiactiveInstanceV3.
        :type project_name: str
        """
        self._project_name = project_name

    @property
    def region_code(self):
        r"""Gets the region_code of this BiactiveInstanceV3.

        **参数解释：** 区域。 **取值范围：** 不涉及。

        :return: The region_code of this BiactiveInstanceV3.
        :rtype: str
        """
        return self._region_code

    @region_code.setter
    def region_code(self, region_code):
        r"""Sets the region_code of this BiactiveInstanceV3.

        **参数解释：** 区域。 **取值范围：** 不涉及。

        :param region_code: The region_code of this BiactiveInstanceV3.
        :type region_code: str
        """
        self._region_code = region_code

    @property
    def node_num(self):
        r"""Gets the node_num of this BiactiveInstanceV3.

        **参数解释：** 节点数量。 **取值范围：** 不涉及。

        :return: The node_num of this BiactiveInstanceV3.
        :rtype: int
        """
        return self._node_num

    @node_num.setter
    def node_num(self, node_num):
        r"""Sets the node_num of this BiactiveInstanceV3.

        **参数解释：** 节点数量。 **取值范围：** 不涉及。

        :param node_num: The node_num of this BiactiveInstanceV3.
        :type node_num: int
        """
        self._node_num = node_num

    @property
    def vcpus(self):
        r"""Gets the vcpus of this BiactiveInstanceV3.

        **参数解释：** vCPU数量。 **取值范围：** 不涉及。

        :return: The vcpus of this BiactiveInstanceV3.
        :rtype: str
        """
        return self._vcpus

    @vcpus.setter
    def vcpus(self, vcpus):
        r"""Sets the vcpus of this BiactiveInstanceV3.

        **参数解释：** vCPU数量。 **取值范围：** 不涉及。

        :param vcpus: The vcpus of this BiactiveInstanceV3.
        :type vcpus: str
        """
        self._vcpus = vcpus

    @property
    def ram(self):
        r"""Gets the ram of this BiactiveInstanceV3.

        **参数解释：** 内存大小，单位GB。 **取值范围：** 不涉及。

        :return: The ram of this BiactiveInstanceV3.
        :rtype: str
        """
        return self._ram

    @ram.setter
    def ram(self, ram):
        r"""Sets the ram of this BiactiveInstanceV3.

        **参数解释：** 内存大小，单位GB。 **取值范围：** 不涉及。

        :param ram: The ram of this BiactiveInstanceV3.
        :type ram: str
        """
        self._ram = ram

    @property
    def disk_size(self):
        r"""Gets the disk_size of this BiactiveInstanceV3.

        **参数解释：** 磁盘大小，单位GB。 **取值范围：** 不涉及。

        :return: The disk_size of this BiactiveInstanceV3.
        :rtype: str
        """
        return self._disk_size

    @disk_size.setter
    def disk_size(self, disk_size):
        r"""Sets the disk_size of this BiactiveInstanceV3.

        **参数解释：** 磁盘大小，单位GB。 **取值范围：** 不涉及。

        :param disk_size: The disk_size of this BiactiveInstanceV3.
        :type disk_size: str
        """
        self._disk_size = disk_size

    @property
    def used_disk_size(self):
        r"""Gets the used_disk_size of this BiactiveInstanceV3.

        **参数解释：** 已使用磁盘大小，单位GB。 **取值范围：** 不涉及。

        :return: The used_disk_size of this BiactiveInstanceV3.
        :rtype: str
        """
        return self._used_disk_size

    @used_disk_size.setter
    def used_disk_size(self, used_disk_size):
        r"""Sets the used_disk_size of this BiactiveInstanceV3.

        **参数解释：** 已使用磁盘大小，单位GB。 **取值范围：** 不涉及。

        :param used_disk_size: The used_disk_size of this BiactiveInstanceV3.
        :type used_disk_size: str
        """
        self._used_disk_size = used_disk_size

    @property
    def cidr(self):
        r"""Gets the cidr of this BiactiveInstanceV3.

        **参数解释：** VPC CIDR。 **取值范围：** 不涉及。

        :return: The cidr of this BiactiveInstanceV3.
        :rtype: str
        """
        return self._cidr

    @cidr.setter
    def cidr(self, cidr):
        r"""Sets the cidr of this BiactiveInstanceV3.

        **参数解释：** VPC CIDR。 **取值范围：** 不涉及。

        :param cidr: The cidr of this BiactiveInstanceV3.
        :type cidr: str
        """
        self._cidr = cidr

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
        if not isinstance(other, BiactiveInstanceV3):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
