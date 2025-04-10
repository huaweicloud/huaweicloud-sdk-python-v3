# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StaticRouteItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'prefix': 'str',
        'next_hop': 'str',
        'interface_name': 'str',
        'priority': 'int',
        'track_nqa': 'bool',
        'post_to_cloud': 'bool'
    }

    attribute_map = {
        'prefix': 'prefix',
        'next_hop': 'next_hop',
        'interface_name': 'interface_name',
        'priority': 'priority',
        'track_nqa': 'track_nqa',
        'post_to_cloud': 'post_to_cloud'
    }

    def __init__(self, prefix=None, next_hop=None, interface_name=None, priority=None, track_nqa=None, post_to_cloud=None):
        r"""StaticRouteItem

        The model defined in huaweicloud sdk

        :param prefix: 目标网络
        :type prefix: str
        :param next_hop: 下一跳地址
        :type next_hop: str
        :param interface_name: 接口名字
        :type interface_name: str
        :param priority: 优先级
        :type priority: int
        :param track_nqa: 自动检测
        :type track_nqa: bool
        :param post_to_cloud: 发布到企业连接网络
        :type post_to_cloud: bool
        """
        
        

        self._prefix = None
        self._next_hop = None
        self._interface_name = None
        self._priority = None
        self._track_nqa = None
        self._post_to_cloud = None
        self.discriminator = None

        self.prefix = prefix
        self.next_hop = next_hop
        self.interface_name = interface_name
        if priority is not None:
            self.priority = priority
        self.track_nqa = track_nqa
        self.post_to_cloud = post_to_cloud

    @property
    def prefix(self):
        r"""Gets the prefix of this StaticRouteItem.

        目标网络

        :return: The prefix of this StaticRouteItem.
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        r"""Sets the prefix of this StaticRouteItem.

        目标网络

        :param prefix: The prefix of this StaticRouteItem.
        :type prefix: str
        """
        self._prefix = prefix

    @property
    def next_hop(self):
        r"""Gets the next_hop of this StaticRouteItem.

        下一跳地址

        :return: The next_hop of this StaticRouteItem.
        :rtype: str
        """
        return self._next_hop

    @next_hop.setter
    def next_hop(self, next_hop):
        r"""Sets the next_hop of this StaticRouteItem.

        下一跳地址

        :param next_hop: The next_hop of this StaticRouteItem.
        :type next_hop: str
        """
        self._next_hop = next_hop

    @property
    def interface_name(self):
        r"""Gets the interface_name of this StaticRouteItem.

        接口名字

        :return: The interface_name of this StaticRouteItem.
        :rtype: str
        """
        return self._interface_name

    @interface_name.setter
    def interface_name(self, interface_name):
        r"""Sets the interface_name of this StaticRouteItem.

        接口名字

        :param interface_name: The interface_name of this StaticRouteItem.
        :type interface_name: str
        """
        self._interface_name = interface_name

    @property
    def priority(self):
        r"""Gets the priority of this StaticRouteItem.

        优先级

        :return: The priority of this StaticRouteItem.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        r"""Sets the priority of this StaticRouteItem.

        优先级

        :param priority: The priority of this StaticRouteItem.
        :type priority: int
        """
        self._priority = priority

    @property
    def track_nqa(self):
        r"""Gets the track_nqa of this StaticRouteItem.

        自动检测

        :return: The track_nqa of this StaticRouteItem.
        :rtype: bool
        """
        return self._track_nqa

    @track_nqa.setter
    def track_nqa(self, track_nqa):
        r"""Sets the track_nqa of this StaticRouteItem.

        自动检测

        :param track_nqa: The track_nqa of this StaticRouteItem.
        :type track_nqa: bool
        """
        self._track_nqa = track_nqa

    @property
    def post_to_cloud(self):
        r"""Gets the post_to_cloud of this StaticRouteItem.

        发布到企业连接网络

        :return: The post_to_cloud of this StaticRouteItem.
        :rtype: bool
        """
        return self._post_to_cloud

    @post_to_cloud.setter
    def post_to_cloud(self, post_to_cloud):
        r"""Sets the post_to_cloud of this StaticRouteItem.

        发布到企业连接网络

        :param post_to_cloud: The post_to_cloud of this StaticRouteItem.
        :type post_to_cloud: bool
        """
        self._post_to_cloud = post_to_cloud

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
        if not isinstance(other, StaticRouteItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
