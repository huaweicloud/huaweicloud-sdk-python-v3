# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateFactoryJobNameResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_success': 'bool',
        'status_code': 'int'
    }

    attribute_map = {
        'is_success': 'is_success',
        'status_code': 'status_code'
    }

    def __init__(self, is_success=None, status_code=None):
        r"""UpdateFactoryJobNameResponse

        The model defined in huaweicloud sdk

        :param is_success: 取值为true或者false
        :type is_success: bool
        :param status_code: 200表示成功返回
        :type status_code: int
        """
        
        super(UpdateFactoryJobNameResponse, self).__init__()

        self._is_success = None
        self._status_code = None
        self.discriminator = None

        if is_success is not None:
            self.is_success = is_success
        if status_code is not None:
            self.status_code = status_code

    @property
    def is_success(self):
        r"""Gets the is_success of this UpdateFactoryJobNameResponse.

        取值为true或者false

        :return: The is_success of this UpdateFactoryJobNameResponse.
        :rtype: bool
        """
        return self._is_success

    @is_success.setter
    def is_success(self, is_success):
        r"""Sets the is_success of this UpdateFactoryJobNameResponse.

        取值为true或者false

        :param is_success: The is_success of this UpdateFactoryJobNameResponse.
        :type is_success: bool
        """
        self._is_success = is_success

    @property
    def status_code(self):
        r"""Gets the status_code of this UpdateFactoryJobNameResponse.

        200表示成功返回

        :return: The status_code of this UpdateFactoryJobNameResponse.
        :rtype: int
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        r"""Sets the status_code of this UpdateFactoryJobNameResponse.

        200表示成功返回

        :param status_code: The status_code of this UpdateFactoryJobNameResponse.
        :type status_code: int
        """
        self._status_code = status_code

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
        if not isinstance(other, UpdateFactoryJobNameResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
