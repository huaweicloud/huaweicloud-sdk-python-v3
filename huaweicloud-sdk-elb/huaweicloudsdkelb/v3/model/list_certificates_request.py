# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCertificatesRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'admin_state_up': 'bool',
        'description': 'list[str]',
        'domain': 'list[str]',
        'id': 'list[str]',
        'limit': 'int',
        'marker': 'str',
        'name': 'list[str]',
        'page_reverse': 'bool',
        'type': 'list[str]'
    }

    attribute_map = {
        'admin_state_up': 'admin_state_up',
        'description': 'description',
        'domain': 'domain',
        'id': 'id',
        'limit': 'limit',
        'marker': 'marker',
        'name': 'name',
        'page_reverse': 'page_reverse',
        'type': 'type'
    }

    def __init__(self, admin_state_up=None, description=None, domain=None, id=None, limit=None, marker=None, name=None, page_reverse=None, type=None):
        """ListCertificatesRequest - a model defined in huaweicloud sdk"""
        
        

        self._admin_state_up = None
        self._description = None
        self._domain = None
        self._id = None
        self._limit = None
        self._marker = None
        self._name = None
        self._page_reverse = None
        self._type = None
        self.discriminator = None

        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        if description is not None:
            self.description = description
        if domain is not None:
            self.domain = domain
        if id is not None:
            self.id = id
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if name is not None:
            self.name = name
        if page_reverse is not None:
            self.page_reverse = page_reverse
        if type is not None:
            self.type = type

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this ListCertificatesRequest.

        SSL证书的管理状态；暂不支持。

        :return: The admin_state_up of this ListCertificatesRequest.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this ListCertificatesRequest.

        SSL证书的管理状态；暂不支持。

        :param admin_state_up: The admin_state_up of this ListCertificatesRequest.
        :type: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def description(self):
        """Gets the description of this ListCertificatesRequest.

        SSL证书的描述。

        :return: The description of this ListCertificatesRequest.
        :rtype: list[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ListCertificatesRequest.

        SSL证书的描述。

        :param description: The description of this ListCertificatesRequest.
        :type: list[str]
        """
        self._description = description

    @property
    def domain(self):
        """Gets the domain of this ListCertificatesRequest.

        服务器证书所签域名。该字段仅type为server时有效。

        :return: The domain of this ListCertificatesRequest.
        :rtype: list[str]
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this ListCertificatesRequest.

        服务器证书所签域名。该字段仅type为server时有效。

        :param domain: The domain of this ListCertificatesRequest.
        :type: list[str]
        """
        self._domain = domain

    @property
    def id(self):
        """Gets the id of this ListCertificatesRequest.

        证书ID。

        :return: The id of this ListCertificatesRequest.
        :rtype: list[str]
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListCertificatesRequest.

        证书ID。

        :param id: The id of this ListCertificatesRequest.
        :type: list[str]
        """
        self._id = id

    @property
    def limit(self):
        """Gets the limit of this ListCertificatesRequest.

        每页返回的个数。

        :return: The limit of this ListCertificatesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListCertificatesRequest.

        每页返回的个数。

        :param limit: The limit of this ListCertificatesRequest.
        :type: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListCertificatesRequest.

        上一页最后一条记录的ID。  使用说明：  - 必须与limit一起使用。 - 不指定时表示查询第一页。 - 该字段不允许为空或无效的ID。

        :return: The marker of this ListCertificatesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListCertificatesRequest.

        上一页最后一条记录的ID。  使用说明：  - 必须与limit一起使用。 - 不指定时表示查询第一页。 - 该字段不允许为空或无效的ID。

        :param marker: The marker of this ListCertificatesRequest.
        :type: str
        """
        self._marker = marker

    @property
    def name(self):
        """Gets the name of this ListCertificatesRequest.

        SSL证书的名称。

        :return: The name of this ListCertificatesRequest.
        :rtype: list[str]
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListCertificatesRequest.

        SSL证书的名称。

        :param name: The name of this ListCertificatesRequest.
        :type: list[str]
        """
        self._name = name

    @property
    def page_reverse(self):
        """Gets the page_reverse of this ListCertificatesRequest.

        分页的顺序，true表示从后往前分页，false表示从前往后分页，默认为false。使用说明：必须与limit一起使用。

        :return: The page_reverse of this ListCertificatesRequest.
        :rtype: bool
        """
        return self._page_reverse

    @page_reverse.setter
    def page_reverse(self, page_reverse):
        """Sets the page_reverse of this ListCertificatesRequest.

        分页的顺序，true表示从后往前分页，false表示从前往后分页，默认为false。使用说明：必须与limit一起使用。

        :param page_reverse: The page_reverse of this ListCertificatesRequest.
        :type: bool
        """
        self._page_reverse = page_reverse

    @property
    def type(self):
        """Gets the type of this ListCertificatesRequest.

        SSL证书的类型。分为服务器证书(server)和CA证书(client)。

        :return: The type of this ListCertificatesRequest.
        :rtype: list[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListCertificatesRequest.

        SSL证书的类型。分为服务器证书(server)和CA证书(client)。

        :param type: The type of this ListCertificatesRequest.
        :type: list[str]
        """
        self._type = type

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
        if not isinstance(other, ListCertificatesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
