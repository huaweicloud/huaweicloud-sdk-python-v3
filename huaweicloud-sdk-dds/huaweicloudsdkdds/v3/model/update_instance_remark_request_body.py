# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateInstanceRemarkRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'remark': 'str'
    }

    attribute_map = {
        'remark': 'remark'
    }

    def __init__(self, remark=None):
        """UpdateInstanceRemarkRequestBody

        The model defined in huaweicloud sdk

        :param remark: 实例备注内容。 长度不能超过64位，不支持回车和&gt;!&lt;\&quot;&amp;&#39;&#x3D;特殊字符。
        :type remark: str
        """
        
        

        self._remark = None
        self.discriminator = None

        self.remark = remark

    @property
    def remark(self):
        """Gets the remark of this UpdateInstanceRemarkRequestBody.

        实例备注内容。 长度不能超过64位，不支持回车和>!<\"&'=特殊字符。

        :return: The remark of this UpdateInstanceRemarkRequestBody.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        """Sets the remark of this UpdateInstanceRemarkRequestBody.

        实例备注内容。 长度不能超过64位，不支持回车和>!<\"&'=特殊字符。

        :param remark: The remark of this UpdateInstanceRemarkRequestBody.
        :type remark: str
        """
        self._remark = remark

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
        if not isinstance(other, UpdateInstanceRemarkRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
