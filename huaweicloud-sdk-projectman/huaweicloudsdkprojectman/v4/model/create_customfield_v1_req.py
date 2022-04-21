# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateCustomfieldV1Req:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'type': 'str',
        'options': 'str',
        'memo': 'str',
        'scrum_type': 'str'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'options': 'options',
        'memo': 'memo',
        'scrum_type': 'scrum_type'
    }

    def __init__(self, name=None, type=None, options=None, memo=None, scrum_type=None):
        """CreateCustomfieldV1Req

        The model defined in huaweicloud sdk

        :param name: 字段名称
        :type name: str
        :param type: 自定义字段类型 可选类型  textArea|select|radio|text|checkbox|date|time_date|number
        :type type: str
        :param options: 字段选项
        :type options: str
        :param memo: 描述
        :type memo: str
        :param scrum_type: 工作项类型
        :type scrum_type: str
        """
        
        

        self._name = None
        self._type = None
        self._options = None
        self._memo = None
        self._scrum_type = None
        self.discriminator = None

        self.name = name
        self.type = type
        self.options = options
        self.memo = memo
        self.scrum_type = scrum_type

    @property
    def name(self):
        """Gets the name of this CreateCustomfieldV1Req.

        字段名称

        :return: The name of this CreateCustomfieldV1Req.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateCustomfieldV1Req.

        字段名称

        :param name: The name of this CreateCustomfieldV1Req.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        """Gets the type of this CreateCustomfieldV1Req.

        自定义字段类型 可选类型  textArea|select|radio|text|checkbox|date|time_date|number

        :return: The type of this CreateCustomfieldV1Req.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreateCustomfieldV1Req.

        自定义字段类型 可选类型  textArea|select|radio|text|checkbox|date|time_date|number

        :param type: The type of this CreateCustomfieldV1Req.
        :type type: str
        """
        self._type = type

    @property
    def options(self):
        """Gets the options of this CreateCustomfieldV1Req.

        字段选项

        :return: The options of this CreateCustomfieldV1Req.
        :rtype: str
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this CreateCustomfieldV1Req.

        字段选项

        :param options: The options of this CreateCustomfieldV1Req.
        :type options: str
        """
        self._options = options

    @property
    def memo(self):
        """Gets the memo of this CreateCustomfieldV1Req.

        描述

        :return: The memo of this CreateCustomfieldV1Req.
        :rtype: str
        """
        return self._memo

    @memo.setter
    def memo(self, memo):
        """Sets the memo of this CreateCustomfieldV1Req.

        描述

        :param memo: The memo of this CreateCustomfieldV1Req.
        :type memo: str
        """
        self._memo = memo

    @property
    def scrum_type(self):
        """Gets the scrum_type of this CreateCustomfieldV1Req.

        工作项类型

        :return: The scrum_type of this CreateCustomfieldV1Req.
        :rtype: str
        """
        return self._scrum_type

    @scrum_type.setter
    def scrum_type(self, scrum_type):
        """Sets the scrum_type of this CreateCustomfieldV1Req.

        工作项类型

        :param scrum_type: The scrum_type of this CreateCustomfieldV1Req.
        :type scrum_type: str
        """
        self._scrum_type = scrum_type

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
        if not isinstance(other, CreateCustomfieldV1Req):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
