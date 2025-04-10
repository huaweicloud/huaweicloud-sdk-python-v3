# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DescribeInstanceAccessControlAttributeConfigurationResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_access_control_attribute_configuration': 'InstanceAccessControlAttributeConfigurationDto',
        'status': 'str',
        'status_reason': 'str'
    }

    attribute_map = {
        'instance_access_control_attribute_configuration': 'instance_access_control_attribute_configuration',
        'status': 'status',
        'status_reason': 'status_reason'
    }

    def __init__(self, instance_access_control_attribute_configuration=None, status=None, status_reason=None):
        r"""DescribeInstanceAccessControlAttributeConfigurationResponse

        The model defined in huaweicloud sdk

        :param instance_access_control_attribute_configuration: 
        :type instance_access_control_attribute_configuration: :class:`huaweicloudsdkidentitycenter.v1.InstanceAccessControlAttributeConfigurationDto`
        :param status: ABAC属性配置的状态
        :type status: str
        :param status_reason: 提供有关指定属性的当前状态的更多详细信息
        :type status_reason: str
        """
        
        super(DescribeInstanceAccessControlAttributeConfigurationResponse, self).__init__()

        self._instance_access_control_attribute_configuration = None
        self._status = None
        self._status_reason = None
        self.discriminator = None

        if instance_access_control_attribute_configuration is not None:
            self.instance_access_control_attribute_configuration = instance_access_control_attribute_configuration
        if status is not None:
            self.status = status
        if status_reason is not None:
            self.status_reason = status_reason

    @property
    def instance_access_control_attribute_configuration(self):
        r"""Gets the instance_access_control_attribute_configuration of this DescribeInstanceAccessControlAttributeConfigurationResponse.

        :return: The instance_access_control_attribute_configuration of this DescribeInstanceAccessControlAttributeConfigurationResponse.
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.InstanceAccessControlAttributeConfigurationDto`
        """
        return self._instance_access_control_attribute_configuration

    @instance_access_control_attribute_configuration.setter
    def instance_access_control_attribute_configuration(self, instance_access_control_attribute_configuration):
        r"""Sets the instance_access_control_attribute_configuration of this DescribeInstanceAccessControlAttributeConfigurationResponse.

        :param instance_access_control_attribute_configuration: The instance_access_control_attribute_configuration of this DescribeInstanceAccessControlAttributeConfigurationResponse.
        :type instance_access_control_attribute_configuration: :class:`huaweicloudsdkidentitycenter.v1.InstanceAccessControlAttributeConfigurationDto`
        """
        self._instance_access_control_attribute_configuration = instance_access_control_attribute_configuration

    @property
    def status(self):
        r"""Gets the status of this DescribeInstanceAccessControlAttributeConfigurationResponse.

        ABAC属性配置的状态

        :return: The status of this DescribeInstanceAccessControlAttributeConfigurationResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this DescribeInstanceAccessControlAttributeConfigurationResponse.

        ABAC属性配置的状态

        :param status: The status of this DescribeInstanceAccessControlAttributeConfigurationResponse.
        :type status: str
        """
        self._status = status

    @property
    def status_reason(self):
        r"""Gets the status_reason of this DescribeInstanceAccessControlAttributeConfigurationResponse.

        提供有关指定属性的当前状态的更多详细信息

        :return: The status_reason of this DescribeInstanceAccessControlAttributeConfigurationResponse.
        :rtype: str
        """
        return self._status_reason

    @status_reason.setter
    def status_reason(self, status_reason):
        r"""Sets the status_reason of this DescribeInstanceAccessControlAttributeConfigurationResponse.

        提供有关指定属性的当前状态的更多详细信息

        :param status_reason: The status_reason of this DescribeInstanceAccessControlAttributeConfigurationResponse.
        :type status_reason: str
        """
        self._status_reason = status_reason

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
        if not isinstance(other, DescribeInstanceAccessControlAttributeConfigurationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
