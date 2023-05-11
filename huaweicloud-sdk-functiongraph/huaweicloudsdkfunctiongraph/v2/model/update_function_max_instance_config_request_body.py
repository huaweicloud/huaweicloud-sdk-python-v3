# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateFunctionMaxInstanceConfigRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'max_instance_num': 'int'
    }

    attribute_map = {
        'max_instance_num': 'max_instance_num'
    }

    def __init__(self, max_instance_num=None):
        """UpdateFunctionMaxInstanceConfigRequestBody

        The model defined in huaweicloud sdk

        :param max_instance_num: 最大实例数；-1代表该函数实例数无限制，0代表该函数被禁用
        :type max_instance_num: int
        """
        
        

        self._max_instance_num = None
        self.discriminator = None

        if max_instance_num is not None:
            self.max_instance_num = max_instance_num

    @property
    def max_instance_num(self):
        """Gets the max_instance_num of this UpdateFunctionMaxInstanceConfigRequestBody.

        最大实例数；-1代表该函数实例数无限制，0代表该函数被禁用

        :return: The max_instance_num of this UpdateFunctionMaxInstanceConfigRequestBody.
        :rtype: int
        """
        return self._max_instance_num

    @max_instance_num.setter
    def max_instance_num(self, max_instance_num):
        """Sets the max_instance_num of this UpdateFunctionMaxInstanceConfigRequestBody.

        最大实例数；-1代表该函数实例数无限制，0代表该函数被禁用

        :param max_instance_num: The max_instance_num of this UpdateFunctionMaxInstanceConfigRequestBody.
        :type max_instance_num: int
        """
        self._max_instance_num = max_instance_num

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
        if not isinstance(other, UpdateFunctionMaxInstanceConfigRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
