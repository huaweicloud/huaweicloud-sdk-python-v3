# coding: utf-8

import pprint
import re

import six





class DeptBasicDTO:


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
        'corp_id': 'str',
        'dept_name': 'str',
        'dept_name_path': 'str',
        'parent_dept_code': 'str'
    }

    attribute_map = {
        'dept_code': 'deptCode',
        'corp_id': 'corpId',
        'dept_name': 'deptName',
        'dept_name_path': 'deptNamePath',
        'parent_dept_code': 'parentDeptCode'
    }

    def __init__(self, dept_code=None, corp_id=None, dept_name=None, dept_name_path=None, parent_dept_code=None):
        """DeptBasicDTO - a model defined in huaweicloud sdk"""
        
        

        self._dept_code = None
        self._corp_id = None
        self._dept_name = None
        self._dept_name_path = None
        self._parent_dept_code = None
        self.discriminator = None

        if dept_code is not None:
            self.dept_code = dept_code
        if corp_id is not None:
            self.corp_id = corp_id
        if dept_name is not None:
            self.dept_name = dept_name
        if dept_name_path is not None:
            self.dept_name_path = dept_name_path
        if parent_dept_code is not None:
            self.parent_dept_code = parent_dept_code

    @property
    def dept_code(self):
        """Gets the dept_code of this DeptBasicDTO.

        部门编码

        :return: The dept_code of this DeptBasicDTO.
        :rtype: str
        """
        return self._dept_code

    @dept_code.setter
    def dept_code(self, dept_code):
        """Sets the dept_code of this DeptBasicDTO.

        部门编码

        :param dept_code: The dept_code of this DeptBasicDTO.
        :type: str
        """
        self._dept_code = dept_code

    @property
    def corp_id(self):
        """Gets the corp_id of this DeptBasicDTO.

        企业id

        :return: The corp_id of this DeptBasicDTO.
        :rtype: str
        """
        return self._corp_id

    @corp_id.setter
    def corp_id(self, corp_id):
        """Sets the corp_id of this DeptBasicDTO.

        企业id

        :param corp_id: The corp_id of this DeptBasicDTO.
        :type: str
        """
        self._corp_id = corp_id

    @property
    def dept_name(self):
        """Gets the dept_name of this DeptBasicDTO.

        部门名称

        :return: The dept_name of this DeptBasicDTO.
        :rtype: str
        """
        return self._dept_name

    @dept_name.setter
    def dept_name(self, dept_name):
        """Sets the dept_name of this DeptBasicDTO.

        部门名称

        :param dept_name: The dept_name of this DeptBasicDTO.
        :type: str
        """
        self._dept_name = dept_name

    @property
    def dept_name_path(self):
        """Gets the dept_name_path of this DeptBasicDTO.

        部门名称路径

        :return: The dept_name_path of this DeptBasicDTO.
        :rtype: str
        """
        return self._dept_name_path

    @dept_name_path.setter
    def dept_name_path(self, dept_name_path):
        """Sets the dept_name_path of this DeptBasicDTO.

        部门名称路径

        :param dept_name_path: The dept_name_path of this DeptBasicDTO.
        :type: str
        """
        self._dept_name_path = dept_name_path

    @property
    def parent_dept_code(self):
        """Gets the parent_dept_code of this DeptBasicDTO.

        父部门编码

        :return: The parent_dept_code of this DeptBasicDTO.
        :rtype: str
        """
        return self._parent_dept_code

    @parent_dept_code.setter
    def parent_dept_code(self, parent_dept_code):
        """Sets the parent_dept_code of this DeptBasicDTO.

        父部门编码

        :param parent_dept_code: The parent_dept_code of this DeptBasicDTO.
        :type: str
        """
        self._parent_dept_code = parent_dept_code

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
        if not isinstance(other, DeptBasicDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
