# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdatePtrReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ptrdname': 'str',
        'description': 'str',
        'ttl': 'int',
        'tags': 'list[Tag]'
    }

    attribute_map = {
        'ptrdname': 'ptrdname',
        'description': 'description',
        'ttl': 'ttl',
        'tags': 'tags'
    }

    def __init__(self, ptrdname=None, description=None, ttl=None, tags=None):
        """UpdatePtrReq

        The model defined in huaweicloud sdk

        :param ptrdname: PTR记录对应的域名。
        :type ptrdname: str
        :param description: 对PTR记录的描述。
        :type description: str
        :param ttl: PTR记录在本地DNS服务器的缓存时间，缓存时间越长更新生效越慢，以秒为单位。
        :type ttl: int
        :param tags: 资源标签。
        :type tags: list[:class:`huaweicloudsdkdns.v2.Tag`]
        """
        
        

        self._ptrdname = None
        self._description = None
        self._ttl = None
        self._tags = None
        self.discriminator = None

        self.ptrdname = ptrdname
        if description is not None:
            self.description = description
        if ttl is not None:
            self.ttl = ttl
        if tags is not None:
            self.tags = tags

    @property
    def ptrdname(self):
        """Gets the ptrdname of this UpdatePtrReq.

        PTR记录对应的域名。

        :return: The ptrdname of this UpdatePtrReq.
        :rtype: str
        """
        return self._ptrdname

    @ptrdname.setter
    def ptrdname(self, ptrdname):
        """Sets the ptrdname of this UpdatePtrReq.

        PTR记录对应的域名。

        :param ptrdname: The ptrdname of this UpdatePtrReq.
        :type ptrdname: str
        """
        self._ptrdname = ptrdname

    @property
    def description(self):
        """Gets the description of this UpdatePtrReq.

        对PTR记录的描述。

        :return: The description of this UpdatePtrReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdatePtrReq.

        对PTR记录的描述。

        :param description: The description of this UpdatePtrReq.
        :type description: str
        """
        self._description = description

    @property
    def ttl(self):
        """Gets the ttl of this UpdatePtrReq.

        PTR记录在本地DNS服务器的缓存时间，缓存时间越长更新生效越慢，以秒为单位。

        :return: The ttl of this UpdatePtrReq.
        :rtype: int
        """
        return self._ttl

    @ttl.setter
    def ttl(self, ttl):
        """Sets the ttl of this UpdatePtrReq.

        PTR记录在本地DNS服务器的缓存时间，缓存时间越长更新生效越慢，以秒为单位。

        :param ttl: The ttl of this UpdatePtrReq.
        :type ttl: int
        """
        self._ttl = ttl

    @property
    def tags(self):
        """Gets the tags of this UpdatePtrReq.

        资源标签。

        :return: The tags of this UpdatePtrReq.
        :rtype: list[:class:`huaweicloudsdkdns.v2.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this UpdatePtrReq.

        资源标签。

        :param tags: The tags of this UpdatePtrReq.
        :type tags: list[:class:`huaweicloudsdkdns.v2.Tag`]
        """
        self._tags = tags

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
        if not isinstance(other, UpdatePtrReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
