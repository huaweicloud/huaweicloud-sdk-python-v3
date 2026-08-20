# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowIpdProcessInstancesResponseResultOpinions:

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
        'type': 'str',
        'state': 'str',
        'status': 'str',
        'region': 'str',
        'category': 'str',
        'title': 'str',
        'rounds': 'str',
        'opinion': 'str',
        'description': 'str',
        'modified_by': 'str',
        'modified_date': 'str',
        'created_by': 'UserObject',
        'created_date': 'str',
        'tenant_id': 'str',
        'domain_id': 'str',
        'issue_category': 'str',
        'issue_id': 'str',
        'curr_owner': 'UserObject',
        'co_id': 'str',
        'user_id': 'str',
        'opinion_issue_id': 'str',
        'opinion_issue_category': 'str'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'state': 'state',
        'status': 'status',
        'region': 'region',
        'category': 'category',
        'title': 'title',
        'rounds': 'rounds',
        'opinion': 'opinion',
        'description': 'description',
        'modified_by': 'modified_by',
        'modified_date': 'modified_date',
        'created_by': 'created_by',
        'created_date': 'created_date',
        'tenant_id': 'tenant_id',
        'domain_id': 'domain_id',
        'issue_category': 'issue_category',
        'issue_id': 'issue_id',
        'curr_owner': 'curr_owner',
        'co_id': 'co_id',
        'user_id': 'user_id',
        'opinion_issue_id': 'opinion_issue_id',
        'opinion_issue_category': 'opinion_issue_category'
    }

    def __init__(self, id=None, type=None, state=None, status=None, region=None, category=None, title=None, rounds=None, opinion=None, description=None, modified_by=None, modified_date=None, created_by=None, created_date=None, tenant_id=None, domain_id=None, issue_category=None, issue_id=None, curr_owner=None, co_id=None, user_id=None, opinion_issue_id=None, opinion_issue_category=None):
        r"""ShowIpdProcessInstancesResponseResultOpinions

        The model defined in huaweicloud sdk

        :param id: opinion主键。
        :type id: str
        :param type: 类型分类。
        :type type: str
        :param state: 数据状态。
        :type state: str
        :param status: opinion状态。
        :type status: str
        :param region: 区域。
        :type region: str
        :param category: 类型。
        :type category: str
        :param title: 标题。
        :type title: str
        :param rounds: 评审轮次。
        :type rounds: str
        :param opinion: 评审意见。
        :type opinion: str
        :param description: 描述。
        :type description: str
        :param modified_by: 修改人。
        :type modified_by: str
        :param modified_date: 修改时间。
        :type modified_date: str
        :param created_by: 
        :type created_by: :class:`huaweicloudsdkprojectman.v4.UserObject`
        :param created_date: 创建时间。
        :type created_date: str
        :param tenant_id: 租户ID。
        :type tenant_id: str
        :param domain_id: 项目空间ID。
        :type domain_id: str
        :param issue_category: 对象类型。
        :type issue_category: str
        :param issue_id: 对象ID。
        :type issue_id: str
        :param curr_owner: 
        :type curr_owner: :class:`huaweicloudsdkprojectman.v4.UserObject`
        :param co_id: 变更对象ID。
        :type co_id: str
        :param user_id: 用户ID。
        :type user_id: str
        :param opinion_issue_id: 评审工作项ID。
        :type opinion_issue_id: str
        :param opinion_issue_category: 评审工作项类型。
        :type opinion_issue_category: str
        """
        
        

        self._id = None
        self._type = None
        self._state = None
        self._status = None
        self._region = None
        self._category = None
        self._title = None
        self._rounds = None
        self._opinion = None
        self._description = None
        self._modified_by = None
        self._modified_date = None
        self._created_by = None
        self._created_date = None
        self._tenant_id = None
        self._domain_id = None
        self._issue_category = None
        self._issue_id = None
        self._curr_owner = None
        self._co_id = None
        self._user_id = None
        self._opinion_issue_id = None
        self._opinion_issue_category = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if state is not None:
            self.state = state
        if status is not None:
            self.status = status
        if region is not None:
            self.region = region
        if category is not None:
            self.category = category
        if title is not None:
            self.title = title
        if rounds is not None:
            self.rounds = rounds
        if opinion is not None:
            self.opinion = opinion
        if description is not None:
            self.description = description
        if modified_by is not None:
            self.modified_by = modified_by
        if modified_date is not None:
            self.modified_date = modified_date
        if created_by is not None:
            self.created_by = created_by
        if created_date is not None:
            self.created_date = created_date
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if domain_id is not None:
            self.domain_id = domain_id
        if issue_category is not None:
            self.issue_category = issue_category
        if issue_id is not None:
            self.issue_id = issue_id
        if curr_owner is not None:
            self.curr_owner = curr_owner
        if co_id is not None:
            self.co_id = co_id
        if user_id is not None:
            self.user_id = user_id
        if opinion_issue_id is not None:
            self.opinion_issue_id = opinion_issue_id
        if opinion_issue_category is not None:
            self.opinion_issue_category = opinion_issue_category

    @property
    def id(self):
        r"""Gets the id of this ShowIpdProcessInstancesResponseResultOpinions.

        opinion主键。

        :return: The id of this ShowIpdProcessInstancesResponseResultOpinions.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowIpdProcessInstancesResponseResultOpinions.

        opinion主键。

        :param id: The id of this ShowIpdProcessInstancesResponseResultOpinions.
        :type id: str
        """
        self._id = id

    @property
    def type(self):
        r"""Gets the type of this ShowIpdProcessInstancesResponseResultOpinions.

        类型分类。

        :return: The type of this ShowIpdProcessInstancesResponseResultOpinions.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ShowIpdProcessInstancesResponseResultOpinions.

        类型分类。

        :param type: The type of this ShowIpdProcessInstancesResponseResultOpinions.
        :type type: str
        """
        self._type = type

    @property
    def state(self):
        r"""Gets the state of this ShowIpdProcessInstancesResponseResultOpinions.

        数据状态。

        :return: The state of this ShowIpdProcessInstancesResponseResultOpinions.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this ShowIpdProcessInstancesResponseResultOpinions.

        数据状态。

        :param state: The state of this ShowIpdProcessInstancesResponseResultOpinions.
        :type state: str
        """
        self._state = state

    @property
    def status(self):
        r"""Gets the status of this ShowIpdProcessInstancesResponseResultOpinions.

        opinion状态。

        :return: The status of this ShowIpdProcessInstancesResponseResultOpinions.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowIpdProcessInstancesResponseResultOpinions.

        opinion状态。

        :param status: The status of this ShowIpdProcessInstancesResponseResultOpinions.
        :type status: str
        """
        self._status = status

    @property
    def region(self):
        r"""Gets the region of this ShowIpdProcessInstancesResponseResultOpinions.

        区域。

        :return: The region of this ShowIpdProcessInstancesResponseResultOpinions.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this ShowIpdProcessInstancesResponseResultOpinions.

        区域。

        :param region: The region of this ShowIpdProcessInstancesResponseResultOpinions.
        :type region: str
        """
        self._region = region

    @property
    def category(self):
        r"""Gets the category of this ShowIpdProcessInstancesResponseResultOpinions.

        类型。

        :return: The category of this ShowIpdProcessInstancesResponseResultOpinions.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this ShowIpdProcessInstancesResponseResultOpinions.

        类型。

        :param category: The category of this ShowIpdProcessInstancesResponseResultOpinions.
        :type category: str
        """
        self._category = category

    @property
    def title(self):
        r"""Gets the title of this ShowIpdProcessInstancesResponseResultOpinions.

        标题。

        :return: The title of this ShowIpdProcessInstancesResponseResultOpinions.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this ShowIpdProcessInstancesResponseResultOpinions.

        标题。

        :param title: The title of this ShowIpdProcessInstancesResponseResultOpinions.
        :type title: str
        """
        self._title = title

    @property
    def rounds(self):
        r"""Gets the rounds of this ShowIpdProcessInstancesResponseResultOpinions.

        评审轮次。

        :return: The rounds of this ShowIpdProcessInstancesResponseResultOpinions.
        :rtype: str
        """
        return self._rounds

    @rounds.setter
    def rounds(self, rounds):
        r"""Sets the rounds of this ShowIpdProcessInstancesResponseResultOpinions.

        评审轮次。

        :param rounds: The rounds of this ShowIpdProcessInstancesResponseResultOpinions.
        :type rounds: str
        """
        self._rounds = rounds

    @property
    def opinion(self):
        r"""Gets the opinion of this ShowIpdProcessInstancesResponseResultOpinions.

        评审意见。

        :return: The opinion of this ShowIpdProcessInstancesResponseResultOpinions.
        :rtype: str
        """
        return self._opinion

    @opinion.setter
    def opinion(self, opinion):
        r"""Sets the opinion of this ShowIpdProcessInstancesResponseResultOpinions.

        评审意见。

        :param opinion: The opinion of this ShowIpdProcessInstancesResponseResultOpinions.
        :type opinion: str
        """
        self._opinion = opinion

    @property
    def description(self):
        r"""Gets the description of this ShowIpdProcessInstancesResponseResultOpinions.

        描述。

        :return: The description of this ShowIpdProcessInstancesResponseResultOpinions.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ShowIpdProcessInstancesResponseResultOpinions.

        描述。

        :param description: The description of this ShowIpdProcessInstancesResponseResultOpinions.
        :type description: str
        """
        self._description = description

    @property
    def modified_by(self):
        r"""Gets the modified_by of this ShowIpdProcessInstancesResponseResultOpinions.

        修改人。

        :return: The modified_by of this ShowIpdProcessInstancesResponseResultOpinions.
        :rtype: str
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        r"""Sets the modified_by of this ShowIpdProcessInstancesResponseResultOpinions.

        修改人。

        :param modified_by: The modified_by of this ShowIpdProcessInstancesResponseResultOpinions.
        :type modified_by: str
        """
        self._modified_by = modified_by

    @property
    def modified_date(self):
        r"""Gets the modified_date of this ShowIpdProcessInstancesResponseResultOpinions.

        修改时间。

        :return: The modified_date of this ShowIpdProcessInstancesResponseResultOpinions.
        :rtype: str
        """
        return self._modified_date

    @modified_date.setter
    def modified_date(self, modified_date):
        r"""Sets the modified_date of this ShowIpdProcessInstancesResponseResultOpinions.

        修改时间。

        :param modified_date: The modified_date of this ShowIpdProcessInstancesResponseResultOpinions.
        :type modified_date: str
        """
        self._modified_date = modified_date

    @property
    def created_by(self):
        r"""Gets the created_by of this ShowIpdProcessInstancesResponseResultOpinions.

        :return: The created_by of this ShowIpdProcessInstancesResponseResultOpinions.
        :rtype: :class:`huaweicloudsdkprojectman.v4.UserObject`
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        r"""Sets the created_by of this ShowIpdProcessInstancesResponseResultOpinions.

        :param created_by: The created_by of this ShowIpdProcessInstancesResponseResultOpinions.
        :type created_by: :class:`huaweicloudsdkprojectman.v4.UserObject`
        """
        self._created_by = created_by

    @property
    def created_date(self):
        r"""Gets the created_date of this ShowIpdProcessInstancesResponseResultOpinions.

        创建时间。

        :return: The created_date of this ShowIpdProcessInstancesResponseResultOpinions.
        :rtype: str
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        r"""Sets the created_date of this ShowIpdProcessInstancesResponseResultOpinions.

        创建时间。

        :param created_date: The created_date of this ShowIpdProcessInstancesResponseResultOpinions.
        :type created_date: str
        """
        self._created_date = created_date

    @property
    def tenant_id(self):
        r"""Gets the tenant_id of this ShowIpdProcessInstancesResponseResultOpinions.

        租户ID。

        :return: The tenant_id of this ShowIpdProcessInstancesResponseResultOpinions.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        r"""Sets the tenant_id of this ShowIpdProcessInstancesResponseResultOpinions.

        租户ID。

        :param tenant_id: The tenant_id of this ShowIpdProcessInstancesResponseResultOpinions.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def domain_id(self):
        r"""Gets the domain_id of this ShowIpdProcessInstancesResponseResultOpinions.

        项目空间ID。

        :return: The domain_id of this ShowIpdProcessInstancesResponseResultOpinions.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this ShowIpdProcessInstancesResponseResultOpinions.

        项目空间ID。

        :param domain_id: The domain_id of this ShowIpdProcessInstancesResponseResultOpinions.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def issue_category(self):
        r"""Gets the issue_category of this ShowIpdProcessInstancesResponseResultOpinions.

        对象类型。

        :return: The issue_category of this ShowIpdProcessInstancesResponseResultOpinions.
        :rtype: str
        """
        return self._issue_category

    @issue_category.setter
    def issue_category(self, issue_category):
        r"""Sets the issue_category of this ShowIpdProcessInstancesResponseResultOpinions.

        对象类型。

        :param issue_category: The issue_category of this ShowIpdProcessInstancesResponseResultOpinions.
        :type issue_category: str
        """
        self._issue_category = issue_category

    @property
    def issue_id(self):
        r"""Gets the issue_id of this ShowIpdProcessInstancesResponseResultOpinions.

        对象ID。

        :return: The issue_id of this ShowIpdProcessInstancesResponseResultOpinions.
        :rtype: str
        """
        return self._issue_id

    @issue_id.setter
    def issue_id(self, issue_id):
        r"""Sets the issue_id of this ShowIpdProcessInstancesResponseResultOpinions.

        对象ID。

        :param issue_id: The issue_id of this ShowIpdProcessInstancesResponseResultOpinions.
        :type issue_id: str
        """
        self._issue_id = issue_id

    @property
    def curr_owner(self):
        r"""Gets the curr_owner of this ShowIpdProcessInstancesResponseResultOpinions.

        :return: The curr_owner of this ShowIpdProcessInstancesResponseResultOpinions.
        :rtype: :class:`huaweicloudsdkprojectman.v4.UserObject`
        """
        return self._curr_owner

    @curr_owner.setter
    def curr_owner(self, curr_owner):
        r"""Sets the curr_owner of this ShowIpdProcessInstancesResponseResultOpinions.

        :param curr_owner: The curr_owner of this ShowIpdProcessInstancesResponseResultOpinions.
        :type curr_owner: :class:`huaweicloudsdkprojectman.v4.UserObject`
        """
        self._curr_owner = curr_owner

    @property
    def co_id(self):
        r"""Gets the co_id of this ShowIpdProcessInstancesResponseResultOpinions.

        变更对象ID。

        :return: The co_id of this ShowIpdProcessInstancesResponseResultOpinions.
        :rtype: str
        """
        return self._co_id

    @co_id.setter
    def co_id(self, co_id):
        r"""Sets the co_id of this ShowIpdProcessInstancesResponseResultOpinions.

        变更对象ID。

        :param co_id: The co_id of this ShowIpdProcessInstancesResponseResultOpinions.
        :type co_id: str
        """
        self._co_id = co_id

    @property
    def user_id(self):
        r"""Gets the user_id of this ShowIpdProcessInstancesResponseResultOpinions.

        用户ID。

        :return: The user_id of this ShowIpdProcessInstancesResponseResultOpinions.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this ShowIpdProcessInstancesResponseResultOpinions.

        用户ID。

        :param user_id: The user_id of this ShowIpdProcessInstancesResponseResultOpinions.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def opinion_issue_id(self):
        r"""Gets the opinion_issue_id of this ShowIpdProcessInstancesResponseResultOpinions.

        评审工作项ID。

        :return: The opinion_issue_id of this ShowIpdProcessInstancesResponseResultOpinions.
        :rtype: str
        """
        return self._opinion_issue_id

    @opinion_issue_id.setter
    def opinion_issue_id(self, opinion_issue_id):
        r"""Sets the opinion_issue_id of this ShowIpdProcessInstancesResponseResultOpinions.

        评审工作项ID。

        :param opinion_issue_id: The opinion_issue_id of this ShowIpdProcessInstancesResponseResultOpinions.
        :type opinion_issue_id: str
        """
        self._opinion_issue_id = opinion_issue_id

    @property
    def opinion_issue_category(self):
        r"""Gets the opinion_issue_category of this ShowIpdProcessInstancesResponseResultOpinions.

        评审工作项类型。

        :return: The opinion_issue_category of this ShowIpdProcessInstancesResponseResultOpinions.
        :rtype: str
        """
        return self._opinion_issue_category

    @opinion_issue_category.setter
    def opinion_issue_category(self, opinion_issue_category):
        r"""Sets the opinion_issue_category of this ShowIpdProcessInstancesResponseResultOpinions.

        评审工作项类型。

        :param opinion_issue_category: The opinion_issue_category of this ShowIpdProcessInstancesResponseResultOpinions.
        :type opinion_issue_category: str
        """
        self._opinion_issue_category = opinion_issue_category

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
        if not isinstance(other, ShowIpdProcessInstancesResponseResultOpinions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
