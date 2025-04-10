# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDeptAndChildDeptResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'corp_id': 'str',
        'dept_code': 'str',
        'dept_level': 'int',
        'dept_name': 'str',
        'dept_name_path': 'str',
        'is_leaf_node': 'bool',
        'parent_dept_code': 'str',
        'dept_code_path': 'str',
        'note': 'str',
        'in_permission': 'str',
        'out_permission': 'str',
        'designated_out_dept_codes': 'list[IdMarkDTO]',
        'child_depts': 'list[QueryDeptResultDTO]',
        'sort_level': 'int'
    }

    attribute_map = {
        'corp_id': 'corpId',
        'dept_code': 'deptCode',
        'dept_level': 'deptLevel',
        'dept_name': 'deptName',
        'dept_name_path': 'deptNamePath',
        'is_leaf_node': 'isLeafNode',
        'parent_dept_code': 'parentDeptCode',
        'dept_code_path': 'deptCodePath',
        'note': 'note',
        'in_permission': 'inPermission',
        'out_permission': 'outPermission',
        'designated_out_dept_codes': 'designatedOutDeptCodes',
        'child_depts': 'childDepts',
        'sort_level': 'sortLevel'
    }

    def __init__(self, corp_id=None, dept_code=None, dept_level=None, dept_name=None, dept_name_path=None, is_leaf_node=None, parent_dept_code=None, dept_code_path=None, note=None, in_permission=None, out_permission=None, designated_out_dept_codes=None, child_depts=None, sort_level=None):
        r"""ShowDeptAndChildDeptResponse

        The model defined in huaweicloud sdk

        :param corp_id: 企业ID。
        :type corp_id: str
        :param dept_code: 部门编码。
        :type dept_code: str
        :param dept_level: 部门层级。
        :type dept_level: int
        :param dept_name: 部门名称。
        :type dept_name: str
        :param dept_name_path: 部门名路径。
        :type dept_name_path: str
        :param is_leaf_node: 是否叶子节点。
        :type is_leaf_node: bool
        :param parent_dept_code: 父部门编码。
        :type parent_dept_code: str
        :param dept_code_path: 部门编码路径。
        :type dept_code_path: str
        :param note: 备注。
        :type note: str
        :param in_permission: 其他用户对该部门下用户的访问权限。
        :type in_permission: str
        :param out_permission: 该部门下用户访问权限控制。
        :type out_permission: str
        :param designated_out_dept_codes: 允许访问的部门列表。
        :type designated_out_dept_codes: list[:class:`huaweicloudsdkmeeting.v1.IdMarkDTO`]
        :param child_depts: 子部门列表。
        :type child_depts: list[:class:`huaweicloudsdkmeeting.v1.QueryDeptResultDTO`]
        :param sort_level: 部门排序号。
        :type sort_level: int
        """
        
        super(ShowDeptAndChildDeptResponse, self).__init__()

        self._corp_id = None
        self._dept_code = None
        self._dept_level = None
        self._dept_name = None
        self._dept_name_path = None
        self._is_leaf_node = None
        self._parent_dept_code = None
        self._dept_code_path = None
        self._note = None
        self._in_permission = None
        self._out_permission = None
        self._designated_out_dept_codes = None
        self._child_depts = None
        self._sort_level = None
        self.discriminator = None

        if corp_id is not None:
            self.corp_id = corp_id
        if dept_code is not None:
            self.dept_code = dept_code
        if dept_level is not None:
            self.dept_level = dept_level
        if dept_name is not None:
            self.dept_name = dept_name
        if dept_name_path is not None:
            self.dept_name_path = dept_name_path
        if is_leaf_node is not None:
            self.is_leaf_node = is_leaf_node
        if parent_dept_code is not None:
            self.parent_dept_code = parent_dept_code
        if dept_code_path is not None:
            self.dept_code_path = dept_code_path
        if note is not None:
            self.note = note
        if in_permission is not None:
            self.in_permission = in_permission
        if out_permission is not None:
            self.out_permission = out_permission
        if designated_out_dept_codes is not None:
            self.designated_out_dept_codes = designated_out_dept_codes
        if child_depts is not None:
            self.child_depts = child_depts
        if sort_level is not None:
            self.sort_level = sort_level

    @property
    def corp_id(self):
        r"""Gets the corp_id of this ShowDeptAndChildDeptResponse.

        企业ID。

        :return: The corp_id of this ShowDeptAndChildDeptResponse.
        :rtype: str
        """
        return self._corp_id

    @corp_id.setter
    def corp_id(self, corp_id):
        r"""Sets the corp_id of this ShowDeptAndChildDeptResponse.

        企业ID。

        :param corp_id: The corp_id of this ShowDeptAndChildDeptResponse.
        :type corp_id: str
        """
        self._corp_id = corp_id

    @property
    def dept_code(self):
        r"""Gets the dept_code of this ShowDeptAndChildDeptResponse.

        部门编码。

        :return: The dept_code of this ShowDeptAndChildDeptResponse.
        :rtype: str
        """
        return self._dept_code

    @dept_code.setter
    def dept_code(self, dept_code):
        r"""Sets the dept_code of this ShowDeptAndChildDeptResponse.

        部门编码。

        :param dept_code: The dept_code of this ShowDeptAndChildDeptResponse.
        :type dept_code: str
        """
        self._dept_code = dept_code

    @property
    def dept_level(self):
        r"""Gets the dept_level of this ShowDeptAndChildDeptResponse.

        部门层级。

        :return: The dept_level of this ShowDeptAndChildDeptResponse.
        :rtype: int
        """
        return self._dept_level

    @dept_level.setter
    def dept_level(self, dept_level):
        r"""Sets the dept_level of this ShowDeptAndChildDeptResponse.

        部门层级。

        :param dept_level: The dept_level of this ShowDeptAndChildDeptResponse.
        :type dept_level: int
        """
        self._dept_level = dept_level

    @property
    def dept_name(self):
        r"""Gets the dept_name of this ShowDeptAndChildDeptResponse.

        部门名称。

        :return: The dept_name of this ShowDeptAndChildDeptResponse.
        :rtype: str
        """
        return self._dept_name

    @dept_name.setter
    def dept_name(self, dept_name):
        r"""Sets the dept_name of this ShowDeptAndChildDeptResponse.

        部门名称。

        :param dept_name: The dept_name of this ShowDeptAndChildDeptResponse.
        :type dept_name: str
        """
        self._dept_name = dept_name

    @property
    def dept_name_path(self):
        r"""Gets the dept_name_path of this ShowDeptAndChildDeptResponse.

        部门名路径。

        :return: The dept_name_path of this ShowDeptAndChildDeptResponse.
        :rtype: str
        """
        return self._dept_name_path

    @dept_name_path.setter
    def dept_name_path(self, dept_name_path):
        r"""Sets the dept_name_path of this ShowDeptAndChildDeptResponse.

        部门名路径。

        :param dept_name_path: The dept_name_path of this ShowDeptAndChildDeptResponse.
        :type dept_name_path: str
        """
        self._dept_name_path = dept_name_path

    @property
    def is_leaf_node(self):
        r"""Gets the is_leaf_node of this ShowDeptAndChildDeptResponse.

        是否叶子节点。

        :return: The is_leaf_node of this ShowDeptAndChildDeptResponse.
        :rtype: bool
        """
        return self._is_leaf_node

    @is_leaf_node.setter
    def is_leaf_node(self, is_leaf_node):
        r"""Sets the is_leaf_node of this ShowDeptAndChildDeptResponse.

        是否叶子节点。

        :param is_leaf_node: The is_leaf_node of this ShowDeptAndChildDeptResponse.
        :type is_leaf_node: bool
        """
        self._is_leaf_node = is_leaf_node

    @property
    def parent_dept_code(self):
        r"""Gets the parent_dept_code of this ShowDeptAndChildDeptResponse.

        父部门编码。

        :return: The parent_dept_code of this ShowDeptAndChildDeptResponse.
        :rtype: str
        """
        return self._parent_dept_code

    @parent_dept_code.setter
    def parent_dept_code(self, parent_dept_code):
        r"""Sets the parent_dept_code of this ShowDeptAndChildDeptResponse.

        父部门编码。

        :param parent_dept_code: The parent_dept_code of this ShowDeptAndChildDeptResponse.
        :type parent_dept_code: str
        """
        self._parent_dept_code = parent_dept_code

    @property
    def dept_code_path(self):
        r"""Gets the dept_code_path of this ShowDeptAndChildDeptResponse.

        部门编码路径。

        :return: The dept_code_path of this ShowDeptAndChildDeptResponse.
        :rtype: str
        """
        return self._dept_code_path

    @dept_code_path.setter
    def dept_code_path(self, dept_code_path):
        r"""Sets the dept_code_path of this ShowDeptAndChildDeptResponse.

        部门编码路径。

        :param dept_code_path: The dept_code_path of this ShowDeptAndChildDeptResponse.
        :type dept_code_path: str
        """
        self._dept_code_path = dept_code_path

    @property
    def note(self):
        r"""Gets the note of this ShowDeptAndChildDeptResponse.

        备注。

        :return: The note of this ShowDeptAndChildDeptResponse.
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        r"""Sets the note of this ShowDeptAndChildDeptResponse.

        备注。

        :param note: The note of this ShowDeptAndChildDeptResponse.
        :type note: str
        """
        self._note = note

    @property
    def in_permission(self):
        r"""Gets the in_permission of this ShowDeptAndChildDeptResponse.

        其他用户对该部门下用户的访问权限。

        :return: The in_permission of this ShowDeptAndChildDeptResponse.
        :rtype: str
        """
        return self._in_permission

    @in_permission.setter
    def in_permission(self, in_permission):
        r"""Sets the in_permission of this ShowDeptAndChildDeptResponse.

        其他用户对该部门下用户的访问权限。

        :param in_permission: The in_permission of this ShowDeptAndChildDeptResponse.
        :type in_permission: str
        """
        self._in_permission = in_permission

    @property
    def out_permission(self):
        r"""Gets the out_permission of this ShowDeptAndChildDeptResponse.

        该部门下用户访问权限控制。

        :return: The out_permission of this ShowDeptAndChildDeptResponse.
        :rtype: str
        """
        return self._out_permission

    @out_permission.setter
    def out_permission(self, out_permission):
        r"""Sets the out_permission of this ShowDeptAndChildDeptResponse.

        该部门下用户访问权限控制。

        :param out_permission: The out_permission of this ShowDeptAndChildDeptResponse.
        :type out_permission: str
        """
        self._out_permission = out_permission

    @property
    def designated_out_dept_codes(self):
        r"""Gets the designated_out_dept_codes of this ShowDeptAndChildDeptResponse.

        允许访问的部门列表。

        :return: The designated_out_dept_codes of this ShowDeptAndChildDeptResponse.
        :rtype: list[:class:`huaweicloudsdkmeeting.v1.IdMarkDTO`]
        """
        return self._designated_out_dept_codes

    @designated_out_dept_codes.setter
    def designated_out_dept_codes(self, designated_out_dept_codes):
        r"""Sets the designated_out_dept_codes of this ShowDeptAndChildDeptResponse.

        允许访问的部门列表。

        :param designated_out_dept_codes: The designated_out_dept_codes of this ShowDeptAndChildDeptResponse.
        :type designated_out_dept_codes: list[:class:`huaweicloudsdkmeeting.v1.IdMarkDTO`]
        """
        self._designated_out_dept_codes = designated_out_dept_codes

    @property
    def child_depts(self):
        r"""Gets the child_depts of this ShowDeptAndChildDeptResponse.

        子部门列表。

        :return: The child_depts of this ShowDeptAndChildDeptResponse.
        :rtype: list[:class:`huaweicloudsdkmeeting.v1.QueryDeptResultDTO`]
        """
        return self._child_depts

    @child_depts.setter
    def child_depts(self, child_depts):
        r"""Sets the child_depts of this ShowDeptAndChildDeptResponse.

        子部门列表。

        :param child_depts: The child_depts of this ShowDeptAndChildDeptResponse.
        :type child_depts: list[:class:`huaweicloudsdkmeeting.v1.QueryDeptResultDTO`]
        """
        self._child_depts = child_depts

    @property
    def sort_level(self):
        r"""Gets the sort_level of this ShowDeptAndChildDeptResponse.

        部门排序号。

        :return: The sort_level of this ShowDeptAndChildDeptResponse.
        :rtype: int
        """
        return self._sort_level

    @sort_level.setter
    def sort_level(self, sort_level):
        r"""Sets the sort_level of this ShowDeptAndChildDeptResponse.

        部门排序号。

        :param sort_level: The sort_level of this ShowDeptAndChildDeptResponse.
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
        if not isinstance(other, ShowDeptAndChildDeptResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
