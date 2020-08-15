# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class CreateRemuxTaskResponse(SdkResponse):


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
        """CreateRemuxTaskResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

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
        """Gets the task_id of this CreateRemuxTaskResponse.

        任务ID 

        :return: The task_id of this CreateRemuxTaskResponse.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this CreateRemuxTaskResponse.

        任务ID 

        :param task_id: The task_id of this CreateRemuxTaskResponse.
        :type: str
        """
        self._task_id = task_id

    @property
    def status(self):
        """Gets the status of this CreateRemuxTaskResponse.

        任务状态

        :return: The status of this CreateRemuxTaskResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CreateRemuxTaskResponse.

        任务状态

        :param status: The status of this CreateRemuxTaskResponse.
        :type: str
        """
        self._status = status

    @property
    def create_time(self):
        """Gets the create_time of this CreateRemuxTaskResponse.

        任务创建时间

        :return: The create_time of this CreateRemuxTaskResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this CreateRemuxTaskResponse.

        任务创建时间

        :param create_time: The create_time of this CreateRemuxTaskResponse.
        :type: str
        """
        self._create_time = create_time

    @property
    def output(self):
        """Gets the output of this CreateRemuxTaskResponse.


        :return: The output of this CreateRemuxTaskResponse.
        :rtype: ObsObjInfo
        """
        return self._output

    @output.setter
    def output(self, output):
        """Sets the output of this CreateRemuxTaskResponse.


        :param output: The output of this CreateRemuxTaskResponse.
        :type: ObsObjInfo
        """
        self._output = output

    @property
    def output_file_name(self):
        """Gets the output_file_name of this CreateRemuxTaskResponse.

        解析文件名称

        :return: The output_file_name of this CreateRemuxTaskResponse.
        :rtype: str
        """
        return self._output_file_name

    @output_file_name.setter
    def output_file_name(self, output_file_name):
        """Sets the output_file_name of this CreateRemuxTaskResponse.

        解析文件名称

        :param output_file_name: The output_file_name of this CreateRemuxTaskResponse.
        :type: str
        """
        self._output_file_name = output_file_name

    @property
    def description(self):
        """Gets the description of this CreateRemuxTaskResponse.

        任务描述，如当任务异常时，此字段为异常的具体信息

        :return: The description of this CreateRemuxTaskResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateRemuxTaskResponse.

        任务描述，如当任务异常时，此字段为异常的具体信息

        :param description: The description of this CreateRemuxTaskResponse.
        :type: str
        """
        self._description = description

    @property
    def metadata(self):
        """Gets the metadata of this CreateRemuxTaskResponse.


        :return: The metadata of this CreateRemuxTaskResponse.
        :rtype: MetaData
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this CreateRemuxTaskResponse.


        :param metadata: The metadata of this CreateRemuxTaskResponse.
        :type: MetaData
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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateRemuxTaskResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
