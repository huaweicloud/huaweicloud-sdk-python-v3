# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAntileakageRulesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enterprise_project_id': 'str',
        'policy_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'page': 'int',
        'pagesize': 'int'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'policy_id': 'policy_id',
        'offset': 'offset',
        'limit': 'limit',
        'page': 'page',
        'pagesize': 'pagesize'
    }

    def __init__(self, enterprise_project_id=None, policy_id=None, offset=None, limit=None, page=None, pagesize=None):
        r"""ListAntileakageRulesRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: 您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id。若需要查询当前用户所有企业项目绑定的资源信息，请传参all_granted_eps。
        :type enterprise_project_id: str
        :param policy_id: **参数解释：** 防护策略id，您可以通过调用查询防护策略列表（ListPolicy）获取策略id **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type policy_id: str
        :param offset: **参数解释：** 偏移量，表示查询该偏移量之后的记录，与参数limit一起使用 **约束限制：** 不涉及 **取值范围：** [0, 65535] **默认取值：** 不涉及
        :type offset: int
        :param limit: **参数解释：** 查询返回记录的数量限制，与参数offset一起使用，如果offset为设置值，则limit无效 **约束限制：** 不涉及 **取值范围：** [1, 65535] **默认取值：** 10
        :type limit: int
        :param page: **参数解释：** 当前页码，与参数pagesize一起使用 **约束限制：** 不涉及 **取值范围：** [1, 记录数/pagesize] **默认取值：** 1
        :type page: int
        :param pagesize: **参数解释：** 每页大小，与参数page一起使用 **约束限制：** 不涉及 **取值范围：** [0, 2147483647] **默认取值：** 1000
        :type pagesize: int
        """
        
        

        self._enterprise_project_id = None
        self._policy_id = None
        self._offset = None
        self._limit = None
        self._page = None
        self._pagesize = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.policy_id = policy_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if page is not None:
            self.page = page
        if pagesize is not None:
            self.pagesize = pagesize

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListAntileakageRulesRequest.

        您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id。若需要查询当前用户所有企业项目绑定的资源信息，请传参all_granted_eps。

        :return: The enterprise_project_id of this ListAntileakageRulesRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListAntileakageRulesRequest.

        您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id。若需要查询当前用户所有企业项目绑定的资源信息，请传参all_granted_eps。

        :param enterprise_project_id: The enterprise_project_id of this ListAntileakageRulesRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def policy_id(self):
        r"""Gets the policy_id of this ListAntileakageRulesRequest.

        **参数解释：** 防护策略id，您可以通过调用查询防护策略列表（ListPolicy）获取策略id **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The policy_id of this ListAntileakageRulesRequest.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        r"""Sets the policy_id of this ListAntileakageRulesRequest.

        **参数解释：** 防护策略id，您可以通过调用查询防护策略列表（ListPolicy）获取策略id **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param policy_id: The policy_id of this ListAntileakageRulesRequest.
        :type policy_id: str
        """
        self._policy_id = policy_id

    @property
    def offset(self):
        r"""Gets the offset of this ListAntileakageRulesRequest.

        **参数解释：** 偏移量，表示查询该偏移量之后的记录，与参数limit一起使用 **约束限制：** 不涉及 **取值范围：** [0, 65535] **默认取值：** 不涉及

        :return: The offset of this ListAntileakageRulesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListAntileakageRulesRequest.

        **参数解释：** 偏移量，表示查询该偏移量之后的记录，与参数limit一起使用 **约束限制：** 不涉及 **取值范围：** [0, 65535] **默认取值：** 不涉及

        :param offset: The offset of this ListAntileakageRulesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListAntileakageRulesRequest.

        **参数解释：** 查询返回记录的数量限制，与参数offset一起使用，如果offset为设置值，则limit无效 **约束限制：** 不涉及 **取值范围：** [1, 65535] **默认取值：** 10

        :return: The limit of this ListAntileakageRulesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListAntileakageRulesRequest.

        **参数解释：** 查询返回记录的数量限制，与参数offset一起使用，如果offset为设置值，则limit无效 **约束限制：** 不涉及 **取值范围：** [1, 65535] **默认取值：** 10

        :param limit: The limit of this ListAntileakageRulesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def page(self):
        r"""Gets the page of this ListAntileakageRulesRequest.

        **参数解释：** 当前页码，与参数pagesize一起使用 **约束限制：** 不涉及 **取值范围：** [1, 记录数/pagesize] **默认取值：** 1

        :return: The page of this ListAntileakageRulesRequest.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        r"""Sets the page of this ListAntileakageRulesRequest.

        **参数解释：** 当前页码，与参数pagesize一起使用 **约束限制：** 不涉及 **取值范围：** [1, 记录数/pagesize] **默认取值：** 1

        :param page: The page of this ListAntileakageRulesRequest.
        :type page: int
        """
        self._page = page

    @property
    def pagesize(self):
        r"""Gets the pagesize of this ListAntileakageRulesRequest.

        **参数解释：** 每页大小，与参数page一起使用 **约束限制：** 不涉及 **取值范围：** [0, 2147483647] **默认取值：** 1000

        :return: The pagesize of this ListAntileakageRulesRequest.
        :rtype: int
        """
        return self._pagesize

    @pagesize.setter
    def pagesize(self, pagesize):
        r"""Sets the pagesize of this ListAntileakageRulesRequest.

        **参数解释：** 每页大小，与参数page一起使用 **约束限制：** 不涉及 **取值范围：** [0, 2147483647] **默认取值：** 1000

        :param pagesize: The pagesize of this ListAntileakageRulesRequest.
        :type pagesize: int
        """
        self._pagesize = pagesize

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
        if not isinstance(other, ListAntileakageRulesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
