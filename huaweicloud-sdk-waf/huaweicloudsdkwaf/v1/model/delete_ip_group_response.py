# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteIpGroupResponse(SdkResponse):

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
        'size': 'int',
        'rules': 'list[RuleInfo]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'ips': 'ips',
        'size': 'size',
        'rules': 'rules'
    }

    def __init__(self, id=None, name=None, ips=None, size=None, rules=None):
        """DeleteIpGroupResponse

        The model defined in huaweicloud sdk

        :param id: 地址组id
        :type id: str
        :param name: 地址组名称
        :type name: str
        :param ips: 地址组ip（以逗号分隔的ip或ip段）
        :type ips: str
        :param size: 地址组长度
        :type size: int
        :param rules: ip地址组绑定的规则列表
        :type rules: list[:class:`huaweicloudsdkwaf.v1.RuleInfo`]
        """
        
        super(DeleteIpGroupResponse, self).__init__()

        self._id = None
        self._name = None
        self._ips = None
        self._size = None
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
        if rules is not None:
            self.rules = rules

    @property
    def id(self):
        """Gets the id of this DeleteIpGroupResponse.

        地址组id

        :return: The id of this DeleteIpGroupResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DeleteIpGroupResponse.

        地址组id

        :param id: The id of this DeleteIpGroupResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this DeleteIpGroupResponse.

        地址组名称

        :return: The name of this DeleteIpGroupResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DeleteIpGroupResponse.

        地址组名称

        :param name: The name of this DeleteIpGroupResponse.
        :type name: str
        """
        self._name = name

    @property
    def ips(self):
        """Gets the ips of this DeleteIpGroupResponse.

        地址组ip（以逗号分隔的ip或ip段）

        :return: The ips of this DeleteIpGroupResponse.
        :rtype: str
        """
        return self._ips

    @ips.setter
    def ips(self, ips):
        """Sets the ips of this DeleteIpGroupResponse.

        地址组ip（以逗号分隔的ip或ip段）

        :param ips: The ips of this DeleteIpGroupResponse.
        :type ips: str
        """
        self._ips = ips

    @property
    def size(self):
        """Gets the size of this DeleteIpGroupResponse.

        地址组长度

        :return: The size of this DeleteIpGroupResponse.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this DeleteIpGroupResponse.

        地址组长度

        :param size: The size of this DeleteIpGroupResponse.
        :type size: int
        """
        self._size = size

    @property
    def rules(self):
        """Gets the rules of this DeleteIpGroupResponse.

        ip地址组绑定的规则列表

        :return: The rules of this DeleteIpGroupResponse.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.RuleInfo`]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """Sets the rules of this DeleteIpGroupResponse.

        ip地址组绑定的规则列表

        :param rules: The rules of this DeleteIpGroupResponse.
        :type rules: list[:class:`huaweicloudsdkwaf.v1.RuleInfo`]
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
        if not isinstance(other, DeleteIpGroupResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
