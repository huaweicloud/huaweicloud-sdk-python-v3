# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CountMultiCloudResourcesRequest:

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
        'type': 'str',
        'resource_id_list': 'list[str]',
        'name_list': 'list[str]',
        'region_id_list': 'list[str]'
    }

    attribute_map = {
        'vendor': 'vendor',
        'type': 'type',
        'resource_id_list': 'resource_id_list',
        'name_list': 'name_list',
        'region_id_list': 'region_id_list'
    }

    def __init__(self, vendor=None, type=None, resource_id_list=None, name_list=None, region_id_list=None):
        r"""CountMultiCloudResourcesRequest

        The model defined in huaweicloud sdk

        :param vendor: **参数解释：** 云厂商类型。 **约束限制：** 不涉及。 **取值范围：** - AWS：亚马逊。 - AZURE：微软。 - ALI：阿里云。 - HCS：Huawei Cloud Stack。 **默认取值：** 不涉及。
        :type vendor: str
        :param type: **参数解释：** 资源类型。 **约束限制：** 不涉及。 **取值范围：** 资源类型较多，根据实际业务选择资源类型、常用资源类型如下： - cloudservers：弹性云服务器。 - servers：裸金属服务器。 - clusters：云容器引擎。 - instances：云数据库。 **默认取值：** 不涉及。
        :type type: str
        :param resource_id_list: **参数解释：** 用户选择的资源id组成的列表。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type resource_id_list: list[str]
        :param name_list: **参数解释：** 资源名称。 **约束限制：** 不涉及。 **取值范围：** 列表，可参考：裸金属服务器BMS。 **默认取值：** 不涉及。
        :type name_list: list[str]
        :param region_id_list: **参数解释：** 关联的区域region的id组成的列表。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type region_id_list: list[str]
        """
        
        

        self._vendor = None
        self._type = None
        self._resource_id_list = None
        self._name_list = None
        self._region_id_list = None
        self.discriminator = None

        self.vendor = vendor
        if type is not None:
            self.type = type
        if resource_id_list is not None:
            self.resource_id_list = resource_id_list
        if name_list is not None:
            self.name_list = name_list
        if region_id_list is not None:
            self.region_id_list = region_id_list

    @property
    def vendor(self):
        r"""Gets the vendor of this CountMultiCloudResourcesRequest.

        **参数解释：** 云厂商类型。 **约束限制：** 不涉及。 **取值范围：** - AWS：亚马逊。 - AZURE：微软。 - ALI：阿里云。 - HCS：Huawei Cloud Stack。 **默认取值：** 不涉及。

        :return: The vendor of this CountMultiCloudResourcesRequest.
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        r"""Sets the vendor of this CountMultiCloudResourcesRequest.

        **参数解释：** 云厂商类型。 **约束限制：** 不涉及。 **取值范围：** - AWS：亚马逊。 - AZURE：微软。 - ALI：阿里云。 - HCS：Huawei Cloud Stack。 **默认取值：** 不涉及。

        :param vendor: The vendor of this CountMultiCloudResourcesRequest.
        :type vendor: str
        """
        self._vendor = vendor

    @property
    def type(self):
        r"""Gets the type of this CountMultiCloudResourcesRequest.

        **参数解释：** 资源类型。 **约束限制：** 不涉及。 **取值范围：** 资源类型较多，根据实际业务选择资源类型、常用资源类型如下： - cloudservers：弹性云服务器。 - servers：裸金属服务器。 - clusters：云容器引擎。 - instances：云数据库。 **默认取值：** 不涉及。

        :return: The type of this CountMultiCloudResourcesRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CountMultiCloudResourcesRequest.

        **参数解释：** 资源类型。 **约束限制：** 不涉及。 **取值范围：** 资源类型较多，根据实际业务选择资源类型、常用资源类型如下： - cloudservers：弹性云服务器。 - servers：裸金属服务器。 - clusters：云容器引擎。 - instances：云数据库。 **默认取值：** 不涉及。

        :param type: The type of this CountMultiCloudResourcesRequest.
        :type type: str
        """
        self._type = type

    @property
    def resource_id_list(self):
        r"""Gets the resource_id_list of this CountMultiCloudResourcesRequest.

        **参数解释：** 用户选择的资源id组成的列表。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The resource_id_list of this CountMultiCloudResourcesRequest.
        :rtype: list[str]
        """
        return self._resource_id_list

    @resource_id_list.setter
    def resource_id_list(self, resource_id_list):
        r"""Sets the resource_id_list of this CountMultiCloudResourcesRequest.

        **参数解释：** 用户选择的资源id组成的列表。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param resource_id_list: The resource_id_list of this CountMultiCloudResourcesRequest.
        :type resource_id_list: list[str]
        """
        self._resource_id_list = resource_id_list

    @property
    def name_list(self):
        r"""Gets the name_list of this CountMultiCloudResourcesRequest.

        **参数解释：** 资源名称。 **约束限制：** 不涉及。 **取值范围：** 列表，可参考：裸金属服务器BMS。 **默认取值：** 不涉及。

        :return: The name_list of this CountMultiCloudResourcesRequest.
        :rtype: list[str]
        """
        return self._name_list

    @name_list.setter
    def name_list(self, name_list):
        r"""Sets the name_list of this CountMultiCloudResourcesRequest.

        **参数解释：** 资源名称。 **约束限制：** 不涉及。 **取值范围：** 列表，可参考：裸金属服务器BMS。 **默认取值：** 不涉及。

        :param name_list: The name_list of this CountMultiCloudResourcesRequest.
        :type name_list: list[str]
        """
        self._name_list = name_list

    @property
    def region_id_list(self):
        r"""Gets the region_id_list of this CountMultiCloudResourcesRequest.

        **参数解释：** 关联的区域region的id组成的列表。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The region_id_list of this CountMultiCloudResourcesRequest.
        :rtype: list[str]
        """
        return self._region_id_list

    @region_id_list.setter
    def region_id_list(self, region_id_list):
        r"""Sets the region_id_list of this CountMultiCloudResourcesRequest.

        **参数解释：** 关联的区域region的id组成的列表。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param region_id_list: The region_id_list of this CountMultiCloudResourcesRequest.
        :type region_id_list: list[str]
        """
        self._region_id_list = region_id_list

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
        if not isinstance(other, CountMultiCloudResourcesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
