# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowIpGroupResponse(SdkResponse):

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
        'rules': 'list[RuleInfo]',
        'share_info': 'ShareInfo',
        'description': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'ips': 'ips',
        'size': 'size',
        'rules': 'rules',
        'share_info': 'share_info',
        'description': 'description'
    }

    def __init__(self, id=None, name=None, ips=None, size=None, rules=None, share_info=None, description=None):
        """ShowIpGroupResponse

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
        :param share_info: 
        :type share_info: :class:`huaweicloudsdkwaf.v1.ShareInfo`
        :param description: 地址组描述
        :type description: str
        """
        
        super(ShowIpGroupResponse, self).__init__()

        self._id = None
        self._name = None
        self._ips = None
        self._size = None
        self._rules = None
        self._share_info = None
        self._description = None
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
        if share_info is not None:
            self.share_info = share_info
        if description is not None:
            self.description = description

    @property
    def id(self):
        """Gets the id of this ShowIpGroupResponse.

        地址组id

        :return: The id of this ShowIpGroupResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowIpGroupResponse.

        地址组id

        :param id: The id of this ShowIpGroupResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ShowIpGroupResponse.

        地址组名称

        :return: The name of this ShowIpGroupResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowIpGroupResponse.

        地址组名称

        :param name: The name of this ShowIpGroupResponse.
        :type name: str
        """
        self._name = name

    @property
    def ips(self):
        """Gets the ips of this ShowIpGroupResponse.

        地址组ip（以逗号分隔的ip或ip段）

        :return: The ips of this ShowIpGroupResponse.
        :rtype: str
        """
        return self._ips

    @ips.setter
    def ips(self, ips):
        """Sets the ips of this ShowIpGroupResponse.

        地址组ip（以逗号分隔的ip或ip段）

        :param ips: The ips of this ShowIpGroupResponse.
        :type ips: str
        """
        self._ips = ips

    @property
    def size(self):
        """Gets the size of this ShowIpGroupResponse.

        地址组长度

        :return: The size of this ShowIpGroupResponse.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ShowIpGroupResponse.

        地址组长度

        :param size: The size of this ShowIpGroupResponse.
        :type size: int
        """
        self._size = size

    @property
    def rules(self):
        """Gets the rules of this ShowIpGroupResponse.

        ip地址组绑定的规则列表

        :return: The rules of this ShowIpGroupResponse.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.RuleInfo`]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """Sets the rules of this ShowIpGroupResponse.

        ip地址组绑定的规则列表

        :param rules: The rules of this ShowIpGroupResponse.
        :type rules: list[:class:`huaweicloudsdkwaf.v1.RuleInfo`]
        """
        self._rules = rules

    @property
    def share_info(self):
        """Gets the share_info of this ShowIpGroupResponse.

        :return: The share_info of this ShowIpGroupResponse.
        :rtype: :class:`huaweicloudsdkwaf.v1.ShareInfo`
        """
        return self._share_info

    @share_info.setter
    def share_info(self, share_info):
        """Sets the share_info of this ShowIpGroupResponse.

        :param share_info: The share_info of this ShowIpGroupResponse.
        :type share_info: :class:`huaweicloudsdkwaf.v1.ShareInfo`
        """
        self._share_info = share_info

    @property
    def description(self):
        """Gets the description of this ShowIpGroupResponse.

        地址组描述

        :return: The description of this ShowIpGroupResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ShowIpGroupResponse.

        地址组描述

        :param description: The description of this ShowIpGroupResponse.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, ShowIpGroupResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
