# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEnterpriseProjectsForUserResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'enterprise_projects': 'list[ListEnterpriseProjectsResDetail]'
    }

    attribute_map = {
        'enterprise_projects': 'enterprise-projects'
    }

    def __init__(self, enterprise_projects=None):
        """ListEnterpriseProjectsForUserResponse

        The model defined in huaweicloud sdk

        :param enterprise_projects: 企业项目信息。
        :type enterprise_projects: list[:class:`huaweicloudsdkiam.v3.ListEnterpriseProjectsResDetail`]
        """
        
        super(ListEnterpriseProjectsForUserResponse, self).__init__()

        self._enterprise_projects = None
        self.discriminator = None

        if enterprise_projects is not None:
            self.enterprise_projects = enterprise_projects

    @property
    def enterprise_projects(self):
        """Gets the enterprise_projects of this ListEnterpriseProjectsForUserResponse.

        企业项目信息。

        :return: The enterprise_projects of this ListEnterpriseProjectsForUserResponse.
        :rtype: list[:class:`huaweicloudsdkiam.v3.ListEnterpriseProjectsResDetail`]
        """
        return self._enterprise_projects

    @enterprise_projects.setter
    def enterprise_projects(self, enterprise_projects):
        """Sets the enterprise_projects of this ListEnterpriseProjectsForUserResponse.

        企业项目信息。

        :param enterprise_projects: The enterprise_projects of this ListEnterpriseProjectsForUserResponse.
        :type enterprise_projects: list[:class:`huaweicloudsdkiam.v3.ListEnterpriseProjectsResDetail`]
        """
        self._enterprise_projects = enterprise_projects

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
        if not isinstance(other, ListEnterpriseProjectsForUserResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
