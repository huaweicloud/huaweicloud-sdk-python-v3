# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AdditionalBackupRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_additional_backup': 'bool',
        'node_id': 'str'
    }

    attribute_map = {
        'is_additional_backup': 'is_additional_backup',
        'node_id': 'node_id'
    }

    def __init__(self, is_additional_backup=None, node_id=None):
        """AdditionalBackupRequest

        The model defined in huaweicloud sdk

        :param is_additional_backup: 是否高级备份
        :type is_additional_backup: bool
        :param node_id: 节点ID
        :type node_id: str
        """
        
        

        self._is_additional_backup = None
        self._node_id = None
        self.discriminator = None

        if is_additional_backup is not None:
            self.is_additional_backup = is_additional_backup
        if node_id is not None:
            self.node_id = node_id

    @property
    def is_additional_backup(self):
        """Gets the is_additional_backup of this AdditionalBackupRequest.

        是否高级备份

        :return: The is_additional_backup of this AdditionalBackupRequest.
        :rtype: bool
        """
        return self._is_additional_backup

    @is_additional_backup.setter
    def is_additional_backup(self, is_additional_backup):
        """Sets the is_additional_backup of this AdditionalBackupRequest.

        是否高级备份

        :param is_additional_backup: The is_additional_backup of this AdditionalBackupRequest.
        :type is_additional_backup: bool
        """
        self._is_additional_backup = is_additional_backup

    @property
    def node_id(self):
        """Gets the node_id of this AdditionalBackupRequest.

        节点ID

        :return: The node_id of this AdditionalBackupRequest.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this AdditionalBackupRequest.

        节点ID

        :param node_id: The node_id of this AdditionalBackupRequest.
        :type node_id: str
        """
        self._node_id = node_id

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
        if not isinstance(other, AdditionalBackupRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
