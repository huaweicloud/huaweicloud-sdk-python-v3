# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListHourPackagesTypeRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'desktop_resource_spec_code': 'str',
        'resource_spec_code': 'str'
    }

    attribute_map = {
        'desktop_resource_spec_code': 'desktop_resource_spec_code',
        'resource_spec_code': 'resource_spec_code'
    }

    def __init__(self, desktop_resource_spec_code=None, resource_spec_code=None):
        r"""ListHourPackagesTypeRequest

        The model defined in huaweicloud sdk

        :param desktop_resource_spec_code: 小时包对应的按需桌面的资源规格编码。
        :type desktop_resource_spec_code: str
        :param resource_spec_code: 小时包的资源规格编码。
        :type resource_spec_code: str
        """
        
        

        self._desktop_resource_spec_code = None
        self._resource_spec_code = None
        self.discriminator = None

        if desktop_resource_spec_code is not None:
            self.desktop_resource_spec_code = desktop_resource_spec_code
        if resource_spec_code is not None:
            self.resource_spec_code = resource_spec_code

    @property
    def desktop_resource_spec_code(self):
        r"""Gets the desktop_resource_spec_code of this ListHourPackagesTypeRequest.

        小时包对应的按需桌面的资源规格编码。

        :return: The desktop_resource_spec_code of this ListHourPackagesTypeRequest.
        :rtype: str
        """
        return self._desktop_resource_spec_code

    @desktop_resource_spec_code.setter
    def desktop_resource_spec_code(self, desktop_resource_spec_code):
        r"""Sets the desktop_resource_spec_code of this ListHourPackagesTypeRequest.

        小时包对应的按需桌面的资源规格编码。

        :param desktop_resource_spec_code: The desktop_resource_spec_code of this ListHourPackagesTypeRequest.
        :type desktop_resource_spec_code: str
        """
        self._desktop_resource_spec_code = desktop_resource_spec_code

    @property
    def resource_spec_code(self):
        r"""Gets the resource_spec_code of this ListHourPackagesTypeRequest.

        小时包的资源规格编码。

        :return: The resource_spec_code of this ListHourPackagesTypeRequest.
        :rtype: str
        """
        return self._resource_spec_code

    @resource_spec_code.setter
    def resource_spec_code(self, resource_spec_code):
        r"""Sets the resource_spec_code of this ListHourPackagesTypeRequest.

        小时包的资源规格编码。

        :param resource_spec_code: The resource_spec_code of this ListHourPackagesTypeRequest.
        :type resource_spec_code: str
        """
        self._resource_spec_code = resource_spec_code

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
        if not isinstance(other, ListHourPackagesTypeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
