# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SearchCorpDigitalInfoListRequest:

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
        'x_conference_authorization': 'str',
        'type': 'str',
        'language': 'str'
    }

    attribute_map = {
        'conference_id': 'conferenceID',
        'x_conference_authorization': 'X-Conference-Authorization',
        'type': 'type',
        'language': 'language'
    }

    def __init__(self, conference_id=None, x_conference_authorization=None, type=None, language=None):
        """SearchCorpDigitalInfoListRequest

        The model defined in huaweicloud sdk

        :param conference_id: 会议ID。
        :type conference_id: str
        :param x_conference_authorization: 会控Token，通过[[获取会控token](https://support.huaweicloud.com/api-meeting/meeting_21_0027.html)](tag:hws)[[获取会控token](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0027.html)](tag:hk)接口获得。
        :type x_conference_authorization: str
        :param type: 查询类型，PUBLIC：公共、LOCAL：本地会议。
        :type type: str
        :param language: 传译语言。
        :type language: str
        """
        
        

        self._conference_id = None
        self._x_conference_authorization = None
        self._type = None
        self._language = None
        self.discriminator = None

        self.conference_id = conference_id
        self.x_conference_authorization = x_conference_authorization
        self.type = type
        self.language = language

    @property
    def conference_id(self):
        """Gets the conference_id of this SearchCorpDigitalInfoListRequest.

        会议ID。

        :return: The conference_id of this SearchCorpDigitalInfoListRequest.
        :rtype: str
        """
        return self._conference_id

    @conference_id.setter
    def conference_id(self, conference_id):
        """Sets the conference_id of this SearchCorpDigitalInfoListRequest.

        会议ID。

        :param conference_id: The conference_id of this SearchCorpDigitalInfoListRequest.
        :type conference_id: str
        """
        self._conference_id = conference_id

    @property
    def x_conference_authorization(self):
        """Gets the x_conference_authorization of this SearchCorpDigitalInfoListRequest.

        会控Token，通过[[获取会控token](https://support.huaweicloud.com/api-meeting/meeting_21_0027.html)](tag:hws)[[获取会控token](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0027.html)](tag:hk)接口获得。

        :return: The x_conference_authorization of this SearchCorpDigitalInfoListRequest.
        :rtype: str
        """
        return self._x_conference_authorization

    @x_conference_authorization.setter
    def x_conference_authorization(self, x_conference_authorization):
        """Sets the x_conference_authorization of this SearchCorpDigitalInfoListRequest.

        会控Token，通过[[获取会控token](https://support.huaweicloud.com/api-meeting/meeting_21_0027.html)](tag:hws)[[获取会控token](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0027.html)](tag:hk)接口获得。

        :param x_conference_authorization: The x_conference_authorization of this SearchCorpDigitalInfoListRequest.
        :type x_conference_authorization: str
        """
        self._x_conference_authorization = x_conference_authorization

    @property
    def type(self):
        """Gets the type of this SearchCorpDigitalInfoListRequest.

        查询类型，PUBLIC：公共、LOCAL：本地会议。

        :return: The type of this SearchCorpDigitalInfoListRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SearchCorpDigitalInfoListRequest.

        查询类型，PUBLIC：公共、LOCAL：本地会议。

        :param type: The type of this SearchCorpDigitalInfoListRequest.
        :type type: str
        """
        self._type = type

    @property
    def language(self):
        """Gets the language of this SearchCorpDigitalInfoListRequest.

        传译语言。

        :return: The language of this SearchCorpDigitalInfoListRequest.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this SearchCorpDigitalInfoListRequest.

        传译语言。

        :param language: The language of this SearchCorpDigitalInfoListRequest.
        :type language: str
        """
        self._language = language

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
        if not isinstance(other, SearchCorpDigitalInfoListRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
