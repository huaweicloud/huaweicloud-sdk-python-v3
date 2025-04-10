# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CategorySuggestions:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'politics': 'str',
        'terrorism': 'str',
        'porn': 'str'
    }

    attribute_map = {
        'politics': 'politics',
        'terrorism': 'terrorism',
        'porn': 'porn'
    }

    def __init__(self, politics=None, terrorism=None, porn=None):
        r"""CategorySuggestions

        The model defined in huaweicloud sdk

        :param politics: 政治人物审核。
        :type politics: str
        :param terrorism: 暴恐内容审核。
        :type terrorism: str
        :param porn: 情色内容审核。
        :type porn: str
        """
        
        

        self._politics = None
        self._terrorism = None
        self._porn = None
        self.discriminator = None

        if politics is not None:
            self.politics = politics
        if terrorism is not None:
            self.terrorism = terrorism
        if porn is not None:
            self.porn = porn

    @property
    def politics(self):
        r"""Gets the politics of this CategorySuggestions.

        政治人物审核。

        :return: The politics of this CategorySuggestions.
        :rtype: str
        """
        return self._politics

    @politics.setter
    def politics(self, politics):
        r"""Sets the politics of this CategorySuggestions.

        政治人物审核。

        :param politics: The politics of this CategorySuggestions.
        :type politics: str
        """
        self._politics = politics

    @property
    def terrorism(self):
        r"""Gets the terrorism of this CategorySuggestions.

        暴恐内容审核。

        :return: The terrorism of this CategorySuggestions.
        :rtype: str
        """
        return self._terrorism

    @terrorism.setter
    def terrorism(self, terrorism):
        r"""Sets the terrorism of this CategorySuggestions.

        暴恐内容审核。

        :param terrorism: The terrorism of this CategorySuggestions.
        :type terrorism: str
        """
        self._terrorism = terrorism

    @property
    def porn(self):
        r"""Gets the porn of this CategorySuggestions.

        情色内容审核。

        :return: The porn of this CategorySuggestions.
        :rtype: str
        """
        return self._porn

    @porn.setter
    def porn(self, porn):
        r"""Sets the porn of this CategorySuggestions.

        情色内容审核。

        :param porn: The porn of this CategorySuggestions.
        :type porn: str
        """
        self._porn = porn

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
        if not isinstance(other, CategorySuggestions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
