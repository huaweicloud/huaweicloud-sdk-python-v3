# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VolumeProductInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_spec_code': 'str',
        'volume_type': 'str',
        'volume_product_type': 'str',
        'resource_type': 'str',
        'cloud_service_type': 'str',
        'domain_ids': 'list[str]',
        'name': 'list[I18nLanguage]',
        'status': 'str'
    }

    attribute_map = {
        'resource_spec_code': 'resource_spec_code',
        'volume_type': 'volume_type',
        'volume_product_type': 'volume_product_type',
        'resource_type': 'resource_type',
        'cloud_service_type': 'cloud_service_type',
        'domain_ids': 'domain_ids',
        'name': 'name',
        'status': 'status'
    }

    def __init__(self, resource_spec_code=None, volume_type=None, volume_product_type=None, resource_type=None, cloud_service_type=None, domain_ids=None, name=None, status=None):
        r"""VolumeProductInfo

        The model defined in huaweicloud sdk

        :param resource_spec_code: 产品ID。
        :type resource_spec_code: str
        :param volume_type: 磁盘类型： - SATA: 普通IO磁盘 - SAS：高IO磁盘 - SSD：超高IO磁盘
        :type volume_type: str
        :param volume_product_type: 产品类型：workspace。
        :type volume_product_type: str
        :param resource_type: 资源类型。
        :type resource_type: str
        :param cloud_service_type: 云服务类型。
        :type cloud_service_type: str
        :param domain_ids: 该磁盘支持的专有域id（domainId）。
        :type domain_ids: list[str]
        :param name: 磁盘名称。
        :type name: list[:class:`huaweicloudsdkworkspace.v2.I18nLanguage`]
        :param status: 产品状态，normal：正常、sellout：售空。
        :type status: str
        """
        
        

        self._resource_spec_code = None
        self._volume_type = None
        self._volume_product_type = None
        self._resource_type = None
        self._cloud_service_type = None
        self._domain_ids = None
        self._name = None
        self._status = None
        self.discriminator = None

        if resource_spec_code is not None:
            self.resource_spec_code = resource_spec_code
        if volume_type is not None:
            self.volume_type = volume_type
        if volume_product_type is not None:
            self.volume_product_type = volume_product_type
        if resource_type is not None:
            self.resource_type = resource_type
        if cloud_service_type is not None:
            self.cloud_service_type = cloud_service_type
        if domain_ids is not None:
            self.domain_ids = domain_ids
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status

    @property
    def resource_spec_code(self):
        r"""Gets the resource_spec_code of this VolumeProductInfo.

        产品ID。

        :return: The resource_spec_code of this VolumeProductInfo.
        :rtype: str
        """
        return self._resource_spec_code

    @resource_spec_code.setter
    def resource_spec_code(self, resource_spec_code):
        r"""Sets the resource_spec_code of this VolumeProductInfo.

        产品ID。

        :param resource_spec_code: The resource_spec_code of this VolumeProductInfo.
        :type resource_spec_code: str
        """
        self._resource_spec_code = resource_spec_code

    @property
    def volume_type(self):
        r"""Gets the volume_type of this VolumeProductInfo.

        磁盘类型： - SATA: 普通IO磁盘 - SAS：高IO磁盘 - SSD：超高IO磁盘

        :return: The volume_type of this VolumeProductInfo.
        :rtype: str
        """
        return self._volume_type

    @volume_type.setter
    def volume_type(self, volume_type):
        r"""Sets the volume_type of this VolumeProductInfo.

        磁盘类型： - SATA: 普通IO磁盘 - SAS：高IO磁盘 - SSD：超高IO磁盘

        :param volume_type: The volume_type of this VolumeProductInfo.
        :type volume_type: str
        """
        self._volume_type = volume_type

    @property
    def volume_product_type(self):
        r"""Gets the volume_product_type of this VolumeProductInfo.

        产品类型：workspace。

        :return: The volume_product_type of this VolumeProductInfo.
        :rtype: str
        """
        return self._volume_product_type

    @volume_product_type.setter
    def volume_product_type(self, volume_product_type):
        r"""Sets the volume_product_type of this VolumeProductInfo.

        产品类型：workspace。

        :param volume_product_type: The volume_product_type of this VolumeProductInfo.
        :type volume_product_type: str
        """
        self._volume_product_type = volume_product_type

    @property
    def resource_type(self):
        r"""Gets the resource_type of this VolumeProductInfo.

        资源类型。

        :return: The resource_type of this VolumeProductInfo.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this VolumeProductInfo.

        资源类型。

        :param resource_type: The resource_type of this VolumeProductInfo.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def cloud_service_type(self):
        r"""Gets the cloud_service_type of this VolumeProductInfo.

        云服务类型。

        :return: The cloud_service_type of this VolumeProductInfo.
        :rtype: str
        """
        return self._cloud_service_type

    @cloud_service_type.setter
    def cloud_service_type(self, cloud_service_type):
        r"""Sets the cloud_service_type of this VolumeProductInfo.

        云服务类型。

        :param cloud_service_type: The cloud_service_type of this VolumeProductInfo.
        :type cloud_service_type: str
        """
        self._cloud_service_type = cloud_service_type

    @property
    def domain_ids(self):
        r"""Gets the domain_ids of this VolumeProductInfo.

        该磁盘支持的专有域id（domainId）。

        :return: The domain_ids of this VolumeProductInfo.
        :rtype: list[str]
        """
        return self._domain_ids

    @domain_ids.setter
    def domain_ids(self, domain_ids):
        r"""Sets the domain_ids of this VolumeProductInfo.

        该磁盘支持的专有域id（domainId）。

        :param domain_ids: The domain_ids of this VolumeProductInfo.
        :type domain_ids: list[str]
        """
        self._domain_ids = domain_ids

    @property
    def name(self):
        r"""Gets the name of this VolumeProductInfo.

        磁盘名称。

        :return: The name of this VolumeProductInfo.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.I18nLanguage`]
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this VolumeProductInfo.

        磁盘名称。

        :param name: The name of this VolumeProductInfo.
        :type name: list[:class:`huaweicloudsdkworkspace.v2.I18nLanguage`]
        """
        self._name = name

    @property
    def status(self):
        r"""Gets the status of this VolumeProductInfo.

        产品状态，normal：正常、sellout：售空。

        :return: The status of this VolumeProductInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this VolumeProductInfo.

        产品状态，normal：正常、sellout：售空。

        :param status: The status of this VolumeProductInfo.
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
        if not isinstance(other, VolumeProductInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
