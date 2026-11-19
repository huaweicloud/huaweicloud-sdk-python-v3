# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowBackupsStatisticsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count_backedup_server': 'int',
        'count_restored_task': 'int',
        'count_used_capacity': 'int',
        'count_total_capacity': 'int',
        'vault_status': 'str'
    }

    attribute_map = {
        'count_backedup_server': 'count_backedup_server',
        'count_restored_task': 'count_restored_task',
        'count_used_capacity': 'count_used_capacity',
        'count_total_capacity': 'count_total_capacity',
        'vault_status': 'vault_status'
    }

    def __init__(self, count_backedup_server=None, count_restored_task=None, count_used_capacity=None, count_total_capacity=None, vault_status=None):
        r"""ShowBackupsStatisticsResponse

        The model defined in huaweicloud sdk

        :param count_backedup_server: **参数解释**： 已备份服务器数量 **取值范围**： 最小值0，最大值2147483647 
        :type count_backedup_server: int
        :param count_restored_task: **参数解释**： 已恢复的备份任务数量 **取值范围**： 最小值0，最大值2147483647 
        :type count_restored_task: int
        :param count_used_capacity: **参数解释**： 已使用容量 **取值范围**： 最小值0，最大值2147483647 
        :type count_used_capacity: int
        :param count_total_capacity: **参数解释**： 总容量 **取值范围**： 最小值0，最大值2147483647 
        :type count_total_capacity: int
        :param vault_status: **参数解释**： 存储库状态 **取值范围**： 字符长度0-64位 
        :type vault_status: str
        """
        
        super().__init__()

        self._count_backedup_server = None
        self._count_restored_task = None
        self._count_used_capacity = None
        self._count_total_capacity = None
        self._vault_status = None
        self.discriminator = None

        if count_backedup_server is not None:
            self.count_backedup_server = count_backedup_server
        if count_restored_task is not None:
            self.count_restored_task = count_restored_task
        if count_used_capacity is not None:
            self.count_used_capacity = count_used_capacity
        if count_total_capacity is not None:
            self.count_total_capacity = count_total_capacity
        if vault_status is not None:
            self.vault_status = vault_status

    @property
    def count_backedup_server(self):
        r"""Gets the count_backedup_server of this ShowBackupsStatisticsResponse.

        **参数解释**： 已备份服务器数量 **取值范围**： 最小值0，最大值2147483647 

        :return: The count_backedup_server of this ShowBackupsStatisticsResponse.
        :rtype: int
        """
        return self._count_backedup_server

    @count_backedup_server.setter
    def count_backedup_server(self, count_backedup_server):
        r"""Sets the count_backedup_server of this ShowBackupsStatisticsResponse.

        **参数解释**： 已备份服务器数量 **取值范围**： 最小值0，最大值2147483647 

        :param count_backedup_server: The count_backedup_server of this ShowBackupsStatisticsResponse.
        :type count_backedup_server: int
        """
        self._count_backedup_server = count_backedup_server

    @property
    def count_restored_task(self):
        r"""Gets the count_restored_task of this ShowBackupsStatisticsResponse.

        **参数解释**： 已恢复的备份任务数量 **取值范围**： 最小值0，最大值2147483647 

        :return: The count_restored_task of this ShowBackupsStatisticsResponse.
        :rtype: int
        """
        return self._count_restored_task

    @count_restored_task.setter
    def count_restored_task(self, count_restored_task):
        r"""Sets the count_restored_task of this ShowBackupsStatisticsResponse.

        **参数解释**： 已恢复的备份任务数量 **取值范围**： 最小值0，最大值2147483647 

        :param count_restored_task: The count_restored_task of this ShowBackupsStatisticsResponse.
        :type count_restored_task: int
        """
        self._count_restored_task = count_restored_task

    @property
    def count_used_capacity(self):
        r"""Gets the count_used_capacity of this ShowBackupsStatisticsResponse.

        **参数解释**： 已使用容量 **取值范围**： 最小值0，最大值2147483647 

        :return: The count_used_capacity of this ShowBackupsStatisticsResponse.
        :rtype: int
        """
        return self._count_used_capacity

    @count_used_capacity.setter
    def count_used_capacity(self, count_used_capacity):
        r"""Sets the count_used_capacity of this ShowBackupsStatisticsResponse.

        **参数解释**： 已使用容量 **取值范围**： 最小值0，最大值2147483647 

        :param count_used_capacity: The count_used_capacity of this ShowBackupsStatisticsResponse.
        :type count_used_capacity: int
        """
        self._count_used_capacity = count_used_capacity

    @property
    def count_total_capacity(self):
        r"""Gets the count_total_capacity of this ShowBackupsStatisticsResponse.

        **参数解释**： 总容量 **取值范围**： 最小值0，最大值2147483647 

        :return: The count_total_capacity of this ShowBackupsStatisticsResponse.
        :rtype: int
        """
        return self._count_total_capacity

    @count_total_capacity.setter
    def count_total_capacity(self, count_total_capacity):
        r"""Sets the count_total_capacity of this ShowBackupsStatisticsResponse.

        **参数解释**： 总容量 **取值范围**： 最小值0，最大值2147483647 

        :param count_total_capacity: The count_total_capacity of this ShowBackupsStatisticsResponse.
        :type count_total_capacity: int
        """
        self._count_total_capacity = count_total_capacity

    @property
    def vault_status(self):
        r"""Gets the vault_status of this ShowBackupsStatisticsResponse.

        **参数解释**： 存储库状态 **取值范围**： 字符长度0-64位 

        :return: The vault_status of this ShowBackupsStatisticsResponse.
        :rtype: str
        """
        return self._vault_status

    @vault_status.setter
    def vault_status(self, vault_status):
        r"""Sets the vault_status of this ShowBackupsStatisticsResponse.

        **参数解释**： 存储库状态 **取值范围**： 字符长度0-64位 

        :param vault_status: The vault_status of this ShowBackupsStatisticsResponse.
        :type vault_status: str
        """
        self._vault_status = vault_status

    def to_dict(self):
        import warnings
        warnings.warn("ShowBackupsStatisticsResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowBackupsStatisticsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
