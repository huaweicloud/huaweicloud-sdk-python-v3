# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateTestCaseResponse(SdkResponse):

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
        'project_id': 'str',
        'service_id': 'int',
        'name': 'str',
        'testcase_number': 'str',
        'rank_id': 'int',
        'status_id': 'str',
        'assigned_user': 'AssignedUserInfo',
        'execute_count': 'int',
        'result_id': 'str',
        'extend_info': 'ExtendInfo',
        'error_code': 'str',
        'error_msg': 'str'
    }

    attribute_map = {
        'testcase_id': 'testcase_id',
        'project_id': 'project_id',
        'service_id': 'service_id',
        'name': 'name',
        'testcase_number': 'testcase_number',
        'rank_id': 'rank_id',
        'status_id': 'status_id',
        'assigned_user': 'assigned_user',
        'execute_count': 'execute_count',
        'result_id': 'result_id',
        'extend_info': 'extend_info',
        'error_code': 'error_code',
        'error_msg': 'error_msg'
    }

    def __init__(self, testcase_id=None, project_id=None, service_id=None, name=None, testcase_number=None, rank_id=None, status_id=None, assigned_user=None, execute_count=None, result_id=None, extend_info=None, error_code=None, error_msg=None):
        r"""CreateTestCaseResponse

        The model defined in huaweicloud sdk

        :param testcase_id: 测试用例唯一标识
        :type testcase_id: str
        :param project_id: 软开云项目唯一标识
        :type project_id: str
        :param service_id: 注册测试类型服务接口返回的服务id
        :type service_id: int
        :param name: 测试用例名称
        :type name: str
        :param testcase_number: 测试用例编号
        :type testcase_number: str
        :param rank_id: 测试用例等级
        :type rank_id: int
        :param status_id: 测试用例状态
        :type status_id: str
        :param assigned_user: 
        :type assigned_user: :class:`huaweicloudsdkcloudtest.v1.AssignedUserInfo`
        :param execute_count: 测试用例执行次数
        :type execute_count: int
        :param result_id: 测试用例执行结果
        :type result_id: str
        :param extend_info: 
        :type extend_info: :class:`huaweicloudsdkcloudtest.v1.ExtendInfo`
        :param error_code: 接口调用失败错误码
        :type error_code: str
        :param error_msg: 接口调用失败错误信息
        :type error_msg: str
        """
        
        super(CreateTestCaseResponse, self).__init__()

        self._testcase_id = None
        self._project_id = None
        self._service_id = None
        self._name = None
        self._testcase_number = None
        self._rank_id = None
        self._status_id = None
        self._assigned_user = None
        self._execute_count = None
        self._result_id = None
        self._extend_info = None
        self._error_code = None
        self._error_msg = None
        self.discriminator = None

        if testcase_id is not None:
            self.testcase_id = testcase_id
        if project_id is not None:
            self.project_id = project_id
        if service_id is not None:
            self.service_id = service_id
        if name is not None:
            self.name = name
        if testcase_number is not None:
            self.testcase_number = testcase_number
        if rank_id is not None:
            self.rank_id = rank_id
        if status_id is not None:
            self.status_id = status_id
        if assigned_user is not None:
            self.assigned_user = assigned_user
        if execute_count is not None:
            self.execute_count = execute_count
        if result_id is not None:
            self.result_id = result_id
        if extend_info is not None:
            self.extend_info = extend_info
        if error_code is not None:
            self.error_code = error_code
        if error_msg is not None:
            self.error_msg = error_msg

    @property
    def testcase_id(self):
        r"""Gets the testcase_id of this CreateTestCaseResponse.

        测试用例唯一标识

        :return: The testcase_id of this CreateTestCaseResponse.
        :rtype: str
        """
        return self._testcase_id

    @testcase_id.setter
    def testcase_id(self, testcase_id):
        r"""Sets the testcase_id of this CreateTestCaseResponse.

        测试用例唯一标识

        :param testcase_id: The testcase_id of this CreateTestCaseResponse.
        :type testcase_id: str
        """
        self._testcase_id = testcase_id

    @property
    def project_id(self):
        r"""Gets the project_id of this CreateTestCaseResponse.

        软开云项目唯一标识

        :return: The project_id of this CreateTestCaseResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this CreateTestCaseResponse.

        软开云项目唯一标识

        :param project_id: The project_id of this CreateTestCaseResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def service_id(self):
        r"""Gets the service_id of this CreateTestCaseResponse.

        注册测试类型服务接口返回的服务id

        :return: The service_id of this CreateTestCaseResponse.
        :rtype: int
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        r"""Sets the service_id of this CreateTestCaseResponse.

        注册测试类型服务接口返回的服务id

        :param service_id: The service_id of this CreateTestCaseResponse.
        :type service_id: int
        """
        self._service_id = service_id

    @property
    def name(self):
        r"""Gets the name of this CreateTestCaseResponse.

        测试用例名称

        :return: The name of this CreateTestCaseResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateTestCaseResponse.

        测试用例名称

        :param name: The name of this CreateTestCaseResponse.
        :type name: str
        """
        self._name = name

    @property
    def testcase_number(self):
        r"""Gets the testcase_number of this CreateTestCaseResponse.

        测试用例编号

        :return: The testcase_number of this CreateTestCaseResponse.
        :rtype: str
        """
        return self._testcase_number

    @testcase_number.setter
    def testcase_number(self, testcase_number):
        r"""Sets the testcase_number of this CreateTestCaseResponse.

        测试用例编号

        :param testcase_number: The testcase_number of this CreateTestCaseResponse.
        :type testcase_number: str
        """
        self._testcase_number = testcase_number

    @property
    def rank_id(self):
        r"""Gets the rank_id of this CreateTestCaseResponse.

        测试用例等级

        :return: The rank_id of this CreateTestCaseResponse.
        :rtype: int
        """
        return self._rank_id

    @rank_id.setter
    def rank_id(self, rank_id):
        r"""Sets the rank_id of this CreateTestCaseResponse.

        测试用例等级

        :param rank_id: The rank_id of this CreateTestCaseResponse.
        :type rank_id: int
        """
        self._rank_id = rank_id

    @property
    def status_id(self):
        r"""Gets the status_id of this CreateTestCaseResponse.

        测试用例状态

        :return: The status_id of this CreateTestCaseResponse.
        :rtype: str
        """
        return self._status_id

    @status_id.setter
    def status_id(self, status_id):
        r"""Sets the status_id of this CreateTestCaseResponse.

        测试用例状态

        :param status_id: The status_id of this CreateTestCaseResponse.
        :type status_id: str
        """
        self._status_id = status_id

    @property
    def assigned_user(self):
        r"""Gets the assigned_user of this CreateTestCaseResponse.

        :return: The assigned_user of this CreateTestCaseResponse.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.AssignedUserInfo`
        """
        return self._assigned_user

    @assigned_user.setter
    def assigned_user(self, assigned_user):
        r"""Sets the assigned_user of this CreateTestCaseResponse.

        :param assigned_user: The assigned_user of this CreateTestCaseResponse.
        :type assigned_user: :class:`huaweicloudsdkcloudtest.v1.AssignedUserInfo`
        """
        self._assigned_user = assigned_user

    @property
    def execute_count(self):
        r"""Gets the execute_count of this CreateTestCaseResponse.

        测试用例执行次数

        :return: The execute_count of this CreateTestCaseResponse.
        :rtype: int
        """
        return self._execute_count

    @execute_count.setter
    def execute_count(self, execute_count):
        r"""Sets the execute_count of this CreateTestCaseResponse.

        测试用例执行次数

        :param execute_count: The execute_count of this CreateTestCaseResponse.
        :type execute_count: int
        """
        self._execute_count = execute_count

    @property
    def result_id(self):
        r"""Gets the result_id of this CreateTestCaseResponse.

        测试用例执行结果

        :return: The result_id of this CreateTestCaseResponse.
        :rtype: str
        """
        return self._result_id

    @result_id.setter
    def result_id(self, result_id):
        r"""Sets the result_id of this CreateTestCaseResponse.

        测试用例执行结果

        :param result_id: The result_id of this CreateTestCaseResponse.
        :type result_id: str
        """
        self._result_id = result_id

    @property
    def extend_info(self):
        r"""Gets the extend_info of this CreateTestCaseResponse.

        :return: The extend_info of this CreateTestCaseResponse.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.ExtendInfo`
        """
        return self._extend_info

    @extend_info.setter
    def extend_info(self, extend_info):
        r"""Sets the extend_info of this CreateTestCaseResponse.

        :param extend_info: The extend_info of this CreateTestCaseResponse.
        :type extend_info: :class:`huaweicloudsdkcloudtest.v1.ExtendInfo`
        """
        self._extend_info = extend_info

    @property
    def error_code(self):
        r"""Gets the error_code of this CreateTestCaseResponse.

        接口调用失败错误码

        :return: The error_code of this CreateTestCaseResponse.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this CreateTestCaseResponse.

        接口调用失败错误码

        :param error_code: The error_code of this CreateTestCaseResponse.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_msg(self):
        r"""Gets the error_msg of this CreateTestCaseResponse.

        接口调用失败错误信息

        :return: The error_msg of this CreateTestCaseResponse.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        r"""Sets the error_msg of this CreateTestCaseResponse.

        接口调用失败错误信息

        :param error_msg: The error_msg of this CreateTestCaseResponse.
        :type error_msg: str
        """
        self._error_msg = error_msg

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
        if not isinstance(other, CreateTestCaseResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
