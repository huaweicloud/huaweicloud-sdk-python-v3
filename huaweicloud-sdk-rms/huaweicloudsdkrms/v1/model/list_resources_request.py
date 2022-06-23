# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListResourcesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'provider': 'str',
        'type': 'str',
        'region_id': 'str',
        'ep_id': 'str',
        'tag': 'dict(str, list[str])',
        'limit': 'int',
        'marker': 'str'
    }

    attribute_map = {
        'provider': 'provider',
        'type': 'type',
        'region_id': 'region_id',
        'ep_id': 'ep_id',
        'tag': 'tag',
        'limit': 'limit',
        'marker': 'marker'
    }

    def __init__(self, provider=None, type=None, region_id=None, ep_id=None, tag=None, limit=None, marker=None):
        """ListResourcesRequest

        The model defined in huaweicloud sdk

        :param provider: 云服务名称
        :type provider: str
        :param type: 资源类型名称
        :type type: str
        :param region_id: 区域ID
        :type region_id: str
        :param ep_id: 企业项目ID
        :type ep_id: str
        :param tag: 标签
        :type tag: dict(str, list[str])
        :param limit: 最大的返回数量
        :type limit: int
        :param marker: 分页参数，通过上一个请求中返回的marker信息作为输入，获取当前页
        :type marker: str
        """
        
        

        self._provider = None
        self._type = None
        self._region_id = None
        self._ep_id = None
        self._tag = None
        self._limit = None
        self._marker = None
        self.discriminator = None

        self.provider = provider
        self.type = type
        if region_id is not None:
            self.region_id = region_id
        if ep_id is not None:
            self.ep_id = ep_id
        if tag is not None:
            self.tag = tag
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker

    @property
    def provider(self):
        """Gets the provider of this ListResourcesRequest.

        云服务名称

        :return: The provider of this ListResourcesRequest.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this ListResourcesRequest.

        云服务名称

        :param provider: The provider of this ListResourcesRequest.
        :type provider: str
        """
        self._provider = provider

    @property
    def type(self):
        """Gets the type of this ListResourcesRequest.

        资源类型名称

        :return: The type of this ListResourcesRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListResourcesRequest.

        资源类型名称

        :param type: The type of this ListResourcesRequest.
        :type type: str
        """
        self._type = type

    @property
    def region_id(self):
        """Gets the region_id of this ListResourcesRequest.

        区域ID

        :return: The region_id of this ListResourcesRequest.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this ListResourcesRequest.

        区域ID

        :param region_id: The region_id of this ListResourcesRequest.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def ep_id(self):
        """Gets the ep_id of this ListResourcesRequest.

        企业项目ID

        :return: The ep_id of this ListResourcesRequest.
        :rtype: str
        """
        return self._ep_id

    @ep_id.setter
    def ep_id(self, ep_id):
        """Sets the ep_id of this ListResourcesRequest.

        企业项目ID

        :param ep_id: The ep_id of this ListResourcesRequest.
        :type ep_id: str
        """
        self._ep_id = ep_id

    @property
    def tag(self):
        """Gets the tag of this ListResourcesRequest.

        标签

        :return: The tag of this ListResourcesRequest.
        :rtype: dict(str, list[str])
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this ListResourcesRequest.

        标签

        :param tag: The tag of this ListResourcesRequest.
        :type tag: dict(str, list[str])
        """
        self._tag = tag

    @property
    def limit(self):
        """Gets the limit of this ListResourcesRequest.

        最大的返回数量

        :return: The limit of this ListResourcesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListResourcesRequest.

        最大的返回数量

        :param limit: The limit of this ListResourcesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListResourcesRequest.

        分页参数，通过上一个请求中返回的marker信息作为输入，获取当前页

        :return: The marker of this ListResourcesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListResourcesRequest.

        分页参数，通过上一个请求中返回的marker信息作为输入，获取当前页

        :param marker: The marker of this ListResourcesRequest.
        :type marker: str
        """
        self._marker = marker

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
        if not isinstance(other, ListResourcesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
