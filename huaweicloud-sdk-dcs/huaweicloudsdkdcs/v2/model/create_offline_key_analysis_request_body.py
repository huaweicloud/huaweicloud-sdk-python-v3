# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateOfflineKeyAnalysisRequestBody:

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
        'backup_id': 'str'
    }

    attribute_map = {
        'node_id': 'node_id',
        'backup_id': 'backup_id'
    }

    def __init__(self, node_id=None, backup_id=None):
        r"""CreateOfflineKeyAnalysisRequestBody

        The model defined in huaweicloud sdk

        :param node_id: **参数解释**： 实例节点ID，可通过DCS控制台进入实例的节点管理界面查看。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 
        :type node_id: str
        :param backup_id: **参数解释**： 实例备份ID，可通过DCS控制台进入实例的备份与恢复界面查看。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 
        :type backup_id: str
        """
        
        

        self._node_id = None
        self._backup_id = None
        self.discriminator = None

        self.node_id = node_id
        if backup_id is not None:
            self.backup_id = backup_id

    @property
    def node_id(self):
        r"""Gets the node_id of this CreateOfflineKeyAnalysisRequestBody.

        **参数解释**： 实例节点ID，可通过DCS控制台进入实例的节点管理界面查看。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :return: The node_id of this CreateOfflineKeyAnalysisRequestBody.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this CreateOfflineKeyAnalysisRequestBody.

        **参数解释**： 实例节点ID，可通过DCS控制台进入实例的节点管理界面查看。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :param node_id: The node_id of this CreateOfflineKeyAnalysisRequestBody.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def backup_id(self):
        r"""Gets the backup_id of this CreateOfflineKeyAnalysisRequestBody.

        **参数解释**： 实例备份ID，可通过DCS控制台进入实例的备份与恢复界面查看。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :return: The backup_id of this CreateOfflineKeyAnalysisRequestBody.
        :rtype: str
        """
        return self._backup_id

    @backup_id.setter
    def backup_id(self, backup_id):
        r"""Sets the backup_id of this CreateOfflineKeyAnalysisRequestBody.

        **参数解释**： 实例备份ID，可通过DCS控制台进入实例的备份与恢复界面查看。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :param backup_id: The backup_id of this CreateOfflineKeyAnalysisRequestBody.
        :type backup_id: str
        """
        self._backup_id = backup_id

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
        if not isinstance(other, CreateOfflineKeyAnalysisRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
