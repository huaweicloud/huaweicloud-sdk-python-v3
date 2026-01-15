# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DataTransformationItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'data_transformation_id': 'str',
        'data_transformation_name': 'str',
        'script': 'str',
        'status': 'JobStatus',
        'directory': 'str',
        'description': 'str',
        'job_mode': 'IsapJobMode',
        'process_status': 'JobProcessStatus',
        'process_error': 'DataTransformationProcessError',
        'environment': 'JobEnvironment',
        'output_table_id': 'str',
        'output_table_name': 'str',
        'output_table_ids': 'list[str]',
        'output_table_names': 'list[str]',
        'create_by': 'str',
        'create_time': 'int',
        'update_by': 'str',
        'update_time': 'int',
        'delete_time': 'int'
    }

    attribute_map = {
        'data_transformation_id': 'data_transformation_id',
        'data_transformation_name': 'data_transformation_name',
        'script': 'script',
        'status': 'status',
        'directory': 'directory',
        'description': 'description',
        'job_mode': 'job_mode',
        'process_status': 'process_status',
        'process_error': 'process_error',
        'environment': 'environment',
        'output_table_id': 'output_table_id',
        'output_table_name': 'output_table_name',
        'output_table_ids': 'output_table_ids',
        'output_table_names': 'output_table_names',
        'create_by': 'create_by',
        'create_time': 'create_time',
        'update_by': 'update_by',
        'update_time': 'update_time',
        'delete_time': 'delete_time'
    }

    def __init__(self, data_transformation_id=None, data_transformation_name=None, script=None, status=None, directory=None, description=None, job_mode=None, process_status=None, process_error=None, environment=None, output_table_id=None, output_table_name=None, output_table_ids=None, output_table_names=None, create_by=None, create_time=None, update_by=None, update_time=None, delete_time=None):
        r"""DataTransformationItem

        The model defined in huaweicloud sdk

        :param data_transformation_id: UUID
        :type data_transformation_id: str
        :param data_transformation_name: 数据转换名称
        :type data_transformation_name: str
        :param script: Job Script 作业脚本
        :type script: str
        :param status: 
        :type status: :class:`huaweicloudsdksecmaster.v2.JobStatus`
        :param directory: directory 目录分组
        :type directory: str
        :param description: 数据转换描述
        :type description: str
        :param job_mode: 
        :type job_mode: :class:`huaweicloudsdksecmaster.v2.IsapJobMode`
        :param process_status: 
        :type process_status: :class:`huaweicloudsdksecmaster.v2.JobProcessStatus`
        :param process_error: 
        :type process_error: :class:`huaweicloudsdksecmaster.v2.DataTransformationProcessError`
        :param environment: 
        :type environment: :class:`huaweicloudsdksecmaster.v2.JobEnvironment`
        :param output_table_id: UUID
        :type output_table_id: str
        :param output_table_name: 表名称
        :type output_table_name: str
        :param output_table_ids: 输出表ID列表
        :type output_table_ids: list[str]
        :param output_table_names: 输出表名称列表
        :type output_table_names: list[str]
        :param create_by: 创建者
        :type create_by: str
        :param create_time: 毫秒时间戳
        :type create_time: int
        :param update_by: 更新者
        :type update_by: str
        :param update_time: 毫秒时间戳
        :type update_time: int
        :param delete_time: 毫秒时间戳
        :type delete_time: int
        """
        
        

        self._data_transformation_id = None
        self._data_transformation_name = None
        self._script = None
        self._status = None
        self._directory = None
        self._description = None
        self._job_mode = None
        self._process_status = None
        self._process_error = None
        self._environment = None
        self._output_table_id = None
        self._output_table_name = None
        self._output_table_ids = None
        self._output_table_names = None
        self._create_by = None
        self._create_time = None
        self._update_by = None
        self._update_time = None
        self._delete_time = None
        self.discriminator = None

        self.data_transformation_id = data_transformation_id
        self.data_transformation_name = data_transformation_name
        self.script = script
        self.status = status
        if directory is not None:
            self.directory = directory
        if description is not None:
            self.description = description
        self.job_mode = job_mode
        self.process_status = process_status
        self.process_error = process_error
        self.environment = environment
        self.output_table_id = output_table_id
        self.output_table_name = output_table_name
        self.output_table_ids = output_table_ids
        self.output_table_names = output_table_names
        self.create_by = create_by
        self.create_time = create_time
        self.update_by = update_by
        self.update_time = update_time
        if delete_time is not None:
            self.delete_time = delete_time

    @property
    def data_transformation_id(self):
        r"""Gets the data_transformation_id of this DataTransformationItem.

        UUID

        :return: The data_transformation_id of this DataTransformationItem.
        :rtype: str
        """
        return self._data_transformation_id

    @data_transformation_id.setter
    def data_transformation_id(self, data_transformation_id):
        r"""Sets the data_transformation_id of this DataTransformationItem.

        UUID

        :param data_transformation_id: The data_transformation_id of this DataTransformationItem.
        :type data_transformation_id: str
        """
        self._data_transformation_id = data_transformation_id

    @property
    def data_transformation_name(self):
        r"""Gets the data_transformation_name of this DataTransformationItem.

        数据转换名称

        :return: The data_transformation_name of this DataTransformationItem.
        :rtype: str
        """
        return self._data_transformation_name

    @data_transformation_name.setter
    def data_transformation_name(self, data_transformation_name):
        r"""Sets the data_transformation_name of this DataTransformationItem.

        数据转换名称

        :param data_transformation_name: The data_transformation_name of this DataTransformationItem.
        :type data_transformation_name: str
        """
        self._data_transformation_name = data_transformation_name

    @property
    def script(self):
        r"""Gets the script of this DataTransformationItem.

        Job Script 作业脚本

        :return: The script of this DataTransformationItem.
        :rtype: str
        """
        return self._script

    @script.setter
    def script(self, script):
        r"""Sets the script of this DataTransformationItem.

        Job Script 作业脚本

        :param script: The script of this DataTransformationItem.
        :type script: str
        """
        self._script = script

    @property
    def status(self):
        r"""Gets the status of this DataTransformationItem.

        :return: The status of this DataTransformationItem.
        :rtype: :class:`huaweicloudsdksecmaster.v2.JobStatus`
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this DataTransformationItem.

        :param status: The status of this DataTransformationItem.
        :type status: :class:`huaweicloudsdksecmaster.v2.JobStatus`
        """
        self._status = status

    @property
    def directory(self):
        r"""Gets the directory of this DataTransformationItem.

        directory 目录分组

        :return: The directory of this DataTransformationItem.
        :rtype: str
        """
        return self._directory

    @directory.setter
    def directory(self, directory):
        r"""Sets the directory of this DataTransformationItem.

        directory 目录分组

        :param directory: The directory of this DataTransformationItem.
        :type directory: str
        """
        self._directory = directory

    @property
    def description(self):
        r"""Gets the description of this DataTransformationItem.

        数据转换描述

        :return: The description of this DataTransformationItem.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this DataTransformationItem.

        数据转换描述

        :param description: The description of this DataTransformationItem.
        :type description: str
        """
        self._description = description

    @property
    def job_mode(self):
        r"""Gets the job_mode of this DataTransformationItem.

        :return: The job_mode of this DataTransformationItem.
        :rtype: :class:`huaweicloudsdksecmaster.v2.IsapJobMode`
        """
        return self._job_mode

    @job_mode.setter
    def job_mode(self, job_mode):
        r"""Sets the job_mode of this DataTransformationItem.

        :param job_mode: The job_mode of this DataTransformationItem.
        :type job_mode: :class:`huaweicloudsdksecmaster.v2.IsapJobMode`
        """
        self._job_mode = job_mode

    @property
    def process_status(self):
        r"""Gets the process_status of this DataTransformationItem.

        :return: The process_status of this DataTransformationItem.
        :rtype: :class:`huaweicloudsdksecmaster.v2.JobProcessStatus`
        """
        return self._process_status

    @process_status.setter
    def process_status(self, process_status):
        r"""Sets the process_status of this DataTransformationItem.

        :param process_status: The process_status of this DataTransformationItem.
        :type process_status: :class:`huaweicloudsdksecmaster.v2.JobProcessStatus`
        """
        self._process_status = process_status

    @property
    def process_error(self):
        r"""Gets the process_error of this DataTransformationItem.

        :return: The process_error of this DataTransformationItem.
        :rtype: :class:`huaweicloudsdksecmaster.v2.DataTransformationProcessError`
        """
        return self._process_error

    @process_error.setter
    def process_error(self, process_error):
        r"""Sets the process_error of this DataTransformationItem.

        :param process_error: The process_error of this DataTransformationItem.
        :type process_error: :class:`huaweicloudsdksecmaster.v2.DataTransformationProcessError`
        """
        self._process_error = process_error

    @property
    def environment(self):
        r"""Gets the environment of this DataTransformationItem.

        :return: The environment of this DataTransformationItem.
        :rtype: :class:`huaweicloudsdksecmaster.v2.JobEnvironment`
        """
        return self._environment

    @environment.setter
    def environment(self, environment):
        r"""Sets the environment of this DataTransformationItem.

        :param environment: The environment of this DataTransformationItem.
        :type environment: :class:`huaweicloudsdksecmaster.v2.JobEnvironment`
        """
        self._environment = environment

    @property
    def output_table_id(self):
        r"""Gets the output_table_id of this DataTransformationItem.

        UUID

        :return: The output_table_id of this DataTransformationItem.
        :rtype: str
        """
        return self._output_table_id

    @output_table_id.setter
    def output_table_id(self, output_table_id):
        r"""Sets the output_table_id of this DataTransformationItem.

        UUID

        :param output_table_id: The output_table_id of this DataTransformationItem.
        :type output_table_id: str
        """
        self._output_table_id = output_table_id

    @property
    def output_table_name(self):
        r"""Gets the output_table_name of this DataTransformationItem.

        表名称

        :return: The output_table_name of this DataTransformationItem.
        :rtype: str
        """
        return self._output_table_name

    @output_table_name.setter
    def output_table_name(self, output_table_name):
        r"""Sets the output_table_name of this DataTransformationItem.

        表名称

        :param output_table_name: The output_table_name of this DataTransformationItem.
        :type output_table_name: str
        """
        self._output_table_name = output_table_name

    @property
    def output_table_ids(self):
        r"""Gets the output_table_ids of this DataTransformationItem.

        输出表ID列表

        :return: The output_table_ids of this DataTransformationItem.
        :rtype: list[str]
        """
        return self._output_table_ids

    @output_table_ids.setter
    def output_table_ids(self, output_table_ids):
        r"""Sets the output_table_ids of this DataTransformationItem.

        输出表ID列表

        :param output_table_ids: The output_table_ids of this DataTransformationItem.
        :type output_table_ids: list[str]
        """
        self._output_table_ids = output_table_ids

    @property
    def output_table_names(self):
        r"""Gets the output_table_names of this DataTransformationItem.

        输出表名称列表

        :return: The output_table_names of this DataTransformationItem.
        :rtype: list[str]
        """
        return self._output_table_names

    @output_table_names.setter
    def output_table_names(self, output_table_names):
        r"""Sets the output_table_names of this DataTransformationItem.

        输出表名称列表

        :param output_table_names: The output_table_names of this DataTransformationItem.
        :type output_table_names: list[str]
        """
        self._output_table_names = output_table_names

    @property
    def create_by(self):
        r"""Gets the create_by of this DataTransformationItem.

        创建者

        :return: The create_by of this DataTransformationItem.
        :rtype: str
        """
        return self._create_by

    @create_by.setter
    def create_by(self, create_by):
        r"""Sets the create_by of this DataTransformationItem.

        创建者

        :param create_by: The create_by of this DataTransformationItem.
        :type create_by: str
        """
        self._create_by = create_by

    @property
    def create_time(self):
        r"""Gets the create_time of this DataTransformationItem.

        毫秒时间戳

        :return: The create_time of this DataTransformationItem.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this DataTransformationItem.

        毫秒时间戳

        :param create_time: The create_time of this DataTransformationItem.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def update_by(self):
        r"""Gets the update_by of this DataTransformationItem.

        更新者

        :return: The update_by of this DataTransformationItem.
        :rtype: str
        """
        return self._update_by

    @update_by.setter
    def update_by(self, update_by):
        r"""Sets the update_by of this DataTransformationItem.

        更新者

        :param update_by: The update_by of this DataTransformationItem.
        :type update_by: str
        """
        self._update_by = update_by

    @property
    def update_time(self):
        r"""Gets the update_time of this DataTransformationItem.

        毫秒时间戳

        :return: The update_time of this DataTransformationItem.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this DataTransformationItem.

        毫秒时间戳

        :param update_time: The update_time of this DataTransformationItem.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def delete_time(self):
        r"""Gets the delete_time of this DataTransformationItem.

        毫秒时间戳

        :return: The delete_time of this DataTransformationItem.
        :rtype: int
        """
        return self._delete_time

    @delete_time.setter
    def delete_time(self, delete_time):
        r"""Sets the delete_time of this DataTransformationItem.

        毫秒时间戳

        :param delete_time: The delete_time of this DataTransformationItem.
        :type delete_time: int
        """
        self._delete_time = delete_time

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
        if not isinstance(other, DataTransformationItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
