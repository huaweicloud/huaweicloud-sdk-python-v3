# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAllConfigItemByTypeRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'config_type': 'str',
        'types': 'list[str]'
    }

    attribute_map = {
        'config_type': 'configType',
        'types': 'types'
    }

    def __init__(self, config_type=None, types=None):
        """ListAllConfigItemByTypeRequestBody

        The model defined in huaweicloud sdk

        :param config_type: 系统配置，服务自己配置{system、service}
        :type config_type: str
        :param types: 配置类型集合
        :type types: list[str]
        """
        
        

        self._config_type = None
        self._types = None
        self.discriminator = None

        if config_type is not None:
            self.config_type = config_type
        if types is not None:
            self.types = types

    @property
    def config_type(self):
        """Gets the config_type of this ListAllConfigItemByTypeRequestBody.

        系统配置，服务自己配置{system、service}

        :return: The config_type of this ListAllConfigItemByTypeRequestBody.
        :rtype: str
        """
        return self._config_type

    @config_type.setter
    def config_type(self, config_type):
        """Sets the config_type of this ListAllConfigItemByTypeRequestBody.

        系统配置，服务自己配置{system、service}

        :param config_type: The config_type of this ListAllConfigItemByTypeRequestBody.
        :type config_type: str
        """
        self._config_type = config_type

    @property
    def types(self):
        """Gets the types of this ListAllConfigItemByTypeRequestBody.

        配置类型集合

        :return: The types of this ListAllConfigItemByTypeRequestBody.
        :rtype: list[str]
        """
        return self._types

    @types.setter
    def types(self, types):
        """Sets the types of this ListAllConfigItemByTypeRequestBody.

        配置类型集合

        :param types: The types of this ListAllConfigItemByTypeRequestBody.
        :type types: list[str]
        """
        self._types = types

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
        if not isinstance(other, ListAllConfigItemByTypeRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
