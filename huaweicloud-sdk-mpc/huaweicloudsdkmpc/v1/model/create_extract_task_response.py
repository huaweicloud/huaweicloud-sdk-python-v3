# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateExtractTaskResponse(SdkResponse):

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
        'output': 'ObsObjInfo',
        'output_file_name': 'str',
        'description': 'str',
        'metadata': 'MetaData'
    }

    attribute_map = {
        'task_id': 'task_id',
        'status': 'status',
        'create_time': 'create_time',
        'output': 'output',
        'output_file_name': 'output_file_name',
        'description': 'description',
        'metadata': 'metadata'
    }

    def __init__(self, task_id=None, status=None, create_time=None, output=None, output_file_name=None, description=None, metadata=None):
        """CreateExtractTaskResponse

        The model defined in huaweicloud sdk

        :param task_id: 任务ID 
        :type task_id: str
        :param status: 任务状态
        :type status: str
        :param create_time: 任务创建时间
        :type create_time: str
        :param output: 
        :type output: :class:`huaweicloudsdkmpc.v1.ObsObjInfo`
        :param output_file_name: 解析文件名称
        :type output_file_name: str
        :param description: 任务描述，如当任务异常时，此字段为异常的具体信息
        :type description: str
        :param metadata: 
        :type metadata: :class:`huaweicloudsdkmpc.v1.MetaData`
        """
        
        super(CreateExtractTaskResponse, self).__init__()

        self._task_id = None
        self._status = None
        self._create_time = None
        self._output = None
        self._output_file_name = None
        self._description = None
        self._metadata = None
        self.discriminator = None

        if task_id is not None:
            self.task_id = task_id
        if status is not None:
            self.status = status
        if create_time is not None:
            self.create_time = create_time
        if output is not None:
            self.output = output
        if output_file_name is not None:
            self.output_file_name = output_file_name
        if description is not None:
            self.description = description
        if metadata is not None:
            self.metadata = metadata

    @property
    def task_id(self):
        """Gets the task_id of this CreateExtractTaskResponse.

        任务ID 

        :return: The task_id of this CreateExtractTaskResponse.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this CreateExtractTaskResponse.

        任务ID 

        :param task_id: The task_id of this CreateExtractTaskResponse.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def status(self):
        """Gets the status of this CreateExtractTaskResponse.

        任务状态

        :return: The status of this CreateExtractTaskResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CreateExtractTaskResponse.

        任务状态

        :param status: The status of this CreateExtractTaskResponse.
        :type status: str
        """
        self._status = status

    @property
    def create_time(self):
        """Gets the create_time of this CreateExtractTaskResponse.

        任务创建时间

        :return: The create_time of this CreateExtractTaskResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this CreateExtractTaskResponse.

        任务创建时间

        :param create_time: The create_time of this CreateExtractTaskResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def output(self):
        """Gets the output of this CreateExtractTaskResponse.

        :return: The output of this CreateExtractTaskResponse.
        :rtype: :class:`huaweicloudsdkmpc.v1.ObsObjInfo`
        """
        return self._output

    @output.setter
    def output(self, output):
        """Sets the output of this CreateExtractTaskResponse.

        :param output: The output of this CreateExtractTaskResponse.
        :type output: :class:`huaweicloudsdkmpc.v1.ObsObjInfo`
        """
        self._output = output

    @property
    def output_file_name(self):
        """Gets the output_file_name of this CreateExtractTaskResponse.

        解析文件名称

        :return: The output_file_name of this CreateExtractTaskResponse.
        :rtype: str
        """
        return self._output_file_name

    @output_file_name.setter
    def output_file_name(self, output_file_name):
        """Sets the output_file_name of this CreateExtractTaskResponse.

        解析文件名称

        :param output_file_name: The output_file_name of this CreateExtractTaskResponse.
        :type output_file_name: str
        """
        self._output_file_name = output_file_name

    @property
    def description(self):
        """Gets the description of this CreateExtractTaskResponse.

        任务描述，如当任务异常时，此字段为异常的具体信息

        :return: The description of this CreateExtractTaskResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateExtractTaskResponse.

        任务描述，如当任务异常时，此字段为异常的具体信息

        :param description: The description of this CreateExtractTaskResponse.
        :type description: str
        """
        self._description = description

    @property
    def metadata(self):
        """Gets the metadata of this CreateExtractTaskResponse.

        :return: The metadata of this CreateExtractTaskResponse.
        :rtype: :class:`huaweicloudsdkmpc.v1.MetaData`
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this CreateExtractTaskResponse.

        :param metadata: The metadata of this CreateExtractTaskResponse.
        :type metadata: :class:`huaweicloudsdkmpc.v1.MetaData`
        """
        self._metadata = metadata

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
        if not isinstance(other, CreateExtractTaskResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
