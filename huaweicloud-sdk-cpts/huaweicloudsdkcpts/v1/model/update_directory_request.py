# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateDirectoryRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'directory_id': 'int',
        'test_suite_id': 'int',
        'body': 'UpdateDirectoryRequestBody'
    }

    attribute_map = {
        'directory_id': 'directory_id',
        'test_suite_id': 'test_suite_id',
        'body': 'body'
    }

    def __init__(self, directory_id=None, test_suite_id=None, body=None):
        """UpdateDirectoryRequest

        The model defined in huaweicloud sdk

        :param directory_id: 目录id
        :type directory_id: int
        :param test_suite_id: 测试工程id
        :type test_suite_id: int
        :param body: Body of the UpdateDirectoryRequest
        :type body: :class:`huaweicloudsdkcpts.v1.UpdateDirectoryRequestBody`
        """
        
        

        self._directory_id = None
        self._test_suite_id = None
        self._body = None
        self.discriminator = None

        self.directory_id = directory_id
        self.test_suite_id = test_suite_id
        if body is not None:
            self.body = body

    @property
    def directory_id(self):
        """Gets the directory_id of this UpdateDirectoryRequest.

        目录id

        :return: The directory_id of this UpdateDirectoryRequest.
        :rtype: int
        """
        return self._directory_id

    @directory_id.setter
    def directory_id(self, directory_id):
        """Sets the directory_id of this UpdateDirectoryRequest.

        目录id

        :param directory_id: The directory_id of this UpdateDirectoryRequest.
        :type directory_id: int
        """
        self._directory_id = directory_id

    @property
    def test_suite_id(self):
        """Gets the test_suite_id of this UpdateDirectoryRequest.

        测试工程id

        :return: The test_suite_id of this UpdateDirectoryRequest.
        :rtype: int
        """
        return self._test_suite_id

    @test_suite_id.setter
    def test_suite_id(self, test_suite_id):
        """Sets the test_suite_id of this UpdateDirectoryRequest.

        测试工程id

        :param test_suite_id: The test_suite_id of this UpdateDirectoryRequest.
        :type test_suite_id: int
        """
        self._test_suite_id = test_suite_id

    @property
    def body(self):
        """Gets the body of this UpdateDirectoryRequest.

        :return: The body of this UpdateDirectoryRequest.
        :rtype: :class:`huaweicloudsdkcpts.v1.UpdateDirectoryRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateDirectoryRequest.

        :param body: The body of this UpdateDirectoryRequest.
        :type body: :class:`huaweicloudsdkcpts.v1.UpdateDirectoryRequestBody`
        """
        self._body = body

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
        if not isinstance(other, UpdateDirectoryRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
