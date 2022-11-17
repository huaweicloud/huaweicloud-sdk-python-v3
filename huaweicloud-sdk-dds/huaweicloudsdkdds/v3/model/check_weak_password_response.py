# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckWeakPasswordResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'weak': 'bool'
    }

    attribute_map = {
        'weak': 'weak'
    }

    def __init__(self, weak=None):
        """CheckWeakPasswordResponse

        The model defined in huaweicloud sdk

        :param weak: 是否弱密码，true:是弱密码 false:不是弱密码
        :type weak: bool
        """
        
        super(CheckWeakPasswordResponse, self).__init__()

        self._weak = None
        self.discriminator = None

        if weak is not None:
            self.weak = weak

    @property
    def weak(self):
        """Gets the weak of this CheckWeakPasswordResponse.

        是否弱密码，true:是弱密码 false:不是弱密码

        :return: The weak of this CheckWeakPasswordResponse.
        :rtype: bool
        """
        return self._weak

    @weak.setter
    def weak(self, weak):
        """Sets the weak of this CheckWeakPasswordResponse.

        是否弱密码，true:是弱密码 false:不是弱密码

        :param weak: The weak of this CheckWeakPasswordResponse.
        :type weak: bool
        """
        self._weak = weak

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
        if not isinstance(other, CheckWeakPasswordResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
