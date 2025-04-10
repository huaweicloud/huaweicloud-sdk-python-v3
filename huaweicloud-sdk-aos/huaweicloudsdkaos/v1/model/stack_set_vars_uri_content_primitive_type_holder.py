# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StackSetVarsURIContentPrimitiveTypeHolder:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vars_uri_content': 'str'
    }

    attribute_map = {
        'vars_uri_content': 'vars_uri_content'
    }

    def __init__(self, vars_uri_content=None):
        r"""StackSetVarsURIContentPrimitiveTypeHolder

        The model defined in huaweicloud sdk

        :param vars_uri_content: vars_uri对应的文件内容
        :type vars_uri_content: str
        """
        
        

        self._vars_uri_content = None
        self.discriminator = None

        if vars_uri_content is not None:
            self.vars_uri_content = vars_uri_content

    @property
    def vars_uri_content(self):
        r"""Gets the vars_uri_content of this StackSetVarsURIContentPrimitiveTypeHolder.

        vars_uri对应的文件内容

        :return: The vars_uri_content of this StackSetVarsURIContentPrimitiveTypeHolder.
        :rtype: str
        """
        return self._vars_uri_content

    @vars_uri_content.setter
    def vars_uri_content(self, vars_uri_content):
        r"""Sets the vars_uri_content of this StackSetVarsURIContentPrimitiveTypeHolder.

        vars_uri对应的文件内容

        :param vars_uri_content: The vars_uri_content of this StackSetVarsURIContentPrimitiveTypeHolder.
        :type vars_uri_content: str
        """
        self._vars_uri_content = vars_uri_content

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
        if not isinstance(other, StackSetVarsURIContentPrimitiveTypeHolder):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
