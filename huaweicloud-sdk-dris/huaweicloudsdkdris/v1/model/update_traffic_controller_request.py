# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateTrafficControllerRequest:

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
        'traffic_controller_id': 'str',
        'body': 'ModifyTrafficControllerRequestDTO'
    }

    attribute_map = {
        'instance_id': 'Instance-Id',
        'traffic_controller_id': 'traffic_controller_id',
        'body': 'body'
    }

    def __init__(self, instance_id=None, traffic_controller_id=None, body=None):
        """UpdateTrafficControllerRequest

        The model defined in huaweicloud sdk

        :param instance_id: \&quot;**参数说明**：实例ID。dris物理实例的唯一标识。获取方法参见[获取Instance-Id](https://support.huaweicloud.com/api-v2x/v2x_04_0030.html)。  **取值范围**：仅支持数字，小写字母和横杠（-）的组合，长度36。\&quot;
        :type instance_id: str
        :param traffic_controller_id: **参数说明**：信号机设备ID，全局唯一。
        :type traffic_controller_id: str
        :param body: Body of the UpdateTrafficControllerRequest
        :type body: :class:`huaweicloudsdkdris.v1.ModifyTrafficControllerRequestDTO`
        """
        
        

        self._instance_id = None
        self._traffic_controller_id = None
        self._body = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        self.traffic_controller_id = traffic_controller_id
        if body is not None:
            self.body = body

    @property
    def instance_id(self):
        """Gets the instance_id of this UpdateTrafficControllerRequest.

        \"**参数说明**：实例ID。dris物理实例的唯一标识。获取方法参见[获取Instance-Id](https://support.huaweicloud.com/api-v2x/v2x_04_0030.html)。  **取值范围**：仅支持数字，小写字母和横杠（-）的组合，长度36。\"

        :return: The instance_id of this UpdateTrafficControllerRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this UpdateTrafficControllerRequest.

        \"**参数说明**：实例ID。dris物理实例的唯一标识。获取方法参见[获取Instance-Id](https://support.huaweicloud.com/api-v2x/v2x_04_0030.html)。  **取值范围**：仅支持数字，小写字母和横杠（-）的组合，长度36。\"

        :param instance_id: The instance_id of this UpdateTrafficControllerRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def traffic_controller_id(self):
        """Gets the traffic_controller_id of this UpdateTrafficControllerRequest.

        **参数说明**：信号机设备ID，全局唯一。

        :return: The traffic_controller_id of this UpdateTrafficControllerRequest.
        :rtype: str
        """
        return self._traffic_controller_id

    @traffic_controller_id.setter
    def traffic_controller_id(self, traffic_controller_id):
        """Sets the traffic_controller_id of this UpdateTrafficControllerRequest.

        **参数说明**：信号机设备ID，全局唯一。

        :param traffic_controller_id: The traffic_controller_id of this UpdateTrafficControllerRequest.
        :type traffic_controller_id: str
        """
        self._traffic_controller_id = traffic_controller_id

    @property
    def body(self):
        """Gets the body of this UpdateTrafficControllerRequest.

        :return: The body of this UpdateTrafficControllerRequest.
        :rtype: :class:`huaweicloudsdkdris.v1.ModifyTrafficControllerRequestDTO`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateTrafficControllerRequest.

        :param body: The body of this UpdateTrafficControllerRequest.
        :type body: :class:`huaweicloudsdkdris.v1.ModifyTrafficControllerRequestDTO`
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
        if not isinstance(other, UpdateTrafficControllerRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
