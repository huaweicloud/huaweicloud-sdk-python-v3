# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListOrganizationAccountsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'fw_instance_id': 'str',
        'parent_id': 'str',
        'limit': 'int',
        'marker': 'str'
    }

    attribute_map = {
        'fw_instance_id': 'fw_instance_id',
        'parent_id': 'parent_id',
        'limit': 'limit',
        'marker': 'marker'
    }

    def __init__(self, fw_instance_id=None, parent_id=None, limit=None, marker=None):
        r"""ListOrganizationAccountsRequest

        The model defined in huaweicloud sdk

        :param fw_instance_id: **参数解释**： 防火墙ID，用户创建防火墙实例后产生的唯一ID，配置后可区分不同防火墙，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取 **约束限制**： 不涉及 **取值范围**： 32位UUID **默认取值**： 不涉及
        :type fw_instance_id: str
        :param parent_id: **参数解释**： 父节点（根或组织单元）的唯一标识符（ID） **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及
        :type parent_id: str
        :param limit: **参数解释**： 查询返回记录的数量限制 **约束限制**： 不涉及 **取值范围**： 1-2000 **默认取值**： 2000
        :type limit: int
        :param marker: **参数解释**： 分页标记 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及
        :type marker: str
        """
        
        

        self._fw_instance_id = None
        self._parent_id = None
        self._limit = None
        self._marker = None
        self.discriminator = None

        self.fw_instance_id = fw_instance_id
        if parent_id is not None:
            self.parent_id = parent_id
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker

    @property
    def fw_instance_id(self):
        r"""Gets the fw_instance_id of this ListOrganizationAccountsRequest.

        **参数解释**： 防火墙ID，用户创建防火墙实例后产生的唯一ID，配置后可区分不同防火墙，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取 **约束限制**： 不涉及 **取值范围**： 32位UUID **默认取值**： 不涉及

        :return: The fw_instance_id of this ListOrganizationAccountsRequest.
        :rtype: str
        """
        return self._fw_instance_id

    @fw_instance_id.setter
    def fw_instance_id(self, fw_instance_id):
        r"""Sets the fw_instance_id of this ListOrganizationAccountsRequest.

        **参数解释**： 防火墙ID，用户创建防火墙实例后产生的唯一ID，配置后可区分不同防火墙，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取 **约束限制**： 不涉及 **取值范围**： 32位UUID **默认取值**： 不涉及

        :param fw_instance_id: The fw_instance_id of this ListOrganizationAccountsRequest.
        :type fw_instance_id: str
        """
        self._fw_instance_id = fw_instance_id

    @property
    def parent_id(self):
        r"""Gets the parent_id of this ListOrganizationAccountsRequest.

        **参数解释**： 父节点（根或组织单元）的唯一标识符（ID） **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :return: The parent_id of this ListOrganizationAccountsRequest.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        r"""Sets the parent_id of this ListOrganizationAccountsRequest.

        **参数解释**： 父节点（根或组织单元）的唯一标识符（ID） **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :param parent_id: The parent_id of this ListOrganizationAccountsRequest.
        :type parent_id: str
        """
        self._parent_id = parent_id

    @property
    def limit(self):
        r"""Gets the limit of this ListOrganizationAccountsRequest.

        **参数解释**： 查询返回记录的数量限制 **约束限制**： 不涉及 **取值范围**： 1-2000 **默认取值**： 2000

        :return: The limit of this ListOrganizationAccountsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListOrganizationAccountsRequest.

        **参数解释**： 查询返回记录的数量限制 **约束限制**： 不涉及 **取值范围**： 1-2000 **默认取值**： 2000

        :param limit: The limit of this ListOrganizationAccountsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListOrganizationAccountsRequest.

        **参数解释**： 分页标记 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :return: The marker of this ListOrganizationAccountsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListOrganizationAccountsRequest.

        **参数解释**： 分页标记 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :param marker: The marker of this ListOrganizationAccountsRequest.
        :type marker: str
        """
        self._marker = marker

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
        if not isinstance(other, ListOrganizationAccountsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
