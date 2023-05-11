# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SearchResourceSharesReqBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'name': 'str',
        'marker': 'str',
        'permission_id': 'str',
        'resource_owner': 'str',
        'resource_share_ids': 'list[str]',
        'resource_share_status': 'str',
        'tag_filters': 'list[TagFilter]'
    }

    attribute_map = {
        'limit': 'limit',
        'name': 'name',
        'marker': 'marker',
        'permission_id': 'permission_id',
        'resource_owner': 'resource_owner',
        'resource_share_ids': 'resource_share_ids',
        'resource_share_status': 'resource_share_status',
        'tag_filters': 'tag_filters'
    }

    def __init__(self, limit=None, name=None, marker=None, permission_id=None, resource_owner=None, resource_share_ids=None, resource_share_status=None, tag_filters=None):
        """SearchResourceSharesReqBody

        The model defined in huaweicloud sdk

        :param limit: 分页页面的最大值。
        :type limit: int
        :param name: 资源共享实例名称。
        :type name: str
        :param marker: 页面标记。
        :type marker: str
        :param permission_id: 权限ID。
        :type permission_id: str
        :param resource_owner: 检索您创建的或共享给您的（self或者other-accounts）资源共享实例。
        :type resource_owner: str
        :param resource_share_ids: 资源共享实例的ID列表。
        :type resource_share_ids: list[str]
        :param resource_share_status: 资源共享实例的状态。
        :type resource_share_status: str
        :param tag_filters: 资源共享实例的标签。
        :type tag_filters: list[:class:`huaweicloudsdkram.v1.TagFilter`]
        """
        
        

        self._limit = None
        self._name = None
        self._marker = None
        self._permission_id = None
        self._resource_owner = None
        self._resource_share_ids = None
        self._resource_share_status = None
        self._tag_filters = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if name is not None:
            self.name = name
        if marker is not None:
            self.marker = marker
        if permission_id is not None:
            self.permission_id = permission_id
        self.resource_owner = resource_owner
        if resource_share_ids is not None:
            self.resource_share_ids = resource_share_ids
        if resource_share_status is not None:
            self.resource_share_status = resource_share_status
        if tag_filters is not None:
            self.tag_filters = tag_filters

    @property
    def limit(self):
        """Gets the limit of this SearchResourceSharesReqBody.

        分页页面的最大值。

        :return: The limit of this SearchResourceSharesReqBody.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this SearchResourceSharesReqBody.

        分页页面的最大值。

        :param limit: The limit of this SearchResourceSharesReqBody.
        :type limit: int
        """
        self._limit = limit

    @property
    def name(self):
        """Gets the name of this SearchResourceSharesReqBody.

        资源共享实例名称。

        :return: The name of this SearchResourceSharesReqBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SearchResourceSharesReqBody.

        资源共享实例名称。

        :param name: The name of this SearchResourceSharesReqBody.
        :type name: str
        """
        self._name = name

    @property
    def marker(self):
        """Gets the marker of this SearchResourceSharesReqBody.

        页面标记。

        :return: The marker of this SearchResourceSharesReqBody.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this SearchResourceSharesReqBody.

        页面标记。

        :param marker: The marker of this SearchResourceSharesReqBody.
        :type marker: str
        """
        self._marker = marker

    @property
    def permission_id(self):
        """Gets the permission_id of this SearchResourceSharesReqBody.

        权限ID。

        :return: The permission_id of this SearchResourceSharesReqBody.
        :rtype: str
        """
        return self._permission_id

    @permission_id.setter
    def permission_id(self, permission_id):
        """Sets the permission_id of this SearchResourceSharesReqBody.

        权限ID。

        :param permission_id: The permission_id of this SearchResourceSharesReqBody.
        :type permission_id: str
        """
        self._permission_id = permission_id

    @property
    def resource_owner(self):
        """Gets the resource_owner of this SearchResourceSharesReqBody.

        检索您创建的或共享给您的（self或者other-accounts）资源共享实例。

        :return: The resource_owner of this SearchResourceSharesReqBody.
        :rtype: str
        """
        return self._resource_owner

    @resource_owner.setter
    def resource_owner(self, resource_owner):
        """Sets the resource_owner of this SearchResourceSharesReqBody.

        检索您创建的或共享给您的（self或者other-accounts）资源共享实例。

        :param resource_owner: The resource_owner of this SearchResourceSharesReqBody.
        :type resource_owner: str
        """
        self._resource_owner = resource_owner

    @property
    def resource_share_ids(self):
        """Gets the resource_share_ids of this SearchResourceSharesReqBody.

        资源共享实例的ID列表。

        :return: The resource_share_ids of this SearchResourceSharesReqBody.
        :rtype: list[str]
        """
        return self._resource_share_ids

    @resource_share_ids.setter
    def resource_share_ids(self, resource_share_ids):
        """Sets the resource_share_ids of this SearchResourceSharesReqBody.

        资源共享实例的ID列表。

        :param resource_share_ids: The resource_share_ids of this SearchResourceSharesReqBody.
        :type resource_share_ids: list[str]
        """
        self._resource_share_ids = resource_share_ids

    @property
    def resource_share_status(self):
        """Gets the resource_share_status of this SearchResourceSharesReqBody.

        资源共享实例的状态。

        :return: The resource_share_status of this SearchResourceSharesReqBody.
        :rtype: str
        """
        return self._resource_share_status

    @resource_share_status.setter
    def resource_share_status(self, resource_share_status):
        """Sets the resource_share_status of this SearchResourceSharesReqBody.

        资源共享实例的状态。

        :param resource_share_status: The resource_share_status of this SearchResourceSharesReqBody.
        :type resource_share_status: str
        """
        self._resource_share_status = resource_share_status

    @property
    def tag_filters(self):
        """Gets the tag_filters of this SearchResourceSharesReqBody.

        资源共享实例的标签。

        :return: The tag_filters of this SearchResourceSharesReqBody.
        :rtype: list[:class:`huaweicloudsdkram.v1.TagFilter`]
        """
        return self._tag_filters

    @tag_filters.setter
    def tag_filters(self, tag_filters):
        """Sets the tag_filters of this SearchResourceSharesReqBody.

        资源共享实例的标签。

        :param tag_filters: The tag_filters of this SearchResourceSharesReqBody.
        :type tag_filters: list[:class:`huaweicloudsdkram.v1.TagFilter`]
        """
        self._tag_filters = tag_filters

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
        if not isinstance(other, SearchResourceSharesReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
