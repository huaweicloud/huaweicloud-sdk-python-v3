# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProjectModule:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'module_id': 'int',
        'module_name': 'str',
        'owner': 'ModuleOwner',
        'deepth': 'int',
        'is_parent': 'bool',
        'children': 'list[ProjectChildModule]'
    }

    attribute_map = {
        'module_id': 'module_id',
        'module_name': 'module_name',
        'owner': 'owner',
        'deepth': 'deepth',
        'is_parent': 'is_parent',
        'children': 'children'
    }

    def __init__(self, module_id=None, module_name=None, owner=None, deepth=None, is_parent=None, children=None):
        """ProjectModule

        The model defined in huaweicloud sdk

        :param module_id: 模块id
        :type module_id: int
        :param module_name: 模块名称
        :type module_name: str
        :param owner: 
        :type owner: :class:`huaweicloudsdkprojectman.v4.ModuleOwner`
        :param deepth: 模块层级
        :type deepth: int
        :param is_parent: 是否是父级，true 父模块， false 非父模块
        :type is_parent: bool
        :param children: 子模块信息
        :type children: list[:class:`huaweicloudsdkprojectman.v4.ProjectChildModule`]
        """
        
        

        self._module_id = None
        self._module_name = None
        self._owner = None
        self._deepth = None
        self._is_parent = None
        self._children = None
        self.discriminator = None

        if module_id is not None:
            self.module_id = module_id
        if module_name is not None:
            self.module_name = module_name
        if owner is not None:
            self.owner = owner
        if deepth is not None:
            self.deepth = deepth
        if is_parent is not None:
            self.is_parent = is_parent
        if children is not None:
            self.children = children

    @property
    def module_id(self):
        """Gets the module_id of this ProjectModule.

        模块id

        :return: The module_id of this ProjectModule.
        :rtype: int
        """
        return self._module_id

    @module_id.setter
    def module_id(self, module_id):
        """Sets the module_id of this ProjectModule.

        模块id

        :param module_id: The module_id of this ProjectModule.
        :type module_id: int
        """
        self._module_id = module_id

    @property
    def module_name(self):
        """Gets the module_name of this ProjectModule.

        模块名称

        :return: The module_name of this ProjectModule.
        :rtype: str
        """
        return self._module_name

    @module_name.setter
    def module_name(self, module_name):
        """Sets the module_name of this ProjectModule.

        模块名称

        :param module_name: The module_name of this ProjectModule.
        :type module_name: str
        """
        self._module_name = module_name

    @property
    def owner(self):
        """Gets the owner of this ProjectModule.

        :return: The owner of this ProjectModule.
        :rtype: :class:`huaweicloudsdkprojectman.v4.ModuleOwner`
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this ProjectModule.

        :param owner: The owner of this ProjectModule.
        :type owner: :class:`huaweicloudsdkprojectman.v4.ModuleOwner`
        """
        self._owner = owner

    @property
    def deepth(self):
        """Gets the deepth of this ProjectModule.

        模块层级

        :return: The deepth of this ProjectModule.
        :rtype: int
        """
        return self._deepth

    @deepth.setter
    def deepth(self, deepth):
        """Sets the deepth of this ProjectModule.

        模块层级

        :param deepth: The deepth of this ProjectModule.
        :type deepth: int
        """
        self._deepth = deepth

    @property
    def is_parent(self):
        """Gets the is_parent of this ProjectModule.

        是否是父级，true 父模块， false 非父模块

        :return: The is_parent of this ProjectModule.
        :rtype: bool
        """
        return self._is_parent

    @is_parent.setter
    def is_parent(self, is_parent):
        """Sets the is_parent of this ProjectModule.

        是否是父级，true 父模块， false 非父模块

        :param is_parent: The is_parent of this ProjectModule.
        :type is_parent: bool
        """
        self._is_parent = is_parent

    @property
    def children(self):
        """Gets the children of this ProjectModule.

        子模块信息

        :return: The children of this ProjectModule.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.ProjectChildModule`]
        """
        return self._children

    @children.setter
    def children(self, children):
        """Sets the children of this ProjectModule.

        子模块信息

        :param children: The children of this ProjectModule.
        :type children: list[:class:`huaweicloudsdkprojectman.v4.ProjectChildModule`]
        """
        self._children = children

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
        if not isinstance(other, ProjectModule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
