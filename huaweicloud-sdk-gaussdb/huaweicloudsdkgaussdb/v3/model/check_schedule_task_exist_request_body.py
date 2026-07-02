# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckScheduleTaskExistRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'schedule_type': 'str',
        'proxy_id': 'str'
    }

    attribute_map = {
        'schedule_type': 'schedule_type',
        'proxy_id': 'proxy_id'
    }

    def __init__(self, schedule_type=None, proxy_id=None):
        r"""CheckScheduleTaskExistRequestBody

        The model defined in huaweicloud sdk

        :param schedule_type: **参数解释**： 定时任务类型。  **约束限制**： 不涉及。  **取值范围**：   - PROXY_VERSION_UPGRADE：表示升级数据库代理的内核小版本。   - VERSION_UPGRADE：表示升级实例的内核小版本。   - RESIZE_FLAVOR：表示实例规格变更。   - REBOOT_NODE：表示重启节点。   - REBOOT_INSTANCE：表示重启实例。  **默认取值**：   不涉及。
        :type schedule_type: str
        :param proxy_id: **参数解释**： 数据库代理ID。 获取方法请参见[查询数据库代理信息列表](https://support.huaweicloud.com/api-taurusdb/ShowGaussMySqlProxyList.html)。  **约束限制**： 不涉及。  **取值范围**： 不涉及。  **默认取值**： 不涉及。
        :type proxy_id: str
        """
        
        

        self._schedule_type = None
        self._proxy_id = None
        self.discriminator = None

        self.schedule_type = schedule_type
        if proxy_id is not None:
            self.proxy_id = proxy_id

    @property
    def schedule_type(self):
        r"""Gets the schedule_type of this CheckScheduleTaskExistRequestBody.

        **参数解释**： 定时任务类型。  **约束限制**： 不涉及。  **取值范围**：   - PROXY_VERSION_UPGRADE：表示升级数据库代理的内核小版本。   - VERSION_UPGRADE：表示升级实例的内核小版本。   - RESIZE_FLAVOR：表示实例规格变更。   - REBOOT_NODE：表示重启节点。   - REBOOT_INSTANCE：表示重启实例。  **默认取值**：   不涉及。

        :return: The schedule_type of this CheckScheduleTaskExistRequestBody.
        :rtype: str
        """
        return self._schedule_type

    @schedule_type.setter
    def schedule_type(self, schedule_type):
        r"""Sets the schedule_type of this CheckScheduleTaskExistRequestBody.

        **参数解释**： 定时任务类型。  **约束限制**： 不涉及。  **取值范围**：   - PROXY_VERSION_UPGRADE：表示升级数据库代理的内核小版本。   - VERSION_UPGRADE：表示升级实例的内核小版本。   - RESIZE_FLAVOR：表示实例规格变更。   - REBOOT_NODE：表示重启节点。   - REBOOT_INSTANCE：表示重启实例。  **默认取值**：   不涉及。

        :param schedule_type: The schedule_type of this CheckScheduleTaskExistRequestBody.
        :type schedule_type: str
        """
        self._schedule_type = schedule_type

    @property
    def proxy_id(self):
        r"""Gets the proxy_id of this CheckScheduleTaskExistRequestBody.

        **参数解释**： 数据库代理ID。 获取方法请参见[查询数据库代理信息列表](https://support.huaweicloud.com/api-taurusdb/ShowGaussMySqlProxyList.html)。  **约束限制**： 不涉及。  **取值范围**： 不涉及。  **默认取值**： 不涉及。

        :return: The proxy_id of this CheckScheduleTaskExistRequestBody.
        :rtype: str
        """
        return self._proxy_id

    @proxy_id.setter
    def proxy_id(self, proxy_id):
        r"""Sets the proxy_id of this CheckScheduleTaskExistRequestBody.

        **参数解释**： 数据库代理ID。 获取方法请参见[查询数据库代理信息列表](https://support.huaweicloud.com/api-taurusdb/ShowGaussMySqlProxyList.html)。  **约束限制**： 不涉及。  **取值范围**： 不涉及。  **默认取值**： 不涉及。

        :param proxy_id: The proxy_id of this CheckScheduleTaskExistRequestBody.
        :type proxy_id: str
        """
        self._proxy_id = proxy_id

    def to_dict(self):
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
        if not isinstance(other, CheckScheduleTaskExistRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
