# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowResourceTagResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tags': 'list[Tag]',
        'enterprise_project_or_default': 'str'
    }

    attribute_map = {
        'tags': 'tags',
        'enterprise_project_or_default': 'enterpriseProjectOrDefault'
    }

    def __init__(self, tags=None, enterprise_project_or_default=None):
        """ShowResourceTagResponse

        The model defined in huaweicloud sdk

        :param tags: 指定实例的标签列表。
        :type tags: list[:class:`huaweicloudsdkdns.v2.Tag`]
        :param enterprise_project_or_default: 企业项目或默认项目
        :type enterprise_project_or_default: str
        """
        
        super(ShowResourceTagResponse, self).__init__()

        self._tags = None
        self._enterprise_project_or_default = None
        self.discriminator = None

        if tags is not None:
            self.tags = tags
        if enterprise_project_or_default is not None:
            self.enterprise_project_or_default = enterprise_project_or_default

    @property
    def tags(self):
        """Gets the tags of this ShowResourceTagResponse.

        指定实例的标签列表。

        :return: The tags of this ShowResourceTagResponse.
        :rtype: list[:class:`huaweicloudsdkdns.v2.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ShowResourceTagResponse.

        指定实例的标签列表。

        :param tags: The tags of this ShowResourceTagResponse.
        :type tags: list[:class:`huaweicloudsdkdns.v2.Tag`]
        """
        self._tags = tags

    @property
    def enterprise_project_or_default(self):
        """Gets the enterprise_project_or_default of this ShowResourceTagResponse.

        企业项目或默认项目

        :return: The enterprise_project_or_default of this ShowResourceTagResponse.
        :rtype: str
        """
        return self._enterprise_project_or_default

    @enterprise_project_or_default.setter
    def enterprise_project_or_default(self, enterprise_project_or_default):
        """Sets the enterprise_project_or_default of this ShowResourceTagResponse.

        企业项目或默认项目

        :param enterprise_project_or_default: The enterprise_project_or_default of this ShowResourceTagResponse.
        :type enterprise_project_or_default: str
        """
        self._enterprise_project_or_default = enterprise_project_or_default

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
        if not isinstance(other, ShowResourceTagResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
