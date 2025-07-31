# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateAccountPasswordRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vendor': 'str',
        'resource_provider': 'str',
        'resource_type': 'str',
        'instance_type': 'str',
        'password_change_result': 'list[UpdateAccountPassword]'
    }

    attribute_map = {
        'vendor': 'vendor',
        'resource_provider': 'resource_provider',
        'resource_type': 'resource_type',
        'instance_type': 'instance_type',
        'password_change_result': 'password_change_result'
    }

    def __init__(self, vendor=None, resource_provider=None, resource_type=None, instance_type=None, password_change_result=None):
        r"""UpdateAccountPasswordRequestBody

        The model defined in huaweicloud sdk

        :param vendor: 云服务厂商
        :type vendor: str
        :param resource_provider: 云服务
        :type resource_provider: str
        :param resource_type: 资源类型
        :type resource_type: str
        :param instance_type: 实例类型
        :type instance_type: str
        :param password_change_result: 改密结果
        :type password_change_result: list[:class:`huaweicloudsdkcoc.v1.UpdateAccountPassword`]
        """
        
        

        self._vendor = None
        self._resource_provider = None
        self._resource_type = None
        self._instance_type = None
        self._password_change_result = None
        self.discriminator = None

        self.vendor = vendor
        self.resource_provider = resource_provider
        self.resource_type = resource_type
        self.instance_type = instance_type
        self.password_change_result = password_change_result

    @property
    def vendor(self):
        r"""Gets the vendor of this UpdateAccountPasswordRequestBody.

        云服务厂商

        :return: The vendor of this UpdateAccountPasswordRequestBody.
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        r"""Sets the vendor of this UpdateAccountPasswordRequestBody.

        云服务厂商

        :param vendor: The vendor of this UpdateAccountPasswordRequestBody.
        :type vendor: str
        """
        self._vendor = vendor

    @property
    def resource_provider(self):
        r"""Gets the resource_provider of this UpdateAccountPasswordRequestBody.

        云服务

        :return: The resource_provider of this UpdateAccountPasswordRequestBody.
        :rtype: str
        """
        return self._resource_provider

    @resource_provider.setter
    def resource_provider(self, resource_provider):
        r"""Sets the resource_provider of this UpdateAccountPasswordRequestBody.

        云服务

        :param resource_provider: The resource_provider of this UpdateAccountPasswordRequestBody.
        :type resource_provider: str
        """
        self._resource_provider = resource_provider

    @property
    def resource_type(self):
        r"""Gets the resource_type of this UpdateAccountPasswordRequestBody.

        资源类型

        :return: The resource_type of this UpdateAccountPasswordRequestBody.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this UpdateAccountPasswordRequestBody.

        资源类型

        :param resource_type: The resource_type of this UpdateAccountPasswordRequestBody.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def instance_type(self):
        r"""Gets the instance_type of this UpdateAccountPasswordRequestBody.

        实例类型

        :return: The instance_type of this UpdateAccountPasswordRequestBody.
        :rtype: str
        """
        return self._instance_type

    @instance_type.setter
    def instance_type(self, instance_type):
        r"""Sets the instance_type of this UpdateAccountPasswordRequestBody.

        实例类型

        :param instance_type: The instance_type of this UpdateAccountPasswordRequestBody.
        :type instance_type: str
        """
        self._instance_type = instance_type

    @property
    def password_change_result(self):
        r"""Gets the password_change_result of this UpdateAccountPasswordRequestBody.

        改密结果

        :return: The password_change_result of this UpdateAccountPasswordRequestBody.
        :rtype: list[:class:`huaweicloudsdkcoc.v1.UpdateAccountPassword`]
        """
        return self._password_change_result

    @password_change_result.setter
    def password_change_result(self, password_change_result):
        r"""Sets the password_change_result of this UpdateAccountPasswordRequestBody.

        改密结果

        :param password_change_result: The password_change_result of this UpdateAccountPasswordRequestBody.
        :type password_change_result: list[:class:`huaweicloudsdkcoc.v1.UpdateAccountPassword`]
        """
        self._password_change_result = password_change_result

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
        if not isinstance(other, UpdateAccountPasswordRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
