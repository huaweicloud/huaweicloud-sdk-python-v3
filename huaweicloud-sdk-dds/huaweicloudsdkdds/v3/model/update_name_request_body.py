# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateNameRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'new_instance_name': 'str'
    }

    attribute_map = {
        'new_instance_name': 'new_instance_name'
    }

    def __init__(self, new_instance_name=None):
        """UpdateNameRequestBody

        The model defined in huaweicloud sdk

        :param new_instance_name: 新实例名称。用于表示实例的名称，允许和已有名称重复。取值范围：长度为4~64位，必须以字母开头（A~Z或a~z），区分大小写，可以包含字母、数字（0~9）、中划线（-）或者下划线（_），不能包含其他特殊字符。
        :type new_instance_name: str
        """
        
        

        self._new_instance_name = None
        self.discriminator = None

        self.new_instance_name = new_instance_name

    @property
    def new_instance_name(self):
        """Gets the new_instance_name of this UpdateNameRequestBody.

        新实例名称。用于表示实例的名称，允许和已有名称重复。取值范围：长度为4~64位，必须以字母开头（A~Z或a~z），区分大小写，可以包含字母、数字（0~9）、中划线（-）或者下划线（_），不能包含其他特殊字符。

        :return: The new_instance_name of this UpdateNameRequestBody.
        :rtype: str
        """
        return self._new_instance_name

    @new_instance_name.setter
    def new_instance_name(self, new_instance_name):
        """Sets the new_instance_name of this UpdateNameRequestBody.

        新实例名称。用于表示实例的名称，允许和已有名称重复。取值范围：长度为4~64位，必须以字母开头（A~Z或a~z），区分大小写，可以包含字母、数字（0~9）、中划线（-）或者下划线（_），不能包含其他特殊字符。

        :param new_instance_name: The new_instance_name of this UpdateNameRequestBody.
        :type new_instance_name: str
        """
        self._new_instance_name = new_instance_name

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
        if not isinstance(other, UpdateNameRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
