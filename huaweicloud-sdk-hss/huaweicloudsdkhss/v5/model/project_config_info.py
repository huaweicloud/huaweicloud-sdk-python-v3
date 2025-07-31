# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProjectConfigInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'config_name': 'str',
        'config_value': 'str'
    }

    attribute_map = {
        'config_name': 'config_name',
        'config_value': 'config_value'
    }

    def __init__(self, config_name=None, config_value=None):
        r"""ProjectConfigInfo

        The model defined in huaweicloud sdk

        :param config_name: 配置名称，包含如下    - password_min_len ：密码最小长度    - password_digit_min_num ：密码中最少包含数字数量    - password_upper_letter_min_num ：密码中最少包含大写字母数量    - password_lower_letter_min_num ：密码中最少包含小写字母数量    - password_special_char_min_num ：密码中最少包含特殊字符数量    - weakpwd: 自定义弱口令策略
        :type config_name: str
        :param config_value: 配置内容
        :type config_value: str
        """
        
        

        self._config_name = None
        self._config_value = None
        self.discriminator = None

        if config_name is not None:
            self.config_name = config_name
        if config_value is not None:
            self.config_value = config_value

    @property
    def config_name(self):
        r"""Gets the config_name of this ProjectConfigInfo.

        配置名称，包含如下    - password_min_len ：密码最小长度    - password_digit_min_num ：密码中最少包含数字数量    - password_upper_letter_min_num ：密码中最少包含大写字母数量    - password_lower_letter_min_num ：密码中最少包含小写字母数量    - password_special_char_min_num ：密码中最少包含特殊字符数量    - weakpwd: 自定义弱口令策略

        :return: The config_name of this ProjectConfigInfo.
        :rtype: str
        """
        return self._config_name

    @config_name.setter
    def config_name(self, config_name):
        r"""Sets the config_name of this ProjectConfigInfo.

        配置名称，包含如下    - password_min_len ：密码最小长度    - password_digit_min_num ：密码中最少包含数字数量    - password_upper_letter_min_num ：密码中最少包含大写字母数量    - password_lower_letter_min_num ：密码中最少包含小写字母数量    - password_special_char_min_num ：密码中最少包含特殊字符数量    - weakpwd: 自定义弱口令策略

        :param config_name: The config_name of this ProjectConfigInfo.
        :type config_name: str
        """
        self._config_name = config_name

    @property
    def config_value(self):
        r"""Gets the config_value of this ProjectConfigInfo.

        配置内容

        :return: The config_value of this ProjectConfigInfo.
        :rtype: str
        """
        return self._config_value

    @config_value.setter
    def config_value(self, config_value):
        r"""Sets the config_value of this ProjectConfigInfo.

        配置内容

        :param config_value: The config_value of this ProjectConfigInfo.
        :type config_value: str
        """
        self._config_value = config_value

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
        if not isinstance(other, ProjectConfigInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
