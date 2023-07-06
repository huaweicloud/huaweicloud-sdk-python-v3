# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConfigTaskParameterBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'check_id': 'int',
        'ruleset_id': 'str',
        'language': 'str',
        'status': 'str',
        'task_check_settings': 'list[TaskCheckSettingsItem]'
    }

    attribute_map = {
        'check_id': 'check_id',
        'ruleset_id': 'ruleset_id',
        'language': 'language',
        'status': 'status',
        'task_check_settings': 'task_check_settings'
    }

    def __init__(self, check_id=None, ruleset_id=None, language=None, status=None, task_check_settings=None):
        """ConfigTaskParameterBody

        The model defined in huaweicloud sdk

        :param check_id: 检查工具ID
        :type check_id: int
        :param ruleset_id: 规则集ID
        :type ruleset_id: str
        :param language: 规则集语言
        :type language: str
        :param status: off：关闭，on：开启
        :type status: str
        :param task_check_settings: 检查参数信息
        :type task_check_settings: list[:class:`huaweicloudsdkcodeartscheck.v2.TaskCheckSettingsItem`]
        """
        
        

        self._check_id = None
        self._ruleset_id = None
        self._language = None
        self._status = None
        self._task_check_settings = None
        self.discriminator = None

        self.check_id = check_id
        self.ruleset_id = ruleset_id
        self.language = language
        self.status = status
        self.task_check_settings = task_check_settings

    @property
    def check_id(self):
        """Gets the check_id of this ConfigTaskParameterBody.

        检查工具ID

        :return: The check_id of this ConfigTaskParameterBody.
        :rtype: int
        """
        return self._check_id

    @check_id.setter
    def check_id(self, check_id):
        """Sets the check_id of this ConfigTaskParameterBody.

        检查工具ID

        :param check_id: The check_id of this ConfigTaskParameterBody.
        :type check_id: int
        """
        self._check_id = check_id

    @property
    def ruleset_id(self):
        """Gets the ruleset_id of this ConfigTaskParameterBody.

        规则集ID

        :return: The ruleset_id of this ConfigTaskParameterBody.
        :rtype: str
        """
        return self._ruleset_id

    @ruleset_id.setter
    def ruleset_id(self, ruleset_id):
        """Sets the ruleset_id of this ConfigTaskParameterBody.

        规则集ID

        :param ruleset_id: The ruleset_id of this ConfigTaskParameterBody.
        :type ruleset_id: str
        """
        self._ruleset_id = ruleset_id

    @property
    def language(self):
        """Gets the language of this ConfigTaskParameterBody.

        规则集语言

        :return: The language of this ConfigTaskParameterBody.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this ConfigTaskParameterBody.

        规则集语言

        :param language: The language of this ConfigTaskParameterBody.
        :type language: str
        """
        self._language = language

    @property
    def status(self):
        """Gets the status of this ConfigTaskParameterBody.

        off：关闭，on：开启

        :return: The status of this ConfigTaskParameterBody.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ConfigTaskParameterBody.

        off：关闭，on：开启

        :param status: The status of this ConfigTaskParameterBody.
        :type status: str
        """
        self._status = status

    @property
    def task_check_settings(self):
        """Gets the task_check_settings of this ConfigTaskParameterBody.

        检查参数信息

        :return: The task_check_settings of this ConfigTaskParameterBody.
        :rtype: list[:class:`huaweicloudsdkcodeartscheck.v2.TaskCheckSettingsItem`]
        """
        return self._task_check_settings

    @task_check_settings.setter
    def task_check_settings(self, task_check_settings):
        """Sets the task_check_settings of this ConfigTaskParameterBody.

        检查参数信息

        :param task_check_settings: The task_check_settings of this ConfigTaskParameterBody.
        :type task_check_settings: list[:class:`huaweicloudsdkcodeartscheck.v2.TaskCheckSettingsItem`]
        """
        self._task_check_settings = task_check_settings

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
        if not isinstance(other, ConfigTaskParameterBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
