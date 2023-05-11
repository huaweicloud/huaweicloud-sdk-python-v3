# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SearchSharedPrincipalsReqBody:

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
        'principals': 'list[str]',
        'resource_urn': 'str',
        'resource_owner': 'str',
        'resource_share_ids': 'list[str]'
    }

    attribute_map = {
        'limit': 'limit',
        'marker': 'marker',
        'principals': 'principals',
        'resource_urn': 'resource_urn',
        'resource_owner': 'resource_owner',
        'resource_share_ids': 'resource_share_ids'
    }

    def __init__(self, limit=None, marker=None, principals=None, resource_urn=None, resource_owner=None, resource_share_ids=None):
        """SearchSharedPrincipalsReqBody

        The model defined in huaweicloud sdk

        :param limit: 分页页面的最大值。
        :type limit: int
        :param marker: 页面标记。
        :type marker: str
        :param principals: 指定资源使用者。
        :type principals: list[str]
        :param resource_urn: 指定资源的URN。
        :type resource_urn: str
        :param resource_owner: 指定资源共享实例的所有者（self或者other-accounts）。
        :type resource_owner: str
        :param resource_share_ids: 指定资源共享实例的ID列表。
        :type resource_share_ids: list[str]
        """
        
        

        self._limit = None
        self._marker = None
        self._principals = None
        self._resource_urn = None
        self._resource_owner = None
        self._resource_share_ids = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if principals is not None:
            self.principals = principals
        if resource_urn is not None:
            self.resource_urn = resource_urn
        self.resource_owner = resource_owner
        if resource_share_ids is not None:
            self.resource_share_ids = resource_share_ids

    @property
    def limit(self):
        """Gets the limit of this SearchSharedPrincipalsReqBody.

        分页页面的最大值。

        :return: The limit of this SearchSharedPrincipalsReqBody.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this SearchSharedPrincipalsReqBody.

        分页页面的最大值。

        :param limit: The limit of this SearchSharedPrincipalsReqBody.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this SearchSharedPrincipalsReqBody.

        页面标记。

        :return: The marker of this SearchSharedPrincipalsReqBody.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this SearchSharedPrincipalsReqBody.

        页面标记。

        :param marker: The marker of this SearchSharedPrincipalsReqBody.
        :type marker: str
        """
        self._marker = marker

    @property
    def principals(self):
        """Gets the principals of this SearchSharedPrincipalsReqBody.

        指定资源使用者。

        :return: The principals of this SearchSharedPrincipalsReqBody.
        :rtype: list[str]
        """
        return self._principals

    @principals.setter
    def principals(self, principals):
        """Sets the principals of this SearchSharedPrincipalsReqBody.

        指定资源使用者。

        :param principals: The principals of this SearchSharedPrincipalsReqBody.
        :type principals: list[str]
        """
        self._principals = principals

    @property
    def resource_urn(self):
        """Gets the resource_urn of this SearchSharedPrincipalsReqBody.

        指定资源的URN。

        :return: The resource_urn of this SearchSharedPrincipalsReqBody.
        :rtype: str
        """
        return self._resource_urn

    @resource_urn.setter
    def resource_urn(self, resource_urn):
        """Sets the resource_urn of this SearchSharedPrincipalsReqBody.

        指定资源的URN。

        :param resource_urn: The resource_urn of this SearchSharedPrincipalsReqBody.
        :type resource_urn: str
        """
        self._resource_urn = resource_urn

    @property
    def resource_owner(self):
        """Gets the resource_owner of this SearchSharedPrincipalsReqBody.

        指定资源共享实例的所有者（self或者other-accounts）。

        :return: The resource_owner of this SearchSharedPrincipalsReqBody.
        :rtype: str
        """
        return self._resource_owner

    @resource_owner.setter
    def resource_owner(self, resource_owner):
        """Sets the resource_owner of this SearchSharedPrincipalsReqBody.

        指定资源共享实例的所有者（self或者other-accounts）。

        :param resource_owner: The resource_owner of this SearchSharedPrincipalsReqBody.
        :type resource_owner: str
        """
        self._resource_owner = resource_owner

    @property
    def resource_share_ids(self):
        """Gets the resource_share_ids of this SearchSharedPrincipalsReqBody.

        指定资源共享实例的ID列表。

        :return: The resource_share_ids of this SearchSharedPrincipalsReqBody.
        :rtype: list[str]
        """
        return self._resource_share_ids

    @resource_share_ids.setter
    def resource_share_ids(self, resource_share_ids):
        """Sets the resource_share_ids of this SearchSharedPrincipalsReqBody.

        指定资源共享实例的ID列表。

        :param resource_share_ids: The resource_share_ids of this SearchSharedPrincipalsReqBody.
        :type resource_share_ids: list[str]
        """
        self._resource_share_ids = resource_share_ids

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
        if not isinstance(other, SearchSharedPrincipalsReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
