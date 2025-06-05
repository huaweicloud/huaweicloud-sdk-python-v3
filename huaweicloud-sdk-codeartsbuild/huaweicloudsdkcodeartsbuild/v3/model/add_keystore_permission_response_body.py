# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddKeystorePermissionResponseBody:

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
        'setting': 'bool',
        'delete': 'bool',
        'keystore_id': 'str',
        'modify': 'bool',
        'usage': 'bool',
        'user_name': 'str',
        'is_creator': 'bool',
        'can_absent': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'setting': 'setting',
        'delete': 'delete',
        'keystore_id': 'keystore_id',
        'modify': 'modify',
        'usage': 'usage',
        'user_name': 'user_name',
        'is_creator': 'is_creator',
        'can_absent': 'can_absent'
    }

    def __init__(self, id=None, setting=None, delete=None, keystore_id=None, modify=None, usage=None, user_name=None, is_creator=None, can_absent=None):
        r"""AddKeystorePermissionResponseBody

        The model defined in huaweicloud sdk

        :param id: 权限id
        :type id: str
        :param setting: 编辑权限
        :type setting: bool
        :param delete: 是否有删除权限
        :type delete: bool
        :param keystore_id: 文件密钥id
        :type keystore_id: str
        :param modify: 是否有修改权限
        :type modify: bool
        :param usage: 是否有使用权限
        :type usage: bool
        :param user_name: 用户名
        :type user_name: str
        :param is_creator: 是否是创建者
        :type is_creator: bool
        :param can_absent: 是否可编辑
        :type can_absent: bool
        """
        
        

        self._id = None
        self._setting = None
        self._delete = None
        self._keystore_id = None
        self._modify = None
        self._usage = None
        self._user_name = None
        self._is_creator = None
        self._can_absent = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if setting is not None:
            self.setting = setting
        if delete is not None:
            self.delete = delete
        if keystore_id is not None:
            self.keystore_id = keystore_id
        if modify is not None:
            self.modify = modify
        if usage is not None:
            self.usage = usage
        if user_name is not None:
            self.user_name = user_name
        if is_creator is not None:
            self.is_creator = is_creator
        if can_absent is not None:
            self.can_absent = can_absent

    @property
    def id(self):
        r"""Gets the id of this AddKeystorePermissionResponseBody.

        权限id

        :return: The id of this AddKeystorePermissionResponseBody.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this AddKeystorePermissionResponseBody.

        权限id

        :param id: The id of this AddKeystorePermissionResponseBody.
        :type id: str
        """
        self._id = id

    @property
    def setting(self):
        r"""Gets the setting of this AddKeystorePermissionResponseBody.

        编辑权限

        :return: The setting of this AddKeystorePermissionResponseBody.
        :rtype: bool
        """
        return self._setting

    @setting.setter
    def setting(self, setting):
        r"""Sets the setting of this AddKeystorePermissionResponseBody.

        编辑权限

        :param setting: The setting of this AddKeystorePermissionResponseBody.
        :type setting: bool
        """
        self._setting = setting

    @property
    def delete(self):
        r"""Gets the delete of this AddKeystorePermissionResponseBody.

        是否有删除权限

        :return: The delete of this AddKeystorePermissionResponseBody.
        :rtype: bool
        """
        return self._delete

    @delete.setter
    def delete(self, delete):
        r"""Sets the delete of this AddKeystorePermissionResponseBody.

        是否有删除权限

        :param delete: The delete of this AddKeystorePermissionResponseBody.
        :type delete: bool
        """
        self._delete = delete

    @property
    def keystore_id(self):
        r"""Gets the keystore_id of this AddKeystorePermissionResponseBody.

        文件密钥id

        :return: The keystore_id of this AddKeystorePermissionResponseBody.
        :rtype: str
        """
        return self._keystore_id

    @keystore_id.setter
    def keystore_id(self, keystore_id):
        r"""Sets the keystore_id of this AddKeystorePermissionResponseBody.

        文件密钥id

        :param keystore_id: The keystore_id of this AddKeystorePermissionResponseBody.
        :type keystore_id: str
        """
        self._keystore_id = keystore_id

    @property
    def modify(self):
        r"""Gets the modify of this AddKeystorePermissionResponseBody.

        是否有修改权限

        :return: The modify of this AddKeystorePermissionResponseBody.
        :rtype: bool
        """
        return self._modify

    @modify.setter
    def modify(self, modify):
        r"""Sets the modify of this AddKeystorePermissionResponseBody.

        是否有修改权限

        :param modify: The modify of this AddKeystorePermissionResponseBody.
        :type modify: bool
        """
        self._modify = modify

    @property
    def usage(self):
        r"""Gets the usage of this AddKeystorePermissionResponseBody.

        是否有使用权限

        :return: The usage of this AddKeystorePermissionResponseBody.
        :rtype: bool
        """
        return self._usage

    @usage.setter
    def usage(self, usage):
        r"""Sets the usage of this AddKeystorePermissionResponseBody.

        是否有使用权限

        :param usage: The usage of this AddKeystorePermissionResponseBody.
        :type usage: bool
        """
        self._usage = usage

    @property
    def user_name(self):
        r"""Gets the user_name of this AddKeystorePermissionResponseBody.

        用户名

        :return: The user_name of this AddKeystorePermissionResponseBody.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this AddKeystorePermissionResponseBody.

        用户名

        :param user_name: The user_name of this AddKeystorePermissionResponseBody.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def is_creator(self):
        r"""Gets the is_creator of this AddKeystorePermissionResponseBody.

        是否是创建者

        :return: The is_creator of this AddKeystorePermissionResponseBody.
        :rtype: bool
        """
        return self._is_creator

    @is_creator.setter
    def is_creator(self, is_creator):
        r"""Sets the is_creator of this AddKeystorePermissionResponseBody.

        是否是创建者

        :param is_creator: The is_creator of this AddKeystorePermissionResponseBody.
        :type is_creator: bool
        """
        self._is_creator = is_creator

    @property
    def can_absent(self):
        r"""Gets the can_absent of this AddKeystorePermissionResponseBody.

        是否可编辑

        :return: The can_absent of this AddKeystorePermissionResponseBody.
        :rtype: bool
        """
        return self._can_absent

    @can_absent.setter
    def can_absent(self, can_absent):
        r"""Sets the can_absent of this AddKeystorePermissionResponseBody.

        是否可编辑

        :param can_absent: The can_absent of this AddKeystorePermissionResponseBody.
        :type can_absent: bool
        """
        self._can_absent = can_absent

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
        if not isinstance(other, AddKeystorePermissionResponseBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
