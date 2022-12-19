# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowForwardingConfigsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'forwarding_type': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'instance_id': 'Instance-Id',
        'forwarding_type': 'forwarding_type',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, instance_id=None, forwarding_type=None, offset=None, limit=None):
        """ShowForwardingConfigsRequest

        The model defined in huaweicloud sdk

        :param instance_id: **参数说明**：实例ID。dris物理实例的唯一标识。获取方法参见[获取Instance-Id](https://support.huaweicloud.com/api-v2x/v2x_04_0030.html)。  **取值范围**：仅支持数字，小写字母和连接符（-）的组合，长度36。
        :type instance_id: str
        :param forwarding_type: **参数说明**：转发配置的类型。  **取值范围**：当前仅支持“kafka，mrskafka”。
        :type forwarding_type: str
        :param offset: **参数说明**：查询配置列表的偏移量。
        :type offset: int
        :param limit: **参数说明**：查询时每页显示的记录数。
        :type limit: int
        """
        
        

        self._instance_id = None
        self._forwarding_type = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        self.forwarding_type = forwarding_type
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def instance_id(self):
        """Gets the instance_id of this ShowForwardingConfigsRequest.

        **参数说明**：实例ID。dris物理实例的唯一标识。获取方法参见[获取Instance-Id](https://support.huaweicloud.com/api-v2x/v2x_04_0030.html)。  **取值范围**：仅支持数字，小写字母和连接符（-）的组合，长度36。

        :return: The instance_id of this ShowForwardingConfigsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ShowForwardingConfigsRequest.

        **参数说明**：实例ID。dris物理实例的唯一标识。获取方法参见[获取Instance-Id](https://support.huaweicloud.com/api-v2x/v2x_04_0030.html)。  **取值范围**：仅支持数字，小写字母和连接符（-）的组合，长度36。

        :param instance_id: The instance_id of this ShowForwardingConfigsRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def forwarding_type(self):
        """Gets the forwarding_type of this ShowForwardingConfigsRequest.

        **参数说明**：转发配置的类型。  **取值范围**：当前仅支持“kafka，mrskafka”。

        :return: The forwarding_type of this ShowForwardingConfigsRequest.
        :rtype: str
        """
        return self._forwarding_type

    @forwarding_type.setter
    def forwarding_type(self, forwarding_type):
        """Sets the forwarding_type of this ShowForwardingConfigsRequest.

        **参数说明**：转发配置的类型。  **取值范围**：当前仅支持“kafka，mrskafka”。

        :param forwarding_type: The forwarding_type of this ShowForwardingConfigsRequest.
        :type forwarding_type: str
        """
        self._forwarding_type = forwarding_type

    @property
    def offset(self):
        """Gets the offset of this ShowForwardingConfigsRequest.

        **参数说明**：查询配置列表的偏移量。

        :return: The offset of this ShowForwardingConfigsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ShowForwardingConfigsRequest.

        **参数说明**：查询配置列表的偏移量。

        :param offset: The offset of this ShowForwardingConfigsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ShowForwardingConfigsRequest.

        **参数说明**：查询时每页显示的记录数。

        :return: The limit of this ShowForwardingConfigsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ShowForwardingConfigsRequest.

        **参数说明**：查询时每页显示的记录数。

        :param limit: The limit of this ShowForwardingConfigsRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ShowForwardingConfigsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
