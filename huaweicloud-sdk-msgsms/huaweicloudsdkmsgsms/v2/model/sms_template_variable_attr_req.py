# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SmsTemplateVariableAttrReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'variable_desc': 'str',
        'variable_index': 'int',
        'variable_type': 'str'
    }

    attribute_map = {
        'variable_desc': 'variable_desc',
        'variable_index': 'variable_index',
        'variable_type': 'variable_type'
    }

    def __init__(self, variable_desc=None, variable_index=None, variable_type=None):
        r"""SmsTemplateVariableAttrReq

        The model defined in huaweicloud sdk

        :param variable_desc: 变量说明，当变量类型为TEXT时，必填
        :type variable_desc: str
        :param variable_index: 变量索引，对应模板内容变量索引
        :type variable_index: int
        :param variable_type: 变量类型，目前支持：PHONE|CHARDIGIT|DATETIME|MONEY|TEXT|NEWTEXT|LONGTEXT
        :type variable_type: str
        """
        
        

        self._variable_desc = None
        self._variable_index = None
        self._variable_type = None
        self.discriminator = None

        if variable_desc is not None:
            self.variable_desc = variable_desc
        self.variable_index = variable_index
        self.variable_type = variable_type

    @property
    def variable_desc(self):
        r"""Gets the variable_desc of this SmsTemplateVariableAttrReq.

        变量说明，当变量类型为TEXT时，必填

        :return: The variable_desc of this SmsTemplateVariableAttrReq.
        :rtype: str
        """
        return self._variable_desc

    @variable_desc.setter
    def variable_desc(self, variable_desc):
        r"""Sets the variable_desc of this SmsTemplateVariableAttrReq.

        变量说明，当变量类型为TEXT时，必填

        :param variable_desc: The variable_desc of this SmsTemplateVariableAttrReq.
        :type variable_desc: str
        """
        self._variable_desc = variable_desc

    @property
    def variable_index(self):
        r"""Gets the variable_index of this SmsTemplateVariableAttrReq.

        变量索引，对应模板内容变量索引

        :return: The variable_index of this SmsTemplateVariableAttrReq.
        :rtype: int
        """
        return self._variable_index

    @variable_index.setter
    def variable_index(self, variable_index):
        r"""Sets the variable_index of this SmsTemplateVariableAttrReq.

        变量索引，对应模板内容变量索引

        :param variable_index: The variable_index of this SmsTemplateVariableAttrReq.
        :type variable_index: int
        """
        self._variable_index = variable_index

    @property
    def variable_type(self):
        r"""Gets the variable_type of this SmsTemplateVariableAttrReq.

        变量类型，目前支持：PHONE|CHARDIGIT|DATETIME|MONEY|TEXT|NEWTEXT|LONGTEXT

        :return: The variable_type of this SmsTemplateVariableAttrReq.
        :rtype: str
        """
        return self._variable_type

    @variable_type.setter
    def variable_type(self, variable_type):
        r"""Sets the variable_type of this SmsTemplateVariableAttrReq.

        变量类型，目前支持：PHONE|CHARDIGIT|DATETIME|MONEY|TEXT|NEWTEXT|LONGTEXT

        :param variable_type: The variable_type of this SmsTemplateVariableAttrReq.
        :type variable_type: str
        """
        self._variable_type = variable_type

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
        if not isinstance(other, SmsTemplateVariableAttrReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
