# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateDesktopOrderRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enterprise_project_id': 'str',
        'hour_package_resources': 'list[HourPackageResource]',
        'extend_param': 'OrderExtendParam'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'hour_package_resources': 'hour_package_resources',
        'extend_param': 'extend_param'
    }

    def __init__(self, enterprise_project_id=None, hour_package_resources=None, extend_param=None):
        r"""CreateDesktopOrderRequestBody

        The model defined in huaweicloud sdk

        :param enterprise_project_id: 企业项目ID，默认\&quot;0。\&quot;
        :type enterprise_project_id: str
        :param hour_package_resources: 小时包资源。
        :type hour_package_resources: list[:class:`huaweicloudsdkworkspace.v2.HourPackageResource`]
        :param extend_param: 
        :type extend_param: :class:`huaweicloudsdkworkspace.v2.OrderExtendParam`
        """
        
        

        self._enterprise_project_id = None
        self._hour_package_resources = None
        self._extend_param = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.hour_package_resources = hour_package_resources
        if extend_param is not None:
            self.extend_param = extend_param

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this CreateDesktopOrderRequestBody.

        企业项目ID，默认\"0。\"

        :return: The enterprise_project_id of this CreateDesktopOrderRequestBody.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this CreateDesktopOrderRequestBody.

        企业项目ID，默认\"0。\"

        :param enterprise_project_id: The enterprise_project_id of this CreateDesktopOrderRequestBody.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def hour_package_resources(self):
        r"""Gets the hour_package_resources of this CreateDesktopOrderRequestBody.

        小时包资源。

        :return: The hour_package_resources of this CreateDesktopOrderRequestBody.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.HourPackageResource`]
        """
        return self._hour_package_resources

    @hour_package_resources.setter
    def hour_package_resources(self, hour_package_resources):
        r"""Sets the hour_package_resources of this CreateDesktopOrderRequestBody.

        小时包资源。

        :param hour_package_resources: The hour_package_resources of this CreateDesktopOrderRequestBody.
        :type hour_package_resources: list[:class:`huaweicloudsdkworkspace.v2.HourPackageResource`]
        """
        self._hour_package_resources = hour_package_resources

    @property
    def extend_param(self):
        r"""Gets the extend_param of this CreateDesktopOrderRequestBody.

        :return: The extend_param of this CreateDesktopOrderRequestBody.
        :rtype: :class:`huaweicloudsdkworkspace.v2.OrderExtendParam`
        """
        return self._extend_param

    @extend_param.setter
    def extend_param(self, extend_param):
        r"""Sets the extend_param of this CreateDesktopOrderRequestBody.

        :param extend_param: The extend_param of this CreateDesktopOrderRequestBody.
        :type extend_param: :class:`huaweicloudsdkworkspace.v2.OrderExtendParam`
        """
        self._extend_param = extend_param

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
        if not isinstance(other, CreateDesktopOrderRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
