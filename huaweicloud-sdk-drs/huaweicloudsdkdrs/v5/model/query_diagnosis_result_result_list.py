# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryDiagnosisResultResultList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'key': 'str',
        'value': 'str',
        'is_multi_language': 'bool',
        'module_name': 'str',
        'level': 'str'
    }

    attribute_map = {
        'key': 'key',
        'value': 'value',
        'is_multi_language': 'is_multi_language',
        'module_name': 'module_name',
        'level': 'level'
    }

    def __init__(self, key=None, value=None, is_multi_language=None, module_name=None, level=None):
        r"""QueryDiagnosisResultResultList

        The model defined in huaweicloud sdk

        :param key: 内容key。
        :type key: str
        :param value: 结果值。
        :type value: str
        :param is_multi_language: 结果值是否需要国际化。
        :type is_multi_language: bool
        :param module_name: 模块名称。
        :type module_name: str
        :param level: 等级。
        :type level: str
        """
        
        

        self._key = None
        self._value = None
        self._is_multi_language = None
        self._module_name = None
        self._level = None
        self.discriminator = None

        if key is not None:
            self.key = key
        if value is not None:
            self.value = value
        if is_multi_language is not None:
            self.is_multi_language = is_multi_language
        if module_name is not None:
            self.module_name = module_name
        if level is not None:
            self.level = level

    @property
    def key(self):
        r"""Gets the key of this QueryDiagnosisResultResultList.

        内容key。

        :return: The key of this QueryDiagnosisResultResultList.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        r"""Sets the key of this QueryDiagnosisResultResultList.

        内容key。

        :param key: The key of this QueryDiagnosisResultResultList.
        :type key: str
        """
        self._key = key

    @property
    def value(self):
        r"""Gets the value of this QueryDiagnosisResultResultList.

        结果值。

        :return: The value of this QueryDiagnosisResultResultList.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this QueryDiagnosisResultResultList.

        结果值。

        :param value: The value of this QueryDiagnosisResultResultList.
        :type value: str
        """
        self._value = value

    @property
    def is_multi_language(self):
        r"""Gets the is_multi_language of this QueryDiagnosisResultResultList.

        结果值是否需要国际化。

        :return: The is_multi_language of this QueryDiagnosisResultResultList.
        :rtype: bool
        """
        return self._is_multi_language

    @is_multi_language.setter
    def is_multi_language(self, is_multi_language):
        r"""Sets the is_multi_language of this QueryDiagnosisResultResultList.

        结果值是否需要国际化。

        :param is_multi_language: The is_multi_language of this QueryDiagnosisResultResultList.
        :type is_multi_language: bool
        """
        self._is_multi_language = is_multi_language

    @property
    def module_name(self):
        r"""Gets the module_name of this QueryDiagnosisResultResultList.

        模块名称。

        :return: The module_name of this QueryDiagnosisResultResultList.
        :rtype: str
        """
        return self._module_name

    @module_name.setter
    def module_name(self, module_name):
        r"""Sets the module_name of this QueryDiagnosisResultResultList.

        模块名称。

        :param module_name: The module_name of this QueryDiagnosisResultResultList.
        :type module_name: str
        """
        self._module_name = module_name

    @property
    def level(self):
        r"""Gets the level of this QueryDiagnosisResultResultList.

        等级。

        :return: The level of this QueryDiagnosisResultResultList.
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        r"""Sets the level of this QueryDiagnosisResultResultList.

        等级。

        :param level: The level of this QueryDiagnosisResultResultList.
        :type level: str
        """
        self._level = level

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
        if not isinstance(other, QueryDiagnosisResultResultList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
