# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class KeystoneListFederationProjectsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'links': 'LinksSelf',
        'projects': 'list[AuthProjectResult]'
    }

    attribute_map = {
        'links': 'links',
        'projects': 'projects'
    }

    def __init__(self, links=None, projects=None):
        r"""KeystoneListFederationProjectsResponse

        The model defined in huaweicloud sdk

        :param links: 
        :type links: :class:`huaweicloudsdkiam.v3.LinksSelf`
        :param projects: 项目信息列表。
        :type projects: list[:class:`huaweicloudsdkiam.v3.AuthProjectResult`]
        """
        
        super(KeystoneListFederationProjectsResponse, self).__init__()

        self._links = None
        self._projects = None
        self.discriminator = None

        if links is not None:
            self.links = links
        if projects is not None:
            self.projects = projects

    @property
    def links(self):
        r"""Gets the links of this KeystoneListFederationProjectsResponse.

        :return: The links of this KeystoneListFederationProjectsResponse.
        :rtype: :class:`huaweicloudsdkiam.v3.LinksSelf`
        """
        return self._links

    @links.setter
    def links(self, links):
        r"""Sets the links of this KeystoneListFederationProjectsResponse.

        :param links: The links of this KeystoneListFederationProjectsResponse.
        :type links: :class:`huaweicloudsdkiam.v3.LinksSelf`
        """
        self._links = links

    @property
    def projects(self):
        r"""Gets the projects of this KeystoneListFederationProjectsResponse.

        项目信息列表。

        :return: The projects of this KeystoneListFederationProjectsResponse.
        :rtype: list[:class:`huaweicloudsdkiam.v3.AuthProjectResult`]
        """
        return self._projects

    @projects.setter
    def projects(self, projects):
        r"""Sets the projects of this KeystoneListFederationProjectsResponse.

        项目信息列表。

        :param projects: The projects of this KeystoneListFederationProjectsResponse.
        :type projects: list[:class:`huaweicloudsdkiam.v3.AuthProjectResult`]
        """
        self._projects = projects

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
        if not isinstance(other, KeystoneListFederationProjectsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
