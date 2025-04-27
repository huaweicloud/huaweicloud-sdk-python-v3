# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowPtrResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'publicip': 'PublicIpRes',
        'ptrdnames': 'list[str]',
        'id': 'str',
        'description': 'str',
        'ttl': 'int',
        'status': 'str',
        'links': 'PageLink',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'publicip': 'publicip',
        'ptrdnames': 'ptrdnames',
        'id': 'id',
        'description': 'description',
        'ttl': 'ttl',
        'status': 'status',
        'links': 'links',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, publicip=None, ptrdnames=None, id=None, description=None, ttl=None, status=None, links=None, enterprise_project_id=None):
        r"""ShowPtrResponse

        The model defined in huaweicloud sdk

        :param publicip: 
        :type publicip: :class:`huaweicloudsdkdns.v2.PublicIpRes`
        :param ptrdnames: 反向解析记录对应的域名列表,最大个数不超过10个。
        :type ptrdnames: list[str]
        :param id: 反向解析记录的ID。
        :type id: str
        :param description: 对反向解析记录的描述。
        :type description: str
        :param ttl: 反向解析记录在本地DNS服务器的缓存时间，缓存时间越长更新生效越慢，以秒为单位。
        :type ttl: int
        :param status: 资源状态。
        :type status: str
        :param links: 
        :type links: :class:`huaweicloudsdkdns.v2.PageLink`
        :param enterprise_project_id: 反向解析关联的企业项目ID，长度不超过36个字符。
        :type enterprise_project_id: str
        """
        
        super(ShowPtrResponse, self).__init__()

        self._publicip = None
        self._ptrdnames = None
        self._id = None
        self._description = None
        self._ttl = None
        self._status = None
        self._links = None
        self._enterprise_project_id = None
        self.discriminator = None

        if publicip is not None:
            self.publicip = publicip
        if ptrdnames is not None:
            self.ptrdnames = ptrdnames
        if id is not None:
            self.id = id
        if description is not None:
            self.description = description
        if ttl is not None:
            self.ttl = ttl
        if status is not None:
            self.status = status
        if links is not None:
            self.links = links
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def publicip(self):
        r"""Gets the publicip of this ShowPtrResponse.

        :return: The publicip of this ShowPtrResponse.
        :rtype: :class:`huaweicloudsdkdns.v2.PublicIpRes`
        """
        return self._publicip

    @publicip.setter
    def publicip(self, publicip):
        r"""Sets the publicip of this ShowPtrResponse.

        :param publicip: The publicip of this ShowPtrResponse.
        :type publicip: :class:`huaweicloudsdkdns.v2.PublicIpRes`
        """
        self._publicip = publicip

    @property
    def ptrdnames(self):
        r"""Gets the ptrdnames of this ShowPtrResponse.

        反向解析记录对应的域名列表,最大个数不超过10个。

        :return: The ptrdnames of this ShowPtrResponse.
        :rtype: list[str]
        """
        return self._ptrdnames

    @ptrdnames.setter
    def ptrdnames(self, ptrdnames):
        r"""Sets the ptrdnames of this ShowPtrResponse.

        反向解析记录对应的域名列表,最大个数不超过10个。

        :param ptrdnames: The ptrdnames of this ShowPtrResponse.
        :type ptrdnames: list[str]
        """
        self._ptrdnames = ptrdnames

    @property
    def id(self):
        r"""Gets the id of this ShowPtrResponse.

        反向解析记录的ID。

        :return: The id of this ShowPtrResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowPtrResponse.

        反向解析记录的ID。

        :param id: The id of this ShowPtrResponse.
        :type id: str
        """
        self._id = id

    @property
    def description(self):
        r"""Gets the description of this ShowPtrResponse.

        对反向解析记录的描述。

        :return: The description of this ShowPtrResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ShowPtrResponse.

        对反向解析记录的描述。

        :param description: The description of this ShowPtrResponse.
        :type description: str
        """
        self._description = description

    @property
    def ttl(self):
        r"""Gets the ttl of this ShowPtrResponse.

        反向解析记录在本地DNS服务器的缓存时间，缓存时间越长更新生效越慢，以秒为单位。

        :return: The ttl of this ShowPtrResponse.
        :rtype: int
        """
        return self._ttl

    @ttl.setter
    def ttl(self, ttl):
        r"""Sets the ttl of this ShowPtrResponse.

        反向解析记录在本地DNS服务器的缓存时间，缓存时间越长更新生效越慢，以秒为单位。

        :param ttl: The ttl of this ShowPtrResponse.
        :type ttl: int
        """
        self._ttl = ttl

    @property
    def status(self):
        r"""Gets the status of this ShowPtrResponse.

        资源状态。

        :return: The status of this ShowPtrResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowPtrResponse.

        资源状态。

        :param status: The status of this ShowPtrResponse.
        :type status: str
        """
        self._status = status

    @property
    def links(self):
        r"""Gets the links of this ShowPtrResponse.

        :return: The links of this ShowPtrResponse.
        :rtype: :class:`huaweicloudsdkdns.v2.PageLink`
        """
        return self._links

    @links.setter
    def links(self, links):
        r"""Sets the links of this ShowPtrResponse.

        :param links: The links of this ShowPtrResponse.
        :type links: :class:`huaweicloudsdkdns.v2.PageLink`
        """
        self._links = links

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ShowPtrResponse.

        反向解析关联的企业项目ID，长度不超过36个字符。

        :return: The enterprise_project_id of this ShowPtrResponse.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ShowPtrResponse.

        反向解析关联的企业项目ID，长度不超过36个字符。

        :param enterprise_project_id: The enterprise_project_id of this ShowPtrResponse.
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
        if not isinstance(other, ShowPtrResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
