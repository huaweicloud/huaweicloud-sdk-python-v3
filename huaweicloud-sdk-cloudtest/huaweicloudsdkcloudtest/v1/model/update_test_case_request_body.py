# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateTestCaseRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'service_id': 'int',
        'rank_id': 'str',
        'testcase_number': 'str',
        'extend_info': 'ExternalServiceBizCase'
    }

    attribute_map = {
        'name': 'name',
        'service_id': 'service_id',
        'rank_id': 'rank_id',
        'testcase_number': 'testcase_number',
        'extend_info': 'extend_info'
    }

    def __init__(self, name=None, service_id=None, rank_id=None, testcase_number=None, extend_info=None):
        r"""UpdateTestCaseRequestBody

        The model defined in huaweicloud sdk

        :param name: 页面上显示的用例名称，长度为[3-128]位字符
        :type name: str
        :param service_id: 注册测试类型服务接口返回的服务id，取值范围为10-9999
        :type service_id: int
        :param rank_id: 测试用例等级，可选值为[0,1,2,3,4]，不填时默认为2
        :type rank_id: str
        :param testcase_number: 用例编号，不填该值时会自动生成，长度为[3-128]位字符
        :type testcase_number: str
        :param extend_info: 
        :type extend_info: :class:`huaweicloudsdkcloudtest.v1.ExternalServiceBizCase`
        """
        
        

        self._name = None
        self._service_id = None
        self._rank_id = None
        self._testcase_number = None
        self._extend_info = None
        self.discriminator = None

        self.name = name
        self.service_id = service_id
        if rank_id is not None:
            self.rank_id = rank_id
        if testcase_number is not None:
            self.testcase_number = testcase_number
        if extend_info is not None:
            self.extend_info = extend_info

    @property
    def name(self):
        r"""Gets the name of this UpdateTestCaseRequestBody.

        页面上显示的用例名称，长度为[3-128]位字符

        :return: The name of this UpdateTestCaseRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateTestCaseRequestBody.

        页面上显示的用例名称，长度为[3-128]位字符

        :param name: The name of this UpdateTestCaseRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def service_id(self):
        r"""Gets the service_id of this UpdateTestCaseRequestBody.

        注册测试类型服务接口返回的服务id，取值范围为10-9999

        :return: The service_id of this UpdateTestCaseRequestBody.
        :rtype: int
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        r"""Sets the service_id of this UpdateTestCaseRequestBody.

        注册测试类型服务接口返回的服务id，取值范围为10-9999

        :param service_id: The service_id of this UpdateTestCaseRequestBody.
        :type service_id: int
        """
        self._service_id = service_id

    @property
    def rank_id(self):
        r"""Gets the rank_id of this UpdateTestCaseRequestBody.

        测试用例等级，可选值为[0,1,2,3,4]，不填时默认为2

        :return: The rank_id of this UpdateTestCaseRequestBody.
        :rtype: str
        """
        return self._rank_id

    @rank_id.setter
    def rank_id(self, rank_id):
        r"""Sets the rank_id of this UpdateTestCaseRequestBody.

        测试用例等级，可选值为[0,1,2,3,4]，不填时默认为2

        :param rank_id: The rank_id of this UpdateTestCaseRequestBody.
        :type rank_id: str
        """
        self._rank_id = rank_id

    @property
    def testcase_number(self):
        r"""Gets the testcase_number of this UpdateTestCaseRequestBody.

        用例编号，不填该值时会自动生成，长度为[3-128]位字符

        :return: The testcase_number of this UpdateTestCaseRequestBody.
        :rtype: str
        """
        return self._testcase_number

    @testcase_number.setter
    def testcase_number(self, testcase_number):
        r"""Sets the testcase_number of this UpdateTestCaseRequestBody.

        用例编号，不填该值时会自动生成，长度为[3-128]位字符

        :param testcase_number: The testcase_number of this UpdateTestCaseRequestBody.
        :type testcase_number: str
        """
        self._testcase_number = testcase_number

    @property
    def extend_info(self):
        r"""Gets the extend_info of this UpdateTestCaseRequestBody.

        :return: The extend_info of this UpdateTestCaseRequestBody.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.ExternalServiceBizCase`
        """
        return self._extend_info

    @extend_info.setter
    def extend_info(self, extend_info):
        r"""Sets the extend_info of this UpdateTestCaseRequestBody.

        :param extend_info: The extend_info of this UpdateTestCaseRequestBody.
        :type extend_info: :class:`huaweicloudsdkcloudtest.v1.ExternalServiceBizCase`
        """
        self._extend_info = extend_info

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
        if not isinstance(other, UpdateTestCaseRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
