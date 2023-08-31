# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AgentStatusInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'uniagent_status': 'str',
        'extensions': 'list[ExtensionInfo]'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'uniagent_status': 'uniagent_status',
        'extensions': 'extensions'
    }

    def __init__(self, instance_id=None, uniagent_status=None, extensions=None):
        """AgentStatusInfo

        The model defined in huaweicloud sdk

        :param instance_id: 机器id
        :type instance_id: str
        :param uniagent_status: uniagent运行状态,none无，running运行中，silent静默中，unknown故障
        :type uniagent_status: str
        :param extensions: 插件信息列表
        :type extensions: list[:class:`huaweicloudsdkces.v3.ExtensionInfo`]
        """
        
        

        self._instance_id = None
        self._uniagent_status = None
        self._extensions = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if uniagent_status is not None:
            self.uniagent_status = uniagent_status
        if extensions is not None:
            self.extensions = extensions

    @property
    def instance_id(self):
        """Gets the instance_id of this AgentStatusInfo.

        机器id

        :return: The instance_id of this AgentStatusInfo.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this AgentStatusInfo.

        机器id

        :param instance_id: The instance_id of this AgentStatusInfo.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def uniagent_status(self):
        """Gets the uniagent_status of this AgentStatusInfo.

        uniagent运行状态,none无，running运行中，silent静默中，unknown故障

        :return: The uniagent_status of this AgentStatusInfo.
        :rtype: str
        """
        return self._uniagent_status

    @uniagent_status.setter
    def uniagent_status(self, uniagent_status):
        """Sets the uniagent_status of this AgentStatusInfo.

        uniagent运行状态,none无，running运行中，silent静默中，unknown故障

        :param uniagent_status: The uniagent_status of this AgentStatusInfo.
        :type uniagent_status: str
        """
        self._uniagent_status = uniagent_status

    @property
    def extensions(self):
        """Gets the extensions of this AgentStatusInfo.

        插件信息列表

        :return: The extensions of this AgentStatusInfo.
        :rtype: list[:class:`huaweicloudsdkces.v3.ExtensionInfo`]
        """
        return self._extensions

    @extensions.setter
    def extensions(self, extensions):
        """Sets the extensions of this AgentStatusInfo.

        插件信息列表

        :param extensions: The extensions of this AgentStatusInfo.
        :type extensions: list[:class:`huaweicloudsdkces.v3.ExtensionInfo`]
        """
        self._extensions = extensions

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
        if not isinstance(other, AgentStatusInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
