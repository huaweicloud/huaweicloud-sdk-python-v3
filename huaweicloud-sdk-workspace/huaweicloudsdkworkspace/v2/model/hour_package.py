# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HourPackage:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cloud_service_type': 'str',
        'resource_type': 'str',
        'resource_spec_code': 'str',
        'desktop_resource_spec_code': 'str',
        'descriptions': 'ResourcePackageDescription',
        'package_duration': 'int',
        'domain_ids': 'list[str]',
        'status': 'str'
    }

    attribute_map = {
        'cloud_service_type': 'cloud_service_type',
        'resource_type': 'resource_type',
        'resource_spec_code': 'resource_spec_code',
        'desktop_resource_spec_code': 'desktop_resource_spec_code',
        'descriptions': 'descriptions',
        'package_duration': 'package_duration',
        'domain_ids': 'domain_ids',
        'status': 'status'
    }

    def __init__(self, cloud_service_type=None, resource_type=None, resource_spec_code=None, desktop_resource_spec_code=None, descriptions=None, package_duration=None, domain_ids=None, status=None):
        r"""HourPackage

        The model defined in huaweicloud sdk

        :param cloud_service_type: 资源所属云服务类型编码。
        :type cloud_service_type: str
        :param resource_type: 资源类型。
        :type resource_type: str
        :param resource_spec_code: 小时包的资源规格编码。
        :type resource_spec_code: str
        :param desktop_resource_spec_code: 小时包对应的按需桌面的资源规格编码。
        :type desktop_resource_spec_code: str
        :param descriptions: 
        :type descriptions: :class:`huaweicloudsdkworkspace.v2.ResourcePackageDescription`
        :param package_duration: 套餐可使用时长，单位：小时。
        :type package_duration: int
        :param domain_ids: 该产品套餐支持的专有域id（domainId）。
        :type domain_ids: list[str]
        :param status: 产品状态，normal：正常、sellout：售空、abandon：下线。
        :type status: str
        """
        
        

        self._cloud_service_type = None
        self._resource_type = None
        self._resource_spec_code = None
        self._desktop_resource_spec_code = None
        self._descriptions = None
        self._package_duration = None
        self._domain_ids = None
        self._status = None
        self.discriminator = None

        if cloud_service_type is not None:
            self.cloud_service_type = cloud_service_type
        if resource_type is not None:
            self.resource_type = resource_type
        if resource_spec_code is not None:
            self.resource_spec_code = resource_spec_code
        if desktop_resource_spec_code is not None:
            self.desktop_resource_spec_code = desktop_resource_spec_code
        if descriptions is not None:
            self.descriptions = descriptions
        if package_duration is not None:
            self.package_duration = package_duration
        if domain_ids is not None:
            self.domain_ids = domain_ids
        if status is not None:
            self.status = status

    @property
    def cloud_service_type(self):
        r"""Gets the cloud_service_type of this HourPackage.

        资源所属云服务类型编码。

        :return: The cloud_service_type of this HourPackage.
        :rtype: str
        """
        return self._cloud_service_type

    @cloud_service_type.setter
    def cloud_service_type(self, cloud_service_type):
        r"""Sets the cloud_service_type of this HourPackage.

        资源所属云服务类型编码。

        :param cloud_service_type: The cloud_service_type of this HourPackage.
        :type cloud_service_type: str
        """
        self._cloud_service_type = cloud_service_type

    @property
    def resource_type(self):
        r"""Gets the resource_type of this HourPackage.

        资源类型。

        :return: The resource_type of this HourPackage.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this HourPackage.

        资源类型。

        :param resource_type: The resource_type of this HourPackage.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def resource_spec_code(self):
        r"""Gets the resource_spec_code of this HourPackage.

        小时包的资源规格编码。

        :return: The resource_spec_code of this HourPackage.
        :rtype: str
        """
        return self._resource_spec_code

    @resource_spec_code.setter
    def resource_spec_code(self, resource_spec_code):
        r"""Sets the resource_spec_code of this HourPackage.

        小时包的资源规格编码。

        :param resource_spec_code: The resource_spec_code of this HourPackage.
        :type resource_spec_code: str
        """
        self._resource_spec_code = resource_spec_code

    @property
    def desktop_resource_spec_code(self):
        r"""Gets the desktop_resource_spec_code of this HourPackage.

        小时包对应的按需桌面的资源规格编码。

        :return: The desktop_resource_spec_code of this HourPackage.
        :rtype: str
        """
        return self._desktop_resource_spec_code

    @desktop_resource_spec_code.setter
    def desktop_resource_spec_code(self, desktop_resource_spec_code):
        r"""Sets the desktop_resource_spec_code of this HourPackage.

        小时包对应的按需桌面的资源规格编码。

        :param desktop_resource_spec_code: The desktop_resource_spec_code of this HourPackage.
        :type desktop_resource_spec_code: str
        """
        self._desktop_resource_spec_code = desktop_resource_spec_code

    @property
    def descriptions(self):
        r"""Gets the descriptions of this HourPackage.

        :return: The descriptions of this HourPackage.
        :rtype: :class:`huaweicloudsdkworkspace.v2.ResourcePackageDescription`
        """
        return self._descriptions

    @descriptions.setter
    def descriptions(self, descriptions):
        r"""Sets the descriptions of this HourPackage.

        :param descriptions: The descriptions of this HourPackage.
        :type descriptions: :class:`huaweicloudsdkworkspace.v2.ResourcePackageDescription`
        """
        self._descriptions = descriptions

    @property
    def package_duration(self):
        r"""Gets the package_duration of this HourPackage.

        套餐可使用时长，单位：小时。

        :return: The package_duration of this HourPackage.
        :rtype: int
        """
        return self._package_duration

    @package_duration.setter
    def package_duration(self, package_duration):
        r"""Sets the package_duration of this HourPackage.

        套餐可使用时长，单位：小时。

        :param package_duration: The package_duration of this HourPackage.
        :type package_duration: int
        """
        self._package_duration = package_duration

    @property
    def domain_ids(self):
        r"""Gets the domain_ids of this HourPackage.

        该产品套餐支持的专有域id（domainId）。

        :return: The domain_ids of this HourPackage.
        :rtype: list[str]
        """
        return self._domain_ids

    @domain_ids.setter
    def domain_ids(self, domain_ids):
        r"""Sets the domain_ids of this HourPackage.

        该产品套餐支持的专有域id（domainId）。

        :param domain_ids: The domain_ids of this HourPackage.
        :type domain_ids: list[str]
        """
        self._domain_ids = domain_ids

    @property
    def status(self):
        r"""Gets the status of this HourPackage.

        产品状态，normal：正常、sellout：售空、abandon：下线。

        :return: The status of this HourPackage.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this HourPackage.

        产品状态，normal：正常、sellout：售空、abandon：下线。

        :param status: The status of this HourPackage.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, HourPackage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
