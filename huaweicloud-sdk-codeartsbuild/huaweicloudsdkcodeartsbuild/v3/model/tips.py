# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Tips:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'int',
        'next_action': 'int',
        'next_action_remain_day': 'int',
        'next_action_url': 'str'
    }

    attribute_map = {
        'status': 'status',
        'next_action': 'next_action',
        'next_action_remain_day': 'next_action_remain_day',
        'next_action_url': 'next_action_url'
    }

    def __init__(self, status=None, next_action=None, next_action_remain_day=None, next_action_url=None):
        r"""Tips

        The model defined in huaweicloud sdk

        :param status: 状态
        :type status: int
        :param next_action: 下一个活动日
        :type next_action: int
        :param next_action_remain_day: 下一个活动日剩余时间
        :type next_action_remain_day: int
        :param next_action_url: 名称
        :type next_action_url: str
        """
        
        

        self._status = None
        self._next_action = None
        self._next_action_remain_day = None
        self._next_action_url = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if next_action is not None:
            self.next_action = next_action
        if next_action_remain_day is not None:
            self.next_action_remain_day = next_action_remain_day
        if next_action_url is not None:
            self.next_action_url = next_action_url

    @property
    def status(self):
        r"""Gets the status of this Tips.

        状态

        :return: The status of this Tips.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this Tips.

        状态

        :param status: The status of this Tips.
        :type status: int
        """
        self._status = status

    @property
    def next_action(self):
        r"""Gets the next_action of this Tips.

        下一个活动日

        :return: The next_action of this Tips.
        :rtype: int
        """
        return self._next_action

    @next_action.setter
    def next_action(self, next_action):
        r"""Sets the next_action of this Tips.

        下一个活动日

        :param next_action: The next_action of this Tips.
        :type next_action: int
        """
        self._next_action = next_action

    @property
    def next_action_remain_day(self):
        r"""Gets the next_action_remain_day of this Tips.

        下一个活动日剩余时间

        :return: The next_action_remain_day of this Tips.
        :rtype: int
        """
        return self._next_action_remain_day

    @next_action_remain_day.setter
    def next_action_remain_day(self, next_action_remain_day):
        r"""Sets the next_action_remain_day of this Tips.

        下一个活动日剩余时间

        :param next_action_remain_day: The next_action_remain_day of this Tips.
        :type next_action_remain_day: int
        """
        self._next_action_remain_day = next_action_remain_day

    @property
    def next_action_url(self):
        r"""Gets the next_action_url of this Tips.

        名称

        :return: The next_action_url of this Tips.
        :rtype: str
        """
        return self._next_action_url

    @next_action_url.setter
    def next_action_url(self, next_action_url):
        r"""Sets the next_action_url of this Tips.

        名称

        :param next_action_url: The next_action_url of this Tips.
        :type next_action_url: str
        """
        self._next_action_url = next_action_url

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
        if not isinstance(other, Tips):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
