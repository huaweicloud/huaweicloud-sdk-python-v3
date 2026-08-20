# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateThirdPartyAssociateDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tenant_id': 'str',
        'title': 'str',
        'type': 'str',
        'modified_date': 'str',
        'created_by': 'str',
        'url': 'str',
        'domain_id': 'str',
        'workitem_id': 'str',
        'modified_by': 'str',
        'operation_id': 'str',
        'id': 'str',
        'created_date': 'str',
        'state': 'str',
        'category': 'str',
        'region': 'str'
    }

    attribute_map = {
        'tenant_id': 'tenant_id',
        'title': 'title',
        'type': 'type',
        'modified_date': 'modified_date',
        'created_by': 'created_by',
        'url': 'url',
        'domain_id': 'domain_id',
        'workitem_id': 'workitem_id',
        'modified_by': 'modified_by',
        'operation_id': 'operation_id',
        'id': 'id',
        'created_date': 'created_date',
        'state': 'state',
        'category': 'category',
        'region': 'region'
    }

    def __init__(self, tenant_id=None, title=None, type=None, modified_date=None, created_by=None, url=None, domain_id=None, workitem_id=None, modified_by=None, operation_id=None, id=None, created_date=None, state=None, category=None, region=None):
        r"""CreateThirdPartyAssociateDTO

        The model defined in huaweicloud sdk

        :param tenant_id: 租户唯一标识ID。
        :type tenant_id: str
        :param title: 工作项下关联外部链接的名称。
        :type title: str
        :param type: 外部链接的类别。
        :type type: str
        :param modified_date: 工作项下关联外部链接的修改时间。
        :type modified_date: str
        :param created_by: 工作项下关联外部链接的创建人。
        :type created_by: str
        :param url: 工作项下关联外部链接的地址。
        :type url: str
        :param domain_id: 租户下项目唯一标识ID。
        :type domain_id: str
        :param workitem_id: 工作项实例对应的唯一标识ID。
        :type workitem_id: str
        :param modified_by: 工作项下关联外部链接的修改人。
        :type modified_by: str
        :param operation_id: 外部链接操作项ID。
        :type operation_id: str
        :param id: 新关联外部链接时会创建一条数据，该数据的唯一标识ID，可以在查询外部链接接口以及关联外部链接接口响应体中找到。
        :type id: str
        :param created_date: 工作项下关联外部链接的创建时间。
        :type created_date: str
        :param state: 外部链接的生命周期。
        :type state: str
        :param category: 外部链接的类型。
        :type category: str
        :param region: 区域 。
        :type region: str
        """
        
        

        self._tenant_id = None
        self._title = None
        self._type = None
        self._modified_date = None
        self._created_by = None
        self._url = None
        self._domain_id = None
        self._workitem_id = None
        self._modified_by = None
        self._operation_id = None
        self._id = None
        self._created_date = None
        self._state = None
        self._category = None
        self._region = None
        self.discriminator = None

        if tenant_id is not None:
            self.tenant_id = tenant_id
        if title is not None:
            self.title = title
        if type is not None:
            self.type = type
        if modified_date is not None:
            self.modified_date = modified_date
        if created_by is not None:
            self.created_by = created_by
        if url is not None:
            self.url = url
        if domain_id is not None:
            self.domain_id = domain_id
        if workitem_id is not None:
            self.workitem_id = workitem_id
        if modified_by is not None:
            self.modified_by = modified_by
        if operation_id is not None:
            self.operation_id = operation_id
        if id is not None:
            self.id = id
        if created_date is not None:
            self.created_date = created_date
        if state is not None:
            self.state = state
        if category is not None:
            self.category = category
        if region is not None:
            self.region = region

    @property
    def tenant_id(self):
        r"""Gets the tenant_id of this CreateThirdPartyAssociateDTO.

        租户唯一标识ID。

        :return: The tenant_id of this CreateThirdPartyAssociateDTO.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        r"""Sets the tenant_id of this CreateThirdPartyAssociateDTO.

        租户唯一标识ID。

        :param tenant_id: The tenant_id of this CreateThirdPartyAssociateDTO.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def title(self):
        r"""Gets the title of this CreateThirdPartyAssociateDTO.

        工作项下关联外部链接的名称。

        :return: The title of this CreateThirdPartyAssociateDTO.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this CreateThirdPartyAssociateDTO.

        工作项下关联外部链接的名称。

        :param title: The title of this CreateThirdPartyAssociateDTO.
        :type title: str
        """
        self._title = title

    @property
    def type(self):
        r"""Gets the type of this CreateThirdPartyAssociateDTO.

        外部链接的类别。

        :return: The type of this CreateThirdPartyAssociateDTO.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CreateThirdPartyAssociateDTO.

        外部链接的类别。

        :param type: The type of this CreateThirdPartyAssociateDTO.
        :type type: str
        """
        self._type = type

    @property
    def modified_date(self):
        r"""Gets the modified_date of this CreateThirdPartyAssociateDTO.

        工作项下关联外部链接的修改时间。

        :return: The modified_date of this CreateThirdPartyAssociateDTO.
        :rtype: str
        """
        return self._modified_date

    @modified_date.setter
    def modified_date(self, modified_date):
        r"""Sets the modified_date of this CreateThirdPartyAssociateDTO.

        工作项下关联外部链接的修改时间。

        :param modified_date: The modified_date of this CreateThirdPartyAssociateDTO.
        :type modified_date: str
        """
        self._modified_date = modified_date

    @property
    def created_by(self):
        r"""Gets the created_by of this CreateThirdPartyAssociateDTO.

        工作项下关联外部链接的创建人。

        :return: The created_by of this CreateThirdPartyAssociateDTO.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        r"""Sets the created_by of this CreateThirdPartyAssociateDTO.

        工作项下关联外部链接的创建人。

        :param created_by: The created_by of this CreateThirdPartyAssociateDTO.
        :type created_by: str
        """
        self._created_by = created_by

    @property
    def url(self):
        r"""Gets the url of this CreateThirdPartyAssociateDTO.

        工作项下关联外部链接的地址。

        :return: The url of this CreateThirdPartyAssociateDTO.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this CreateThirdPartyAssociateDTO.

        工作项下关联外部链接的地址。

        :param url: The url of this CreateThirdPartyAssociateDTO.
        :type url: str
        """
        self._url = url

    @property
    def domain_id(self):
        r"""Gets the domain_id of this CreateThirdPartyAssociateDTO.

        租户下项目唯一标识ID。

        :return: The domain_id of this CreateThirdPartyAssociateDTO.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this CreateThirdPartyAssociateDTO.

        租户下项目唯一标识ID。

        :param domain_id: The domain_id of this CreateThirdPartyAssociateDTO.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def workitem_id(self):
        r"""Gets the workitem_id of this CreateThirdPartyAssociateDTO.

        工作项实例对应的唯一标识ID。

        :return: The workitem_id of this CreateThirdPartyAssociateDTO.
        :rtype: str
        """
        return self._workitem_id

    @workitem_id.setter
    def workitem_id(self, workitem_id):
        r"""Sets the workitem_id of this CreateThirdPartyAssociateDTO.

        工作项实例对应的唯一标识ID。

        :param workitem_id: The workitem_id of this CreateThirdPartyAssociateDTO.
        :type workitem_id: str
        """
        self._workitem_id = workitem_id

    @property
    def modified_by(self):
        r"""Gets the modified_by of this CreateThirdPartyAssociateDTO.

        工作项下关联外部链接的修改人。

        :return: The modified_by of this CreateThirdPartyAssociateDTO.
        :rtype: str
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        r"""Sets the modified_by of this CreateThirdPartyAssociateDTO.

        工作项下关联外部链接的修改人。

        :param modified_by: The modified_by of this CreateThirdPartyAssociateDTO.
        :type modified_by: str
        """
        self._modified_by = modified_by

    @property
    def operation_id(self):
        r"""Gets the operation_id of this CreateThirdPartyAssociateDTO.

        外部链接操作项ID。

        :return: The operation_id of this CreateThirdPartyAssociateDTO.
        :rtype: str
        """
        return self._operation_id

    @operation_id.setter
    def operation_id(self, operation_id):
        r"""Sets the operation_id of this CreateThirdPartyAssociateDTO.

        外部链接操作项ID。

        :param operation_id: The operation_id of this CreateThirdPartyAssociateDTO.
        :type operation_id: str
        """
        self._operation_id = operation_id

    @property
    def id(self):
        r"""Gets the id of this CreateThirdPartyAssociateDTO.

        新关联外部链接时会创建一条数据，该数据的唯一标识ID，可以在查询外部链接接口以及关联外部链接接口响应体中找到。

        :return: The id of this CreateThirdPartyAssociateDTO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CreateThirdPartyAssociateDTO.

        新关联外部链接时会创建一条数据，该数据的唯一标识ID，可以在查询外部链接接口以及关联外部链接接口响应体中找到。

        :param id: The id of this CreateThirdPartyAssociateDTO.
        :type id: str
        """
        self._id = id

    @property
    def created_date(self):
        r"""Gets the created_date of this CreateThirdPartyAssociateDTO.

        工作项下关联外部链接的创建时间。

        :return: The created_date of this CreateThirdPartyAssociateDTO.
        :rtype: str
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        r"""Sets the created_date of this CreateThirdPartyAssociateDTO.

        工作项下关联外部链接的创建时间。

        :param created_date: The created_date of this CreateThirdPartyAssociateDTO.
        :type created_date: str
        """
        self._created_date = created_date

    @property
    def state(self):
        r"""Gets the state of this CreateThirdPartyAssociateDTO.

        外部链接的生命周期。

        :return: The state of this CreateThirdPartyAssociateDTO.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this CreateThirdPartyAssociateDTO.

        外部链接的生命周期。

        :param state: The state of this CreateThirdPartyAssociateDTO.
        :type state: str
        """
        self._state = state

    @property
    def category(self):
        r"""Gets the category of this CreateThirdPartyAssociateDTO.

        外部链接的类型。

        :return: The category of this CreateThirdPartyAssociateDTO.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this CreateThirdPartyAssociateDTO.

        外部链接的类型。

        :param category: The category of this CreateThirdPartyAssociateDTO.
        :type category: str
        """
        self._category = category

    @property
    def region(self):
        r"""Gets the region of this CreateThirdPartyAssociateDTO.

        区域 。

        :return: The region of this CreateThirdPartyAssociateDTO.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this CreateThirdPartyAssociateDTO.

        区域 。

        :param region: The region of this CreateThirdPartyAssociateDTO.
        :type region: str
        """
        self._region = region

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
        if not isinstance(other, CreateThirdPartyAssociateDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
