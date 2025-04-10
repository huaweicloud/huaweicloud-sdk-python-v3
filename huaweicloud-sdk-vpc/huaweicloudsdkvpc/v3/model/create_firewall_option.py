# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateFirewallOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'description': 'str',
        'enterprise_project_id': 'str',
        'tags': 'list[ResourceTag]',
        'admin_state_up': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'enterprise_project_id': 'enterprise_project_id',
        'tags': 'tags',
        'admin_state_up': 'admin_state_up'
    }

    def __init__(self, name=None, description=None, enterprise_project_id=None, tags=None, admin_state_up=None):
        r"""CreateFirewallOption

        The model defined in huaweicloud sdk

        :param name: 功能说明：ACL名称 取值范围：0-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）
        :type name: str
        :param description: 功能说明：ACL描述信息 取值范围：0-255个字符 约束：不能包含“&lt;”和“&gt;”。
        :type description: str
        :param enterprise_project_id: 功能说明：ACL企业项目ID。 取值范围：最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。“0”表示默认企业项目。
        :type enterprise_project_id: str
        :param tags: 功能描述：ACL资源标签
        :type tags: list[:class:`huaweicloudsdkvpc.v3.ResourceTag`]
        :param admin_state_up: 功能说明：ACL是否开启，默认值true 取值范围：true表示ACL开启；false表示ACL关闭
        :type admin_state_up: bool
        """
        
        

        self._name = None
        self._description = None
        self._enterprise_project_id = None
        self._tags = None
        self._admin_state_up = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if tags is not None:
            self.tags = tags
        if admin_state_up is not None:
            self.admin_state_up = admin_state_up

    @property
    def name(self):
        r"""Gets the name of this CreateFirewallOption.

        功能说明：ACL名称 取值范围：0-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）

        :return: The name of this CreateFirewallOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateFirewallOption.

        功能说明：ACL名称 取值范围：0-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）

        :param name: The name of this CreateFirewallOption.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this CreateFirewallOption.

        功能说明：ACL描述信息 取值范围：0-255个字符 约束：不能包含“<”和“>”。

        :return: The description of this CreateFirewallOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateFirewallOption.

        功能说明：ACL描述信息 取值范围：0-255个字符 约束：不能包含“<”和“>”。

        :param description: The description of this CreateFirewallOption.
        :type description: str
        """
        self._description = description

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this CreateFirewallOption.

        功能说明：ACL企业项目ID。 取值范围：最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。“0”表示默认企业项目。

        :return: The enterprise_project_id of this CreateFirewallOption.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this CreateFirewallOption.

        功能说明：ACL企业项目ID。 取值范围：最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。“0”表示默认企业项目。

        :param enterprise_project_id: The enterprise_project_id of this CreateFirewallOption.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def tags(self):
        r"""Gets the tags of this CreateFirewallOption.

        功能描述：ACL资源标签

        :return: The tags of this CreateFirewallOption.
        :rtype: list[:class:`huaweicloudsdkvpc.v3.ResourceTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this CreateFirewallOption.

        功能描述：ACL资源标签

        :param tags: The tags of this CreateFirewallOption.
        :type tags: list[:class:`huaweicloudsdkvpc.v3.ResourceTag`]
        """
        self._tags = tags

    @property
    def admin_state_up(self):
        r"""Gets the admin_state_up of this CreateFirewallOption.

        功能说明：ACL是否开启，默认值true 取值范围：true表示ACL开启；false表示ACL关闭

        :return: The admin_state_up of this CreateFirewallOption.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        r"""Sets the admin_state_up of this CreateFirewallOption.

        功能说明：ACL是否开启，默认值true 取值范围：true表示ACL开启；false表示ACL关闭

        :param admin_state_up: The admin_state_up of this CreateFirewallOption.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

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
        if not isinstance(other, CreateFirewallOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
