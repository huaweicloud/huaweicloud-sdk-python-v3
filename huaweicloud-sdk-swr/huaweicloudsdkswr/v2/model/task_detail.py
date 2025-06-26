# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'execution_id': 'int',
        'resource_type': 'str',
        'src_resource': 'str',
        'dst_resource': 'str',
        'operation': 'str',
        'job_id': 'str',
        'status': 'str',
        'status_revision': 'int',
        'start_time': 'str',
        'end_time': 'str'
    }

    attribute_map = {
        'id': 'id',
        'execution_id': 'execution_id',
        'resource_type': 'resource_type',
        'src_resource': 'src_resource',
        'dst_resource': 'dst_resource',
        'operation': 'operation',
        'job_id': 'job_id',
        'status': 'status',
        'status_revision': 'StatusRevision',
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, id=None, execution_id=None, resource_type=None, src_resource=None, dst_resource=None, operation=None, job_id=None, status=None, status_revision=None, start_time=None, end_time=None):
        r"""TaskDetail

        The model defined in huaweicloud sdk

        :param id: 任务ID
        :type id: int
        :param execution_id: 执行任务的ID
        :type execution_id: int
        :param resource_type: 资源类型
        :type resource_type: str
        :param src_resource: 源资源
        :type src_resource: str
        :param dst_resource: 目标资源
        :type dst_resource: str
        :param operation: 操作类型
        :type operation: str
        :param job_id: harbor任务ID
        :type job_id: str
        :param status: 状态
        :type status: str
        :param status_revision: 状态修订
        :type status_revision: int
        :param start_time: 开始时间
        :type start_time: str
        :param end_time: 结束时间
        :type end_time: str
        """
        
        

        self._id = None
        self._execution_id = None
        self._resource_type = None
        self._src_resource = None
        self._dst_resource = None
        self._operation = None
        self._job_id = None
        self._status = None
        self._status_revision = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        self.id = id
        self.execution_id = execution_id
        self.resource_type = resource_type
        self.src_resource = src_resource
        self.dst_resource = dst_resource
        self.operation = operation
        self.job_id = job_id
        self.status = status
        self.status_revision = status_revision
        self.start_time = start_time
        self.end_time = end_time

    @property
    def id(self):
        r"""Gets the id of this TaskDetail.

        任务ID

        :return: The id of this TaskDetail.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this TaskDetail.

        任务ID

        :param id: The id of this TaskDetail.
        :type id: int
        """
        self._id = id

    @property
    def execution_id(self):
        r"""Gets the execution_id of this TaskDetail.

        执行任务的ID

        :return: The execution_id of this TaskDetail.
        :rtype: int
        """
        return self._execution_id

    @execution_id.setter
    def execution_id(self, execution_id):
        r"""Sets the execution_id of this TaskDetail.

        执行任务的ID

        :param execution_id: The execution_id of this TaskDetail.
        :type execution_id: int
        """
        self._execution_id = execution_id

    @property
    def resource_type(self):
        r"""Gets the resource_type of this TaskDetail.

        资源类型

        :return: The resource_type of this TaskDetail.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this TaskDetail.

        资源类型

        :param resource_type: The resource_type of this TaskDetail.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def src_resource(self):
        r"""Gets the src_resource of this TaskDetail.

        源资源

        :return: The src_resource of this TaskDetail.
        :rtype: str
        """
        return self._src_resource

    @src_resource.setter
    def src_resource(self, src_resource):
        r"""Sets the src_resource of this TaskDetail.

        源资源

        :param src_resource: The src_resource of this TaskDetail.
        :type src_resource: str
        """
        self._src_resource = src_resource

    @property
    def dst_resource(self):
        r"""Gets the dst_resource of this TaskDetail.

        目标资源

        :return: The dst_resource of this TaskDetail.
        :rtype: str
        """
        return self._dst_resource

    @dst_resource.setter
    def dst_resource(self, dst_resource):
        r"""Sets the dst_resource of this TaskDetail.

        目标资源

        :param dst_resource: The dst_resource of this TaskDetail.
        :type dst_resource: str
        """
        self._dst_resource = dst_resource

    @property
    def operation(self):
        r"""Gets the operation of this TaskDetail.

        操作类型

        :return: The operation of this TaskDetail.
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        r"""Sets the operation of this TaskDetail.

        操作类型

        :param operation: The operation of this TaskDetail.
        :type operation: str
        """
        self._operation = operation

    @property
    def job_id(self):
        r"""Gets the job_id of this TaskDetail.

        harbor任务ID

        :return: The job_id of this TaskDetail.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this TaskDetail.

        harbor任务ID

        :param job_id: The job_id of this TaskDetail.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def status(self):
        r"""Gets the status of this TaskDetail.

        状态

        :return: The status of this TaskDetail.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this TaskDetail.

        状态

        :param status: The status of this TaskDetail.
        :type status: str
        """
        self._status = status

    @property
    def status_revision(self):
        r"""Gets the status_revision of this TaskDetail.

        状态修订

        :return: The status_revision of this TaskDetail.
        :rtype: int
        """
        return self._status_revision

    @status_revision.setter
    def status_revision(self, status_revision):
        r"""Sets the status_revision of this TaskDetail.

        状态修订

        :param status_revision: The status_revision of this TaskDetail.
        :type status_revision: int
        """
        self._status_revision = status_revision

    @property
    def start_time(self):
        r"""Gets the start_time of this TaskDetail.

        开始时间

        :return: The start_time of this TaskDetail.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this TaskDetail.

        开始时间

        :param start_time: The start_time of this TaskDetail.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this TaskDetail.

        结束时间

        :return: The end_time of this TaskDetail.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this TaskDetail.

        结束时间

        :param end_time: The end_time of this TaskDetail.
        :type end_time: str
        """
        self._end_time = end_time

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
        if not isinstance(other, TaskDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
