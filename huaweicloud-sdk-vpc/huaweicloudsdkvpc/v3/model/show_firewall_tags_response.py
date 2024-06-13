# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowFirewallTagsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tags': 'ResourceTag',
        'request_id': 'str',
        'sys_tags': 'ResourceTag'
    }

    attribute_map = {
        'tags': 'tags',
        'request_id': 'request_id',
        'sys_tags': 'sys_tags'
    }

    def __init__(self, tags=None, request_id=None, sys_tags=None):
        """ShowFirewallTagsResponse

        The model defined in huaweicloud sdk

        :param tags: 
        :type tags: :class:`huaweicloudsdkvpc.v3.ResourceTag`
        :param request_id: 请求ID
        :type request_id: str
        :param sys_tags: 
        :type sys_tags: :class:`huaweicloudsdkvpc.v3.ResourceTag`
        """
        
        super(ShowFirewallTagsResponse, self).__init__()

        self._tags = None
        self._request_id = None
        self._sys_tags = None
        self.discriminator = None

        if tags is not None:
            self.tags = tags
        if request_id is not None:
            self.request_id = request_id
        if sys_tags is not None:
            self.sys_tags = sys_tags

    @property
    def tags(self):
        """Gets the tags of this ShowFirewallTagsResponse.

        :return: The tags of this ShowFirewallTagsResponse.
        :rtype: :class:`huaweicloudsdkvpc.v3.ResourceTag`
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ShowFirewallTagsResponse.

        :param tags: The tags of this ShowFirewallTagsResponse.
        :type tags: :class:`huaweicloudsdkvpc.v3.ResourceTag`
        """
        self._tags = tags

    @property
    def request_id(self):
        """Gets the request_id of this ShowFirewallTagsResponse.

        请求ID

        :return: The request_id of this ShowFirewallTagsResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ShowFirewallTagsResponse.

        请求ID

        :param request_id: The request_id of this ShowFirewallTagsResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def sys_tags(self):
        """Gets the sys_tags of this ShowFirewallTagsResponse.

        :return: The sys_tags of this ShowFirewallTagsResponse.
        :rtype: :class:`huaweicloudsdkvpc.v3.ResourceTag`
        """
        return self._sys_tags

    @sys_tags.setter
    def sys_tags(self, sys_tags):
        """Sets the sys_tags of this ShowFirewallTagsResponse.

        :param sys_tags: The sys_tags of this ShowFirewallTagsResponse.
        :type sys_tags: :class:`huaweicloudsdkvpc.v3.ResourceTag`
        """
        self._sys_tags = sys_tags

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
        if not isinstance(other, ShowFirewallTagsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
