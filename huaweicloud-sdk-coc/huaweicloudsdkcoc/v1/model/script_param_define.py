# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ScriptParamDefine:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'param_name': 'str',
        'param_value': 'str',
        'param_description': 'str',
        'param_order': 'int',
        'sensitive': 'bool'
    }

    attribute_map = {
        'param_name': 'param_name',
        'param_value': 'param_value',
        'param_description': 'param_description',
        'param_order': 'param_order',
        'sensitive': 'sensitive'
    }

    def __init__(self, param_name=None, param_value=None, param_description=None, param_order=None, sensitive=None):
        r"""ScriptParamDefine

        The model defined in huaweicloud sdk

        :param param_name: 参数名仅支持字母、数字以及下划线
        :type param_name: str
        :param param_value: 1.参数长度为1-4096位 2.可以包含大写字母、小写字母、数字及特殊字符(_-/.* ?:\&quot;,&#x3D;+@#\\[{]}) 3.禁止出现连续&#39;.&#39;
        :type param_value: str
        :param param_description: 参数描述
        :type param_description: str
        :param param_order: 该参数已废弃，传入该参数不会生效。
        :type param_order: int
        :param sensitive: 是否是敏感参数
        :type sensitive: bool
        """
        
        

        self._param_name = None
        self._param_value = None
        self._param_description = None
        self._param_order = None
        self._sensitive = None
        self.discriminator = None

        self.param_name = param_name
        self.param_value = param_value
        self.param_description = param_description
        self.param_order = param_order
        self.sensitive = sensitive

    @property
    def param_name(self):
        r"""Gets the param_name of this ScriptParamDefine.

        参数名仅支持字母、数字以及下划线

        :return: The param_name of this ScriptParamDefine.
        :rtype: str
        """
        return self._param_name

    @param_name.setter
    def param_name(self, param_name):
        r"""Sets the param_name of this ScriptParamDefine.

        参数名仅支持字母、数字以及下划线

        :param param_name: The param_name of this ScriptParamDefine.
        :type param_name: str
        """
        self._param_name = param_name

    @property
    def param_value(self):
        r"""Gets the param_value of this ScriptParamDefine.

        1.参数长度为1-4096位 2.可以包含大写字母、小写字母、数字及特殊字符(_-/.* ?:\",=+@#\\[{]}) 3.禁止出现连续'.'

        :return: The param_value of this ScriptParamDefine.
        :rtype: str
        """
        return self._param_value

    @param_value.setter
    def param_value(self, param_value):
        r"""Sets the param_value of this ScriptParamDefine.

        1.参数长度为1-4096位 2.可以包含大写字母、小写字母、数字及特殊字符(_-/.* ?:\",=+@#\\[{]}) 3.禁止出现连续'.'

        :param param_value: The param_value of this ScriptParamDefine.
        :type param_value: str
        """
        self._param_value = param_value

    @property
    def param_description(self):
        r"""Gets the param_description of this ScriptParamDefine.

        参数描述

        :return: The param_description of this ScriptParamDefine.
        :rtype: str
        """
        return self._param_description

    @param_description.setter
    def param_description(self, param_description):
        r"""Sets the param_description of this ScriptParamDefine.

        参数描述

        :param param_description: The param_description of this ScriptParamDefine.
        :type param_description: str
        """
        self._param_description = param_description

    @property
    def param_order(self):
        r"""Gets the param_order of this ScriptParamDefine.

        该参数已废弃，传入该参数不会生效。

        :return: The param_order of this ScriptParamDefine.
        :rtype: int
        """
        return self._param_order

    @param_order.setter
    def param_order(self, param_order):
        r"""Sets the param_order of this ScriptParamDefine.

        该参数已废弃，传入该参数不会生效。

        :param param_order: The param_order of this ScriptParamDefine.
        :type param_order: int
        """
        self._param_order = param_order

    @property
    def sensitive(self):
        r"""Gets the sensitive of this ScriptParamDefine.

        是否是敏感参数

        :return: The sensitive of this ScriptParamDefine.
        :rtype: bool
        """
        return self._sensitive

    @sensitive.setter
    def sensitive(self, sensitive):
        r"""Sets the sensitive of this ScriptParamDefine.

        是否是敏感参数

        :param sensitive: The sensitive of this ScriptParamDefine.
        :type sensitive: bool
        """
        self._sensitive = sensitive

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
        if not isinstance(other, ScriptParamDefine):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
