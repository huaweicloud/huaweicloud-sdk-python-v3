# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CollectHotQuestionsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'qabot_id': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'top': 'int',
        'domain': 'str',
        'domain_id': 'str',
        'exclude': 'bool'
    }

    attribute_map = {
        'qabot_id': 'qabot_id',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'top': 'top',
        'domain': 'domain',
        'domain_id': 'domain_id',
        'exclude': 'exclude'
    }

    def __init__(self, qabot_id=None, start_time=None, end_time=None, top=None, domain=None, domain_id=None, exclude=None):
        """CollectHotQuestionsRequest

        The model defined in huaweicloud sdk

        :param qabot_id: qabot编号，UUID格式。
        :type qabot_id: str
        :param start_time: 查询的起始时间，long，UTC时间，默认值为0。
        :type start_time: str
        :param end_time: 查询的结束时间，long，UTC时间，默认值为当前时间的毫秒数。
        :type end_time: str
        :param top: 热点问题最多显示的个数，默认值为10，取值范围1-20。
        :type top: int
        :param domain: 热点问题所属的领域。如果指定领域为非空字符串则从指定领域中查询热点问题，否则从所有标准问题中查询热点问题。
        :type domain: str
        :param domain_id: 统计的目标问题类别id。
        :type domain_id: str
        :param exclude: true:根据问答对信息展示热点问题（如：热点问题对应的问答对“你好”发生了修改，变成了 “你好啊”，此时热点问题也将返回 “你好啊”；但是如果这个问题对被删除，则“你好”不会被展示在热点问中） false: 不根据问答对信息展示热点问题。
        :type exclude: bool
        """
        
        

        self._qabot_id = None
        self._start_time = None
        self._end_time = None
        self._top = None
        self._domain = None
        self._domain_id = None
        self._exclude = None
        self.discriminator = None

        self.qabot_id = qabot_id
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if top is not None:
            self.top = top
        if domain is not None:
            self.domain = domain
        if domain_id is not None:
            self.domain_id = domain_id
        if exclude is not None:
            self.exclude = exclude

    @property
    def qabot_id(self):
        """Gets the qabot_id of this CollectHotQuestionsRequest.

        qabot编号，UUID格式。

        :return: The qabot_id of this CollectHotQuestionsRequest.
        :rtype: str
        """
        return self._qabot_id

    @qabot_id.setter
    def qabot_id(self, qabot_id):
        """Sets the qabot_id of this CollectHotQuestionsRequest.

        qabot编号，UUID格式。

        :param qabot_id: The qabot_id of this CollectHotQuestionsRequest.
        :type qabot_id: str
        """
        self._qabot_id = qabot_id

    @property
    def start_time(self):
        """Gets the start_time of this CollectHotQuestionsRequest.

        查询的起始时间，long，UTC时间，默认值为0。

        :return: The start_time of this CollectHotQuestionsRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this CollectHotQuestionsRequest.

        查询的起始时间，long，UTC时间，默认值为0。

        :param start_time: The start_time of this CollectHotQuestionsRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this CollectHotQuestionsRequest.

        查询的结束时间，long，UTC时间，默认值为当前时间的毫秒数。

        :return: The end_time of this CollectHotQuestionsRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this CollectHotQuestionsRequest.

        查询的结束时间，long，UTC时间，默认值为当前时间的毫秒数。

        :param end_time: The end_time of this CollectHotQuestionsRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def top(self):
        """Gets the top of this CollectHotQuestionsRequest.

        热点问题最多显示的个数，默认值为10，取值范围1-20。

        :return: The top of this CollectHotQuestionsRequest.
        :rtype: int
        """
        return self._top

    @top.setter
    def top(self, top):
        """Sets the top of this CollectHotQuestionsRequest.

        热点问题最多显示的个数，默认值为10，取值范围1-20。

        :param top: The top of this CollectHotQuestionsRequest.
        :type top: int
        """
        self._top = top

    @property
    def domain(self):
        """Gets the domain of this CollectHotQuestionsRequest.

        热点问题所属的领域。如果指定领域为非空字符串则从指定领域中查询热点问题，否则从所有标准问题中查询热点问题。

        :return: The domain of this CollectHotQuestionsRequest.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this CollectHotQuestionsRequest.

        热点问题所属的领域。如果指定领域为非空字符串则从指定领域中查询热点问题，否则从所有标准问题中查询热点问题。

        :param domain: The domain of this CollectHotQuestionsRequest.
        :type domain: str
        """
        self._domain = domain

    @property
    def domain_id(self):
        """Gets the domain_id of this CollectHotQuestionsRequest.

        统计的目标问题类别id。

        :return: The domain_id of this CollectHotQuestionsRequest.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this CollectHotQuestionsRequest.

        统计的目标问题类别id。

        :param domain_id: The domain_id of this CollectHotQuestionsRequest.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def exclude(self):
        """Gets the exclude of this CollectHotQuestionsRequest.

        true:根据问答对信息展示热点问题（如：热点问题对应的问答对“你好”发生了修改，变成了 “你好啊”，此时热点问题也将返回 “你好啊”；但是如果这个问题对被删除，则“你好”不会被展示在热点问中） false: 不根据问答对信息展示热点问题。

        :return: The exclude of this CollectHotQuestionsRequest.
        :rtype: bool
        """
        return self._exclude

    @exclude.setter
    def exclude(self, exclude):
        """Sets the exclude of this CollectHotQuestionsRequest.

        true:根据问答对信息展示热点问题（如：热点问题对应的问答对“你好”发生了修改，变成了 “你好啊”，此时热点问题也将返回 “你好啊”；但是如果这个问题对被删除，则“你好”不会被展示在热点问中） false: 不根据问答对信息展示热点问题。

        :param exclude: The exclude of this CollectHotQuestionsRequest.
        :type exclude: bool
        """
        self._exclude = exclude

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
        if not isinstance(other, CollectHotQuestionsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
