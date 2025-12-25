# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListImageMembersResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'members': 'list[ImageMember]',
        'schema': 'str',
        'page_info': 'GlancePageInfo'
    }

    attribute_map = {
        'members': 'members',
        'schema': 'schema',
        'page_info': 'page_info'
    }

    def __init__(self, members=None, schema=None, page_info=None):
        r"""ListImageMembersResponse

        The model defined in huaweicloud sdk

        :param members: 成员信息
        :type members: list[:class:`huaweicloudsdkims.v2.ImageMember`]
        :param schema: 视图信息
        :type schema: str
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkims.v2.GlancePageInfo`
        """
        
        super().__init__()

        self._members = None
        self._schema = None
        self._page_info = None
        self.discriminator = None

        if members is not None:
            self.members = members
        if schema is not None:
            self.schema = schema
        if page_info is not None:
            self.page_info = page_info

    @property
    def members(self):
        r"""Gets the members of this ListImageMembersResponse.

        成员信息

        :return: The members of this ListImageMembersResponse.
        :rtype: list[:class:`huaweicloudsdkims.v2.ImageMember`]
        """
        return self._members

    @members.setter
    def members(self, members):
        r"""Sets the members of this ListImageMembersResponse.

        成员信息

        :param members: The members of this ListImageMembersResponse.
        :type members: list[:class:`huaweicloudsdkims.v2.ImageMember`]
        """
        self._members = members

    @property
    def schema(self):
        r"""Gets the schema of this ListImageMembersResponse.

        视图信息

        :return: The schema of this ListImageMembersResponse.
        :rtype: str
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        r"""Sets the schema of this ListImageMembersResponse.

        视图信息

        :param schema: The schema of this ListImageMembersResponse.
        :type schema: str
        """
        self._schema = schema

    @property
    def page_info(self):
        r"""Gets the page_info of this ListImageMembersResponse.

        :return: The page_info of this ListImageMembersResponse.
        :rtype: :class:`huaweicloudsdkims.v2.GlancePageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ListImageMembersResponse.

        :param page_info: The page_info of this ListImageMembersResponse.
        :type page_info: :class:`huaweicloudsdkims.v2.GlancePageInfo`
        """
        self._page_info = page_info

    def to_dict(self):
        import warnings
        warnings.warn("ListImageMembersResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListImageMembersResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
