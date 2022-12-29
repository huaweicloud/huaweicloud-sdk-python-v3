# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListLineGroupsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'linegroups': 'list[CreateLineGroupsResp]',
        'metadata': 'Metadata'
    }

    attribute_map = {
        'linegroups': 'linegroups',
        'metadata': 'metadata'
    }

    def __init__(self, linegroups=None, metadata=None):
        """ListLineGroupsResponse

        The model defined in huaweicloud sdk

        :param linegroups: 列表对象。
        :type linegroups: list[:class:`huaweicloudsdkdns.v2.CreateLineGroupsResp`]
        :param metadata: 
        :type metadata: :class:`huaweicloudsdkdns.v2.Metadata`
        """
        
        super(ListLineGroupsResponse, self).__init__()

        self._linegroups = None
        self._metadata = None
        self.discriminator = None

        if linegroups is not None:
            self.linegroups = linegroups
        if metadata is not None:
            self.metadata = metadata

    @property
    def linegroups(self):
        """Gets the linegroups of this ListLineGroupsResponse.

        列表对象。

        :return: The linegroups of this ListLineGroupsResponse.
        :rtype: list[:class:`huaweicloudsdkdns.v2.CreateLineGroupsResp`]
        """
        return self._linegroups

    @linegroups.setter
    def linegroups(self, linegroups):
        """Sets the linegroups of this ListLineGroupsResponse.

        列表对象。

        :param linegroups: The linegroups of this ListLineGroupsResponse.
        :type linegroups: list[:class:`huaweicloudsdkdns.v2.CreateLineGroupsResp`]
        """
        self._linegroups = linegroups

    @property
    def metadata(self):
        """Gets the metadata of this ListLineGroupsResponse.

        :return: The metadata of this ListLineGroupsResponse.
        :rtype: :class:`huaweicloudsdkdns.v2.Metadata`
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this ListLineGroupsResponse.

        :param metadata: The metadata of this ListLineGroupsResponse.
        :type metadata: :class:`huaweicloudsdkdns.v2.Metadata`
        """
        self._metadata = metadata

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
        if not isinstance(other, ListLineGroupsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
