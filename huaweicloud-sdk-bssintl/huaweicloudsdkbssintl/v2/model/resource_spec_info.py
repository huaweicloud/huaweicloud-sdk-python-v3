# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceSpecInfo:

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
        'cloud_service_type_name': 'str',
        'resource_type': 'str',
        'resource_type_name': 'str',
        'resource_spec': 'str',
        'resource_spec_name': 'str',
        'attributes': 'list[Attribute]',
        'price_lists': 'list[PriceItem]'
    }

    attribute_map = {
        'cloud_service_type': 'cloud_service_type',
        'cloud_service_type_name': 'cloud_service_type_name',
        'resource_type': 'resource_type',
        'resource_type_name': 'resource_type_name',
        'resource_spec': 'resource_spec',
        'resource_spec_name': 'resource_spec_name',
        'attributes': 'attributes',
        'price_lists': 'price_lists'
    }

    def __init__(self, cloud_service_type=None, cloud_service_type_name=None, resource_type=None, resource_type_name=None, resource_spec=None, resource_spec_name=None, attributes=None, price_lists=None):
        r"""ResourceSpecInfo

        The model defined in huaweicloud sdk

        :param cloud_service_type: 云服务类型编码
        :type cloud_service_type: str
        :param cloud_service_type_name: 云服务类型名称
        :type cloud_service_type_name: str
        :param resource_type: 资源类型编码
        :type resource_type: str
        :param resource_type_name: 资源类型名称
        :type resource_type_name: str
        :param resource_spec: 云服务类型的资源规格编码
        :type resource_spec: str
        :param resource_spec_name: 云服务类型的资源规格名称
        :type resource_spec_name: str
        :param attributes: 属性列表，need_attributes&#x3D;true时返回属性信息。
        :type attributes: list[:class:`huaweicloudsdkbssintl.v2.Attribute`]
        :param price_lists: 定价列表，need_price&#x3D;true时返回定价信息。
        :type price_lists: list[:class:`huaweicloudsdkbssintl.v2.PriceItem`]
        """
        
        

        self._cloud_service_type = None
        self._cloud_service_type_name = None
        self._resource_type = None
        self._resource_type_name = None
        self._resource_spec = None
        self._resource_spec_name = None
        self._attributes = None
        self._price_lists = None
        self.discriminator = None

        if cloud_service_type is not None:
            self.cloud_service_type = cloud_service_type
        if cloud_service_type_name is not None:
            self.cloud_service_type_name = cloud_service_type_name
        if resource_type is not None:
            self.resource_type = resource_type
        if resource_type_name is not None:
            self.resource_type_name = resource_type_name
        if resource_spec is not None:
            self.resource_spec = resource_spec
        if resource_spec_name is not None:
            self.resource_spec_name = resource_spec_name
        if attributes is not None:
            self.attributes = attributes
        if price_lists is not None:
            self.price_lists = price_lists

    @property
    def cloud_service_type(self):
        r"""Gets the cloud_service_type of this ResourceSpecInfo.

        云服务类型编码

        :return: The cloud_service_type of this ResourceSpecInfo.
        :rtype: str
        """
        return self._cloud_service_type

    @cloud_service_type.setter
    def cloud_service_type(self, cloud_service_type):
        r"""Sets the cloud_service_type of this ResourceSpecInfo.

        云服务类型编码

        :param cloud_service_type: The cloud_service_type of this ResourceSpecInfo.
        :type cloud_service_type: str
        """
        self._cloud_service_type = cloud_service_type

    @property
    def cloud_service_type_name(self):
        r"""Gets the cloud_service_type_name of this ResourceSpecInfo.

        云服务类型名称

        :return: The cloud_service_type_name of this ResourceSpecInfo.
        :rtype: str
        """
        return self._cloud_service_type_name

    @cloud_service_type_name.setter
    def cloud_service_type_name(self, cloud_service_type_name):
        r"""Sets the cloud_service_type_name of this ResourceSpecInfo.

        云服务类型名称

        :param cloud_service_type_name: The cloud_service_type_name of this ResourceSpecInfo.
        :type cloud_service_type_name: str
        """
        self._cloud_service_type_name = cloud_service_type_name

    @property
    def resource_type(self):
        r"""Gets the resource_type of this ResourceSpecInfo.

        资源类型编码

        :return: The resource_type of this ResourceSpecInfo.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this ResourceSpecInfo.

        资源类型编码

        :param resource_type: The resource_type of this ResourceSpecInfo.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def resource_type_name(self):
        r"""Gets the resource_type_name of this ResourceSpecInfo.

        资源类型名称

        :return: The resource_type_name of this ResourceSpecInfo.
        :rtype: str
        """
        return self._resource_type_name

    @resource_type_name.setter
    def resource_type_name(self, resource_type_name):
        r"""Sets the resource_type_name of this ResourceSpecInfo.

        资源类型名称

        :param resource_type_name: The resource_type_name of this ResourceSpecInfo.
        :type resource_type_name: str
        """
        self._resource_type_name = resource_type_name

    @property
    def resource_spec(self):
        r"""Gets the resource_spec of this ResourceSpecInfo.

        云服务类型的资源规格编码

        :return: The resource_spec of this ResourceSpecInfo.
        :rtype: str
        """
        return self._resource_spec

    @resource_spec.setter
    def resource_spec(self, resource_spec):
        r"""Sets the resource_spec of this ResourceSpecInfo.

        云服务类型的资源规格编码

        :param resource_spec: The resource_spec of this ResourceSpecInfo.
        :type resource_spec: str
        """
        self._resource_spec = resource_spec

    @property
    def resource_spec_name(self):
        r"""Gets the resource_spec_name of this ResourceSpecInfo.

        云服务类型的资源规格名称

        :return: The resource_spec_name of this ResourceSpecInfo.
        :rtype: str
        """
        return self._resource_spec_name

    @resource_spec_name.setter
    def resource_spec_name(self, resource_spec_name):
        r"""Sets the resource_spec_name of this ResourceSpecInfo.

        云服务类型的资源规格名称

        :param resource_spec_name: The resource_spec_name of this ResourceSpecInfo.
        :type resource_spec_name: str
        """
        self._resource_spec_name = resource_spec_name

    @property
    def attributes(self):
        r"""Gets the attributes of this ResourceSpecInfo.

        属性列表，need_attributes=true时返回属性信息。

        :return: The attributes of this ResourceSpecInfo.
        :rtype: list[:class:`huaweicloudsdkbssintl.v2.Attribute`]
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        r"""Sets the attributes of this ResourceSpecInfo.

        属性列表，need_attributes=true时返回属性信息。

        :param attributes: The attributes of this ResourceSpecInfo.
        :type attributes: list[:class:`huaweicloudsdkbssintl.v2.Attribute`]
        """
        self._attributes = attributes

    @property
    def price_lists(self):
        r"""Gets the price_lists of this ResourceSpecInfo.

        定价列表，need_price=true时返回定价信息。

        :return: The price_lists of this ResourceSpecInfo.
        :rtype: list[:class:`huaweicloudsdkbssintl.v2.PriceItem`]
        """
        return self._price_lists

    @price_lists.setter
    def price_lists(self, price_lists):
        r"""Sets the price_lists of this ResourceSpecInfo.

        定价列表，need_price=true时返回定价信息。

        :param price_lists: The price_lists of this ResourceSpecInfo.
        :type price_lists: list[:class:`huaweicloudsdkbssintl.v2.PriceItem`]
        """
        self._price_lists = price_lists

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ResourceSpecInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
