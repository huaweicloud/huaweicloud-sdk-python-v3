# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EditingJob:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'task_id': 'str',
        'status': 'str',
        'create_time': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'description': 'str',
        'user_data': 'str',
        'job_id': 'str',
        'edit_type': 'list[str]',
        'edit_task_req': 'CreateEditingJobReq',
        'output_file_info': 'list[OutputFileInfo]'
    }

    attribute_map = {
        'task_id': 'task_id',
        'status': 'status',
        'create_time': 'create_time',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'description': 'description',
        'user_data': 'user_data',
        'job_id': 'job_id',
        'edit_type': 'edit_type',
        'edit_task_req': 'edit_task_req',
        'output_file_info': 'output_file_info'
    }

    def __init__(self, task_id=None, status=None, create_time=None, start_time=None, end_time=None, description=None, user_data=None, job_id=None, edit_type=None, edit_task_req=None, output_file_info=None):
        """EditingJob - a model defined in huaweicloud sdk"""
        
        

        self._task_id = None
        self._status = None
        self._create_time = None
        self._start_time = None
        self._end_time = None
        self._description = None
        self._user_data = None
        self._job_id = None
        self._edit_type = None
        self._edit_task_req = None
        self._output_file_info = None
        self.discriminator = None

        if task_id is not None:
            self.task_id = task_id
        if status is not None:
            self.status = status
        if create_time is not None:
            self.create_time = create_time
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if description is not None:
            self.description = description
        if user_data is not None:
            self.user_data = user_data
        if job_id is not None:
            self.job_id = job_id
        if edit_type is not None:
            self.edit_type = edit_type
        if edit_task_req is not None:
            self.edit_task_req = edit_task_req
        if output_file_info is not None:
            self.output_file_info = output_file_info

    @property
    def task_id(self):
        """Gets the task_id of this EditingJob.

        任务ID 

        :return: The task_id of this EditingJob.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this EditingJob.

        任务ID 

        :param task_id: The task_id of this EditingJob.
        :type: str
        """
        self._task_id = task_id

    @property
    def status(self):
        """Gets the status of this EditingJob.

        任务状态。  取值如下： - INIT：初始状态。 - WAITING：等待启动。 - PROCESSING：处理中。 - SUCCEED：处理成功。 - FAILED：处理失败。 - CANCELED：已取消。 

        :return: The status of this EditingJob.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this EditingJob.

        任务状态。  取值如下： - INIT：初始状态。 - WAITING：等待启动。 - PROCESSING：处理中。 - SUCCEED：处理成功。 - FAILED：处理失败。 - CANCELED：已取消。 

        :param status: The status of this EditingJob.
        :type: str
        """
        self._status = status

    @property
    def create_time(self):
        """Gets the create_time of this EditingJob.

        任务创建时间 

        :return: The create_time of this EditingJob.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this EditingJob.

        任务创建时间 

        :param create_time: The create_time of this EditingJob.
        :type: str
        """
        self._create_time = create_time

    @property
    def start_time(self):
        """Gets the start_time of this EditingJob.

        任务启动时间 

        :return: The start_time of this EditingJob.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this EditingJob.

        任务启动时间 

        :param start_time: The start_time of this EditingJob.
        :type: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this EditingJob.

        任务结束时间 

        :return: The end_time of this EditingJob.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this EditingJob.

        任务结束时间 

        :param end_time: The end_time of this EditingJob.
        :type: str
        """
        self._end_time = end_time

    @property
    def description(self):
        """Gets the description of this EditingJob.

        错误描述 

        :return: The description of this EditingJob.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this EditingJob.

        错误描述 

        :param description: The description of this EditingJob.
        :type: str
        """
        self._description = description

    @property
    def user_data(self):
        """Gets the user_data of this EditingJob.

        用户数据。 

        :return: The user_data of this EditingJob.
        :rtype: str
        """
        return self._user_data

    @user_data.setter
    def user_data(self, user_data):
        """Sets the user_data of this EditingJob.

        用户数据。 

        :param user_data: The user_data of this EditingJob.
        :type: str
        """
        self._user_data = user_data

    @property
    def job_id(self):
        """Gets the job_id of this EditingJob.

        任务ID 

        :return: The job_id of this EditingJob.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this EditingJob.

        任务ID 

        :param job_id: The job_id of this EditingJob.
        :type: str
        """
        self._job_id = job_id

    @property
    def edit_type(self):
        """Gets the edit_type of this EditingJob.

        剪辑任务类型。取值如下：\"CLIP\",\"CONCAT\"。

        :return: The edit_type of this EditingJob.
        :rtype: list[str]
        """
        return self._edit_type

    @edit_type.setter
    def edit_type(self, edit_type):
        """Sets the edit_type of this EditingJob.

        剪辑任务类型。取值如下：\"CLIP\",\"CONCAT\"。

        :param edit_type: The edit_type of this EditingJob.
        :type: list[str]
        """
        self._edit_type = edit_type

    @property
    def edit_task_req(self):
        """Gets the edit_task_req of this EditingJob.


        :return: The edit_task_req of this EditingJob.
        :rtype: CreateEditingJobReq
        """
        return self._edit_task_req

    @edit_task_req.setter
    def edit_task_req(self, edit_task_req):
        """Sets the edit_task_req of this EditingJob.


        :param edit_task_req: The edit_task_req of this EditingJob.
        :type: CreateEditingJobReq
        """
        self._edit_task_req = edit_task_req

    @property
    def output_file_info(self):
        """Gets the output_file_info of this EditingJob.

        剪辑输出meta信息

        :return: The output_file_info of this EditingJob.
        :rtype: list[OutputFileInfo]
        """
        return self._output_file_info

    @output_file_info.setter
    def output_file_info(self, output_file_info):
        """Sets the output_file_info of this EditingJob.

        剪辑输出meta信息

        :param output_file_info: The output_file_info of this EditingJob.
        :type: list[OutputFileInfo]
        """
        self._output_file_info = output_file_info

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
        if not isinstance(other, EditingJob):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
