# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAppResponse(SdkResponse):

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
        'name': 'str',
        'version': 'str',
        'summary': 'str',
        'description': 'str',
        'labels': 'list[str]',
        'image': 'str',
        'commands': 'list[str]',
        'resources': 'ResourceDto',
        'inputs': 'list[AppInputParameterDto]',
        'outputs': 'list[AppOutputParameterDto]',
        'create_time': 'str',
        'update_time': 'str',
        'user_name': 'str',
        'source_project_name': 'str',
        'source_resource_id': 'str',
        'node_labels': 'list[str]',
        'icon': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'version': 'version',
        'summary': 'summary',
        'description': 'description',
        'labels': 'labels',
        'image': 'image',
        'commands': 'commands',
        'resources': 'resources',
        'inputs': 'inputs',
        'outputs': 'outputs',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'user_name': 'user_name',
        'source_project_name': 'source_project_name',
        'source_resource_id': 'source_resource_id',
        'node_labels': 'node_labels',
        'icon': 'icon'
    }

    def __init__(self, id=None, name=None, version=None, summary=None, description=None, labels=None, image=None, commands=None, resources=None, inputs=None, outputs=None, create_time=None, update_time=None, user_name=None, source_project_name=None, source_resource_id=None, node_labels=None, icon=None):
        """ShowAppResponse

        The model defined in huaweicloud sdk

        :param id: 应用id
        :type id: str
        :param name: 应用名称
        :type name: str
        :param version: 应用版本
        :type version: str
        :param summary: 应用短描述
        :type summary: str
        :param description: 应用描述
        :type description: str
        :param labels: 应用标签
        :type labels: list[str]
        :param image: 应用镜像
        :type image: str
        :param commands: 应用命令
        :type commands: list[str]
        :param resources: 
        :type resources: :class:`huaweicloudsdkeihealth.v1.ResourceDto`
        :param inputs: 应用的输入参数信息
        :type inputs: list[:class:`huaweicloudsdkeihealth.v1.AppInputParameterDto`]
        :param outputs: 应用的输出参数信息
        :type outputs: list[:class:`huaweicloudsdkeihealth.v1.AppOutputParameterDto`]
        :param create_time: 创建应用时间
        :type create_time: str
        :param update_time: 更新应用时间
        :type update_time: str
        :param user_name: 创建应用的用户名
        :type user_name: str
        :param source_project_name: 源项目名称
        :type source_project_name: str
        :param source_resource_id: 源资源id
        :type source_resource_id: str
        :param node_labels: 节点标签
        :type node_labels: list[str]
        :param icon: 图标base64编码
        :type icon: str
        """
        
        super(ShowAppResponse, self).__init__()

        self._id = None
        self._name = None
        self._version = None
        self._summary = None
        self._description = None
        self._labels = None
        self._image = None
        self._commands = None
        self._resources = None
        self._inputs = None
        self._outputs = None
        self._create_time = None
        self._update_time = None
        self._user_name = None
        self._source_project_name = None
        self._source_resource_id = None
        self._node_labels = None
        self._icon = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if version is not None:
            self.version = version
        if summary is not None:
            self.summary = summary
        if description is not None:
            self.description = description
        if labels is not None:
            self.labels = labels
        if image is not None:
            self.image = image
        if commands is not None:
            self.commands = commands
        if resources is not None:
            self.resources = resources
        if inputs is not None:
            self.inputs = inputs
        if outputs is not None:
            self.outputs = outputs
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if user_name is not None:
            self.user_name = user_name
        if source_project_name is not None:
            self.source_project_name = source_project_name
        if source_resource_id is not None:
            self.source_resource_id = source_resource_id
        if node_labels is not None:
            self.node_labels = node_labels
        if icon is not None:
            self.icon = icon

    @property
    def id(self):
        """Gets the id of this ShowAppResponse.

        应用id

        :return: The id of this ShowAppResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowAppResponse.

        应用id

        :param id: The id of this ShowAppResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ShowAppResponse.

        应用名称

        :return: The name of this ShowAppResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowAppResponse.

        应用名称

        :param name: The name of this ShowAppResponse.
        :type name: str
        """
        self._name = name

    @property
    def version(self):
        """Gets the version of this ShowAppResponse.

        应用版本

        :return: The version of this ShowAppResponse.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ShowAppResponse.

        应用版本

        :param version: The version of this ShowAppResponse.
        :type version: str
        """
        self._version = version

    @property
    def summary(self):
        """Gets the summary of this ShowAppResponse.

        应用短描述

        :return: The summary of this ShowAppResponse.
        :rtype: str
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this ShowAppResponse.

        应用短描述

        :param summary: The summary of this ShowAppResponse.
        :type summary: str
        """
        self._summary = summary

    @property
    def description(self):
        """Gets the description of this ShowAppResponse.

        应用描述

        :return: The description of this ShowAppResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ShowAppResponse.

        应用描述

        :param description: The description of this ShowAppResponse.
        :type description: str
        """
        self._description = description

    @property
    def labels(self):
        """Gets the labels of this ShowAppResponse.

        应用标签

        :return: The labels of this ShowAppResponse.
        :rtype: list[str]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this ShowAppResponse.

        应用标签

        :param labels: The labels of this ShowAppResponse.
        :type labels: list[str]
        """
        self._labels = labels

    @property
    def image(self):
        """Gets the image of this ShowAppResponse.

        应用镜像

        :return: The image of this ShowAppResponse.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this ShowAppResponse.

        应用镜像

        :param image: The image of this ShowAppResponse.
        :type image: str
        """
        self._image = image

    @property
    def commands(self):
        """Gets the commands of this ShowAppResponse.

        应用命令

        :return: The commands of this ShowAppResponse.
        :rtype: list[str]
        """
        return self._commands

    @commands.setter
    def commands(self, commands):
        """Sets the commands of this ShowAppResponse.

        应用命令

        :param commands: The commands of this ShowAppResponse.
        :type commands: list[str]
        """
        self._commands = commands

    @property
    def resources(self):
        """Gets the resources of this ShowAppResponse.


        :return: The resources of this ShowAppResponse.
        :rtype: :class:`huaweicloudsdkeihealth.v1.ResourceDto`
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this ShowAppResponse.


        :param resources: The resources of this ShowAppResponse.
        :type resources: :class:`huaweicloudsdkeihealth.v1.ResourceDto`
        """
        self._resources = resources

    @property
    def inputs(self):
        """Gets the inputs of this ShowAppResponse.

        应用的输入参数信息

        :return: The inputs of this ShowAppResponse.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.AppInputParameterDto`]
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        """Sets the inputs of this ShowAppResponse.

        应用的输入参数信息

        :param inputs: The inputs of this ShowAppResponse.
        :type inputs: list[:class:`huaweicloudsdkeihealth.v1.AppInputParameterDto`]
        """
        self._inputs = inputs

    @property
    def outputs(self):
        """Gets the outputs of this ShowAppResponse.

        应用的输出参数信息

        :return: The outputs of this ShowAppResponse.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.AppOutputParameterDto`]
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        """Sets the outputs of this ShowAppResponse.

        应用的输出参数信息

        :param outputs: The outputs of this ShowAppResponse.
        :type outputs: list[:class:`huaweicloudsdkeihealth.v1.AppOutputParameterDto`]
        """
        self._outputs = outputs

    @property
    def create_time(self):
        """Gets the create_time of this ShowAppResponse.

        创建应用时间

        :return: The create_time of this ShowAppResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ShowAppResponse.

        创建应用时间

        :param create_time: The create_time of this ShowAppResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this ShowAppResponse.

        更新应用时间

        :return: The update_time of this ShowAppResponse.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this ShowAppResponse.

        更新应用时间

        :param update_time: The update_time of this ShowAppResponse.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def user_name(self):
        """Gets the user_name of this ShowAppResponse.

        创建应用的用户名

        :return: The user_name of this ShowAppResponse.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this ShowAppResponse.

        创建应用的用户名

        :param user_name: The user_name of this ShowAppResponse.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def source_project_name(self):
        """Gets the source_project_name of this ShowAppResponse.

        源项目名称

        :return: The source_project_name of this ShowAppResponse.
        :rtype: str
        """
        return self._source_project_name

    @source_project_name.setter
    def source_project_name(self, source_project_name):
        """Sets the source_project_name of this ShowAppResponse.

        源项目名称

        :param source_project_name: The source_project_name of this ShowAppResponse.
        :type source_project_name: str
        """
        self._source_project_name = source_project_name

    @property
    def source_resource_id(self):
        """Gets the source_resource_id of this ShowAppResponse.

        源资源id

        :return: The source_resource_id of this ShowAppResponse.
        :rtype: str
        """
        return self._source_resource_id

    @source_resource_id.setter
    def source_resource_id(self, source_resource_id):
        """Sets the source_resource_id of this ShowAppResponse.

        源资源id

        :param source_resource_id: The source_resource_id of this ShowAppResponse.
        :type source_resource_id: str
        """
        self._source_resource_id = source_resource_id

    @property
    def node_labels(self):
        """Gets the node_labels of this ShowAppResponse.

        节点标签

        :return: The node_labels of this ShowAppResponse.
        :rtype: list[str]
        """
        return self._node_labels

    @node_labels.setter
    def node_labels(self, node_labels):
        """Sets the node_labels of this ShowAppResponse.

        节点标签

        :param node_labels: The node_labels of this ShowAppResponse.
        :type node_labels: list[str]
        """
        self._node_labels = node_labels

    @property
    def icon(self):
        """Gets the icon of this ShowAppResponse.

        图标base64编码

        :return: The icon of this ShowAppResponse.
        :rtype: str
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        """Sets the icon of this ShowAppResponse.

        图标base64编码

        :param icon: The icon of this ShowAppResponse.
        :type icon: str
        """
        self._icon = icon

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
        if not isinstance(other, ShowAppResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
