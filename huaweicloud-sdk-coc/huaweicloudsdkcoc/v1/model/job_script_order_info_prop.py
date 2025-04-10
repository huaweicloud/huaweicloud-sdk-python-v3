# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobScriptOrderInfoProp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'script_uuid': 'str',
        'script_name': 'str',
        'script_version_uuid': 'int',
        'script_version_name': 'str',
        'current_execute_batch_index': 'int',
        'execute_param': 'ScriptExecuteParam'
    }

    attribute_map = {
        'script_uuid': 'script_uuid',
        'script_name': 'script_name',
        'script_version_uuid': 'script_version_uuid',
        'script_version_name': 'script_version_name',
        'current_execute_batch_index': 'current_execute_batch_index',
        'execute_param': 'execute_param'
    }

    def __init__(self, script_uuid=None, script_name=None, script_version_uuid=None, script_version_name=None, current_execute_batch_index=None, execute_param=None):
        r"""JobScriptOrderInfoProp

        The model defined in huaweicloud sdk

        :param script_uuid: 脚本uuid
        :type script_uuid: str
        :param script_name: 脚本名称
        :type script_name: str
        :param script_version_uuid: 脚本版本uuid
        :type script_version_uuid: int
        :param script_version_name: 脚本版本名
        :type script_version_name: str
        :param current_execute_batch_index: 当前执行批次index
        :type current_execute_batch_index: int
        :param execute_param: 
        :type execute_param: :class:`huaweicloudsdkcoc.v1.ScriptExecuteParam`
        """
        
        

        self._script_uuid = None
        self._script_name = None
        self._script_version_uuid = None
        self._script_version_name = None
        self._current_execute_batch_index = None
        self._execute_param = None
        self.discriminator = None

        if script_uuid is not None:
            self.script_uuid = script_uuid
        if script_name is not None:
            self.script_name = script_name
        if script_version_uuid is not None:
            self.script_version_uuid = script_version_uuid
        if script_version_name is not None:
            self.script_version_name = script_version_name
        if current_execute_batch_index is not None:
            self.current_execute_batch_index = current_execute_batch_index
        if execute_param is not None:
            self.execute_param = execute_param

    @property
    def script_uuid(self):
        r"""Gets the script_uuid of this JobScriptOrderInfoProp.

        脚本uuid

        :return: The script_uuid of this JobScriptOrderInfoProp.
        :rtype: str
        """
        return self._script_uuid

    @script_uuid.setter
    def script_uuid(self, script_uuid):
        r"""Sets the script_uuid of this JobScriptOrderInfoProp.

        脚本uuid

        :param script_uuid: The script_uuid of this JobScriptOrderInfoProp.
        :type script_uuid: str
        """
        self._script_uuid = script_uuid

    @property
    def script_name(self):
        r"""Gets the script_name of this JobScriptOrderInfoProp.

        脚本名称

        :return: The script_name of this JobScriptOrderInfoProp.
        :rtype: str
        """
        return self._script_name

    @script_name.setter
    def script_name(self, script_name):
        r"""Sets the script_name of this JobScriptOrderInfoProp.

        脚本名称

        :param script_name: The script_name of this JobScriptOrderInfoProp.
        :type script_name: str
        """
        self._script_name = script_name

    @property
    def script_version_uuid(self):
        r"""Gets the script_version_uuid of this JobScriptOrderInfoProp.

        脚本版本uuid

        :return: The script_version_uuid of this JobScriptOrderInfoProp.
        :rtype: int
        """
        return self._script_version_uuid

    @script_version_uuid.setter
    def script_version_uuid(self, script_version_uuid):
        r"""Sets the script_version_uuid of this JobScriptOrderInfoProp.

        脚本版本uuid

        :param script_version_uuid: The script_version_uuid of this JobScriptOrderInfoProp.
        :type script_version_uuid: int
        """
        self._script_version_uuid = script_version_uuid

    @property
    def script_version_name(self):
        r"""Gets the script_version_name of this JobScriptOrderInfoProp.

        脚本版本名

        :return: The script_version_name of this JobScriptOrderInfoProp.
        :rtype: str
        """
        return self._script_version_name

    @script_version_name.setter
    def script_version_name(self, script_version_name):
        r"""Sets the script_version_name of this JobScriptOrderInfoProp.

        脚本版本名

        :param script_version_name: The script_version_name of this JobScriptOrderInfoProp.
        :type script_version_name: str
        """
        self._script_version_name = script_version_name

    @property
    def current_execute_batch_index(self):
        r"""Gets the current_execute_batch_index of this JobScriptOrderInfoProp.

        当前执行批次index

        :return: The current_execute_batch_index of this JobScriptOrderInfoProp.
        :rtype: int
        """
        return self._current_execute_batch_index

    @current_execute_batch_index.setter
    def current_execute_batch_index(self, current_execute_batch_index):
        r"""Sets the current_execute_batch_index of this JobScriptOrderInfoProp.

        当前执行批次index

        :param current_execute_batch_index: The current_execute_batch_index of this JobScriptOrderInfoProp.
        :type current_execute_batch_index: int
        """
        self._current_execute_batch_index = current_execute_batch_index

    @property
    def execute_param(self):
        r"""Gets the execute_param of this JobScriptOrderInfoProp.

        :return: The execute_param of this JobScriptOrderInfoProp.
        :rtype: :class:`huaweicloudsdkcoc.v1.ScriptExecuteParam`
        """
        return self._execute_param

    @execute_param.setter
    def execute_param(self, execute_param):
        r"""Sets the execute_param of this JobScriptOrderInfoProp.

        :param execute_param: The execute_param of this JobScriptOrderInfoProp.
        :type execute_param: :class:`huaweicloudsdkcoc.v1.ScriptExecuteParam`
        """
        self._execute_param = execute_param

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
        if not isinstance(other, JobScriptOrderInfoProp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
