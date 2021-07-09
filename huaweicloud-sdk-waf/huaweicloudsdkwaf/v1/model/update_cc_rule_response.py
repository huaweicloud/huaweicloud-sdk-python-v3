# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class UpdateCcRuleResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'url': 'str',
        'limit_num': 'int',
        'limit_period': 'int',
        'lock_time': 'int',
        'tag_type': 'str',
        'tag_index': 'str',
        'action': 'CcrulesListInfoAction',
        'timestamp': 'int'
    }

    attribute_map = {
        'id': 'id',
        'url': 'url',
        'limit_num': 'limit_num',
        'limit_period': 'limit_period',
        'lock_time': 'lock_time',
        'tag_type': 'tag_type',
        'tag_index': 'tag_index',
        'action': 'action',
        'timestamp': 'timestamp'
    }

    def __init__(self, id=None, url=None, limit_num=None, limit_period=None, lock_time=None, tag_type=None, tag_index=None, action=None, timestamp=None):
        """UpdateCcRuleResponse - a model defined in huaweicloud sdk"""
        
        super(UpdateCcRuleResponse, self).__init__()

        self._id = None
        self._url = None
        self._limit_num = None
        self._limit_period = None
        self._lock_time = None
        self._tag_type = None
        self._tag_index = None
        self._action = None
        self._timestamp = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if url is not None:
            self.url = url
        if limit_num is not None:
            self.limit_num = limit_num
        if limit_period is not None:
            self.limit_period = limit_period
        if lock_time is not None:
            self.lock_time = lock_time
        if tag_type is not None:
            self.tag_type = tag_type
        if tag_index is not None:
            self.tag_index = tag_index
        if action is not None:
            self.action = action
        if timestamp is not None:
            self.timestamp = timestamp

    @property
    def id(self):
        """Gets the id of this UpdateCcRuleResponse.

        cc规则id

        :return: The id of this UpdateCcRuleResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UpdateCcRuleResponse.

        cc规则id

        :param id: The id of this UpdateCcRuleResponse.
        :type: str
        """
        self._id = id

    @property
    def url(self):
        """Gets the url of this UpdateCcRuleResponse.

        规则应用的url链接

        :return: The url of this UpdateCcRuleResponse.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this UpdateCcRuleResponse.

        规则应用的url链接

        :param url: The url of this UpdateCcRuleResponse.
        :type: str
        """
        self._url = url

    @property
    def limit_num(self):
        """Gets the limit_num of this UpdateCcRuleResponse.

        单个用户的周期内请求次数

        :return: The limit_num of this UpdateCcRuleResponse.
        :rtype: int
        """
        return self._limit_num

    @limit_num.setter
    def limit_num(self, limit_num):
        """Sets the limit_num of this UpdateCcRuleResponse.

        单个用户的周期内请求次数

        :param limit_num: The limit_num of this UpdateCcRuleResponse.
        :type: int
        """
        self._limit_num = limit_num

    @property
    def limit_period(self):
        """Gets the limit_period of this UpdateCcRuleResponse.

        限速周期

        :return: The limit_period of this UpdateCcRuleResponse.
        :rtype: int
        """
        return self._limit_period

    @limit_period.setter
    def limit_period(self, limit_period):
        """Sets the limit_period of this UpdateCcRuleResponse.

        限速周期

        :param limit_period: The limit_period of this UpdateCcRuleResponse.
        :type: int
        """
        self._limit_period = limit_period

    @property
    def lock_time(self):
        """Gets the lock_time of this UpdateCcRuleResponse.

        锁定时长

        :return: The lock_time of this UpdateCcRuleResponse.
        :rtype: int
        """
        return self._lock_time

    @lock_time.setter
    def lock_time(self, lock_time):
        """Sets the lock_time of this UpdateCcRuleResponse.

        锁定时长

        :param lock_time: The lock_time of this UpdateCcRuleResponse.
        :type: int
        """
        self._lock_time = lock_time

    @property
    def tag_type(self):
        """Gets the tag_type of this UpdateCcRuleResponse.

        防护模式

        :return: The tag_type of this UpdateCcRuleResponse.
        :rtype: str
        """
        return self._tag_type

    @tag_type.setter
    def tag_type(self, tag_type):
        """Sets the tag_type of this UpdateCcRuleResponse.

        防护模式

        :param tag_type: The tag_type of this UpdateCcRuleResponse.
        :type: str
        """
        self._tag_type = tag_type

    @property
    def tag_index(self):
        """Gets the tag_index of this UpdateCcRuleResponse.

        防护模式标签

        :return: The tag_index of this UpdateCcRuleResponse.
        :rtype: str
        """
        return self._tag_index

    @tag_index.setter
    def tag_index(self, tag_index):
        """Sets the tag_index of this UpdateCcRuleResponse.

        防护模式标签

        :param tag_index: The tag_index of this UpdateCcRuleResponse.
        :type: str
        """
        self._tag_index = tag_index

    @property
    def action(self):
        """Gets the action of this UpdateCcRuleResponse.


        :return: The action of this UpdateCcRuleResponse.
        :rtype: CcrulesListInfoAction
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this UpdateCcRuleResponse.


        :param action: The action of this UpdateCcRuleResponse.
        :type: CcrulesListInfoAction
        """
        self._action = action

    @property
    def timestamp(self):
        """Gets the timestamp of this UpdateCcRuleResponse.

        创建规则时间戳

        :return: The timestamp of this UpdateCcRuleResponse.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this UpdateCcRuleResponse.

        创建规则时间戳

        :param timestamp: The timestamp of this UpdateCcRuleResponse.
        :type: int
        """
        self._timestamp = timestamp

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
        import simplejson as json
        return json.dumps(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpdateCcRuleResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
