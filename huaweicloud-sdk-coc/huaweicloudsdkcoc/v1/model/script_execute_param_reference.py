# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ScriptExecuteParamReference:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'refer_type': 'str',
        'param_id': 'str',
        'param_version': 'str'
    }

    attribute_map = {
        'refer_type': 'refer_type',
        'param_id': 'param_id',
        'param_version': 'param_version'
    }

    def __init__(self, refer_type=None, param_id=None, param_version=None):
        r"""ScriptExecuteParamReference

        The model defined in huaweicloud sdk

        :param refer_type: 参数引用类型：PARAM_STORE
        :type refer_type: str
        :param param_id: 引用参数的唯一主键id
        :type param_id: str
        :param param_version: 引用参数的版本号
        :type param_version: str
        """
        
        

        self._refer_type = None
        self._param_id = None
        self._param_version = None
        self.discriminator = None

        self.refer_type = refer_type
        self.param_id = param_id
        if param_version is not None:
            self.param_version = param_version

    @property
    def refer_type(self):
        r"""Gets the refer_type of this ScriptExecuteParamReference.

        参数引用类型：PARAM_STORE

        :return: The refer_type of this ScriptExecuteParamReference.
        :rtype: str
        """
        return self._refer_type

    @refer_type.setter
    def refer_type(self, refer_type):
        r"""Sets the refer_type of this ScriptExecuteParamReference.

        参数引用类型：PARAM_STORE

        :param refer_type: The refer_type of this ScriptExecuteParamReference.
        :type refer_type: str
        """
        self._refer_type = refer_type

    @property
    def param_id(self):
        r"""Gets the param_id of this ScriptExecuteParamReference.

        引用参数的唯一主键id

        :return: The param_id of this ScriptExecuteParamReference.
        :rtype: str
        """
        return self._param_id

    @param_id.setter
    def param_id(self, param_id):
        r"""Sets the param_id of this ScriptExecuteParamReference.

        引用参数的唯一主键id

        :param param_id: The param_id of this ScriptExecuteParamReference.
        :type param_id: str
        """
        self._param_id = param_id

    @property
    def param_version(self):
        r"""Gets the param_version of this ScriptExecuteParamReference.

        引用参数的版本号

        :return: The param_version of this ScriptExecuteParamReference.
        :rtype: str
        """
        return self._param_version

    @param_version.setter
    def param_version(self, param_version):
        r"""Sets the param_version of this ScriptExecuteParamReference.

        引用参数的版本号

        :param param_version: The param_version of this ScriptExecuteParamReference.
        :type param_version: str
        """
        self._param_version = param_version

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
        if not isinstance(other, ScriptExecuteParamReference):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
