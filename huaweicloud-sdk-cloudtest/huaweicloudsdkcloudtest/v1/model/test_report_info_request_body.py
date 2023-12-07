# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TestReportInfoRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'plan_id': 'str',
        'branch_id': 'str',
        'module_id': 'str',
        'fixed_version_id': 'str'
    }

    attribute_map = {
        'plan_id': 'plan_id',
        'branch_id': 'branch_id',
        'module_id': 'module_id',
        'fixed_version_id': 'fixed_version_id'
    }

    def __init__(self, plan_id=None, branch_id=None, module_id=None, fixed_version_id=None):
        """TestReportInfoRequestBody

        The model defined in huaweicloud sdk

        :param plan_id: 测试计划id,(plan_id和branch_id不能同时为空，优先取plan_id)
        :type plan_id: str
        :param branch_id: 分支id,(plan_id和branch_id不能同时为空，优先取plan_id)
        :type branch_id: str
        :param module_id: 模块ID(查询未设置传入-2)
        :type module_id: str
        :param fixed_version_id: 筛选迭代ID(查询未设置传入-2)
        :type fixed_version_id: str
        """
        
        

        self._plan_id = None
        self._branch_id = None
        self._module_id = None
        self._fixed_version_id = None
        self.discriminator = None

        if plan_id is not None:
            self.plan_id = plan_id
        if branch_id is not None:
            self.branch_id = branch_id
        if module_id is not None:
            self.module_id = module_id
        if fixed_version_id is not None:
            self.fixed_version_id = fixed_version_id

    @property
    def plan_id(self):
        """Gets the plan_id of this TestReportInfoRequestBody.

        测试计划id,(plan_id和branch_id不能同时为空，优先取plan_id)

        :return: The plan_id of this TestReportInfoRequestBody.
        :rtype: str
        """
        return self._plan_id

    @plan_id.setter
    def plan_id(self, plan_id):
        """Sets the plan_id of this TestReportInfoRequestBody.

        测试计划id,(plan_id和branch_id不能同时为空，优先取plan_id)

        :param plan_id: The plan_id of this TestReportInfoRequestBody.
        :type plan_id: str
        """
        self._plan_id = plan_id

    @property
    def branch_id(self):
        """Gets the branch_id of this TestReportInfoRequestBody.

        分支id,(plan_id和branch_id不能同时为空，优先取plan_id)

        :return: The branch_id of this TestReportInfoRequestBody.
        :rtype: str
        """
        return self._branch_id

    @branch_id.setter
    def branch_id(self, branch_id):
        """Sets the branch_id of this TestReportInfoRequestBody.

        分支id,(plan_id和branch_id不能同时为空，优先取plan_id)

        :param branch_id: The branch_id of this TestReportInfoRequestBody.
        :type branch_id: str
        """
        self._branch_id = branch_id

    @property
    def module_id(self):
        """Gets the module_id of this TestReportInfoRequestBody.

        模块ID(查询未设置传入-2)

        :return: The module_id of this TestReportInfoRequestBody.
        :rtype: str
        """
        return self._module_id

    @module_id.setter
    def module_id(self, module_id):
        """Sets the module_id of this TestReportInfoRequestBody.

        模块ID(查询未设置传入-2)

        :param module_id: The module_id of this TestReportInfoRequestBody.
        :type module_id: str
        """
        self._module_id = module_id

    @property
    def fixed_version_id(self):
        """Gets the fixed_version_id of this TestReportInfoRequestBody.

        筛选迭代ID(查询未设置传入-2)

        :return: The fixed_version_id of this TestReportInfoRequestBody.
        :rtype: str
        """
        return self._fixed_version_id

    @fixed_version_id.setter
    def fixed_version_id(self, fixed_version_id):
        """Sets the fixed_version_id of this TestReportInfoRequestBody.

        筛选迭代ID(查询未设置传入-2)

        :param fixed_version_id: The fixed_version_id of this TestReportInfoRequestBody.
        :type fixed_version_id: str
        """
        self._fixed_version_id = fixed_version_id

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
        if not isinstance(other, TestReportInfoRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
