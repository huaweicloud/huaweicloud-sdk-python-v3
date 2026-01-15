# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExportUsersNewReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'user_name': 'str',
        'description': 'str',
        'active_type': 'str',
        'language': 'str',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'user_name': 'user_name',
        'description': 'description',
        'active_type': 'active_type',
        'language': 'language',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, user_name=None, description=None, active_type=None, language=None, enterprise_project_id=None):
        r"""ExportUsersNewReq

        The model defined in huaweicloud sdk

        :param user_name: 桌面用户名，长度范围为1-20，不能包含特殊字符，不能以数字开头。支持模糊查询导出。
        :type user_name: str
        :param description: 描述，支持模糊查询导出。
        :type description: str
        :param active_type: 激活类型，默认为用户激活。 * USER_ACTIVATE： 用户激活 * ADMIN_ACTIVATE： 管理员激活
        :type active_type: str
        :param language: 语言，默认英文。 * zh_CN： 中文 * en_US： 英文
        :type language: str
        :param enterprise_project_id: 企业项目ID。
        :type enterprise_project_id: str
        """
        
        

        self._user_name = None
        self._description = None
        self._active_type = None
        self._language = None
        self._enterprise_project_id = None
        self.discriminator = None

        if user_name is not None:
            self.user_name = user_name
        if description is not None:
            self.description = description
        if active_type is not None:
            self.active_type = active_type
        if language is not None:
            self.language = language
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def user_name(self):
        r"""Gets the user_name of this ExportUsersNewReq.

        桌面用户名，长度范围为1-20，不能包含特殊字符，不能以数字开头。支持模糊查询导出。

        :return: The user_name of this ExportUsersNewReq.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this ExportUsersNewReq.

        桌面用户名，长度范围为1-20，不能包含特殊字符，不能以数字开头。支持模糊查询导出。

        :param user_name: The user_name of this ExportUsersNewReq.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def description(self):
        r"""Gets the description of this ExportUsersNewReq.

        描述，支持模糊查询导出。

        :return: The description of this ExportUsersNewReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ExportUsersNewReq.

        描述，支持模糊查询导出。

        :param description: The description of this ExportUsersNewReq.
        :type description: str
        """
        self._description = description

    @property
    def active_type(self):
        r"""Gets the active_type of this ExportUsersNewReq.

        激活类型，默认为用户激活。 * USER_ACTIVATE： 用户激活 * ADMIN_ACTIVATE： 管理员激活

        :return: The active_type of this ExportUsersNewReq.
        :rtype: str
        """
        return self._active_type

    @active_type.setter
    def active_type(self, active_type):
        r"""Sets the active_type of this ExportUsersNewReq.

        激活类型，默认为用户激活。 * USER_ACTIVATE： 用户激活 * ADMIN_ACTIVATE： 管理员激活

        :param active_type: The active_type of this ExportUsersNewReq.
        :type active_type: str
        """
        self._active_type = active_type

    @property
    def language(self):
        r"""Gets the language of this ExportUsersNewReq.

        语言，默认英文。 * zh_CN： 中文 * en_US： 英文

        :return: The language of this ExportUsersNewReq.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        r"""Sets the language of this ExportUsersNewReq.

        语言，默认英文。 * zh_CN： 中文 * en_US： 英文

        :param language: The language of this ExportUsersNewReq.
        :type language: str
        """
        self._language = language

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ExportUsersNewReq.

        企业项目ID。

        :return: The enterprise_project_id of this ExportUsersNewReq.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ExportUsersNewReq.

        企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this ExportUsersNewReq.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, ExportUsersNewReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
