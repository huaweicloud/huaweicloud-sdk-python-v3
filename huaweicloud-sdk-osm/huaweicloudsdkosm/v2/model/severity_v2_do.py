# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SeverityV2Do:

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
        'severity_name': 'str',
        'severity_id': 'str'
    }

    attribute_map = {
        'language': 'language',
        'severity_name': 'severity_name',
        'severity_id': 'severity_id'
    }

    def __init__(self, language=None, severity_name=None, severity_id=None):
        """SeverityV2Do

        The model defined in huaweicloud sdk

        :param language: 语言
        :type language: str
        :param severity_name: 严重性名称
        :type severity_name: str
        :param severity_id: 严重性id
        :type severity_id: str
        """
        
        

        self._language = None
        self._severity_name = None
        self._severity_id = None
        self.discriminator = None

        if language is not None:
            self.language = language
        if severity_name is not None:
            self.severity_name = severity_name
        if severity_id is not None:
            self.severity_id = severity_id

    @property
    def language(self):
        """Gets the language of this SeverityV2Do.

        语言

        :return: The language of this SeverityV2Do.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this SeverityV2Do.

        语言

        :param language: The language of this SeverityV2Do.
        :type language: str
        """
        self._language = language

    @property
    def severity_name(self):
        """Gets the severity_name of this SeverityV2Do.

        严重性名称

        :return: The severity_name of this SeverityV2Do.
        :rtype: str
        """
        return self._severity_name

    @severity_name.setter
    def severity_name(self, severity_name):
        """Sets the severity_name of this SeverityV2Do.

        严重性名称

        :param severity_name: The severity_name of this SeverityV2Do.
        :type severity_name: str
        """
        self._severity_name = severity_name

    @property
    def severity_id(self):
        """Gets the severity_id of this SeverityV2Do.

        严重性id

        :return: The severity_id of this SeverityV2Do.
        :rtype: str
        """
        return self._severity_id

    @severity_id.setter
    def severity_id(self, severity_id):
        """Sets the severity_id of this SeverityV2Do.

        严重性id

        :param severity_id: The severity_id of this SeverityV2Do.
        :type severity_id: str
        """
        self._severity_id = severity_id

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
        if not isinstance(other, SeverityV2Do):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
