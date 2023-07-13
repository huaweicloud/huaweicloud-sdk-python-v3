# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MulInputFileInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'language': 'str',
        'input': 'ObsObjInfo'
    }

    attribute_map = {
        'language': 'language',
        'input': 'input'
    }

    def __init__(self, language=None, input=None):
        """MulInputFileInfo

        The model defined in huaweicloud sdk

        :param language: 语言标签。
        :type language: str
        :param input: 
        :type input: :class:`huaweicloudsdkmpc.v1.ObsObjInfo`
        """
        
        

        self._language = None
        self._input = None
        self.discriminator = None

        if language is not None:
            self.language = language
        if input is not None:
            self.input = input

    @property
    def language(self):
        """Gets the language of this MulInputFileInfo.

        语言标签。

        :return: The language of this MulInputFileInfo.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this MulInputFileInfo.

        语言标签。

        :param language: The language of this MulInputFileInfo.
        :type language: str
        """
        self._language = language

    @property
    def input(self):
        """Gets the input of this MulInputFileInfo.

        :return: The input of this MulInputFileInfo.
        :rtype: :class:`huaweicloudsdkmpc.v1.ObsObjInfo`
        """
        return self._input

    @input.setter
    def input(self, input):
        """Sets the input of this MulInputFileInfo.

        :param input: The input of this MulInputFileInfo.
        :type input: :class:`huaweicloudsdkmpc.v1.ObsObjInfo`
        """
        self._input = input

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
        if not isinstance(other, MulInputFileInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
