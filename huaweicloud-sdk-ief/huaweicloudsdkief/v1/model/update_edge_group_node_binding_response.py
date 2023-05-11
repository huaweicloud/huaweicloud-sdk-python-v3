# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateEdgeGroupNodeBindingResponse(SdkResponse):

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
        'description': 'str',
        'created_at': 'str',
        'updated_at': 'str',
        'project_id': 'str',
        'iam_role': 'str',
        'cpu': 'int',
        'memory': 'int',
        'gpu_num': 'int',
        'nodes': 'list[EdgeNodeResp]',
        'deployments': 'list[GroupDeployment]',
        'attributes': 'list[Attributes]',
        'tags': 'list[Attributes]',
        'success_node_add': 'list[str]',
        'success_node_del': 'list[str]',
        'failed_node_add': 'list[str]',
        'failed_node_del': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'project_id': 'project_id',
        'iam_role': 'iam_role',
        'cpu': 'cpu',
        'memory': 'memory',
        'gpu_num': 'gpu_num',
        'nodes': 'nodes',
        'deployments': 'deployments',
        'attributes': 'attributes',
        'tags': 'tags',
        'success_node_add': 'success_node_add',
        'success_node_del': 'success_node_del',
        'failed_node_add': 'failed_node_add',
        'failed_node_del': 'failed_node_del'
    }

    def __init__(self, id=None, name=None, description=None, created_at=None, updated_at=None, project_id=None, iam_role=None, cpu=None, memory=None, gpu_num=None, nodes=None, deployments=None, attributes=None, tags=None, success_node_add=None, success_node_del=None, failed_node_add=None, failed_node_del=None):
        """UpdateEdgeGroupNodeBindingResponse

        The model defined in huaweicloud sdk

        :param id: 边缘节点组ID
        :type id: str
        :param name: 边缘节点组名称，小写英文字母、数字、中划线，以小写字母或数字开头，最大长度为32个字符，不能为空
        :type name: str
        :param description: 描述
        :type description: str
        :param created_at: 创建时间
        :type created_at: str
        :param updated_at: 更新时间
        :type updated_at: str
        :param project_id: 边缘节点组所属的项目ID
        :type project_id: str
        :param iam_role: 边缘节点组所属账号的IAM权限，没有铂金版权限的账号无法使用节点组功能
        :type iam_role: str
        :param cpu: 边缘节点组CPU总数，为边缘节点组所绑定的边缘节点的CPU数目之和
        :type cpu: int
        :param memory: 边缘节点组内存总数，为边缘节点组所绑定的边缘节点的内存之和
        :type memory: int
        :param gpu_num: 边缘节点组GPU总数，为边缘节点组所绑定的边缘节点的GPU数目之和
        :type gpu_num: int
        :param nodes: 绑定的边缘节点详情
        :type nodes: list[:class:`huaweicloudsdkief.v1.EdgeNodeResp`]
        :param deployments: 绑定的边缘应用详情
        :type deployments: list[:class:`huaweicloudsdkief.v1.GroupDeployment`]
        :param attributes: 属性
        :type attributes: list[:class:`huaweicloudsdkief.v1.Attributes`]
        :param tags: 标签
        :type tags: list[:class:`huaweicloudsdkief.v1.Attributes`]
        :param success_node_add: 绑定操作成功的节点ID列表
        :type success_node_add: list[str]
        :param success_node_del: 解绑操作成功的节点ID列表
        :type success_node_del: list[str]
        :param failed_node_add: 绑定操作失败的节点ID列表
        :type failed_node_add: list[str]
        :param failed_node_del: 解绑操作失败的节点ID列表
        :type failed_node_del: list[str]
        """
        
        super(UpdateEdgeGroupNodeBindingResponse, self).__init__()

        self._id = None
        self._name = None
        self._description = None
        self._created_at = None
        self._updated_at = None
        self._project_id = None
        self._iam_role = None
        self._cpu = None
        self._memory = None
        self._gpu_num = None
        self._nodes = None
        self._deployments = None
        self._attributes = None
        self._tags = None
        self._success_node_add = None
        self._success_node_del = None
        self._failed_node_add = None
        self._failed_node_del = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if project_id is not None:
            self.project_id = project_id
        if iam_role is not None:
            self.iam_role = iam_role
        if cpu is not None:
            self.cpu = cpu
        if memory is not None:
            self.memory = memory
        if gpu_num is not None:
            self.gpu_num = gpu_num
        if nodes is not None:
            self.nodes = nodes
        if deployments is not None:
            self.deployments = deployments
        if attributes is not None:
            self.attributes = attributes
        if tags is not None:
            self.tags = tags
        if success_node_add is not None:
            self.success_node_add = success_node_add
        if success_node_del is not None:
            self.success_node_del = success_node_del
        if failed_node_add is not None:
            self.failed_node_add = failed_node_add
        if failed_node_del is not None:
            self.failed_node_del = failed_node_del

    @property
    def id(self):
        """Gets the id of this UpdateEdgeGroupNodeBindingResponse.

        边缘节点组ID

        :return: The id of this UpdateEdgeGroupNodeBindingResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UpdateEdgeGroupNodeBindingResponse.

        边缘节点组ID

        :param id: The id of this UpdateEdgeGroupNodeBindingResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this UpdateEdgeGroupNodeBindingResponse.

        边缘节点组名称，小写英文字母、数字、中划线，以小写字母或数字开头，最大长度为32个字符，不能为空

        :return: The name of this UpdateEdgeGroupNodeBindingResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateEdgeGroupNodeBindingResponse.

        边缘节点组名称，小写英文字母、数字、中划线，以小写字母或数字开头，最大长度为32个字符，不能为空

        :param name: The name of this UpdateEdgeGroupNodeBindingResponse.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this UpdateEdgeGroupNodeBindingResponse.

        描述

        :return: The description of this UpdateEdgeGroupNodeBindingResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateEdgeGroupNodeBindingResponse.

        描述

        :param description: The description of this UpdateEdgeGroupNodeBindingResponse.
        :type description: str
        """
        self._description = description

    @property
    def created_at(self):
        """Gets the created_at of this UpdateEdgeGroupNodeBindingResponse.

        创建时间

        :return: The created_at of this UpdateEdgeGroupNodeBindingResponse.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this UpdateEdgeGroupNodeBindingResponse.

        创建时间

        :param created_at: The created_at of this UpdateEdgeGroupNodeBindingResponse.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this UpdateEdgeGroupNodeBindingResponse.

        更新时间

        :return: The updated_at of this UpdateEdgeGroupNodeBindingResponse.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this UpdateEdgeGroupNodeBindingResponse.

        更新时间

        :param updated_at: The updated_at of this UpdateEdgeGroupNodeBindingResponse.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def project_id(self):
        """Gets the project_id of this UpdateEdgeGroupNodeBindingResponse.

        边缘节点组所属的项目ID

        :return: The project_id of this UpdateEdgeGroupNodeBindingResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this UpdateEdgeGroupNodeBindingResponse.

        边缘节点组所属的项目ID

        :param project_id: The project_id of this UpdateEdgeGroupNodeBindingResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def iam_role(self):
        """Gets the iam_role of this UpdateEdgeGroupNodeBindingResponse.

        边缘节点组所属账号的IAM权限，没有铂金版权限的账号无法使用节点组功能

        :return: The iam_role of this UpdateEdgeGroupNodeBindingResponse.
        :rtype: str
        """
        return self._iam_role

    @iam_role.setter
    def iam_role(self, iam_role):
        """Sets the iam_role of this UpdateEdgeGroupNodeBindingResponse.

        边缘节点组所属账号的IAM权限，没有铂金版权限的账号无法使用节点组功能

        :param iam_role: The iam_role of this UpdateEdgeGroupNodeBindingResponse.
        :type iam_role: str
        """
        self._iam_role = iam_role

    @property
    def cpu(self):
        """Gets the cpu of this UpdateEdgeGroupNodeBindingResponse.

        边缘节点组CPU总数，为边缘节点组所绑定的边缘节点的CPU数目之和

        :return: The cpu of this UpdateEdgeGroupNodeBindingResponse.
        :rtype: int
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        """Sets the cpu of this UpdateEdgeGroupNodeBindingResponse.

        边缘节点组CPU总数，为边缘节点组所绑定的边缘节点的CPU数目之和

        :param cpu: The cpu of this UpdateEdgeGroupNodeBindingResponse.
        :type cpu: int
        """
        self._cpu = cpu

    @property
    def memory(self):
        """Gets the memory of this UpdateEdgeGroupNodeBindingResponse.

        边缘节点组内存总数，为边缘节点组所绑定的边缘节点的内存之和

        :return: The memory of this UpdateEdgeGroupNodeBindingResponse.
        :rtype: int
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        """Sets the memory of this UpdateEdgeGroupNodeBindingResponse.

        边缘节点组内存总数，为边缘节点组所绑定的边缘节点的内存之和

        :param memory: The memory of this UpdateEdgeGroupNodeBindingResponse.
        :type memory: int
        """
        self._memory = memory

    @property
    def gpu_num(self):
        """Gets the gpu_num of this UpdateEdgeGroupNodeBindingResponse.

        边缘节点组GPU总数，为边缘节点组所绑定的边缘节点的GPU数目之和

        :return: The gpu_num of this UpdateEdgeGroupNodeBindingResponse.
        :rtype: int
        """
        return self._gpu_num

    @gpu_num.setter
    def gpu_num(self, gpu_num):
        """Sets the gpu_num of this UpdateEdgeGroupNodeBindingResponse.

        边缘节点组GPU总数，为边缘节点组所绑定的边缘节点的GPU数目之和

        :param gpu_num: The gpu_num of this UpdateEdgeGroupNodeBindingResponse.
        :type gpu_num: int
        """
        self._gpu_num = gpu_num

    @property
    def nodes(self):
        """Gets the nodes of this UpdateEdgeGroupNodeBindingResponse.

        绑定的边缘节点详情

        :return: The nodes of this UpdateEdgeGroupNodeBindingResponse.
        :rtype: list[:class:`huaweicloudsdkief.v1.EdgeNodeResp`]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        """Sets the nodes of this UpdateEdgeGroupNodeBindingResponse.

        绑定的边缘节点详情

        :param nodes: The nodes of this UpdateEdgeGroupNodeBindingResponse.
        :type nodes: list[:class:`huaweicloudsdkief.v1.EdgeNodeResp`]
        """
        self._nodes = nodes

    @property
    def deployments(self):
        """Gets the deployments of this UpdateEdgeGroupNodeBindingResponse.

        绑定的边缘应用详情

        :return: The deployments of this UpdateEdgeGroupNodeBindingResponse.
        :rtype: list[:class:`huaweicloudsdkief.v1.GroupDeployment`]
        """
        return self._deployments

    @deployments.setter
    def deployments(self, deployments):
        """Sets the deployments of this UpdateEdgeGroupNodeBindingResponse.

        绑定的边缘应用详情

        :param deployments: The deployments of this UpdateEdgeGroupNodeBindingResponse.
        :type deployments: list[:class:`huaweicloudsdkief.v1.GroupDeployment`]
        """
        self._deployments = deployments

    @property
    def attributes(self):
        """Gets the attributes of this UpdateEdgeGroupNodeBindingResponse.

        属性

        :return: The attributes of this UpdateEdgeGroupNodeBindingResponse.
        :rtype: list[:class:`huaweicloudsdkief.v1.Attributes`]
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this UpdateEdgeGroupNodeBindingResponse.

        属性

        :param attributes: The attributes of this UpdateEdgeGroupNodeBindingResponse.
        :type attributes: list[:class:`huaweicloudsdkief.v1.Attributes`]
        """
        self._attributes = attributes

    @property
    def tags(self):
        """Gets the tags of this UpdateEdgeGroupNodeBindingResponse.

        标签

        :return: The tags of this UpdateEdgeGroupNodeBindingResponse.
        :rtype: list[:class:`huaweicloudsdkief.v1.Attributes`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this UpdateEdgeGroupNodeBindingResponse.

        标签

        :param tags: The tags of this UpdateEdgeGroupNodeBindingResponse.
        :type tags: list[:class:`huaweicloudsdkief.v1.Attributes`]
        """
        self._tags = tags

    @property
    def success_node_add(self):
        """Gets the success_node_add of this UpdateEdgeGroupNodeBindingResponse.

        绑定操作成功的节点ID列表

        :return: The success_node_add of this UpdateEdgeGroupNodeBindingResponse.
        :rtype: list[str]
        """
        return self._success_node_add

    @success_node_add.setter
    def success_node_add(self, success_node_add):
        """Sets the success_node_add of this UpdateEdgeGroupNodeBindingResponse.

        绑定操作成功的节点ID列表

        :param success_node_add: The success_node_add of this UpdateEdgeGroupNodeBindingResponse.
        :type success_node_add: list[str]
        """
        self._success_node_add = success_node_add

    @property
    def success_node_del(self):
        """Gets the success_node_del of this UpdateEdgeGroupNodeBindingResponse.

        解绑操作成功的节点ID列表

        :return: The success_node_del of this UpdateEdgeGroupNodeBindingResponse.
        :rtype: list[str]
        """
        return self._success_node_del

    @success_node_del.setter
    def success_node_del(self, success_node_del):
        """Sets the success_node_del of this UpdateEdgeGroupNodeBindingResponse.

        解绑操作成功的节点ID列表

        :param success_node_del: The success_node_del of this UpdateEdgeGroupNodeBindingResponse.
        :type success_node_del: list[str]
        """
        self._success_node_del = success_node_del

    @property
    def failed_node_add(self):
        """Gets the failed_node_add of this UpdateEdgeGroupNodeBindingResponse.

        绑定操作失败的节点ID列表

        :return: The failed_node_add of this UpdateEdgeGroupNodeBindingResponse.
        :rtype: list[str]
        """
        return self._failed_node_add

    @failed_node_add.setter
    def failed_node_add(self, failed_node_add):
        """Sets the failed_node_add of this UpdateEdgeGroupNodeBindingResponse.

        绑定操作失败的节点ID列表

        :param failed_node_add: The failed_node_add of this UpdateEdgeGroupNodeBindingResponse.
        :type failed_node_add: list[str]
        """
        self._failed_node_add = failed_node_add

    @property
    def failed_node_del(self):
        """Gets the failed_node_del of this UpdateEdgeGroupNodeBindingResponse.

        解绑操作失败的节点ID列表

        :return: The failed_node_del of this UpdateEdgeGroupNodeBindingResponse.
        :rtype: list[str]
        """
        return self._failed_node_del

    @failed_node_del.setter
    def failed_node_del(self, failed_node_del):
        """Sets the failed_node_del of this UpdateEdgeGroupNodeBindingResponse.

        解绑操作失败的节点ID列表

        :param failed_node_del: The failed_node_del of this UpdateEdgeGroupNodeBindingResponse.
        :type failed_node_del: list[str]
        """
        self._failed_node_del = failed_node_del

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
        if not isinstance(other, UpdateEdgeGroupNodeBindingResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
