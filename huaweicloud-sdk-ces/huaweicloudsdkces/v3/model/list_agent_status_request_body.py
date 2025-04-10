# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAgentStatusRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_ids': 'list[str]',
        'uniagent_status': 'str',
        'extension_name': 'str',
        'extension_status': 'str'
    }

    attribute_map = {
        'instance_ids': 'instance_ids',
        'uniagent_status': 'uniagent_status',
        'extension_name': 'extension_name',
        'extension_status': 'extension_status'
    }

    def __init__(self, instance_ids=None, uniagent_status=None, extension_name=None, extension_status=None):
        r"""ListAgentStatusRequestBody

        The model defined in huaweicloud sdk

        :param instance_ids: 机器实例id列表
        :type instance_ids: list[str]
        :param uniagent_status: uniagent运行状态，不传查所有状态,none无，running运行中，silent静默中，unknown故障
        :type uniagent_status: str
        :param extension_name: 插件名称，不传查所有插件，目前仅支持telescope
        :type extension_name: str
        :param extension_status: 插件状态，不传查所有状态, none未安装，running运行中，stopped已停止，fault故障（进程异常），unknown故障（连接异常）
        :type extension_status: str
        """
        
        

        self._instance_ids = None
        self._uniagent_status = None
        self._extension_name = None
        self._extension_status = None
        self.discriminator = None

        self.instance_ids = instance_ids
        if uniagent_status is not None:
            self.uniagent_status = uniagent_status
        if extension_name is not None:
            self.extension_name = extension_name
        if extension_status is not None:
            self.extension_status = extension_status

    @property
    def instance_ids(self):
        r"""Gets the instance_ids of this ListAgentStatusRequestBody.

        机器实例id列表

        :return: The instance_ids of this ListAgentStatusRequestBody.
        :rtype: list[str]
        """
        return self._instance_ids

    @instance_ids.setter
    def instance_ids(self, instance_ids):
        r"""Sets the instance_ids of this ListAgentStatusRequestBody.

        机器实例id列表

        :param instance_ids: The instance_ids of this ListAgentStatusRequestBody.
        :type instance_ids: list[str]
        """
        self._instance_ids = instance_ids

    @property
    def uniagent_status(self):
        r"""Gets the uniagent_status of this ListAgentStatusRequestBody.

        uniagent运行状态，不传查所有状态,none无，running运行中，silent静默中，unknown故障

        :return: The uniagent_status of this ListAgentStatusRequestBody.
        :rtype: str
        """
        return self._uniagent_status

    @uniagent_status.setter
    def uniagent_status(self, uniagent_status):
        r"""Sets the uniagent_status of this ListAgentStatusRequestBody.

        uniagent运行状态，不传查所有状态,none无，running运行中，silent静默中，unknown故障

        :param uniagent_status: The uniagent_status of this ListAgentStatusRequestBody.
        :type uniagent_status: str
        """
        self._uniagent_status = uniagent_status

    @property
    def extension_name(self):
        r"""Gets the extension_name of this ListAgentStatusRequestBody.

        插件名称，不传查所有插件，目前仅支持telescope

        :return: The extension_name of this ListAgentStatusRequestBody.
        :rtype: str
        """
        return self._extension_name

    @extension_name.setter
    def extension_name(self, extension_name):
        r"""Sets the extension_name of this ListAgentStatusRequestBody.

        插件名称，不传查所有插件，目前仅支持telescope

        :param extension_name: The extension_name of this ListAgentStatusRequestBody.
        :type extension_name: str
        """
        self._extension_name = extension_name

    @property
    def extension_status(self):
        r"""Gets the extension_status of this ListAgentStatusRequestBody.

        插件状态，不传查所有状态, none未安装，running运行中，stopped已停止，fault故障（进程异常），unknown故障（连接异常）

        :return: The extension_status of this ListAgentStatusRequestBody.
        :rtype: str
        """
        return self._extension_status

    @extension_status.setter
    def extension_status(self, extension_status):
        r"""Sets the extension_status of this ListAgentStatusRequestBody.

        插件状态，不传查所有状态, none未安装，running运行中，stopped已停止，fault故障（进程异常），unknown故障（连接异常）

        :param extension_status: The extension_status of this ListAgentStatusRequestBody.
        :type extension_status: str
        """
        self._extension_status = extension_status

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
        if not isinstance(other, ListAgentStatusRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
