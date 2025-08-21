# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MergeErrorDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'merge_user_name': 'str',
        'merge_start_time': 'str',
        'error_title': 'str',
        'http_code_status': 'str',
        'error_code': 'str',
        'error_message': 'str'
    }

    attribute_map = {
        'merge_user_name': 'merge_user_name',
        'merge_start_time': 'merge_start_time',
        'error_title': 'error_title',
        'http_code_status': 'http_code_status',
        'error_code': 'error_code',
        'error_message': 'error_message'
    }

    def __init__(self, merge_user_name=None, merge_start_time=None, error_title=None, http_code_status=None, error_code=None, error_message=None):
        r"""MergeErrorDto

        The model defined in huaweicloud sdk

        :param merge_user_name: 合并人名字
        :type merge_user_name: str
        :param merge_start_time: 合入时间
        :type merge_start_time: str
        :param error_title: 错误标题
        :type error_title: str
        :param http_code_status: 状态码
        :type http_code_status: str
        :param error_code: 错误码
        :type error_code: str
        :param error_message: 错误信息
        :type error_message: str
        """
        
        

        self._merge_user_name = None
        self._merge_start_time = None
        self._error_title = None
        self._http_code_status = None
        self._error_code = None
        self._error_message = None
        self.discriminator = None

        if merge_user_name is not None:
            self.merge_user_name = merge_user_name
        if merge_start_time is not None:
            self.merge_start_time = merge_start_time
        if error_title is not None:
            self.error_title = error_title
        if http_code_status is not None:
            self.http_code_status = http_code_status
        if error_code is not None:
            self.error_code = error_code
        if error_message is not None:
            self.error_message = error_message

    @property
    def merge_user_name(self):
        r"""Gets the merge_user_name of this MergeErrorDto.

        合并人名字

        :return: The merge_user_name of this MergeErrorDto.
        :rtype: str
        """
        return self._merge_user_name

    @merge_user_name.setter
    def merge_user_name(self, merge_user_name):
        r"""Sets the merge_user_name of this MergeErrorDto.

        合并人名字

        :param merge_user_name: The merge_user_name of this MergeErrorDto.
        :type merge_user_name: str
        """
        self._merge_user_name = merge_user_name

    @property
    def merge_start_time(self):
        r"""Gets the merge_start_time of this MergeErrorDto.

        合入时间

        :return: The merge_start_time of this MergeErrorDto.
        :rtype: str
        """
        return self._merge_start_time

    @merge_start_time.setter
    def merge_start_time(self, merge_start_time):
        r"""Sets the merge_start_time of this MergeErrorDto.

        合入时间

        :param merge_start_time: The merge_start_time of this MergeErrorDto.
        :type merge_start_time: str
        """
        self._merge_start_time = merge_start_time

    @property
    def error_title(self):
        r"""Gets the error_title of this MergeErrorDto.

        错误标题

        :return: The error_title of this MergeErrorDto.
        :rtype: str
        """
        return self._error_title

    @error_title.setter
    def error_title(self, error_title):
        r"""Sets the error_title of this MergeErrorDto.

        错误标题

        :param error_title: The error_title of this MergeErrorDto.
        :type error_title: str
        """
        self._error_title = error_title

    @property
    def http_code_status(self):
        r"""Gets the http_code_status of this MergeErrorDto.

        状态码

        :return: The http_code_status of this MergeErrorDto.
        :rtype: str
        """
        return self._http_code_status

    @http_code_status.setter
    def http_code_status(self, http_code_status):
        r"""Sets the http_code_status of this MergeErrorDto.

        状态码

        :param http_code_status: The http_code_status of this MergeErrorDto.
        :type http_code_status: str
        """
        self._http_code_status = http_code_status

    @property
    def error_code(self):
        r"""Gets the error_code of this MergeErrorDto.

        错误码

        :return: The error_code of this MergeErrorDto.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this MergeErrorDto.

        错误码

        :param error_code: The error_code of this MergeErrorDto.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_message(self):
        r"""Gets the error_message of this MergeErrorDto.

        错误信息

        :return: The error_message of this MergeErrorDto.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        r"""Sets the error_message of this MergeErrorDto.

        错误信息

        :param error_message: The error_message of this MergeErrorDto.
        :type error_message: str
        """
        self._error_message = error_message

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
        if not isinstance(other, MergeErrorDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
