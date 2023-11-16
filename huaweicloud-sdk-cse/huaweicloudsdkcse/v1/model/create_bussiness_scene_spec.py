# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateBussinessSceneSpec:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'alias': 'str',
        'matches': 'list[CreateBussinessSceneSpecMatches]'
    }

    attribute_map = {
        'alias': 'alias',
        'matches': 'matches'
    }

    def __init__(self, alias=None, matches=None):
        """CreateBussinessSceneSpec

        The model defined in huaweicloud sdk

        :param alias: 特征名称
        :type alias: str
        :param matches: 匹配条件定义
        :type matches: list[:class:`huaweicloudsdkcse.v1.CreateBussinessSceneSpecMatches`]
        """
        
        

        self._alias = None
        self._matches = None
        self.discriminator = None

        if alias is not None:
            self.alias = alias
        if matches is not None:
            self.matches = matches

    @property
    def alias(self):
        """Gets the alias of this CreateBussinessSceneSpec.

        特征名称

        :return: The alias of this CreateBussinessSceneSpec.
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this CreateBussinessSceneSpec.

        特征名称

        :param alias: The alias of this CreateBussinessSceneSpec.
        :type alias: str
        """
        self._alias = alias

    @property
    def matches(self):
        """Gets the matches of this CreateBussinessSceneSpec.

        匹配条件定义

        :return: The matches of this CreateBussinessSceneSpec.
        :rtype: list[:class:`huaweicloudsdkcse.v1.CreateBussinessSceneSpecMatches`]
        """
        return self._matches

    @matches.setter
    def matches(self, matches):
        """Sets the matches of this CreateBussinessSceneSpec.

        匹配条件定义

        :param matches: The matches of this CreateBussinessSceneSpec.
        :type matches: list[:class:`huaweicloudsdkcse.v1.CreateBussinessSceneSpecMatches`]
        """
        self._matches = matches

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
        if not isinstance(other, CreateBussinessSceneSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
