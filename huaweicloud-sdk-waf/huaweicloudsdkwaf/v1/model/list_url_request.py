# coding: utf-8

import re
import six





class ListUrlRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'top': 'str',
        'recent': 'str',
        '_from': 'int',
        'to': 'int',
        'hosts': 'list[str]',
        'instances': 'list[str]'
    }

    attribute_map = {
        'top': 'top',
        'recent': 'recent',
        '_from': 'from',
        'to': 'to',
        'hosts': 'hosts',
        'instances': 'instances'
    }

    def __init__(self, top=None, recent=None, _from=None, to=None, hosts=None, instances=None):
        """ListUrlRequest - a model defined in huaweicloud sdk"""
        
        

        self._top = None
        self._recent = None
        self.__from = None
        self._to = None
        self._hosts = None
        self._instances = None
        self.discriminator = None

        self.top = top
        if recent is not None:
            self.recent = recent
        if _from is not None:
            self._from = _from
        if to is not None:
            self.to = to
        if hosts is not None:
            self.hosts = hosts
        if instances is not None:
            self.instances = instances

    @property
    def top(self):
        """Gets the top of this ListUrlRequest.

        受攻击次数最多的几条url

        :return: The top of this ListUrlRequest.
        :rtype: str
        """
        return self._top

    @top.setter
    def top(self, top):
        """Sets the top of this ListUrlRequest.

        受攻击次数最多的几条url

        :param top: The top of this ListUrlRequest.
        :type: str
        """
        self._top = top

    @property
    def recent(self):
        """Gets the recent of this ListUrlRequest.

        要查询事件时间范围

        :return: The recent of this ListUrlRequest.
        :rtype: str
        """
        return self._recent

    @recent.setter
    def recent(self, recent):
        """Sets the recent of this ListUrlRequest.

        要查询事件时间范围

        :param recent: The recent of this ListUrlRequest.
        :type: str
        """
        self._recent = recent

    @property
    def _from(self):
        """Gets the _from of this ListUrlRequest.

        起始时间戳

        :return: The _from of this ListUrlRequest.
        :rtype: int
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this ListUrlRequest.

        起始时间戳

        :param _from: The _from of this ListUrlRequest.
        :type: int
        """
        self.__from = _from

    @property
    def to(self):
        """Gets the to of this ListUrlRequest.

        截止时间戳

        :return: The to of this ListUrlRequest.
        :rtype: int
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this ListUrlRequest.

        截止时间戳

        :param to: The to of this ListUrlRequest.
        :type: int
        """
        self._to = to

    @property
    def hosts(self):
        """Gets the hosts of this ListUrlRequest.

        要查询事件的域名列表

        :return: The hosts of this ListUrlRequest.
        :rtype: list[str]
        """
        return self._hosts

    @hosts.setter
    def hosts(self, hosts):
        """Sets the hosts of this ListUrlRequest.

        要查询事件的域名列表

        :param hosts: The hosts of this ListUrlRequest.
        :type: list[str]
        """
        self._hosts = hosts

    @property
    def instances(self):
        """Gets the instances of this ListUrlRequest.

        域名

        :return: The instances of this ListUrlRequest.
        :rtype: list[str]
        """
        return self._instances

    @instances.setter
    def instances(self, instances):
        """Sets the instances of this ListUrlRequest.

        域名

        :param instances: The instances of this ListUrlRequest.
        :type: list[str]
        """
        self._instances = instances

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
        if not isinstance(other, ListUrlRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
