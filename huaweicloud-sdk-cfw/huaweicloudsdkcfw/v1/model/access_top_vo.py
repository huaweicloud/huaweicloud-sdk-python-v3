# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AccessTopVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'deny_count': 'int',
        'deny_top_one_acl_id': 'str',
        'deny_top_one_acl_name': 'str',
        'hit_count': 'int',
        'in2out_deny_dst_ip_list': 'list[AccessTopMemberVO]',
        'in2out_deny_dst_port_list': 'list[AccessTopMemberVO]',
        'in2out_deny_dst_region_list': 'list[AccessTopMemberVO]',
        'in2out_deny_src_ip_list': 'list[AccessTopMemberVO]',
        'out2in_deny_dst_ip_list': 'list[AccessTopMemberVO]',
        'out2in_deny_dst_port_list': 'list[AccessTopMemberVO]',
        'out2in_deny_src_ip_list': 'list[AccessTopMemberVO]',
        'out2in_deny_src_port_list': 'list[AccessTopMemberVO]',
        'out2in_deny_src_region_list': 'list[AccessTopMemberVO]',
        'permit_count': 'int',
        'permit_top_one_acl_id': 'str',
        'permit_top_one_acl_name': 'str',
        'records': 'list[AccessTopStatisticsVO]',
        'top_deny_rule_list': 'list[AccessTopMemberVO]'
    }

    attribute_map = {
        'deny_count': 'deny_count',
        'deny_top_one_acl_id': 'deny_top_one_acl_id',
        'deny_top_one_acl_name': 'deny_top_one_acl_name',
        'hit_count': 'hit_count',
        'in2out_deny_dst_ip_list': 'in2out_deny_dst_ip_list',
        'in2out_deny_dst_port_list': 'in2out_deny_dst_port_list',
        'in2out_deny_dst_region_list': 'in2out_deny_dst_region_list',
        'in2out_deny_src_ip_list': 'in2out_deny_src_ip_list',
        'out2in_deny_dst_ip_list': 'out2in_deny_dst_ip_list',
        'out2in_deny_dst_port_list': 'out2in_deny_dst_port_list',
        'out2in_deny_src_ip_list': 'out2in_deny_src_ip_list',
        'out2in_deny_src_port_list': 'out2in_deny_src_port_list',
        'out2in_deny_src_region_list': 'out2in_deny_src_region_list',
        'permit_count': 'permit_count',
        'permit_top_one_acl_id': 'permit_top_one_acl_id',
        'permit_top_one_acl_name': 'permit_top_one_acl_name',
        'records': 'records',
        'top_deny_rule_list': 'top_deny_rule_list'
    }

    def __init__(self, deny_count=None, deny_top_one_acl_id=None, deny_top_one_acl_name=None, hit_count=None, in2out_deny_dst_ip_list=None, in2out_deny_dst_port_list=None, in2out_deny_dst_region_list=None, in2out_deny_src_ip_list=None, out2in_deny_dst_ip_list=None, out2in_deny_dst_port_list=None, out2in_deny_src_ip_list=None, out2in_deny_src_port_list=None, out2in_deny_src_region_list=None, permit_count=None, permit_top_one_acl_id=None, permit_top_one_acl_name=None, records=None, top_deny_rule_list=None):
        r"""AccessTopVO

        The model defined in huaweicloud sdk

        :param deny_count: **参数解释**： 阻断次数 **取值范围**： 不涉及
        :type deny_count: int
        :param deny_top_one_acl_id: **参数解释**： 高频命中的阻断策略ID **取值范围**： 不涉及
        :type deny_top_one_acl_id: str
        :param deny_top_one_acl_name: **参数解释**： 高频命中的阻断策略ID **取值范围**： 不涉及
        :type deny_top_one_acl_name: str
        :param hit_count: **参数解释**： 命中次数 **取值范围**： 不涉及
        :type hit_count: int
        :param in2out_deny_dst_ip_list: **参数解释**： TOP出云阻断目的IP列表 **取值范围**： 不涉及
        :type in2out_deny_dst_ip_list: list[:class:`huaweicloudsdkcfw.v1.AccessTopMemberVO`]
        :param in2out_deny_dst_port_list: **参数解释**： TOP出云阻断端口列表 **取值范围**： 不涉及
        :type in2out_deny_dst_port_list: list[:class:`huaweicloudsdkcfw.v1.AccessTopMemberVO`]
        :param in2out_deny_dst_region_list: **参数解释**： TOP出云阻断目的地区列表 **取值范围**： 不涉及
        :type in2out_deny_dst_region_list: list[:class:`huaweicloudsdkcfw.v1.AccessTopMemberVO`]
        :param in2out_deny_src_ip_list: **参数解释**： TOP出云阻断源IP列表 **取值范围**： 不涉及
        :type in2out_deny_src_ip_list: list[:class:`huaweicloudsdkcfw.v1.AccessTopMemberVO`]
        :param out2in_deny_dst_ip_list: **参数解释**： TOP入云阻断目的IP列表 **取值范围**： 不涉及
        :type out2in_deny_dst_ip_list: list[:class:`huaweicloudsdkcfw.v1.AccessTopMemberVO`]
        :param out2in_deny_dst_port_list: **参数解释**： TOP入云阻断目的端口列表 **取值范围**： 不涉及
        :type out2in_deny_dst_port_list: list[:class:`huaweicloudsdkcfw.v1.AccessTopMemberVO`]
        :param out2in_deny_src_ip_list: **参数解释**： TOP入云阻断源IP列表 **取值范围**： 不涉及
        :type out2in_deny_src_ip_list: list[:class:`huaweicloudsdkcfw.v1.AccessTopMemberVO`]
        :param out2in_deny_src_port_list: **参数解释**： TOP入云阻断源端口列表 **取值范围**： 不涉及
        :type out2in_deny_src_port_list: list[:class:`huaweicloudsdkcfw.v1.AccessTopMemberVO`]
        :param out2in_deny_src_region_list: **参数解释**： TOP入云阻断源地区列表 **取值范围**： 不涉及
        :type out2in_deny_src_region_list: list[:class:`huaweicloudsdkcfw.v1.AccessTopMemberVO`]
        :param permit_count: **参数解释**： 放行次数 **取值范围**： 不涉及
        :type permit_count: int
        :param permit_top_one_acl_id: **参数解释**： 高频命中的放行策略ID **取值范围**： 不涉及
        :type permit_top_one_acl_id: str
        :param permit_top_one_acl_name: **参数解释**： 高频命中的放行策略名称 **取值范围**： 不涉及
        :type permit_top_one_acl_name: str
        :param records: **参数解释**： 命中趋势 **取值范围**： 不涉及
        :type records: list[:class:`huaweicloudsdkcfw.v1.AccessTopStatisticsVO`]
        :param top_deny_rule_list: **参数解释**： TOP阻断规则列表 **取值范围**： 不涉及
        :type top_deny_rule_list: list[:class:`huaweicloudsdkcfw.v1.AccessTopMemberVO`]
        """
        
        

        self._deny_count = None
        self._deny_top_one_acl_id = None
        self._deny_top_one_acl_name = None
        self._hit_count = None
        self._in2out_deny_dst_ip_list = None
        self._in2out_deny_dst_port_list = None
        self._in2out_deny_dst_region_list = None
        self._in2out_deny_src_ip_list = None
        self._out2in_deny_dst_ip_list = None
        self._out2in_deny_dst_port_list = None
        self._out2in_deny_src_ip_list = None
        self._out2in_deny_src_port_list = None
        self._out2in_deny_src_region_list = None
        self._permit_count = None
        self._permit_top_one_acl_id = None
        self._permit_top_one_acl_name = None
        self._records = None
        self._top_deny_rule_list = None
        self.discriminator = None

        if deny_count is not None:
            self.deny_count = deny_count
        if deny_top_one_acl_id is not None:
            self.deny_top_one_acl_id = deny_top_one_acl_id
        if deny_top_one_acl_name is not None:
            self.deny_top_one_acl_name = deny_top_one_acl_name
        if hit_count is not None:
            self.hit_count = hit_count
        if in2out_deny_dst_ip_list is not None:
            self.in2out_deny_dst_ip_list = in2out_deny_dst_ip_list
        if in2out_deny_dst_port_list is not None:
            self.in2out_deny_dst_port_list = in2out_deny_dst_port_list
        if in2out_deny_dst_region_list is not None:
            self.in2out_deny_dst_region_list = in2out_deny_dst_region_list
        if in2out_deny_src_ip_list is not None:
            self.in2out_deny_src_ip_list = in2out_deny_src_ip_list
        if out2in_deny_dst_ip_list is not None:
            self.out2in_deny_dst_ip_list = out2in_deny_dst_ip_list
        if out2in_deny_dst_port_list is not None:
            self.out2in_deny_dst_port_list = out2in_deny_dst_port_list
        if out2in_deny_src_ip_list is not None:
            self.out2in_deny_src_ip_list = out2in_deny_src_ip_list
        if out2in_deny_src_port_list is not None:
            self.out2in_deny_src_port_list = out2in_deny_src_port_list
        if out2in_deny_src_region_list is not None:
            self.out2in_deny_src_region_list = out2in_deny_src_region_list
        if permit_count is not None:
            self.permit_count = permit_count
        if permit_top_one_acl_id is not None:
            self.permit_top_one_acl_id = permit_top_one_acl_id
        if permit_top_one_acl_name is not None:
            self.permit_top_one_acl_name = permit_top_one_acl_name
        if records is not None:
            self.records = records
        if top_deny_rule_list is not None:
            self.top_deny_rule_list = top_deny_rule_list

    @property
    def deny_count(self):
        r"""Gets the deny_count of this AccessTopVO.

        **参数解释**： 阻断次数 **取值范围**： 不涉及

        :return: The deny_count of this AccessTopVO.
        :rtype: int
        """
        return self._deny_count

    @deny_count.setter
    def deny_count(self, deny_count):
        r"""Sets the deny_count of this AccessTopVO.

        **参数解释**： 阻断次数 **取值范围**： 不涉及

        :param deny_count: The deny_count of this AccessTopVO.
        :type deny_count: int
        """
        self._deny_count = deny_count

    @property
    def deny_top_one_acl_id(self):
        r"""Gets the deny_top_one_acl_id of this AccessTopVO.

        **参数解释**： 高频命中的阻断策略ID **取值范围**： 不涉及

        :return: The deny_top_one_acl_id of this AccessTopVO.
        :rtype: str
        """
        return self._deny_top_one_acl_id

    @deny_top_one_acl_id.setter
    def deny_top_one_acl_id(self, deny_top_one_acl_id):
        r"""Sets the deny_top_one_acl_id of this AccessTopVO.

        **参数解释**： 高频命中的阻断策略ID **取值范围**： 不涉及

        :param deny_top_one_acl_id: The deny_top_one_acl_id of this AccessTopVO.
        :type deny_top_one_acl_id: str
        """
        self._deny_top_one_acl_id = deny_top_one_acl_id

    @property
    def deny_top_one_acl_name(self):
        r"""Gets the deny_top_one_acl_name of this AccessTopVO.

        **参数解释**： 高频命中的阻断策略ID **取值范围**： 不涉及

        :return: The deny_top_one_acl_name of this AccessTopVO.
        :rtype: str
        """
        return self._deny_top_one_acl_name

    @deny_top_one_acl_name.setter
    def deny_top_one_acl_name(self, deny_top_one_acl_name):
        r"""Sets the deny_top_one_acl_name of this AccessTopVO.

        **参数解释**： 高频命中的阻断策略ID **取值范围**： 不涉及

        :param deny_top_one_acl_name: The deny_top_one_acl_name of this AccessTopVO.
        :type deny_top_one_acl_name: str
        """
        self._deny_top_one_acl_name = deny_top_one_acl_name

    @property
    def hit_count(self):
        r"""Gets the hit_count of this AccessTopVO.

        **参数解释**： 命中次数 **取值范围**： 不涉及

        :return: The hit_count of this AccessTopVO.
        :rtype: int
        """
        return self._hit_count

    @hit_count.setter
    def hit_count(self, hit_count):
        r"""Sets the hit_count of this AccessTopVO.

        **参数解释**： 命中次数 **取值范围**： 不涉及

        :param hit_count: The hit_count of this AccessTopVO.
        :type hit_count: int
        """
        self._hit_count = hit_count

    @property
    def in2out_deny_dst_ip_list(self):
        r"""Gets the in2out_deny_dst_ip_list of this AccessTopVO.

        **参数解释**： TOP出云阻断目的IP列表 **取值范围**： 不涉及

        :return: The in2out_deny_dst_ip_list of this AccessTopVO.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.AccessTopMemberVO`]
        """
        return self._in2out_deny_dst_ip_list

    @in2out_deny_dst_ip_list.setter
    def in2out_deny_dst_ip_list(self, in2out_deny_dst_ip_list):
        r"""Sets the in2out_deny_dst_ip_list of this AccessTopVO.

        **参数解释**： TOP出云阻断目的IP列表 **取值范围**： 不涉及

        :param in2out_deny_dst_ip_list: The in2out_deny_dst_ip_list of this AccessTopVO.
        :type in2out_deny_dst_ip_list: list[:class:`huaweicloudsdkcfw.v1.AccessTopMemberVO`]
        """
        self._in2out_deny_dst_ip_list = in2out_deny_dst_ip_list

    @property
    def in2out_deny_dst_port_list(self):
        r"""Gets the in2out_deny_dst_port_list of this AccessTopVO.

        **参数解释**： TOP出云阻断端口列表 **取值范围**： 不涉及

        :return: The in2out_deny_dst_port_list of this AccessTopVO.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.AccessTopMemberVO`]
        """
        return self._in2out_deny_dst_port_list

    @in2out_deny_dst_port_list.setter
    def in2out_deny_dst_port_list(self, in2out_deny_dst_port_list):
        r"""Sets the in2out_deny_dst_port_list of this AccessTopVO.

        **参数解释**： TOP出云阻断端口列表 **取值范围**： 不涉及

        :param in2out_deny_dst_port_list: The in2out_deny_dst_port_list of this AccessTopVO.
        :type in2out_deny_dst_port_list: list[:class:`huaweicloudsdkcfw.v1.AccessTopMemberVO`]
        """
        self._in2out_deny_dst_port_list = in2out_deny_dst_port_list

    @property
    def in2out_deny_dst_region_list(self):
        r"""Gets the in2out_deny_dst_region_list of this AccessTopVO.

        **参数解释**： TOP出云阻断目的地区列表 **取值范围**： 不涉及

        :return: The in2out_deny_dst_region_list of this AccessTopVO.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.AccessTopMemberVO`]
        """
        return self._in2out_deny_dst_region_list

    @in2out_deny_dst_region_list.setter
    def in2out_deny_dst_region_list(self, in2out_deny_dst_region_list):
        r"""Sets the in2out_deny_dst_region_list of this AccessTopVO.

        **参数解释**： TOP出云阻断目的地区列表 **取值范围**： 不涉及

        :param in2out_deny_dst_region_list: The in2out_deny_dst_region_list of this AccessTopVO.
        :type in2out_deny_dst_region_list: list[:class:`huaweicloudsdkcfw.v1.AccessTopMemberVO`]
        """
        self._in2out_deny_dst_region_list = in2out_deny_dst_region_list

    @property
    def in2out_deny_src_ip_list(self):
        r"""Gets the in2out_deny_src_ip_list of this AccessTopVO.

        **参数解释**： TOP出云阻断源IP列表 **取值范围**： 不涉及

        :return: The in2out_deny_src_ip_list of this AccessTopVO.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.AccessTopMemberVO`]
        """
        return self._in2out_deny_src_ip_list

    @in2out_deny_src_ip_list.setter
    def in2out_deny_src_ip_list(self, in2out_deny_src_ip_list):
        r"""Sets the in2out_deny_src_ip_list of this AccessTopVO.

        **参数解释**： TOP出云阻断源IP列表 **取值范围**： 不涉及

        :param in2out_deny_src_ip_list: The in2out_deny_src_ip_list of this AccessTopVO.
        :type in2out_deny_src_ip_list: list[:class:`huaweicloudsdkcfw.v1.AccessTopMemberVO`]
        """
        self._in2out_deny_src_ip_list = in2out_deny_src_ip_list

    @property
    def out2in_deny_dst_ip_list(self):
        r"""Gets the out2in_deny_dst_ip_list of this AccessTopVO.

        **参数解释**： TOP入云阻断目的IP列表 **取值范围**： 不涉及

        :return: The out2in_deny_dst_ip_list of this AccessTopVO.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.AccessTopMemberVO`]
        """
        return self._out2in_deny_dst_ip_list

    @out2in_deny_dst_ip_list.setter
    def out2in_deny_dst_ip_list(self, out2in_deny_dst_ip_list):
        r"""Sets the out2in_deny_dst_ip_list of this AccessTopVO.

        **参数解释**： TOP入云阻断目的IP列表 **取值范围**： 不涉及

        :param out2in_deny_dst_ip_list: The out2in_deny_dst_ip_list of this AccessTopVO.
        :type out2in_deny_dst_ip_list: list[:class:`huaweicloudsdkcfw.v1.AccessTopMemberVO`]
        """
        self._out2in_deny_dst_ip_list = out2in_deny_dst_ip_list

    @property
    def out2in_deny_dst_port_list(self):
        r"""Gets the out2in_deny_dst_port_list of this AccessTopVO.

        **参数解释**： TOP入云阻断目的端口列表 **取值范围**： 不涉及

        :return: The out2in_deny_dst_port_list of this AccessTopVO.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.AccessTopMemberVO`]
        """
        return self._out2in_deny_dst_port_list

    @out2in_deny_dst_port_list.setter
    def out2in_deny_dst_port_list(self, out2in_deny_dst_port_list):
        r"""Sets the out2in_deny_dst_port_list of this AccessTopVO.

        **参数解释**： TOP入云阻断目的端口列表 **取值范围**： 不涉及

        :param out2in_deny_dst_port_list: The out2in_deny_dst_port_list of this AccessTopVO.
        :type out2in_deny_dst_port_list: list[:class:`huaweicloudsdkcfw.v1.AccessTopMemberVO`]
        """
        self._out2in_deny_dst_port_list = out2in_deny_dst_port_list

    @property
    def out2in_deny_src_ip_list(self):
        r"""Gets the out2in_deny_src_ip_list of this AccessTopVO.

        **参数解释**： TOP入云阻断源IP列表 **取值范围**： 不涉及

        :return: The out2in_deny_src_ip_list of this AccessTopVO.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.AccessTopMemberVO`]
        """
        return self._out2in_deny_src_ip_list

    @out2in_deny_src_ip_list.setter
    def out2in_deny_src_ip_list(self, out2in_deny_src_ip_list):
        r"""Sets the out2in_deny_src_ip_list of this AccessTopVO.

        **参数解释**： TOP入云阻断源IP列表 **取值范围**： 不涉及

        :param out2in_deny_src_ip_list: The out2in_deny_src_ip_list of this AccessTopVO.
        :type out2in_deny_src_ip_list: list[:class:`huaweicloudsdkcfw.v1.AccessTopMemberVO`]
        """
        self._out2in_deny_src_ip_list = out2in_deny_src_ip_list

    @property
    def out2in_deny_src_port_list(self):
        r"""Gets the out2in_deny_src_port_list of this AccessTopVO.

        **参数解释**： TOP入云阻断源端口列表 **取值范围**： 不涉及

        :return: The out2in_deny_src_port_list of this AccessTopVO.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.AccessTopMemberVO`]
        """
        return self._out2in_deny_src_port_list

    @out2in_deny_src_port_list.setter
    def out2in_deny_src_port_list(self, out2in_deny_src_port_list):
        r"""Sets the out2in_deny_src_port_list of this AccessTopVO.

        **参数解释**： TOP入云阻断源端口列表 **取值范围**： 不涉及

        :param out2in_deny_src_port_list: The out2in_deny_src_port_list of this AccessTopVO.
        :type out2in_deny_src_port_list: list[:class:`huaweicloudsdkcfw.v1.AccessTopMemberVO`]
        """
        self._out2in_deny_src_port_list = out2in_deny_src_port_list

    @property
    def out2in_deny_src_region_list(self):
        r"""Gets the out2in_deny_src_region_list of this AccessTopVO.

        **参数解释**： TOP入云阻断源地区列表 **取值范围**： 不涉及

        :return: The out2in_deny_src_region_list of this AccessTopVO.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.AccessTopMemberVO`]
        """
        return self._out2in_deny_src_region_list

    @out2in_deny_src_region_list.setter
    def out2in_deny_src_region_list(self, out2in_deny_src_region_list):
        r"""Sets the out2in_deny_src_region_list of this AccessTopVO.

        **参数解释**： TOP入云阻断源地区列表 **取值范围**： 不涉及

        :param out2in_deny_src_region_list: The out2in_deny_src_region_list of this AccessTopVO.
        :type out2in_deny_src_region_list: list[:class:`huaweicloudsdkcfw.v1.AccessTopMemberVO`]
        """
        self._out2in_deny_src_region_list = out2in_deny_src_region_list

    @property
    def permit_count(self):
        r"""Gets the permit_count of this AccessTopVO.

        **参数解释**： 放行次数 **取值范围**： 不涉及

        :return: The permit_count of this AccessTopVO.
        :rtype: int
        """
        return self._permit_count

    @permit_count.setter
    def permit_count(self, permit_count):
        r"""Sets the permit_count of this AccessTopVO.

        **参数解释**： 放行次数 **取值范围**： 不涉及

        :param permit_count: The permit_count of this AccessTopVO.
        :type permit_count: int
        """
        self._permit_count = permit_count

    @property
    def permit_top_one_acl_id(self):
        r"""Gets the permit_top_one_acl_id of this AccessTopVO.

        **参数解释**： 高频命中的放行策略ID **取值范围**： 不涉及

        :return: The permit_top_one_acl_id of this AccessTopVO.
        :rtype: str
        """
        return self._permit_top_one_acl_id

    @permit_top_one_acl_id.setter
    def permit_top_one_acl_id(self, permit_top_one_acl_id):
        r"""Sets the permit_top_one_acl_id of this AccessTopVO.

        **参数解释**： 高频命中的放行策略ID **取值范围**： 不涉及

        :param permit_top_one_acl_id: The permit_top_one_acl_id of this AccessTopVO.
        :type permit_top_one_acl_id: str
        """
        self._permit_top_one_acl_id = permit_top_one_acl_id

    @property
    def permit_top_one_acl_name(self):
        r"""Gets the permit_top_one_acl_name of this AccessTopVO.

        **参数解释**： 高频命中的放行策略名称 **取值范围**： 不涉及

        :return: The permit_top_one_acl_name of this AccessTopVO.
        :rtype: str
        """
        return self._permit_top_one_acl_name

    @permit_top_one_acl_name.setter
    def permit_top_one_acl_name(self, permit_top_one_acl_name):
        r"""Sets the permit_top_one_acl_name of this AccessTopVO.

        **参数解释**： 高频命中的放行策略名称 **取值范围**： 不涉及

        :param permit_top_one_acl_name: The permit_top_one_acl_name of this AccessTopVO.
        :type permit_top_one_acl_name: str
        """
        self._permit_top_one_acl_name = permit_top_one_acl_name

    @property
    def records(self):
        r"""Gets the records of this AccessTopVO.

        **参数解释**： 命中趋势 **取值范围**： 不涉及

        :return: The records of this AccessTopVO.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.AccessTopStatisticsVO`]
        """
        return self._records

    @records.setter
    def records(self, records):
        r"""Sets the records of this AccessTopVO.

        **参数解释**： 命中趋势 **取值范围**： 不涉及

        :param records: The records of this AccessTopVO.
        :type records: list[:class:`huaweicloudsdkcfw.v1.AccessTopStatisticsVO`]
        """
        self._records = records

    @property
    def top_deny_rule_list(self):
        r"""Gets the top_deny_rule_list of this AccessTopVO.

        **参数解释**： TOP阻断规则列表 **取值范围**： 不涉及

        :return: The top_deny_rule_list of this AccessTopVO.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.AccessTopMemberVO`]
        """
        return self._top_deny_rule_list

    @top_deny_rule_list.setter
    def top_deny_rule_list(self, top_deny_rule_list):
        r"""Sets the top_deny_rule_list of this AccessTopVO.

        **参数解释**： TOP阻断规则列表 **取值范围**： 不涉及

        :param top_deny_rule_list: The top_deny_rule_list of this AccessTopVO.
        :type top_deny_rule_list: list[:class:`huaweicloudsdkcfw.v1.AccessTopMemberVO`]
        """
        self._top_deny_rule_list = top_deny_rule_list

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
        if not isinstance(other, AccessTopVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
