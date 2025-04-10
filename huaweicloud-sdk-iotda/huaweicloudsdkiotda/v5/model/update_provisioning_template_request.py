# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateProvisioningTemplateRequest:

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
        'template_id': 'str',
        'body': 'UpdateProvisioningTemplate'
    }

    attribute_map = {
        'instance_id': 'Instance-Id',
        'template_id': 'template_id',
        'body': 'body'
    }

    def __init__(self, instance_id=None, template_id=None, body=None):
        r"""UpdateProvisioningTemplateRequest

        The model defined in huaweicloud sdk

        :param instance_id: **参数说明**：实例ID。物理多租下各实例的唯一标识，建议携带该参数，在使用专业版时必须携带该参数。您可以在IoTDA管理控制台界面，选择左侧导航栏“总览”页签查看当前实例的ID，具体获取方式请参考[[查看实例详情](https://support.huaweicloud.com/usermanual-iothub/iot_01_0079.html#section1)](tag:hws) [[查看实例详情](https://support.huaweicloud.com/intl/zh-cn/usermanual-iothub/iot_01_0079.html#section1)](tag:hws_hk)。
        :type instance_id: str
        :param template_id: 预调配模板ID
        :type template_id: str
        :param body: Body of the UpdateProvisioningTemplateRequest
        :type body: :class:`huaweicloudsdkiotda.v5.UpdateProvisioningTemplate`
        """
        
        

        self._instance_id = None
        self._template_id = None
        self._body = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        self.template_id = template_id
        if body is not None:
            self.body = body

    @property
    def instance_id(self):
        r"""Gets the instance_id of this UpdateProvisioningTemplateRequest.

        **参数说明**：实例ID。物理多租下各实例的唯一标识，建议携带该参数，在使用专业版时必须携带该参数。您可以在IoTDA管理控制台界面，选择左侧导航栏“总览”页签查看当前实例的ID，具体获取方式请参考[[查看实例详情](https://support.huaweicloud.com/usermanual-iothub/iot_01_0079.html#section1)](tag:hws) [[查看实例详情](https://support.huaweicloud.com/intl/zh-cn/usermanual-iothub/iot_01_0079.html#section1)](tag:hws_hk)。

        :return: The instance_id of this UpdateProvisioningTemplateRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this UpdateProvisioningTemplateRequest.

        **参数说明**：实例ID。物理多租下各实例的唯一标识，建议携带该参数，在使用专业版时必须携带该参数。您可以在IoTDA管理控制台界面，选择左侧导航栏“总览”页签查看当前实例的ID，具体获取方式请参考[[查看实例详情](https://support.huaweicloud.com/usermanual-iothub/iot_01_0079.html#section1)](tag:hws) [[查看实例详情](https://support.huaweicloud.com/intl/zh-cn/usermanual-iothub/iot_01_0079.html#section1)](tag:hws_hk)。

        :param instance_id: The instance_id of this UpdateProvisioningTemplateRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def template_id(self):
        r"""Gets the template_id of this UpdateProvisioningTemplateRequest.

        预调配模板ID

        :return: The template_id of this UpdateProvisioningTemplateRequest.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        r"""Sets the template_id of this UpdateProvisioningTemplateRequest.

        预调配模板ID

        :param template_id: The template_id of this UpdateProvisioningTemplateRequest.
        :type template_id: str
        """
        self._template_id = template_id

    @property
    def body(self):
        r"""Gets the body of this UpdateProvisioningTemplateRequest.

        :return: The body of this UpdateProvisioningTemplateRequest.
        :rtype: :class:`huaweicloudsdkiotda.v5.UpdateProvisioningTemplate`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateProvisioningTemplateRequest.

        :param body: The body of this UpdateProvisioningTemplateRequest.
        :type body: :class:`huaweicloudsdkiotda.v5.UpdateProvisioningTemplate`
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
        if not isinstance(other, UpdateProvisioningTemplateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
