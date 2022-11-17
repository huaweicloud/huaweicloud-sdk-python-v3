# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckpointReplicateParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'auto_trigger': 'bool',
        'destination_project_id': 'str',
        'destination_region': 'str',
        'destination_vault_id': 'str',
        'enable_acceleration': 'bool',
        'vault_id': 'str'
    }

    attribute_map = {
        'auto_trigger': 'auto_trigger',
        'destination_project_id': 'destination_project_id',
        'destination_region': 'destination_region',
        'destination_vault_id': 'destination_vault_id',
        'enable_acceleration': 'enable_acceleration',
        'vault_id': 'vault_id'
    }

    def __init__(self, auto_trigger=None, destination_project_id=None, destination_region=None, destination_vault_id=None, enable_acceleration=None, vault_id=None):
        """CheckpointReplicateParam

        The model defined in huaweicloud sdk

        :param auto_trigger: 本次复制是否自动触发，默认为false，代表手动触发
        :type auto_trigger: bool
        :param destination_project_id: 复制的目标项目ID
        :type destination_project_id: str
        :param destination_region: 复制的目标区域id
        :type destination_region: str
        :param destination_vault_id: 目标区域存储库ID
        :type destination_vault_id: str
        :param enable_acceleration: 跨区域复制时，是否启用加速从而缩短复制的时间，如果不指定，默认不启用加速，如果启用加速，会额外收取加速的费用。
        :type enable_acceleration: bool
        :param vault_id: 存储库ID: uuid
        :type vault_id: str
        """
        
        

        self._auto_trigger = None
        self._destination_project_id = None
        self._destination_region = None
        self._destination_vault_id = None
        self._enable_acceleration = None
        self._vault_id = None
        self.discriminator = None

        if auto_trigger is not None:
            self.auto_trigger = auto_trigger
        self.destination_project_id = destination_project_id
        self.destination_region = destination_region
        self.destination_vault_id = destination_vault_id
        if enable_acceleration is not None:
            self.enable_acceleration = enable_acceleration
        self.vault_id = vault_id

    @property
    def auto_trigger(self):
        """Gets the auto_trigger of this CheckpointReplicateParam.

        本次复制是否自动触发，默认为false，代表手动触发

        :return: The auto_trigger of this CheckpointReplicateParam.
        :rtype: bool
        """
        return self._auto_trigger

    @auto_trigger.setter
    def auto_trigger(self, auto_trigger):
        """Sets the auto_trigger of this CheckpointReplicateParam.

        本次复制是否自动触发，默认为false，代表手动触发

        :param auto_trigger: The auto_trigger of this CheckpointReplicateParam.
        :type auto_trigger: bool
        """
        self._auto_trigger = auto_trigger

    @property
    def destination_project_id(self):
        """Gets the destination_project_id of this CheckpointReplicateParam.

        复制的目标项目ID

        :return: The destination_project_id of this CheckpointReplicateParam.
        :rtype: str
        """
        return self._destination_project_id

    @destination_project_id.setter
    def destination_project_id(self, destination_project_id):
        """Sets the destination_project_id of this CheckpointReplicateParam.

        复制的目标项目ID

        :param destination_project_id: The destination_project_id of this CheckpointReplicateParam.
        :type destination_project_id: str
        """
        self._destination_project_id = destination_project_id

    @property
    def destination_region(self):
        """Gets the destination_region of this CheckpointReplicateParam.

        复制的目标区域id

        :return: The destination_region of this CheckpointReplicateParam.
        :rtype: str
        """
        return self._destination_region

    @destination_region.setter
    def destination_region(self, destination_region):
        """Sets the destination_region of this CheckpointReplicateParam.

        复制的目标区域id

        :param destination_region: The destination_region of this CheckpointReplicateParam.
        :type destination_region: str
        """
        self._destination_region = destination_region

    @property
    def destination_vault_id(self):
        """Gets the destination_vault_id of this CheckpointReplicateParam.

        目标区域存储库ID

        :return: The destination_vault_id of this CheckpointReplicateParam.
        :rtype: str
        """
        return self._destination_vault_id

    @destination_vault_id.setter
    def destination_vault_id(self, destination_vault_id):
        """Sets the destination_vault_id of this CheckpointReplicateParam.

        目标区域存储库ID

        :param destination_vault_id: The destination_vault_id of this CheckpointReplicateParam.
        :type destination_vault_id: str
        """
        self._destination_vault_id = destination_vault_id

    @property
    def enable_acceleration(self):
        """Gets the enable_acceleration of this CheckpointReplicateParam.

        跨区域复制时，是否启用加速从而缩短复制的时间，如果不指定，默认不启用加速，如果启用加速，会额外收取加速的费用。

        :return: The enable_acceleration of this CheckpointReplicateParam.
        :rtype: bool
        """
        return self._enable_acceleration

    @enable_acceleration.setter
    def enable_acceleration(self, enable_acceleration):
        """Sets the enable_acceleration of this CheckpointReplicateParam.

        跨区域复制时，是否启用加速从而缩短复制的时间，如果不指定，默认不启用加速，如果启用加速，会额外收取加速的费用。

        :param enable_acceleration: The enable_acceleration of this CheckpointReplicateParam.
        :type enable_acceleration: bool
        """
        self._enable_acceleration = enable_acceleration

    @property
    def vault_id(self):
        """Gets the vault_id of this CheckpointReplicateParam.

        存储库ID: uuid

        :return: The vault_id of this CheckpointReplicateParam.
        :rtype: str
        """
        return self._vault_id

    @vault_id.setter
    def vault_id(self, vault_id):
        """Sets the vault_id of this CheckpointReplicateParam.

        存储库ID: uuid

        :param vault_id: The vault_id of this CheckpointReplicateParam.
        :type vault_id: str
        """
        self._vault_id = vault_id

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
        if not isinstance(other, CheckpointReplicateParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
