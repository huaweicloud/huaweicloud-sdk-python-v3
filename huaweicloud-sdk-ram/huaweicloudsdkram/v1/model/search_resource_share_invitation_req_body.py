# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SearchResourceShareInvitationReqBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_share_ids': 'list[str]',
        'resource_share_invitation_ids': 'list[str]',
        'status': 'str',
        'limit': 'int',
        'marker': 'str'
    }

    attribute_map = {
        'resource_share_ids': 'resource_share_ids',
        'resource_share_invitation_ids': 'resource_share_invitation_ids',
        'status': 'status',
        'limit': 'limit',
        'marker': 'marker'
    }

    def __init__(self, resource_share_ids=None, resource_share_invitation_ids=None, status=None, limit=None, marker=None):
        """SearchResourceShareInvitationReqBody

        The model defined in huaweicloud sdk

        :param resource_share_ids: 资源共享实例的ID列表。
        :type resource_share_ids: list[str]
        :param resource_share_invitation_ids: 资源共享邀请的ID列表。
        :type resource_share_invitation_ids: list[str]
        :param status: 资源共享邀请的当前状态。
        :type status: str
        :param limit: 分页页面的最大值。
        :type limit: int
        :param marker: 分页位置标识。从marker指定索引的下一条数据开始查询。查询第一页数据时，不需要传入此参数，查询后续页码数据时，将查询前一页数据响应体中marker值配入此参数。
        :type marker: str
        """
        
        

        self._resource_share_ids = None
        self._resource_share_invitation_ids = None
        self._status = None
        self._limit = None
        self._marker = None
        self.discriminator = None

        if resource_share_ids is not None:
            self.resource_share_ids = resource_share_ids
        if resource_share_invitation_ids is not None:
            self.resource_share_invitation_ids = resource_share_invitation_ids
        if status is not None:
            self.status = status
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker

    @property
    def resource_share_ids(self):
        """Gets the resource_share_ids of this SearchResourceShareInvitationReqBody.

        资源共享实例的ID列表。

        :return: The resource_share_ids of this SearchResourceShareInvitationReqBody.
        :rtype: list[str]
        """
        return self._resource_share_ids

    @resource_share_ids.setter
    def resource_share_ids(self, resource_share_ids):
        """Sets the resource_share_ids of this SearchResourceShareInvitationReqBody.

        资源共享实例的ID列表。

        :param resource_share_ids: The resource_share_ids of this SearchResourceShareInvitationReqBody.
        :type resource_share_ids: list[str]
        """
        self._resource_share_ids = resource_share_ids

    @property
    def resource_share_invitation_ids(self):
        """Gets the resource_share_invitation_ids of this SearchResourceShareInvitationReqBody.

        资源共享邀请的ID列表。

        :return: The resource_share_invitation_ids of this SearchResourceShareInvitationReqBody.
        :rtype: list[str]
        """
        return self._resource_share_invitation_ids

    @resource_share_invitation_ids.setter
    def resource_share_invitation_ids(self, resource_share_invitation_ids):
        """Sets the resource_share_invitation_ids of this SearchResourceShareInvitationReqBody.

        资源共享邀请的ID列表。

        :param resource_share_invitation_ids: The resource_share_invitation_ids of this SearchResourceShareInvitationReqBody.
        :type resource_share_invitation_ids: list[str]
        """
        self._resource_share_invitation_ids = resource_share_invitation_ids

    @property
    def status(self):
        """Gets the status of this SearchResourceShareInvitationReqBody.

        资源共享邀请的当前状态。

        :return: The status of this SearchResourceShareInvitationReqBody.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SearchResourceShareInvitationReqBody.

        资源共享邀请的当前状态。

        :param status: The status of this SearchResourceShareInvitationReqBody.
        :type status: str
        """
        self._status = status

    @property
    def limit(self):
        """Gets the limit of this SearchResourceShareInvitationReqBody.

        分页页面的最大值。

        :return: The limit of this SearchResourceShareInvitationReqBody.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this SearchResourceShareInvitationReqBody.

        分页页面的最大值。

        :param limit: The limit of this SearchResourceShareInvitationReqBody.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this SearchResourceShareInvitationReqBody.

        分页位置标识。从marker指定索引的下一条数据开始查询。查询第一页数据时，不需要传入此参数，查询后续页码数据时，将查询前一页数据响应体中marker值配入此参数。

        :return: The marker of this SearchResourceShareInvitationReqBody.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this SearchResourceShareInvitationReqBody.

        分页位置标识。从marker指定索引的下一条数据开始查询。查询第一页数据时，不需要传入此参数，查询后续页码数据时，将查询前一页数据响应体中marker值配入此参数。

        :param marker: The marker of this SearchResourceShareInvitationReqBody.
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
        if not isinstance(other, SearchResourceShareInvitationReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
