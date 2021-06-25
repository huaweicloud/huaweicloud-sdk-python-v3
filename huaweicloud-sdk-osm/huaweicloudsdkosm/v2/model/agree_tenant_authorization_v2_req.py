# coding: utf-8

import pprint
import re

import six





class AgreeTenantAuthorizationV2Req:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'auth_detail_list': 'list[TenantAgreeAuthDetailV2]',
        'auth_effective_time': 'int',
        'auth_expire_time': 'int',
        'group_id': 'str',
        'agency_id': 'str'
    }

    attribute_map = {
        'auth_detail_list': 'auth_detail_list',
        'auth_effective_time': 'auth_effective_time',
        'auth_expire_time': 'auth_expire_time',
        'group_id': 'group_id',
        'agency_id': 'agency_id'
    }

    def __init__(self, auth_detail_list=None, auth_effective_time=None, auth_expire_time=None, group_id=None, agency_id=None):
        """AgreeTenantAuthorizationV2Req - a model defined in huaweicloud sdk"""
        
        

        self._auth_detail_list = None
        self._auth_effective_time = None
        self._auth_expire_time = None
        self._group_id = None
        self._agency_id = None
        self.discriminator = None

        if auth_detail_list is not None:
            self.auth_detail_list = auth_detail_list
        if auth_effective_time is not None:
            self.auth_effective_time = auth_effective_time
        if auth_expire_time is not None:
            self.auth_expire_time = auth_expire_time
        if group_id is not None:
            self.group_id = group_id
        if agency_id is not None:
            self.agency_id = agency_id

    @property
    def auth_detail_list(self):
        """Gets the auth_detail_list of this AgreeTenantAuthorizationV2Req.

        授权详情列表

        :return: The auth_detail_list of this AgreeTenantAuthorizationV2Req.
        :rtype: list[TenantAgreeAuthDetailV2]
        """
        return self._auth_detail_list

    @auth_detail_list.setter
    def auth_detail_list(self, auth_detail_list):
        """Sets the auth_detail_list of this AgreeTenantAuthorizationV2Req.

        授权详情列表

        :param auth_detail_list: The auth_detail_list of this AgreeTenantAuthorizationV2Req.
        :type: list[TenantAgreeAuthDetailV2]
        """
        self._auth_detail_list = auth_detail_list

    @property
    def auth_effective_time(self):
        """Gets the auth_effective_time of this AgreeTenantAuthorizationV2Req.

        授权生效时间

        :return: The auth_effective_time of this AgreeTenantAuthorizationV2Req.
        :rtype: int
        """
        return self._auth_effective_time

    @auth_effective_time.setter
    def auth_effective_time(self, auth_effective_time):
        """Sets the auth_effective_time of this AgreeTenantAuthorizationV2Req.

        授权生效时间

        :param auth_effective_time: The auth_effective_time of this AgreeTenantAuthorizationV2Req.
        :type: int
        """
        self._auth_effective_time = auth_effective_time

    @property
    def auth_expire_time(self):
        """Gets the auth_expire_time of this AgreeTenantAuthorizationV2Req.

        授权到期时间

        :return: The auth_expire_time of this AgreeTenantAuthorizationV2Req.
        :rtype: int
        """
        return self._auth_expire_time

    @auth_expire_time.setter
    def auth_expire_time(self, auth_expire_time):
        """Sets the auth_expire_time of this AgreeTenantAuthorizationV2Req.

        授权到期时间

        :param auth_expire_time: The auth_expire_time of this AgreeTenantAuthorizationV2Req.
        :type: int
        """
        self._auth_expire_time = auth_expire_time

    @property
    def group_id(self):
        """Gets the group_id of this AgreeTenantAuthorizationV2Req.

        组id

        :return: The group_id of this AgreeTenantAuthorizationV2Req.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this AgreeTenantAuthorizationV2Req.

        组id

        :param group_id: The group_id of this AgreeTenantAuthorizationV2Req.
        :type: str
        """
        self._group_id = group_id

    @property
    def agency_id(self):
        """Gets the agency_id of this AgreeTenantAuthorizationV2Req.

        委托id

        :return: The agency_id of this AgreeTenantAuthorizationV2Req.
        :rtype: str
        """
        return self._agency_id

    @agency_id.setter
    def agency_id(self, agency_id):
        """Sets the agency_id of this AgreeTenantAuthorizationV2Req.

        委托id

        :param agency_id: The agency_id of this AgreeTenantAuthorizationV2Req.
        :type: str
        """
        self._agency_id = agency_id

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AgreeTenantAuthorizationV2Req):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other