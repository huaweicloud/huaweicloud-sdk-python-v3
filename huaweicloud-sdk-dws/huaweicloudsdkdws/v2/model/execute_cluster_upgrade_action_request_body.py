# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExecuteClusterUpgradeActionRequestBody:

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
        'item_id': 'str'
    }

    attribute_map = {
        'action': 'action',
        'item_id': 'item_id'
    }

    def __init__(self, action=None, item_id=None):
        r"""ExecuteClusterUpgradeActionRequestBody

        The model defined in huaweicloud sdk

        :param action: **参数解释**： 当前集群要做的操作。 **取值范围**： 不涉及。
        :type action: str
        :param item_id: **参数解释**： 升级项ID。 **取值范围**： 不涉及。
        :type item_id: str
        """
        
        

        self._action = None
        self._item_id = None
        self.discriminator = None

        self.action = action
        self.item_id = item_id

    @property
    def action(self):
        r"""Gets the action of this ExecuteClusterUpgradeActionRequestBody.

        **参数解释**： 当前集群要做的操作。 **取值范围**： 不涉及。

        :return: The action of this ExecuteClusterUpgradeActionRequestBody.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this ExecuteClusterUpgradeActionRequestBody.

        **参数解释**： 当前集群要做的操作。 **取值范围**： 不涉及。

        :param action: The action of this ExecuteClusterUpgradeActionRequestBody.
        :type action: str
        """
        self._action = action

    @property
    def item_id(self):
        r"""Gets the item_id of this ExecuteClusterUpgradeActionRequestBody.

        **参数解释**： 升级项ID。 **取值范围**： 不涉及。

        :return: The item_id of this ExecuteClusterUpgradeActionRequestBody.
        :rtype: str
        """
        return self._item_id

    @item_id.setter
    def item_id(self, item_id):
        r"""Sets the item_id of this ExecuteClusterUpgradeActionRequestBody.

        **参数解释**： 升级项ID。 **取值范围**： 不涉及。

        :param item_id: The item_id of this ExecuteClusterUpgradeActionRequestBody.
        :type item_id: str
        """
        self._item_id = item_id

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
        if not isinstance(other, ExecuteClusterUpgradeActionRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
