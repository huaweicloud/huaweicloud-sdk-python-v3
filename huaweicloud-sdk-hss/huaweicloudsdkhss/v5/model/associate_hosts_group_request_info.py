# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AssociateHostsGroupRequestInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_id': 'str',
        'host_id_list': 'list[str]',
        'operate_all': 'bool'
    }

    attribute_map = {
        'group_id': 'group_id',
        'host_id_list': 'host_id_list',
        'operate_all': 'operate_all'
    }

    def __init__(self, group_id=None, host_id_list=None, operate_all=None):
        r"""AssociateHostsGroupRequestInfo

        The model defined in huaweicloud sdk

        :param group_id: **参数解释**: 服务器组ID **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 
        :type group_id: str
        :param host_id_list: **参数解释**： 服务器ID列表 **约束限制**： 不涉及 **取值范围**： 列表长度1-200条 **默认取值**： 不涉及 
        :type host_id_list: list[str]
        :param operate_all: **参数解释**: 是否要对全量主机分配到组，如果为true的话，将所有主机分配到组，不需填写host_id_list，如果为false的话，需要填写host_id_list **约束限制**: 不涉及 **取值范围**: - true: 将所有主机分配到组，不需填写host_id_list。 - false: 非全量分配到组，仅对指定的主机列表分配到组，需要填写host_id_list。 **默认取值**: 不涉及 
        :type operate_all: bool
        """
        
        

        self._group_id = None
        self._host_id_list = None
        self._operate_all = None
        self.discriminator = None

        self.group_id = group_id
        if host_id_list is not None:
            self.host_id_list = host_id_list
        self.operate_all = operate_all

    @property
    def group_id(self):
        r"""Gets the group_id of this AssociateHostsGroupRequestInfo.

        **参数解释**: 服务器组ID **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 

        :return: The group_id of this AssociateHostsGroupRequestInfo.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this AssociateHostsGroupRequestInfo.

        **参数解释**: 服务器组ID **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 

        :param group_id: The group_id of this AssociateHostsGroupRequestInfo.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def host_id_list(self):
        r"""Gets the host_id_list of this AssociateHostsGroupRequestInfo.

        **参数解释**： 服务器ID列表 **约束限制**： 不涉及 **取值范围**： 列表长度1-200条 **默认取值**： 不涉及 

        :return: The host_id_list of this AssociateHostsGroupRequestInfo.
        :rtype: list[str]
        """
        return self._host_id_list

    @host_id_list.setter
    def host_id_list(self, host_id_list):
        r"""Sets the host_id_list of this AssociateHostsGroupRequestInfo.

        **参数解释**： 服务器ID列表 **约束限制**： 不涉及 **取值范围**： 列表长度1-200条 **默认取值**： 不涉及 

        :param host_id_list: The host_id_list of this AssociateHostsGroupRequestInfo.
        :type host_id_list: list[str]
        """
        self._host_id_list = host_id_list

    @property
    def operate_all(self):
        r"""Gets the operate_all of this AssociateHostsGroupRequestInfo.

        **参数解释**: 是否要对全量主机分配到组，如果为true的话，将所有主机分配到组，不需填写host_id_list，如果为false的话，需要填写host_id_list **约束限制**: 不涉及 **取值范围**: - true: 将所有主机分配到组，不需填写host_id_list。 - false: 非全量分配到组，仅对指定的主机列表分配到组，需要填写host_id_list。 **默认取值**: 不涉及 

        :return: The operate_all of this AssociateHostsGroupRequestInfo.
        :rtype: bool
        """
        return self._operate_all

    @operate_all.setter
    def operate_all(self, operate_all):
        r"""Sets the operate_all of this AssociateHostsGroupRequestInfo.

        **参数解释**: 是否要对全量主机分配到组，如果为true的话，将所有主机分配到组，不需填写host_id_list，如果为false的话，需要填写host_id_list **约束限制**: 不涉及 **取值范围**: - true: 将所有主机分配到组，不需填写host_id_list。 - false: 非全量分配到组，仅对指定的主机列表分配到组，需要填写host_id_list。 **默认取值**: 不涉及 

        :param operate_all: The operate_all of this AssociateHostsGroupRequestInfo.
        :type operate_all: bool
        """
        self._operate_all = operate_all

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
        if not isinstance(other, AssociateHostsGroupRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
