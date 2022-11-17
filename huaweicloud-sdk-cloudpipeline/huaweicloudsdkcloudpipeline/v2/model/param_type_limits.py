# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ParamTypeLimits:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'disable': 'str',
        'name': 'str',
        'displayname': 'str',
        'id': 'str',
        'language': 'str'
    }

    attribute_map = {
        'disable': 'disable',
        'name': 'name',
        'displayname': 'displayname',
        'id': 'id',
        'language': 'language'
    }

    def __init__(self, disable=None, name=None, displayname=None, id=None, language=None):
        """ParamTypeLimits

        The model defined in huaweicloud sdk

        :param disable: 是否废弃
        :type disable: str
        :param name: 语言名字
        :type name: str
        :param displayname: 语言展示名字
        :type displayname: str
        :param id: 规则集ID
        :type id: str
        :param language: 扫描语言
        :type language: str
        """
        
        

        self._disable = None
        self._name = None
        self._displayname = None
        self._id = None
        self._language = None
        self.discriminator = None

        self.disable = disable
        self.name = name
        self.displayname = displayname
        self.id = id
        self.language = language

    @property
    def disable(self):
        """Gets the disable of this ParamTypeLimits.

        是否废弃

        :return: The disable of this ParamTypeLimits.
        :rtype: str
        """
        return self._disable

    @disable.setter
    def disable(self, disable):
        """Sets the disable of this ParamTypeLimits.

        是否废弃

        :param disable: The disable of this ParamTypeLimits.
        :type disable: str
        """
        self._disable = disable

    @property
    def name(self):
        """Gets the name of this ParamTypeLimits.

        语言名字

        :return: The name of this ParamTypeLimits.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ParamTypeLimits.

        语言名字

        :param name: The name of this ParamTypeLimits.
        :type name: str
        """
        self._name = name

    @property
    def displayname(self):
        """Gets the displayname of this ParamTypeLimits.

        语言展示名字

        :return: The displayname of this ParamTypeLimits.
        :rtype: str
        """
        return self._displayname

    @displayname.setter
    def displayname(self, displayname):
        """Sets the displayname of this ParamTypeLimits.

        语言展示名字

        :param displayname: The displayname of this ParamTypeLimits.
        :type displayname: str
        """
        self._displayname = displayname

    @property
    def id(self):
        """Gets the id of this ParamTypeLimits.

        规则集ID

        :return: The id of this ParamTypeLimits.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ParamTypeLimits.

        规则集ID

        :param id: The id of this ParamTypeLimits.
        :type id: str
        """
        self._id = id

    @property
    def language(self):
        """Gets the language of this ParamTypeLimits.

        扫描语言

        :return: The language of this ParamTypeLimits.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this ParamTypeLimits.

        扫描语言

        :param language: The language of this ParamTypeLimits.
        :type language: str
        """
        self._language = language

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
        if not isinstance(other, ParamTypeLimits):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
