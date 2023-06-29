# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VolumeTypeInfo:

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
        'name': 'list[dict(str, str)]',
        'volume_type_extra_specs': 'VolumeTypeExtraSpecs'
    }

    attribute_map = {
        'resource_spec_code': 'resource_spec_code',
        'volume_type': 'volume_type',
        'volume_product_type': 'volume_product_type',
        'resource_type': 'resource_type',
        'cloud_service_type': 'cloud_service_type',
        'name': 'name',
        'volume_type_extra_specs': 'volume_type_extra_specs'
    }

    def __init__(self, resource_spec_code=None, volume_type=None, volume_product_type=None, resource_type=None, cloud_service_type=None, name=None, volume_type_extra_specs=None):
        """VolumeTypeInfo

        The model defined in huaweicloud sdk

        :param resource_spec_code: 资源规格编码
        :type resource_spec_code: str
        :param volume_type: 磁盘类型
        :type volume_type: str
        :param volume_product_type: 磁盘产品类型
        :type volume_product_type: str
        :param resource_type: 资源类型字段
        :type resource_type: str
        :param cloud_service_type: 资源所属云服务类型编码
        :type cloud_service_type: str
        :param name: 磁盘中英文名称
        :type name: list[dict(str, str)]
        :param volume_type_extra_specs: 
        :type volume_type_extra_specs: :class:`huaweicloudsdkworkspaceapp.v1.VolumeTypeExtraSpecs`
        """
        
        

        self._resource_spec_code = None
        self._volume_type = None
        self._volume_product_type = None
        self._resource_type = None
        self._cloud_service_type = None
        self._name = None
        self._volume_type_extra_specs = None
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
        if name is not None:
            self.name = name
        if volume_type_extra_specs is not None:
            self.volume_type_extra_specs = volume_type_extra_specs

    @property
    def resource_spec_code(self):
        """Gets the resource_spec_code of this VolumeTypeInfo.

        资源规格编码

        :return: The resource_spec_code of this VolumeTypeInfo.
        :rtype: str
        """
        return self._resource_spec_code

    @resource_spec_code.setter
    def resource_spec_code(self, resource_spec_code):
        """Sets the resource_spec_code of this VolumeTypeInfo.

        资源规格编码

        :param resource_spec_code: The resource_spec_code of this VolumeTypeInfo.
        :type resource_spec_code: str
        """
        self._resource_spec_code = resource_spec_code

    @property
    def volume_type(self):
        """Gets the volume_type of this VolumeTypeInfo.

        磁盘类型

        :return: The volume_type of this VolumeTypeInfo.
        :rtype: str
        """
        return self._volume_type

    @volume_type.setter
    def volume_type(self, volume_type):
        """Sets the volume_type of this VolumeTypeInfo.

        磁盘类型

        :param volume_type: The volume_type of this VolumeTypeInfo.
        :type volume_type: str
        """
        self._volume_type = volume_type

    @property
    def volume_product_type(self):
        """Gets the volume_product_type of this VolumeTypeInfo.

        磁盘产品类型

        :return: The volume_product_type of this VolumeTypeInfo.
        :rtype: str
        """
        return self._volume_product_type

    @volume_product_type.setter
    def volume_product_type(self, volume_product_type):
        """Sets the volume_product_type of this VolumeTypeInfo.

        磁盘产品类型

        :param volume_product_type: The volume_product_type of this VolumeTypeInfo.
        :type volume_product_type: str
        """
        self._volume_product_type = volume_product_type

    @property
    def resource_type(self):
        """Gets the resource_type of this VolumeTypeInfo.

        资源类型字段

        :return: The resource_type of this VolumeTypeInfo.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this VolumeTypeInfo.

        资源类型字段

        :param resource_type: The resource_type of this VolumeTypeInfo.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def cloud_service_type(self):
        """Gets the cloud_service_type of this VolumeTypeInfo.

        资源所属云服务类型编码

        :return: The cloud_service_type of this VolumeTypeInfo.
        :rtype: str
        """
        return self._cloud_service_type

    @cloud_service_type.setter
    def cloud_service_type(self, cloud_service_type):
        """Sets the cloud_service_type of this VolumeTypeInfo.

        资源所属云服务类型编码

        :param cloud_service_type: The cloud_service_type of this VolumeTypeInfo.
        :type cloud_service_type: str
        """
        self._cloud_service_type = cloud_service_type

    @property
    def name(self):
        """Gets the name of this VolumeTypeInfo.

        磁盘中英文名称

        :return: The name of this VolumeTypeInfo.
        :rtype: list[dict(str, str)]
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VolumeTypeInfo.

        磁盘中英文名称

        :param name: The name of this VolumeTypeInfo.
        :type name: list[dict(str, str)]
        """
        self._name = name

    @property
    def volume_type_extra_specs(self):
        """Gets the volume_type_extra_specs of this VolumeTypeInfo.

        :return: The volume_type_extra_specs of this VolumeTypeInfo.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.VolumeTypeExtraSpecs`
        """
        return self._volume_type_extra_specs

    @volume_type_extra_specs.setter
    def volume_type_extra_specs(self, volume_type_extra_specs):
        """Sets the volume_type_extra_specs of this VolumeTypeInfo.

        :param volume_type_extra_specs: The volume_type_extra_specs of this VolumeTypeInfo.
        :type volume_type_extra_specs: :class:`huaweicloudsdkworkspaceapp.v1.VolumeTypeExtraSpecs`
        """
        self._volume_type_extra_specs = volume_type_extra_specs

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
        if not isinstance(other, VolumeTypeInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
