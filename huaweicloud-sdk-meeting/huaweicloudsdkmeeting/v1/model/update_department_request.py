# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateDepartmentRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'x_request_id': 'str',
        'accept_language': 'str',
        'dept_code': 'str',
        'body': 'ModDeptDTO'
    }

    attribute_map = {
        'x_request_id': 'X-Request-Id',
        'accept_language': 'Accept-Language',
        'dept_code': 'dept_code',
        'body': 'body'
    }

    def __init__(self, x_request_id=None, accept_language=None, dept_code=None, body=None):
        """UpdateDepartmentRequest

        The model defined in huaweicloud sdk

        :param x_request_id: 请求requestId，用来标识一路请求，用于问题跟踪定位，建议使用UUID，若不携带，则后台自动生成。
        :type x_request_id: str
        :param accept_language: 语言参数，默认为中文zh-CN，英文为en-US。
        :type accept_language: str
        :param dept_code: 部门编码。 长度： 0-32位。
        :type dept_code: str
        :param body: Body of the UpdateDepartmentRequest
        :type body: :class:`huaweicloudsdkmeeting.v1.ModDeptDTO`
        """
        
        

        self._x_request_id = None
        self._accept_language = None
        self._dept_code = None
        self._body = None
        self.discriminator = None

        if x_request_id is not None:
            self.x_request_id = x_request_id
        if accept_language is not None:
            self.accept_language = accept_language
        self.dept_code = dept_code
        if body is not None:
            self.body = body

    @property
    def x_request_id(self):
        """Gets the x_request_id of this UpdateDepartmentRequest.

        请求requestId，用来标识一路请求，用于问题跟踪定位，建议使用UUID，若不携带，则后台自动生成。

        :return: The x_request_id of this UpdateDepartmentRequest.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this UpdateDepartmentRequest.

        请求requestId，用来标识一路请求，用于问题跟踪定位，建议使用UUID，若不携带，则后台自动生成。

        :param x_request_id: The x_request_id of this UpdateDepartmentRequest.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

    @property
    def accept_language(self):
        """Gets the accept_language of this UpdateDepartmentRequest.

        语言参数，默认为中文zh-CN，英文为en-US。

        :return: The accept_language of this UpdateDepartmentRequest.
        :rtype: str
        """
        return self._accept_language

    @accept_language.setter
    def accept_language(self, accept_language):
        """Sets the accept_language of this UpdateDepartmentRequest.

        语言参数，默认为中文zh-CN，英文为en-US。

        :param accept_language: The accept_language of this UpdateDepartmentRequest.
        :type accept_language: str
        """
        self._accept_language = accept_language

    @property
    def dept_code(self):
        """Gets the dept_code of this UpdateDepartmentRequest.

        部门编码。 长度： 0-32位。

        :return: The dept_code of this UpdateDepartmentRequest.
        :rtype: str
        """
        return self._dept_code

    @dept_code.setter
    def dept_code(self, dept_code):
        """Sets the dept_code of this UpdateDepartmentRequest.

        部门编码。 长度： 0-32位。

        :param dept_code: The dept_code of this UpdateDepartmentRequest.
        :type dept_code: str
        """
        self._dept_code = dept_code

    @property
    def body(self):
        """Gets the body of this UpdateDepartmentRequest.


        :return: The body of this UpdateDepartmentRequest.
        :rtype: :class:`huaweicloudsdkmeeting.v1.ModDeptDTO`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateDepartmentRequest.


        :param body: The body of this UpdateDepartmentRequest.
        :type body: :class:`huaweicloudsdkmeeting.v1.ModDeptDTO`
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
        if not isinstance(other, UpdateDepartmentRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
