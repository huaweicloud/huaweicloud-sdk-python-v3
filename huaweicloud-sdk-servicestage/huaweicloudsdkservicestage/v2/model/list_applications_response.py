# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListApplicationsResponse(SdkResponse):

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
        'applications': 'list[ApplicationView]'
    }

    attribute_map = {
        'count': 'count',
        'applications': 'applications'
    }

    def __init__(self, count=None, applications=None):
        r"""ListApplicationsResponse

        The model defined in huaweicloud sdk

        :param count: 应用总数。
        :type count: int
        :param applications: 应用列表。
        :type applications: list[:class:`huaweicloudsdkservicestage.v2.ApplicationView`]
        """
        
        super(ListApplicationsResponse, self).__init__()

        self._count = None
        self._applications = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if applications is not None:
            self.applications = applications

    @property
    def count(self):
        r"""Gets the count of this ListApplicationsResponse.

        应用总数。

        :return: The count of this ListApplicationsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListApplicationsResponse.

        应用总数。

        :param count: The count of this ListApplicationsResponse.
        :type count: int
        """
        self._count = count

    @property
    def applications(self):
        r"""Gets the applications of this ListApplicationsResponse.

        应用列表。

        :return: The applications of this ListApplicationsResponse.
        :rtype: list[:class:`huaweicloudsdkservicestage.v2.ApplicationView`]
        """
        return self._applications

    @applications.setter
    def applications(self, applications):
        r"""Sets the applications of this ListApplicationsResponse.

        应用列表。

        :param applications: The applications of this ListApplicationsResponse.
        :type applications: list[:class:`huaweicloudsdkservicestage.v2.ApplicationView`]
        """
        self._applications = applications

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
        if not isinstance(other, ListApplicationsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
