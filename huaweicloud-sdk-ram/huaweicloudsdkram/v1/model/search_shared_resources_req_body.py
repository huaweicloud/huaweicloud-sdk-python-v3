# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SearchSharedResourcesReqBody:

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
        'principal': 'str',
        'resource_ids': 'list[str]',
        'resource_urns': 'list[str]',
        'resource_owner': 'str',
        'resource_share_ids': 'list[str]',
        'resource_region': 'str',
        'resource_type': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'marker': 'marker',
        'principal': 'principal',
        'resource_ids': 'resource_ids',
        'resource_urns': 'resource_urns',
        'resource_owner': 'resource_owner',
        'resource_share_ids': 'resource_share_ids',
        'resource_region': 'resource_region',
        'resource_type': 'resource_type'
    }

    def __init__(self, limit=None, marker=None, principal=None, resource_ids=None, resource_urns=None, resource_owner=None, resource_share_ids=None, resource_region=None, resource_type=None):
        r"""SearchSharedResourcesReqBody

        The model defined in huaweicloud sdk

        :param limit: 分页页面的最大值。
        :type limit: int
        :param marker: 页面标记。
        :type marker: str
        :param principal: 指定资源使用者。
        :type principal: str
        :param resource_ids: 指定资源ID列表。
        :type resource_ids: list[str]
        :param resource_urns: 指定资源URN的列表。
        :type resource_urns: list[str]
        :param resource_owner: 指定资源共享实例的所有者（self或者other-accounts）。
        :type resource_owner: str
        :param resource_share_ids: 指定资源共享实例的ID列表。
        :type resource_share_ids: list[str]
        :param resource_region: 资源所在的区域。
        :type resource_region: str
        :param resource_type: 指定资源类型。
        :type resource_type: str
        """
        
        

        self._limit = None
        self._marker = None
        self._principal = None
        self._resource_ids = None
        self._resource_urns = None
        self._resource_owner = None
        self._resource_share_ids = None
        self._resource_region = None
        self._resource_type = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if principal is not None:
            self.principal = principal
        if resource_ids is not None:
            self.resource_ids = resource_ids
        if resource_urns is not None:
            self.resource_urns = resource_urns
        self.resource_owner = resource_owner
        if resource_share_ids is not None:
            self.resource_share_ids = resource_share_ids
        if resource_region is not None:
            self.resource_region = resource_region
        if resource_type is not None:
            self.resource_type = resource_type

    @property
    def limit(self):
        r"""Gets the limit of this SearchSharedResourcesReqBody.

        分页页面的最大值。

        :return: The limit of this SearchSharedResourcesReqBody.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this SearchSharedResourcesReqBody.

        分页页面的最大值。

        :param limit: The limit of this SearchSharedResourcesReqBody.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this SearchSharedResourcesReqBody.

        页面标记。

        :return: The marker of this SearchSharedResourcesReqBody.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this SearchSharedResourcesReqBody.

        页面标记。

        :param marker: The marker of this SearchSharedResourcesReqBody.
        :type marker: str
        """
        self._marker = marker

    @property
    def principal(self):
        r"""Gets the principal of this SearchSharedResourcesReqBody.

        指定资源使用者。

        :return: The principal of this SearchSharedResourcesReqBody.
        :rtype: str
        """
        return self._principal

    @principal.setter
    def principal(self, principal):
        r"""Sets the principal of this SearchSharedResourcesReqBody.

        指定资源使用者。

        :param principal: The principal of this SearchSharedResourcesReqBody.
        :type principal: str
        """
        self._principal = principal

    @property
    def resource_ids(self):
        r"""Gets the resource_ids of this SearchSharedResourcesReqBody.

        指定资源ID列表。

        :return: The resource_ids of this SearchSharedResourcesReqBody.
        :rtype: list[str]
        """
        return self._resource_ids

    @resource_ids.setter
    def resource_ids(self, resource_ids):
        r"""Sets the resource_ids of this SearchSharedResourcesReqBody.

        指定资源ID列表。

        :param resource_ids: The resource_ids of this SearchSharedResourcesReqBody.
        :type resource_ids: list[str]
        """
        self._resource_ids = resource_ids

    @property
    def resource_urns(self):
        r"""Gets the resource_urns of this SearchSharedResourcesReqBody.

        指定资源URN的列表。

        :return: The resource_urns of this SearchSharedResourcesReqBody.
        :rtype: list[str]
        """
        return self._resource_urns

    @resource_urns.setter
    def resource_urns(self, resource_urns):
        r"""Sets the resource_urns of this SearchSharedResourcesReqBody.

        指定资源URN的列表。

        :param resource_urns: The resource_urns of this SearchSharedResourcesReqBody.
        :type resource_urns: list[str]
        """
        self._resource_urns = resource_urns

    @property
    def resource_owner(self):
        r"""Gets the resource_owner of this SearchSharedResourcesReqBody.

        指定资源共享实例的所有者（self或者other-accounts）。

        :return: The resource_owner of this SearchSharedResourcesReqBody.
        :rtype: str
        """
        return self._resource_owner

    @resource_owner.setter
    def resource_owner(self, resource_owner):
        r"""Sets the resource_owner of this SearchSharedResourcesReqBody.

        指定资源共享实例的所有者（self或者other-accounts）。

        :param resource_owner: The resource_owner of this SearchSharedResourcesReqBody.
        :type resource_owner: str
        """
        self._resource_owner = resource_owner

    @property
    def resource_share_ids(self):
        r"""Gets the resource_share_ids of this SearchSharedResourcesReqBody.

        指定资源共享实例的ID列表。

        :return: The resource_share_ids of this SearchSharedResourcesReqBody.
        :rtype: list[str]
        """
        return self._resource_share_ids

    @resource_share_ids.setter
    def resource_share_ids(self, resource_share_ids):
        r"""Sets the resource_share_ids of this SearchSharedResourcesReqBody.

        指定资源共享实例的ID列表。

        :param resource_share_ids: The resource_share_ids of this SearchSharedResourcesReqBody.
        :type resource_share_ids: list[str]
        """
        self._resource_share_ids = resource_share_ids

    @property
    def resource_region(self):
        r"""Gets the resource_region of this SearchSharedResourcesReqBody.

        资源所在的区域。

        :return: The resource_region of this SearchSharedResourcesReqBody.
        :rtype: str
        """
        return self._resource_region

    @resource_region.setter
    def resource_region(self, resource_region):
        r"""Sets the resource_region of this SearchSharedResourcesReqBody.

        资源所在的区域。

        :param resource_region: The resource_region of this SearchSharedResourcesReqBody.
        :type resource_region: str
        """
        self._resource_region = resource_region

    @property
    def resource_type(self):
        r"""Gets the resource_type of this SearchSharedResourcesReqBody.

        指定资源类型。

        :return: The resource_type of this SearchSharedResourcesReqBody.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this SearchSharedResourcesReqBody.

        指定资源类型。

        :param resource_type: The resource_type of this SearchSharedResourcesReqBody.
        :type resource_type: str
        """
        self._resource_type = resource_type

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
        if not isinstance(other, SearchSharedResourcesReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
