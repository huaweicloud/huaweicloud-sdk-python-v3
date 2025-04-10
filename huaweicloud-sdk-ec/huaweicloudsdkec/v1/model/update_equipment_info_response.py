# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateEquipmentInfoResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'ieg_id': 'str',
        'esn': 'str',
        'name': 'str',
        'type': 'str',
        'ha_type': 'str',
        'version': 'str',
        'active_at': 'datetime',
        'go_live_at': 'datetime',
        'start_up_at': 'datetime',
        'cloud_access_status': 'str',
        'status': 'str'
    }

    attribute_map = {
        'id': 'id',
        'ieg_id': 'ieg_id',
        'esn': 'esn',
        'name': 'name',
        'type': 'type',
        'ha_type': 'ha_type',
        'version': 'version',
        'active_at': 'active_at',
        'go_live_at': 'go_live_at',
        'start_up_at': 'start_up_at',
        'cloud_access_status': 'cloud_access_status',
        'status': 'status'
    }

    def __init__(self, id=None, ieg_id=None, esn=None, name=None, type=None, ha_type=None, version=None, active_at=None, go_live_at=None, start_up_at=None, cloud_access_status=None, status=None):
        r"""UpdateEquipmentInfoResponse

        The model defined in huaweicloud sdk

        :param id: 智能企业网关设备ID
        :type id: str
        :param ieg_id: 智能企业网关ID
        :type ieg_id: str
        :param esn: esn
        :type esn: str
        :param name: 设备名字
        :type name: str
        :param type: 设备类型
        :type type: str
        :param ha_type: 高可用类型
        :type ha_type: str
        :param version: 设备软件版本
        :type version: str
        :param active_at: 激活时间
        :type active_at: datetime
        :param go_live_at: 上线时间
        :type go_live_at: datetime
        :param start_up_at: 设备启动时间
        :type start_up_at: datetime
        :param cloud_access_status: VPN状态
        :type cloud_access_status: str
        :param status: 状态
        :type status: str
        """
        
        super(UpdateEquipmentInfoResponse, self).__init__()

        self._id = None
        self._ieg_id = None
        self._esn = None
        self._name = None
        self._type = None
        self._ha_type = None
        self._version = None
        self._active_at = None
        self._go_live_at = None
        self._start_up_at = None
        self._cloud_access_status = None
        self._status = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if ieg_id is not None:
            self.ieg_id = ieg_id
        if esn is not None:
            self.esn = esn
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if ha_type is not None:
            self.ha_type = ha_type
        if version is not None:
            self.version = version
        if active_at is not None:
            self.active_at = active_at
        if go_live_at is not None:
            self.go_live_at = go_live_at
        if start_up_at is not None:
            self.start_up_at = start_up_at
        if cloud_access_status is not None:
            self.cloud_access_status = cloud_access_status
        if status is not None:
            self.status = status

    @property
    def id(self):
        r"""Gets the id of this UpdateEquipmentInfoResponse.

        智能企业网关设备ID

        :return: The id of this UpdateEquipmentInfoResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this UpdateEquipmentInfoResponse.

        智能企业网关设备ID

        :param id: The id of this UpdateEquipmentInfoResponse.
        :type id: str
        """
        self._id = id

    @property
    def ieg_id(self):
        r"""Gets the ieg_id of this UpdateEquipmentInfoResponse.

        智能企业网关ID

        :return: The ieg_id of this UpdateEquipmentInfoResponse.
        :rtype: str
        """
        return self._ieg_id

    @ieg_id.setter
    def ieg_id(self, ieg_id):
        r"""Sets the ieg_id of this UpdateEquipmentInfoResponse.

        智能企业网关ID

        :param ieg_id: The ieg_id of this UpdateEquipmentInfoResponse.
        :type ieg_id: str
        """
        self._ieg_id = ieg_id

    @property
    def esn(self):
        r"""Gets the esn of this UpdateEquipmentInfoResponse.

        esn

        :return: The esn of this UpdateEquipmentInfoResponse.
        :rtype: str
        """
        return self._esn

    @esn.setter
    def esn(self, esn):
        r"""Sets the esn of this UpdateEquipmentInfoResponse.

        esn

        :param esn: The esn of this UpdateEquipmentInfoResponse.
        :type esn: str
        """
        self._esn = esn

    @property
    def name(self):
        r"""Gets the name of this UpdateEquipmentInfoResponse.

        设备名字

        :return: The name of this UpdateEquipmentInfoResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateEquipmentInfoResponse.

        设备名字

        :param name: The name of this UpdateEquipmentInfoResponse.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this UpdateEquipmentInfoResponse.

        设备类型

        :return: The type of this UpdateEquipmentInfoResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this UpdateEquipmentInfoResponse.

        设备类型

        :param type: The type of this UpdateEquipmentInfoResponse.
        :type type: str
        """
        self._type = type

    @property
    def ha_type(self):
        r"""Gets the ha_type of this UpdateEquipmentInfoResponse.

        高可用类型

        :return: The ha_type of this UpdateEquipmentInfoResponse.
        :rtype: str
        """
        return self._ha_type

    @ha_type.setter
    def ha_type(self, ha_type):
        r"""Sets the ha_type of this UpdateEquipmentInfoResponse.

        高可用类型

        :param ha_type: The ha_type of this UpdateEquipmentInfoResponse.
        :type ha_type: str
        """
        self._ha_type = ha_type

    @property
    def version(self):
        r"""Gets the version of this UpdateEquipmentInfoResponse.

        设备软件版本

        :return: The version of this UpdateEquipmentInfoResponse.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this UpdateEquipmentInfoResponse.

        设备软件版本

        :param version: The version of this UpdateEquipmentInfoResponse.
        :type version: str
        """
        self._version = version

    @property
    def active_at(self):
        r"""Gets the active_at of this UpdateEquipmentInfoResponse.

        激活时间

        :return: The active_at of this UpdateEquipmentInfoResponse.
        :rtype: datetime
        """
        return self._active_at

    @active_at.setter
    def active_at(self, active_at):
        r"""Sets the active_at of this UpdateEquipmentInfoResponse.

        激活时间

        :param active_at: The active_at of this UpdateEquipmentInfoResponse.
        :type active_at: datetime
        """
        self._active_at = active_at

    @property
    def go_live_at(self):
        r"""Gets the go_live_at of this UpdateEquipmentInfoResponse.

        上线时间

        :return: The go_live_at of this UpdateEquipmentInfoResponse.
        :rtype: datetime
        """
        return self._go_live_at

    @go_live_at.setter
    def go_live_at(self, go_live_at):
        r"""Sets the go_live_at of this UpdateEquipmentInfoResponse.

        上线时间

        :param go_live_at: The go_live_at of this UpdateEquipmentInfoResponse.
        :type go_live_at: datetime
        """
        self._go_live_at = go_live_at

    @property
    def start_up_at(self):
        r"""Gets the start_up_at of this UpdateEquipmentInfoResponse.

        设备启动时间

        :return: The start_up_at of this UpdateEquipmentInfoResponse.
        :rtype: datetime
        """
        return self._start_up_at

    @start_up_at.setter
    def start_up_at(self, start_up_at):
        r"""Sets the start_up_at of this UpdateEquipmentInfoResponse.

        设备启动时间

        :param start_up_at: The start_up_at of this UpdateEquipmentInfoResponse.
        :type start_up_at: datetime
        """
        self._start_up_at = start_up_at

    @property
    def cloud_access_status(self):
        r"""Gets the cloud_access_status of this UpdateEquipmentInfoResponse.

        VPN状态

        :return: The cloud_access_status of this UpdateEquipmentInfoResponse.
        :rtype: str
        """
        return self._cloud_access_status

    @cloud_access_status.setter
    def cloud_access_status(self, cloud_access_status):
        r"""Sets the cloud_access_status of this UpdateEquipmentInfoResponse.

        VPN状态

        :param cloud_access_status: The cloud_access_status of this UpdateEquipmentInfoResponse.
        :type cloud_access_status: str
        """
        self._cloud_access_status = cloud_access_status

    @property
    def status(self):
        r"""Gets the status of this UpdateEquipmentInfoResponse.

        状态

        :return: The status of this UpdateEquipmentInfoResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this UpdateEquipmentInfoResponse.

        状态

        :param status: The status of this UpdateEquipmentInfoResponse.
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
        if not isinstance(other, UpdateEquipmentInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
