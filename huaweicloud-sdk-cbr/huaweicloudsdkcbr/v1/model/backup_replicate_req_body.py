# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BackupReplicateReqBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'description': 'str',
        'destination_project_id': 'str',
        'destination_region': 'str',
        'destination_vault_id': 'str',
        'enable_acceleration': 'bool',
        'name': 'str'
    }

    attribute_map = {
        'description': 'description',
        'destination_project_id': 'destination_project_id',
        'destination_region': 'destination_region',
        'destination_vault_id': 'destination_vault_id',
        'enable_acceleration': 'enable_acceleration',
        'name': 'name'
    }

    def __init__(self, description=None, destination_project_id=None, destination_region=None, destination_vault_id=None, enable_acceleration=None, name=None):
        """BackupReplicateReqBody

        The model defined in huaweicloud sdk

        :param description: 复制的描述
        :type description: str
        :param destination_project_id: 复制的目标项目ID
        :type destination_project_id: str
        :param destination_region: 复制的目标区域
        :type destination_region: str
        :param destination_vault_id: 复制的目标区域的存储库ID
        :type destination_vault_id: str
        :param enable_acceleration: 跨区域复制时，是否启用加速从而缩短复制的时间，如果不指定，默认不启用加速。
        :type enable_acceleration: bool
        :param name: 复制名称
        :type name: str
        """
        
        

        self._description = None
        self._destination_project_id = None
        self._destination_region = None
        self._destination_vault_id = None
        self._enable_acceleration = None
        self._name = None
        self.discriminator = None

        if description is not None:
            self.description = description
        self.destination_project_id = destination_project_id
        self.destination_region = destination_region
        self.destination_vault_id = destination_vault_id
        if enable_acceleration is not None:
            self.enable_acceleration = enable_acceleration
        if name is not None:
            self.name = name

    @property
    def description(self):
        """Gets the description of this BackupReplicateReqBody.

        复制的描述

        :return: The description of this BackupReplicateReqBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this BackupReplicateReqBody.

        复制的描述

        :param description: The description of this BackupReplicateReqBody.
        :type description: str
        """
        self._description = description

    @property
    def destination_project_id(self):
        """Gets the destination_project_id of this BackupReplicateReqBody.

        复制的目标项目ID

        :return: The destination_project_id of this BackupReplicateReqBody.
        :rtype: str
        """
        return self._destination_project_id

    @destination_project_id.setter
    def destination_project_id(self, destination_project_id):
        """Sets the destination_project_id of this BackupReplicateReqBody.

        复制的目标项目ID

        :param destination_project_id: The destination_project_id of this BackupReplicateReqBody.
        :type destination_project_id: str
        """
        self._destination_project_id = destination_project_id

    @property
    def destination_region(self):
        """Gets the destination_region of this BackupReplicateReqBody.

        复制的目标区域

        :return: The destination_region of this BackupReplicateReqBody.
        :rtype: str
        """
        return self._destination_region

    @destination_region.setter
    def destination_region(self, destination_region):
        """Sets the destination_region of this BackupReplicateReqBody.

        复制的目标区域

        :param destination_region: The destination_region of this BackupReplicateReqBody.
        :type destination_region: str
        """
        self._destination_region = destination_region

    @property
    def destination_vault_id(self):
        """Gets the destination_vault_id of this BackupReplicateReqBody.

        复制的目标区域的存储库ID

        :return: The destination_vault_id of this BackupReplicateReqBody.
        :rtype: str
        """
        return self._destination_vault_id

    @destination_vault_id.setter
    def destination_vault_id(self, destination_vault_id):
        """Sets the destination_vault_id of this BackupReplicateReqBody.

        复制的目标区域的存储库ID

        :param destination_vault_id: The destination_vault_id of this BackupReplicateReqBody.
        :type destination_vault_id: str
        """
        self._destination_vault_id = destination_vault_id

    @property
    def enable_acceleration(self):
        """Gets the enable_acceleration of this BackupReplicateReqBody.

        跨区域复制时，是否启用加速从而缩短复制的时间，如果不指定，默认不启用加速。

        :return: The enable_acceleration of this BackupReplicateReqBody.
        :rtype: bool
        """
        return self._enable_acceleration

    @enable_acceleration.setter
    def enable_acceleration(self, enable_acceleration):
        """Sets the enable_acceleration of this BackupReplicateReqBody.

        跨区域复制时，是否启用加速从而缩短复制的时间，如果不指定，默认不启用加速。

        :param enable_acceleration: The enable_acceleration of this BackupReplicateReqBody.
        :type enable_acceleration: bool
        """
        self._enable_acceleration = enable_acceleration

    @property
    def name(self):
        """Gets the name of this BackupReplicateReqBody.

        复制名称

        :return: The name of this BackupReplicateReqBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BackupReplicateReqBody.

        复制名称

        :param name: The name of this BackupReplicateReqBody.
        :type name: str
        """
        self._name = name

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
        if not isinstance(other, BackupReplicateReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
