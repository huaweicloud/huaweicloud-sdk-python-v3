# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SearchResourceShareAssociationsReqBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'association_status': 'str',
        'association_type': 'str',
        'limit': 'int',
        'marker': 'str',
        'principal': 'str',
        'resource_urn': 'str',
        'resource_share_ids': 'list[str]',
        'resource_ids': 'list[str]'
    }

    attribute_map = {
        'association_status': 'association_status',
        'association_type': 'association_type',
        'limit': 'limit',
        'marker': 'marker',
        'principal': 'principal',
        'resource_urn': 'resource_urn',
        'resource_share_ids': 'resource_share_ids',
        'resource_ids': 'resource_ids'
    }

    def __init__(self, association_status=None, association_type=None, limit=None, marker=None, principal=None, resource_urn=None, resource_share_ids=None, resource_ids=None):
        r"""SearchResourceShareAssociationsReqBody

        The model defined in huaweicloud sdk

        :param association_status: 指定绑定的状态。
        :type association_status: str
        :param association_type: 指定绑定的类型（principal或resource）。
        :type association_type: str
        :param limit: 分页页面的最大值。
        :type limit: int
        :param marker: 页面标记。
        :type marker: str
        :param principal: 指定绑定的资源使用者。
        :type principal: str
        :param resource_urn: 指定绑定的共享资源URN。
        :type resource_urn: str
        :param resource_share_ids: 指定资源共享实例的ID列表。
        :type resource_share_ids: list[str]
        :param resource_ids: 指定共享资源ID列表。
        :type resource_ids: list[str]
        """
        
        

        self._association_status = None
        self._association_type = None
        self._limit = None
        self._marker = None
        self._principal = None
        self._resource_urn = None
        self._resource_share_ids = None
        self._resource_ids = None
        self.discriminator = None

        if association_status is not None:
            self.association_status = association_status
        self.association_type = association_type
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if principal is not None:
            self.principal = principal
        if resource_urn is not None:
            self.resource_urn = resource_urn
        if resource_share_ids is not None:
            self.resource_share_ids = resource_share_ids
        if resource_ids is not None:
            self.resource_ids = resource_ids

    @property
    def association_status(self):
        r"""Gets the association_status of this SearchResourceShareAssociationsReqBody.

        指定绑定的状态。

        :return: The association_status of this SearchResourceShareAssociationsReqBody.
        :rtype: str
        """
        return self._association_status

    @association_status.setter
    def association_status(self, association_status):
        r"""Sets the association_status of this SearchResourceShareAssociationsReqBody.

        指定绑定的状态。

        :param association_status: The association_status of this SearchResourceShareAssociationsReqBody.
        :type association_status: str
        """
        self._association_status = association_status

    @property
    def association_type(self):
        r"""Gets the association_type of this SearchResourceShareAssociationsReqBody.

        指定绑定的类型（principal或resource）。

        :return: The association_type of this SearchResourceShareAssociationsReqBody.
        :rtype: str
        """
        return self._association_type

    @association_type.setter
    def association_type(self, association_type):
        r"""Sets the association_type of this SearchResourceShareAssociationsReqBody.

        指定绑定的类型（principal或resource）。

        :param association_type: The association_type of this SearchResourceShareAssociationsReqBody.
        :type association_type: str
        """
        self._association_type = association_type

    @property
    def limit(self):
        r"""Gets the limit of this SearchResourceShareAssociationsReqBody.

        分页页面的最大值。

        :return: The limit of this SearchResourceShareAssociationsReqBody.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this SearchResourceShareAssociationsReqBody.

        分页页面的最大值。

        :param limit: The limit of this SearchResourceShareAssociationsReqBody.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this SearchResourceShareAssociationsReqBody.

        页面标记。

        :return: The marker of this SearchResourceShareAssociationsReqBody.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this SearchResourceShareAssociationsReqBody.

        页面标记。

        :param marker: The marker of this SearchResourceShareAssociationsReqBody.
        :type marker: str
        """
        self._marker = marker

    @property
    def principal(self):
        r"""Gets the principal of this SearchResourceShareAssociationsReqBody.

        指定绑定的资源使用者。

        :return: The principal of this SearchResourceShareAssociationsReqBody.
        :rtype: str
        """
        return self._principal

    @principal.setter
    def principal(self, principal):
        r"""Sets the principal of this SearchResourceShareAssociationsReqBody.

        指定绑定的资源使用者。

        :param principal: The principal of this SearchResourceShareAssociationsReqBody.
        :type principal: str
        """
        self._principal = principal

    @property
    def resource_urn(self):
        r"""Gets the resource_urn of this SearchResourceShareAssociationsReqBody.

        指定绑定的共享资源URN。

        :return: The resource_urn of this SearchResourceShareAssociationsReqBody.
        :rtype: str
        """
        return self._resource_urn

    @resource_urn.setter
    def resource_urn(self, resource_urn):
        r"""Sets the resource_urn of this SearchResourceShareAssociationsReqBody.

        指定绑定的共享资源URN。

        :param resource_urn: The resource_urn of this SearchResourceShareAssociationsReqBody.
        :type resource_urn: str
        """
        self._resource_urn = resource_urn

    @property
    def resource_share_ids(self):
        r"""Gets the resource_share_ids of this SearchResourceShareAssociationsReqBody.

        指定资源共享实例的ID列表。

        :return: The resource_share_ids of this SearchResourceShareAssociationsReqBody.
        :rtype: list[str]
        """
        return self._resource_share_ids

    @resource_share_ids.setter
    def resource_share_ids(self, resource_share_ids):
        r"""Sets the resource_share_ids of this SearchResourceShareAssociationsReqBody.

        指定资源共享实例的ID列表。

        :param resource_share_ids: The resource_share_ids of this SearchResourceShareAssociationsReqBody.
        :type resource_share_ids: list[str]
        """
        self._resource_share_ids = resource_share_ids

    @property
    def resource_ids(self):
        r"""Gets the resource_ids of this SearchResourceShareAssociationsReqBody.

        指定共享资源ID列表。

        :return: The resource_ids of this SearchResourceShareAssociationsReqBody.
        :rtype: list[str]
        """
        return self._resource_ids

    @resource_ids.setter
    def resource_ids(self, resource_ids):
        r"""Sets the resource_ids of this SearchResourceShareAssociationsReqBody.

        指定共享资源ID列表。

        :param resource_ids: The resource_ids of this SearchResourceShareAssociationsReqBody.
        :type resource_ids: list[str]
        """
        self._resource_ids = resource_ids

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
        if not isinstance(other, SearchResourceShareAssociationsReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
