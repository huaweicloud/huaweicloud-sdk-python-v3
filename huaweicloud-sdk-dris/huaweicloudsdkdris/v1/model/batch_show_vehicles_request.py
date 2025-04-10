# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchShowVehiclesRequest:

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
        'vehicle_id': 'str',
        'status': 'str'
    }

    attribute_map = {
        'instance_id': 'Instance-Id',
        'offset': 'offset',
        'limit': 'limit',
        'vehicle_id': 'vehicle_id',
        'status': 'status'
    }

    def __init__(self, instance_id=None, offset=None, limit=None, vehicle_id=None, status=None):
        r"""BatchShowVehiclesRequest

        The model defined in huaweicloud sdk

        :param instance_id: \&quot;**参数说明**：实例ID。dris物理实例的唯一标识。获取方法参见[获取Instance-Id](https://support.huaweicloud.com/api-v2x/v2x_04_0030.html)。  **取值范围**：仅支持数字，小写字母和横杠（-）的组合，长度36。\&quot;
        :type instance_id: str
        :param offset: **参数说明**：分页查询时的页码， offset大于等于0，默认取值为0。
        :type offset: int
        :param limit: **参数说明**：分页查询时每页显示的记录数，默认值为10，取值范围为0-20的整数。
        :type limit: int
        :param vehicle_id: **参数说明**：车辆唯一标识符。  **取值范围**：长度不超过128，只允许字母、数字、以及_-等字符的组合。 
        :type vehicle_id: str
        :param status: **参数说明**：设备状态。  **取值范围**： - ONLINE：在线 - OFFLINE：离线 - INITIAL：初始化 
        :type status: str
        """
        
        

        self._instance_id = None
        self._offset = None
        self._limit = None
        self._vehicle_id = None
        self._status = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if vehicle_id is not None:
            self.vehicle_id = vehicle_id
        if status is not None:
            self.status = status

    @property
    def instance_id(self):
        r"""Gets the instance_id of this BatchShowVehiclesRequest.

        \"**参数说明**：实例ID。dris物理实例的唯一标识。获取方法参见[获取Instance-Id](https://support.huaweicloud.com/api-v2x/v2x_04_0030.html)。  **取值范围**：仅支持数字，小写字母和横杠（-）的组合，长度36。\"

        :return: The instance_id of this BatchShowVehiclesRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this BatchShowVehiclesRequest.

        \"**参数说明**：实例ID。dris物理实例的唯一标识。获取方法参见[获取Instance-Id](https://support.huaweicloud.com/api-v2x/v2x_04_0030.html)。  **取值范围**：仅支持数字，小写字母和横杠（-）的组合，长度36。\"

        :param instance_id: The instance_id of this BatchShowVehiclesRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def offset(self):
        r"""Gets the offset of this BatchShowVehiclesRequest.

        **参数说明**：分页查询时的页码， offset大于等于0，默认取值为0。

        :return: The offset of this BatchShowVehiclesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this BatchShowVehiclesRequest.

        **参数说明**：分页查询时的页码， offset大于等于0，默认取值为0。

        :param offset: The offset of this BatchShowVehiclesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this BatchShowVehiclesRequest.

        **参数说明**：分页查询时每页显示的记录数，默认值为10，取值范围为0-20的整数。

        :return: The limit of this BatchShowVehiclesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this BatchShowVehiclesRequest.

        **参数说明**：分页查询时每页显示的记录数，默认值为10，取值范围为0-20的整数。

        :param limit: The limit of this BatchShowVehiclesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def vehicle_id(self):
        r"""Gets the vehicle_id of this BatchShowVehiclesRequest.

        **参数说明**：车辆唯一标识符。  **取值范围**：长度不超过128，只允许字母、数字、以及_-等字符的组合。 

        :return: The vehicle_id of this BatchShowVehiclesRequest.
        :rtype: str
        """
        return self._vehicle_id

    @vehicle_id.setter
    def vehicle_id(self, vehicle_id):
        r"""Sets the vehicle_id of this BatchShowVehiclesRequest.

        **参数说明**：车辆唯一标识符。  **取值范围**：长度不超过128，只允许字母、数字、以及_-等字符的组合。 

        :param vehicle_id: The vehicle_id of this BatchShowVehiclesRequest.
        :type vehicle_id: str
        """
        self._vehicle_id = vehicle_id

    @property
    def status(self):
        r"""Gets the status of this BatchShowVehiclesRequest.

        **参数说明**：设备状态。  **取值范围**： - ONLINE：在线 - OFFLINE：离线 - INITIAL：初始化 

        :return: The status of this BatchShowVehiclesRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this BatchShowVehiclesRequest.

        **参数说明**：设备状态。  **取值范围**： - ONLINE：在线 - OFFLINE：离线 - INITIAL：初始化 

        :param status: The status of this BatchShowVehiclesRequest.
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
        if not isinstance(other, BatchShowVehiclesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
