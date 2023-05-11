# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchShowTrafficControllersRequest:

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
        'offset': 'int',
        'limit': 'int',
        'traffic_controller_id': 'str',
        'esn': 'str',
        'status': 'str'
    }

    attribute_map = {
        'instance_id': 'Instance-Id',
        'offset': 'offset',
        'limit': 'limit',
        'traffic_controller_id': 'traffic_controller_id',
        'esn': 'esn',
        'status': 'status'
    }

    def __init__(self, instance_id=None, offset=None, limit=None, traffic_controller_id=None, esn=None, status=None):
        """BatchShowTrafficControllersRequest

        The model defined in huaweicloud sdk

        :param instance_id: \&quot;**参数说明**：实例ID。dris物理实例的唯一标识。获取方法参见[获取Instance-Id](https://support.huaweicloud.com/api-v2x/v2x_04_0030.html)。  **取值范围**：仅支持数字，小写字母和横杠（-）的组合，长度36。\&quot;
        :type instance_id: str
        :param offset: **参数说明**：分页查询时的页码， offset大于等于0，默认取值为0
        :type offset: int
        :param limit: **参数说明**：分页查询时每页显示的记录数，默认值为10，取值范围为0-20的整数。
        :type limit: int
        :param traffic_controller_id: **参数说明**：信号机设备ID，全局唯一。  **取值范围**：长度不超过128，只允许字母、数字、以及_-等字符的组合。 
        :type traffic_controller_id: str
        :param esn: **参数说明**：序列号。  **取值范围**：长度不超过64，只允许字母、数字、以及_等字符的组合。 
        :type esn: str
        :param status: **参数说明**：设备状态。  **取值范围**： - ONLINE：在线 - OFFLINE：离线 - INITIAL：初始化 
        :type status: str
        """
        
        

        self._instance_id = None
        self._offset = None
        self._limit = None
        self._traffic_controller_id = None
        self._esn = None
        self._status = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if traffic_controller_id is not None:
            self.traffic_controller_id = traffic_controller_id
        if esn is not None:
            self.esn = esn
        if status is not None:
            self.status = status

    @property
    def instance_id(self):
        """Gets the instance_id of this BatchShowTrafficControllersRequest.

        \"**参数说明**：实例ID。dris物理实例的唯一标识。获取方法参见[获取Instance-Id](https://support.huaweicloud.com/api-v2x/v2x_04_0030.html)。  **取值范围**：仅支持数字，小写字母和横杠（-）的组合，长度36。\"

        :return: The instance_id of this BatchShowTrafficControllersRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this BatchShowTrafficControllersRequest.

        \"**参数说明**：实例ID。dris物理实例的唯一标识。获取方法参见[获取Instance-Id](https://support.huaweicloud.com/api-v2x/v2x_04_0030.html)。  **取值范围**：仅支持数字，小写字母和横杠（-）的组合，长度36。\"

        :param instance_id: The instance_id of this BatchShowTrafficControllersRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def offset(self):
        """Gets the offset of this BatchShowTrafficControllersRequest.

        **参数说明**：分页查询时的页码， offset大于等于0，默认取值为0

        :return: The offset of this BatchShowTrafficControllersRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this BatchShowTrafficControllersRequest.

        **参数说明**：分页查询时的页码， offset大于等于0，默认取值为0

        :param offset: The offset of this BatchShowTrafficControllersRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this BatchShowTrafficControllersRequest.

        **参数说明**：分页查询时每页显示的记录数，默认值为10，取值范围为0-20的整数。

        :return: The limit of this BatchShowTrafficControllersRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this BatchShowTrafficControllersRequest.

        **参数说明**：分页查询时每页显示的记录数，默认值为10，取值范围为0-20的整数。

        :param limit: The limit of this BatchShowTrafficControllersRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def traffic_controller_id(self):
        """Gets the traffic_controller_id of this BatchShowTrafficControllersRequest.

        **参数说明**：信号机设备ID，全局唯一。  **取值范围**：长度不超过128，只允许字母、数字、以及_-等字符的组合。 

        :return: The traffic_controller_id of this BatchShowTrafficControllersRequest.
        :rtype: str
        """
        return self._traffic_controller_id

    @traffic_controller_id.setter
    def traffic_controller_id(self, traffic_controller_id):
        """Sets the traffic_controller_id of this BatchShowTrafficControllersRequest.

        **参数说明**：信号机设备ID，全局唯一。  **取值范围**：长度不超过128，只允许字母、数字、以及_-等字符的组合。 

        :param traffic_controller_id: The traffic_controller_id of this BatchShowTrafficControllersRequest.
        :type traffic_controller_id: str
        """
        self._traffic_controller_id = traffic_controller_id

    @property
    def esn(self):
        """Gets the esn of this BatchShowTrafficControllersRequest.

        **参数说明**：序列号。  **取值范围**：长度不超过64，只允许字母、数字、以及_等字符的组合。 

        :return: The esn of this BatchShowTrafficControllersRequest.
        :rtype: str
        """
        return self._esn

    @esn.setter
    def esn(self, esn):
        """Sets the esn of this BatchShowTrafficControllersRequest.

        **参数说明**：序列号。  **取值范围**：长度不超过64，只允许字母、数字、以及_等字符的组合。 

        :param esn: The esn of this BatchShowTrafficControllersRequest.
        :type esn: str
        """
        self._esn = esn

    @property
    def status(self):
        """Gets the status of this BatchShowTrafficControllersRequest.

        **参数说明**：设备状态。  **取值范围**： - ONLINE：在线 - OFFLINE：离线 - INITIAL：初始化 

        :return: The status of this BatchShowTrafficControllersRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this BatchShowTrafficControllersRequest.

        **参数说明**：设备状态。  **取值范围**： - ONLINE：在线 - OFFLINE：离线 - INITIAL：初始化 

        :param status: The status of this BatchShowTrafficControllersRequest.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, BatchShowTrafficControllersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
