# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChildDeptDTO:

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
        'is_leaf_nodes': 'bool'
    }

    attribute_map = {
        'dept_code': 'deptCode',
        'dept_name': 'deptName',
        'is_leaf_nodes': 'isLeafNodes'
    }

    def __init__(self, dept_code=None, dept_name=None, is_leaf_nodes=None):
        """ChildDeptDTO

        The model defined in huaweicloud sdk

        :param dept_code: 部门编码。
        :type dept_code: str
        :param dept_name: 部门名称。
        :type dept_name: str
        :param is_leaf_nodes: 是否为叶子节点（没有子部门的称为叶子节点）。
        :type is_leaf_nodes: bool
        """
        
        

        self._dept_code = None
        self._dept_name = None
        self._is_leaf_nodes = None
        self.discriminator = None

        if dept_code is not None:
            self.dept_code = dept_code
        if dept_name is not None:
            self.dept_name = dept_name
        if is_leaf_nodes is not None:
            self.is_leaf_nodes = is_leaf_nodes

    @property
    def dept_code(self):
        """Gets the dept_code of this ChildDeptDTO.

        部门编码。

        :return: The dept_code of this ChildDeptDTO.
        :rtype: str
        """
        return self._dept_code

    @dept_code.setter
    def dept_code(self, dept_code):
        """Sets the dept_code of this ChildDeptDTO.

        部门编码。

        :param dept_code: The dept_code of this ChildDeptDTO.
        :type dept_code: str
        """
        self._dept_code = dept_code

    @property
    def dept_name(self):
        """Gets the dept_name of this ChildDeptDTO.

        部门名称。

        :return: The dept_name of this ChildDeptDTO.
        :rtype: str
        """
        return self._dept_name

    @dept_name.setter
    def dept_name(self, dept_name):
        """Sets the dept_name of this ChildDeptDTO.

        部门名称。

        :param dept_name: The dept_name of this ChildDeptDTO.
        :type dept_name: str
        """
        self._dept_name = dept_name

    @property
    def is_leaf_nodes(self):
        """Gets the is_leaf_nodes of this ChildDeptDTO.

        是否为叶子节点（没有子部门的称为叶子节点）。

        :return: The is_leaf_nodes of this ChildDeptDTO.
        :rtype: bool
        """
        return self._is_leaf_nodes

    @is_leaf_nodes.setter
    def is_leaf_nodes(self, is_leaf_nodes):
        """Sets the is_leaf_nodes of this ChildDeptDTO.

        是否为叶子节点（没有子部门的称为叶子节点）。

        :param is_leaf_nodes: The is_leaf_nodes of this ChildDeptDTO.
        :type is_leaf_nodes: bool
        """
        self._is_leaf_nodes = is_leaf_nodes

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
        if not isinstance(other, ChildDeptDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
