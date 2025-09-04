# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateDeviceCertificateRequest:

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
        'certificate_id': 'str',
        'body': 'UpdateDeviceCertificate'
    }

    attribute_map = {
        'instance_id': 'Instance-Id',
        'certificate_id': 'certificate_id',
        'body': 'body'
    }

    def __init__(self, instance_id=None, certificate_id=None, body=None):
        r"""UpdateDeviceCertificateRequest

        The model defined in huaweicloud sdk

        :param instance_id: **参数说明**：实例ID。物理多租下各实例的唯一标识，建议携带该参数，在使用专业版时必须携带该参数。您可以在IoTDA管理控制台界面，选择左侧导航栏“总览”页签查看当前实例的ID，具体获取方式请参考[[查看实例详情](https://support.huaweicloud.com/usermanual-iothub/iot_01_0121.html)](tag:hws) [[查看实例详情](https://support.huaweicloud.com/intl/zh-cn/usermanual-iothub/iot_01_0121.html)](tag:hws_hk)。
        :type instance_id: str
        :param certificate_id: **参数说明**：设备证书ID，用于唯一标识一个设备证书。在注册设备证书时由物联网平台分配获得。
        :type certificate_id: str
        :param body: Body of the UpdateDeviceCertificateRequest
        :type body: :class:`huaweicloudsdkiotda.v5.UpdateDeviceCertificate`
        """
        
        

        self._instance_id = None
        self._certificate_id = None
        self._body = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        self.certificate_id = certificate_id
        if body is not None:
            self.body = body

    @property
    def instance_id(self):
        r"""Gets the instance_id of this UpdateDeviceCertificateRequest.

        **参数说明**：实例ID。物理多租下各实例的唯一标识，建议携带该参数，在使用专业版时必须携带该参数。您可以在IoTDA管理控制台界面，选择左侧导航栏“总览”页签查看当前实例的ID，具体获取方式请参考[[查看实例详情](https://support.huaweicloud.com/usermanual-iothub/iot_01_0121.html)](tag:hws) [[查看实例详情](https://support.huaweicloud.com/intl/zh-cn/usermanual-iothub/iot_01_0121.html)](tag:hws_hk)。

        :return: The instance_id of this UpdateDeviceCertificateRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this UpdateDeviceCertificateRequest.

        **参数说明**：实例ID。物理多租下各实例的唯一标识，建议携带该参数，在使用专业版时必须携带该参数。您可以在IoTDA管理控制台界面，选择左侧导航栏“总览”页签查看当前实例的ID，具体获取方式请参考[[查看实例详情](https://support.huaweicloud.com/usermanual-iothub/iot_01_0121.html)](tag:hws) [[查看实例详情](https://support.huaweicloud.com/intl/zh-cn/usermanual-iothub/iot_01_0121.html)](tag:hws_hk)。

        :param instance_id: The instance_id of this UpdateDeviceCertificateRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def certificate_id(self):
        r"""Gets the certificate_id of this UpdateDeviceCertificateRequest.

        **参数说明**：设备证书ID，用于唯一标识一个设备证书。在注册设备证书时由物联网平台分配获得。

        :return: The certificate_id of this UpdateDeviceCertificateRequest.
        :rtype: str
        """
        return self._certificate_id

    @certificate_id.setter
    def certificate_id(self, certificate_id):
        r"""Sets the certificate_id of this UpdateDeviceCertificateRequest.

        **参数说明**：设备证书ID，用于唯一标识一个设备证书。在注册设备证书时由物联网平台分配获得。

        :param certificate_id: The certificate_id of this UpdateDeviceCertificateRequest.
        :type certificate_id: str
        """
        self._certificate_id = certificate_id

    @property
    def body(self):
        r"""Gets the body of this UpdateDeviceCertificateRequest.

        :return: The body of this UpdateDeviceCertificateRequest.
        :rtype: :class:`huaweicloudsdkiotda.v5.UpdateDeviceCertificate`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateDeviceCertificateRequest.

        :param body: The body of this UpdateDeviceCertificateRequest.
        :type body: :class:`huaweicloudsdkiotda.v5.UpdateDeviceCertificate`
        """
        self._body = body

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
        if not isinstance(other, UpdateDeviceCertificateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
