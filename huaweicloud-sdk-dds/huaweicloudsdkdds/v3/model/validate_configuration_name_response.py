# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ValidateConfigurationNameResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_existed': 'bool'
    }

    attribute_map = {
        'is_existed': 'is_existed'
    }

    def __init__(self, is_existed=None):
        r"""ValidateConfigurationNameResponse

        The model defined in huaweicloud sdk

        :param is_existed: 参数组名称是否存在。 - true：参数组名称存在 - false：参数组名称不存在
        :type is_existed: bool
        """
        
        super(ValidateConfigurationNameResponse, self).__init__()

        self._is_existed = None
        self.discriminator = None

        if is_existed is not None:
            self.is_existed = is_existed

    @property
    def is_existed(self):
        r"""Gets the is_existed of this ValidateConfigurationNameResponse.

        参数组名称是否存在。 - true：参数组名称存在 - false：参数组名称不存在

        :return: The is_existed of this ValidateConfigurationNameResponse.
        :rtype: bool
        """
        return self._is_existed

    @is_existed.setter
    def is_existed(self, is_existed):
        r"""Sets the is_existed of this ValidateConfigurationNameResponse.

        参数组名称是否存在。 - true：参数组名称存在 - false：参数组名称不存在

        :param is_existed: The is_existed of this ValidateConfigurationNameResponse.
        :type is_existed: bool
        """
        self._is_existed = is_existed

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
        if not isinstance(other, ValidateConfigurationNameResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
