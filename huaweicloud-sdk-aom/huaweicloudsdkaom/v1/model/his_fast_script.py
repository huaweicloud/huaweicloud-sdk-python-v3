# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HISFastScript:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'script_type': 'str',
        'cmd_user': 'str',
        'script_content': 'str',
        'ecs_id_list': 'str',
        'name': 'str',
        'project_id': 'str',
        'script_args': 'str'
    }

    attribute_map = {
        'script_type': 'script_type',
        'cmd_user': 'cmd_user',
        'script_content': 'script_content',
        'ecs_id_list': 'ecs_id_list',
        'name': 'name',
        'project_id': 'project_id',
        'script_args': 'script_args'
    }

    def __init__(self, script_type=None, cmd_user=None, script_content=None, ecs_id_list=None, name=None, project_id=None, script_args=None):
        """HISFastScript

        The model defined in huaweicloud sdk

        :param script_type: 脚本类型。
        :type script_type: str
        :param cmd_user: 执行脚本的ECS机器用户。
        :type cmd_user: str
        :param script_content: 脚本内容。
        :type script_content: str
        :param ecs_id_list: 执行的机器列表。
        :type ecs_id_list: str
        :param name: 任务名称。
        :type name: str
        :param project_id: 项目ID。
        :type project_id: str
        :param script_args: 任务参数，多个参数以空格分隔。
        :type script_args: str
        """
        
        

        self._script_type = None
        self._cmd_user = None
        self._script_content = None
        self._ecs_id_list = None
        self._name = None
        self._project_id = None
        self._script_args = None
        self.discriminator = None

        self.script_type = script_type
        self.cmd_user = cmd_user
        self.script_content = script_content
        self.ecs_id_list = ecs_id_list
        self.name = name
        self.project_id = project_id
        if script_args is not None:
            self.script_args = script_args

    @property
    def script_type(self):
        """Gets the script_type of this HISFastScript.

        脚本类型。

        :return: The script_type of this HISFastScript.
        :rtype: str
        """
        return self._script_type

    @script_type.setter
    def script_type(self, script_type):
        """Sets the script_type of this HISFastScript.

        脚本类型。

        :param script_type: The script_type of this HISFastScript.
        :type script_type: str
        """
        self._script_type = script_type

    @property
    def cmd_user(self):
        """Gets the cmd_user of this HISFastScript.

        执行脚本的ECS机器用户。

        :return: The cmd_user of this HISFastScript.
        :rtype: str
        """
        return self._cmd_user

    @cmd_user.setter
    def cmd_user(self, cmd_user):
        """Sets the cmd_user of this HISFastScript.

        执行脚本的ECS机器用户。

        :param cmd_user: The cmd_user of this HISFastScript.
        :type cmd_user: str
        """
        self._cmd_user = cmd_user

    @property
    def script_content(self):
        """Gets the script_content of this HISFastScript.

        脚本内容。

        :return: The script_content of this HISFastScript.
        :rtype: str
        """
        return self._script_content

    @script_content.setter
    def script_content(self, script_content):
        """Sets the script_content of this HISFastScript.

        脚本内容。

        :param script_content: The script_content of this HISFastScript.
        :type script_content: str
        """
        self._script_content = script_content

    @property
    def ecs_id_list(self):
        """Gets the ecs_id_list of this HISFastScript.

        执行的机器列表。

        :return: The ecs_id_list of this HISFastScript.
        :rtype: str
        """
        return self._ecs_id_list

    @ecs_id_list.setter
    def ecs_id_list(self, ecs_id_list):
        """Sets the ecs_id_list of this HISFastScript.

        执行的机器列表。

        :param ecs_id_list: The ecs_id_list of this HISFastScript.
        :type ecs_id_list: str
        """
        self._ecs_id_list = ecs_id_list

    @property
    def name(self):
        """Gets the name of this HISFastScript.

        任务名称。

        :return: The name of this HISFastScript.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this HISFastScript.

        任务名称。

        :param name: The name of this HISFastScript.
        :type name: str
        """
        self._name = name

    @property
    def project_id(self):
        """Gets the project_id of this HISFastScript.

        项目ID。

        :return: The project_id of this HISFastScript.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this HISFastScript.

        项目ID。

        :param project_id: The project_id of this HISFastScript.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def script_args(self):
        """Gets the script_args of this HISFastScript.

        任务参数，多个参数以空格分隔。

        :return: The script_args of this HISFastScript.
        :rtype: str
        """
        return self._script_args

    @script_args.setter
    def script_args(self, script_args):
        """Sets the script_args of this HISFastScript.

        任务参数，多个参数以空格分隔。

        :param script_args: The script_args of this HISFastScript.
        :type script_args: str
        """
        self._script_args = script_args

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
        if not isinstance(other, HISFastScript):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
