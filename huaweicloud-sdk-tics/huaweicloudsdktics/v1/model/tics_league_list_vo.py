# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TicsLeagueListVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'bcs_channel_name': 'str',
        'bcs_ip': 'str',
        'bcs_org_name': 'str',
        'block_chain_id': 'str',
        'block_chain_name': 'str',
        'create_date': 'datetime',
        'create_time': 'int',
        'creator_id': 'str',
        'creator_name': 'str',
        'expire_time': 'int',
        'id': 'str',
        'league_status': 'str',
        'name': 'str',
        'partners': 'int',
        'type': 'str',
        'version': 'str'
    }

    attribute_map = {
        'bcs_channel_name': 'bcs_channel_name',
        'bcs_ip': 'bcs_ip',
        'bcs_org_name': 'bcs_org_name',
        'block_chain_id': 'block_chain_id',
        'block_chain_name': 'block_chain_name',
        'create_date': 'create_date',
        'create_time': 'create_time',
        'creator_id': 'creator_id',
        'creator_name': 'creator_name',
        'expire_time': 'expire_time',
        'id': 'id',
        'league_status': 'league_status',
        'name': 'name',
        'partners': 'partners',
        'type': 'type',
        'version': 'version'
    }

    def __init__(self, bcs_channel_name=None, bcs_ip=None, bcs_org_name=None, block_chain_id=None, block_chain_name=None, create_date=None, create_time=None, creator_id=None, creator_name=None, expire_time=None, id=None, league_status=None, name=None, partners=None, type=None, version=None):
        """TicsLeagueListVo

        The model defined in huaweicloud sdk

        :param bcs_channel_name: BCS通道名称
        :type bcs_channel_name: str
        :param bcs_ip: BCS浏览器ip
        :type bcs_ip: str
        :param bcs_org_name: BCS组织名称
        :type bcs_org_name: str
        :param block_chain_id: BCS服务实例ID
        :type block_chain_id: str
        :param block_chain_name: BCS服务实例名称
        :type block_chain_name: str
        :param create_date: 创建日期
        :type create_date: datetime
        :param create_time: 创建时间
        :type create_time: int
        :param creator_id: 创建人id
        :type creator_id: str
        :param creator_name: 创建人名称
        :type creator_name: str
        :param expire_time: 过期时间
        :type expire_time: int
        :param id: 联盟id
        :type id: str
        :param league_status: 联盟状态,CREATING.创建中,CREATE_FAILED.创建失败,NORMAL.正常,UPDATING.升级中,UPDATE_FAILED.升级失败,ROLLING.回滚中,ROLL_FAILED.回滚失败,DELETING.删除中,DELETE_FAILED.删除失败,DELETED.已删除
        :type league_status: str
        :param name: 联盟名称
        :type name: str
        :param partners: 联盟成员数
        :type partners: int
        :param type: 参与类型,OWNER.所有者,PARTNER.参与者
        :type type: str
        :param version: 联盟版本
        :type version: str
        """
        
        

        self._bcs_channel_name = None
        self._bcs_ip = None
        self._bcs_org_name = None
        self._block_chain_id = None
        self._block_chain_name = None
        self._create_date = None
        self._create_time = None
        self._creator_id = None
        self._creator_name = None
        self._expire_time = None
        self._id = None
        self._league_status = None
        self._name = None
        self._partners = None
        self._type = None
        self._version = None
        self.discriminator = None

        if bcs_channel_name is not None:
            self.bcs_channel_name = bcs_channel_name
        if bcs_ip is not None:
            self.bcs_ip = bcs_ip
        if bcs_org_name is not None:
            self.bcs_org_name = bcs_org_name
        if block_chain_id is not None:
            self.block_chain_id = block_chain_id
        if block_chain_name is not None:
            self.block_chain_name = block_chain_name
        if create_date is not None:
            self.create_date = create_date
        if create_time is not None:
            self.create_time = create_time
        self.creator_id = creator_id
        self.creator_name = creator_name
        if expire_time is not None:
            self.expire_time = expire_time
        self.id = id
        self.league_status = league_status
        self.name = name
        self.partners = partners
        self.type = type
        if version is not None:
            self.version = version

    @property
    def bcs_channel_name(self):
        """Gets the bcs_channel_name of this TicsLeagueListVo.

        BCS通道名称

        :return: The bcs_channel_name of this TicsLeagueListVo.
        :rtype: str
        """
        return self._bcs_channel_name

    @bcs_channel_name.setter
    def bcs_channel_name(self, bcs_channel_name):
        """Sets the bcs_channel_name of this TicsLeagueListVo.

        BCS通道名称

        :param bcs_channel_name: The bcs_channel_name of this TicsLeagueListVo.
        :type bcs_channel_name: str
        """
        self._bcs_channel_name = bcs_channel_name

    @property
    def bcs_ip(self):
        """Gets the bcs_ip of this TicsLeagueListVo.

        BCS浏览器ip

        :return: The bcs_ip of this TicsLeagueListVo.
        :rtype: str
        """
        return self._bcs_ip

    @bcs_ip.setter
    def bcs_ip(self, bcs_ip):
        """Sets the bcs_ip of this TicsLeagueListVo.

        BCS浏览器ip

        :param bcs_ip: The bcs_ip of this TicsLeagueListVo.
        :type bcs_ip: str
        """
        self._bcs_ip = bcs_ip

    @property
    def bcs_org_name(self):
        """Gets the bcs_org_name of this TicsLeagueListVo.

        BCS组织名称

        :return: The bcs_org_name of this TicsLeagueListVo.
        :rtype: str
        """
        return self._bcs_org_name

    @bcs_org_name.setter
    def bcs_org_name(self, bcs_org_name):
        """Sets the bcs_org_name of this TicsLeagueListVo.

        BCS组织名称

        :param bcs_org_name: The bcs_org_name of this TicsLeagueListVo.
        :type bcs_org_name: str
        """
        self._bcs_org_name = bcs_org_name

    @property
    def block_chain_id(self):
        """Gets the block_chain_id of this TicsLeagueListVo.

        BCS服务实例ID

        :return: The block_chain_id of this TicsLeagueListVo.
        :rtype: str
        """
        return self._block_chain_id

    @block_chain_id.setter
    def block_chain_id(self, block_chain_id):
        """Sets the block_chain_id of this TicsLeagueListVo.

        BCS服务实例ID

        :param block_chain_id: The block_chain_id of this TicsLeagueListVo.
        :type block_chain_id: str
        """
        self._block_chain_id = block_chain_id

    @property
    def block_chain_name(self):
        """Gets the block_chain_name of this TicsLeagueListVo.

        BCS服务实例名称

        :return: The block_chain_name of this TicsLeagueListVo.
        :rtype: str
        """
        return self._block_chain_name

    @block_chain_name.setter
    def block_chain_name(self, block_chain_name):
        """Sets the block_chain_name of this TicsLeagueListVo.

        BCS服务实例名称

        :param block_chain_name: The block_chain_name of this TicsLeagueListVo.
        :type block_chain_name: str
        """
        self._block_chain_name = block_chain_name

    @property
    def create_date(self):
        """Gets the create_date of this TicsLeagueListVo.

        创建日期

        :return: The create_date of this TicsLeagueListVo.
        :rtype: datetime
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """Sets the create_date of this TicsLeagueListVo.

        创建日期

        :param create_date: The create_date of this TicsLeagueListVo.
        :type create_date: datetime
        """
        self._create_date = create_date

    @property
    def create_time(self):
        """Gets the create_time of this TicsLeagueListVo.

        创建时间

        :return: The create_time of this TicsLeagueListVo.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this TicsLeagueListVo.

        创建时间

        :param create_time: The create_time of this TicsLeagueListVo.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def creator_id(self):
        """Gets the creator_id of this TicsLeagueListVo.

        创建人id

        :return: The creator_id of this TicsLeagueListVo.
        :rtype: str
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        """Sets the creator_id of this TicsLeagueListVo.

        创建人id

        :param creator_id: The creator_id of this TicsLeagueListVo.
        :type creator_id: str
        """
        self._creator_id = creator_id

    @property
    def creator_name(self):
        """Gets the creator_name of this TicsLeagueListVo.

        创建人名称

        :return: The creator_name of this TicsLeagueListVo.
        :rtype: str
        """
        return self._creator_name

    @creator_name.setter
    def creator_name(self, creator_name):
        """Sets the creator_name of this TicsLeagueListVo.

        创建人名称

        :param creator_name: The creator_name of this TicsLeagueListVo.
        :type creator_name: str
        """
        self._creator_name = creator_name

    @property
    def expire_time(self):
        """Gets the expire_time of this TicsLeagueListVo.

        过期时间

        :return: The expire_time of this TicsLeagueListVo.
        :rtype: int
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        """Sets the expire_time of this TicsLeagueListVo.

        过期时间

        :param expire_time: The expire_time of this TicsLeagueListVo.
        :type expire_time: int
        """
        self._expire_time = expire_time

    @property
    def id(self):
        """Gets the id of this TicsLeagueListVo.

        联盟id

        :return: The id of this TicsLeagueListVo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TicsLeagueListVo.

        联盟id

        :param id: The id of this TicsLeagueListVo.
        :type id: str
        """
        self._id = id

    @property
    def league_status(self):
        """Gets the league_status of this TicsLeagueListVo.

        联盟状态,CREATING.创建中,CREATE_FAILED.创建失败,NORMAL.正常,UPDATING.升级中,UPDATE_FAILED.升级失败,ROLLING.回滚中,ROLL_FAILED.回滚失败,DELETING.删除中,DELETE_FAILED.删除失败,DELETED.已删除

        :return: The league_status of this TicsLeagueListVo.
        :rtype: str
        """
        return self._league_status

    @league_status.setter
    def league_status(self, league_status):
        """Sets the league_status of this TicsLeagueListVo.

        联盟状态,CREATING.创建中,CREATE_FAILED.创建失败,NORMAL.正常,UPDATING.升级中,UPDATE_FAILED.升级失败,ROLLING.回滚中,ROLL_FAILED.回滚失败,DELETING.删除中,DELETE_FAILED.删除失败,DELETED.已删除

        :param league_status: The league_status of this TicsLeagueListVo.
        :type league_status: str
        """
        self._league_status = league_status

    @property
    def name(self):
        """Gets the name of this TicsLeagueListVo.

        联盟名称

        :return: The name of this TicsLeagueListVo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TicsLeagueListVo.

        联盟名称

        :param name: The name of this TicsLeagueListVo.
        :type name: str
        """
        self._name = name

    @property
    def partners(self):
        """Gets the partners of this TicsLeagueListVo.

        联盟成员数

        :return: The partners of this TicsLeagueListVo.
        :rtype: int
        """
        return self._partners

    @partners.setter
    def partners(self, partners):
        """Sets the partners of this TicsLeagueListVo.

        联盟成员数

        :param partners: The partners of this TicsLeagueListVo.
        :type partners: int
        """
        self._partners = partners

    @property
    def type(self):
        """Gets the type of this TicsLeagueListVo.

        参与类型,OWNER.所有者,PARTNER.参与者

        :return: The type of this TicsLeagueListVo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TicsLeagueListVo.

        参与类型,OWNER.所有者,PARTNER.参与者

        :param type: The type of this TicsLeagueListVo.
        :type type: str
        """
        self._type = type

    @property
    def version(self):
        """Gets the version of this TicsLeagueListVo.

        联盟版本

        :return: The version of this TicsLeagueListVo.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this TicsLeagueListVo.

        联盟版本

        :param version: The version of this TicsLeagueListVo.
        :type version: str
        """
        self._version = version

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
        if not isinstance(other, TicsLeagueListVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
