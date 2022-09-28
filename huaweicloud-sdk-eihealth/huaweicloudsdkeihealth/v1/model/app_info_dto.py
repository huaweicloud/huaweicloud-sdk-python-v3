# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AppInfoDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'app_id': 'str',
        'app_name': 'str',
        'app_version': 'str',
        'app_src_project_name': 'str',
        'app_labels': 'list[str]',
        'app_summary': 'str',
        'app_description': 'str',
        'app_image': 'str',
        'app_commands': 'list[str]',
        'app_input_parameters': 'list[AppInputParameterDto]',
        'app_output_parameters': 'list[AppOutputParameterDto]',
        'app_node_labels': 'list[str]',
        'app_icon': 'str'
    }

    attribute_map = {
        'app_id': 'app_id',
        'app_name': 'app_name',
        'app_version': 'app_version',
        'app_src_project_name': 'app_src_project_name',
        'app_labels': 'app_labels',
        'app_summary': 'app_summary',
        'app_description': 'app_description',
        'app_image': 'app_image',
        'app_commands': 'app_commands',
        'app_input_parameters': 'app_input_parameters',
        'app_output_parameters': 'app_output_parameters',
        'app_node_labels': 'app_node_labels',
        'app_icon': 'app_icon'
    }

    def __init__(self, app_id=None, app_name=None, app_version=None, app_src_project_name=None, app_labels=None, app_summary=None, app_description=None, app_image=None, app_commands=None, app_input_parameters=None, app_output_parameters=None, app_node_labels=None, app_icon=None):
        """AppInfoDto

        The model defined in huaweicloud sdk

        :param app_id: 应用id
        :type app_id: str
        :param app_name: 应用名称
        :type app_name: str
        :param app_version: 应用版本
        :type app_version: str
        :param app_src_project_name: 应用来源项目名称
        :type app_src_project_name: str
        :param app_labels: 应用标签
        :type app_labels: list[str]
        :param app_summary: 应用简述
        :type app_summary: str
        :param app_description: 应用描述
        :type app_description: str
        :param app_image: 应用镜像
        :type app_image: str
        :param app_commands: 任务使用到的应用自带的命令信息
        :type app_commands: list[str]
        :param app_input_parameters: 任务使用到的应用自带的输入参数信息
        :type app_input_parameters: list[:class:`huaweicloudsdkeihealth.v1.AppInputParameterDto`]
        :param app_output_parameters: 任务使用到的应用自带的输出参数信息
        :type app_output_parameters: list[:class:`huaweicloudsdkeihealth.v1.AppOutputParameterDto`]
        :param app_node_labels: 计算节点标签
        :type app_node_labels: list[str]
        :param app_icon: 图标base64编码
        :type app_icon: str
        """
        
        

        self._app_id = None
        self._app_name = None
        self._app_version = None
        self._app_src_project_name = None
        self._app_labels = None
        self._app_summary = None
        self._app_description = None
        self._app_image = None
        self._app_commands = None
        self._app_input_parameters = None
        self._app_output_parameters = None
        self._app_node_labels = None
        self._app_icon = None
        self.discriminator = None

        if app_id is not None:
            self.app_id = app_id
        if app_name is not None:
            self.app_name = app_name
        if app_version is not None:
            self.app_version = app_version
        if app_src_project_name is not None:
            self.app_src_project_name = app_src_project_name
        if app_labels is not None:
            self.app_labels = app_labels
        if app_summary is not None:
            self.app_summary = app_summary
        if app_description is not None:
            self.app_description = app_description
        if app_image is not None:
            self.app_image = app_image
        if app_commands is not None:
            self.app_commands = app_commands
        if app_input_parameters is not None:
            self.app_input_parameters = app_input_parameters
        if app_output_parameters is not None:
            self.app_output_parameters = app_output_parameters
        if app_node_labels is not None:
            self.app_node_labels = app_node_labels
        if app_icon is not None:
            self.app_icon = app_icon

    @property
    def app_id(self):
        """Gets the app_id of this AppInfoDto.

        应用id

        :return: The app_id of this AppInfoDto.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this AppInfoDto.

        应用id

        :param app_id: The app_id of this AppInfoDto.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def app_name(self):
        """Gets the app_name of this AppInfoDto.

        应用名称

        :return: The app_name of this AppInfoDto.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        """Sets the app_name of this AppInfoDto.

        应用名称

        :param app_name: The app_name of this AppInfoDto.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def app_version(self):
        """Gets the app_version of this AppInfoDto.

        应用版本

        :return: The app_version of this AppInfoDto.
        :rtype: str
        """
        return self._app_version

    @app_version.setter
    def app_version(self, app_version):
        """Sets the app_version of this AppInfoDto.

        应用版本

        :param app_version: The app_version of this AppInfoDto.
        :type app_version: str
        """
        self._app_version = app_version

    @property
    def app_src_project_name(self):
        """Gets the app_src_project_name of this AppInfoDto.

        应用来源项目名称

        :return: The app_src_project_name of this AppInfoDto.
        :rtype: str
        """
        return self._app_src_project_name

    @app_src_project_name.setter
    def app_src_project_name(self, app_src_project_name):
        """Sets the app_src_project_name of this AppInfoDto.

        应用来源项目名称

        :param app_src_project_name: The app_src_project_name of this AppInfoDto.
        :type app_src_project_name: str
        """
        self._app_src_project_name = app_src_project_name

    @property
    def app_labels(self):
        """Gets the app_labels of this AppInfoDto.

        应用标签

        :return: The app_labels of this AppInfoDto.
        :rtype: list[str]
        """
        return self._app_labels

    @app_labels.setter
    def app_labels(self, app_labels):
        """Sets the app_labels of this AppInfoDto.

        应用标签

        :param app_labels: The app_labels of this AppInfoDto.
        :type app_labels: list[str]
        """
        self._app_labels = app_labels

    @property
    def app_summary(self):
        """Gets the app_summary of this AppInfoDto.

        应用简述

        :return: The app_summary of this AppInfoDto.
        :rtype: str
        """
        return self._app_summary

    @app_summary.setter
    def app_summary(self, app_summary):
        """Sets the app_summary of this AppInfoDto.

        应用简述

        :param app_summary: The app_summary of this AppInfoDto.
        :type app_summary: str
        """
        self._app_summary = app_summary

    @property
    def app_description(self):
        """Gets the app_description of this AppInfoDto.

        应用描述

        :return: The app_description of this AppInfoDto.
        :rtype: str
        """
        return self._app_description

    @app_description.setter
    def app_description(self, app_description):
        """Sets the app_description of this AppInfoDto.

        应用描述

        :param app_description: The app_description of this AppInfoDto.
        :type app_description: str
        """
        self._app_description = app_description

    @property
    def app_image(self):
        """Gets the app_image of this AppInfoDto.

        应用镜像

        :return: The app_image of this AppInfoDto.
        :rtype: str
        """
        return self._app_image

    @app_image.setter
    def app_image(self, app_image):
        """Sets the app_image of this AppInfoDto.

        应用镜像

        :param app_image: The app_image of this AppInfoDto.
        :type app_image: str
        """
        self._app_image = app_image

    @property
    def app_commands(self):
        """Gets the app_commands of this AppInfoDto.

        任务使用到的应用自带的命令信息

        :return: The app_commands of this AppInfoDto.
        :rtype: list[str]
        """
        return self._app_commands

    @app_commands.setter
    def app_commands(self, app_commands):
        """Sets the app_commands of this AppInfoDto.

        任务使用到的应用自带的命令信息

        :param app_commands: The app_commands of this AppInfoDto.
        :type app_commands: list[str]
        """
        self._app_commands = app_commands

    @property
    def app_input_parameters(self):
        """Gets the app_input_parameters of this AppInfoDto.

        任务使用到的应用自带的输入参数信息

        :return: The app_input_parameters of this AppInfoDto.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.AppInputParameterDto`]
        """
        return self._app_input_parameters

    @app_input_parameters.setter
    def app_input_parameters(self, app_input_parameters):
        """Sets the app_input_parameters of this AppInfoDto.

        任务使用到的应用自带的输入参数信息

        :param app_input_parameters: The app_input_parameters of this AppInfoDto.
        :type app_input_parameters: list[:class:`huaweicloudsdkeihealth.v1.AppInputParameterDto`]
        """
        self._app_input_parameters = app_input_parameters

    @property
    def app_output_parameters(self):
        """Gets the app_output_parameters of this AppInfoDto.

        任务使用到的应用自带的输出参数信息

        :return: The app_output_parameters of this AppInfoDto.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.AppOutputParameterDto`]
        """
        return self._app_output_parameters

    @app_output_parameters.setter
    def app_output_parameters(self, app_output_parameters):
        """Sets the app_output_parameters of this AppInfoDto.

        任务使用到的应用自带的输出参数信息

        :param app_output_parameters: The app_output_parameters of this AppInfoDto.
        :type app_output_parameters: list[:class:`huaweicloudsdkeihealth.v1.AppOutputParameterDto`]
        """
        self._app_output_parameters = app_output_parameters

    @property
    def app_node_labels(self):
        """Gets the app_node_labels of this AppInfoDto.

        计算节点标签

        :return: The app_node_labels of this AppInfoDto.
        :rtype: list[str]
        """
        return self._app_node_labels

    @app_node_labels.setter
    def app_node_labels(self, app_node_labels):
        """Sets the app_node_labels of this AppInfoDto.

        计算节点标签

        :param app_node_labels: The app_node_labels of this AppInfoDto.
        :type app_node_labels: list[str]
        """
        self._app_node_labels = app_node_labels

    @property
    def app_icon(self):
        """Gets the app_icon of this AppInfoDto.

        图标base64编码

        :return: The app_icon of this AppInfoDto.
        :rtype: str
        """
        return self._app_icon

    @app_icon.setter
    def app_icon(self, app_icon):
        """Sets the app_icon of this AppInfoDto.

        图标base64编码

        :param app_icon: The app_icon of this AppInfoDto.
        :type app_icon: str
        """
        self._app_icon = app_icon

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
        if not isinstance(other, AppInfoDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
