# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ThirdPartyAssociatedDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain_id': 'str',
        'id': 'str',
        'created_date': 'str',
        'created_by': 'str',
        'title': 'str',
        'url': 'str'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'id': 'id',
        'created_date': 'created_date',
        'created_by': 'created_by',
        'title': 'title',
        'url': 'url'
    }

    def __init__(self, domain_id=None, id=None, created_date=None, created_by=None, title=None, url=None):
        r"""ThirdPartyAssociatedDTO

        The model defined in huaweicloud sdk

        :param domain_id: 工作项归属项目的项目空间ID。
        :type domain_id: str
        :param id: 新关联外部链接时会创建一条数据，该数据的唯一标识ID，可以在查询外部链接接口以及关联外部链接接口响应体中找到。
        :type id: str
        :param created_date: 工作项下关联外部链接的创建时间。
        :type created_date: str
        :param created_by: 工作项下关联外部链接的创建人。
        :type created_by: str
        :param title: 工作项下关联外部链接的名称。
        :type title: str
        :param url: 工作项下关联外部链接的地址。
        :type url: str
        """
        
        

        self._domain_id = None
        self._id = None
        self._created_date = None
        self._created_by = None
        self._title = None
        self._url = None
        self.discriminator = None

        if domain_id is not None:
            self.domain_id = domain_id
        if id is not None:
            self.id = id
        if created_date is not None:
            self.created_date = created_date
        if created_by is not None:
            self.created_by = created_by
        if title is not None:
            self.title = title
        if url is not None:
            self.url = url

    @property
    def domain_id(self):
        r"""Gets the domain_id of this ThirdPartyAssociatedDTO.

        工作项归属项目的项目空间ID。

        :return: The domain_id of this ThirdPartyAssociatedDTO.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this ThirdPartyAssociatedDTO.

        工作项归属项目的项目空间ID。

        :param domain_id: The domain_id of this ThirdPartyAssociatedDTO.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def id(self):
        r"""Gets the id of this ThirdPartyAssociatedDTO.

        新关联外部链接时会创建一条数据，该数据的唯一标识ID，可以在查询外部链接接口以及关联外部链接接口响应体中找到。

        :return: The id of this ThirdPartyAssociatedDTO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ThirdPartyAssociatedDTO.

        新关联外部链接时会创建一条数据，该数据的唯一标识ID，可以在查询外部链接接口以及关联外部链接接口响应体中找到。

        :param id: The id of this ThirdPartyAssociatedDTO.
        :type id: str
        """
        self._id = id

    @property
    def created_date(self):
        r"""Gets the created_date of this ThirdPartyAssociatedDTO.

        工作项下关联外部链接的创建时间。

        :return: The created_date of this ThirdPartyAssociatedDTO.
        :rtype: str
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        r"""Sets the created_date of this ThirdPartyAssociatedDTO.

        工作项下关联外部链接的创建时间。

        :param created_date: The created_date of this ThirdPartyAssociatedDTO.
        :type created_date: str
        """
        self._created_date = created_date

    @property
    def created_by(self):
        r"""Gets the created_by of this ThirdPartyAssociatedDTO.

        工作项下关联外部链接的创建人。

        :return: The created_by of this ThirdPartyAssociatedDTO.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        r"""Sets the created_by of this ThirdPartyAssociatedDTO.

        工作项下关联外部链接的创建人。

        :param created_by: The created_by of this ThirdPartyAssociatedDTO.
        :type created_by: str
        """
        self._created_by = created_by

    @property
    def title(self):
        r"""Gets the title of this ThirdPartyAssociatedDTO.

        工作项下关联外部链接的名称。

        :return: The title of this ThirdPartyAssociatedDTO.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this ThirdPartyAssociatedDTO.

        工作项下关联外部链接的名称。

        :param title: The title of this ThirdPartyAssociatedDTO.
        :type title: str
        """
        self._title = title

    @property
    def url(self):
        r"""Gets the url of this ThirdPartyAssociatedDTO.

        工作项下关联外部链接的地址。

        :return: The url of this ThirdPartyAssociatedDTO.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this ThirdPartyAssociatedDTO.

        工作项下关联外部链接的地址。

        :param url: The url of this ThirdPartyAssociatedDTO.
        :type url: str
        """
        self._url = url

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ThirdPartyAssociatedDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
