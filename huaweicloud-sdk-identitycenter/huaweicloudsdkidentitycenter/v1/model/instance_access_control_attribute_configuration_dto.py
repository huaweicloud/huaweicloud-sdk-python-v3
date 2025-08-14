# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstanceAccessControlAttributeConfigurationDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'access_control_attributes': 'list[AccessControlAttributeDto]'
    }

    attribute_map = {
        'access_control_attributes': 'access_control_attributes'
    }

    def __init__(self, access_control_attributes=None):
        r"""InstanceAccessControlAttributeConfigurationDto

        The model defined in huaweicloud sdk

        :param access_control_attributes: IAM Identity Center实例中ABAC配置的属性
        :type access_control_attributes: list[:class:`huaweicloudsdkidentitycenter.v1.AccessControlAttributeDto`]
        """
        
        

        self._access_control_attributes = None
        self.discriminator = None

        self.access_control_attributes = access_control_attributes

    @property
    def access_control_attributes(self):
        r"""Gets the access_control_attributes of this InstanceAccessControlAttributeConfigurationDto.

        IAM Identity Center实例中ABAC配置的属性

        :return: The access_control_attributes of this InstanceAccessControlAttributeConfigurationDto.
        :rtype: list[:class:`huaweicloudsdkidentitycenter.v1.AccessControlAttributeDto`]
        """
        return self._access_control_attributes

    @access_control_attributes.setter
    def access_control_attributes(self, access_control_attributes):
        r"""Sets the access_control_attributes of this InstanceAccessControlAttributeConfigurationDto.

        IAM Identity Center实例中ABAC配置的属性

        :param access_control_attributes: The access_control_attributes of this InstanceAccessControlAttributeConfigurationDto.
        :type access_control_attributes: list[:class:`huaweicloudsdkidentitycenter.v1.AccessControlAttributeDto`]
        """
        self._access_control_attributes = access_control_attributes

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
        if not isinstance(other, InstanceAccessControlAttributeConfigurationDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
