# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateHttpIpGroupResponse(SdkResponse):

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
        'name': 'str',
        'ips': 'str',
        'size': 'str',
        'description': 'str',
        'timestamp': 'int',
        'rules': 'list[HttpRuleInfo]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'ips': 'ips',
        'size': 'size',
        'description': 'description',
        'timestamp': 'timestamp',
        'rules': 'rules'
    }

    def __init__(self, id=None, name=None, ips=None, size=None, description=None, timestamp=None, rules=None):
        r"""UpdateHttpIpGroupResponse

        The model defined in huaweicloud sdk

        :param id: IP地址组id
        :type id: str
        :param name: IP地址组名称
        :type name: str
        :param ips: IP地址/地址段
        :type ips: str
        :param size: IP地址/地址段大小
        :type size: str
        :param description: IP地址组备注
        :type description: str
        :param timestamp: 创建IP地址组的时间
        :type timestamp: int
        :param rules: 使用IP地址组的策略和规则列表
        :type rules: list[:class:`huaweicloudsdkedgesec.v2.HttpRuleInfo`]
        """
        
        super(UpdateHttpIpGroupResponse, self).__init__()

        self._id = None
        self._name = None
        self._ips = None
        self._size = None
        self._description = None
        self._timestamp = None
        self._rules = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if ips is not None:
            self.ips = ips
        if size is not None:
            self.size = size
        if description is not None:
            self.description = description
        if timestamp is not None:
            self.timestamp = timestamp
        if rules is not None:
            self.rules = rules

    @property
    def id(self):
        r"""Gets the id of this UpdateHttpIpGroupResponse.

        IP地址组id

        :return: The id of this UpdateHttpIpGroupResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this UpdateHttpIpGroupResponse.

        IP地址组id

        :param id: The id of this UpdateHttpIpGroupResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this UpdateHttpIpGroupResponse.

        IP地址组名称

        :return: The name of this UpdateHttpIpGroupResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateHttpIpGroupResponse.

        IP地址组名称

        :param name: The name of this UpdateHttpIpGroupResponse.
        :type name: str
        """
        self._name = name

    @property
    def ips(self):
        r"""Gets the ips of this UpdateHttpIpGroupResponse.

        IP地址/地址段

        :return: The ips of this UpdateHttpIpGroupResponse.
        :rtype: str
        """
        return self._ips

    @ips.setter
    def ips(self, ips):
        r"""Sets the ips of this UpdateHttpIpGroupResponse.

        IP地址/地址段

        :param ips: The ips of this UpdateHttpIpGroupResponse.
        :type ips: str
        """
        self._ips = ips

    @property
    def size(self):
        r"""Gets the size of this UpdateHttpIpGroupResponse.

        IP地址/地址段大小

        :return: The size of this UpdateHttpIpGroupResponse.
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this UpdateHttpIpGroupResponse.

        IP地址/地址段大小

        :param size: The size of this UpdateHttpIpGroupResponse.
        :type size: str
        """
        self._size = size

    @property
    def description(self):
        r"""Gets the description of this UpdateHttpIpGroupResponse.

        IP地址组备注

        :return: The description of this UpdateHttpIpGroupResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateHttpIpGroupResponse.

        IP地址组备注

        :param description: The description of this UpdateHttpIpGroupResponse.
        :type description: str
        """
        self._description = description

    @property
    def timestamp(self):
        r"""Gets the timestamp of this UpdateHttpIpGroupResponse.

        创建IP地址组的时间

        :return: The timestamp of this UpdateHttpIpGroupResponse.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        r"""Sets the timestamp of this UpdateHttpIpGroupResponse.

        创建IP地址组的时间

        :param timestamp: The timestamp of this UpdateHttpIpGroupResponse.
        :type timestamp: int
        """
        self._timestamp = timestamp

    @property
    def rules(self):
        r"""Gets the rules of this UpdateHttpIpGroupResponse.

        使用IP地址组的策略和规则列表

        :return: The rules of this UpdateHttpIpGroupResponse.
        :rtype: list[:class:`huaweicloudsdkedgesec.v2.HttpRuleInfo`]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        r"""Sets the rules of this UpdateHttpIpGroupResponse.

        使用IP地址组的策略和规则列表

        :param rules: The rules of this UpdateHttpIpGroupResponse.
        :type rules: list[:class:`huaweicloudsdkedgesec.v2.HttpRuleInfo`]
        """
        self._rules = rules

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
        if not isinstance(other, UpdateHttpIpGroupResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
