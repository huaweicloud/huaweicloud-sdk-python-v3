# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RespcodeBrokens:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'check_point_failed': 'list[int]',
        'error': 'list[int]',
        'others_failed': 'list[int]',
        'parsed_failed': 'list[int]',
        'refused_failed': 'list[int]',
        'success': 'list[int]',
        'timeout': 'list[int]'
    }

    attribute_map = {
        'check_point_failed': 'checkPointFailed',
        'error': 'error',
        'others_failed': 'othersFailed',
        'parsed_failed': 'parsedFailed',
        'refused_failed': 'refusedFailed',
        'success': 'success',
        'timeout': 'timeout'
    }

    def __init__(self, check_point_failed=None, error=None, others_failed=None, parsed_failed=None, refused_failed=None, success=None, timeout=None):
        """RespcodeBrokens - a model defined in huaweicloud sdk"""
        
        

        self._check_point_failed = None
        self._error = None
        self._others_failed = None
        self._parsed_failed = None
        self._refused_failed = None
        self._success = None
        self._timeout = None
        self.discriminator = None

        if check_point_failed is not None:
            self.check_point_failed = check_point_failed
        if error is not None:
            self.error = error
        if others_failed is not None:
            self.others_failed = others_failed
        if parsed_failed is not None:
            self.parsed_failed = parsed_failed
        if refused_failed is not None:
            self.refused_failed = refused_failed
        if success is not None:
            self.success = success
        if timeout is not None:
            self.timeout = timeout

    @property
    def check_point_failed(self):
        """Gets the check_point_failed of this RespcodeBrokens.

        checkPointFailed

        :return: The check_point_failed of this RespcodeBrokens.
        :rtype: list[int]
        """
        return self._check_point_failed

    @check_point_failed.setter
    def check_point_failed(self, check_point_failed):
        """Sets the check_point_failed of this RespcodeBrokens.

        checkPointFailed

        :param check_point_failed: The check_point_failed of this RespcodeBrokens.
        :type: list[int]
        """
        self._check_point_failed = check_point_failed

    @property
    def error(self):
        """Gets the error of this RespcodeBrokens.

        error

        :return: The error of this RespcodeBrokens.
        :rtype: list[int]
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this RespcodeBrokens.

        error

        :param error: The error of this RespcodeBrokens.
        :type: list[int]
        """
        self._error = error

    @property
    def others_failed(self):
        """Gets the others_failed of this RespcodeBrokens.

        othersFailed

        :return: The others_failed of this RespcodeBrokens.
        :rtype: list[int]
        """
        return self._others_failed

    @others_failed.setter
    def others_failed(self, others_failed):
        """Sets the others_failed of this RespcodeBrokens.

        othersFailed

        :param others_failed: The others_failed of this RespcodeBrokens.
        :type: list[int]
        """
        self._others_failed = others_failed

    @property
    def parsed_failed(self):
        """Gets the parsed_failed of this RespcodeBrokens.

        parsedFailed

        :return: The parsed_failed of this RespcodeBrokens.
        :rtype: list[int]
        """
        return self._parsed_failed

    @parsed_failed.setter
    def parsed_failed(self, parsed_failed):
        """Sets the parsed_failed of this RespcodeBrokens.

        parsedFailed

        :param parsed_failed: The parsed_failed of this RespcodeBrokens.
        :type: list[int]
        """
        self._parsed_failed = parsed_failed

    @property
    def refused_failed(self):
        """Gets the refused_failed of this RespcodeBrokens.

        refusedFailed

        :return: The refused_failed of this RespcodeBrokens.
        :rtype: list[int]
        """
        return self._refused_failed

    @refused_failed.setter
    def refused_failed(self, refused_failed):
        """Sets the refused_failed of this RespcodeBrokens.

        refusedFailed

        :param refused_failed: The refused_failed of this RespcodeBrokens.
        :type: list[int]
        """
        self._refused_failed = refused_failed

    @property
    def success(self):
        """Gets the success of this RespcodeBrokens.

        success

        :return: The success of this RespcodeBrokens.
        :rtype: list[int]
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this RespcodeBrokens.

        success

        :param success: The success of this RespcodeBrokens.
        :type: list[int]
        """
        self._success = success

    @property
    def timeout(self):
        """Gets the timeout of this RespcodeBrokens.

        timeout

        :return: The timeout of this RespcodeBrokens.
        :rtype: list[int]
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this RespcodeBrokens.

        timeout

        :param timeout: The timeout of this RespcodeBrokens.
        :type: list[int]
        """
        self._timeout = timeout

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
        if not isinstance(other, RespcodeBrokens):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
