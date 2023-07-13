# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAuthorizationsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'incident_auth_list': 'list[IncidentOrderAuthV2]'
    }

    attribute_map = {
        'count': 'count',
        'incident_auth_list': 'incident_auth_list'
    }

    def __init__(self, count=None, incident_auth_list=None):
        """ListAuthorizationsResponse

        The model defined in huaweicloud sdk

        :param count: 总数
        :type count: int
        :param incident_auth_list: 授权列表
        :type incident_auth_list: list[:class:`huaweicloudsdkosm.v2.IncidentOrderAuthV2`]
        """
        
        super(ListAuthorizationsResponse, self).__init__()

        self._count = None
        self._incident_auth_list = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if incident_auth_list is not None:
            self.incident_auth_list = incident_auth_list

    @property
    def count(self):
        """Gets the count of this ListAuthorizationsResponse.

        总数

        :return: The count of this ListAuthorizationsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListAuthorizationsResponse.

        总数

        :param count: The count of this ListAuthorizationsResponse.
        :type count: int
        """
        self._count = count

    @property
    def incident_auth_list(self):
        """Gets the incident_auth_list of this ListAuthorizationsResponse.

        授权列表

        :return: The incident_auth_list of this ListAuthorizationsResponse.
        :rtype: list[:class:`huaweicloudsdkosm.v2.IncidentOrderAuthV2`]
        """
        return self._incident_auth_list

    @incident_auth_list.setter
    def incident_auth_list(self, incident_auth_list):
        """Sets the incident_auth_list of this ListAuthorizationsResponse.

        授权列表

        :param incident_auth_list: The incident_auth_list of this ListAuthorizationsResponse.
        :type incident_auth_list: list[:class:`huaweicloudsdkosm.v2.IncidentOrderAuthV2`]
        """
        self._incident_auth_list = incident_auth_list

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
        if not isinstance(other, ListAuthorizationsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
