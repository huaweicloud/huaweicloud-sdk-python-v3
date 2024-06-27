# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskAssignCaseVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sort': 'int',
        'case_uri': 'str',
        'is_available': 'int',
        'test_case_name': 'str',
        'test_case_number': 'str'
    }

    attribute_map = {
        'sort': 'sort',
        'case_uri': 'case_uri',
        'is_available': 'is_available',
        'test_case_name': 'test_case_name',
        'test_case_number': 'test_case_number'
    }

    def __init__(self, sort=None, case_uri=None, is_available=None, test_case_name=None, test_case_number=None):
        """TaskAssignCaseVo

        The model defined in huaweicloud sdk

        :param sort: 排序顺序
        :type sort: int
        :param case_uri: 用例uri
        :type case_uri: str
        :param is_available: 是否可用
        :type is_available: int
        :param test_case_name: 用例名称
        :type test_case_name: str
        :param test_case_number: 用例编号
        :type test_case_number: str
        """
        
        

        self._sort = None
        self._case_uri = None
        self._is_available = None
        self._test_case_name = None
        self._test_case_number = None
        self.discriminator = None

        if sort is not None:
            self.sort = sort
        if case_uri is not None:
            self.case_uri = case_uri
        if is_available is not None:
            self.is_available = is_available
        if test_case_name is not None:
            self.test_case_name = test_case_name
        if test_case_number is not None:
            self.test_case_number = test_case_number

    @property
    def sort(self):
        """Gets the sort of this TaskAssignCaseVo.

        排序顺序

        :return: The sort of this TaskAssignCaseVo.
        :rtype: int
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        """Sets the sort of this TaskAssignCaseVo.

        排序顺序

        :param sort: The sort of this TaskAssignCaseVo.
        :type sort: int
        """
        self._sort = sort

    @property
    def case_uri(self):
        """Gets the case_uri of this TaskAssignCaseVo.

        用例uri

        :return: The case_uri of this TaskAssignCaseVo.
        :rtype: str
        """
        return self._case_uri

    @case_uri.setter
    def case_uri(self, case_uri):
        """Sets the case_uri of this TaskAssignCaseVo.

        用例uri

        :param case_uri: The case_uri of this TaskAssignCaseVo.
        :type case_uri: str
        """
        self._case_uri = case_uri

    @property
    def is_available(self):
        """Gets the is_available of this TaskAssignCaseVo.

        是否可用

        :return: The is_available of this TaskAssignCaseVo.
        :rtype: int
        """
        return self._is_available

    @is_available.setter
    def is_available(self, is_available):
        """Sets the is_available of this TaskAssignCaseVo.

        是否可用

        :param is_available: The is_available of this TaskAssignCaseVo.
        :type is_available: int
        """
        self._is_available = is_available

    @property
    def test_case_name(self):
        """Gets the test_case_name of this TaskAssignCaseVo.

        用例名称

        :return: The test_case_name of this TaskAssignCaseVo.
        :rtype: str
        """
        return self._test_case_name

    @test_case_name.setter
    def test_case_name(self, test_case_name):
        """Sets the test_case_name of this TaskAssignCaseVo.

        用例名称

        :param test_case_name: The test_case_name of this TaskAssignCaseVo.
        :type test_case_name: str
        """
        self._test_case_name = test_case_name

    @property
    def test_case_number(self):
        """Gets the test_case_number of this TaskAssignCaseVo.

        用例编号

        :return: The test_case_number of this TaskAssignCaseVo.
        :rtype: str
        """
        return self._test_case_number

    @test_case_number.setter
    def test_case_number(self, test_case_number):
        """Sets the test_case_number of this TaskAssignCaseVo.

        用例编号

        :param test_case_number: The test_case_number of this TaskAssignCaseVo.
        :type test_case_number: str
        """
        self._test_case_number = test_case_number

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
        if not isinstance(other, TaskAssignCaseVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
