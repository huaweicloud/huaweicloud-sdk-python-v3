# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ScriptExecuteParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resourceful': 'bool',
        'timeout': 'int',
        'success_rate': 'float',
        'execute_user': 'str',
        'script_params': 'list[ScriptExecuteInputParam]'
    }

    attribute_map = {
        'resourceful': 'resourceful',
        'timeout': 'timeout',
        'success_rate': 'success_rate',
        'execute_user': 'execute_user',
        'script_params': 'script_params'
    }

    def __init__(self, resourceful=None, timeout=None, success_rate=None, execute_user=None, script_params=None):
        r"""ScriptExecuteParam

        The model defined in huaweicloud sdk

        :param resourceful: 该参数已废弃，传入该参数不会生效。
        :type resourceful: bool
        :param timeout: 超时时间，单位：秒，取值范围待定，5 &lt; timeout &lt; 1800
        :type timeout: int
        :param success_rate: 成功率，支持小数点后一位
        :type success_rate: float
        :param execute_user: 脚本执行用户，如：root
        :type execute_user: str
        :param script_params: 脚本入参列表
        :type script_params: list[:class:`huaweicloudsdkcoc.v1.ScriptExecuteInputParam`]
        """
        
        

        self._resourceful = None
        self._timeout = None
        self._success_rate = None
        self._execute_user = None
        self._script_params = None
        self.discriminator = None

        if resourceful is not None:
            self.resourceful = resourceful
        self.timeout = timeout
        self.success_rate = success_rate
        self.execute_user = execute_user
        if script_params is not None:
            self.script_params = script_params

    @property
    def resourceful(self):
        r"""Gets the resourceful of this ScriptExecuteParam.

        该参数已废弃，传入该参数不会生效。

        :return: The resourceful of this ScriptExecuteParam.
        :rtype: bool
        """
        return self._resourceful

    @resourceful.setter
    def resourceful(self, resourceful):
        r"""Sets the resourceful of this ScriptExecuteParam.

        该参数已废弃，传入该参数不会生效。

        :param resourceful: The resourceful of this ScriptExecuteParam.
        :type resourceful: bool
        """
        self._resourceful = resourceful

    @property
    def timeout(self):
        r"""Gets the timeout of this ScriptExecuteParam.

        超时时间，单位：秒，取值范围待定，5 < timeout < 1800

        :return: The timeout of this ScriptExecuteParam.
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        r"""Sets the timeout of this ScriptExecuteParam.

        超时时间，单位：秒，取值范围待定，5 < timeout < 1800

        :param timeout: The timeout of this ScriptExecuteParam.
        :type timeout: int
        """
        self._timeout = timeout

    @property
    def success_rate(self):
        r"""Gets the success_rate of this ScriptExecuteParam.

        成功率，支持小数点后一位

        :return: The success_rate of this ScriptExecuteParam.
        :rtype: float
        """
        return self._success_rate

    @success_rate.setter
    def success_rate(self, success_rate):
        r"""Sets the success_rate of this ScriptExecuteParam.

        成功率，支持小数点后一位

        :param success_rate: The success_rate of this ScriptExecuteParam.
        :type success_rate: float
        """
        self._success_rate = success_rate

    @property
    def execute_user(self):
        r"""Gets the execute_user of this ScriptExecuteParam.

        脚本执行用户，如：root

        :return: The execute_user of this ScriptExecuteParam.
        :rtype: str
        """
        return self._execute_user

    @execute_user.setter
    def execute_user(self, execute_user):
        r"""Sets the execute_user of this ScriptExecuteParam.

        脚本执行用户，如：root

        :param execute_user: The execute_user of this ScriptExecuteParam.
        :type execute_user: str
        """
        self._execute_user = execute_user

    @property
    def script_params(self):
        r"""Gets the script_params of this ScriptExecuteParam.

        脚本入参列表

        :return: The script_params of this ScriptExecuteParam.
        :rtype: list[:class:`huaweicloudsdkcoc.v1.ScriptExecuteInputParam`]
        """
        return self._script_params

    @script_params.setter
    def script_params(self, script_params):
        r"""Sets the script_params of this ScriptExecuteParam.

        脚本入参列表

        :param script_params: The script_params of this ScriptExecuteParam.
        :type script_params: list[:class:`huaweicloudsdkcoc.v1.ScriptExecuteInputParam`]
        """
        self._script_params = script_params

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
        if not isinstance(other, ScriptExecuteParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
