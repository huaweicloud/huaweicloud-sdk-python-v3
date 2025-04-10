# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTrackedResourcesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'region_id': 'str',
        'ep_id': 'str',
        'type': 'str',
        'limit': 'int',
        'marker': 'str',
        'id': 'str',
        'name': 'str',
        'tags': 'list[str]',
        'resource_deleted': 'bool'
    }

    attribute_map = {
        'region_id': 'region_id',
        'ep_id': 'ep_id',
        'type': 'type',
        'limit': 'limit',
        'marker': 'marker',
        'id': 'id',
        'name': 'name',
        'tags': 'tags',
        'resource_deleted': 'resource_deleted'
    }

    def __init__(self, region_id=None, ep_id=None, type=None, limit=None, marker=None, id=None, name=None, tags=None, resource_deleted=None):
        r"""ListTrackedResourcesRequest

        The model defined in huaweicloud sdk

        :param region_id: 区域ID
        :type region_id: str
        :param ep_id: 企业项目ID
        :type ep_id: str
        :param type: 资源类型（provider.type）
        :type type: str
        :param limit: 最大的返回数量。
        :type limit: int
        :param marker: 分页参数，通过上一个请求中返回的marker信息作为输入，获取当前页
        :type marker: str
        :param id: 资源ID
        :type id: str
        :param name: 资源名称
        :type name: str
        :param tags: 标签列表
        :type tags: list[str]
        :param resource_deleted: 是否查询已删除的资源。默认为false，不查询已删除的资源
        :type resource_deleted: bool
        """
        
        

        self._region_id = None
        self._ep_id = None
        self._type = None
        self._limit = None
        self._marker = None
        self._id = None
        self._name = None
        self._tags = None
        self._resource_deleted = None
        self.discriminator = None

        if region_id is not None:
            self.region_id = region_id
        if ep_id is not None:
            self.ep_id = ep_id
        if type is not None:
            self.type = type
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if tags is not None:
            self.tags = tags
        if resource_deleted is not None:
            self.resource_deleted = resource_deleted

    @property
    def region_id(self):
        r"""Gets the region_id of this ListTrackedResourcesRequest.

        区域ID

        :return: The region_id of this ListTrackedResourcesRequest.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this ListTrackedResourcesRequest.

        区域ID

        :param region_id: The region_id of this ListTrackedResourcesRequest.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def ep_id(self):
        r"""Gets the ep_id of this ListTrackedResourcesRequest.

        企业项目ID

        :return: The ep_id of this ListTrackedResourcesRequest.
        :rtype: str
        """
        return self._ep_id

    @ep_id.setter
    def ep_id(self, ep_id):
        r"""Sets the ep_id of this ListTrackedResourcesRequest.

        企业项目ID

        :param ep_id: The ep_id of this ListTrackedResourcesRequest.
        :type ep_id: str
        """
        self._ep_id = ep_id

    @property
    def type(self):
        r"""Gets the type of this ListTrackedResourcesRequest.

        资源类型（provider.type）

        :return: The type of this ListTrackedResourcesRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListTrackedResourcesRequest.

        资源类型（provider.type）

        :param type: The type of this ListTrackedResourcesRequest.
        :type type: str
        """
        self._type = type

    @property
    def limit(self):
        r"""Gets the limit of this ListTrackedResourcesRequest.

        最大的返回数量。

        :return: The limit of this ListTrackedResourcesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListTrackedResourcesRequest.

        最大的返回数量。

        :param limit: The limit of this ListTrackedResourcesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListTrackedResourcesRequest.

        分页参数，通过上一个请求中返回的marker信息作为输入，获取当前页

        :return: The marker of this ListTrackedResourcesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListTrackedResourcesRequest.

        分页参数，通过上一个请求中返回的marker信息作为输入，获取当前页

        :param marker: The marker of this ListTrackedResourcesRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def id(self):
        r"""Gets the id of this ListTrackedResourcesRequest.

        资源ID

        :return: The id of this ListTrackedResourcesRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListTrackedResourcesRequest.

        资源ID

        :param id: The id of this ListTrackedResourcesRequest.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ListTrackedResourcesRequest.

        资源名称

        :return: The name of this ListTrackedResourcesRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListTrackedResourcesRequest.

        资源名称

        :param name: The name of this ListTrackedResourcesRequest.
        :type name: str
        """
        self._name = name

    @property
    def tags(self):
        r"""Gets the tags of this ListTrackedResourcesRequest.

        标签列表

        :return: The tags of this ListTrackedResourcesRequest.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ListTrackedResourcesRequest.

        标签列表

        :param tags: The tags of this ListTrackedResourcesRequest.
        :type tags: list[str]
        """
        self._tags = tags

    @property
    def resource_deleted(self):
        r"""Gets the resource_deleted of this ListTrackedResourcesRequest.

        是否查询已删除的资源。默认为false，不查询已删除的资源

        :return: The resource_deleted of this ListTrackedResourcesRequest.
        :rtype: bool
        """
        return self._resource_deleted

    @resource_deleted.setter
    def resource_deleted(self, resource_deleted):
        r"""Sets the resource_deleted of this ListTrackedResourcesRequest.

        是否查询已删除的资源。默认为false，不查询已删除的资源

        :param resource_deleted: The resource_deleted of this ListTrackedResourcesRequest.
        :type resource_deleted: bool
        """
        self._resource_deleted = resource_deleted

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
        if not isinstance(other, ListTrackedResourcesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
