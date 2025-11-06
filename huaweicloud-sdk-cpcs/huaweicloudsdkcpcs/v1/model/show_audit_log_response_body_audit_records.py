# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAuditLogResponseBodyAuditRecords:

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
        'tenant_id': 'str',
        'cluster_id': 'str',
        'cluster_type': 'str',
        'operation': 'str',
        'time': 'int',
        'operate_status': 'int',
        'operate_message': 'str',
        'audit_status': 'int'
    }

    attribute_map = {
        'id': 'id',
        'tenant_id': 'tenant_id',
        'cluster_id': 'cluster_id',
        'cluster_type': 'cluster_type',
        'operation': 'operation',
        'time': 'time',
        'operate_status': 'operate_status',
        'operate_message': 'operate_message',
        'audit_status': 'audit_status'
    }

    def __init__(self, id=None, tenant_id=None, cluster_id=None, cluster_type=None, operation=None, time=None, operate_status=None, operate_message=None, audit_status=None):
        r"""ShowAuditLogResponseBodyAuditRecords

        The model defined in huaweicloud sdk

        :param id: 日志ID
        :type id: str
        :param tenant_id: 租户ID
        :type tenant_id: str
        :param cluster_id: 集群ID
        :type cluster_id: str
        :param cluster_type: 集群类型
        :type cluster_type: str
        :param operation: 操作
        :type operation: str
        :param time: 时间
        :type time: int
        :param operate_status: 操作状态
        :type operate_status: int
        :param operate_message: 操作结果消息
        :type operate_message: str
        :param audit_status: 审计状态
        :type audit_status: int
        """
        
        

        self._id = None
        self._tenant_id = None
        self._cluster_id = None
        self._cluster_type = None
        self._operation = None
        self._time = None
        self._operate_status = None
        self._operate_message = None
        self._audit_status = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if cluster_type is not None:
            self.cluster_type = cluster_type
        if operation is not None:
            self.operation = operation
        if time is not None:
            self.time = time
        if operate_status is not None:
            self.operate_status = operate_status
        if operate_message is not None:
            self.operate_message = operate_message
        if audit_status is not None:
            self.audit_status = audit_status

    @property
    def id(self):
        r"""Gets the id of this ShowAuditLogResponseBodyAuditRecords.

        日志ID

        :return: The id of this ShowAuditLogResponseBodyAuditRecords.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowAuditLogResponseBodyAuditRecords.

        日志ID

        :param id: The id of this ShowAuditLogResponseBodyAuditRecords.
        :type id: str
        """
        self._id = id

    @property
    def tenant_id(self):
        r"""Gets the tenant_id of this ShowAuditLogResponseBodyAuditRecords.

        租户ID

        :return: The tenant_id of this ShowAuditLogResponseBodyAuditRecords.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        r"""Sets the tenant_id of this ShowAuditLogResponseBodyAuditRecords.

        租户ID

        :param tenant_id: The tenant_id of this ShowAuditLogResponseBodyAuditRecords.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this ShowAuditLogResponseBodyAuditRecords.

        集群ID

        :return: The cluster_id of this ShowAuditLogResponseBodyAuditRecords.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this ShowAuditLogResponseBodyAuditRecords.

        集群ID

        :param cluster_id: The cluster_id of this ShowAuditLogResponseBodyAuditRecords.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def cluster_type(self):
        r"""Gets the cluster_type of this ShowAuditLogResponseBodyAuditRecords.

        集群类型

        :return: The cluster_type of this ShowAuditLogResponseBodyAuditRecords.
        :rtype: str
        """
        return self._cluster_type

    @cluster_type.setter
    def cluster_type(self, cluster_type):
        r"""Sets the cluster_type of this ShowAuditLogResponseBodyAuditRecords.

        集群类型

        :param cluster_type: The cluster_type of this ShowAuditLogResponseBodyAuditRecords.
        :type cluster_type: str
        """
        self._cluster_type = cluster_type

    @property
    def operation(self):
        r"""Gets the operation of this ShowAuditLogResponseBodyAuditRecords.

        操作

        :return: The operation of this ShowAuditLogResponseBodyAuditRecords.
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        r"""Sets the operation of this ShowAuditLogResponseBodyAuditRecords.

        操作

        :param operation: The operation of this ShowAuditLogResponseBodyAuditRecords.
        :type operation: str
        """
        self._operation = operation

    @property
    def time(self):
        r"""Gets the time of this ShowAuditLogResponseBodyAuditRecords.

        时间

        :return: The time of this ShowAuditLogResponseBodyAuditRecords.
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        r"""Sets the time of this ShowAuditLogResponseBodyAuditRecords.

        时间

        :param time: The time of this ShowAuditLogResponseBodyAuditRecords.
        :type time: int
        """
        self._time = time

    @property
    def operate_status(self):
        r"""Gets the operate_status of this ShowAuditLogResponseBodyAuditRecords.

        操作状态

        :return: The operate_status of this ShowAuditLogResponseBodyAuditRecords.
        :rtype: int
        """
        return self._operate_status

    @operate_status.setter
    def operate_status(self, operate_status):
        r"""Sets the operate_status of this ShowAuditLogResponseBodyAuditRecords.

        操作状态

        :param operate_status: The operate_status of this ShowAuditLogResponseBodyAuditRecords.
        :type operate_status: int
        """
        self._operate_status = operate_status

    @property
    def operate_message(self):
        r"""Gets the operate_message of this ShowAuditLogResponseBodyAuditRecords.

        操作结果消息

        :return: The operate_message of this ShowAuditLogResponseBodyAuditRecords.
        :rtype: str
        """
        return self._operate_message

    @operate_message.setter
    def operate_message(self, operate_message):
        r"""Sets the operate_message of this ShowAuditLogResponseBodyAuditRecords.

        操作结果消息

        :param operate_message: The operate_message of this ShowAuditLogResponseBodyAuditRecords.
        :type operate_message: str
        """
        self._operate_message = operate_message

    @property
    def audit_status(self):
        r"""Gets the audit_status of this ShowAuditLogResponseBodyAuditRecords.

        审计状态

        :return: The audit_status of this ShowAuditLogResponseBodyAuditRecords.
        :rtype: int
        """
        return self._audit_status

    @audit_status.setter
    def audit_status(self, audit_status):
        r"""Sets the audit_status of this ShowAuditLogResponseBodyAuditRecords.

        审计状态

        :param audit_status: The audit_status of this ShowAuditLogResponseBodyAuditRecords.
        :type audit_status: int
        """
        self._audit_status = audit_status

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
        if not isinstance(other, ShowAuditLogResponseBodyAuditRecords):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
