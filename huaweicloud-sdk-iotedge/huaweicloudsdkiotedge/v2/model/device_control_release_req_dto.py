# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeviceControlReleaseReqDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'control_id': 'str',
        'service_id': 'str',
        'priority': 'int',
        'properties': 'list[str]'
    }

    attribute_map = {
        'control_id': 'control_id',
        'service_id': 'service_id',
        'priority': 'priority',
        'properties': 'properties'
    }

    def __init__(self, control_id=None, service_id=None, priority=None, properties=None):
        r"""DeviceControlReleaseReqDTO

        The model defined in huaweicloud sdk

        :param control_id: 控制id
        :type control_id: str
        :param service_id: 服务id，可选
        :type service_id: str
        :param priority: 调度计划优先级。
        :type priority: int
        :param properties: 控制释放的属性数组
        :type properties: list[str]
        """
        
        

        self._control_id = None
        self._service_id = None
        self._priority = None
        self._properties = None
        self.discriminator = None

        self.control_id = control_id
        if service_id is not None:
            self.service_id = service_id
        self.priority = priority
        self.properties = properties

    @property
    def control_id(self):
        r"""Gets the control_id of this DeviceControlReleaseReqDTO.

        控制id

        :return: The control_id of this DeviceControlReleaseReqDTO.
        :rtype: str
        """
        return self._control_id

    @control_id.setter
    def control_id(self, control_id):
        r"""Sets the control_id of this DeviceControlReleaseReqDTO.

        控制id

        :param control_id: The control_id of this DeviceControlReleaseReqDTO.
        :type control_id: str
        """
        self._control_id = control_id

    @property
    def service_id(self):
        r"""Gets the service_id of this DeviceControlReleaseReqDTO.

        服务id，可选

        :return: The service_id of this DeviceControlReleaseReqDTO.
        :rtype: str
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        r"""Sets the service_id of this DeviceControlReleaseReqDTO.

        服务id，可选

        :param service_id: The service_id of this DeviceControlReleaseReqDTO.
        :type service_id: str
        """
        self._service_id = service_id

    @property
    def priority(self):
        r"""Gets the priority of this DeviceControlReleaseReqDTO.

        调度计划优先级。

        :return: The priority of this DeviceControlReleaseReqDTO.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        r"""Sets the priority of this DeviceControlReleaseReqDTO.

        调度计划优先级。

        :param priority: The priority of this DeviceControlReleaseReqDTO.
        :type priority: int
        """
        self._priority = priority

    @property
    def properties(self):
        r"""Gets the properties of this DeviceControlReleaseReqDTO.

        控制释放的属性数组

        :return: The properties of this DeviceControlReleaseReqDTO.
        :rtype: list[str]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        r"""Sets the properties of this DeviceControlReleaseReqDTO.

        控制释放的属性数组

        :param properties: The properties of this DeviceControlReleaseReqDTO.
        :type properties: list[str]
        """
        self._properties = properties

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
        if not isinstance(other, DeviceControlReleaseReqDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
