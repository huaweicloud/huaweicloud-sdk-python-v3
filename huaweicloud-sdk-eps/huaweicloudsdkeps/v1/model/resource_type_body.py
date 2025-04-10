# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceTypeBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_type': 'str',
        'resource_type_i18n_display_name': 'str',
        'regions': 'list[str]',
        '_global': 'bool'
    }

    attribute_map = {
        'resource_type': 'resource_type',
        'resource_type_i18n_display_name': 'resource_type_i18n_display_name',
        'regions': 'regions',
        '_global': 'global'
    }

    def __init__(self, resource_type=None, resource_type_i18n_display_name=None, regions=None, _global=None):
        r"""ResourceTypeBody

        The model defined in huaweicloud sdk

        :param resource_type: 资源类型名称
        :type resource_type: str
        :param resource_type_i18n_display_name: 资源类型显示名称，可以通过参数中&#39;locale&#39;设置语言
        :type resource_type_i18n_display_name: str
        :param regions: 支持的region列表
        :type regions: list[str]
        :param _global: 是否是全局类型的资源
        :type _global: bool
        """
        
        

        self._resource_type = None
        self._resource_type_i18n_display_name = None
        self._regions = None
        self.__global = None
        self.discriminator = None

        self.resource_type = resource_type
        self.resource_type_i18n_display_name = resource_type_i18n_display_name
        self.regions = regions
        self._global = _global

    @property
    def resource_type(self):
        r"""Gets the resource_type of this ResourceTypeBody.

        资源类型名称

        :return: The resource_type of this ResourceTypeBody.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this ResourceTypeBody.

        资源类型名称

        :param resource_type: The resource_type of this ResourceTypeBody.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def resource_type_i18n_display_name(self):
        r"""Gets the resource_type_i18n_display_name of this ResourceTypeBody.

        资源类型显示名称，可以通过参数中'locale'设置语言

        :return: The resource_type_i18n_display_name of this ResourceTypeBody.
        :rtype: str
        """
        return self._resource_type_i18n_display_name

    @resource_type_i18n_display_name.setter
    def resource_type_i18n_display_name(self, resource_type_i18n_display_name):
        r"""Sets the resource_type_i18n_display_name of this ResourceTypeBody.

        资源类型显示名称，可以通过参数中'locale'设置语言

        :param resource_type_i18n_display_name: The resource_type_i18n_display_name of this ResourceTypeBody.
        :type resource_type_i18n_display_name: str
        """
        self._resource_type_i18n_display_name = resource_type_i18n_display_name

    @property
    def regions(self):
        r"""Gets the regions of this ResourceTypeBody.

        支持的region列表

        :return: The regions of this ResourceTypeBody.
        :rtype: list[str]
        """
        return self._regions

    @regions.setter
    def regions(self, regions):
        r"""Sets the regions of this ResourceTypeBody.

        支持的region列表

        :param regions: The regions of this ResourceTypeBody.
        :type regions: list[str]
        """
        self._regions = regions

    @property
    def _global(self):
        r"""Gets the _global of this ResourceTypeBody.

        是否是全局类型的资源

        :return: The _global of this ResourceTypeBody.
        :rtype: bool
        """
        return self.__global

    @_global.setter
    def _global(self, _global):
        r"""Sets the _global of this ResourceTypeBody.

        是否是全局类型的资源

        :param _global: The _global of this ResourceTypeBody.
        :type _global: bool
        """
        self.__global = _global

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
        if not isinstance(other, ResourceTypeBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
