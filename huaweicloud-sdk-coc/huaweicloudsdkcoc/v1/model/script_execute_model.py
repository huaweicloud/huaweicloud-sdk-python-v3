# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ScriptExecuteModel:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'execute_param': 'ScriptExecuteParam',
        'execute_batches': 'list[ExecuteInstancesBatchInfo]'
    }

    attribute_map = {
        'execute_param': 'execute_param',
        'execute_batches': 'execute_batches'
    }

    def __init__(self, execute_param=None, execute_batches=None):
        r"""ScriptExecuteModel

        The model defined in huaweicloud sdk

        :param execute_param: 
        :type execute_param: :class:`huaweicloudsdkcoc.v1.ScriptExecuteParam`
        :param execute_batches: 目标实例分批信息
        :type execute_batches: list[:class:`huaweicloudsdkcoc.v1.ExecuteInstancesBatchInfo`]
        """
        
        

        self._execute_param = None
        self._execute_batches = None
        self.discriminator = None

        self.execute_param = execute_param
        self.execute_batches = execute_batches

    @property
    def execute_param(self):
        r"""Gets the execute_param of this ScriptExecuteModel.

        :return: The execute_param of this ScriptExecuteModel.
        :rtype: :class:`huaweicloudsdkcoc.v1.ScriptExecuteParam`
        """
        return self._execute_param

    @execute_param.setter
    def execute_param(self, execute_param):
        r"""Sets the execute_param of this ScriptExecuteModel.

        :param execute_param: The execute_param of this ScriptExecuteModel.
        :type execute_param: :class:`huaweicloudsdkcoc.v1.ScriptExecuteParam`
        """
        self._execute_param = execute_param

    @property
    def execute_batches(self):
        r"""Gets the execute_batches of this ScriptExecuteModel.

        目标实例分批信息

        :return: The execute_batches of this ScriptExecuteModel.
        :rtype: list[:class:`huaweicloudsdkcoc.v1.ExecuteInstancesBatchInfo`]
        """
        return self._execute_batches

    @execute_batches.setter
    def execute_batches(self, execute_batches):
        r"""Sets the execute_batches of this ScriptExecuteModel.

        目标实例分批信息

        :param execute_batches: The execute_batches of this ScriptExecuteModel.
        :type execute_batches: list[:class:`huaweicloudsdkcoc.v1.ExecuteInstancesBatchInfo`]
        """
        self._execute_batches = execute_batches

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
        if not isinstance(other, ScriptExecuteModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
