# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AttachUsersInfo:

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
        'user_group': 'str',
        'type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'user_group': 'user_group',
        'type': 'type'
    }

    def __init__(self, id=None, name=None, user_group=None, type=None):
        """AttachUsersInfo

        The model defined in huaweicloud sdk

        :param id: 当type字段为USER时，填写用户id；当type字段为GROUP时，填写用户组id，后端服务会校验组id是否存在；
        :type id: str
        :param name: 桌面分配对象的名称，当type类型USER时填写用户名字；当type类型GROUP时填写用户组名称。 - 当type类型USER时：桌面所属的用户，当桌面分配成功后此用户可以登录该桌面。只允许输入大写字母、小写字母、数字、中划线（-）和下划线（_）。域类型为LITE_AD时，使用小写字母或者大写字母开头，长度范围为[1-20]。当域类型为LOCAL_AD时，用户名可以使用小写字母或者大写字母或者数字开头，长度范围为[1-64]。Windows桌面用户最长支持20个字符，Linux桌面用户最长支持64个字符。后端服务会校验用户名是否存在，并且用户名不能与机器名重复。 - 当type类型GROUP时：只能为中文、字母、数字及特殊符号-_。
        :type name: str
        :param user_group: 桌面用户所属的用户组。 - sudo：Linux管理员组。 - default：Linux默认用户组。 - administrators：Windows管理员组。管理员拥有对该桌面的完全访问权，可以做任何需要的更改（禁用操作除外）。 - users：Windows标准用户组。标准用户可以使用大多数软件，并可以更改不影响其他用户的系统设置。
        :type user_group: str
        :param type: 对象类型，可选值为： - USER：用户。 - GROUP：用户组。
        :type type: str
        """
        
        

        self._id = None
        self._name = None
        self._user_group = None
        self._type = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if user_group is not None:
            self.user_group = user_group
        if type is not None:
            self.type = type

    @property
    def id(self):
        """Gets the id of this AttachUsersInfo.

        当type字段为USER时，填写用户id；当type字段为GROUP时，填写用户组id，后端服务会校验组id是否存在；

        :return: The id of this AttachUsersInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AttachUsersInfo.

        当type字段为USER时，填写用户id；当type字段为GROUP时，填写用户组id，后端服务会校验组id是否存在；

        :param id: The id of this AttachUsersInfo.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this AttachUsersInfo.

        桌面分配对象的名称，当type类型USER时填写用户名字；当type类型GROUP时填写用户组名称。 - 当type类型USER时：桌面所属的用户，当桌面分配成功后此用户可以登录该桌面。只允许输入大写字母、小写字母、数字、中划线（-）和下划线（_）。域类型为LITE_AD时，使用小写字母或者大写字母开头，长度范围为[1-20]。当域类型为LOCAL_AD时，用户名可以使用小写字母或者大写字母或者数字开头，长度范围为[1-64]。Windows桌面用户最长支持20个字符，Linux桌面用户最长支持64个字符。后端服务会校验用户名是否存在，并且用户名不能与机器名重复。 - 当type类型GROUP时：只能为中文、字母、数字及特殊符号-_。

        :return: The name of this AttachUsersInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AttachUsersInfo.

        桌面分配对象的名称，当type类型USER时填写用户名字；当type类型GROUP时填写用户组名称。 - 当type类型USER时：桌面所属的用户，当桌面分配成功后此用户可以登录该桌面。只允许输入大写字母、小写字母、数字、中划线（-）和下划线（_）。域类型为LITE_AD时，使用小写字母或者大写字母开头，长度范围为[1-20]。当域类型为LOCAL_AD时，用户名可以使用小写字母或者大写字母或者数字开头，长度范围为[1-64]。Windows桌面用户最长支持20个字符，Linux桌面用户最长支持64个字符。后端服务会校验用户名是否存在，并且用户名不能与机器名重复。 - 当type类型GROUP时：只能为中文、字母、数字及特殊符号-_。

        :param name: The name of this AttachUsersInfo.
        :type name: str
        """
        self._name = name

    @property
    def user_group(self):
        """Gets the user_group of this AttachUsersInfo.

        桌面用户所属的用户组。 - sudo：Linux管理员组。 - default：Linux默认用户组。 - administrators：Windows管理员组。管理员拥有对该桌面的完全访问权，可以做任何需要的更改（禁用操作除外）。 - users：Windows标准用户组。标准用户可以使用大多数软件，并可以更改不影响其他用户的系统设置。

        :return: The user_group of this AttachUsersInfo.
        :rtype: str
        """
        return self._user_group

    @user_group.setter
    def user_group(self, user_group):
        """Sets the user_group of this AttachUsersInfo.

        桌面用户所属的用户组。 - sudo：Linux管理员组。 - default：Linux默认用户组。 - administrators：Windows管理员组。管理员拥有对该桌面的完全访问权，可以做任何需要的更改（禁用操作除外）。 - users：Windows标准用户组。标准用户可以使用大多数软件，并可以更改不影响其他用户的系统设置。

        :param user_group: The user_group of this AttachUsersInfo.
        :type user_group: str
        """
        self._user_group = user_group

    @property
    def type(self):
        """Gets the type of this AttachUsersInfo.

        对象类型，可选值为： - USER：用户。 - GROUP：用户组。

        :return: The type of this AttachUsersInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AttachUsersInfo.

        对象类型，可选值为： - USER：用户。 - GROUP：用户组。

        :param type: The type of this AttachUsersInfo.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, AttachUsersInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
