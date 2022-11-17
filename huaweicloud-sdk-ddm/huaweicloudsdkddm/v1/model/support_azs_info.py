# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SupportAzsInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'code': 'str',
        'name': 'str',
        'favored': 'bool'
    }

    attribute_map = {
        'code': 'code',
        'name': 'name',
        'favored': 'favored'
    }

    def __init__(self, code=None, name=None, favored=None):
        """SupportAzsInfo

        The model defined in huaweicloud sdk

        :param code: 可用区编码。
        :type code: str
        :param name: 可用区名称。
        :type name: str
        :param favored: 是否支持。
        :type favored: bool
        """
        
        

        self._code = None
        self._name = None
        self._favored = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if name is not None:
            self.name = name
        if favored is not None:
            self.favored = favored

    @property
    def code(self):
        """Gets the code of this SupportAzsInfo.

        可用区编码。

        :return: The code of this SupportAzsInfo.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this SupportAzsInfo.

        可用区编码。

        :param code: The code of this SupportAzsInfo.
        :type code: str
        """
        self._code = code

    @property
    def name(self):
        """Gets the name of this SupportAzsInfo.

        可用区名称。

        :return: The name of this SupportAzsInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SupportAzsInfo.

        可用区名称。

        :param name: The name of this SupportAzsInfo.
        :type name: str
        """
        self._name = name

    @property
    def favored(self):
        """Gets the favored of this SupportAzsInfo.

        是否支持。

        :return: The favored of this SupportAzsInfo.
        :rtype: bool
        """
        return self._favored

    @favored.setter
    def favored(self, favored):
        """Sets the favored of this SupportAzsInfo.

        是否支持。

        :param favored: The favored of this SupportAzsInfo.
        :type favored: bool
        """
        self._favored = favored

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
        if not isinstance(other, SupportAzsInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
