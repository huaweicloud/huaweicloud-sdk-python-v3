# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


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
        'designated_out_dept_codes': 'list[str]',
        'sort_level': 'int'
    }

    attribute_map = {
        'dept_name': 'deptName',
        'parent_dept_code': 'parentDeptCode',
        'note': 'note',
        'in_permission': 'inPermission',
        'out_permission': 'outPermission',
        'designated_out_dept_codes': 'designatedOutDeptCodes',
        'sort_level': 'sortLevel'
    }

    def __init__(self, dept_name=None, parent_dept_code=None, note=None, in_permission=None, out_permission=None, designated_out_dept_codes=None, sort_level=None):
        """ModDeptDTO

        The model defined in huaweicloud sdk

        :param dept_name: 部门名称。
        :type dept_name: str
        :param parent_dept_code: 父部门编码。
        :type parent_dept_code: str
        :param note: 备注。
        :type note: str
        :param in_permission: 其他用户对该部门下用户的访问权限： - UNLIMITED：默认，不做限制 - OPEN：公开，其他部门都可访问（无论对方权限如何配置） - CLOSE：隐藏，其他部门不可访问（暂未实现） - DESIGNATED_DEPARTMENT：指定部门能访问（暂未实现）
        :type in_permission: str
        :param out_permission: 该部门下用户访问权限控制。 - UNLIMITED：不限制 - ONLY_SELF：仅能查询自己 - SELF_AND_CHILD_DEPARTMENT：该部门下用户能查询本部门及子部门通讯 - DESIGNATED_DEPARTMENT：该部门下用户能查询指定部门通讯录
        :type out_permission: str
        :param designated_out_dept_codes: 允许访问的部门列表,仅outPermission为DESIGNATED_DEPARTMENT时有效，最多支持配置150个部门。
        :type designated_out_dept_codes: list[str]
        :param sort_level: 部门排序号，序号越小,部门排序越靠前。
        :type sort_level: int
        """
        
        

        self._dept_name = None
        self._parent_dept_code = None
        self._note = None
        self._in_permission = None
        self._out_permission = None
        self._designated_out_dept_codes = None
        self._sort_level = None
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
        if sort_level is not None:
            self.sort_level = sort_level

    @property
    def dept_name(self):
        """Gets the dept_name of this ModDeptDTO.

        部门名称。

        :return: The dept_name of this ModDeptDTO.
        :rtype: str
        """
        return self._dept_name

    @dept_name.setter
    def dept_name(self, dept_name):
        """Sets the dept_name of this ModDeptDTO.

        部门名称。

        :param dept_name: The dept_name of this ModDeptDTO.
        :type dept_name: str
        """
        self._dept_name = dept_name

    @property
    def parent_dept_code(self):
        """Gets the parent_dept_code of this ModDeptDTO.

        父部门编码。

        :return: The parent_dept_code of this ModDeptDTO.
        :rtype: str
        """
        return self._parent_dept_code

    @parent_dept_code.setter
    def parent_dept_code(self, parent_dept_code):
        """Sets the parent_dept_code of this ModDeptDTO.

        父部门编码。

        :param parent_dept_code: The parent_dept_code of this ModDeptDTO.
        :type parent_dept_code: str
        """
        self._parent_dept_code = parent_dept_code

    @property
    def note(self):
        """Gets the note of this ModDeptDTO.

        备注。

        :return: The note of this ModDeptDTO.
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this ModDeptDTO.

        备注。

        :param note: The note of this ModDeptDTO.
        :type note: str
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
        :type in_permission: str
        """
        self._in_permission = in_permission

    @property
    def out_permission(self):
        """Gets the out_permission of this ModDeptDTO.

        该部门下用户访问权限控制。 - UNLIMITED：不限制 - ONLY_SELF：仅能查询自己 - SELF_AND_CHILD_DEPARTMENT：该部门下用户能查询本部门及子部门通讯 - DESIGNATED_DEPARTMENT：该部门下用户能查询指定部门通讯录

        :return: The out_permission of this ModDeptDTO.
        :rtype: str
        """
        return self._out_permission

    @out_permission.setter
    def out_permission(self, out_permission):
        """Sets the out_permission of this ModDeptDTO.

        该部门下用户访问权限控制。 - UNLIMITED：不限制 - ONLY_SELF：仅能查询自己 - SELF_AND_CHILD_DEPARTMENT：该部门下用户能查询本部门及子部门通讯 - DESIGNATED_DEPARTMENT：该部门下用户能查询指定部门通讯录

        :param out_permission: The out_permission of this ModDeptDTO.
        :type out_permission: str
        """
        self._out_permission = out_permission

    @property
    def designated_out_dept_codes(self):
        """Gets the designated_out_dept_codes of this ModDeptDTO.

        允许访问的部门列表,仅outPermission为DESIGNATED_DEPARTMENT时有效，最多支持配置150个部门。

        :return: The designated_out_dept_codes of this ModDeptDTO.
        :rtype: list[str]
        """
        return self._designated_out_dept_codes

    @designated_out_dept_codes.setter
    def designated_out_dept_codes(self, designated_out_dept_codes):
        """Sets the designated_out_dept_codes of this ModDeptDTO.

        允许访问的部门列表,仅outPermission为DESIGNATED_DEPARTMENT时有效，最多支持配置150个部门。

        :param designated_out_dept_codes: The designated_out_dept_codes of this ModDeptDTO.
        :type designated_out_dept_codes: list[str]
        """
        self._designated_out_dept_codes = designated_out_dept_codes

    @property
    def sort_level(self):
        """Gets the sort_level of this ModDeptDTO.

        部门排序号，序号越小,部门排序越靠前。

        :return: The sort_level of this ModDeptDTO.
        :rtype: int
        """
        return self._sort_level

    @sort_level.setter
    def sort_level(self, sort_level):
        """Sets the sort_level of this ModDeptDTO.

        部门排序号，序号越小,部门排序越靠前。

        :param sort_level: The sort_level of this ModDeptDTO.
        :type sort_level: int
        """
        self._sort_level = sort_level

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
        if not isinstance(other, ModDeptDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
