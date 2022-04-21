# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchDeleteTestCaseRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'service_id': 'int',
        'testcase_id_list': 'list[str]'
    }

    attribute_map = {
        'service_id': 'service_id',
        'testcase_id_list': 'testcase_id_list'
    }

    def __init__(self, service_id=None, testcase_id_list=None):
        """BatchDeleteTestCaseRequestBody

        The model defined in huaweicloud sdk

        :param service_id: 注册测试类型服务接口返回的服务id，取值范围为10-9999
        :type service_id: int
        :param testcase_id_list: 测试用例唯一标识，数组长度小于50个
        :type testcase_id_list: list[str]
        """
        
        

        self._service_id = None
        self._testcase_id_list = None
        self.discriminator = None

        self.service_id = service_id
        self.testcase_id_list = testcase_id_list

    @property
    def service_id(self):
        """Gets the service_id of this BatchDeleteTestCaseRequestBody.

        注册测试类型服务接口返回的服务id，取值范围为10-9999

        :return: The service_id of this BatchDeleteTestCaseRequestBody.
        :rtype: int
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        """Sets the service_id of this BatchDeleteTestCaseRequestBody.

        注册测试类型服务接口返回的服务id，取值范围为10-9999

        :param service_id: The service_id of this BatchDeleteTestCaseRequestBody.
        :type service_id: int
        """
        self._service_id = service_id

    @property
    def testcase_id_list(self):
        """Gets the testcase_id_list of this BatchDeleteTestCaseRequestBody.

        测试用例唯一标识，数组长度小于50个

        :return: The testcase_id_list of this BatchDeleteTestCaseRequestBody.
        :rtype: list[str]
        """
        return self._testcase_id_list

    @testcase_id_list.setter
    def testcase_id_list(self, testcase_id_list):
        """Sets the testcase_id_list of this BatchDeleteTestCaseRequestBody.

        测试用例唯一标识，数组长度小于50个

        :param testcase_id_list: The testcase_id_list of this BatchDeleteTestCaseRequestBody.
        :type testcase_id_list: list[str]
        """
        self._testcase_id_list = testcase_id_list

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
        if not isinstance(other, BatchDeleteTestCaseRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
