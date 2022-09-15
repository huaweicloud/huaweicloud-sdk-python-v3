# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAuthorizationDetailResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'status': 'int',
        'incident_id': 'str',
        'simple_description': 'str',
        'resource_type_id': 'str',
        'resource_type_name': 'str',
        'visit_type_id': 'str',
        'visit_type_name': 'str',
        'auth_effective_time': 'datetime',
        'auth_expire_time': 'datetime',
        'reject_reason': 'str',
        'incident_auth_detail_list': 'list[IncidentOrderAuthDetailInfoV2]',
        'xcustomer_name': 'str',
        'auth_handler_name': 'str',
        'agency_name': 'str',
        'auth_describe': 'str',
        'content_type_id': 'str',
        'content_type_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'status': 'status',
        'incident_id': 'incident_id',
        'simple_description': 'simple_description',
        'resource_type_id': 'resource_type_id',
        'resource_type_name': 'resource_type_name',
        'visit_type_id': 'visit_type_id',
        'visit_type_name': 'visit_type_name',
        'auth_effective_time': 'auth_effective_time',
        'auth_expire_time': 'auth_expire_time',
        'reject_reason': 'reject_reason',
        'incident_auth_detail_list': 'incident_auth_detail_list',
        'xcustomer_name': 'xcustomer_name',
        'auth_handler_name': 'auth_handler_name',
        'agency_name': 'agency_name',
        'auth_describe': 'auth_describe',
        'content_type_id': 'content_type_id',
        'content_type_name': 'content_type_name'
    }

    def __init__(self, id=None, status=None, incident_id=None, simple_description=None, resource_type_id=None, resource_type_name=None, visit_type_id=None, visit_type_name=None, auth_effective_time=None, auth_expire_time=None, reject_reason=None, incident_auth_detail_list=None, xcustomer_name=None, auth_handler_name=None, agency_name=None, auth_describe=None, content_type_id=None, content_type_name=None):
        """ShowAuthorizationDetailResponse

        The model defined in huaweicloud sdk

        :param id: 授权id
        :type id: str
        :param status: 授权状态
        :type status: int
        :param incident_id: 工单id
        :type incident_id: str
        :param simple_description: 简要描述
        :type simple_description: str
        :param resource_type_id: 授权资源类型id
        :type resource_type_id: str
        :param resource_type_name: 授权资源类型名称
        :type resource_type_name: str
        :param visit_type_id: 授权访问类型id
        :type visit_type_id: str
        :param visit_type_name: 授权访问类型名称
        :type visit_type_name: str
        :param auth_effective_time: 授权生效时间
        :type auth_effective_time: datetime
        :param auth_expire_time: 授权到期时间
        :type auth_expire_time: datetime
        :param reject_reason: 拒绝原因
        :type reject_reason: str
        :param incident_auth_detail_list: 授权详情列表
        :type incident_auth_detail_list: list[:class:`huaweicloudsdkosm.v2.IncidentOrderAuthDetailInfoV2`]
        :param xcustomer_name: 子账号名称
        :type xcustomer_name: str
        :param auth_handler_name: 授权处理人名称
        :type auth_handler_name: str
        :param agency_name: 委托名称
        :type agency_name: str
        :param auth_describe: 授权描述
        :type auth_describe: str
        :param content_type_id: 授权内容Id 
        :type content_type_id: str
        :param content_type_name: 授权内容名称
        :type content_type_name: str
        """
        
        super(ShowAuthorizationDetailResponse, self).__init__()

        self._id = None
        self._status = None
        self._incident_id = None
        self._simple_description = None
        self._resource_type_id = None
        self._resource_type_name = None
        self._visit_type_id = None
        self._visit_type_name = None
        self._auth_effective_time = None
        self._auth_expire_time = None
        self._reject_reason = None
        self._incident_auth_detail_list = None
        self._xcustomer_name = None
        self._auth_handler_name = None
        self._agency_name = None
        self._auth_describe = None
        self._content_type_id = None
        self._content_type_name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if status is not None:
            self.status = status
        if incident_id is not None:
            self.incident_id = incident_id
        if simple_description is not None:
            self.simple_description = simple_description
        if resource_type_id is not None:
            self.resource_type_id = resource_type_id
        if resource_type_name is not None:
            self.resource_type_name = resource_type_name
        if visit_type_id is not None:
            self.visit_type_id = visit_type_id
        if visit_type_name is not None:
            self.visit_type_name = visit_type_name
        if auth_effective_time is not None:
            self.auth_effective_time = auth_effective_time
        if auth_expire_time is not None:
            self.auth_expire_time = auth_expire_time
        if reject_reason is not None:
            self.reject_reason = reject_reason
        if incident_auth_detail_list is not None:
            self.incident_auth_detail_list = incident_auth_detail_list
        if xcustomer_name is not None:
            self.xcustomer_name = xcustomer_name
        if auth_handler_name is not None:
            self.auth_handler_name = auth_handler_name
        if agency_name is not None:
            self.agency_name = agency_name
        if auth_describe is not None:
            self.auth_describe = auth_describe
        if content_type_id is not None:
            self.content_type_id = content_type_id
        if content_type_name is not None:
            self.content_type_name = content_type_name

    @property
    def id(self):
        """Gets the id of this ShowAuthorizationDetailResponse.

        授权id

        :return: The id of this ShowAuthorizationDetailResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowAuthorizationDetailResponse.

        授权id

        :param id: The id of this ShowAuthorizationDetailResponse.
        :type id: str
        """
        self._id = id

    @property
    def status(self):
        """Gets the status of this ShowAuthorizationDetailResponse.

        授权状态

        :return: The status of this ShowAuthorizationDetailResponse.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowAuthorizationDetailResponse.

        授权状态

        :param status: The status of this ShowAuthorizationDetailResponse.
        :type status: int
        """
        self._status = status

    @property
    def incident_id(self):
        """Gets the incident_id of this ShowAuthorizationDetailResponse.

        工单id

        :return: The incident_id of this ShowAuthorizationDetailResponse.
        :rtype: str
        """
        return self._incident_id

    @incident_id.setter
    def incident_id(self, incident_id):
        """Sets the incident_id of this ShowAuthorizationDetailResponse.

        工单id

        :param incident_id: The incident_id of this ShowAuthorizationDetailResponse.
        :type incident_id: str
        """
        self._incident_id = incident_id

    @property
    def simple_description(self):
        """Gets the simple_description of this ShowAuthorizationDetailResponse.

        简要描述

        :return: The simple_description of this ShowAuthorizationDetailResponse.
        :rtype: str
        """
        return self._simple_description

    @simple_description.setter
    def simple_description(self, simple_description):
        """Sets the simple_description of this ShowAuthorizationDetailResponse.

        简要描述

        :param simple_description: The simple_description of this ShowAuthorizationDetailResponse.
        :type simple_description: str
        """
        self._simple_description = simple_description

    @property
    def resource_type_id(self):
        """Gets the resource_type_id of this ShowAuthorizationDetailResponse.

        授权资源类型id

        :return: The resource_type_id of this ShowAuthorizationDetailResponse.
        :rtype: str
        """
        return self._resource_type_id

    @resource_type_id.setter
    def resource_type_id(self, resource_type_id):
        """Sets the resource_type_id of this ShowAuthorizationDetailResponse.

        授权资源类型id

        :param resource_type_id: The resource_type_id of this ShowAuthorizationDetailResponse.
        :type resource_type_id: str
        """
        self._resource_type_id = resource_type_id

    @property
    def resource_type_name(self):
        """Gets the resource_type_name of this ShowAuthorizationDetailResponse.

        授权资源类型名称

        :return: The resource_type_name of this ShowAuthorizationDetailResponse.
        :rtype: str
        """
        return self._resource_type_name

    @resource_type_name.setter
    def resource_type_name(self, resource_type_name):
        """Sets the resource_type_name of this ShowAuthorizationDetailResponse.

        授权资源类型名称

        :param resource_type_name: The resource_type_name of this ShowAuthorizationDetailResponse.
        :type resource_type_name: str
        """
        self._resource_type_name = resource_type_name

    @property
    def visit_type_id(self):
        """Gets the visit_type_id of this ShowAuthorizationDetailResponse.

        授权访问类型id

        :return: The visit_type_id of this ShowAuthorizationDetailResponse.
        :rtype: str
        """
        return self._visit_type_id

    @visit_type_id.setter
    def visit_type_id(self, visit_type_id):
        """Sets the visit_type_id of this ShowAuthorizationDetailResponse.

        授权访问类型id

        :param visit_type_id: The visit_type_id of this ShowAuthorizationDetailResponse.
        :type visit_type_id: str
        """
        self._visit_type_id = visit_type_id

    @property
    def visit_type_name(self):
        """Gets the visit_type_name of this ShowAuthorizationDetailResponse.

        授权访问类型名称

        :return: The visit_type_name of this ShowAuthorizationDetailResponse.
        :rtype: str
        """
        return self._visit_type_name

    @visit_type_name.setter
    def visit_type_name(self, visit_type_name):
        """Sets the visit_type_name of this ShowAuthorizationDetailResponse.

        授权访问类型名称

        :param visit_type_name: The visit_type_name of this ShowAuthorizationDetailResponse.
        :type visit_type_name: str
        """
        self._visit_type_name = visit_type_name

    @property
    def auth_effective_time(self):
        """Gets the auth_effective_time of this ShowAuthorizationDetailResponse.

        授权生效时间

        :return: The auth_effective_time of this ShowAuthorizationDetailResponse.
        :rtype: datetime
        """
        return self._auth_effective_time

    @auth_effective_time.setter
    def auth_effective_time(self, auth_effective_time):
        """Sets the auth_effective_time of this ShowAuthorizationDetailResponse.

        授权生效时间

        :param auth_effective_time: The auth_effective_time of this ShowAuthorizationDetailResponse.
        :type auth_effective_time: datetime
        """
        self._auth_effective_time = auth_effective_time

    @property
    def auth_expire_time(self):
        """Gets the auth_expire_time of this ShowAuthorizationDetailResponse.

        授权到期时间

        :return: The auth_expire_time of this ShowAuthorizationDetailResponse.
        :rtype: datetime
        """
        return self._auth_expire_time

    @auth_expire_time.setter
    def auth_expire_time(self, auth_expire_time):
        """Sets the auth_expire_time of this ShowAuthorizationDetailResponse.

        授权到期时间

        :param auth_expire_time: The auth_expire_time of this ShowAuthorizationDetailResponse.
        :type auth_expire_time: datetime
        """
        self._auth_expire_time = auth_expire_time

    @property
    def reject_reason(self):
        """Gets the reject_reason of this ShowAuthorizationDetailResponse.

        拒绝原因

        :return: The reject_reason of this ShowAuthorizationDetailResponse.
        :rtype: str
        """
        return self._reject_reason

    @reject_reason.setter
    def reject_reason(self, reject_reason):
        """Sets the reject_reason of this ShowAuthorizationDetailResponse.

        拒绝原因

        :param reject_reason: The reject_reason of this ShowAuthorizationDetailResponse.
        :type reject_reason: str
        """
        self._reject_reason = reject_reason

    @property
    def incident_auth_detail_list(self):
        """Gets the incident_auth_detail_list of this ShowAuthorizationDetailResponse.

        授权详情列表

        :return: The incident_auth_detail_list of this ShowAuthorizationDetailResponse.
        :rtype: list[:class:`huaweicloudsdkosm.v2.IncidentOrderAuthDetailInfoV2`]
        """
        return self._incident_auth_detail_list

    @incident_auth_detail_list.setter
    def incident_auth_detail_list(self, incident_auth_detail_list):
        """Sets the incident_auth_detail_list of this ShowAuthorizationDetailResponse.

        授权详情列表

        :param incident_auth_detail_list: The incident_auth_detail_list of this ShowAuthorizationDetailResponse.
        :type incident_auth_detail_list: list[:class:`huaweicloudsdkosm.v2.IncidentOrderAuthDetailInfoV2`]
        """
        self._incident_auth_detail_list = incident_auth_detail_list

    @property
    def xcustomer_name(self):
        """Gets the xcustomer_name of this ShowAuthorizationDetailResponse.

        子账号名称

        :return: The xcustomer_name of this ShowAuthorizationDetailResponse.
        :rtype: str
        """
        return self._xcustomer_name

    @xcustomer_name.setter
    def xcustomer_name(self, xcustomer_name):
        """Sets the xcustomer_name of this ShowAuthorizationDetailResponse.

        子账号名称

        :param xcustomer_name: The xcustomer_name of this ShowAuthorizationDetailResponse.
        :type xcustomer_name: str
        """
        self._xcustomer_name = xcustomer_name

    @property
    def auth_handler_name(self):
        """Gets the auth_handler_name of this ShowAuthorizationDetailResponse.

        授权处理人名称

        :return: The auth_handler_name of this ShowAuthorizationDetailResponse.
        :rtype: str
        """
        return self._auth_handler_name

    @auth_handler_name.setter
    def auth_handler_name(self, auth_handler_name):
        """Sets the auth_handler_name of this ShowAuthorizationDetailResponse.

        授权处理人名称

        :param auth_handler_name: The auth_handler_name of this ShowAuthorizationDetailResponse.
        :type auth_handler_name: str
        """
        self._auth_handler_name = auth_handler_name

    @property
    def agency_name(self):
        """Gets the agency_name of this ShowAuthorizationDetailResponse.

        委托名称

        :return: The agency_name of this ShowAuthorizationDetailResponse.
        :rtype: str
        """
        return self._agency_name

    @agency_name.setter
    def agency_name(self, agency_name):
        """Sets the agency_name of this ShowAuthorizationDetailResponse.

        委托名称

        :param agency_name: The agency_name of this ShowAuthorizationDetailResponse.
        :type agency_name: str
        """
        self._agency_name = agency_name

    @property
    def auth_describe(self):
        """Gets the auth_describe of this ShowAuthorizationDetailResponse.

        授权描述

        :return: The auth_describe of this ShowAuthorizationDetailResponse.
        :rtype: str
        """
        return self._auth_describe

    @auth_describe.setter
    def auth_describe(self, auth_describe):
        """Sets the auth_describe of this ShowAuthorizationDetailResponse.

        授权描述

        :param auth_describe: The auth_describe of this ShowAuthorizationDetailResponse.
        :type auth_describe: str
        """
        self._auth_describe = auth_describe

    @property
    def content_type_id(self):
        """Gets the content_type_id of this ShowAuthorizationDetailResponse.

        授权内容Id 

        :return: The content_type_id of this ShowAuthorizationDetailResponse.
        :rtype: str
        """
        return self._content_type_id

    @content_type_id.setter
    def content_type_id(self, content_type_id):
        """Sets the content_type_id of this ShowAuthorizationDetailResponse.

        授权内容Id 

        :param content_type_id: The content_type_id of this ShowAuthorizationDetailResponse.
        :type content_type_id: str
        """
        self._content_type_id = content_type_id

    @property
    def content_type_name(self):
        """Gets the content_type_name of this ShowAuthorizationDetailResponse.

        授权内容名称

        :return: The content_type_name of this ShowAuthorizationDetailResponse.
        :rtype: str
        """
        return self._content_type_name

    @content_type_name.setter
    def content_type_name(self, content_type_name):
        """Sets the content_type_name of this ShowAuthorizationDetailResponse.

        授权内容名称

        :param content_type_name: The content_type_name of this ShowAuthorizationDetailResponse.
        :type content_type_name: str
        """
        self._content_type_name = content_type_name

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
        if not isinstance(other, ShowAuthorizationDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
