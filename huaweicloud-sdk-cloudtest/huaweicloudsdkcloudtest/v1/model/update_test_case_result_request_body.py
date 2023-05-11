# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateTestCaseResultRequestBody:

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
        'execute_list': 'list[UpdateTestCaseResultBean]'
    }

    attribute_map = {
        'service_id': 'service_id',
        'execute_list': 'execute_list'
    }

    def __init__(self, service_id=None, execute_list=None):
        """UpdateTestCaseResultRequestBody

        The model defined in huaweicloud sdk

        :param service_id: 注册测试类型服务接口返回的服务id
        :type service_id: int
        :param execute_list: 测试用例状态信息，数组长度小于等于50
        :type execute_list: list[:class:`huaweicloudsdkcloudtest.v1.UpdateTestCaseResultBean`]
        """
        
        

        self._service_id = None
        self._execute_list = None
        self.discriminator = None

        self.service_id = service_id
        self.execute_list = execute_list

    @property
    def service_id(self):
        """Gets the service_id of this UpdateTestCaseResultRequestBody.

        注册测试类型服务接口返回的服务id

        :return: The service_id of this UpdateTestCaseResultRequestBody.
        :rtype: int
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        """Sets the service_id of this UpdateTestCaseResultRequestBody.

        注册测试类型服务接口返回的服务id

        :param service_id: The service_id of this UpdateTestCaseResultRequestBody.
        :type service_id: int
        """
        self._service_id = service_id

    @property
    def execute_list(self):
        """Gets the execute_list of this UpdateTestCaseResultRequestBody.

        测试用例状态信息，数组长度小于等于50

        :return: The execute_list of this UpdateTestCaseResultRequestBody.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.UpdateTestCaseResultBean`]
        """
        return self._execute_list

    @execute_list.setter
    def execute_list(self, execute_list):
        """Sets the execute_list of this UpdateTestCaseResultRequestBody.

        测试用例状态信息，数组长度小于等于50

        :param execute_list: The execute_list of this UpdateTestCaseResultRequestBody.
        :type execute_list: list[:class:`huaweicloudsdkcloudtest.v1.UpdateTestCaseResultBean`]
        """
        self._execute_list = execute_list

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
        if not isinstance(other, UpdateTestCaseResultRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
