# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAgencyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'agency_name': 'str',
        'authorized': 'bool',
        'agency_policies': 'list[AgencyPolicy]'
    }

    attribute_map = {
        'agency_name': 'agency_name',
        'authorized': 'authorized',
        'agency_policies': 'agency_policies'
    }

    def __init__(self, agency_name=None, authorized=None, agency_policies=None):
        r"""ListAgencyResponse

        The model defined in huaweicloud sdk

        :param agency_name: 委托名称
        :type agency_name: str
        :param authorized: 授权与否。如果用户的服务委托权限包含系统所需要的委托权限返回true，否则返回false。
        :type authorized: bool
        :param agency_policies: 委托策略列表。
        :type agency_policies: list[:class:`huaweicloudsdkdataartsfabric.v1.AgencyPolicy`]
        """
        
        super(ListAgencyResponse, self).__init__()

        self._agency_name = None
        self._authorized = None
        self._agency_policies = None
        self.discriminator = None

        if agency_name is not None:
            self.agency_name = agency_name
        if authorized is not None:
            self.authorized = authorized
        if agency_policies is not None:
            self.agency_policies = agency_policies

    @property
    def agency_name(self):
        r"""Gets the agency_name of this ListAgencyResponse.

        委托名称

        :return: The agency_name of this ListAgencyResponse.
        :rtype: str
        """
        return self._agency_name

    @agency_name.setter
    def agency_name(self, agency_name):
        r"""Sets the agency_name of this ListAgencyResponse.

        委托名称

        :param agency_name: The agency_name of this ListAgencyResponse.
        :type agency_name: str
        """
        self._agency_name = agency_name

    @property
    def authorized(self):
        r"""Gets the authorized of this ListAgencyResponse.

        授权与否。如果用户的服务委托权限包含系统所需要的委托权限返回true，否则返回false。

        :return: The authorized of this ListAgencyResponse.
        :rtype: bool
        """
        return self._authorized

    @authorized.setter
    def authorized(self, authorized):
        r"""Sets the authorized of this ListAgencyResponse.

        授权与否。如果用户的服务委托权限包含系统所需要的委托权限返回true，否则返回false。

        :param authorized: The authorized of this ListAgencyResponse.
        :type authorized: bool
        """
        self._authorized = authorized

    @property
    def agency_policies(self):
        r"""Gets the agency_policies of this ListAgencyResponse.

        委托策略列表。

        :return: The agency_policies of this ListAgencyResponse.
        :rtype: list[:class:`huaweicloudsdkdataartsfabric.v1.AgencyPolicy`]
        """
        return self._agency_policies

    @agency_policies.setter
    def agency_policies(self, agency_policies):
        r"""Sets the agency_policies of this ListAgencyResponse.

        委托策略列表。

        :param agency_policies: The agency_policies of this ListAgencyResponse.
        :type agency_policies: list[:class:`huaweicloudsdkdataartsfabric.v1.AgencyPolicy`]
        """
        self._agency_policies = agency_policies

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
        if not isinstance(other, ListAgencyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
