# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskDefinitionDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_name': 'str',
        'display_name': 'str',
        'output_dir': 'str',
        'whole_output_dir': 'str',
        'io_acc_type': 'str',
        'resources': 'TaskResourceDto',
        'location': 'VertexLocationDto',
        'inputs': 'list[TaskParameterDto]',
        'app_info': 'AppInfoDto'
    }

    attribute_map = {
        'task_name': 'task_name',
        'display_name': 'display_name',
        'output_dir': 'output_dir',
        'whole_output_dir': 'whole_output_dir',
        'io_acc_type': 'io_acc_type',
        'resources': 'resources',
        'location': 'location',
        'inputs': 'inputs',
        'app_info': 'app_info'
    }

    def __init__(self, task_name=None, display_name=None, output_dir=None, whole_output_dir=None, io_acc_type=None, resources=None, location=None, inputs=None, app_info=None):
        """TaskDefinitionDto

        The model defined in huaweicloud sdk

        :param task_name: 子任务实际名称
        :type task_name: str
        :param display_name: 流程的子任务展示名称
        :type display_name: str
        :param output_dir: 子任务的输出存放路径
        :type output_dir: str
        :param whole_output_dir: 子任务的完整输出路径，查看流程不会返回，查看作业时才会返回完整输出路径
        :type whole_output_dir: str
        :param io_acc_type: 子任务使用的IO加速类型，不填表示不使用；
        :type io_acc_type: str
        :param resources: 
        :type resources: :class:`huaweicloudsdkeihealth.v1.TaskResourceDto`
        :param location: 
        :type location: :class:`huaweicloudsdkeihealth.v1.VertexLocationDto`
        :param inputs: 子任务的输入参数信息
        :type inputs: list[:class:`huaweicloudsdkeihealth.v1.TaskParameterDto`]
        :param app_info: 
        :type app_info: :class:`huaweicloudsdkeihealth.v1.AppInfoDto`
        """
        
        

        self._task_name = None
        self._display_name = None
        self._output_dir = None
        self._whole_output_dir = None
        self._io_acc_type = None
        self._resources = None
        self._location = None
        self._inputs = None
        self._app_info = None
        self.discriminator = None

        if task_name is not None:
            self.task_name = task_name
        if display_name is not None:
            self.display_name = display_name
        if output_dir is not None:
            self.output_dir = output_dir
        if whole_output_dir is not None:
            self.whole_output_dir = whole_output_dir
        if io_acc_type is not None:
            self.io_acc_type = io_acc_type
        if resources is not None:
            self.resources = resources
        if location is not None:
            self.location = location
        if inputs is not None:
            self.inputs = inputs
        if app_info is not None:
            self.app_info = app_info

    @property
    def task_name(self):
        """Gets the task_name of this TaskDefinitionDto.

        子任务实际名称

        :return: The task_name of this TaskDefinitionDto.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        """Sets the task_name of this TaskDefinitionDto.

        子任务实际名称

        :param task_name: The task_name of this TaskDefinitionDto.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def display_name(self):
        """Gets the display_name of this TaskDefinitionDto.

        流程的子任务展示名称

        :return: The display_name of this TaskDefinitionDto.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this TaskDefinitionDto.

        流程的子任务展示名称

        :param display_name: The display_name of this TaskDefinitionDto.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def output_dir(self):
        """Gets the output_dir of this TaskDefinitionDto.

        子任务的输出存放路径

        :return: The output_dir of this TaskDefinitionDto.
        :rtype: str
        """
        return self._output_dir

    @output_dir.setter
    def output_dir(self, output_dir):
        """Sets the output_dir of this TaskDefinitionDto.

        子任务的输出存放路径

        :param output_dir: The output_dir of this TaskDefinitionDto.
        :type output_dir: str
        """
        self._output_dir = output_dir

    @property
    def whole_output_dir(self):
        """Gets the whole_output_dir of this TaskDefinitionDto.

        子任务的完整输出路径，查看流程不会返回，查看作业时才会返回完整输出路径

        :return: The whole_output_dir of this TaskDefinitionDto.
        :rtype: str
        """
        return self._whole_output_dir

    @whole_output_dir.setter
    def whole_output_dir(self, whole_output_dir):
        """Sets the whole_output_dir of this TaskDefinitionDto.

        子任务的完整输出路径，查看流程不会返回，查看作业时才会返回完整输出路径

        :param whole_output_dir: The whole_output_dir of this TaskDefinitionDto.
        :type whole_output_dir: str
        """
        self._whole_output_dir = whole_output_dir

    @property
    def io_acc_type(self):
        """Gets the io_acc_type of this TaskDefinitionDto.

        子任务使用的IO加速类型，不填表示不使用；

        :return: The io_acc_type of this TaskDefinitionDto.
        :rtype: str
        """
        return self._io_acc_type

    @io_acc_type.setter
    def io_acc_type(self, io_acc_type):
        """Sets the io_acc_type of this TaskDefinitionDto.

        子任务使用的IO加速类型，不填表示不使用；

        :param io_acc_type: The io_acc_type of this TaskDefinitionDto.
        :type io_acc_type: str
        """
        self._io_acc_type = io_acc_type

    @property
    def resources(self):
        """Gets the resources of this TaskDefinitionDto.

        :return: The resources of this TaskDefinitionDto.
        :rtype: :class:`huaweicloudsdkeihealth.v1.TaskResourceDto`
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this TaskDefinitionDto.

        :param resources: The resources of this TaskDefinitionDto.
        :type resources: :class:`huaweicloudsdkeihealth.v1.TaskResourceDto`
        """
        self._resources = resources

    @property
    def location(self):
        """Gets the location of this TaskDefinitionDto.

        :return: The location of this TaskDefinitionDto.
        :rtype: :class:`huaweicloudsdkeihealth.v1.VertexLocationDto`
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this TaskDefinitionDto.

        :param location: The location of this TaskDefinitionDto.
        :type location: :class:`huaweicloudsdkeihealth.v1.VertexLocationDto`
        """
        self._location = location

    @property
    def inputs(self):
        """Gets the inputs of this TaskDefinitionDto.

        子任务的输入参数信息

        :return: The inputs of this TaskDefinitionDto.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.TaskParameterDto`]
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        """Sets the inputs of this TaskDefinitionDto.

        子任务的输入参数信息

        :param inputs: The inputs of this TaskDefinitionDto.
        :type inputs: list[:class:`huaweicloudsdkeihealth.v1.TaskParameterDto`]
        """
        self._inputs = inputs

    @property
    def app_info(self):
        """Gets the app_info of this TaskDefinitionDto.

        :return: The app_info of this TaskDefinitionDto.
        :rtype: :class:`huaweicloudsdkeihealth.v1.AppInfoDto`
        """
        return self._app_info

    @app_info.setter
    def app_info(self, app_info):
        """Sets the app_info of this TaskDefinitionDto.

        :param app_info: The app_info of this TaskDefinitionDto.
        :type app_info: :class:`huaweicloudsdkeihealth.v1.AppInfoDto`
        """
        self._app_info = app_info

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
        if not isinstance(other, TaskDefinitionDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
