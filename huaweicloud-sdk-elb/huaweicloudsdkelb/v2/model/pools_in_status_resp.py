# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PoolsInStatusResp:

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
        'members': 'list[MembersInStatusResp]',
        'operating_status': 'str',
        'provisioning_status': 'str',
        'healthmonitor': 'HealthmonitorsInStatusResp'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'members': 'members',
        'operating_status': 'operating_status',
        'provisioning_status': 'provisioning_status',
        'healthmonitor': 'healthmonitor'
    }

    def __init__(self, id=None, name=None, members=None, operating_status=None, provisioning_status=None, healthmonitor=None):
        r"""PoolsInStatusResp

        The model defined in huaweicloud sdk

        :param id: 后端云服务器组ID
        :type id: str
        :param name: 后端云服务器组名称
        :type name: str
        :param members: 后端云服务器组关联的后端云服务器列表
        :type members: list[:class:`huaweicloudsdkelb.v2.MembersInStatusResp`]
        :param operating_status: 后端云服务器组的操作状态；该字段为预留字段，暂未启用。默认为ONLINE。
        :type operating_status: str
        :param provisioning_status: 后端云服务器组的配置状态；该字段为预留字段，暂未启用。默认为ACTIVE。
        :type provisioning_status: str
        :param healthmonitor: 
        :type healthmonitor: :class:`huaweicloudsdkelb.v2.HealthmonitorsInStatusResp`
        """
        
        

        self._id = None
        self._name = None
        self._members = None
        self._operating_status = None
        self._provisioning_status = None
        self._healthmonitor = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.members = members
        self.operating_status = operating_status
        self.provisioning_status = provisioning_status
        self.healthmonitor = healthmonitor

    @property
    def id(self):
        r"""Gets the id of this PoolsInStatusResp.

        后端云服务器组ID

        :return: The id of this PoolsInStatusResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this PoolsInStatusResp.

        后端云服务器组ID

        :param id: The id of this PoolsInStatusResp.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this PoolsInStatusResp.

        后端云服务器组名称

        :return: The name of this PoolsInStatusResp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this PoolsInStatusResp.

        后端云服务器组名称

        :param name: The name of this PoolsInStatusResp.
        :type name: str
        """
        self._name = name

    @property
    def members(self):
        r"""Gets the members of this PoolsInStatusResp.

        后端云服务器组关联的后端云服务器列表

        :return: The members of this PoolsInStatusResp.
        :rtype: list[:class:`huaweicloudsdkelb.v2.MembersInStatusResp`]
        """
        return self._members

    @members.setter
    def members(self, members):
        r"""Sets the members of this PoolsInStatusResp.

        后端云服务器组关联的后端云服务器列表

        :param members: The members of this PoolsInStatusResp.
        :type members: list[:class:`huaweicloudsdkelb.v2.MembersInStatusResp`]
        """
        self._members = members

    @property
    def operating_status(self):
        r"""Gets the operating_status of this PoolsInStatusResp.

        后端云服务器组的操作状态；该字段为预留字段，暂未启用。默认为ONLINE。

        :return: The operating_status of this PoolsInStatusResp.
        :rtype: str
        """
        return self._operating_status

    @operating_status.setter
    def operating_status(self, operating_status):
        r"""Sets the operating_status of this PoolsInStatusResp.

        后端云服务器组的操作状态；该字段为预留字段，暂未启用。默认为ONLINE。

        :param operating_status: The operating_status of this PoolsInStatusResp.
        :type operating_status: str
        """
        self._operating_status = operating_status

    @property
    def provisioning_status(self):
        r"""Gets the provisioning_status of this PoolsInStatusResp.

        后端云服务器组的配置状态；该字段为预留字段，暂未启用。默认为ACTIVE。

        :return: The provisioning_status of this PoolsInStatusResp.
        :rtype: str
        """
        return self._provisioning_status

    @provisioning_status.setter
    def provisioning_status(self, provisioning_status):
        r"""Sets the provisioning_status of this PoolsInStatusResp.

        后端云服务器组的配置状态；该字段为预留字段，暂未启用。默认为ACTIVE。

        :param provisioning_status: The provisioning_status of this PoolsInStatusResp.
        :type provisioning_status: str
        """
        self._provisioning_status = provisioning_status

    @property
    def healthmonitor(self):
        r"""Gets the healthmonitor of this PoolsInStatusResp.

        :return: The healthmonitor of this PoolsInStatusResp.
        :rtype: :class:`huaweicloudsdkelb.v2.HealthmonitorsInStatusResp`
        """
        return self._healthmonitor

    @healthmonitor.setter
    def healthmonitor(self, healthmonitor):
        r"""Sets the healthmonitor of this PoolsInStatusResp.

        :param healthmonitor: The healthmonitor of this PoolsInStatusResp.
        :type healthmonitor: :class:`huaweicloudsdkelb.v2.HealthmonitorsInStatusResp`
        """
        self._healthmonitor = healthmonitor

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
        if not isinstance(other, PoolsInStatusResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
