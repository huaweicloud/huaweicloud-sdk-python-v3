# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CommonPoolDict:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'status': 'str',
        'type': 'str',
        'used': 'int',
        'public_border_group': 'str',
        'id': 'str',
        'allow_share_bandwidth_types': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'status': 'status',
        'type': 'type',
        'used': 'used',
        'public_border_group': 'public_border_group',
        'id': 'id',
        'allow_share_bandwidth_types': 'allow_share_bandwidth_types'
    }

    def __init__(self, name=None, status=None, type=None, used=None, public_border_group=None, id=None, allow_share_bandwidth_types=None):
        """CommonPoolDict

        The model defined in huaweicloud sdk

        :param name: 公共池名字
        :type name: str
        :param status: 状态
        :type status: str
        :param type: 公共池类型，如bgp，sbgp等
        :type type: str
        :param used: 已经使用的ip数量
        :type used: int
        :param public_border_group: 功能说明：表示中心站点资源或者边缘站点资源 取值范围： center、边缘站点名称 约束：publicip只能绑定该字段相同的资源
        :type public_border_group: str
        :param id: 默认不展示，取值, 公共池ID
        :type id: str
        :param allow_share_bandwidth_types: 功能说明：表示此publicip可以加入的共享带宽类型列表，如果为空列表，则表示该           publicip不能加入任何共享带宽 约束：publicip只能加入到有该带宽类型的共享带宽中
        :type allow_share_bandwidth_types: list[str]
        """
        
        

        self._name = None
        self._status = None
        self._type = None
        self._used = None
        self._public_border_group = None
        self._id = None
        self._allow_share_bandwidth_types = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if type is not None:
            self.type = type
        if used is not None:
            self.used = used
        if public_border_group is not None:
            self.public_border_group = public_border_group
        if id is not None:
            self.id = id
        if allow_share_bandwidth_types is not None:
            self.allow_share_bandwidth_types = allow_share_bandwidth_types

    @property
    def name(self):
        """Gets the name of this CommonPoolDict.

        公共池名字

        :return: The name of this CommonPoolDict.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CommonPoolDict.

        公共池名字

        :param name: The name of this CommonPoolDict.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        """Gets the status of this CommonPoolDict.

        状态

        :return: The status of this CommonPoolDict.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CommonPoolDict.

        状态

        :param status: The status of this CommonPoolDict.
        :type status: str
        """
        self._status = status

    @property
    def type(self):
        """Gets the type of this CommonPoolDict.

        公共池类型，如bgp，sbgp等

        :return: The type of this CommonPoolDict.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CommonPoolDict.

        公共池类型，如bgp，sbgp等

        :param type: The type of this CommonPoolDict.
        :type type: str
        """
        self._type = type

    @property
    def used(self):
        """Gets the used of this CommonPoolDict.

        已经使用的ip数量

        :return: The used of this CommonPoolDict.
        :rtype: int
        """
        return self._used

    @used.setter
    def used(self, used):
        """Sets the used of this CommonPoolDict.

        已经使用的ip数量

        :param used: The used of this CommonPoolDict.
        :type used: int
        """
        self._used = used

    @property
    def public_border_group(self):
        """Gets the public_border_group of this CommonPoolDict.

        功能说明：表示中心站点资源或者边缘站点资源 取值范围： center、边缘站点名称 约束：publicip只能绑定该字段相同的资源

        :return: The public_border_group of this CommonPoolDict.
        :rtype: str
        """
        return self._public_border_group

    @public_border_group.setter
    def public_border_group(self, public_border_group):
        """Sets the public_border_group of this CommonPoolDict.

        功能说明：表示中心站点资源或者边缘站点资源 取值范围： center、边缘站点名称 约束：publicip只能绑定该字段相同的资源

        :param public_border_group: The public_border_group of this CommonPoolDict.
        :type public_border_group: str
        """
        self._public_border_group = public_border_group

    @property
    def id(self):
        """Gets the id of this CommonPoolDict.

        默认不展示，取值, 公共池ID

        :return: The id of this CommonPoolDict.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CommonPoolDict.

        默认不展示，取值, 公共池ID

        :param id: The id of this CommonPoolDict.
        :type id: str
        """
        self._id = id

    @property
    def allow_share_bandwidth_types(self):
        """Gets the allow_share_bandwidth_types of this CommonPoolDict.

        功能说明：表示此publicip可以加入的共享带宽类型列表，如果为空列表，则表示该           publicip不能加入任何共享带宽 约束：publicip只能加入到有该带宽类型的共享带宽中

        :return: The allow_share_bandwidth_types of this CommonPoolDict.
        :rtype: list[str]
        """
        return self._allow_share_bandwidth_types

    @allow_share_bandwidth_types.setter
    def allow_share_bandwidth_types(self, allow_share_bandwidth_types):
        """Sets the allow_share_bandwidth_types of this CommonPoolDict.

        功能说明：表示此publicip可以加入的共享带宽类型列表，如果为空列表，则表示该           publicip不能加入任何共享带宽 约束：publicip只能加入到有该带宽类型的共享带宽中

        :param allow_share_bandwidth_types: The allow_share_bandwidth_types of this CommonPoolDict.
        :type allow_share_bandwidth_types: list[str]
        """
        self._allow_share_bandwidth_types = allow_share_bandwidth_types

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
        if not isinstance(other, CommonPoolDict):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
