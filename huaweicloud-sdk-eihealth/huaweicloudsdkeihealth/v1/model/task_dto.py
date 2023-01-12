# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskDto:

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
        'app_id': 'str',
        'display_name': 'str',
        'output_dir': 'str',
        'resources': 'TaskResourceDto',
        'location': 'VertexLocationDto',
        'inputs': 'list[TaskParameterDto]'
    }

    attribute_map = {
        'task_name': 'task_name',
        'app_id': 'app_id',
        'display_name': 'display_name',
        'output_dir': 'output_dir',
        'resources': 'resources',
        'location': 'location',
        'inputs': 'inputs'
    }

    def __init__(self, task_name=None, app_id=None, display_name=None, output_dir=None, resources=None, location=None, inputs=None):
        """TaskDto

        The model defined in huaweicloud sdk

        :param task_name: 子任务实际名称，取值范围[1,32]，只能以大小写字母开头，由大小写字母、数字、中划线（-）、下划线（_）组成，以大小写字符或数字结尾。
        :type task_name: str
        :param app_id: 应用id，取值范围[1,135]，正则先不能有中文，两种格式。特殊id，采用{app_name}::{app_version}::{src_project_name}格式，用于手动创建场景；其他场景，app_id为系统分配的唯一标识
        :type app_id: str
        :param display_name: 流程的子任务展示名称，最大长度64
        :type display_name: str
        :param output_dir: 子任务的输出存放路径，用户可显式指定;输出路径必须以斜杠（/）开头且不能以斜杠（/）结尾，不能包含两个以上相邻的斜杠（/），不能包含以下特殊字符：\\ : ; * ? &lt; \&quot; &gt; | 。其中单个文件夹名称不能以中划线（-）开头，不能以英文句号（.）或斜杠（/）或空格开头或结尾
        :type output_dir: str
        :param resources: 
        :type resources: :class:`huaweicloudsdkeihealth.v1.TaskResourceDto`
        :param location: 
        :type location: :class:`huaweicloudsdkeihealth.v1.VertexLocationDto`
        :param inputs: 任务的输入参数信息
        :type inputs: list[:class:`huaweicloudsdkeihealth.v1.TaskParameterDto`]
        """
        
        

        self._task_name = None
        self._app_id = None
        self._display_name = None
        self._output_dir = None
        self._resources = None
        self._location = None
        self._inputs = None
        self.discriminator = None

        self.task_name = task_name
        self.app_id = app_id
        if display_name is not None:
            self.display_name = display_name
        if output_dir is not None:
            self.output_dir = output_dir
        if resources is not None:
            self.resources = resources
        if location is not None:
            self.location = location
        if inputs is not None:
            self.inputs = inputs

    @property
    def task_name(self):
        """Gets the task_name of this TaskDto.

        子任务实际名称，取值范围[1,32]，只能以大小写字母开头，由大小写字母、数字、中划线（-）、下划线（_）组成，以大小写字符或数字结尾。

        :return: The task_name of this TaskDto.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        """Sets the task_name of this TaskDto.

        子任务实际名称，取值范围[1,32]，只能以大小写字母开头，由大小写字母、数字、中划线（-）、下划线（_）组成，以大小写字符或数字结尾。

        :param task_name: The task_name of this TaskDto.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def app_id(self):
        """Gets the app_id of this TaskDto.

        应用id，取值范围[1,135]，正则先不能有中文，两种格式。特殊id，采用{app_name}::{app_version}::{src_project_name}格式，用于手动创建场景；其他场景，app_id为系统分配的唯一标识

        :return: The app_id of this TaskDto.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this TaskDto.

        应用id，取值范围[1,135]，正则先不能有中文，两种格式。特殊id，采用{app_name}::{app_version}::{src_project_name}格式，用于手动创建场景；其他场景，app_id为系统分配的唯一标识

        :param app_id: The app_id of this TaskDto.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def display_name(self):
        """Gets the display_name of this TaskDto.

        流程的子任务展示名称，最大长度64

        :return: The display_name of this TaskDto.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this TaskDto.

        流程的子任务展示名称，最大长度64

        :param display_name: The display_name of this TaskDto.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def output_dir(self):
        """Gets the output_dir of this TaskDto.

        子任务的输出存放路径，用户可显式指定;输出路径必须以斜杠（/）开头且不能以斜杠（/）结尾，不能包含两个以上相邻的斜杠（/），不能包含以下特殊字符：\\ : ; * ? < \" > | 。其中单个文件夹名称不能以中划线（-）开头，不能以英文句号（.）或斜杠（/）或空格开头或结尾

        :return: The output_dir of this TaskDto.
        :rtype: str
        """
        return self._output_dir

    @output_dir.setter
    def output_dir(self, output_dir):
        """Sets the output_dir of this TaskDto.

        子任务的输出存放路径，用户可显式指定;输出路径必须以斜杠（/）开头且不能以斜杠（/）结尾，不能包含两个以上相邻的斜杠（/），不能包含以下特殊字符：\\ : ; * ? < \" > | 。其中单个文件夹名称不能以中划线（-）开头，不能以英文句号（.）或斜杠（/）或空格开头或结尾

        :param output_dir: The output_dir of this TaskDto.
        :type output_dir: str
        """
        self._output_dir = output_dir

    @property
    def resources(self):
        """Gets the resources of this TaskDto.

        :return: The resources of this TaskDto.
        :rtype: :class:`huaweicloudsdkeihealth.v1.TaskResourceDto`
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this TaskDto.

        :param resources: The resources of this TaskDto.
        :type resources: :class:`huaweicloudsdkeihealth.v1.TaskResourceDto`
        """
        self._resources = resources

    @property
    def location(self):
        """Gets the location of this TaskDto.

        :return: The location of this TaskDto.
        :rtype: :class:`huaweicloudsdkeihealth.v1.VertexLocationDto`
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this TaskDto.

        :param location: The location of this TaskDto.
        :type location: :class:`huaweicloudsdkeihealth.v1.VertexLocationDto`
        """
        self._location = location

    @property
    def inputs(self):
        """Gets the inputs of this TaskDto.

        任务的输入参数信息

        :return: The inputs of this TaskDto.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.TaskParameterDto`]
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        """Sets the inputs of this TaskDto.

        任务的输入参数信息

        :param inputs: The inputs of this TaskDto.
        :type inputs: list[:class:`huaweicloudsdkeihealth.v1.TaskParameterDto`]
        """
        self._inputs = inputs

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
        if not isinstance(other, TaskDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
