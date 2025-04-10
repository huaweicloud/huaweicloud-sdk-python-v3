# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SwitchNodeConnectionRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'node_id': 'str',
        'provider': 'str',
        'action': 'str'
    }

    attribute_map = {
        'node_id': 'node_id',
        'provider': 'provider',
        'action': 'action'
    }

    def __init__(self, node_id=None, provider=None, action=None):
        r"""SwitchNodeConnectionRequest

        The model defined in huaweicloud sdk

        :param node_id: 设备ID，从专业版HiLens控制台设备管理[查询设备列表](ListNodeUsingGeT.xml)获取
        :type node_id: str
        :param provider: 服务提供者：ief或hilens，选择设备纳管到不同的平台。不填默认为hilens平台
        :type provider: str
        :param action: 设备启用/停用动作，启用（start）,停用（stop）
        :type action: str
        """
        
        

        self._node_id = None
        self._provider = None
        self._action = None
        self.discriminator = None

        self.node_id = node_id
        if provider is not None:
            self.provider = provider
        self.action = action

    @property
    def node_id(self):
        r"""Gets the node_id of this SwitchNodeConnectionRequest.

        设备ID，从专业版HiLens控制台设备管理[查询设备列表](ListNodeUsingGeT.xml)获取

        :return: The node_id of this SwitchNodeConnectionRequest.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this SwitchNodeConnectionRequest.

        设备ID，从专业版HiLens控制台设备管理[查询设备列表](ListNodeUsingGeT.xml)获取

        :param node_id: The node_id of this SwitchNodeConnectionRequest.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def provider(self):
        r"""Gets the provider of this SwitchNodeConnectionRequest.

        服务提供者：ief或hilens，选择设备纳管到不同的平台。不填默认为hilens平台

        :return: The provider of this SwitchNodeConnectionRequest.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        r"""Sets the provider of this SwitchNodeConnectionRequest.

        服务提供者：ief或hilens，选择设备纳管到不同的平台。不填默认为hilens平台

        :param provider: The provider of this SwitchNodeConnectionRequest.
        :type provider: str
        """
        self._provider = provider

    @property
    def action(self):
        r"""Gets the action of this SwitchNodeConnectionRequest.

        设备启用/停用动作，启用（start）,停用（stop）

        :return: The action of this SwitchNodeConnectionRequest.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this SwitchNodeConnectionRequest.

        设备启用/停用动作，启用（start）,停用（stop）

        :param action: The action of this SwitchNodeConnectionRequest.
        :type action: str
        """
        self._action = action

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
        if not isinstance(other, SwitchNodeConnectionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
