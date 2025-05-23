# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChangeAgentStatusResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'flag': 'str'
    }

    attribute_map = {
        'flag': 'flag'
    }

    def __init__(self, flag=None):
        r"""ChangeAgentStatusResponse

        The model defined in huaweicloud sdk

        :param flag: 返回结果ok表示成功。
        :type flag: str
        """
        
        super(ChangeAgentStatusResponse, self).__init__()

        self._flag = None
        self.discriminator = None

        if flag is not None:
            self.flag = flag

    @property
    def flag(self):
        r"""Gets the flag of this ChangeAgentStatusResponse.

        返回结果ok表示成功。

        :return: The flag of this ChangeAgentStatusResponse.
        :rtype: str
        """
        return self._flag

    @flag.setter
    def flag(self, flag):
        r"""Sets the flag of this ChangeAgentStatusResponse.

        返回结果ok表示成功。

        :param flag: The flag of this ChangeAgentStatusResponse.
        :type flag: str
        """
        self._flag = flag

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
        if not isinstance(other, ChangeAgentStatusResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
