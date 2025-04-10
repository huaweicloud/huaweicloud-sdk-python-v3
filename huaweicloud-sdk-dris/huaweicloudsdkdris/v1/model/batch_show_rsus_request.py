# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchShowRsusRequest:

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
        'rsu_id': 'str',
        'esn': 'str',
        'status': 'str',
        'rsu_model_id': 'str'
    }

    attribute_map = {
        'instance_id': 'Instance-Id',
        'offset': 'offset',
        'limit': 'limit',
        'rsu_id': 'rsu_id',
        'esn': 'esn',
        'status': 'status',
        'rsu_model_id': 'rsu_model_id'
    }

    def __init__(self, instance_id=None, offset=None, limit=None, rsu_id=None, esn=None, status=None, rsu_model_id=None):
        r"""BatchShowRsusRequest

        The model defined in huaweicloud sdk

        :param instance_id: \&quot;**参数说明**：实例ID。dris物理实例的唯一标识。获取方法参见[获取Instance-Id](https://support.huaweicloud.com/api-v2x/v2x_04_0030.html)。  **取值范围**：仅支持数字，小写字母和横杠（-）的组合，长度36。\&quot;
        :type instance_id: str
        :param offset: **参数说明**：分页查询时的页码。
        :type offset: int
        :param limit: **参数说明**：分页查询时每页显示的记录数。
        :type limit: int
        :param rsu_id: **参数说明**：RSU的唯一标识符，在平台创建RSU时由平台生成。
        :type rsu_id: str
        :param esn: **参数说明**：RSU的设备序列号。  **取值范围**：只允许字母、数字、下划线（_）的组合。 
        :type esn: str
        :param status: **参数说明**：设备状态。  **取值范围**：  - ONLINE：在线  - OFFLINE：离线  - INITIAL：初始化  - UNKNOWN：未知 
        :type status: str
        :param rsu_model_id: **参数说明**：RSU型号ID，用于唯一标识一个RSU型号，在平台创建RSU型号后由平台分配获得，获取方法可参见 [创建RSU型号](https://support.huaweicloud.com/api-v2x/v2x_04_0020.html)。  **取值范围**：长度不低于1不超过36，只允许字母、数字、连接符（-）的组合。  **该字段仅供使用MQTT协议RSU设备的用户输入。使用websocket协议RSU设备的用户需忽略此字段。** 
        :type rsu_model_id: str
        """
        
        

        self._instance_id = None
        self._offset = None
        self._limit = None
        self._rsu_id = None
        self._esn = None
        self._status = None
        self._rsu_model_id = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if rsu_id is not None:
            self.rsu_id = rsu_id
        if esn is not None:
            self.esn = esn
        if status is not None:
            self.status = status
        if rsu_model_id is not None:
            self.rsu_model_id = rsu_model_id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this BatchShowRsusRequest.

        \"**参数说明**：实例ID。dris物理实例的唯一标识。获取方法参见[获取Instance-Id](https://support.huaweicloud.com/api-v2x/v2x_04_0030.html)。  **取值范围**：仅支持数字，小写字母和横杠（-）的组合，长度36。\"

        :return: The instance_id of this BatchShowRsusRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this BatchShowRsusRequest.

        \"**参数说明**：实例ID。dris物理实例的唯一标识。获取方法参见[获取Instance-Id](https://support.huaweicloud.com/api-v2x/v2x_04_0030.html)。  **取值范围**：仅支持数字，小写字母和横杠（-）的组合，长度36。\"

        :param instance_id: The instance_id of this BatchShowRsusRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def offset(self):
        r"""Gets the offset of this BatchShowRsusRequest.

        **参数说明**：分页查询时的页码。

        :return: The offset of this BatchShowRsusRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this BatchShowRsusRequest.

        **参数说明**：分页查询时的页码。

        :param offset: The offset of this BatchShowRsusRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this BatchShowRsusRequest.

        **参数说明**：分页查询时每页显示的记录数。

        :return: The limit of this BatchShowRsusRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this BatchShowRsusRequest.

        **参数说明**：分页查询时每页显示的记录数。

        :param limit: The limit of this BatchShowRsusRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def rsu_id(self):
        r"""Gets the rsu_id of this BatchShowRsusRequest.

        **参数说明**：RSU的唯一标识符，在平台创建RSU时由平台生成。

        :return: The rsu_id of this BatchShowRsusRequest.
        :rtype: str
        """
        return self._rsu_id

    @rsu_id.setter
    def rsu_id(self, rsu_id):
        r"""Sets the rsu_id of this BatchShowRsusRequest.

        **参数说明**：RSU的唯一标识符，在平台创建RSU时由平台生成。

        :param rsu_id: The rsu_id of this BatchShowRsusRequest.
        :type rsu_id: str
        """
        self._rsu_id = rsu_id

    @property
    def esn(self):
        r"""Gets the esn of this BatchShowRsusRequest.

        **参数说明**：RSU的设备序列号。  **取值范围**：只允许字母、数字、下划线（_）的组合。 

        :return: The esn of this BatchShowRsusRequest.
        :rtype: str
        """
        return self._esn

    @esn.setter
    def esn(self, esn):
        r"""Sets the esn of this BatchShowRsusRequest.

        **参数说明**：RSU的设备序列号。  **取值范围**：只允许字母、数字、下划线（_）的组合。 

        :param esn: The esn of this BatchShowRsusRequest.
        :type esn: str
        """
        self._esn = esn

    @property
    def status(self):
        r"""Gets the status of this BatchShowRsusRequest.

        **参数说明**：设备状态。  **取值范围**：  - ONLINE：在线  - OFFLINE：离线  - INITIAL：初始化  - UNKNOWN：未知 

        :return: The status of this BatchShowRsusRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this BatchShowRsusRequest.

        **参数说明**：设备状态。  **取值范围**：  - ONLINE：在线  - OFFLINE：离线  - INITIAL：初始化  - UNKNOWN：未知 

        :param status: The status of this BatchShowRsusRequest.
        :type status: str
        """
        self._status = status

    @property
    def rsu_model_id(self):
        r"""Gets the rsu_model_id of this BatchShowRsusRequest.

        **参数说明**：RSU型号ID，用于唯一标识一个RSU型号，在平台创建RSU型号后由平台分配获得，获取方法可参见 [创建RSU型号](https://support.huaweicloud.com/api-v2x/v2x_04_0020.html)。  **取值范围**：长度不低于1不超过36，只允许字母、数字、连接符（-）的组合。  **该字段仅供使用MQTT协议RSU设备的用户输入。使用websocket协议RSU设备的用户需忽略此字段。** 

        :return: The rsu_model_id of this BatchShowRsusRequest.
        :rtype: str
        """
        return self._rsu_model_id

    @rsu_model_id.setter
    def rsu_model_id(self, rsu_model_id):
        r"""Sets the rsu_model_id of this BatchShowRsusRequest.

        **参数说明**：RSU型号ID，用于唯一标识一个RSU型号，在平台创建RSU型号后由平台分配获得，获取方法可参见 [创建RSU型号](https://support.huaweicloud.com/api-v2x/v2x_04_0020.html)。  **取值范围**：长度不低于1不超过36，只允许字母、数字、连接符（-）的组合。  **该字段仅供使用MQTT协议RSU设备的用户输入。使用websocket协议RSU设备的用户需忽略此字段。** 

        :param rsu_model_id: The rsu_model_id of this BatchShowRsusRequest.
        :type rsu_model_id: str
        """
        self._rsu_model_id = rsu_model_id

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
        if not isinstance(other, BatchShowRsusRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
