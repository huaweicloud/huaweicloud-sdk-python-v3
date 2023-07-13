# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SearchDistinctSharedResourcesReqBody:

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
        'marker': 'str',
        'resource_ids': 'list[str]',
        'principal': 'str',
        'resource_region': 'str',
        'resource_urns': 'list[str]',
        'status': 'str',
        'resource_owner': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'marker': 'marker',
        'resource_ids': 'resource_ids',
        'principal': 'principal',
        'resource_region': 'resource_region',
        'resource_urns': 'resource_urns',
        'status': 'status',
        'resource_owner': 'resource_owner'
    }

    def __init__(self, limit=None, marker=None, resource_ids=None, principal=None, resource_region=None, resource_urns=None, status=None, resource_owner=None):
        """SearchDistinctSharedResourcesReqBody

        The model defined in huaweicloud sdk

        :param limit: 分页页面的最大值。
        :type limit: int
        :param marker: 页面标记。
        :type marker: str
        :param resource_ids: 指定资源ID。
        :type resource_ids: list[str]
        :param principal: 指定资源使用者。
        :type principal: str
        :param resource_region: 资源所在的区域。
        :type resource_region: str
        :param resource_urns: 指定资源URN的列表。
        :type resource_urns: list[str]
        :param status: 资源关联的状态。
        :type status: str
        :param resource_owner: 指定资源共享实例的所有者（self或者other-accounts）。
        :type resource_owner: str
        """
        
        

        self._limit = None
        self._marker = None
        self._resource_ids = None
        self._principal = None
        self._resource_region = None
        self._resource_urns = None
        self._status = None
        self._resource_owner = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if resource_ids is not None:
            self.resource_ids = resource_ids
        if principal is not None:
            self.principal = principal
        if resource_region is not None:
            self.resource_region = resource_region
        if resource_urns is not None:
            self.resource_urns = resource_urns
        if status is not None:
            self.status = status
        self.resource_owner = resource_owner

    @property
    def limit(self):
        """Gets the limit of this SearchDistinctSharedResourcesReqBody.

        分页页面的最大值。

        :return: The limit of this SearchDistinctSharedResourcesReqBody.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this SearchDistinctSharedResourcesReqBody.

        分页页面的最大值。

        :param limit: The limit of this SearchDistinctSharedResourcesReqBody.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this SearchDistinctSharedResourcesReqBody.

        页面标记。

        :return: The marker of this SearchDistinctSharedResourcesReqBody.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this SearchDistinctSharedResourcesReqBody.

        页面标记。

        :param marker: The marker of this SearchDistinctSharedResourcesReqBody.
        :type marker: str
        """
        self._marker = marker

    @property
    def resource_ids(self):
        """Gets the resource_ids of this SearchDistinctSharedResourcesReqBody.

        指定资源ID。

        :return: The resource_ids of this SearchDistinctSharedResourcesReqBody.
        :rtype: list[str]
        """
        return self._resource_ids

    @resource_ids.setter
    def resource_ids(self, resource_ids):
        """Sets the resource_ids of this SearchDistinctSharedResourcesReqBody.

        指定资源ID。

        :param resource_ids: The resource_ids of this SearchDistinctSharedResourcesReqBody.
        :type resource_ids: list[str]
        """
        self._resource_ids = resource_ids

    @property
    def principal(self):
        """Gets the principal of this SearchDistinctSharedResourcesReqBody.

        指定资源使用者。

        :return: The principal of this SearchDistinctSharedResourcesReqBody.
        :rtype: str
        """
        return self._principal

    @principal.setter
    def principal(self, principal):
        """Sets the principal of this SearchDistinctSharedResourcesReqBody.

        指定资源使用者。

        :param principal: The principal of this SearchDistinctSharedResourcesReqBody.
        :type principal: str
        """
        self._principal = principal

    @property
    def resource_region(self):
        """Gets the resource_region of this SearchDistinctSharedResourcesReqBody.

        资源所在的区域。

        :return: The resource_region of this SearchDistinctSharedResourcesReqBody.
        :rtype: str
        """
        return self._resource_region

    @resource_region.setter
    def resource_region(self, resource_region):
        """Sets the resource_region of this SearchDistinctSharedResourcesReqBody.

        资源所在的区域。

        :param resource_region: The resource_region of this SearchDistinctSharedResourcesReqBody.
        :type resource_region: str
        """
        self._resource_region = resource_region

    @property
    def resource_urns(self):
        """Gets the resource_urns of this SearchDistinctSharedResourcesReqBody.

        指定资源URN的列表。

        :return: The resource_urns of this SearchDistinctSharedResourcesReqBody.
        :rtype: list[str]
        """
        return self._resource_urns

    @resource_urns.setter
    def resource_urns(self, resource_urns):
        """Sets the resource_urns of this SearchDistinctSharedResourcesReqBody.

        指定资源URN的列表。

        :param resource_urns: The resource_urns of this SearchDistinctSharedResourcesReqBody.
        :type resource_urns: list[str]
        """
        self._resource_urns = resource_urns

    @property
    def status(self):
        """Gets the status of this SearchDistinctSharedResourcesReqBody.

        资源关联的状态。

        :return: The status of this SearchDistinctSharedResourcesReqBody.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SearchDistinctSharedResourcesReqBody.

        资源关联的状态。

        :param status: The status of this SearchDistinctSharedResourcesReqBody.
        :type status: str
        """
        self._status = status

    @property
    def resource_owner(self):
        """Gets the resource_owner of this SearchDistinctSharedResourcesReqBody.

        指定资源共享实例的所有者（self或者other-accounts）。

        :return: The resource_owner of this SearchDistinctSharedResourcesReqBody.
        :rtype: str
        """
        return self._resource_owner

    @resource_owner.setter
    def resource_owner(self, resource_owner):
        """Sets the resource_owner of this SearchDistinctSharedResourcesReqBody.

        指定资源共享实例的所有者（self或者other-accounts）。

        :param resource_owner: The resource_owner of this SearchDistinctSharedResourcesReqBody.
        :type resource_owner: str
        """
        self._resource_owner = resource_owner

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
        if not isinstance(other, SearchDistinctSharedResourcesReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
