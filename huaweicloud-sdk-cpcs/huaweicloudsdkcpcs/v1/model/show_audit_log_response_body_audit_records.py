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
        'status': 'str',
        'failure_message': 'str',
        'verification': 'str'
    }

    attribute_map = {
        'id': 'id',
        'tenant_id': 'tenant_id',
        'cluster_id': 'cluster_id',
        'cluster_type': 'cluster_type',
        'operation': 'operation',
        'time': 'time',
        'status': 'status',
        'failure_message': 'failure_message',
        'verification': 'verification'
    }

    def __init__(self, id=None, tenant_id=None, cluster_id=None, cluster_type=None, operation=None, time=None, status=None, failure_message=None, verification=None):
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
        :param status: 操作状态
        :type status: str
        :param failure_message: 操作失败消息
        :type failure_message: str
        :param verification: 操作验证信息
        :type verification: str
        """
        
        

        self._id = None
        self._tenant_id = None
        self._cluster_id = None
        self._cluster_type = None
        self._operation = None
        self._time = None
        self._status = None
        self._failure_message = None
        self._verification = None
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
        if status is not None:
            self.status = status
        if failure_message is not None:
            self.failure_message = failure_message
        if verification is not None:
            self.verification = verification

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
    def status(self):
        r"""Gets the status of this ShowAuditLogResponseBodyAuditRecords.

        操作状态

        :return: The status of this ShowAuditLogResponseBodyAuditRecords.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowAuditLogResponseBodyAuditRecords.

        操作状态

        :param status: The status of this ShowAuditLogResponseBodyAuditRecords.
        :type status: str
        """
        self._status = status

    @property
    def failure_message(self):
        r"""Gets the failure_message of this ShowAuditLogResponseBodyAuditRecords.

        操作失败消息

        :return: The failure_message of this ShowAuditLogResponseBodyAuditRecords.
        :rtype: str
        """
        return self._failure_message

    @failure_message.setter
    def failure_message(self, failure_message):
        r"""Sets the failure_message of this ShowAuditLogResponseBodyAuditRecords.

        操作失败消息

        :param failure_message: The failure_message of this ShowAuditLogResponseBodyAuditRecords.
        :type failure_message: str
        """
        self._failure_message = failure_message

    @property
    def verification(self):
        r"""Gets the verification of this ShowAuditLogResponseBodyAuditRecords.

        操作验证信息

        :return: The verification of this ShowAuditLogResponseBodyAuditRecords.
        :rtype: str
        """
        return self._verification

    @verification.setter
    def verification(self, verification):
        r"""Sets the verification of this ShowAuditLogResponseBodyAuditRecords.

        操作验证信息

        :param verification: The verification of this ShowAuditLogResponseBodyAuditRecords.
        :type verification: str
        """
        self._verification = verification

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
