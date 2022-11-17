# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OperateInfoResponseBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'info_code': 'str',
        'info_description': 'str'
    }

    attribute_map = {
        'info_code': 'info_code',
        'info_description': 'info_description'
    }

    def __init__(self, info_code=None, info_description=None):
        """OperateInfoResponseBody

        The model defined in huaweicloud sdk

        :param info_code: 状态码:   * success - 成功   * failure - 失败 
        :type info_code: str
        :param info_description: 返回的提示信息
        :type info_description: str
        """
        
        

        self._info_code = None
        self._info_description = None
        self.discriminator = None

        if info_code is not None:
            self.info_code = info_code
        if info_description is not None:
            self.info_description = info_description

    @property
    def info_code(self):
        """Gets the info_code of this OperateInfoResponseBody.

        状态码:   * success - 成功   * failure - 失败 

        :return: The info_code of this OperateInfoResponseBody.
        :rtype: str
        """
        return self._info_code

    @info_code.setter
    def info_code(self, info_code):
        """Sets the info_code of this OperateInfoResponseBody.

        状态码:   * success - 成功   * failure - 失败 

        :param info_code: The info_code of this OperateInfoResponseBody.
        :type info_code: str
        """
        self._info_code = info_code

    @property
    def info_description(self):
        """Gets the info_description of this OperateInfoResponseBody.

        返回的提示信息

        :return: The info_description of this OperateInfoResponseBody.
        :rtype: str
        """
        return self._info_description

    @info_description.setter
    def info_description(self, info_description):
        """Sets the info_description of this OperateInfoResponseBody.

        返回的提示信息

        :param info_description: The info_description of this OperateInfoResponseBody.
        :type info_description: str
        """
        self._info_description = info_description

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
        if not isinstance(other, OperateInfoResponseBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
