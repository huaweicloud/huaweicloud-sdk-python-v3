# coding: utf-8

import pprint
import re

import six





class DeviceShadowData:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'service_id': 'str',
        'desired': 'DeviceShadowProperties',
        'reported': 'DeviceShadowProperties',
        'version': 'int'
    }

    attribute_map = {
        'service_id': 'service_id',
        'desired': 'desired',
        'reported': 'reported',
        'version': 'version'
    }

    def __init__(self, service_id=None, desired=None, reported=None, version=None):
        """DeviceShadowData - a model defined in huaweicloud sdk"""
        
        

        self._service_id = None
        self._desired = None
        self._reported = None
        self._version = None
        self.discriminator = None

        self.service_id = service_id
        if desired is not None:
            self.desired = desired
        if reported is not None:
            self.reported = reported
        if version is not None:
            self.version = version

    @property
    def service_id(self):
        """Gets the service_id of this DeviceShadowData.

        设备的服务ID，在设备关联的产品模型中定义。

        :return: The service_id of this DeviceShadowData.
        :rtype: str
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        """Sets the service_id of this DeviceShadowData.

        设备的服务ID，在设备关联的产品模型中定义。

        :param service_id: The service_id of this DeviceShadowData.
        :type: str
        """
        self._service_id = service_id

    @property
    def desired(self):
        """Gets the desired of this DeviceShadowData.


        :return: The desired of this DeviceShadowData.
        :rtype: DeviceShadowProperties
        """
        return self._desired

    @desired.setter
    def desired(self, desired):
        """Sets the desired of this DeviceShadowData.


        :param desired: The desired of this DeviceShadowData.
        :type: DeviceShadowProperties
        """
        self._desired = desired

    @property
    def reported(self):
        """Gets the reported of this DeviceShadowData.


        :return: The reported of this DeviceShadowData.
        :rtype: DeviceShadowProperties
        """
        return self._reported

    @reported.setter
    def reported(self, reported):
        """Sets the reported of this DeviceShadowData.


        :param reported: The reported of this DeviceShadowData.
        :type: DeviceShadowProperties
        """
        self._reported = reported

    @property
    def version(self):
        """Gets the version of this DeviceShadowData.

        设备影子的版本，携带改参数时平台会校验值必须等于当前影子版本，初始从0开始。

        :return: The version of this DeviceShadowData.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this DeviceShadowData.

        设备影子的版本，携带改参数时平台会校验值必须等于当前影子版本，初始从0开始。

        :param version: The version of this DeviceShadowData.
        :type: int
        """
        self._version = version

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
        if not isinstance(other, DeviceShadowData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
