# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowMeetingDetailRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'conference_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'search_key': 'str',
        'user_uuid': 'str',
        'x_type': 'str',
        'x_query_type': 'str',
        'x_authorization_type': 'str',
        'x_site_id': 'str'
    }

    attribute_map = {
        'conference_id': 'conferenceID',
        'offset': 'offset',
        'limit': 'limit',
        'search_key': 'searchKey',
        'user_uuid': 'userUUID',
        'x_type': 'X-Type',
        'x_query_type': 'X-Query-Type',
        'x_authorization_type': 'X-Authorization-Type',
        'x_site_id': 'X-Site-Id'
    }

    def __init__(self, conference_id=None, offset=None, limit=None, search_key=None, user_uuid=None, x_type=None, x_query_type=None, x_authorization_type=None, x_site_id=None):
        """ShowMeetingDetailRequest

        The model defined in huaweicloud sdk

        :param conference_id: 会议ID。 &gt; 创建会议时返回的conferenceID。不是vmrConferenceID。 
        :type conference_id: str
        :param offset: 查询偏移量。默认为0。针对PageParticipant 中的与会者分页。
        :type offset: int
        :param limit: 查询数量。默认值20。
        :type limit: int
        :param search_key: 查询条件。长度限制为1-128个字符。
        :type search_key: str
        :param user_uuid: 用户的UUID。 &gt; 该参数将废弃，请勿使用。 
        :type user_uuid: str
        :param x_type: 默认值为0。 - 0: 不区分终端和与会人 - 1: 分页查询区分终端和与会人，结果合并返回 - 2: 单独查询终端和与会人，结果单独返回
        :type x_type: str
        :param x_query_type: 当X-Type为2时，有效。默认为0。 - 0: 查询与会人 - 1: 查询终端
        :type x_query_type: str
        :param x_authorization_type: 标识是否为第三方portal过来的请求。 &gt; 该参数将废弃，请勿使用。 
        :type x_authorization_type: str
        :param x_site_id: 用于区分到哪个HCSO站点鉴权。 &gt; 该参数将废弃，请勿使用。 
        :type x_site_id: str
        """
        
        

        self._conference_id = None
        self._offset = None
        self._limit = None
        self._search_key = None
        self._user_uuid = None
        self._x_type = None
        self._x_query_type = None
        self._x_authorization_type = None
        self._x_site_id = None
        self.discriminator = None

        self.conference_id = conference_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if search_key is not None:
            self.search_key = search_key
        if user_uuid is not None:
            self.user_uuid = user_uuid
        if x_type is not None:
            self.x_type = x_type
        if x_query_type is not None:
            self.x_query_type = x_query_type
        if x_authorization_type is not None:
            self.x_authorization_type = x_authorization_type
        if x_site_id is not None:
            self.x_site_id = x_site_id

    @property
    def conference_id(self):
        """Gets the conference_id of this ShowMeetingDetailRequest.

        会议ID。 > 创建会议时返回的conferenceID。不是vmrConferenceID。 

        :return: The conference_id of this ShowMeetingDetailRequest.
        :rtype: str
        """
        return self._conference_id

    @conference_id.setter
    def conference_id(self, conference_id):
        """Sets the conference_id of this ShowMeetingDetailRequest.

        会议ID。 > 创建会议时返回的conferenceID。不是vmrConferenceID。 

        :param conference_id: The conference_id of this ShowMeetingDetailRequest.
        :type conference_id: str
        """
        self._conference_id = conference_id

    @property
    def offset(self):
        """Gets the offset of this ShowMeetingDetailRequest.

        查询偏移量。默认为0。针对PageParticipant 中的与会者分页。

        :return: The offset of this ShowMeetingDetailRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ShowMeetingDetailRequest.

        查询偏移量。默认为0。针对PageParticipant 中的与会者分页。

        :param offset: The offset of this ShowMeetingDetailRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ShowMeetingDetailRequest.

        查询数量。默认值20。

        :return: The limit of this ShowMeetingDetailRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ShowMeetingDetailRequest.

        查询数量。默认值20。

        :param limit: The limit of this ShowMeetingDetailRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def search_key(self):
        """Gets the search_key of this ShowMeetingDetailRequest.

        查询条件。长度限制为1-128个字符。

        :return: The search_key of this ShowMeetingDetailRequest.
        :rtype: str
        """
        return self._search_key

    @search_key.setter
    def search_key(self, search_key):
        """Sets the search_key of this ShowMeetingDetailRequest.

        查询条件。长度限制为1-128个字符。

        :param search_key: The search_key of this ShowMeetingDetailRequest.
        :type search_key: str
        """
        self._search_key = search_key

    @property
    def user_uuid(self):
        """Gets the user_uuid of this ShowMeetingDetailRequest.

        用户的UUID。 > 该参数将废弃，请勿使用。 

        :return: The user_uuid of this ShowMeetingDetailRequest.
        :rtype: str
        """
        return self._user_uuid

    @user_uuid.setter
    def user_uuid(self, user_uuid):
        """Sets the user_uuid of this ShowMeetingDetailRequest.

        用户的UUID。 > 该参数将废弃，请勿使用。 

        :param user_uuid: The user_uuid of this ShowMeetingDetailRequest.
        :type user_uuid: str
        """
        self._user_uuid = user_uuid

    @property
    def x_type(self):
        """Gets the x_type of this ShowMeetingDetailRequest.

        默认值为0。 - 0: 不区分终端和与会人 - 1: 分页查询区分终端和与会人，结果合并返回 - 2: 单独查询终端和与会人，结果单独返回

        :return: The x_type of this ShowMeetingDetailRequest.
        :rtype: str
        """
        return self._x_type

    @x_type.setter
    def x_type(self, x_type):
        """Sets the x_type of this ShowMeetingDetailRequest.

        默认值为0。 - 0: 不区分终端和与会人 - 1: 分页查询区分终端和与会人，结果合并返回 - 2: 单独查询终端和与会人，结果单独返回

        :param x_type: The x_type of this ShowMeetingDetailRequest.
        :type x_type: str
        """
        self._x_type = x_type

    @property
    def x_query_type(self):
        """Gets the x_query_type of this ShowMeetingDetailRequest.

        当X-Type为2时，有效。默认为0。 - 0: 查询与会人 - 1: 查询终端

        :return: The x_query_type of this ShowMeetingDetailRequest.
        :rtype: str
        """
        return self._x_query_type

    @x_query_type.setter
    def x_query_type(self, x_query_type):
        """Sets the x_query_type of this ShowMeetingDetailRequest.

        当X-Type为2时，有效。默认为0。 - 0: 查询与会人 - 1: 查询终端

        :param x_query_type: The x_query_type of this ShowMeetingDetailRequest.
        :type x_query_type: str
        """
        self._x_query_type = x_query_type

    @property
    def x_authorization_type(self):
        """Gets the x_authorization_type of this ShowMeetingDetailRequest.

        标识是否为第三方portal过来的请求。 > 该参数将废弃，请勿使用。 

        :return: The x_authorization_type of this ShowMeetingDetailRequest.
        :rtype: str
        """
        return self._x_authorization_type

    @x_authorization_type.setter
    def x_authorization_type(self, x_authorization_type):
        """Sets the x_authorization_type of this ShowMeetingDetailRequest.

        标识是否为第三方portal过来的请求。 > 该参数将废弃，请勿使用。 

        :param x_authorization_type: The x_authorization_type of this ShowMeetingDetailRequest.
        :type x_authorization_type: str
        """
        self._x_authorization_type = x_authorization_type

    @property
    def x_site_id(self):
        """Gets the x_site_id of this ShowMeetingDetailRequest.

        用于区分到哪个HCSO站点鉴权。 > 该参数将废弃，请勿使用。 

        :return: The x_site_id of this ShowMeetingDetailRequest.
        :rtype: str
        """
        return self._x_site_id

    @x_site_id.setter
    def x_site_id(self, x_site_id):
        """Sets the x_site_id of this ShowMeetingDetailRequest.

        用于区分到哪个HCSO站点鉴权。 > 该参数将废弃，请勿使用。 

        :param x_site_id: The x_site_id of this ShowMeetingDetailRequest.
        :type x_site_id: str
        """
        self._x_site_id = x_site_id

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
        if not isinstance(other, ShowMeetingDetailRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
