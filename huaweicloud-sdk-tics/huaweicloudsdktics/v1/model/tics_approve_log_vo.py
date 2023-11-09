# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TicsApproveLogVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'create_time': 'datetime',
        'creator_id': 'str',
        'creator_name': 'str',
        'domain_alias': 'str',
        'domain_name': 'str',
        'league': 'TicsLeagueNoticeVo',
        'league_id': 'str',
        'league_name': 'str',
        'partner_id': 'str',
        'partner_status': 'str',
        'partners': 'list[TicsLeaguePartnerVo]',
        'update_id': 'str',
        'update_name': 'str',
        'update_time': 'datetime'
    }

    attribute_map = {
        'create_time': 'create_time',
        'creator_id': 'creator_id',
        'creator_name': 'creator_name',
        'domain_alias': 'domain_alias',
        'domain_name': 'domain_name',
        'league': 'league',
        'league_id': 'league_id',
        'league_name': 'league_name',
        'partner_id': 'partner_id',
        'partner_status': 'partner_status',
        'partners': 'partners',
        'update_id': 'update_id',
        'update_name': 'update_name',
        'update_time': 'update_time'
    }

    def __init__(self, create_time=None, creator_id=None, creator_name=None, domain_alias=None, domain_name=None, league=None, league_id=None, league_name=None, partner_id=None, partner_status=None, partners=None, update_id=None, update_name=None, update_time=None):
        """TicsApproveLogVo

        The model defined in huaweicloud sdk

        :param create_time: 创建时间
        :type create_time: datetime
        :param creator_id: 创建者Id
        :type creator_id: str
        :param creator_name: 创建者名称
        :type creator_name: str
        :param domain_alias: 租户别名
        :type domain_alias: str
        :param domain_name: 租户名称
        :type domain_name: str
        :param league: 
        :type league: :class:`huaweicloudsdktics.v1.TicsLeagueNoticeVo`
        :param league_id: 联盟Id
        :type league_id: str
        :param league_name: 联盟名称
        :type league_name: str
        :param partner_id: 联盟参与方Id
        :type partner_id: str
        :param partner_status: 联盟参与方状态，JOINED.已加入，JOIN_PENDING_APPROVAL.待审核，JOIN_REJECTED.拒绝加入，QUIT.已退出
        :type partner_status: str
        :param partners: 
        :type partners: list[:class:`huaweicloudsdktics.v1.TicsLeaguePartnerVo`]
        :param update_id: 更新者Id
        :type update_id: str
        :param update_name: 更新者名称
        :type update_name: str
        :param update_time: 更新时间
        :type update_time: datetime
        """
        
        

        self._create_time = None
        self._creator_id = None
        self._creator_name = None
        self._domain_alias = None
        self._domain_name = None
        self._league = None
        self._league_id = None
        self._league_name = None
        self._partner_id = None
        self._partner_status = None
        self._partners = None
        self._update_id = None
        self._update_name = None
        self._update_time = None
        self.discriminator = None

        if create_time is not None:
            self.create_time = create_time
        if creator_id is not None:
            self.creator_id = creator_id
        if creator_name is not None:
            self.creator_name = creator_name
        if domain_alias is not None:
            self.domain_alias = domain_alias
        if domain_name is not None:
            self.domain_name = domain_name
        if league is not None:
            self.league = league
        if league_id is not None:
            self.league_id = league_id
        if league_name is not None:
            self.league_name = league_name
        if partner_id is not None:
            self.partner_id = partner_id
        if partner_status is not None:
            self.partner_status = partner_status
        if partners is not None:
            self.partners = partners
        if update_id is not None:
            self.update_id = update_id
        if update_name is not None:
            self.update_name = update_name
        if update_time is not None:
            self.update_time = update_time

    @property
    def create_time(self):
        """Gets the create_time of this TicsApproveLogVo.

        创建时间

        :return: The create_time of this TicsApproveLogVo.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this TicsApproveLogVo.

        创建时间

        :param create_time: The create_time of this TicsApproveLogVo.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def creator_id(self):
        """Gets the creator_id of this TicsApproveLogVo.

        创建者Id

        :return: The creator_id of this TicsApproveLogVo.
        :rtype: str
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        """Sets the creator_id of this TicsApproveLogVo.

        创建者Id

        :param creator_id: The creator_id of this TicsApproveLogVo.
        :type creator_id: str
        """
        self._creator_id = creator_id

    @property
    def creator_name(self):
        """Gets the creator_name of this TicsApproveLogVo.

        创建者名称

        :return: The creator_name of this TicsApproveLogVo.
        :rtype: str
        """
        return self._creator_name

    @creator_name.setter
    def creator_name(self, creator_name):
        """Sets the creator_name of this TicsApproveLogVo.

        创建者名称

        :param creator_name: The creator_name of this TicsApproveLogVo.
        :type creator_name: str
        """
        self._creator_name = creator_name

    @property
    def domain_alias(self):
        """Gets the domain_alias of this TicsApproveLogVo.

        租户别名

        :return: The domain_alias of this TicsApproveLogVo.
        :rtype: str
        """
        return self._domain_alias

    @domain_alias.setter
    def domain_alias(self, domain_alias):
        """Sets the domain_alias of this TicsApproveLogVo.

        租户别名

        :param domain_alias: The domain_alias of this TicsApproveLogVo.
        :type domain_alias: str
        """
        self._domain_alias = domain_alias

    @property
    def domain_name(self):
        """Gets the domain_name of this TicsApproveLogVo.

        租户名称

        :return: The domain_name of this TicsApproveLogVo.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this TicsApproveLogVo.

        租户名称

        :param domain_name: The domain_name of this TicsApproveLogVo.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def league(self):
        """Gets the league of this TicsApproveLogVo.

        :return: The league of this TicsApproveLogVo.
        :rtype: :class:`huaweicloudsdktics.v1.TicsLeagueNoticeVo`
        """
        return self._league

    @league.setter
    def league(self, league):
        """Sets the league of this TicsApproveLogVo.

        :param league: The league of this TicsApproveLogVo.
        :type league: :class:`huaweicloudsdktics.v1.TicsLeagueNoticeVo`
        """
        self._league = league

    @property
    def league_id(self):
        """Gets the league_id of this TicsApproveLogVo.

        联盟Id

        :return: The league_id of this TicsApproveLogVo.
        :rtype: str
        """
        return self._league_id

    @league_id.setter
    def league_id(self, league_id):
        """Sets the league_id of this TicsApproveLogVo.

        联盟Id

        :param league_id: The league_id of this TicsApproveLogVo.
        :type league_id: str
        """
        self._league_id = league_id

    @property
    def league_name(self):
        """Gets the league_name of this TicsApproveLogVo.

        联盟名称

        :return: The league_name of this TicsApproveLogVo.
        :rtype: str
        """
        return self._league_name

    @league_name.setter
    def league_name(self, league_name):
        """Sets the league_name of this TicsApproveLogVo.

        联盟名称

        :param league_name: The league_name of this TicsApproveLogVo.
        :type league_name: str
        """
        self._league_name = league_name

    @property
    def partner_id(self):
        """Gets the partner_id of this TicsApproveLogVo.

        联盟参与方Id

        :return: The partner_id of this TicsApproveLogVo.
        :rtype: str
        """
        return self._partner_id

    @partner_id.setter
    def partner_id(self, partner_id):
        """Sets the partner_id of this TicsApproveLogVo.

        联盟参与方Id

        :param partner_id: The partner_id of this TicsApproveLogVo.
        :type partner_id: str
        """
        self._partner_id = partner_id

    @property
    def partner_status(self):
        """Gets the partner_status of this TicsApproveLogVo.

        联盟参与方状态，JOINED.已加入，JOIN_PENDING_APPROVAL.待审核，JOIN_REJECTED.拒绝加入，QUIT.已退出

        :return: The partner_status of this TicsApproveLogVo.
        :rtype: str
        """
        return self._partner_status

    @partner_status.setter
    def partner_status(self, partner_status):
        """Sets the partner_status of this TicsApproveLogVo.

        联盟参与方状态，JOINED.已加入，JOIN_PENDING_APPROVAL.待审核，JOIN_REJECTED.拒绝加入，QUIT.已退出

        :param partner_status: The partner_status of this TicsApproveLogVo.
        :type partner_status: str
        """
        self._partner_status = partner_status

    @property
    def partners(self):
        """Gets the partners of this TicsApproveLogVo.

        :return: The partners of this TicsApproveLogVo.
        :rtype: list[:class:`huaweicloudsdktics.v1.TicsLeaguePartnerVo`]
        """
        return self._partners

    @partners.setter
    def partners(self, partners):
        """Sets the partners of this TicsApproveLogVo.

        :param partners: The partners of this TicsApproveLogVo.
        :type partners: list[:class:`huaweicloudsdktics.v1.TicsLeaguePartnerVo`]
        """
        self._partners = partners

    @property
    def update_id(self):
        """Gets the update_id of this TicsApproveLogVo.

        更新者Id

        :return: The update_id of this TicsApproveLogVo.
        :rtype: str
        """
        return self._update_id

    @update_id.setter
    def update_id(self, update_id):
        """Sets the update_id of this TicsApproveLogVo.

        更新者Id

        :param update_id: The update_id of this TicsApproveLogVo.
        :type update_id: str
        """
        self._update_id = update_id

    @property
    def update_name(self):
        """Gets the update_name of this TicsApproveLogVo.

        更新者名称

        :return: The update_name of this TicsApproveLogVo.
        :rtype: str
        """
        return self._update_name

    @update_name.setter
    def update_name(self, update_name):
        """Sets the update_name of this TicsApproveLogVo.

        更新者名称

        :param update_name: The update_name of this TicsApproveLogVo.
        :type update_name: str
        """
        self._update_name = update_name

    @property
    def update_time(self):
        """Gets the update_time of this TicsApproveLogVo.

        更新时间

        :return: The update_time of this TicsApproveLogVo.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this TicsApproveLogVo.

        更新时间

        :param update_time: The update_time of this TicsApproveLogVo.
        :type update_time: datetime
        """
        self._update_time = update_time

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
        if not isinstance(other, TicsApproveLogVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
