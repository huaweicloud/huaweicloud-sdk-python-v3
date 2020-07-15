# coding: utf-8

import pprint
import re

import six





class DeptDTO:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'dept_code': 'str',
        'dept_name': 'str',
        'parent_dept_code': 'str',
        'note': 'str',
        'in_permission': 'str',
        'out_permission': 'str',
        'designated_out_dept_codes': 'list[str]'
    }

    attribute_map = {
        'dept_code': 'deptCode',
        'dept_name': 'deptName',
        'parent_dept_code': 'parentDeptCode',
        'note': 'note',
        'in_permission': 'inPermission',
        'out_permission': 'outPermission',
        'designated_out_dept_codes': 'designatedOutDeptCodes'
    }

    def __init__(self, dept_code=None, dept_name=None, parent_dept_code=None, note=None, in_permission=None, out_permission=None, designated_out_dept_codes=None):
        """DeptDTO - a model defined in huaweicloud sdk"""
        
        

        self._dept_code = None
        self._dept_name = None
        self._parent_dept_code = None
        self._note = None
        self._in_permission = None
        self._out_permission = None
        self._designated_out_dept_codes = None
        self.discriminator = None

        if dept_code is not None:
            self.dept_code = dept_code
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
    def dept_code(self):
        """Gets the dept_code of this DeptDTO.

        部门编码，企业内唯一，若携带则以携带为准，不支持修改。 maxLength：32 

        :return: The dept_code of this DeptDTO.
        :rtype: str
        """
        return self._dept_code

    @dept_code.setter
    def dept_code(self, dept_code):
        """Sets the dept_code of this DeptDTO.

        部门编码，企业内唯一，若携带则以携带为准，不支持修改。 maxLength：32 

        :param dept_code: The dept_code of this DeptDTO.
        :type: str
        """
        self._dept_code = dept_code

    @property
    def dept_name(self):
        """Gets the dept_name of this DeptDTO.

        部门名称 maxLength：128 minLength：1 

        :return: The dept_name of this DeptDTO.
        :rtype: str
        """
        return self._dept_name

    @dept_name.setter
    def dept_name(self, dept_name):
        """Sets the dept_name of this DeptDTO.

        部门名称 maxLength：128 minLength：1 

        :param dept_name: The dept_name of this DeptDTO.
        :type: str
        """
        self._dept_name = dept_name

    @property
    def parent_dept_code(self):
        """Gets the parent_dept_code of this DeptDTO.

        父部门编码,默认为根部门。 默认值：1： maxLength：32 

        :return: The parent_dept_code of this DeptDTO.
        :rtype: str
        """
        return self._parent_dept_code

    @parent_dept_code.setter
    def parent_dept_code(self, parent_dept_code):
        """Sets the parent_dept_code of this DeptDTO.

        父部门编码,默认为根部门。 默认值：1： maxLength：32 

        :param parent_dept_code: The parent_dept_code of this DeptDTO.
        :type: str
        """
        self._parent_dept_code = parent_dept_code

    @property
    def note(self):
        """Gets the note of this DeptDTO.

        备注 maxLength：96 minLength：0 

        :return: The note of this DeptDTO.
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this DeptDTO.

        备注 maxLength：96 minLength：0 

        :param note: The note of this DeptDTO.
        :type: str
        """
        self._note = note

    @property
    def in_permission(self):
        """Gets the in_permission of this DeptDTO.

        其他用户对该部门下用户的访问权限： - UNLIMITED：默认，不做限制 - OPEN：公开，其他部门都可访问（无论对方权限如何配置）

        :return: The in_permission of this DeptDTO.
        :rtype: str
        """
        return self._in_permission

    @in_permission.setter
    def in_permission(self, in_permission):
        """Sets the in_permission of this DeptDTO.

        其他用户对该部门下用户的访问权限： - UNLIMITED：默认，不做限制 - OPEN：公开，其他部门都可访问（无论对方权限如何配置）

        :param in_permission: The in_permission of this DeptDTO.
        :type: str
        """
        self._in_permission = in_permission

    @property
    def out_permission(self):
        """Gets the out_permission of this DeptDTO.

        该部门下用户访问权限控制 - UNLIMITED：不限制 - ONLY_SELF：仅能查询自己 - SELF_AND_CHILD_DEPARTMENT：该部门下用户能查询本部门及子部门通讯 - DESIGNATED_DEPARTMENT：该部门下用户能查询指定部门通讯录

        :return: The out_permission of this DeptDTO.
        :rtype: str
        """
        return self._out_permission

    @out_permission.setter
    def out_permission(self, out_permission):
        """Sets the out_permission of this DeptDTO.

        该部门下用户访问权限控制 - UNLIMITED：不限制 - ONLY_SELF：仅能查询自己 - SELF_AND_CHILD_DEPARTMENT：该部门下用户能查询本部门及子部门通讯 - DESIGNATED_DEPARTMENT：该部门下用户能查询指定部门通讯录

        :param out_permission: The out_permission of this DeptDTO.
        :type: str
        """
        self._out_permission = out_permission

    @property
    def designated_out_dept_codes(self):
        """Gets the designated_out_dept_codes of this DeptDTO.

        允许访问的部门列表,仅outPermission为DESIGNATED_DEPARTMENT时有效，最多支持配置150

        :return: The designated_out_dept_codes of this DeptDTO.
        :rtype: list[str]
        """
        return self._designated_out_dept_codes

    @designated_out_dept_codes.setter
    def designated_out_dept_codes(self, designated_out_dept_codes):
        """Sets the designated_out_dept_codes of this DeptDTO.

        允许访问的部门列表,仅outPermission为DESIGNATED_DEPARTMENT时有效，最多支持配置150

        :param designated_out_dept_codes: The designated_out_dept_codes of this DeptDTO.
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
        if not isinstance(other, DeptDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
