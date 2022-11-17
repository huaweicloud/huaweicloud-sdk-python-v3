# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'created_by': 'str',
        'execution_status': 'str',
        'job_desc': 'str',
        'job_id': 'str',
        'job_name': 'str',
        'job_type': 'str',
        'order_id': 'str',
        'project_id': 'str',
        'service_instance_id': 'str'
    }

    attribute_map = {
        'created_by': 'CREATED_BY',
        'execution_status': 'EXECUTION_STATUS',
        'job_desc': 'JOB_DESC',
        'job_id': 'JOB_ID',
        'job_name': 'JOB_NAME',
        'job_type': 'JOB_TYPE',
        'order_id': 'ORDER_ID',
        'project_id': 'PROJECT_ID',
        'service_instance_id': 'SERVICE_INSTANCE_ID'
    }

    def __init__(self, created_by=None, execution_status=None, job_desc=None, job_id=None, job_name=None, job_type=None, order_id=None, project_id=None, service_instance_id=None):
        """JobInfo

        The model defined in huaweicloud sdk

        :param created_by: 创建者。
        :type created_by: str
        :param execution_status: 执行状态。
        :type execution_status: str
        :param job_desc: 工作描述。
        :type job_desc: str
        :param job_id: 工作ID。
        :type job_id: str
        :param job_name: 工作名称。
        :type job_name: str
        :param job_type: 类别。
        :type job_type: str
        :param order_id: 排序ID。
        :type order_id: str
        :param project_id: 创建租户的项目ID。
        :type project_id: str
        :param service_instance_id: 实例ID。
        :type service_instance_id: str
        """
        
        

        self._created_by = None
        self._execution_status = None
        self._job_desc = None
        self._job_id = None
        self._job_name = None
        self._job_type = None
        self._order_id = None
        self._project_id = None
        self._service_instance_id = None
        self.discriminator = None

        if created_by is not None:
            self.created_by = created_by
        if execution_status is not None:
            self.execution_status = execution_status
        if job_desc is not None:
            self.job_desc = job_desc
        if job_id is not None:
            self.job_id = job_id
        if job_name is not None:
            self.job_name = job_name
        if job_type is not None:
            self.job_type = job_type
        if order_id is not None:
            self.order_id = order_id
        if project_id is not None:
            self.project_id = project_id
        if service_instance_id is not None:
            self.service_instance_id = service_instance_id

    @property
    def created_by(self):
        """Gets the created_by of this JobInfo.

        创建者。

        :return: The created_by of this JobInfo.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this JobInfo.

        创建者。

        :param created_by: The created_by of this JobInfo.
        :type created_by: str
        """
        self._created_by = created_by

    @property
    def execution_status(self):
        """Gets the execution_status of this JobInfo.

        执行状态。

        :return: The execution_status of this JobInfo.
        :rtype: str
        """
        return self._execution_status

    @execution_status.setter
    def execution_status(self, execution_status):
        """Sets the execution_status of this JobInfo.

        执行状态。

        :param execution_status: The execution_status of this JobInfo.
        :type execution_status: str
        """
        self._execution_status = execution_status

    @property
    def job_desc(self):
        """Gets the job_desc of this JobInfo.

        工作描述。

        :return: The job_desc of this JobInfo.
        :rtype: str
        """
        return self._job_desc

    @job_desc.setter
    def job_desc(self, job_desc):
        """Sets the job_desc of this JobInfo.

        工作描述。

        :param job_desc: The job_desc of this JobInfo.
        :type job_desc: str
        """
        self._job_desc = job_desc

    @property
    def job_id(self):
        """Gets the job_id of this JobInfo.

        工作ID。

        :return: The job_id of this JobInfo.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this JobInfo.

        工作ID。

        :param job_id: The job_id of this JobInfo.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def job_name(self):
        """Gets the job_name of this JobInfo.

        工作名称。

        :return: The job_name of this JobInfo.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        """Sets the job_name of this JobInfo.

        工作名称。

        :param job_name: The job_name of this JobInfo.
        :type job_name: str
        """
        self._job_name = job_name

    @property
    def job_type(self):
        """Gets the job_type of this JobInfo.

        类别。

        :return: The job_type of this JobInfo.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        """Sets the job_type of this JobInfo.

        类别。

        :param job_type: The job_type of this JobInfo.
        :type job_type: str
        """
        self._job_type = job_type

    @property
    def order_id(self):
        """Gets the order_id of this JobInfo.

        排序ID。

        :return: The order_id of this JobInfo.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this JobInfo.

        排序ID。

        :param order_id: The order_id of this JobInfo.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def project_id(self):
        """Gets the project_id of this JobInfo.

        创建租户的项目ID。

        :return: The project_id of this JobInfo.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this JobInfo.

        创建租户的项目ID。

        :param project_id: The project_id of this JobInfo.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def service_instance_id(self):
        """Gets the service_instance_id of this JobInfo.

        实例ID。

        :return: The service_instance_id of this JobInfo.
        :rtype: str
        """
        return self._service_instance_id

    @service_instance_id.setter
    def service_instance_id(self, service_instance_id):
        """Sets the service_instance_id of this JobInfo.

        实例ID。

        :param service_instance_id: The service_instance_id of this JobInfo.
        :type service_instance_id: str
        """
        self._service_instance_id = service_instance_id

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
        if not isinstance(other, JobInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
