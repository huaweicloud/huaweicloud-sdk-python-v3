# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListStorageTypesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'x_language': 'str',
        'version': 'str',
        'ha_mode': 'str'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'version': 'version',
        'ha_mode': 'ha_mode'
    }

    def __init__(self, x_language=None, version=None, ha_mode=None):
        """ListStorageTypesRequest

        The model defined in huaweicloud sdk

        :param x_language: 语言
        :type x_language: str
        :param version: 数据库版本号。
        :type version: str
        :param ha_mode: 实例类型： enterprise(企业版)， centralization_standard(主备版)，不区分大小写。
        :type ha_mode: str
        """
        
        

        self._x_language = None
        self._version = None
        self._ha_mode = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        self.version = version
        if ha_mode is not None:
            self.ha_mode = ha_mode

    @property
    def x_language(self):
        """Gets the x_language of this ListStorageTypesRequest.

        语言

        :return: The x_language of this ListStorageTypesRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this ListStorageTypesRequest.

        语言

        :param x_language: The x_language of this ListStorageTypesRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def version(self):
        """Gets the version of this ListStorageTypesRequest.

        数据库版本号。

        :return: The version of this ListStorageTypesRequest.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ListStorageTypesRequest.

        数据库版本号。

        :param version: The version of this ListStorageTypesRequest.
        :type version: str
        """
        self._version = version

    @property
    def ha_mode(self):
        """Gets the ha_mode of this ListStorageTypesRequest.

        实例类型： enterprise(企业版)， centralization_standard(主备版)，不区分大小写。

        :return: The ha_mode of this ListStorageTypesRequest.
        :rtype: str
        """
        return self._ha_mode

    @ha_mode.setter
    def ha_mode(self, ha_mode):
        """Sets the ha_mode of this ListStorageTypesRequest.

        实例类型： enterprise(企业版)， centralization_standard(主备版)，不区分大小写。

        :param ha_mode: The ha_mode of this ListStorageTypesRequest.
        :type ha_mode: str
        """
        self._ha_mode = ha_mode

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
        if not isinstance(other, ListStorageTypesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
