# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LdApiScriptCreate:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'api_type': 'str',
        'scripts': 'list[LdApiScriptBase]'
    }

    attribute_map = {
        'api_type': 'api_type',
        'scripts': 'scripts'
    }

    def __init__(self, api_type=None, scripts=None):
        """LdApiScriptCreate

        The model defined in huaweicloud sdk

        :param api_type: API类型 - data：数据API - function：函数API 
        :type api_type: str
        :param scripts: API脚本信息列表
        :type scripts: list[:class:`huaweicloudsdkroma.v2.LdApiScriptBase`]
        """
        
        

        self._api_type = None
        self._scripts = None
        self.discriminator = None

        if api_type is not None:
            self.api_type = api_type
        if scripts is not None:
            self.scripts = scripts

    @property
    def api_type(self):
        """Gets the api_type of this LdApiScriptCreate.

        API类型 - data：数据API - function：函数API 

        :return: The api_type of this LdApiScriptCreate.
        :rtype: str
        """
        return self._api_type

    @api_type.setter
    def api_type(self, api_type):
        """Sets the api_type of this LdApiScriptCreate.

        API类型 - data：数据API - function：函数API 

        :param api_type: The api_type of this LdApiScriptCreate.
        :type api_type: str
        """
        self._api_type = api_type

    @property
    def scripts(self):
        """Gets the scripts of this LdApiScriptCreate.

        API脚本信息列表

        :return: The scripts of this LdApiScriptCreate.
        :rtype: list[:class:`huaweicloudsdkroma.v2.LdApiScriptBase`]
        """
        return self._scripts

    @scripts.setter
    def scripts(self, scripts):
        """Sets the scripts of this LdApiScriptCreate.

        API脚本信息列表

        :param scripts: The scripts of this LdApiScriptCreate.
        :type scripts: list[:class:`huaweicloudsdkroma.v2.LdApiScriptBase`]
        """
        self._scripts = scripts

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
        if not isinstance(other, LdApiScriptCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
