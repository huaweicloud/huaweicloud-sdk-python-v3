# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddHarmonySoftBusResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'bus_id': 'str',
        'bus_name': 'str',
        'group_id': 'str',
        'app_id': 'str',
        'status': 'str'
    }

    attribute_map = {
        'bus_id': 'bus_id',
        'bus_name': 'bus_name',
        'group_id': 'group_id',
        'app_id': 'app_id',
        'status': 'status'
    }

    def __init__(self, bus_id=None, bus_name=None, group_id=None, app_id=None, status=None):
        r"""AddHarmonySoftBusResponse

        The model defined in huaweicloud sdk

        :param bus_id: 鸿蒙软总线ID，用于唯一标识一个鸿蒙软总线，在创建鸿蒙软总线时由物联网平台分配。
        :type bus_id: str
        :param bus_name: 鸿蒙软总线名称，单个资源空间下不可重复。
        :type bus_name: str
        :param group_id: 设备组ID。
        :type group_id: str
        :param app_id: **参数说明**：资源空间ID。此参数为非必选参数，存在多资源空间的用户需要使用该接口时，建议携带该参数指定创建的设备组归属到哪个资源空间下，否则创建的设备组将会归属到[默认资源空间](https://support.huaweicloud.com/usermanual-iothub/iot_01_0006.html#section0)下。 **取值范围**：长度不超过36，只允许字母、数字、下划线（_）、连接符（-）的组合。
        :type app_id: str
        :param status: 鸿蒙软总线组信息同步状态，结果范围：Synchronized，Synchronizing，ToBeSynchronized - Synchronized：已同步。 - Synchronizing：同步中。 - ToBeSynchronized：待同步。 
        :type status: str
        """
        
        super(AddHarmonySoftBusResponse, self).__init__()

        self._bus_id = None
        self._bus_name = None
        self._group_id = None
        self._app_id = None
        self._status = None
        self.discriminator = None

        if bus_id is not None:
            self.bus_id = bus_id
        if bus_name is not None:
            self.bus_name = bus_name
        if group_id is not None:
            self.group_id = group_id
        if app_id is not None:
            self.app_id = app_id
        if status is not None:
            self.status = status

    @property
    def bus_id(self):
        r"""Gets the bus_id of this AddHarmonySoftBusResponse.

        鸿蒙软总线ID，用于唯一标识一个鸿蒙软总线，在创建鸿蒙软总线时由物联网平台分配。

        :return: The bus_id of this AddHarmonySoftBusResponse.
        :rtype: str
        """
        return self._bus_id

    @bus_id.setter
    def bus_id(self, bus_id):
        r"""Sets the bus_id of this AddHarmonySoftBusResponse.

        鸿蒙软总线ID，用于唯一标识一个鸿蒙软总线，在创建鸿蒙软总线时由物联网平台分配。

        :param bus_id: The bus_id of this AddHarmonySoftBusResponse.
        :type bus_id: str
        """
        self._bus_id = bus_id

    @property
    def bus_name(self):
        r"""Gets the bus_name of this AddHarmonySoftBusResponse.

        鸿蒙软总线名称，单个资源空间下不可重复。

        :return: The bus_name of this AddHarmonySoftBusResponse.
        :rtype: str
        """
        return self._bus_name

    @bus_name.setter
    def bus_name(self, bus_name):
        r"""Sets the bus_name of this AddHarmonySoftBusResponse.

        鸿蒙软总线名称，单个资源空间下不可重复。

        :param bus_name: The bus_name of this AddHarmonySoftBusResponse.
        :type bus_name: str
        """
        self._bus_name = bus_name

    @property
    def group_id(self):
        r"""Gets the group_id of this AddHarmonySoftBusResponse.

        设备组ID。

        :return: The group_id of this AddHarmonySoftBusResponse.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this AddHarmonySoftBusResponse.

        设备组ID。

        :param group_id: The group_id of this AddHarmonySoftBusResponse.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def app_id(self):
        r"""Gets the app_id of this AddHarmonySoftBusResponse.

        **参数说明**：资源空间ID。此参数为非必选参数，存在多资源空间的用户需要使用该接口时，建议携带该参数指定创建的设备组归属到哪个资源空间下，否则创建的设备组将会归属到[默认资源空间](https://support.huaweicloud.com/usermanual-iothub/iot_01_0006.html#section0)下。 **取值范围**：长度不超过36，只允许字母、数字、下划线（_）、连接符（-）的组合。

        :return: The app_id of this AddHarmonySoftBusResponse.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        r"""Sets the app_id of this AddHarmonySoftBusResponse.

        **参数说明**：资源空间ID。此参数为非必选参数，存在多资源空间的用户需要使用该接口时，建议携带该参数指定创建的设备组归属到哪个资源空间下，否则创建的设备组将会归属到[默认资源空间](https://support.huaweicloud.com/usermanual-iothub/iot_01_0006.html#section0)下。 **取值范围**：长度不超过36，只允许字母、数字、下划线（_）、连接符（-）的组合。

        :param app_id: The app_id of this AddHarmonySoftBusResponse.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def status(self):
        r"""Gets the status of this AddHarmonySoftBusResponse.

        鸿蒙软总线组信息同步状态，结果范围：Synchronized，Synchronizing，ToBeSynchronized - Synchronized：已同步。 - Synchronizing：同步中。 - ToBeSynchronized：待同步。 

        :return: The status of this AddHarmonySoftBusResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this AddHarmonySoftBusResponse.

        鸿蒙软总线组信息同步状态，结果范围：Synchronized，Synchronizing，ToBeSynchronized - Synchronized：已同步。 - Synchronizing：同步中。 - ToBeSynchronized：待同步。 

        :param status: The status of this AddHarmonySoftBusResponse.
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
        if not isinstance(other, AddHarmonySoftBusResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
