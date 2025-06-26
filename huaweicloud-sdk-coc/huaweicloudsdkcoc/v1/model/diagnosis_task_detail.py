# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DiagnosisTaskDetail:

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
        'code': 'str',
        'domain_id': 'str',
        'project_id': 'str',
        'user_id': 'str',
        'user_name': 'str',
        'progress': 'int',
        'work_order_id': 'str',
        'instance_id': 'str',
        'instance_name': 'str',
        'type': 'str',
        'status': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'instance_num': 'int',
        'os_type': 'str',
        'region': 'str',
        'node_list': 'list[DiagnosisTaskNode]',
        'message': 'str'
    }

    attribute_map = {
        'id': 'id',
        'code': 'code',
        'domain_id': 'domain_id',
        'project_id': 'project_id',
        'user_id': 'user_id',
        'user_name': 'user_name',
        'progress': 'progress',
        'work_order_id': 'work_order_id',
        'instance_id': 'instance_id',
        'instance_name': 'instance_name',
        'type': 'type',
        'status': 'status',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'instance_num': 'instance_num',
        'os_type': 'os_type',
        'region': 'region',
        'node_list': 'node_list',
        'message': 'message'
    }

    def __init__(self, id=None, code=None, domain_id=None, project_id=None, user_id=None, user_name=None, progress=None, work_order_id=None, instance_id=None, instance_name=None, type=None, status=None, start_time=None, end_time=None, instance_num=None, os_type=None, region=None, node_list=None, message=None):
        r"""DiagnosisTaskDetail

        The model defined in huaweicloud sdk

        :param id: id
        :type id: str
        :param code: code
        :type code: str
        :param domain_id: 诊断记录所属租户ID
        :type domain_id: str
        :param project_id: 被诊断实例所属项目ID
        :type project_id: str
        :param user_id: 诊断记录所属用户ID
        :type user_id: str
        :param user_name: 诊断记录所属用户名称
        :type user_name: str
        :param progress: 诊断进度
        :type progress: int
        :param work_order_id: 诊断任务工单ID
        :type work_order_id: str
        :param instance_id: 被诊断的实例ID
        :type instance_id: str
        :param instance_name: 被诊断的实例名称
        :type instance_name: str
        :param type: 被诊断实例类别，ECS、RDS等
        :type type: str
        :param status: 诊断任务状态执行状态
        :type status: str
        :param start_time: 创建时间，遵循RFC3339规范，精确到秒 示例：2020-09-01T18:50:20Z
        :type start_time: str
        :param end_time: 结束时间，遵循RFC3339规范，精确到秒 示例：2020-09-01T18:50:20Z
        :type end_time: str
        :param instance_num: 被诊断实例的数量
        :type instance_num: int
        :param os_type: 被诊断实例的操作系统类型
        :type os_type: str
        :param region: 诊断资源所属局点
        :type region: str
        :param node_list: 诊断步骤
        :type node_list: list[:class:`huaweicloudsdkcoc.v1.DiagnosisTaskNode`]
        :param message: 诊断结果
        :type message: str
        """
        
        

        self._id = None
        self._code = None
        self._domain_id = None
        self._project_id = None
        self._user_id = None
        self._user_name = None
        self._progress = None
        self._work_order_id = None
        self._instance_id = None
        self._instance_name = None
        self._type = None
        self._status = None
        self._start_time = None
        self._end_time = None
        self._instance_num = None
        self._os_type = None
        self._region = None
        self._node_list = None
        self._message = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if code is not None:
            self.code = code
        if domain_id is not None:
            self.domain_id = domain_id
        if project_id is not None:
            self.project_id = project_id
        if user_id is not None:
            self.user_id = user_id
        if user_name is not None:
            self.user_name = user_name
        if progress is not None:
            self.progress = progress
        if work_order_id is not None:
            self.work_order_id = work_order_id
        if instance_id is not None:
            self.instance_id = instance_id
        if instance_name is not None:
            self.instance_name = instance_name
        if type is not None:
            self.type = type
        if status is not None:
            self.status = status
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if instance_num is not None:
            self.instance_num = instance_num
        if os_type is not None:
            self.os_type = os_type
        if region is not None:
            self.region = region
        if node_list is not None:
            self.node_list = node_list
        if message is not None:
            self.message = message

    @property
    def id(self):
        r"""Gets the id of this DiagnosisTaskDetail.

        id

        :return: The id of this DiagnosisTaskDetail.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this DiagnosisTaskDetail.

        id

        :param id: The id of this DiagnosisTaskDetail.
        :type id: str
        """
        self._id = id

    @property
    def code(self):
        r"""Gets the code of this DiagnosisTaskDetail.

        code

        :return: The code of this DiagnosisTaskDetail.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this DiagnosisTaskDetail.

        code

        :param code: The code of this DiagnosisTaskDetail.
        :type code: str
        """
        self._code = code

    @property
    def domain_id(self):
        r"""Gets the domain_id of this DiagnosisTaskDetail.

        诊断记录所属租户ID

        :return: The domain_id of this DiagnosisTaskDetail.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this DiagnosisTaskDetail.

        诊断记录所属租户ID

        :param domain_id: The domain_id of this DiagnosisTaskDetail.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def project_id(self):
        r"""Gets the project_id of this DiagnosisTaskDetail.

        被诊断实例所属项目ID

        :return: The project_id of this DiagnosisTaskDetail.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this DiagnosisTaskDetail.

        被诊断实例所属项目ID

        :param project_id: The project_id of this DiagnosisTaskDetail.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def user_id(self):
        r"""Gets the user_id of this DiagnosisTaskDetail.

        诊断记录所属用户ID

        :return: The user_id of this DiagnosisTaskDetail.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this DiagnosisTaskDetail.

        诊断记录所属用户ID

        :param user_id: The user_id of this DiagnosisTaskDetail.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def user_name(self):
        r"""Gets the user_name of this DiagnosisTaskDetail.

        诊断记录所属用户名称

        :return: The user_name of this DiagnosisTaskDetail.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this DiagnosisTaskDetail.

        诊断记录所属用户名称

        :param user_name: The user_name of this DiagnosisTaskDetail.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def progress(self):
        r"""Gets the progress of this DiagnosisTaskDetail.

        诊断进度

        :return: The progress of this DiagnosisTaskDetail.
        :rtype: int
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        r"""Sets the progress of this DiagnosisTaskDetail.

        诊断进度

        :param progress: The progress of this DiagnosisTaskDetail.
        :type progress: int
        """
        self._progress = progress

    @property
    def work_order_id(self):
        r"""Gets the work_order_id of this DiagnosisTaskDetail.

        诊断任务工单ID

        :return: The work_order_id of this DiagnosisTaskDetail.
        :rtype: str
        """
        return self._work_order_id

    @work_order_id.setter
    def work_order_id(self, work_order_id):
        r"""Sets the work_order_id of this DiagnosisTaskDetail.

        诊断任务工单ID

        :param work_order_id: The work_order_id of this DiagnosisTaskDetail.
        :type work_order_id: str
        """
        self._work_order_id = work_order_id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this DiagnosisTaskDetail.

        被诊断的实例ID

        :return: The instance_id of this DiagnosisTaskDetail.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this DiagnosisTaskDetail.

        被诊断的实例ID

        :param instance_id: The instance_id of this DiagnosisTaskDetail.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def instance_name(self):
        r"""Gets the instance_name of this DiagnosisTaskDetail.

        被诊断的实例名称

        :return: The instance_name of this DiagnosisTaskDetail.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        r"""Sets the instance_name of this DiagnosisTaskDetail.

        被诊断的实例名称

        :param instance_name: The instance_name of this DiagnosisTaskDetail.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def type(self):
        r"""Gets the type of this DiagnosisTaskDetail.

        被诊断实例类别，ECS、RDS等

        :return: The type of this DiagnosisTaskDetail.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this DiagnosisTaskDetail.

        被诊断实例类别，ECS、RDS等

        :param type: The type of this DiagnosisTaskDetail.
        :type type: str
        """
        self._type = type

    @property
    def status(self):
        r"""Gets the status of this DiagnosisTaskDetail.

        诊断任务状态执行状态

        :return: The status of this DiagnosisTaskDetail.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this DiagnosisTaskDetail.

        诊断任务状态执行状态

        :param status: The status of this DiagnosisTaskDetail.
        :type status: str
        """
        self._status = status

    @property
    def start_time(self):
        r"""Gets the start_time of this DiagnosisTaskDetail.

        创建时间，遵循RFC3339规范，精确到秒 示例：2020-09-01T18:50:20Z

        :return: The start_time of this DiagnosisTaskDetail.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this DiagnosisTaskDetail.

        创建时间，遵循RFC3339规范，精确到秒 示例：2020-09-01T18:50:20Z

        :param start_time: The start_time of this DiagnosisTaskDetail.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this DiagnosisTaskDetail.

        结束时间，遵循RFC3339规范，精确到秒 示例：2020-09-01T18:50:20Z

        :return: The end_time of this DiagnosisTaskDetail.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this DiagnosisTaskDetail.

        结束时间，遵循RFC3339规范，精确到秒 示例：2020-09-01T18:50:20Z

        :param end_time: The end_time of this DiagnosisTaskDetail.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def instance_num(self):
        r"""Gets the instance_num of this DiagnosisTaskDetail.

        被诊断实例的数量

        :return: The instance_num of this DiagnosisTaskDetail.
        :rtype: int
        """
        return self._instance_num

    @instance_num.setter
    def instance_num(self, instance_num):
        r"""Sets the instance_num of this DiagnosisTaskDetail.

        被诊断实例的数量

        :param instance_num: The instance_num of this DiagnosisTaskDetail.
        :type instance_num: int
        """
        self._instance_num = instance_num

    @property
    def os_type(self):
        r"""Gets the os_type of this DiagnosisTaskDetail.

        被诊断实例的操作系统类型

        :return: The os_type of this DiagnosisTaskDetail.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        r"""Sets the os_type of this DiagnosisTaskDetail.

        被诊断实例的操作系统类型

        :param os_type: The os_type of this DiagnosisTaskDetail.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def region(self):
        r"""Gets the region of this DiagnosisTaskDetail.

        诊断资源所属局点

        :return: The region of this DiagnosisTaskDetail.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this DiagnosisTaskDetail.

        诊断资源所属局点

        :param region: The region of this DiagnosisTaskDetail.
        :type region: str
        """
        self._region = region

    @property
    def node_list(self):
        r"""Gets the node_list of this DiagnosisTaskDetail.

        诊断步骤

        :return: The node_list of this DiagnosisTaskDetail.
        :rtype: list[:class:`huaweicloudsdkcoc.v1.DiagnosisTaskNode`]
        """
        return self._node_list

    @node_list.setter
    def node_list(self, node_list):
        r"""Sets the node_list of this DiagnosisTaskDetail.

        诊断步骤

        :param node_list: The node_list of this DiagnosisTaskDetail.
        :type node_list: list[:class:`huaweicloudsdkcoc.v1.DiagnosisTaskNode`]
        """
        self._node_list = node_list

    @property
    def message(self):
        r"""Gets the message of this DiagnosisTaskDetail.

        诊断结果

        :return: The message of this DiagnosisTaskDetail.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this DiagnosisTaskDetail.

        诊断结果

        :param message: The message of this DiagnosisTaskDetail.
        :type message: str
        """
        self._message = message

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
        if not isinstance(other, DiagnosisTaskDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
