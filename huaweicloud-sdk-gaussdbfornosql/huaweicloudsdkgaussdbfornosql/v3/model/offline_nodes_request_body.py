# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OfflineNodesRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'action': 'str',
        'node_ids': 'list[str]'
    }

    attribute_map = {
        'action': 'action',
        'node_ids': 'node_ids'
    }

    def __init__(self, action=None, node_ids=None):
        r"""OfflineNodesRequestBody

        The model defined in huaweicloud sdk

        :param action: 操作类型 ,shutdown代表关机,开机是startup。
        :type action: str
        :param node_ids: 节点ID列表,最多10个。
        :type node_ids: list[str]
        """
        
        

        self._action = None
        self._node_ids = None
        self.discriminator = None

        self.action = action
        self.node_ids = node_ids

    @property
    def action(self):
        r"""Gets the action of this OfflineNodesRequestBody.

        操作类型 ,shutdown代表关机,开机是startup。

        :return: The action of this OfflineNodesRequestBody.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this OfflineNodesRequestBody.

        操作类型 ,shutdown代表关机,开机是startup。

        :param action: The action of this OfflineNodesRequestBody.
        :type action: str
        """
        self._action = action

    @property
    def node_ids(self):
        r"""Gets the node_ids of this OfflineNodesRequestBody.

        节点ID列表,最多10个。

        :return: The node_ids of this OfflineNodesRequestBody.
        :rtype: list[str]
        """
        return self._node_ids

    @node_ids.setter
    def node_ids(self, node_ids):
        r"""Sets the node_ids of this OfflineNodesRequestBody.

        节点ID列表,最多10个。

        :param node_ids: The node_ids of this OfflineNodesRequestBody.
        :type node_ids: list[str]
        """
        self._node_ids = node_ids

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
        if not isinstance(other, OfflineNodesRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
