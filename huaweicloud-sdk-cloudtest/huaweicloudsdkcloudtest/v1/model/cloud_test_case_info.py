# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CloudTestCaseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'case_id': 'str',
        'case_type': 'int',
        'is_forbidden': 'int',
        'owner': 'CommonDto',
        'result': 'CommonDto',
        'script_url': 'str',
        'status': 'CommonDto',
        'test_case_name': 'str',
        'test_case_number': 'str',
        'tmss_version_uri': 'str'
    }

    attribute_map = {
        'case_id': 'case_id',
        'case_type': 'caseType',
        'is_forbidden': 'is_forbidden',
        'owner': 'owner',
        'result': 'result',
        'script_url': 'scriptUrl',
        'status': 'status',
        'test_case_name': 'testCaseName',
        'test_case_number': 'testCaseNumber',
        'tmss_version_uri': 'tmssVersionUri'
    }

    def __init__(self, case_id=None, case_type=None, is_forbidden=None, owner=None, result=None, script_url=None, status=None, test_case_name=None, test_case_number=None, tmss_version_uri=None):
        r"""CloudTestCaseInfo

        The model defined in huaweicloud sdk

        :param case_id: 用例id
        :type case_id: str
        :param case_type: tmss用例类型
        :type case_type: int
        :param is_forbidden: 是否未禁用，1为未禁用，0为已禁用
        :type is_forbidden: int
        :param owner: 
        :type owner: :class:`huaweicloudsdkcloudtest.v1.CommonDto`
        :param result: 
        :type result: :class:`huaweicloudsdkcloudtest.v1.CommonDto`
        :param script_url: 用例脚本路径
        :type script_url: str
        :param status: 
        :type status: :class:`huaweicloudsdkcloudtest.v1.CommonDto`
        :param test_case_name: 用例名称
        :type test_case_name: str
        :param test_case_number: 用例编号
        :type test_case_number: str
        :param tmss_version_uri: tmss版本地址
        :type tmss_version_uri: str
        """
        
        

        self._case_id = None
        self._case_type = None
        self._is_forbidden = None
        self._owner = None
        self._result = None
        self._script_url = None
        self._status = None
        self._test_case_name = None
        self._test_case_number = None
        self._tmss_version_uri = None
        self.discriminator = None

        if case_id is not None:
            self.case_id = case_id
        if case_type is not None:
            self.case_type = case_type
        if is_forbidden is not None:
            self.is_forbidden = is_forbidden
        if owner is not None:
            self.owner = owner
        if result is not None:
            self.result = result
        if script_url is not None:
            self.script_url = script_url
        if status is not None:
            self.status = status
        if test_case_name is not None:
            self.test_case_name = test_case_name
        if test_case_number is not None:
            self.test_case_number = test_case_number
        if tmss_version_uri is not None:
            self.tmss_version_uri = tmss_version_uri

    @property
    def case_id(self):
        r"""Gets the case_id of this CloudTestCaseInfo.

        用例id

        :return: The case_id of this CloudTestCaseInfo.
        :rtype: str
        """
        return self._case_id

    @case_id.setter
    def case_id(self, case_id):
        r"""Sets the case_id of this CloudTestCaseInfo.

        用例id

        :param case_id: The case_id of this CloudTestCaseInfo.
        :type case_id: str
        """
        self._case_id = case_id

    @property
    def case_type(self):
        r"""Gets the case_type of this CloudTestCaseInfo.

        tmss用例类型

        :return: The case_type of this CloudTestCaseInfo.
        :rtype: int
        """
        return self._case_type

    @case_type.setter
    def case_type(self, case_type):
        r"""Sets the case_type of this CloudTestCaseInfo.

        tmss用例类型

        :param case_type: The case_type of this CloudTestCaseInfo.
        :type case_type: int
        """
        self._case_type = case_type

    @property
    def is_forbidden(self):
        r"""Gets the is_forbidden of this CloudTestCaseInfo.

        是否未禁用，1为未禁用，0为已禁用

        :return: The is_forbidden of this CloudTestCaseInfo.
        :rtype: int
        """
        return self._is_forbidden

    @is_forbidden.setter
    def is_forbidden(self, is_forbidden):
        r"""Sets the is_forbidden of this CloudTestCaseInfo.

        是否未禁用，1为未禁用，0为已禁用

        :param is_forbidden: The is_forbidden of this CloudTestCaseInfo.
        :type is_forbidden: int
        """
        self._is_forbidden = is_forbidden

    @property
    def owner(self):
        r"""Gets the owner of this CloudTestCaseInfo.

        :return: The owner of this CloudTestCaseInfo.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.CommonDto`
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        r"""Sets the owner of this CloudTestCaseInfo.

        :param owner: The owner of this CloudTestCaseInfo.
        :type owner: :class:`huaweicloudsdkcloudtest.v1.CommonDto`
        """
        self._owner = owner

    @property
    def result(self):
        r"""Gets the result of this CloudTestCaseInfo.

        :return: The result of this CloudTestCaseInfo.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.CommonDto`
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this CloudTestCaseInfo.

        :param result: The result of this CloudTestCaseInfo.
        :type result: :class:`huaweicloudsdkcloudtest.v1.CommonDto`
        """
        self._result = result

    @property
    def script_url(self):
        r"""Gets the script_url of this CloudTestCaseInfo.

        用例脚本路径

        :return: The script_url of this CloudTestCaseInfo.
        :rtype: str
        """
        return self._script_url

    @script_url.setter
    def script_url(self, script_url):
        r"""Sets the script_url of this CloudTestCaseInfo.

        用例脚本路径

        :param script_url: The script_url of this CloudTestCaseInfo.
        :type script_url: str
        """
        self._script_url = script_url

    @property
    def status(self):
        r"""Gets the status of this CloudTestCaseInfo.

        :return: The status of this CloudTestCaseInfo.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.CommonDto`
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CloudTestCaseInfo.

        :param status: The status of this CloudTestCaseInfo.
        :type status: :class:`huaweicloudsdkcloudtest.v1.CommonDto`
        """
        self._status = status

    @property
    def test_case_name(self):
        r"""Gets the test_case_name of this CloudTestCaseInfo.

        用例名称

        :return: The test_case_name of this CloudTestCaseInfo.
        :rtype: str
        """
        return self._test_case_name

    @test_case_name.setter
    def test_case_name(self, test_case_name):
        r"""Sets the test_case_name of this CloudTestCaseInfo.

        用例名称

        :param test_case_name: The test_case_name of this CloudTestCaseInfo.
        :type test_case_name: str
        """
        self._test_case_name = test_case_name

    @property
    def test_case_number(self):
        r"""Gets the test_case_number of this CloudTestCaseInfo.

        用例编号

        :return: The test_case_number of this CloudTestCaseInfo.
        :rtype: str
        """
        return self._test_case_number

    @test_case_number.setter
    def test_case_number(self, test_case_number):
        r"""Sets the test_case_number of this CloudTestCaseInfo.

        用例编号

        :param test_case_number: The test_case_number of this CloudTestCaseInfo.
        :type test_case_number: str
        """
        self._test_case_number = test_case_number

    @property
    def tmss_version_uri(self):
        r"""Gets the tmss_version_uri of this CloudTestCaseInfo.

        tmss版本地址

        :return: The tmss_version_uri of this CloudTestCaseInfo.
        :rtype: str
        """
        return self._tmss_version_uri

    @tmss_version_uri.setter
    def tmss_version_uri(self, tmss_version_uri):
        r"""Sets the tmss_version_uri of this CloudTestCaseInfo.

        tmss版本地址

        :param tmss_version_uri: The tmss_version_uri of this CloudTestCaseInfo.
        :type tmss_version_uri: str
        """
        self._tmss_version_uri = tmss_version_uri

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CloudTestCaseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
