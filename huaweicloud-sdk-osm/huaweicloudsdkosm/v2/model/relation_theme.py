# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RelationTheme:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'theme_name': 'str',
        'relation_type': 'str'
    }

    attribute_map = {
        'theme_name': 'theme_name',
        'relation_type': 'relation_type'
    }

    def __init__(self, theme_name=None, relation_type=None):
        """RelationTheme

        The model defined in huaweicloud sdk

        :param theme_name: 主题
        :type theme_name: str
        :param relation_type: - NON_PRIMARY: 主主题 - PRIMARY:  
        :type relation_type: str
        """
        
        

        self._theme_name = None
        self._relation_type = None
        self.discriminator = None

        if theme_name is not None:
            self.theme_name = theme_name
        if relation_type is not None:
            self.relation_type = relation_type

    @property
    def theme_name(self):
        """Gets the theme_name of this RelationTheme.

        主题

        :return: The theme_name of this RelationTheme.
        :rtype: str
        """
        return self._theme_name

    @theme_name.setter
    def theme_name(self, theme_name):
        """Sets the theme_name of this RelationTheme.

        主题

        :param theme_name: The theme_name of this RelationTheme.
        :type theme_name: str
        """
        self._theme_name = theme_name

    @property
    def relation_type(self):
        """Gets the relation_type of this RelationTheme.

        - NON_PRIMARY: 主主题 - PRIMARY:  

        :return: The relation_type of this RelationTheme.
        :rtype: str
        """
        return self._relation_type

    @relation_type.setter
    def relation_type(self, relation_type):
        """Sets the relation_type of this RelationTheme.

        - NON_PRIMARY: 主主题 - PRIMARY:  

        :param relation_type: The relation_type of this RelationTheme.
        :type relation_type: str
        """
        self._relation_type = relation_type

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
        if not isinstance(other, RelationTheme):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
