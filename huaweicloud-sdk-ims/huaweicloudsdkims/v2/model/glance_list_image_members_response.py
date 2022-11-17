# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GlanceListImageMembersResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'members': 'list[GlanceImageMembers]',
        'schema': 'str'
    }

    attribute_map = {
        'members': 'members',
        'schema': 'schema'
    }

    def __init__(self, members=None, schema=None):
        """GlanceListImageMembersResponse

        The model defined in huaweicloud sdk

        :param members: 成员信息
        :type members: list[:class:`huaweicloudsdkims.v2.GlanceImageMembers`]
        :param schema: 视图信息
        :type schema: str
        """
        
        super(GlanceListImageMembersResponse, self).__init__()

        self._members = None
        self._schema = None
        self.discriminator = None

        if members is not None:
            self.members = members
        if schema is not None:
            self.schema = schema

    @property
    def members(self):
        """Gets the members of this GlanceListImageMembersResponse.

        成员信息

        :return: The members of this GlanceListImageMembersResponse.
        :rtype: list[:class:`huaweicloudsdkims.v2.GlanceImageMembers`]
        """
        return self._members

    @members.setter
    def members(self, members):
        """Sets the members of this GlanceListImageMembersResponse.

        成员信息

        :param members: The members of this GlanceListImageMembersResponse.
        :type members: list[:class:`huaweicloudsdkims.v2.GlanceImageMembers`]
        """
        self._members = members

    @property
    def schema(self):
        """Gets the schema of this GlanceListImageMembersResponse.

        视图信息

        :return: The schema of this GlanceListImageMembersResponse.
        :rtype: str
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """Sets the schema of this GlanceListImageMembersResponse.

        视图信息

        :param schema: The schema of this GlanceListImageMembersResponse.
        :type schema: str
        """
        self._schema = schema

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
        if not isinstance(other, GlanceListImageMembersResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
