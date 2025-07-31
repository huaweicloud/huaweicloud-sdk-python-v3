# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceNameItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_name': 'str',
        'operator': 'str',
        'resource_name_is_ignore_case': 'bool'
    }

    attribute_map = {
        'resource_name': 'resource_name',
        'operator': 'operator',
        'resource_name_is_ignore_case': 'resource_name_is_ignore_case'
    }

    def __init__(self, resource_name=None, operator=None, resource_name_is_ignore_case=None):
        r"""ResourceNameItem

        The model defined in huaweicloud sdk

        :param resource_name: 资源名称条件值
        :type resource_name: str
        :param operator: 实例操作符，含义是真实资源的名称与资源名称条件值的运算关系。   include表示包含   prefix表示前缀   suffix表示后缀   notInclude表示不包含   equal表示相等   all表示全部 
        :type operator: str
        :param resource_name_is_ignore_case: 资源名称忽略大小写
        :type resource_name_is_ignore_case: bool
        """
        
        

        self._resource_name = None
        self._operator = None
        self._resource_name_is_ignore_case = None
        self.discriminator = None

        if resource_name is not None:
            self.resource_name = resource_name
        self.operator = operator
        if resource_name_is_ignore_case is not None:
            self.resource_name_is_ignore_case = resource_name_is_ignore_case

    @property
    def resource_name(self):
        r"""Gets the resource_name of this ResourceNameItem.

        资源名称条件值

        :return: The resource_name of this ResourceNameItem.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        r"""Sets the resource_name of this ResourceNameItem.

        资源名称条件值

        :param resource_name: The resource_name of this ResourceNameItem.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def operator(self):
        r"""Gets the operator of this ResourceNameItem.

        实例操作符，含义是真实资源的名称与资源名称条件值的运算关系。   include表示包含   prefix表示前缀   suffix表示后缀   notInclude表示不包含   equal表示相等   all表示全部 

        :return: The operator of this ResourceNameItem.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        r"""Sets the operator of this ResourceNameItem.

        实例操作符，含义是真实资源的名称与资源名称条件值的运算关系。   include表示包含   prefix表示前缀   suffix表示后缀   notInclude表示不包含   equal表示相等   all表示全部 

        :param operator: The operator of this ResourceNameItem.
        :type operator: str
        """
        self._operator = operator

    @property
    def resource_name_is_ignore_case(self):
        r"""Gets the resource_name_is_ignore_case of this ResourceNameItem.

        资源名称忽略大小写

        :return: The resource_name_is_ignore_case of this ResourceNameItem.
        :rtype: bool
        """
        return self._resource_name_is_ignore_case

    @resource_name_is_ignore_case.setter
    def resource_name_is_ignore_case(self, resource_name_is_ignore_case):
        r"""Sets the resource_name_is_ignore_case of this ResourceNameItem.

        资源名称忽略大小写

        :param resource_name_is_ignore_case: The resource_name_is_ignore_case of this ResourceNameItem.
        :type resource_name_is_ignore_case: bool
        """
        self._resource_name_is_ignore_case = resource_name_is_ignore_case

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
        if not isinstance(other, ResourceNameItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
