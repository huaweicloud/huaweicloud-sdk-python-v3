# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdatePtrRecordResponse(SdkResponse):

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
        'ptrdname': 'str',
        'description': 'str',
        'ttl': 'int',
        'address': 'str',
        'status': 'str',
        'action': 'str',
        'links': 'PageLink'
    }

    attribute_map = {
        'id': 'id',
        'ptrdname': 'ptrdname',
        'description': 'description',
        'ttl': 'ttl',
        'address': 'address',
        'status': 'status',
        'action': 'action',
        'links': 'links'
    }

    def __init__(self, id=None, ptrdname=None, description=None, ttl=None, address=None, status=None, action=None, links=None):
        """UpdatePtrRecordResponse

        The model defined in huaweicloud sdk

        :param id: PTR记录的ID，格式形如{region}:{floatingip_id}。
        :type id: str
        :param ptrdname: PTR记录对应的域名。
        :type ptrdname: str
        :param description: 对PTR记录的描述。
        :type description: str
        :param ttl: PTR记录在本地DNS服务器的缓存时间，缓存时间越长更新生效越慢，以秒为单位。
        :type ttl: int
        :param address: 弹性IP的IP地址。
        :type address: str
        :param status: 资源状态。
        :type status: str
        :param action: 对该资源的当前操作。  取值范围：  CREATE：表示创建 UPDATE：表示更新 DELETE：表示删除 NONE：表示无操作
        :type action: str
        :param links: 
        :type links: :class:`huaweicloudsdkdns.v2.PageLink`
        """
        
        super(UpdatePtrRecordResponse, self).__init__()

        self._id = None
        self._ptrdname = None
        self._description = None
        self._ttl = None
        self._address = None
        self._status = None
        self._action = None
        self._links = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if ptrdname is not None:
            self.ptrdname = ptrdname
        if description is not None:
            self.description = description
        if ttl is not None:
            self.ttl = ttl
        if address is not None:
            self.address = address
        if status is not None:
            self.status = status
        if action is not None:
            self.action = action
        if links is not None:
            self.links = links

    @property
    def id(self):
        """Gets the id of this UpdatePtrRecordResponse.

        PTR记录的ID，格式形如{region}:{floatingip_id}。

        :return: The id of this UpdatePtrRecordResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UpdatePtrRecordResponse.

        PTR记录的ID，格式形如{region}:{floatingip_id}。

        :param id: The id of this UpdatePtrRecordResponse.
        :type id: str
        """
        self._id = id

    @property
    def ptrdname(self):
        """Gets the ptrdname of this UpdatePtrRecordResponse.

        PTR记录对应的域名。

        :return: The ptrdname of this UpdatePtrRecordResponse.
        :rtype: str
        """
        return self._ptrdname

    @ptrdname.setter
    def ptrdname(self, ptrdname):
        """Sets the ptrdname of this UpdatePtrRecordResponse.

        PTR记录对应的域名。

        :param ptrdname: The ptrdname of this UpdatePtrRecordResponse.
        :type ptrdname: str
        """
        self._ptrdname = ptrdname

    @property
    def description(self):
        """Gets the description of this UpdatePtrRecordResponse.

        对PTR记录的描述。

        :return: The description of this UpdatePtrRecordResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdatePtrRecordResponse.

        对PTR记录的描述。

        :param description: The description of this UpdatePtrRecordResponse.
        :type description: str
        """
        self._description = description

    @property
    def ttl(self):
        """Gets the ttl of this UpdatePtrRecordResponse.

        PTR记录在本地DNS服务器的缓存时间，缓存时间越长更新生效越慢，以秒为单位。

        :return: The ttl of this UpdatePtrRecordResponse.
        :rtype: int
        """
        return self._ttl

    @ttl.setter
    def ttl(self, ttl):
        """Sets the ttl of this UpdatePtrRecordResponse.

        PTR记录在本地DNS服务器的缓存时间，缓存时间越长更新生效越慢，以秒为单位。

        :param ttl: The ttl of this UpdatePtrRecordResponse.
        :type ttl: int
        """
        self._ttl = ttl

    @property
    def address(self):
        """Gets the address of this UpdatePtrRecordResponse.

        弹性IP的IP地址。

        :return: The address of this UpdatePtrRecordResponse.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this UpdatePtrRecordResponse.

        弹性IP的IP地址。

        :param address: The address of this UpdatePtrRecordResponse.
        :type address: str
        """
        self._address = address

    @property
    def status(self):
        """Gets the status of this UpdatePtrRecordResponse.

        资源状态。

        :return: The status of this UpdatePtrRecordResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UpdatePtrRecordResponse.

        资源状态。

        :param status: The status of this UpdatePtrRecordResponse.
        :type status: str
        """
        self._status = status

    @property
    def action(self):
        """Gets the action of this UpdatePtrRecordResponse.

        对该资源的当前操作。  取值范围：  CREATE：表示创建 UPDATE：表示更新 DELETE：表示删除 NONE：表示无操作

        :return: The action of this UpdatePtrRecordResponse.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this UpdatePtrRecordResponse.

        对该资源的当前操作。  取值范围：  CREATE：表示创建 UPDATE：表示更新 DELETE：表示删除 NONE：表示无操作

        :param action: The action of this UpdatePtrRecordResponse.
        :type action: str
        """
        self._action = action

    @property
    def links(self):
        """Gets the links of this UpdatePtrRecordResponse.

        :return: The links of this UpdatePtrRecordResponse.
        :rtype: :class:`huaweicloudsdkdns.v2.PageLink`
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this UpdatePtrRecordResponse.

        :param links: The links of this UpdatePtrRecordResponse.
        :type links: :class:`huaweicloudsdkdns.v2.PageLink`
        """
        self._links = links

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
        if not isinstance(other, UpdatePtrRecordResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
