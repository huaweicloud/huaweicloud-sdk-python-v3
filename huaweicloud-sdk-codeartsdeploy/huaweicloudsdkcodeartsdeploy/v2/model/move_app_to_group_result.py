# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MoveAppToGroupResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'code': 'str',
        'application_id': 'str',
        'application_name': 'str',
        'error_code': 'str',
        'error_msg': 'str'
    }

    attribute_map = {
        'code': 'code',
        'application_id': 'application_id',
        'application_name': 'application_name',
        'error_code': 'error_code',
        'error_msg': 'error_msg'
    }

    def __init__(self, code=None, application_id=None, application_name=None, error_code=None, error_msg=None):
        r"""MoveAppToGroupResult

        The model defined in huaweicloud sdk

        :param code: 是否失败
        :type code: str
        :param application_id: 应用id
        :type application_id: str
        :param application_name: 应用名称
        :type application_name: str
        :param error_code: 错误码
        :type error_code: str
        :param error_msg: 错误信息
        :type error_msg: str
        """
        
        

        self._code = None
        self._application_id = None
        self._application_name = None
        self._error_code = None
        self._error_msg = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if application_id is not None:
            self.application_id = application_id
        if application_name is not None:
            self.application_name = application_name
        if error_code is not None:
            self.error_code = error_code
        if error_msg is not None:
            self.error_msg = error_msg

    @property
    def code(self):
        r"""Gets the code of this MoveAppToGroupResult.

        是否失败

        :return: The code of this MoveAppToGroupResult.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this MoveAppToGroupResult.

        是否失败

        :param code: The code of this MoveAppToGroupResult.
        :type code: str
        """
        self._code = code

    @property
    def application_id(self):
        r"""Gets the application_id of this MoveAppToGroupResult.

        应用id

        :return: The application_id of this MoveAppToGroupResult.
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        r"""Sets the application_id of this MoveAppToGroupResult.

        应用id

        :param application_id: The application_id of this MoveAppToGroupResult.
        :type application_id: str
        """
        self._application_id = application_id

    @property
    def application_name(self):
        r"""Gets the application_name of this MoveAppToGroupResult.

        应用名称

        :return: The application_name of this MoveAppToGroupResult.
        :rtype: str
        """
        return self._application_name

    @application_name.setter
    def application_name(self, application_name):
        r"""Sets the application_name of this MoveAppToGroupResult.

        应用名称

        :param application_name: The application_name of this MoveAppToGroupResult.
        :type application_name: str
        """
        self._application_name = application_name

    @property
    def error_code(self):
        r"""Gets the error_code of this MoveAppToGroupResult.

        错误码

        :return: The error_code of this MoveAppToGroupResult.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this MoveAppToGroupResult.

        错误码

        :param error_code: The error_code of this MoveAppToGroupResult.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_msg(self):
        r"""Gets the error_msg of this MoveAppToGroupResult.

        错误信息

        :return: The error_msg of this MoveAppToGroupResult.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        r"""Sets the error_msg of this MoveAppToGroupResult.

        错误信息

        :param error_msg: The error_msg of this MoveAppToGroupResult.
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
        if not isinstance(other, MoveAppToGroupResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
