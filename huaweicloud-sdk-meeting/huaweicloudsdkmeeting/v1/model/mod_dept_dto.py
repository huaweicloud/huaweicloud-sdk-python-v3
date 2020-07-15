# coding: utf-8

import pprint
import re

import six





class ModDeptDTO:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'dept_name': 'str',
        'parent_dept_code': 'str',
        'note': 'str',
        'in_permission': 'str',
        'out_permission': 'str',
        'designated_out_dept_codes': 'list[str]'
    }

    attribute_map = {
        'dept_name': 'deptName',
        'parent_dept_code': 'parentDeptCode',
        'note': 'note',
        'in_permission': 'inPermission',
        'out_permission': 'outPermission',
        'designated_out_dept_codes': 'designatedOutDeptCodes'
    }

    def __init__(self, dept_name=None, parent_dept_code='1', note=None, in_permission=None, out_permission=None, designated_out_dept_codes=None):
        """ModDeptDTO - a model defined in huaweicloud sdk"""
        
        

        self._dept_name = None
        self._parent_dept_code = None
        self._note = None
        self._in_permission = None
        self._out_permission = None
        self._designated_out_dept_codes = None
        self.discriminator = None

        if dept_name is not None:
            self.dept_name = dept_name
        if parent_dept_code is not None:
            self.parent_dept_code = parent_dept_code
        if note is not None:
            self.note = note
        if in_permission is not None:
            self.in_permission = in_permission
        if out_permission is not None:
            self.out_permission = out_permission
        if designated_out_dept_codes is not None:
            self.designated_out_dept_codes = designated_out_dept_codes

    @property
    def dept_name(self):
        """Gets the dept_name of this ModDeptDTO.

        部门名称 maxLength：128 minLength：1

        :return: The dept_name of this ModDeptDTO.
        :rtype: str
        """
        return self._dept_name

    @dept_name.setter
    def dept_name(self, dept_name):
        """Sets the dept_name of this ModDeptDTO.

        部门名称 maxLength：128 minLength：1

        :param dept_name: The dept_name of this ModDeptDTO.
        :type: str
        """
        self._dept_name = dept_name

    @property
    def parent_dept_code(self):
        """Gets the parent_dept_code of this ModDeptDTO.

        父部门编码 maxLength：32

        :return: The parent_dept_code of this ModDeptDTO.
        :rtype: str
        """
        return self._parent_dept_code

    @parent_dept_code.setter
    def parent_dept_code(self, parent_dept_code):
        """Sets the parent_dept_code of this ModDeptDTO.

        父部门编码 maxLength：32

        :param parent_dept_code: The parent_dept_code of this ModDeptDTO.
        :type: str
        """
        self._parent_dept_code = parent_dept_code

    @property
    def note(self):
        """Gets the note of this ModDeptDTO.

        备注 maxLength：96 minLength：0

        :return: The note of this ModDeptDTO.
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this ModDeptDTO.

        备注 maxLength：96 minLength：0

        :param note: The note of this ModDeptDTO.
        :type: str
        """
        self._note = note

    @property
    def in_permission(self):
        """Gets the in_permission of this ModDeptDTO.

        其他用户对该部门下用户的访问权限： - UNLIMITED：默认，不做限制 - OPEN：公开，其他部门都可访问（无论对方权限如何配置） - CLOSE：隐藏，其他部门不可访问（暂未实现） - DESIGNATED_DEPARTMENT：指定部门能访问（暂未实现）

        :return: The in_permission of this ModDeptDTO.
        :rtype: str
        """
        return self._in_permission

    @in_permission.setter
    def in_permission(self, in_permission):
        """Sets the in_permission of this ModDeptDTO.

        其他用户对该部门下用户的访问权限： - UNLIMITED：默认，不做限制 - OPEN：公开，其他部门都可访问（无论对方权限如何配置） - CLOSE：隐藏，其他部门不可访问（暂未实现） - DESIGNATED_DEPARTMENT：指定部门能访问（暂未实现）

        :param in_permission: The in_permission of this ModDeptDTO.
        :type: str
        """
        self._in_permission = in_permission

    @property
    def out_permission(self):
        """Gets the out_permission of this ModDeptDTO.

        该部门下用户访问权限控制 - UNLIMITED：不限制 - ONLY_SELF：仅能查询自己 - SELF_AND_CHILD_DEPARTMENT：该部门下用户能查询本部门及子部门通讯 - DESIGNATED_DEPARTMENT：该部门下用户能查询指定部门通讯录

        :return: The out_permission of this ModDeptDTO.
        :rtype: str
        """
        return self._out_permission

    @out_permission.setter
    def out_permission(self, out_permission):
        """Sets the out_permission of this ModDeptDTO.

        该部门下用户访问权限控制 - UNLIMITED：不限制 - ONLY_SELF：仅能查询自己 - SELF_AND_CHILD_DEPARTMENT：该部门下用户能查询本部门及子部门通讯 - DESIGNATED_DEPARTMENT：该部门下用户能查询指定部门通讯录

        :param out_permission: The out_permission of this ModDeptDTO.
        :type: str
        """
        self._out_permission = out_permission

    @property
    def designated_out_dept_codes(self):
        """Gets the designated_out_dept_codes of this ModDeptDTO.

        允许访问的部门列表,仅outPermission为DESIGNATED_DEPARTMENT时有效，最多支持配置150

        :return: The designated_out_dept_codes of this ModDeptDTO.
        :rtype: list[str]
        """
        return self._designated_out_dept_codes

    @designated_out_dept_codes.setter
    def designated_out_dept_codes(self, designated_out_dept_codes):
        """Sets the designated_out_dept_codes of this ModDeptDTO.

        允许访问的部门列表,仅outPermission为DESIGNATED_DEPARTMENT时有效，最多支持配置150

        :param designated_out_dept_codes: The designated_out_dept_codes of this ModDeptDTO.
        :type: list[str]
        """
        self._designated_out_dept_codes = designated_out_dept_codes

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ModDeptDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
