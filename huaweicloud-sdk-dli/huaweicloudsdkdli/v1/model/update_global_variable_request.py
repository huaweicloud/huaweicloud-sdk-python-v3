# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateGlobalVariableRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'var_name': 'str',
        'body': 'UpdateGlobalValueReq'
    }

    attribute_map = {
        'var_name': 'var_name',
        'body': 'body'
    }

    def __init__(self, var_name=None, body=None):
        """UpdateGlobalVariableRequest

        The model defined in huaweicloud sdk

        :param var_name: 全局变量名，名称只能包含数字、英文字母和下划线，但不能是纯数字，不能以下划线开头，且不能超过128字符
        :type var_name: str
        :param body: Body of the UpdateGlobalVariableRequest
        :type body: :class:`huaweicloudsdkdli.v1.UpdateGlobalValueReq`
        """
        
        

        self._var_name = None
        self._body = None
        self.discriminator = None

        self.var_name = var_name
        if body is not None:
            self.body = body

    @property
    def var_name(self):
        """Gets the var_name of this UpdateGlobalVariableRequest.

        全局变量名，名称只能包含数字、英文字母和下划线，但不能是纯数字，不能以下划线开头，且不能超过128字符

        :return: The var_name of this UpdateGlobalVariableRequest.
        :rtype: str
        """
        return self._var_name

    @var_name.setter
    def var_name(self, var_name):
        """Sets the var_name of this UpdateGlobalVariableRequest.

        全局变量名，名称只能包含数字、英文字母和下划线，但不能是纯数字，不能以下划线开头，且不能超过128字符

        :param var_name: The var_name of this UpdateGlobalVariableRequest.
        :type var_name: str
        """
        self._var_name = var_name

    @property
    def body(self):
        """Gets the body of this UpdateGlobalVariableRequest.

        :return: The body of this UpdateGlobalVariableRequest.
        :rtype: :class:`huaweicloudsdkdli.v1.UpdateGlobalValueReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateGlobalVariableRequest.

        :param body: The body of this UpdateGlobalVariableRequest.
        :type body: :class:`huaweicloudsdkdli.v1.UpdateGlobalValueReq`
        """
        self._body = body

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
        if not isinstance(other, UpdateGlobalVariableRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
