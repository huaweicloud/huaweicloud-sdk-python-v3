# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UploadUserJdbcDriverRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_language': 'str',
        'driver_type': 'str',
        'body': 'UploadUserJdbcDriverRequestBody'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'driver_type': 'driver_type',
        'body': 'body'
    }

    def __init__(self, x_language=None, driver_type=None, body=None):
        r"""UploadUserJdbcDriverRequest

        The model defined in huaweicloud sdk

        :param x_language: 请求语言类型。
        :type x_language: str
        :param driver_type: 指定待上传的驱动文件类型。取值范围： - db2：DB2 for LUW - informix：Informix
        :type driver_type: str
        :param body: Body of the UploadUserJdbcDriverRequest
        :type body: :class:`huaweicloudsdkdrs.v5.UploadUserJdbcDriverRequestBody`
        """
        
        

        self._x_language = None
        self._driver_type = None
        self._body = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        self.driver_type = driver_type
        if body is not None:
            self.body = body

    @property
    def x_language(self):
        r"""Gets the x_language of this UploadUserJdbcDriverRequest.

        请求语言类型。

        :return: The x_language of this UploadUserJdbcDriverRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this UploadUserJdbcDriverRequest.

        请求语言类型。

        :param x_language: The x_language of this UploadUserJdbcDriverRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def driver_type(self):
        r"""Gets the driver_type of this UploadUserJdbcDriverRequest.

        指定待上传的驱动文件类型。取值范围： - db2：DB2 for LUW - informix：Informix

        :return: The driver_type of this UploadUserJdbcDriverRequest.
        :rtype: str
        """
        return self._driver_type

    @driver_type.setter
    def driver_type(self, driver_type):
        r"""Sets the driver_type of this UploadUserJdbcDriverRequest.

        指定待上传的驱动文件类型。取值范围： - db2：DB2 for LUW - informix：Informix

        :param driver_type: The driver_type of this UploadUserJdbcDriverRequest.
        :type driver_type: str
        """
        self._driver_type = driver_type

    @property
    def body(self):
        r"""Gets the body of this UploadUserJdbcDriverRequest.

        :return: The body of this UploadUserJdbcDriverRequest.
        :rtype: :class:`huaweicloudsdkdrs.v5.UploadUserJdbcDriverRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UploadUserJdbcDriverRequest.

        :param body: The body of this UploadUserJdbcDriverRequest.
        :type body: :class:`huaweicloudsdkdrs.v5.UploadUserJdbcDriverRequestBody`
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
        if not isinstance(other, UploadUserJdbcDriverRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
