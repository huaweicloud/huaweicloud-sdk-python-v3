# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreatePtrRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'publicip': 'PublicIpReq',
        'ptrdnames': 'list[str]',
        'description': 'str',
        'ttl': 'int',
        'tags': 'list[Tag]',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'publicip': 'publicip',
        'ptrdnames': 'ptrdnames',
        'description': 'description',
        'ttl': 'ttl',
        'tags': 'tags',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, publicip=None, ptrdnames=None, description=None, ttl=None, tags=None, enterprise_project_id=None):
        r"""CreatePtrRequestBody

        The model defined in huaweicloud sdk

        :param publicip: 
        :type publicip: :class:`huaweicloudsdkdns.v2.PublicIpReq`
        :param ptrdnames: 反向解析记录对应的域名列表，最大个数不超过10个。
        :type ptrdnames: list[str]
        :param description: 对反向解析记录的描述。
        :type description: str
        :param ttl: 反向解析记录在本地DNS服务器的缓存时间，缓存时间越长更新生效越慢，以秒为单位。取值范围：1～2147483647
        :type ttl: int
        :param tags: 资源标签。
        :type tags: list[:class:`huaweicloudsdkdns.v2.Tag`]
        :param enterprise_project_id: 反向解析关联的企业项目ID，长度不超过36个字符。默认值为0。
        :type enterprise_project_id: str
        """
        
        

        self._publicip = None
        self._ptrdnames = None
        self._description = None
        self._ttl = None
        self._tags = None
        self._enterprise_project_id = None
        self.discriminator = None

        if publicip is not None:
            self.publicip = publicip
        self.ptrdnames = ptrdnames
        if description is not None:
            self.description = description
        if ttl is not None:
            self.ttl = ttl
        if tags is not None:
            self.tags = tags
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def publicip(self):
        r"""Gets the publicip of this CreatePtrRequestBody.

        :return: The publicip of this CreatePtrRequestBody.
        :rtype: :class:`huaweicloudsdkdns.v2.PublicIpReq`
        """
        return self._publicip

    @publicip.setter
    def publicip(self, publicip):
        r"""Sets the publicip of this CreatePtrRequestBody.

        :param publicip: The publicip of this CreatePtrRequestBody.
        :type publicip: :class:`huaweicloudsdkdns.v2.PublicIpReq`
        """
        self._publicip = publicip

    @property
    def ptrdnames(self):
        r"""Gets the ptrdnames of this CreatePtrRequestBody.

        反向解析记录对应的域名列表，最大个数不超过10个。

        :return: The ptrdnames of this CreatePtrRequestBody.
        :rtype: list[str]
        """
        return self._ptrdnames

    @ptrdnames.setter
    def ptrdnames(self, ptrdnames):
        r"""Sets the ptrdnames of this CreatePtrRequestBody.

        反向解析记录对应的域名列表，最大个数不超过10个。

        :param ptrdnames: The ptrdnames of this CreatePtrRequestBody.
        :type ptrdnames: list[str]
        """
        self._ptrdnames = ptrdnames

    @property
    def description(self):
        r"""Gets the description of this CreatePtrRequestBody.

        对反向解析记录的描述。

        :return: The description of this CreatePtrRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreatePtrRequestBody.

        对反向解析记录的描述。

        :param description: The description of this CreatePtrRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def ttl(self):
        r"""Gets the ttl of this CreatePtrRequestBody.

        反向解析记录在本地DNS服务器的缓存时间，缓存时间越长更新生效越慢，以秒为单位。取值范围：1～2147483647

        :return: The ttl of this CreatePtrRequestBody.
        :rtype: int
        """
        return self._ttl

    @ttl.setter
    def ttl(self, ttl):
        r"""Sets the ttl of this CreatePtrRequestBody.

        反向解析记录在本地DNS服务器的缓存时间，缓存时间越长更新生效越慢，以秒为单位。取值范围：1～2147483647

        :param ttl: The ttl of this CreatePtrRequestBody.
        :type ttl: int
        """
        self._ttl = ttl

    @property
    def tags(self):
        r"""Gets the tags of this CreatePtrRequestBody.

        资源标签。

        :return: The tags of this CreatePtrRequestBody.
        :rtype: list[:class:`huaweicloudsdkdns.v2.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this CreatePtrRequestBody.

        资源标签。

        :param tags: The tags of this CreatePtrRequestBody.
        :type tags: list[:class:`huaweicloudsdkdns.v2.Tag`]
        """
        self._tags = tags

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this CreatePtrRequestBody.

        反向解析关联的企业项目ID，长度不超过36个字符。默认值为0。

        :return: The enterprise_project_id of this CreatePtrRequestBody.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this CreatePtrRequestBody.

        反向解析关联的企业项目ID，长度不超过36个字符。默认值为0。

        :param enterprise_project_id: The enterprise_project_id of this CreatePtrRequestBody.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, CreatePtrRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
