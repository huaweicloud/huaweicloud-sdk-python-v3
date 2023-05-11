# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResizeInstanceOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'target_spec_code': 'str'
    }

    attribute_map = {
        'target_spec_code': 'target_spec_code'
    }

    def __init__(self, target_spec_code=None):
        """ResizeInstanceOption

        The model defined in huaweicloud sdk

        :param target_spec_code: 变更至新规格的资源规格编码。获取方法请参见查询数据库规格中响应参数“flavors.spec_code”的值。
        :type target_spec_code: str
        """
        
        

        self._target_spec_code = None
        self.discriminator = None

        self.target_spec_code = target_spec_code

    @property
    def target_spec_code(self):
        """Gets the target_spec_code of this ResizeInstanceOption.

        变更至新规格的资源规格编码。获取方法请参见查询数据库规格中响应参数“flavors.spec_code”的值。

        :return: The target_spec_code of this ResizeInstanceOption.
        :rtype: str
        """
        return self._target_spec_code

    @target_spec_code.setter
    def target_spec_code(self, target_spec_code):
        """Sets the target_spec_code of this ResizeInstanceOption.

        变更至新规格的资源规格编码。获取方法请参见查询数据库规格中响应参数“flavors.spec_code”的值。

        :param target_spec_code: The target_spec_code of this ResizeInstanceOption.
        :type target_spec_code: str
        """
        self._target_spec_code = target_spec_code

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
        if not isinstance(other, ResizeInstanceOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
