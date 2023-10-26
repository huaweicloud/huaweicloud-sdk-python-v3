# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowBackUpInfoResponse(SdkResponse):

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
        'node_id': 'str',
        'node_ip': 'str',
        'node_role': 'str',
        'backup_period': 'str'
    }

    attribute_map = {
        'is_additional_backup': 'is_additional_backup',
        'node_id': 'node_id',
        'node_ip': 'node_ip',
        'node_role': 'node_role',
        'backup_period': 'backup_period'
    }

    def __init__(self, is_additional_backup=None, node_id=None, node_ip=None, node_role=None, backup_period=None):
        """ShowBackUpInfoResponse

        The model defined in huaweicloud sdk

        :param is_additional_backup: 是否备份
        :type is_additional_backup: bool
        :param node_id: 节点ID
        :type node_id: str
        :param node_ip: 节点IP
        :type node_ip: str
        :param node_role: 节点角色
        :type node_role: str
        :param backup_period: 备份周期
        :type backup_period: str
        """
        
        super(ShowBackUpInfoResponse, self).__init__()

        self._is_additional_backup = None
        self._node_id = None
        self._node_ip = None
        self._node_role = None
        self._backup_period = None
        self.discriminator = None

        if is_additional_backup is not None:
            self.is_additional_backup = is_additional_backup
        if node_id is not None:
            self.node_id = node_id
        if node_ip is not None:
            self.node_ip = node_ip
        if node_role is not None:
            self.node_role = node_role
        if backup_period is not None:
            self.backup_period = backup_period

    @property
    def is_additional_backup(self):
        """Gets the is_additional_backup of this ShowBackUpInfoResponse.

        是否备份

        :return: The is_additional_backup of this ShowBackUpInfoResponse.
        :rtype: bool
        """
        return self._is_additional_backup

    @is_additional_backup.setter
    def is_additional_backup(self, is_additional_backup):
        """Sets the is_additional_backup of this ShowBackUpInfoResponse.

        是否备份

        :param is_additional_backup: The is_additional_backup of this ShowBackUpInfoResponse.
        :type is_additional_backup: bool
        """
        self._is_additional_backup = is_additional_backup

    @property
    def node_id(self):
        """Gets the node_id of this ShowBackUpInfoResponse.

        节点ID

        :return: The node_id of this ShowBackUpInfoResponse.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this ShowBackUpInfoResponse.

        节点ID

        :param node_id: The node_id of this ShowBackUpInfoResponse.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def node_ip(self):
        """Gets the node_ip of this ShowBackUpInfoResponse.

        节点IP

        :return: The node_ip of this ShowBackUpInfoResponse.
        :rtype: str
        """
        return self._node_ip

    @node_ip.setter
    def node_ip(self, node_ip):
        """Sets the node_ip of this ShowBackUpInfoResponse.

        节点IP

        :param node_ip: The node_ip of this ShowBackUpInfoResponse.
        :type node_ip: str
        """
        self._node_ip = node_ip

    @property
    def node_role(self):
        """Gets the node_role of this ShowBackUpInfoResponse.

        节点角色

        :return: The node_role of this ShowBackUpInfoResponse.
        :rtype: str
        """
        return self._node_role

    @node_role.setter
    def node_role(self, node_role):
        """Sets the node_role of this ShowBackUpInfoResponse.

        节点角色

        :param node_role: The node_role of this ShowBackUpInfoResponse.
        :type node_role: str
        """
        self._node_role = node_role

    @property
    def backup_period(self):
        """Gets the backup_period of this ShowBackUpInfoResponse.

        备份周期

        :return: The backup_period of this ShowBackUpInfoResponse.
        :rtype: str
        """
        return self._backup_period

    @backup_period.setter
    def backup_period(self, backup_period):
        """Sets the backup_period of this ShowBackUpInfoResponse.

        备份周期

        :param backup_period: The backup_period of this ShowBackUpInfoResponse.
        :type backup_period: str
        """
        self._backup_period = backup_period

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
        if not isinstance(other, ShowBackUpInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
