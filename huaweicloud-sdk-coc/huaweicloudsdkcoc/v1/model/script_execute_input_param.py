# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ScriptExecuteInputParam:

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
        'param_order': 'int',
        'param_refer': 'ScriptExecuteParamReference'
    }

    attribute_map = {
        'param_name': 'param_name',
        'param_value': 'param_value',
        'param_order': 'param_order',
        'param_refer': 'param_refer'
    }

    def __init__(self, param_name=None, param_value=None, param_order=None, param_refer=None):
        r"""ScriptExecuteInputParam

        The model defined in huaweicloud sdk

        :param param_name: 脚本入参的名称,同一个脚本，参数名不能重复
        :type param_name: str
        :param param_value: 脚本入参的值，默认必填。有引用参数（param_refer不为空）时，允许为空 1.参数长度为1-4096位 2.可以包含大写字母、小写字母、数字及特殊字符(_-/.* ?:\&quot;,&#x3D;+@#\\[{]}) 3.禁止出现连续&#39;.&#39;
        :type param_value: str
        :param param_order: 该参数已废弃，传入该参数不会生效。
        :type param_order: int
        :param param_refer: 
        :type param_refer: :class:`huaweicloudsdkcoc.v1.ScriptExecuteParamReference`
        """
        
        

        self._param_name = None
        self._param_value = None
        self._param_order = None
        self._param_refer = None
        self.discriminator = None

        self.param_name = param_name
        self.param_value = param_value
        if param_order is not None:
            self.param_order = param_order
        if param_refer is not None:
            self.param_refer = param_refer

    @property
    def param_name(self):
        r"""Gets the param_name of this ScriptExecuteInputParam.

        脚本入参的名称,同一个脚本，参数名不能重复

        :return: The param_name of this ScriptExecuteInputParam.
        :rtype: str
        """
        return self._param_name

    @param_name.setter
    def param_name(self, param_name):
        r"""Sets the param_name of this ScriptExecuteInputParam.

        脚本入参的名称,同一个脚本，参数名不能重复

        :param param_name: The param_name of this ScriptExecuteInputParam.
        :type param_name: str
        """
        self._param_name = param_name

    @property
    def param_value(self):
        r"""Gets the param_value of this ScriptExecuteInputParam.

        脚本入参的值，默认必填。有引用参数（param_refer不为空）时，允许为空 1.参数长度为1-4096位 2.可以包含大写字母、小写字母、数字及特殊字符(_-/.* ?:\",=+@#\\[{]}) 3.禁止出现连续'.'

        :return: The param_value of this ScriptExecuteInputParam.
        :rtype: str
        """
        return self._param_value

    @param_value.setter
    def param_value(self, param_value):
        r"""Sets the param_value of this ScriptExecuteInputParam.

        脚本入参的值，默认必填。有引用参数（param_refer不为空）时，允许为空 1.参数长度为1-4096位 2.可以包含大写字母、小写字母、数字及特殊字符(_-/.* ?:\",=+@#\\[{]}) 3.禁止出现连续'.'

        :param param_value: The param_value of this ScriptExecuteInputParam.
        :type param_value: str
        """
        self._param_value = param_value

    @property
    def param_order(self):
        r"""Gets the param_order of this ScriptExecuteInputParam.

        该参数已废弃，传入该参数不会生效。

        :return: The param_order of this ScriptExecuteInputParam.
        :rtype: int
        """
        return self._param_order

    @param_order.setter
    def param_order(self, param_order):
        r"""Sets the param_order of this ScriptExecuteInputParam.

        该参数已废弃，传入该参数不会生效。

        :param param_order: The param_order of this ScriptExecuteInputParam.
        :type param_order: int
        """
        self._param_order = param_order

    @property
    def param_refer(self):
        r"""Gets the param_refer of this ScriptExecuteInputParam.

        :return: The param_refer of this ScriptExecuteInputParam.
        :rtype: :class:`huaweicloudsdkcoc.v1.ScriptExecuteParamReference`
        """
        return self._param_refer

    @param_refer.setter
    def param_refer(self, param_refer):
        r"""Sets the param_refer of this ScriptExecuteInputParam.

        :param param_refer: The param_refer of this ScriptExecuteInputParam.
        :type param_refer: :class:`huaweicloudsdkcoc.v1.ScriptExecuteParamReference`
        """
        self._param_refer = param_refer

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
        if not isinstance(other, ScriptExecuteInputParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
