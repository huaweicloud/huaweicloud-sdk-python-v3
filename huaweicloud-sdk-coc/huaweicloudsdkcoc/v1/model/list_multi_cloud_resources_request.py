# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListMultiCloudResourcesRequest:

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
        'limit': 'int',
        'marker': 'str',
        'resource_id_list': 'list[str]',
        'name_list': 'list[str]',
        'region_id_list': 'list[str]'
    }

    attribute_map = {
        'vendor': 'vendor',
        'type': 'type',
        'limit': 'limit',
        'marker': 'marker',
        'resource_id_list': 'resource_id_list',
        'name_list': 'name_list',
        'region_id_list': 'region_id_list'
    }

    def __init__(self, vendor=None, type=None, limit=None, marker=None, resource_id_list=None, name_list=None, region_id_list=None):
        """ListMultiCloudResourcesRequest

        The model defined in huaweicloud sdk

        :param vendor: 云厂商
        :type vendor: str
        :param type: 资源类型
        :type type: str
        :param limit: 最大的返回数量
        :type limit: int
        :param marker: 分页参数，通过上一个请求中返回的marker信息作为输入，获取当前页
        :type marker: str
        :param resource_id_list: 资源id列表
        :type resource_id_list: list[str]
        :param name_list: 资源名称
        :type name_list: list[str]
        :param region_id_list: region id列表
        :type region_id_list: list[str]
        """
        
        

        self._vendor = None
        self._type = None
        self._limit = None
        self._marker = None
        self._resource_id_list = None
        self._name_list = None
        self._region_id_list = None
        self.discriminator = None

        self.vendor = vendor
        if type is not None:
            self.type = type
        self.limit = limit
        if marker is not None:
            self.marker = marker
        if resource_id_list is not None:
            self.resource_id_list = resource_id_list
        if name_list is not None:
            self.name_list = name_list
        if region_id_list is not None:
            self.region_id_list = region_id_list

    @property
    def vendor(self):
        """Gets the vendor of this ListMultiCloudResourcesRequest.

        云厂商

        :return: The vendor of this ListMultiCloudResourcesRequest.
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """Sets the vendor of this ListMultiCloudResourcesRequest.

        云厂商

        :param vendor: The vendor of this ListMultiCloudResourcesRequest.
        :type vendor: str
        """
        self._vendor = vendor

    @property
    def type(self):
        """Gets the type of this ListMultiCloudResourcesRequest.

        资源类型

        :return: The type of this ListMultiCloudResourcesRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListMultiCloudResourcesRequest.

        资源类型

        :param type: The type of this ListMultiCloudResourcesRequest.
        :type type: str
        """
        self._type = type

    @property
    def limit(self):
        """Gets the limit of this ListMultiCloudResourcesRequest.

        最大的返回数量

        :return: The limit of this ListMultiCloudResourcesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListMultiCloudResourcesRequest.

        最大的返回数量

        :param limit: The limit of this ListMultiCloudResourcesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListMultiCloudResourcesRequest.

        分页参数，通过上一个请求中返回的marker信息作为输入，获取当前页

        :return: The marker of this ListMultiCloudResourcesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListMultiCloudResourcesRequest.

        分页参数，通过上一个请求中返回的marker信息作为输入，获取当前页

        :param marker: The marker of this ListMultiCloudResourcesRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def resource_id_list(self):
        """Gets the resource_id_list of this ListMultiCloudResourcesRequest.

        资源id列表

        :return: The resource_id_list of this ListMultiCloudResourcesRequest.
        :rtype: list[str]
        """
        return self._resource_id_list

    @resource_id_list.setter
    def resource_id_list(self, resource_id_list):
        """Sets the resource_id_list of this ListMultiCloudResourcesRequest.

        资源id列表

        :param resource_id_list: The resource_id_list of this ListMultiCloudResourcesRequest.
        :type resource_id_list: list[str]
        """
        self._resource_id_list = resource_id_list

    @property
    def name_list(self):
        """Gets the name_list of this ListMultiCloudResourcesRequest.

        资源名称

        :return: The name_list of this ListMultiCloudResourcesRequest.
        :rtype: list[str]
        """
        return self._name_list

    @name_list.setter
    def name_list(self, name_list):
        """Sets the name_list of this ListMultiCloudResourcesRequest.

        资源名称

        :param name_list: The name_list of this ListMultiCloudResourcesRequest.
        :type name_list: list[str]
        """
        self._name_list = name_list

    @property
    def region_id_list(self):
        """Gets the region_id_list of this ListMultiCloudResourcesRequest.

        region id列表

        :return: The region_id_list of this ListMultiCloudResourcesRequest.
        :rtype: list[str]
        """
        return self._region_id_list

    @region_id_list.setter
    def region_id_list(self, region_id_list):
        """Sets the region_id_list of this ListMultiCloudResourcesRequest.

        region id列表

        :param region_id_list: The region_id_list of this ListMultiCloudResourcesRequest.
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
        if not isinstance(other, ListMultiCloudResourcesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
