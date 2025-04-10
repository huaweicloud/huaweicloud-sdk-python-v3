# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TemplateV2:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'create_time': 'str',
        'creator_name': 'str',
        'creator_num': 'str',
        'description': 'str',
        'id': 'str',
        'is_default': 'str',
        'mindmap': 'str',
        'name': 'str',
        'update_time': 'str',
        'edit_permission': 'bool',
        'delete_permission': 'bool'
    }

    attribute_map = {
        'create_time': 'create_time',
        'creator_name': 'creator_name',
        'creator_num': 'creator_num',
        'description': 'description',
        'id': 'id',
        'is_default': 'is_default',
        'mindmap': 'mindmap',
        'name': 'name',
        'update_time': 'update_time',
        'edit_permission': 'editPermission',
        'delete_permission': 'deletePermission'
    }

    def __init__(self, create_time=None, creator_name=None, creator_num=None, description=None, id=None, is_default=None, mindmap=None, name=None, update_time=None, edit_permission=None, delete_permission=None):
        r"""TemplateV2

        The model defined in huaweicloud sdk

        :param create_time: 创建时间
        :type create_time: str
        :param creator_name: 创建人名称
        :type creator_name: str
        :param creator_num: 创建人工号
        :type creator_num: str
        :param description: 描述
        :type description: str
        :param id: id 主键
        :type id: str
        :param is_default: 是否默认
        :type is_default: str
        :param mindmap: 脑图json
        :type mindmap: str
        :param name: 名称
        :type name: str
        :param update_time: 更新时间
        :type update_time: str
        :param edit_permission: 编辑权限
        :type edit_permission: bool
        :param delete_permission: 删除权限
        :type delete_permission: bool
        """
        
        

        self._create_time = None
        self._creator_name = None
        self._creator_num = None
        self._description = None
        self._id = None
        self._is_default = None
        self._mindmap = None
        self._name = None
        self._update_time = None
        self._edit_permission = None
        self._delete_permission = None
        self.discriminator = None

        if create_time is not None:
            self.create_time = create_time
        if creator_name is not None:
            self.creator_name = creator_name
        if creator_num is not None:
            self.creator_num = creator_num
        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        if is_default is not None:
            self.is_default = is_default
        if mindmap is not None:
            self.mindmap = mindmap
        if name is not None:
            self.name = name
        if update_time is not None:
            self.update_time = update_time
        if edit_permission is not None:
            self.edit_permission = edit_permission
        if delete_permission is not None:
            self.delete_permission = delete_permission

    @property
    def create_time(self):
        r"""Gets the create_time of this TemplateV2.

        创建时间

        :return: The create_time of this TemplateV2.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this TemplateV2.

        创建时间

        :param create_time: The create_time of this TemplateV2.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def creator_name(self):
        r"""Gets the creator_name of this TemplateV2.

        创建人名称

        :return: The creator_name of this TemplateV2.
        :rtype: str
        """
        return self._creator_name

    @creator_name.setter
    def creator_name(self, creator_name):
        r"""Sets the creator_name of this TemplateV2.

        创建人名称

        :param creator_name: The creator_name of this TemplateV2.
        :type creator_name: str
        """
        self._creator_name = creator_name

    @property
    def creator_num(self):
        r"""Gets the creator_num of this TemplateV2.

        创建人工号

        :return: The creator_num of this TemplateV2.
        :rtype: str
        """
        return self._creator_num

    @creator_num.setter
    def creator_num(self, creator_num):
        r"""Sets the creator_num of this TemplateV2.

        创建人工号

        :param creator_num: The creator_num of this TemplateV2.
        :type creator_num: str
        """
        self._creator_num = creator_num

    @property
    def description(self):
        r"""Gets the description of this TemplateV2.

        描述

        :return: The description of this TemplateV2.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this TemplateV2.

        描述

        :param description: The description of this TemplateV2.
        :type description: str
        """
        self._description = description

    @property
    def id(self):
        r"""Gets the id of this TemplateV2.

        id 主键

        :return: The id of this TemplateV2.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this TemplateV2.

        id 主键

        :param id: The id of this TemplateV2.
        :type id: str
        """
        self._id = id

    @property
    def is_default(self):
        r"""Gets the is_default of this TemplateV2.

        是否默认

        :return: The is_default of this TemplateV2.
        :rtype: str
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        r"""Sets the is_default of this TemplateV2.

        是否默认

        :param is_default: The is_default of this TemplateV2.
        :type is_default: str
        """
        self._is_default = is_default

    @property
    def mindmap(self):
        r"""Gets the mindmap of this TemplateV2.

        脑图json

        :return: The mindmap of this TemplateV2.
        :rtype: str
        """
        return self._mindmap

    @mindmap.setter
    def mindmap(self, mindmap):
        r"""Sets the mindmap of this TemplateV2.

        脑图json

        :param mindmap: The mindmap of this TemplateV2.
        :type mindmap: str
        """
        self._mindmap = mindmap

    @property
    def name(self):
        r"""Gets the name of this TemplateV2.

        名称

        :return: The name of this TemplateV2.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this TemplateV2.

        名称

        :param name: The name of this TemplateV2.
        :type name: str
        """
        self._name = name

    @property
    def update_time(self):
        r"""Gets the update_time of this TemplateV2.

        更新时间

        :return: The update_time of this TemplateV2.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this TemplateV2.

        更新时间

        :param update_time: The update_time of this TemplateV2.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def edit_permission(self):
        r"""Gets the edit_permission of this TemplateV2.

        编辑权限

        :return: The edit_permission of this TemplateV2.
        :rtype: bool
        """
        return self._edit_permission

    @edit_permission.setter
    def edit_permission(self, edit_permission):
        r"""Sets the edit_permission of this TemplateV2.

        编辑权限

        :param edit_permission: The edit_permission of this TemplateV2.
        :type edit_permission: bool
        """
        self._edit_permission = edit_permission

    @property
    def delete_permission(self):
        r"""Gets the delete_permission of this TemplateV2.

        删除权限

        :return: The delete_permission of this TemplateV2.
        :rtype: bool
        """
        return self._delete_permission

    @delete_permission.setter
    def delete_permission(self, delete_permission):
        r"""Sets the delete_permission of this TemplateV2.

        删除权限

        :param delete_permission: The delete_permission of this TemplateV2.
        :type delete_permission: bool
        """
        self._delete_permission = delete_permission

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
        if not isinstance(other, TemplateV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
