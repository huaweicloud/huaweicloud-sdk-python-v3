# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AppDeleteResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'application_id': 'str',
        'application_name': 'str',
        'status': 'str',
        'error_reason': 'str'
    }

    attribute_map = {
        'application_id': 'application_id',
        'application_name': 'application_name',
        'status': 'status',
        'error_reason': 'error_reason'
    }

    def __init__(self, application_id=None, application_name=None, status=None, error_reason=None):
        r"""AppDeleteResult

        The model defined in huaweicloud sdk

        :param application_id: 应用id
        :type application_id: str
        :param application_name: 应用名称
        :type application_name: str
        :param status: 删除是否成功 success | error
        :type status: str
        :param error_reason: 删除失败原因
        :type error_reason: str
        """
        
        

        self._application_id = None
        self._application_name = None
        self._status = None
        self._error_reason = None
        self.discriminator = None

        if application_id is not None:
            self.application_id = application_id
        if application_name is not None:
            self.application_name = application_name
        if status is not None:
            self.status = status
        if error_reason is not None:
            self.error_reason = error_reason

    @property
    def application_id(self):
        r"""Gets the application_id of this AppDeleteResult.

        应用id

        :return: The application_id of this AppDeleteResult.
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        r"""Sets the application_id of this AppDeleteResult.

        应用id

        :param application_id: The application_id of this AppDeleteResult.
        :type application_id: str
        """
        self._application_id = application_id

    @property
    def application_name(self):
        r"""Gets the application_name of this AppDeleteResult.

        应用名称

        :return: The application_name of this AppDeleteResult.
        :rtype: str
        """
        return self._application_name

    @application_name.setter
    def application_name(self, application_name):
        r"""Sets the application_name of this AppDeleteResult.

        应用名称

        :param application_name: The application_name of this AppDeleteResult.
        :type application_name: str
        """
        self._application_name = application_name

    @property
    def status(self):
        r"""Gets the status of this AppDeleteResult.

        删除是否成功 success | error

        :return: The status of this AppDeleteResult.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this AppDeleteResult.

        删除是否成功 success | error

        :param status: The status of this AppDeleteResult.
        :type status: str
        """
        self._status = status

    @property
    def error_reason(self):
        r"""Gets the error_reason of this AppDeleteResult.

        删除失败原因

        :return: The error_reason of this AppDeleteResult.
        :rtype: str
        """
        return self._error_reason

    @error_reason.setter
    def error_reason(self, error_reason):
        r"""Sets the error_reason of this AppDeleteResult.

        删除失败原因

        :param error_reason: The error_reason of this AppDeleteResult.
        :type error_reason: str
        """
        self._error_reason = error_reason

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
        if not isinstance(other, AppDeleteResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
