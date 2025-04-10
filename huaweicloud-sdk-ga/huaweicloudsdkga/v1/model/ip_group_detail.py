# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IpGroupDetail:

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
        'description': 'str',
        'status': 'ConfigStatus',
        'ip_list': 'list[IpInfo]',
        'associated_listeners': 'list[ListenerAccessControlPolicy]',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'status': 'status',
        'ip_list': 'ip_list',
        'associated_listeners': 'associated_listeners',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, name=None, description=None, status=None, ip_list=None, associated_listeners=None, created_at=None, updated_at=None):
        r"""IpGroupDetail

        The model defined in huaweicloud sdk

        :param id: IP地址组ID。
        :type id: str
        :param name: IP地址组名称。
        :type name: str
        :param description: IP地址组描述。
        :type description: str
        :param status: 
        :type status: :class:`huaweicloudsdkga.v1.ConfigStatus`
        :param ip_list: IP地址组中的IP网段列表。
        :type ip_list: list[:class:`huaweicloudsdkga.v1.IpInfo`]
        :param associated_listeners: 
        :type associated_listeners: list[:class:`huaweicloudsdkga.v1.ListenerAccessControlPolicy`]
        :param created_at: 创建时间。
        :type created_at: datetime
        :param updated_at: 更新时间。
        :type updated_at: datetime
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._status = None
        self._ip_list = None
        self._associated_listeners = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if status is not None:
            self.status = status
        if ip_list is not None:
            self.ip_list = ip_list
        if associated_listeners is not None:
            self.associated_listeners = associated_listeners
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def id(self):
        r"""Gets the id of this IpGroupDetail.

        IP地址组ID。

        :return: The id of this IpGroupDetail.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this IpGroupDetail.

        IP地址组ID。

        :param id: The id of this IpGroupDetail.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this IpGroupDetail.

        IP地址组名称。

        :return: The name of this IpGroupDetail.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this IpGroupDetail.

        IP地址组名称。

        :param name: The name of this IpGroupDetail.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this IpGroupDetail.

        IP地址组描述。

        :return: The description of this IpGroupDetail.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this IpGroupDetail.

        IP地址组描述。

        :param description: The description of this IpGroupDetail.
        :type description: str
        """
        self._description = description

    @property
    def status(self):
        r"""Gets the status of this IpGroupDetail.

        :return: The status of this IpGroupDetail.
        :rtype: :class:`huaweicloudsdkga.v1.ConfigStatus`
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this IpGroupDetail.

        :param status: The status of this IpGroupDetail.
        :type status: :class:`huaweicloudsdkga.v1.ConfigStatus`
        """
        self._status = status

    @property
    def ip_list(self):
        r"""Gets the ip_list of this IpGroupDetail.

        IP地址组中的IP网段列表。

        :return: The ip_list of this IpGroupDetail.
        :rtype: list[:class:`huaweicloudsdkga.v1.IpInfo`]
        """
        return self._ip_list

    @ip_list.setter
    def ip_list(self, ip_list):
        r"""Sets the ip_list of this IpGroupDetail.

        IP地址组中的IP网段列表。

        :param ip_list: The ip_list of this IpGroupDetail.
        :type ip_list: list[:class:`huaweicloudsdkga.v1.IpInfo`]
        """
        self._ip_list = ip_list

    @property
    def associated_listeners(self):
        r"""Gets the associated_listeners of this IpGroupDetail.

        :return: The associated_listeners of this IpGroupDetail.
        :rtype: list[:class:`huaweicloudsdkga.v1.ListenerAccessControlPolicy`]
        """
        return self._associated_listeners

    @associated_listeners.setter
    def associated_listeners(self, associated_listeners):
        r"""Sets the associated_listeners of this IpGroupDetail.

        :param associated_listeners: The associated_listeners of this IpGroupDetail.
        :type associated_listeners: list[:class:`huaweicloudsdkga.v1.ListenerAccessControlPolicy`]
        """
        self._associated_listeners = associated_listeners

    @property
    def created_at(self):
        r"""Gets the created_at of this IpGroupDetail.

        创建时间。

        :return: The created_at of this IpGroupDetail.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this IpGroupDetail.

        创建时间。

        :param created_at: The created_at of this IpGroupDetail.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this IpGroupDetail.

        更新时间。

        :return: The updated_at of this IpGroupDetail.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this IpGroupDetail.

        更新时间。

        :param updated_at: The updated_at of this IpGroupDetail.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

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
        if not isinstance(other, IpGroupDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
