# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowApiTestcaseHistoriesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'testcase_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'plan_id': 'str',
        'project_id': 'str'
    }

    attribute_map = {
        'testcase_id': 'testcase_id',
        'offset': 'offset',
        'limit': 'limit',
        'plan_id': 'plan_id',
        'project_id': 'project_id'
    }

    def __init__(self, testcase_id=None, offset=None, limit=None, plan_id=None, project_id=None):
        r"""ShowApiTestcaseHistoriesRequest

        The model defined in huaweicloud sdk

        :param testcase_id: 测试用例id
        :type testcase_id: str
        :param offset: 起始偏移量，表示从此偏移量开始查询， offset大于等于1
        :type offset: int
        :param limit: 每页显示的条目数量,最大支持200条
        :type limit: int
        :param plan_id: 测试计划id
        :type plan_id: str
        :param project_id: 项目ID，固定长度32位字符（字母和数字）。
        :type project_id: str
        """
        
        

        self._testcase_id = None
        self._offset = None
        self._limit = None
        self._plan_id = None
        self._project_id = None
        self.discriminator = None

        self.testcase_id = testcase_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if plan_id is not None:
            self.plan_id = plan_id
        self.project_id = project_id

    @property
    def testcase_id(self):
        r"""Gets the testcase_id of this ShowApiTestcaseHistoriesRequest.

        测试用例id

        :return: The testcase_id of this ShowApiTestcaseHistoriesRequest.
        :rtype: str
        """
        return self._testcase_id

    @testcase_id.setter
    def testcase_id(self, testcase_id):
        r"""Sets the testcase_id of this ShowApiTestcaseHistoriesRequest.

        测试用例id

        :param testcase_id: The testcase_id of this ShowApiTestcaseHistoriesRequest.
        :type testcase_id: str
        """
        self._testcase_id = testcase_id

    @property
    def offset(self):
        r"""Gets the offset of this ShowApiTestcaseHistoriesRequest.

        起始偏移量，表示从此偏移量开始查询， offset大于等于1

        :return: The offset of this ShowApiTestcaseHistoriesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ShowApiTestcaseHistoriesRequest.

        起始偏移量，表示从此偏移量开始查询， offset大于等于1

        :param offset: The offset of this ShowApiTestcaseHistoriesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ShowApiTestcaseHistoriesRequest.

        每页显示的条目数量,最大支持200条

        :return: The limit of this ShowApiTestcaseHistoriesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowApiTestcaseHistoriesRequest.

        每页显示的条目数量,最大支持200条

        :param limit: The limit of this ShowApiTestcaseHistoriesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def plan_id(self):
        r"""Gets the plan_id of this ShowApiTestcaseHistoriesRequest.

        测试计划id

        :return: The plan_id of this ShowApiTestcaseHistoriesRequest.
        :rtype: str
        """
        return self._plan_id

    @plan_id.setter
    def plan_id(self, plan_id):
        r"""Sets the plan_id of this ShowApiTestcaseHistoriesRequest.

        测试计划id

        :param plan_id: The plan_id of this ShowApiTestcaseHistoriesRequest.
        :type plan_id: str
        """
        self._plan_id = plan_id

    @property
    def project_id(self):
        r"""Gets the project_id of this ShowApiTestcaseHistoriesRequest.

        项目ID，固定长度32位字符（字母和数字）。

        :return: The project_id of this ShowApiTestcaseHistoriesRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ShowApiTestcaseHistoriesRequest.

        项目ID，固定长度32位字符（字母和数字）。

        :param project_id: The project_id of this ShowApiTestcaseHistoriesRequest.
        :type project_id: str
        """
        self._project_id = project_id

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
        if not isinstance(other, ShowApiTestcaseHistoriesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
