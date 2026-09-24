# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConnectionItem:

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
        'domain_id': 'str',
        'project_id': 'str',
        'status': 'str',
        'created_at': 'str',
        'updated_at': 'str',
        'protected': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'domain_id': 'domain_id',
        'project_id': 'project_id',
        'status': 'status',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'protected': 'protected'
    }

    def __init__(self, id=None, domain_id=None, project_id=None, status=None, created_at=None, updated_at=None, protected=None):
        r"""ConnectionItem

        The model defined in huaweicloud sdk

        :param id: VPC终端节点ID
        :type id: str
        :param domain_id: VPC终端节点所属的租户ID
        :type domain_id: str
        :param project_id: VPC终端节点所属的项目ID
        :type project_id: str
        :param status: VPC终端节点的连接状态 取值范围: - pendingAcceptance:待接受 - creating:创建中 - accepted:已接受 - rejected:已拒绝 - failed:失败 - deleting:删除中
        :type status: str
        :param created_at: VPC终端节点的创建时间。采用UTC时间格式，格式为：YYYY-MM-DDTHH:MM:SSZ
        :type created_at: str
        :param updated_at: VPC终端节点的更新时间。采用UTC时间格式，格式为：YYYY-MM-DDTHH:MM:SSZ
        :type updated_at: str
        :param protected: 是否为保护内网访问连接；如果为true则不允许添加或者移除
        :type protected: bool
        """
        
        

        self._id = None
        self._domain_id = None
        self._project_id = None
        self._status = None
        self._created_at = None
        self._updated_at = None
        self._protected = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if domain_id is not None:
            self.domain_id = domain_id
        if project_id is not None:
            self.project_id = project_id
        if status is not None:
            self.status = status
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if protected is not None:
            self.protected = protected

    @property
    def id(self):
        r"""Gets the id of this ConnectionItem.

        VPC终端节点ID

        :return: The id of this ConnectionItem.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ConnectionItem.

        VPC终端节点ID

        :param id: The id of this ConnectionItem.
        :type id: str
        """
        self._id = id

    @property
    def domain_id(self):
        r"""Gets the domain_id of this ConnectionItem.

        VPC终端节点所属的租户ID

        :return: The domain_id of this ConnectionItem.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this ConnectionItem.

        VPC终端节点所属的租户ID

        :param domain_id: The domain_id of this ConnectionItem.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def project_id(self):
        r"""Gets the project_id of this ConnectionItem.

        VPC终端节点所属的项目ID

        :return: The project_id of this ConnectionItem.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ConnectionItem.

        VPC终端节点所属的项目ID

        :param project_id: The project_id of this ConnectionItem.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def status(self):
        r"""Gets the status of this ConnectionItem.

        VPC终端节点的连接状态 取值范围: - pendingAcceptance:待接受 - creating:创建中 - accepted:已接受 - rejected:已拒绝 - failed:失败 - deleting:删除中

        :return: The status of this ConnectionItem.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ConnectionItem.

        VPC终端节点的连接状态 取值范围: - pendingAcceptance:待接受 - creating:创建中 - accepted:已接受 - rejected:已拒绝 - failed:失败 - deleting:删除中

        :param status: The status of this ConnectionItem.
        :type status: str
        """
        self._status = status

    @property
    def created_at(self):
        r"""Gets the created_at of this ConnectionItem.

        VPC终端节点的创建时间。采用UTC时间格式，格式为：YYYY-MM-DDTHH:MM:SSZ

        :return: The created_at of this ConnectionItem.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this ConnectionItem.

        VPC终端节点的创建时间。采用UTC时间格式，格式为：YYYY-MM-DDTHH:MM:SSZ

        :param created_at: The created_at of this ConnectionItem.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this ConnectionItem.

        VPC终端节点的更新时间。采用UTC时间格式，格式为：YYYY-MM-DDTHH:MM:SSZ

        :return: The updated_at of this ConnectionItem.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this ConnectionItem.

        VPC终端节点的更新时间。采用UTC时间格式，格式为：YYYY-MM-DDTHH:MM:SSZ

        :param updated_at: The updated_at of this ConnectionItem.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def protected(self):
        r"""Gets the protected of this ConnectionItem.

        是否为保护内网访问连接；如果为true则不允许添加或者移除

        :return: The protected of this ConnectionItem.
        :rtype: bool
        """
        return self._protected

    @protected.setter
    def protected(self, protected):
        r"""Sets the protected of this ConnectionItem.

        是否为保护内网访问连接；如果为true则不允许添加或者移除

        :param protected: The protected of this ConnectionItem.
        :type protected: bool
        """
        self._protected = protected

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
        if not isinstance(other, ConnectionItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
