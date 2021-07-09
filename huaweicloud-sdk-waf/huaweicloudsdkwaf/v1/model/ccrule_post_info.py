# coding: utf-8

import re
import six





class CcrulePostInfo:


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
        'policyid': 'str',
        'status': 'int',
        'description': 'str',
        'mode': 'int',
        'unaggregation': 'bool',
        'prefix': 'bool',
        'total_num': 'int',
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
        'policyid': 'policyid',
        'status': 'status',
        'description': 'description',
        'mode': 'mode',
        'unaggregation': 'unaggregation',
        'prefix': 'prefix',
        'total_num': 'total_num',
        'url': 'url',
        'limit_num': 'limit_num',
        'limit_period': 'limit_period',
        'lock_time': 'lock_time',
        'tag_type': 'tag_type',
        'tag_index': 'tag_index',
        'action': 'action',
        'timestamp': 'timestamp'
    }

    def __init__(self, id=None, policyid=None, status=None, description=None, mode=None, unaggregation=None, prefix=None, total_num=None, url=None, limit_num=None, limit_period=None, lock_time=None, tag_type=None, tag_index=None, action=None, timestamp=None):
        """CcrulePostInfo - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._policyid = None
        self._status = None
        self._description = None
        self._mode = None
        self._unaggregation = None
        self._prefix = None
        self._total_num = None
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
        if policyid is not None:
            self.policyid = policyid
        if status is not None:
            self.status = status
        if description is not None:
            self.description = description
        if mode is not None:
            self.mode = mode
        if unaggregation is not None:
            self.unaggregation = unaggregation
        if prefix is not None:
            self.prefix = prefix
        if total_num is not None:
            self.total_num = total_num
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
        """Gets the id of this CcrulePostInfo.

        cc规则id

        :return: The id of this CcrulePostInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CcrulePostInfo.

        cc规则id

        :param id: The id of this CcrulePostInfo.
        :type: str
        """
        self._id = id

    @property
    def policyid(self):
        """Gets the policyid of this CcrulePostInfo.

        所属策略id

        :return: The policyid of this CcrulePostInfo.
        :rtype: str
        """
        return self._policyid

    @policyid.setter
    def policyid(self, policyid):
        """Sets the policyid of this CcrulePostInfo.

        所属策略id

        :param policyid: The policyid of this CcrulePostInfo.
        :type: str
        """
        self._policyid = policyid

    @property
    def status(self):
        """Gets the status of this CcrulePostInfo.

        状态

        :return: The status of this CcrulePostInfo.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CcrulePostInfo.

        状态

        :param status: The status of this CcrulePostInfo.
        :type: int
        """
        self._status = status

    @property
    def description(self):
        """Gets the description of this CcrulePostInfo.

        规则描述

        :return: The description of this CcrulePostInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CcrulePostInfo.

        规则描述

        :param description: The description of this CcrulePostInfo.
        :type: str
        """
        self._description = description

    @property
    def mode(self):
        """Gets the mode of this CcrulePostInfo.

        阻断模式

        :return: The mode of this CcrulePostInfo.
        :rtype: int
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this CcrulePostInfo.

        阻断模式

        :param mode: The mode of this CcrulePostInfo.
        :type: int
        """
        self._mode = mode

    @property
    def unaggregation(self):
        """Gets the unaggregation of this CcrulePostInfo.

        人机验证

        :return: The unaggregation of this CcrulePostInfo.
        :rtype: bool
        """
        return self._unaggregation

    @unaggregation.setter
    def unaggregation(self, unaggregation):
        """Sets the unaggregation of this CcrulePostInfo.

        人机验证

        :param unaggregation: The unaggregation of this CcrulePostInfo.
        :type: bool
        """
        self._unaggregation = unaggregation

    @property
    def prefix(self):
        """Gets the prefix of this CcrulePostInfo.

        前缀包含

        :return: The prefix of this CcrulePostInfo.
        :rtype: bool
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        """Sets the prefix of this CcrulePostInfo.

        前缀包含

        :param prefix: The prefix of this CcrulePostInfo.
        :type: bool
        """
        self._prefix = prefix

    @property
    def total_num(self):
        """Gets the total_num of this CcrulePostInfo.

        总数

        :return: The total_num of this CcrulePostInfo.
        :rtype: int
        """
        return self._total_num

    @total_num.setter
    def total_num(self, total_num):
        """Sets the total_num of this CcrulePostInfo.

        总数

        :param total_num: The total_num of this CcrulePostInfo.
        :type: int
        """
        self._total_num = total_num

    @property
    def url(self):
        """Gets the url of this CcrulePostInfo.

        规则应用的url链接

        :return: The url of this CcrulePostInfo.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this CcrulePostInfo.

        规则应用的url链接

        :param url: The url of this CcrulePostInfo.
        :type: str
        """
        self._url = url

    @property
    def limit_num(self):
        """Gets the limit_num of this CcrulePostInfo.

        单个用户的周期内请求次数

        :return: The limit_num of this CcrulePostInfo.
        :rtype: int
        """
        return self._limit_num

    @limit_num.setter
    def limit_num(self, limit_num):
        """Sets the limit_num of this CcrulePostInfo.

        单个用户的周期内请求次数

        :param limit_num: The limit_num of this CcrulePostInfo.
        :type: int
        """
        self._limit_num = limit_num

    @property
    def limit_period(self):
        """Gets the limit_period of this CcrulePostInfo.

        限速周期

        :return: The limit_period of this CcrulePostInfo.
        :rtype: int
        """
        return self._limit_period

    @limit_period.setter
    def limit_period(self, limit_period):
        """Sets the limit_period of this CcrulePostInfo.

        限速周期

        :param limit_period: The limit_period of this CcrulePostInfo.
        :type: int
        """
        self._limit_period = limit_period

    @property
    def lock_time(self):
        """Gets the lock_time of this CcrulePostInfo.

        锁定时长

        :return: The lock_time of this CcrulePostInfo.
        :rtype: int
        """
        return self._lock_time

    @lock_time.setter
    def lock_time(self, lock_time):
        """Sets the lock_time of this CcrulePostInfo.

        锁定时长

        :param lock_time: The lock_time of this CcrulePostInfo.
        :type: int
        """
        self._lock_time = lock_time

    @property
    def tag_type(self):
        """Gets the tag_type of this CcrulePostInfo.

        防护模式

        :return: The tag_type of this CcrulePostInfo.
        :rtype: str
        """
        return self._tag_type

    @tag_type.setter
    def tag_type(self, tag_type):
        """Sets the tag_type of this CcrulePostInfo.

        防护模式

        :param tag_type: The tag_type of this CcrulePostInfo.
        :type: str
        """
        self._tag_type = tag_type

    @property
    def tag_index(self):
        """Gets the tag_index of this CcrulePostInfo.

        防护模式标签

        :return: The tag_index of this CcrulePostInfo.
        :rtype: str
        """
        return self._tag_index

    @tag_index.setter
    def tag_index(self, tag_index):
        """Sets the tag_index of this CcrulePostInfo.

        防护模式标签

        :param tag_index: The tag_index of this CcrulePostInfo.
        :type: str
        """
        self._tag_index = tag_index

    @property
    def action(self):
        """Gets the action of this CcrulePostInfo.


        :return: The action of this CcrulePostInfo.
        :rtype: CcrulesListInfoAction
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this CcrulePostInfo.


        :param action: The action of this CcrulePostInfo.
        :type: CcrulesListInfoAction
        """
        self._action = action

    @property
    def timestamp(self):
        """Gets the timestamp of this CcrulePostInfo.

        创建规则时间戳

        :return: The timestamp of this CcrulePostInfo.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this CcrulePostInfo.

        创建规则时间戳

        :param timestamp: The timestamp of this CcrulePostInfo.
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
        if not isinstance(other, CcrulePostInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
