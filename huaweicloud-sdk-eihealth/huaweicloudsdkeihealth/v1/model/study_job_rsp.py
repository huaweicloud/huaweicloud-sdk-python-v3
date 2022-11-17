# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StudyJobRsp:

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
        'workflow_job_id': 'str',
        'name': 'str',
        'status': 'str',
        'template_id': 'str',
        'database_name': 'str',
        'database_id': 'str',
        'relative_path': 'str',
        'output_file_type': 'str',
        'workflow_name': 'str',
        'label': 'str',
        'create_time': 'str',
        'update_time': 'str'
    }

    attribute_map = {
        'id': 'id',
        'workflow_job_id': 'workflow_job_id',
        'name': 'name',
        'status': 'status',
        'template_id': 'template_id',
        'database_name': 'database_name',
        'database_id': 'database_id',
        'relative_path': 'relative_path',
        'output_file_type': 'output_file_type',
        'workflow_name': 'workflow_name',
        'label': 'label',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, id=None, workflow_job_id=None, name=None, status=None, template_id=None, database_name=None, database_id=None, relative_path=None, output_file_type=None, workflow_name=None, label=None, create_time=None, update_time=None):
        """StudyJobRsp

        The model defined in huaweicloud sdk

        :param id: study作业id
        :type id: str
        :param workflow_job_id: workflow作业id
        :type workflow_job_id: str
        :param name: 作业名称
        :type name: str
        :param status: 作业状态
        :type status: str
        :param template_id: 生成study作业结果的模板id
        :type template_id: str
        :param database_name: study作业结果的数据库实例名称
        :type database_name: str
        :param database_id: study作业结果的数据库实例id
        :type database_id: str
        :param relative_path: 生成study作业结果的文件的相对路径
        :type relative_path: str
        :param output_file_type: 生成study作业结果的文件的类型
        :type output_file_type: str
        :param workflow_name: 使用的workflow名称
        :type workflow_name: str
        :param label: 使用的workflow标签
        :type label: str
        :param create_time: 作业创建时间
        :type create_time: str
        :param update_time: 作业更新时间
        :type update_time: str
        """
        
        

        self._id = None
        self._workflow_job_id = None
        self._name = None
        self._status = None
        self._template_id = None
        self._database_name = None
        self._database_id = None
        self._relative_path = None
        self._output_file_type = None
        self._workflow_name = None
        self._label = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if workflow_job_id is not None:
            self.workflow_job_id = workflow_job_id
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if template_id is not None:
            self.template_id = template_id
        if database_name is not None:
            self.database_name = database_name
        if database_id is not None:
            self.database_id = database_id
        if relative_path is not None:
            self.relative_path = relative_path
        if output_file_type is not None:
            self.output_file_type = output_file_type
        if workflow_name is not None:
            self.workflow_name = workflow_name
        if label is not None:
            self.label = label
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def id(self):
        """Gets the id of this StudyJobRsp.

        study作业id

        :return: The id of this StudyJobRsp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this StudyJobRsp.

        study作业id

        :param id: The id of this StudyJobRsp.
        :type id: str
        """
        self._id = id

    @property
    def workflow_job_id(self):
        """Gets the workflow_job_id of this StudyJobRsp.

        workflow作业id

        :return: The workflow_job_id of this StudyJobRsp.
        :rtype: str
        """
        return self._workflow_job_id

    @workflow_job_id.setter
    def workflow_job_id(self, workflow_job_id):
        """Sets the workflow_job_id of this StudyJobRsp.

        workflow作业id

        :param workflow_job_id: The workflow_job_id of this StudyJobRsp.
        :type workflow_job_id: str
        """
        self._workflow_job_id = workflow_job_id

    @property
    def name(self):
        """Gets the name of this StudyJobRsp.

        作业名称

        :return: The name of this StudyJobRsp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this StudyJobRsp.

        作业名称

        :param name: The name of this StudyJobRsp.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        """Gets the status of this StudyJobRsp.

        作业状态

        :return: The status of this StudyJobRsp.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this StudyJobRsp.

        作业状态

        :param status: The status of this StudyJobRsp.
        :type status: str
        """
        self._status = status

    @property
    def template_id(self):
        """Gets the template_id of this StudyJobRsp.

        生成study作业结果的模板id

        :return: The template_id of this StudyJobRsp.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this StudyJobRsp.

        生成study作业结果的模板id

        :param template_id: The template_id of this StudyJobRsp.
        :type template_id: str
        """
        self._template_id = template_id

    @property
    def database_name(self):
        """Gets the database_name of this StudyJobRsp.

        study作业结果的数据库实例名称

        :return: The database_name of this StudyJobRsp.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        """Sets the database_name of this StudyJobRsp.

        study作业结果的数据库实例名称

        :param database_name: The database_name of this StudyJobRsp.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def database_id(self):
        """Gets the database_id of this StudyJobRsp.

        study作业结果的数据库实例id

        :return: The database_id of this StudyJobRsp.
        :rtype: str
        """
        return self._database_id

    @database_id.setter
    def database_id(self, database_id):
        """Sets the database_id of this StudyJobRsp.

        study作业结果的数据库实例id

        :param database_id: The database_id of this StudyJobRsp.
        :type database_id: str
        """
        self._database_id = database_id

    @property
    def relative_path(self):
        """Gets the relative_path of this StudyJobRsp.

        生成study作业结果的文件的相对路径

        :return: The relative_path of this StudyJobRsp.
        :rtype: str
        """
        return self._relative_path

    @relative_path.setter
    def relative_path(self, relative_path):
        """Sets the relative_path of this StudyJobRsp.

        生成study作业结果的文件的相对路径

        :param relative_path: The relative_path of this StudyJobRsp.
        :type relative_path: str
        """
        self._relative_path = relative_path

    @property
    def output_file_type(self):
        """Gets the output_file_type of this StudyJobRsp.

        生成study作业结果的文件的类型

        :return: The output_file_type of this StudyJobRsp.
        :rtype: str
        """
        return self._output_file_type

    @output_file_type.setter
    def output_file_type(self, output_file_type):
        """Sets the output_file_type of this StudyJobRsp.

        生成study作业结果的文件的类型

        :param output_file_type: The output_file_type of this StudyJobRsp.
        :type output_file_type: str
        """
        self._output_file_type = output_file_type

    @property
    def workflow_name(self):
        """Gets the workflow_name of this StudyJobRsp.

        使用的workflow名称

        :return: The workflow_name of this StudyJobRsp.
        :rtype: str
        """
        return self._workflow_name

    @workflow_name.setter
    def workflow_name(self, workflow_name):
        """Sets the workflow_name of this StudyJobRsp.

        使用的workflow名称

        :param workflow_name: The workflow_name of this StudyJobRsp.
        :type workflow_name: str
        """
        self._workflow_name = workflow_name

    @property
    def label(self):
        """Gets the label of this StudyJobRsp.

        使用的workflow标签

        :return: The label of this StudyJobRsp.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this StudyJobRsp.

        使用的workflow标签

        :param label: The label of this StudyJobRsp.
        :type label: str
        """
        self._label = label

    @property
    def create_time(self):
        """Gets the create_time of this StudyJobRsp.

        作业创建时间

        :return: The create_time of this StudyJobRsp.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this StudyJobRsp.

        作业创建时间

        :param create_time: The create_time of this StudyJobRsp.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this StudyJobRsp.

        作业更新时间

        :return: The update_time of this StudyJobRsp.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this StudyJobRsp.

        作业更新时间

        :param update_time: The update_time of this StudyJobRsp.
        :type update_time: str
        """
        self._update_time = update_time

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
        if not isinstance(other, StudyJobRsp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
