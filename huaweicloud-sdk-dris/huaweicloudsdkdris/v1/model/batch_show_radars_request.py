# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchShowRadarsRequest:

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
        'esn': 'str',
        'offset': 'int',
        'limit': 'int',
        'status': 'str'
    }

    attribute_map = {
        'instance_id': 'Instance-Id',
        'esn': 'esn',
        'offset': 'offset',
        'limit': 'limit',
        'status': 'status'
    }

    def __init__(self, instance_id=None, esn=None, offset=None, limit=None, status=None):
        """BatchShowRadarsRequest

        The model defined in huaweicloud sdk

        :param instance_id: \&quot;**参数说明**：实例ID。dris物理实例的唯一标识。获取方法参见[获取Instance-Id](https://support.huaweicloud.com/api-v2x/v2x_04_0030.html)。  **取值范围**：仅支持数字，小写字母和横杠（-）的组合，长度36。\&quot;
        :type instance_id: str
        :param esn: **参数说明**：设备序列号。
        :type esn: str
        :param offset: **参数说明**：分页查询时的页码。
        :type offset: int
        :param limit: **参数说明**：分页查询时每页显示的记录数。
        :type limit: int
        :param status: **参数说明**：状态。  **取值范围**： - ONLINE：在线 - OFFLINE：离线 - UNKNOWN：未知 - SLEEP：睡眠 
        :type status: str
        """
        
        

        self._instance_id = None
        self._esn = None
        self._offset = None
        self._limit = None
        self._status = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if esn is not None:
            self.esn = esn
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if status is not None:
            self.status = status

    @property
    def instance_id(self):
        """Gets the instance_id of this BatchShowRadarsRequest.

        \"**参数说明**：实例ID。dris物理实例的唯一标识。获取方法参见[获取Instance-Id](https://support.huaweicloud.com/api-v2x/v2x_04_0030.html)。  **取值范围**：仅支持数字，小写字母和横杠（-）的组合，长度36。\"

        :return: The instance_id of this BatchShowRadarsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this BatchShowRadarsRequest.

        \"**参数说明**：实例ID。dris物理实例的唯一标识。获取方法参见[获取Instance-Id](https://support.huaweicloud.com/api-v2x/v2x_04_0030.html)。  **取值范围**：仅支持数字，小写字母和横杠（-）的组合，长度36。\"

        :param instance_id: The instance_id of this BatchShowRadarsRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def esn(self):
        """Gets the esn of this BatchShowRadarsRequest.

        **参数说明**：设备序列号。

        :return: The esn of this BatchShowRadarsRequest.
        :rtype: str
        """
        return self._esn

    @esn.setter
    def esn(self, esn):
        """Sets the esn of this BatchShowRadarsRequest.

        **参数说明**：设备序列号。

        :param esn: The esn of this BatchShowRadarsRequest.
        :type esn: str
        """
        self._esn = esn

    @property
    def offset(self):
        """Gets the offset of this BatchShowRadarsRequest.

        **参数说明**：分页查询时的页码。

        :return: The offset of this BatchShowRadarsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this BatchShowRadarsRequest.

        **参数说明**：分页查询时的页码。

        :param offset: The offset of this BatchShowRadarsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this BatchShowRadarsRequest.

        **参数说明**：分页查询时每页显示的记录数。

        :return: The limit of this BatchShowRadarsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this BatchShowRadarsRequest.

        **参数说明**：分页查询时每页显示的记录数。

        :param limit: The limit of this BatchShowRadarsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def status(self):
        """Gets the status of this BatchShowRadarsRequest.

        **参数说明**：状态。  **取值范围**： - ONLINE：在线 - OFFLINE：离线 - UNKNOWN：未知 - SLEEP：睡眠 

        :return: The status of this BatchShowRadarsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this BatchShowRadarsRequest.

        **参数说明**：状态。  **取值范围**： - ONLINE：在线 - OFFLINE：离线 - UNKNOWN：未知 - SLEEP：睡眠 

        :param status: The status of this BatchShowRadarsRequest.
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
        if not isinstance(other, BatchShowRadarsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
