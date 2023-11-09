# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TicsLeagueNoticeVo:

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
        'create_time': 'int',
        'creator_name': 'str',
        'description': 'str',
        'expire_time': 'int',
        'id': 'str',
        'name': 'str',
        'partners': 'int'
    }

    attribute_map = {
        'bcs_channel_name': 'bcs_channel_name',
        'bcs_ip': 'bcs_ip',
        'bcs_org_name': 'bcs_org_name',
        'block_chain_id': 'block_chain_id',
        'block_chain_name': 'block_chain_name',
        'create_time': 'create_time',
        'creator_name': 'creator_name',
        'description': 'description',
        'expire_time': 'expire_time',
        'id': 'id',
        'name': 'name',
        'partners': 'partners'
    }

    def __init__(self, bcs_channel_name=None, bcs_ip=None, bcs_org_name=None, block_chain_id=None, block_chain_name=None, create_time=None, creator_name=None, description=None, expire_time=None, id=None, name=None, partners=None):
        """TicsLeagueNoticeVo

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
        :param create_time: 创建时间
        :type create_time: int
        :param creator_name: 创建人名称
        :type creator_name: str
        :param description: 描述信息
        :type description: str
        :param expire_time: 过期时间
        :type expire_time: int
        :param id: 联盟id
        :type id: str
        :param name: 联盟名称
        :type name: str
        :param partners: 联盟成员数
        :type partners: int
        """
        
        

        self._bcs_channel_name = None
        self._bcs_ip = None
        self._bcs_org_name = None
        self._block_chain_id = None
        self._block_chain_name = None
        self._create_time = None
        self._creator_name = None
        self._description = None
        self._expire_time = None
        self._id = None
        self._name = None
        self._partners = None
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
        if create_time is not None:
            self.create_time = create_time
        self.creator_name = creator_name
        if description is not None:
            self.description = description
        if expire_time is not None:
            self.expire_time = expire_time
        self.id = id
        self.name = name
        self.partners = partners

    @property
    def bcs_channel_name(self):
        """Gets the bcs_channel_name of this TicsLeagueNoticeVo.

        BCS通道名称

        :return: The bcs_channel_name of this TicsLeagueNoticeVo.
        :rtype: str
        """
        return self._bcs_channel_name

    @bcs_channel_name.setter
    def bcs_channel_name(self, bcs_channel_name):
        """Sets the bcs_channel_name of this TicsLeagueNoticeVo.

        BCS通道名称

        :param bcs_channel_name: The bcs_channel_name of this TicsLeagueNoticeVo.
        :type bcs_channel_name: str
        """
        self._bcs_channel_name = bcs_channel_name

    @property
    def bcs_ip(self):
        """Gets the bcs_ip of this TicsLeagueNoticeVo.

        BCS浏览器ip

        :return: The bcs_ip of this TicsLeagueNoticeVo.
        :rtype: str
        """
        return self._bcs_ip

    @bcs_ip.setter
    def bcs_ip(self, bcs_ip):
        """Sets the bcs_ip of this TicsLeagueNoticeVo.

        BCS浏览器ip

        :param bcs_ip: The bcs_ip of this TicsLeagueNoticeVo.
        :type bcs_ip: str
        """
        self._bcs_ip = bcs_ip

    @property
    def bcs_org_name(self):
        """Gets the bcs_org_name of this TicsLeagueNoticeVo.

        BCS组织名称

        :return: The bcs_org_name of this TicsLeagueNoticeVo.
        :rtype: str
        """
        return self._bcs_org_name

    @bcs_org_name.setter
    def bcs_org_name(self, bcs_org_name):
        """Sets the bcs_org_name of this TicsLeagueNoticeVo.

        BCS组织名称

        :param bcs_org_name: The bcs_org_name of this TicsLeagueNoticeVo.
        :type bcs_org_name: str
        """
        self._bcs_org_name = bcs_org_name

    @property
    def block_chain_id(self):
        """Gets the block_chain_id of this TicsLeagueNoticeVo.

        BCS服务实例ID

        :return: The block_chain_id of this TicsLeagueNoticeVo.
        :rtype: str
        """
        return self._block_chain_id

    @block_chain_id.setter
    def block_chain_id(self, block_chain_id):
        """Sets the block_chain_id of this TicsLeagueNoticeVo.

        BCS服务实例ID

        :param block_chain_id: The block_chain_id of this TicsLeagueNoticeVo.
        :type block_chain_id: str
        """
        self._block_chain_id = block_chain_id

    @property
    def block_chain_name(self):
        """Gets the block_chain_name of this TicsLeagueNoticeVo.

        BCS服务实例名称

        :return: The block_chain_name of this TicsLeagueNoticeVo.
        :rtype: str
        """
        return self._block_chain_name

    @block_chain_name.setter
    def block_chain_name(self, block_chain_name):
        """Sets the block_chain_name of this TicsLeagueNoticeVo.

        BCS服务实例名称

        :param block_chain_name: The block_chain_name of this TicsLeagueNoticeVo.
        :type block_chain_name: str
        """
        self._block_chain_name = block_chain_name

    @property
    def create_time(self):
        """Gets the create_time of this TicsLeagueNoticeVo.

        创建时间

        :return: The create_time of this TicsLeagueNoticeVo.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this TicsLeagueNoticeVo.

        创建时间

        :param create_time: The create_time of this TicsLeagueNoticeVo.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def creator_name(self):
        """Gets the creator_name of this TicsLeagueNoticeVo.

        创建人名称

        :return: The creator_name of this TicsLeagueNoticeVo.
        :rtype: str
        """
        return self._creator_name

    @creator_name.setter
    def creator_name(self, creator_name):
        """Sets the creator_name of this TicsLeagueNoticeVo.

        创建人名称

        :param creator_name: The creator_name of this TicsLeagueNoticeVo.
        :type creator_name: str
        """
        self._creator_name = creator_name

    @property
    def description(self):
        """Gets the description of this TicsLeagueNoticeVo.

        描述信息

        :return: The description of this TicsLeagueNoticeVo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TicsLeagueNoticeVo.

        描述信息

        :param description: The description of this TicsLeagueNoticeVo.
        :type description: str
        """
        self._description = description

    @property
    def expire_time(self):
        """Gets the expire_time of this TicsLeagueNoticeVo.

        过期时间

        :return: The expire_time of this TicsLeagueNoticeVo.
        :rtype: int
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        """Sets the expire_time of this TicsLeagueNoticeVo.

        过期时间

        :param expire_time: The expire_time of this TicsLeagueNoticeVo.
        :type expire_time: int
        """
        self._expire_time = expire_time

    @property
    def id(self):
        """Gets the id of this TicsLeagueNoticeVo.

        联盟id

        :return: The id of this TicsLeagueNoticeVo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TicsLeagueNoticeVo.

        联盟id

        :param id: The id of this TicsLeagueNoticeVo.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this TicsLeagueNoticeVo.

        联盟名称

        :return: The name of this TicsLeagueNoticeVo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TicsLeagueNoticeVo.

        联盟名称

        :param name: The name of this TicsLeagueNoticeVo.
        :type name: str
        """
        self._name = name

    @property
    def partners(self):
        """Gets the partners of this TicsLeagueNoticeVo.

        联盟成员数

        :return: The partners of this TicsLeagueNoticeVo.
        :rtype: int
        """
        return self._partners

    @partners.setter
    def partners(self, partners):
        """Sets the partners of this TicsLeagueNoticeVo.

        联盟成员数

        :param partners: The partners of this TicsLeagueNoticeVo.
        :type partners: int
        """
        self._partners = partners

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
        if not isinstance(other, TicsLeagueNoticeVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
