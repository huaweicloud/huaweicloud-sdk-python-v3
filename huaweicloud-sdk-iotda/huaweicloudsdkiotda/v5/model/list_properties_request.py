# coding: utf-8

import pprint
import re

import six





class ListPropertiesRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []
    sensitive_list.append('stage_auth_token')

    openapi_types = {
        'device_id': 'str',
        'stage_auth_token': 'str',
        'instance_id': 'str',
        'service_id': 'str'
    }

    attribute_map = {
        'device_id': 'device_id',
        'stage_auth_token': 'Stage-Auth-Token',
        'instance_id': 'Instance-Id',
        'service_id': 'service_id'
    }

    def __init__(self, device_id=None, stage_auth_token=None, instance_id=None, service_id=None):
        """ListPropertiesRequest - a model defined in huaweicloud sdk"""
        
        

        self._device_id = None
        self._stage_auth_token = None
        self._instance_id = None
        self._service_id = None
        self.discriminator = None

        self.device_id = device_id
        if stage_auth_token is not None:
            self.stage_auth_token = stage_auth_token
        if instance_id is not None:
            self.instance_id = instance_id
        self.service_id = service_id

    @property
    def device_id(self):
        """Gets the device_id of this ListPropertiesRequest.

        下发属性的设备ID，用于唯一标识一个设备，在注册设备时由物联网平台分配获得。

        :return: The device_id of this ListPropertiesRequest.
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this ListPropertiesRequest.

        下发属性的设备ID，用于唯一标识一个设备，在注册设备时由物联网平台分配获得。

        :param device_id: The device_id of this ListPropertiesRequest.
        :type: str
        """
        self._device_id = device_id

    @property
    def stage_auth_token(self):
        """Gets the stage_auth_token of this ListPropertiesRequest.

        Stage用户的Token, 仅提供给IoStage服务使用

        :return: The stage_auth_token of this ListPropertiesRequest.
        :rtype: str
        """
        return self._stage_auth_token

    @stage_auth_token.setter
    def stage_auth_token(self, stage_auth_token):
        """Sets the stage_auth_token of this ListPropertiesRequest.

        Stage用户的Token, 仅提供给IoStage服务使用

        :param stage_auth_token: The stage_auth_token of this ListPropertiesRequest.
        :type: str
        """
        self._stage_auth_token = stage_auth_token

    @property
    def instance_id(self):
        """Gets the instance_id of this ListPropertiesRequest.

        实例ID。物理多租下各实例的唯一标识，一般华为云租户无需携带该参数，仅在物理多租场景下从管理面访问API时需要携带该参数。

        :return: The instance_id of this ListPropertiesRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListPropertiesRequest.

        实例ID。物理多租下各实例的唯一标识，一般华为云租户无需携带该参数，仅在物理多租场景下从管理面访问API时需要携带该参数。

        :param instance_id: The instance_id of this ListPropertiesRequest.
        :type: str
        """
        self._instance_id = instance_id

    @property
    def service_id(self):
        """Gets the service_id of this ListPropertiesRequest.

        设备的服务ID，在设备关联的产品模型中定义。

        :return: The service_id of this ListPropertiesRequest.
        :rtype: str
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        """Sets the service_id of this ListPropertiesRequest.

        设备的服务ID，在设备关联的产品模型中定义。

        :param service_id: The service_id of this ListPropertiesRequest.
        :type: str
        """
        self._service_id = service_id

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListPropertiesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
