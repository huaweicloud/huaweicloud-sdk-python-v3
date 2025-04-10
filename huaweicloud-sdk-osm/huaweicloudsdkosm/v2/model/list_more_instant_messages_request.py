# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListMoreInstantMessagesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'case_id': 'str',
        'create_time': 'str',
        'type': 'int',
        'group_id': 'str',
        'limit': 'int',
        'x_site': 'int',
        'x_language': 'str',
        'x_time_zone': 'str'
    }

    attribute_map = {
        'case_id': 'case_id',
        'create_time': 'create_time',
        'type': 'type',
        'group_id': 'group_id',
        'limit': 'limit',
        'x_site': 'X-Site',
        'x_language': 'X-Language',
        'x_time_zone': 'X-Time-Zone'
    }

    def __init__(self, case_id=None, create_time=None, type=None, group_id=None, limit=None, x_site=None, x_language=None, x_time_zone=None):
        r"""ListMoreInstantMessagesRequest

        The model defined in huaweicloud sdk

        :param case_id: 工单id
        :type case_id: str
        :param create_time: 创建时间，时间戳
        :type create_time: str
        :param type: 上一条消息的留言方式 0是客户留言 1是客服回留言
        :type type: int
        :param group_id: 华为云IAM组id，同组其他工单时，该id必传
        :type group_id: str
        :param limit: 查询数量
        :type limit: int
        :param x_site: 对接站点信息。  0（中国站） 1（国际站），不填的话默认为0。
        :type x_site: int
        :param x_language: 语言环境，值为通用的语言描述字符串，比如zh-cn等，默认为zh-cn。  会根据语言环境对应展示一些国际化的信息，比如工单类型名称等。
        :type x_language: str
        :param x_time_zone: 环境时区，值为通用的时区描述字符串，比如GMT+8等，默认为GMT+8。  涉及时间的数据会根据环境时区处理。
        :type x_time_zone: str
        """
        
        

        self._case_id = None
        self._create_time = None
        self._type = None
        self._group_id = None
        self._limit = None
        self._x_site = None
        self._x_language = None
        self._x_time_zone = None
        self.discriminator = None

        self.case_id = case_id
        self.create_time = create_time
        self.type = type
        if group_id is not None:
            self.group_id = group_id
        self.limit = limit
        if x_site is not None:
            self.x_site = x_site
        if x_language is not None:
            self.x_language = x_language
        if x_time_zone is not None:
            self.x_time_zone = x_time_zone

    @property
    def case_id(self):
        r"""Gets the case_id of this ListMoreInstantMessagesRequest.

        工单id

        :return: The case_id of this ListMoreInstantMessagesRequest.
        :rtype: str
        """
        return self._case_id

    @case_id.setter
    def case_id(self, case_id):
        r"""Sets the case_id of this ListMoreInstantMessagesRequest.

        工单id

        :param case_id: The case_id of this ListMoreInstantMessagesRequest.
        :type case_id: str
        """
        self._case_id = case_id

    @property
    def create_time(self):
        r"""Gets the create_time of this ListMoreInstantMessagesRequest.

        创建时间，时间戳

        :return: The create_time of this ListMoreInstantMessagesRequest.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ListMoreInstantMessagesRequest.

        创建时间，时间戳

        :param create_time: The create_time of this ListMoreInstantMessagesRequest.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def type(self):
        r"""Gets the type of this ListMoreInstantMessagesRequest.

        上一条消息的留言方式 0是客户留言 1是客服回留言

        :return: The type of this ListMoreInstantMessagesRequest.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListMoreInstantMessagesRequest.

        上一条消息的留言方式 0是客户留言 1是客服回留言

        :param type: The type of this ListMoreInstantMessagesRequest.
        :type type: int
        """
        self._type = type

    @property
    def group_id(self):
        r"""Gets the group_id of this ListMoreInstantMessagesRequest.

        华为云IAM组id，同组其他工单时，该id必传

        :return: The group_id of this ListMoreInstantMessagesRequest.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this ListMoreInstantMessagesRequest.

        华为云IAM组id，同组其他工单时，该id必传

        :param group_id: The group_id of this ListMoreInstantMessagesRequest.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def limit(self):
        r"""Gets the limit of this ListMoreInstantMessagesRequest.

        查询数量

        :return: The limit of this ListMoreInstantMessagesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListMoreInstantMessagesRequest.

        查询数量

        :param limit: The limit of this ListMoreInstantMessagesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def x_site(self):
        r"""Gets the x_site of this ListMoreInstantMessagesRequest.

        对接站点信息。  0（中国站） 1（国际站），不填的话默认为0。

        :return: The x_site of this ListMoreInstantMessagesRequest.
        :rtype: int
        """
        return self._x_site

    @x_site.setter
    def x_site(self, x_site):
        r"""Sets the x_site of this ListMoreInstantMessagesRequest.

        对接站点信息。  0（中国站） 1（国际站），不填的话默认为0。

        :param x_site: The x_site of this ListMoreInstantMessagesRequest.
        :type x_site: int
        """
        self._x_site = x_site

    @property
    def x_language(self):
        r"""Gets the x_language of this ListMoreInstantMessagesRequest.

        语言环境，值为通用的语言描述字符串，比如zh-cn等，默认为zh-cn。  会根据语言环境对应展示一些国际化的信息，比如工单类型名称等。

        :return: The x_language of this ListMoreInstantMessagesRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ListMoreInstantMessagesRequest.

        语言环境，值为通用的语言描述字符串，比如zh-cn等，默认为zh-cn。  会根据语言环境对应展示一些国际化的信息，比如工单类型名称等。

        :param x_language: The x_language of this ListMoreInstantMessagesRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def x_time_zone(self):
        r"""Gets the x_time_zone of this ListMoreInstantMessagesRequest.

        环境时区，值为通用的时区描述字符串，比如GMT+8等，默认为GMT+8。  涉及时间的数据会根据环境时区处理。

        :return: The x_time_zone of this ListMoreInstantMessagesRequest.
        :rtype: str
        """
        return self._x_time_zone

    @x_time_zone.setter
    def x_time_zone(self, x_time_zone):
        r"""Sets the x_time_zone of this ListMoreInstantMessagesRequest.

        环境时区，值为通用的时区描述字符串，比如GMT+8等，默认为GMT+8。  涉及时间的数据会根据环境时区处理。

        :param x_time_zone: The x_time_zone of this ListMoreInstantMessagesRequest.
        :type x_time_zone: str
        """
        self._x_time_zone = x_time_zone

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
        if not isinstance(other, ListMoreInstantMessagesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
