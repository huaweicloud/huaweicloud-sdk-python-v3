# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RecordDetailInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'operation_id': 'str',
        'resource_type': 'str',
        'operation_type': 'str',
        'domain_id': 'str',
        'project_id': 'str',
        'blockchain_id': 'str',
        'blockchain_name': 'str',
        'cluster_info': 'OprecordCluster',
        'operation_process': 'dict(str, ProcessInfo)',
        'record_time': 'int',
        'operation_status': 'str',
        'message': 'list[str]',
        'desc': 'str'
    }

    attribute_map = {
        'operation_id': 'operation_id',
        'resource_type': 'resource_type',
        'operation_type': 'operation_type',
        'domain_id': 'domain_id',
        'project_id': 'project_id',
        'blockchain_id': 'blockchain_id',
        'blockchain_name': 'blockchain_name',
        'cluster_info': 'cluster_info',
        'operation_process': 'operation_process',
        'record_time': 'record_time',
        'operation_status': 'operation_status',
        'message': 'message',
        'desc': 'desc'
    }

    def __init__(self, operation_id=None, resource_type=None, operation_type=None, domain_id=None, project_id=None, blockchain_id=None, blockchain_name=None, cluster_info=None, operation_process=None, record_time=None, operation_status=None, message=None, desc=None):
        """RecordDetailInfo

        The model defined in huaweicloud sdk

        :param operation_id: 操作记录ID
        :type operation_id: str
        :param resource_type: 资源类型
        :type resource_type: str
        :param operation_type: 操作类型
        :type operation_type: str
        :param domain_id: 租户ID
        :type domain_id: str
        :param project_id: 项目ID
        :type project_id: str
        :param blockchain_id: 区块链ID
        :type blockchain_id: str
        :param blockchain_name: 区块链名称
        :type blockchain_name: str
        :param cluster_info: 
        :type cluster_info: :class:`huaweicloudsdkbcs.v2.OprecordCluster`
        :param operation_process: 操作流程，key为流程名，value为流程信息
        :type operation_process: dict(str, ProcessInfo)
        :param record_time: 记录更新时间
        :type record_time: int
        :param operation_status: 操作状态
        :type operation_status: str
        :param message: 操作过程信息记录
        :type message: list[str]
        :param desc: 操作描述
        :type desc: str
        """
        
        

        self._operation_id = None
        self._resource_type = None
        self._operation_type = None
        self._domain_id = None
        self._project_id = None
        self._blockchain_id = None
        self._blockchain_name = None
        self._cluster_info = None
        self._operation_process = None
        self._record_time = None
        self._operation_status = None
        self._message = None
        self._desc = None
        self.discriminator = None

        if operation_id is not None:
            self.operation_id = operation_id
        if resource_type is not None:
            self.resource_type = resource_type
        if operation_type is not None:
            self.operation_type = operation_type
        if domain_id is not None:
            self.domain_id = domain_id
        if project_id is not None:
            self.project_id = project_id
        if blockchain_id is not None:
            self.blockchain_id = blockchain_id
        if blockchain_name is not None:
            self.blockchain_name = blockchain_name
        if cluster_info is not None:
            self.cluster_info = cluster_info
        if operation_process is not None:
            self.operation_process = operation_process
        if record_time is not None:
            self.record_time = record_time
        if operation_status is not None:
            self.operation_status = operation_status
        if message is not None:
            self.message = message
        if desc is not None:
            self.desc = desc

    @property
    def operation_id(self):
        """Gets the operation_id of this RecordDetailInfo.

        操作记录ID

        :return: The operation_id of this RecordDetailInfo.
        :rtype: str
        """
        return self._operation_id

    @operation_id.setter
    def operation_id(self, operation_id):
        """Sets the operation_id of this RecordDetailInfo.

        操作记录ID

        :param operation_id: The operation_id of this RecordDetailInfo.
        :type operation_id: str
        """
        self._operation_id = operation_id

    @property
    def resource_type(self):
        """Gets the resource_type of this RecordDetailInfo.

        资源类型

        :return: The resource_type of this RecordDetailInfo.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this RecordDetailInfo.

        资源类型

        :param resource_type: The resource_type of this RecordDetailInfo.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def operation_type(self):
        """Gets the operation_type of this RecordDetailInfo.

        操作类型

        :return: The operation_type of this RecordDetailInfo.
        :rtype: str
        """
        return self._operation_type

    @operation_type.setter
    def operation_type(self, operation_type):
        """Sets the operation_type of this RecordDetailInfo.

        操作类型

        :param operation_type: The operation_type of this RecordDetailInfo.
        :type operation_type: str
        """
        self._operation_type = operation_type

    @property
    def domain_id(self):
        """Gets the domain_id of this RecordDetailInfo.

        租户ID

        :return: The domain_id of this RecordDetailInfo.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this RecordDetailInfo.

        租户ID

        :param domain_id: The domain_id of this RecordDetailInfo.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def project_id(self):
        """Gets the project_id of this RecordDetailInfo.

        项目ID

        :return: The project_id of this RecordDetailInfo.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this RecordDetailInfo.

        项目ID

        :param project_id: The project_id of this RecordDetailInfo.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def blockchain_id(self):
        """Gets the blockchain_id of this RecordDetailInfo.

        区块链ID

        :return: The blockchain_id of this RecordDetailInfo.
        :rtype: str
        """
        return self._blockchain_id

    @blockchain_id.setter
    def blockchain_id(self, blockchain_id):
        """Sets the blockchain_id of this RecordDetailInfo.

        区块链ID

        :param blockchain_id: The blockchain_id of this RecordDetailInfo.
        :type blockchain_id: str
        """
        self._blockchain_id = blockchain_id

    @property
    def blockchain_name(self):
        """Gets the blockchain_name of this RecordDetailInfo.

        区块链名称

        :return: The blockchain_name of this RecordDetailInfo.
        :rtype: str
        """
        return self._blockchain_name

    @blockchain_name.setter
    def blockchain_name(self, blockchain_name):
        """Sets the blockchain_name of this RecordDetailInfo.

        区块链名称

        :param blockchain_name: The blockchain_name of this RecordDetailInfo.
        :type blockchain_name: str
        """
        self._blockchain_name = blockchain_name

    @property
    def cluster_info(self):
        """Gets the cluster_info of this RecordDetailInfo.


        :return: The cluster_info of this RecordDetailInfo.
        :rtype: :class:`huaweicloudsdkbcs.v2.OprecordCluster`
        """
        return self._cluster_info

    @cluster_info.setter
    def cluster_info(self, cluster_info):
        """Sets the cluster_info of this RecordDetailInfo.


        :param cluster_info: The cluster_info of this RecordDetailInfo.
        :type cluster_info: :class:`huaweicloudsdkbcs.v2.OprecordCluster`
        """
        self._cluster_info = cluster_info

    @property
    def operation_process(self):
        """Gets the operation_process of this RecordDetailInfo.

        操作流程，key为流程名，value为流程信息

        :return: The operation_process of this RecordDetailInfo.
        :rtype: dict(str, ProcessInfo)
        """
        return self._operation_process

    @operation_process.setter
    def operation_process(self, operation_process):
        """Sets the operation_process of this RecordDetailInfo.

        操作流程，key为流程名，value为流程信息

        :param operation_process: The operation_process of this RecordDetailInfo.
        :type operation_process: dict(str, ProcessInfo)
        """
        self._operation_process = operation_process

    @property
    def record_time(self):
        """Gets the record_time of this RecordDetailInfo.

        记录更新时间

        :return: The record_time of this RecordDetailInfo.
        :rtype: int
        """
        return self._record_time

    @record_time.setter
    def record_time(self, record_time):
        """Sets the record_time of this RecordDetailInfo.

        记录更新时间

        :param record_time: The record_time of this RecordDetailInfo.
        :type record_time: int
        """
        self._record_time = record_time

    @property
    def operation_status(self):
        """Gets the operation_status of this RecordDetailInfo.

        操作状态

        :return: The operation_status of this RecordDetailInfo.
        :rtype: str
        """
        return self._operation_status

    @operation_status.setter
    def operation_status(self, operation_status):
        """Sets the operation_status of this RecordDetailInfo.

        操作状态

        :param operation_status: The operation_status of this RecordDetailInfo.
        :type operation_status: str
        """
        self._operation_status = operation_status

    @property
    def message(self):
        """Gets the message of this RecordDetailInfo.

        操作过程信息记录

        :return: The message of this RecordDetailInfo.
        :rtype: list[str]
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this RecordDetailInfo.

        操作过程信息记录

        :param message: The message of this RecordDetailInfo.
        :type message: list[str]
        """
        self._message = message

    @property
    def desc(self):
        """Gets the desc of this RecordDetailInfo.

        操作描述

        :return: The desc of this RecordDetailInfo.
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        """Sets the desc of this RecordDetailInfo.

        操作描述

        :param desc: The desc of this RecordDetailInfo.
        :type desc: str
        """
        self._desc = desc

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
        if not isinstance(other, RecordDetailInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
