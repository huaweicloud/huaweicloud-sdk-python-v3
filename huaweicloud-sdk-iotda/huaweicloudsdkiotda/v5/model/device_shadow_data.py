# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


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
        r"""DeviceShadowData

        The model defined in huaweicloud sdk

        :param service_id: 设备的服务ID，在设备关联的产品模型中定义。
        :type service_id: str
        :param desired: 
        :type desired: :class:`huaweicloudsdkiotda.v5.DeviceShadowProperties`
        :param reported: 
        :type reported: :class:`huaweicloudsdkiotda.v5.DeviceShadowProperties`
        :param version: 设备影子的版本，携带该参数时平台会校验值必须等于当前影子版本，初始从0开始。
        :type version: int
        """
        
        

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
        r"""Gets the service_id of this DeviceShadowData.

        设备的服务ID，在设备关联的产品模型中定义。

        :return: The service_id of this DeviceShadowData.
        :rtype: str
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        r"""Sets the service_id of this DeviceShadowData.

        设备的服务ID，在设备关联的产品模型中定义。

        :param service_id: The service_id of this DeviceShadowData.
        :type service_id: str
        """
        self._service_id = service_id

    @property
    def desired(self):
        r"""Gets the desired of this DeviceShadowData.

        :return: The desired of this DeviceShadowData.
        :rtype: :class:`huaweicloudsdkiotda.v5.DeviceShadowProperties`
        """
        return self._desired

    @desired.setter
    def desired(self, desired):
        r"""Sets the desired of this DeviceShadowData.

        :param desired: The desired of this DeviceShadowData.
        :type desired: :class:`huaweicloudsdkiotda.v5.DeviceShadowProperties`
        """
        self._desired = desired

    @property
    def reported(self):
        r"""Gets the reported of this DeviceShadowData.

        :return: The reported of this DeviceShadowData.
        :rtype: :class:`huaweicloudsdkiotda.v5.DeviceShadowProperties`
        """
        return self._reported

    @reported.setter
    def reported(self, reported):
        r"""Sets the reported of this DeviceShadowData.

        :param reported: The reported of this DeviceShadowData.
        :type reported: :class:`huaweicloudsdkiotda.v5.DeviceShadowProperties`
        """
        self._reported = reported

    @property
    def version(self):
        r"""Gets the version of this DeviceShadowData.

        设备影子的版本，携带该参数时平台会校验值必须等于当前影子版本，初始从0开始。

        :return: The version of this DeviceShadowData.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this DeviceShadowData.

        设备影子的版本，携带该参数时平台会校验值必须等于当前影子版本，初始从0开始。

        :param version: The version of this DeviceShadowData.
        :type version: int
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
        if not isinstance(other, DeviceShadowData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
