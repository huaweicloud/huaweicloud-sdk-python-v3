# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AppDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
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
        'node_labels': 'list[str]',
        'icon': 'str'
    }

    attribute_map = {
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
        'node_labels': 'node_labels',
        'icon': 'icon'
    }

    def __init__(self, name=None, version=None, summary=None, description=None, labels=None, image=None, commands=None, resources=None, inputs=None, outputs=None, node_labels=None, icon=None):
        """AppDto

        The model defined in huaweicloud sdk

        :param name: 应用名称 目标应用名称 取值范围：长度为[1,56]，以大小写字母开头，允许出现中划线(-)、下划线(_)、小写字母和数字，且必须以大小写字母或数字结尾。
        :type name: str
        :param version: 应用版本 取值范围：[1,24]，以小写字母或数字或大写字母开头，允许出现中划线，必须以小写字母或数字或大写字母结尾。更新应用时，应用版本不支持修改。
        :type version: str
        :param summary: 应用简述 取值范围[0,128]
        :type summary: str
        :param description: 应用描述 取值范围[0,65535]，后续支持markdown文本
        :type description: str
        :param labels: 应用标签 取值范围[0,5]，单个标签最大长度32字符，仅仅包含小写字母或数字或大写字母
        :type labels: list[str]
        :param image: docker镜像地址 取值范围[1-255]，不能包含中文字符
        :type image: str
        :param commands: docker启动时执行命令 单个命令长度取值范围[1-1024]，不能包含中文字符
        :type commands: list[str]
        :param resources: 
        :type resources: :class:`huaweicloudsdkeihealth.v1.ResourceDto`
        :param inputs: 应用的输入参数列表
        :type inputs: list[:class:`huaweicloudsdkeihealth.v1.AppInputParameterDto`]
        :param outputs: 应用的输出参数列表
        :type outputs: list[:class:`huaweicloudsdkeihealth.v1.AppOutputParameterDto`]
        :param node_labels: 节点标签 取值范围[0,1]，单个标签最大长度63字符
        :type node_labels: list[str]
        :param icon: 图标base64编码
        :type icon: str
        """
        
        

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
        self._node_labels = None
        self._icon = None
        self.discriminator = None

        self.name = name
        self.version = version
        if summary is not None:
            self.summary = summary
        if description is not None:
            self.description = description
        if labels is not None:
            self.labels = labels
        self.image = image
        self.commands = commands
        if resources is not None:
            self.resources = resources
        if inputs is not None:
            self.inputs = inputs
        if outputs is not None:
            self.outputs = outputs
        if node_labels is not None:
            self.node_labels = node_labels
        if icon is not None:
            self.icon = icon

    @property
    def name(self):
        """Gets the name of this AppDto.

        应用名称 目标应用名称 取值范围：长度为[1,56]，以大小写字母开头，允许出现中划线(-)、下划线(_)、小写字母和数字，且必须以大小写字母或数字结尾。

        :return: The name of this AppDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AppDto.

        应用名称 目标应用名称 取值范围：长度为[1,56]，以大小写字母开头，允许出现中划线(-)、下划线(_)、小写字母和数字，且必须以大小写字母或数字结尾。

        :param name: The name of this AppDto.
        :type name: str
        """
        self._name = name

    @property
    def version(self):
        """Gets the version of this AppDto.

        应用版本 取值范围：[1,24]，以小写字母或数字或大写字母开头，允许出现中划线，必须以小写字母或数字或大写字母结尾。更新应用时，应用版本不支持修改。

        :return: The version of this AppDto.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this AppDto.

        应用版本 取值范围：[1,24]，以小写字母或数字或大写字母开头，允许出现中划线，必须以小写字母或数字或大写字母结尾。更新应用时，应用版本不支持修改。

        :param version: The version of this AppDto.
        :type version: str
        """
        self._version = version

    @property
    def summary(self):
        """Gets the summary of this AppDto.

        应用简述 取值范围[0,128]

        :return: The summary of this AppDto.
        :rtype: str
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this AppDto.

        应用简述 取值范围[0,128]

        :param summary: The summary of this AppDto.
        :type summary: str
        """
        self._summary = summary

    @property
    def description(self):
        """Gets the description of this AppDto.

        应用描述 取值范围[0,65535]，后续支持markdown文本

        :return: The description of this AppDto.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AppDto.

        应用描述 取值范围[0,65535]，后续支持markdown文本

        :param description: The description of this AppDto.
        :type description: str
        """
        self._description = description

    @property
    def labels(self):
        """Gets the labels of this AppDto.

        应用标签 取值范围[0,5]，单个标签最大长度32字符，仅仅包含小写字母或数字或大写字母

        :return: The labels of this AppDto.
        :rtype: list[str]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this AppDto.

        应用标签 取值范围[0,5]，单个标签最大长度32字符，仅仅包含小写字母或数字或大写字母

        :param labels: The labels of this AppDto.
        :type labels: list[str]
        """
        self._labels = labels

    @property
    def image(self):
        """Gets the image of this AppDto.

        docker镜像地址 取值范围[1-255]，不能包含中文字符

        :return: The image of this AppDto.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this AppDto.

        docker镜像地址 取值范围[1-255]，不能包含中文字符

        :param image: The image of this AppDto.
        :type image: str
        """
        self._image = image

    @property
    def commands(self):
        """Gets the commands of this AppDto.

        docker启动时执行命令 单个命令长度取值范围[1-1024]，不能包含中文字符

        :return: The commands of this AppDto.
        :rtype: list[str]
        """
        return self._commands

    @commands.setter
    def commands(self, commands):
        """Sets the commands of this AppDto.

        docker启动时执行命令 单个命令长度取值范围[1-1024]，不能包含中文字符

        :param commands: The commands of this AppDto.
        :type commands: list[str]
        """
        self._commands = commands

    @property
    def resources(self):
        """Gets the resources of this AppDto.

        :return: The resources of this AppDto.
        :rtype: :class:`huaweicloudsdkeihealth.v1.ResourceDto`
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this AppDto.

        :param resources: The resources of this AppDto.
        :type resources: :class:`huaweicloudsdkeihealth.v1.ResourceDto`
        """
        self._resources = resources

    @property
    def inputs(self):
        """Gets the inputs of this AppDto.

        应用的输入参数列表

        :return: The inputs of this AppDto.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.AppInputParameterDto`]
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        """Sets the inputs of this AppDto.

        应用的输入参数列表

        :param inputs: The inputs of this AppDto.
        :type inputs: list[:class:`huaweicloudsdkeihealth.v1.AppInputParameterDto`]
        """
        self._inputs = inputs

    @property
    def outputs(self):
        """Gets the outputs of this AppDto.

        应用的输出参数列表

        :return: The outputs of this AppDto.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.AppOutputParameterDto`]
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        """Sets the outputs of this AppDto.

        应用的输出参数列表

        :param outputs: The outputs of this AppDto.
        :type outputs: list[:class:`huaweicloudsdkeihealth.v1.AppOutputParameterDto`]
        """
        self._outputs = outputs

    @property
    def node_labels(self):
        """Gets the node_labels of this AppDto.

        节点标签 取值范围[0,1]，单个标签最大长度63字符

        :return: The node_labels of this AppDto.
        :rtype: list[str]
        """
        return self._node_labels

    @node_labels.setter
    def node_labels(self, node_labels):
        """Sets the node_labels of this AppDto.

        节点标签 取值范围[0,1]，单个标签最大长度63字符

        :param node_labels: The node_labels of this AppDto.
        :type node_labels: list[str]
        """
        self._node_labels = node_labels

    @property
    def icon(self):
        """Gets the icon of this AppDto.

        图标base64编码

        :return: The icon of this AppDto.
        :rtype: str
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        """Sets the icon of this AppDto.

        图标base64编码

        :param icon: The icon of this AppDto.
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
        if not isinstance(other, AppDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
