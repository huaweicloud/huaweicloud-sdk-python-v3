# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ServerOsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'admin_pass': 'str',
        'key_pair_name': 'str',
        'image_id': 'str',
        'user_data': 'str'
    }

    attribute_map = {
        'admin_pass': 'admin_pass',
        'key_pair_name': 'key_pair_name',
        'image_id': 'image_id',
        'user_data': 'user_data'
    }

    def __init__(self, admin_pass=None, key_pair_name=None, image_id=None, user_data=None):
        r"""ServerOsRequest

        The model defined in huaweicloud sdk

        :param admin_pass: **参数解释**：用于登录服务器密码。注意弹性云服务器和裸金属服务器admin_pass和key_pair_name必须二选一，超节点不支持admin_pass。 **约束限制**：密码规则： - 长度为8至26个 - 至少包含大写字母、小写字母、数字及特殊符号(!@%-_&#x3D;+[{}]:,./?)中的3种 - 不能与用户名或倒序的用户名相同 - 不能包含root或administrator及其逆序 **取值范围**：不涉及 **默认取值**：不涉及
        :type admin_pass: str
        :param key_pair_name: **参数解释**：服务器登录密钥对名称。注意admin_pass和key_pair_name必须二选一。 **约束限制**：不涉及。 **取值范围**：不涉及 **默认取值**：不涉及
        :type key_pair_name: str
        :param image_id: **参数解释**：镜像ID，切换操作系统场景，该参数必填。 **约束限制**：不涉及。 **取值范围**：不涉及 **默认取值**：不涉及
        :type image_id: str
        :param user_data: **参数解释**： 创建云服务器过程中待注入实例自定义数据。支持注入文本、文本文件。 示例： base64编码前： * Linux服务器： &#x60;&#x60;&#x60;bash #!/bin/bash echo user_test &gt; /home/user.txt &#x60;&#x60;&#x60; base64编码后： * Linux服务器： &#x60;&#x60;&#x60;bash IyEvYmluL2Jhc2gKZWNobyB1c2VyX3Rlc3QgPiAvaG9tZS91c2VyLnR4dA&#x3D;&#x3D; &#x60;&#x60;&#x60; 了解更多实例自定义数据注入请参考[[用户数据注入](https://support.huaweicloud.com/usermanual-ecs/zh-cn_topic_0032380449.html)](tag:hc)[[用户数据注入](https://support.huaweicloud.com/intl/zh-cn/usermanual-ecs/zh-cn_topic_0032380449.html)][ECS服务“通过实例自定义数据配置ECS实例”章节](tag:fcs,hcso)。 用户需明确user_data的使用效果，可能产生的影响和风险由用户自行承担。 **约束限制**： - user_data的值为base64编码之后的内容。 - 注入内容（编码之前的内容）最大长度为32K。  **取值范围**：不涉及。 **默认取值**：不涉及。
        :type user_data: str
        """
        
        

        self._admin_pass = None
        self._key_pair_name = None
        self._image_id = None
        self._user_data = None
        self.discriminator = None

        if admin_pass is not None:
            self.admin_pass = admin_pass
        if key_pair_name is not None:
            self.key_pair_name = key_pair_name
        if image_id is not None:
            self.image_id = image_id
        if user_data is not None:
            self.user_data = user_data

    @property
    def admin_pass(self):
        r"""Gets the admin_pass of this ServerOsRequest.

        **参数解释**：用于登录服务器密码。注意弹性云服务器和裸金属服务器admin_pass和key_pair_name必须二选一，超节点不支持admin_pass。 **约束限制**：密码规则： - 长度为8至26个 - 至少包含大写字母、小写字母、数字及特殊符号(!@%-_=+[{}]:,./?)中的3种 - 不能与用户名或倒序的用户名相同 - 不能包含root或administrator及其逆序 **取值范围**：不涉及 **默认取值**：不涉及

        :return: The admin_pass of this ServerOsRequest.
        :rtype: str
        """
        return self._admin_pass

    @admin_pass.setter
    def admin_pass(self, admin_pass):
        r"""Sets the admin_pass of this ServerOsRequest.

        **参数解释**：用于登录服务器密码。注意弹性云服务器和裸金属服务器admin_pass和key_pair_name必须二选一，超节点不支持admin_pass。 **约束限制**：密码规则： - 长度为8至26个 - 至少包含大写字母、小写字母、数字及特殊符号(!@%-_=+[{}]:,./?)中的3种 - 不能与用户名或倒序的用户名相同 - 不能包含root或administrator及其逆序 **取值范围**：不涉及 **默认取值**：不涉及

        :param admin_pass: The admin_pass of this ServerOsRequest.
        :type admin_pass: str
        """
        self._admin_pass = admin_pass

    @property
    def key_pair_name(self):
        r"""Gets the key_pair_name of this ServerOsRequest.

        **参数解释**：服务器登录密钥对名称。注意admin_pass和key_pair_name必须二选一。 **约束限制**：不涉及。 **取值范围**：不涉及 **默认取值**：不涉及

        :return: The key_pair_name of this ServerOsRequest.
        :rtype: str
        """
        return self._key_pair_name

    @key_pair_name.setter
    def key_pair_name(self, key_pair_name):
        r"""Sets the key_pair_name of this ServerOsRequest.

        **参数解释**：服务器登录密钥对名称。注意admin_pass和key_pair_name必须二选一。 **约束限制**：不涉及。 **取值范围**：不涉及 **默认取值**：不涉及

        :param key_pair_name: The key_pair_name of this ServerOsRequest.
        :type key_pair_name: str
        """
        self._key_pair_name = key_pair_name

    @property
    def image_id(self):
        r"""Gets the image_id of this ServerOsRequest.

        **参数解释**：镜像ID，切换操作系统场景，该参数必填。 **约束限制**：不涉及。 **取值范围**：不涉及 **默认取值**：不涉及

        :return: The image_id of this ServerOsRequest.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this ServerOsRequest.

        **参数解释**：镜像ID，切换操作系统场景，该参数必填。 **约束限制**：不涉及。 **取值范围**：不涉及 **默认取值**：不涉及

        :param image_id: The image_id of this ServerOsRequest.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def user_data(self):
        r"""Gets the user_data of this ServerOsRequest.

        **参数解释**： 创建云服务器过程中待注入实例自定义数据。支持注入文本、文本文件。 示例： base64编码前： * Linux服务器： ```bash #!/bin/bash echo user_test > /home/user.txt ``` base64编码后： * Linux服务器： ```bash IyEvYmluL2Jhc2gKZWNobyB1c2VyX3Rlc3QgPiAvaG9tZS91c2VyLnR4dA== ``` 了解更多实例自定义数据注入请参考[[用户数据注入](https://support.huaweicloud.com/usermanual-ecs/zh-cn_topic_0032380449.html)](tag:hc)[[用户数据注入](https://support.huaweicloud.com/intl/zh-cn/usermanual-ecs/zh-cn_topic_0032380449.html)][ECS服务“通过实例自定义数据配置ECS实例”章节](tag:fcs,hcso)。 用户需明确user_data的使用效果，可能产生的影响和风险由用户自行承担。 **约束限制**： - user_data的值为base64编码之后的内容。 - 注入内容（编码之前的内容）最大长度为32K。  **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The user_data of this ServerOsRequest.
        :rtype: str
        """
        return self._user_data

    @user_data.setter
    def user_data(self, user_data):
        r"""Sets the user_data of this ServerOsRequest.

        **参数解释**： 创建云服务器过程中待注入实例自定义数据。支持注入文本、文本文件。 示例： base64编码前： * Linux服务器： ```bash #!/bin/bash echo user_test > /home/user.txt ``` base64编码后： * Linux服务器： ```bash IyEvYmluL2Jhc2gKZWNobyB1c2VyX3Rlc3QgPiAvaG9tZS91c2VyLnR4dA== ``` 了解更多实例自定义数据注入请参考[[用户数据注入](https://support.huaweicloud.com/usermanual-ecs/zh-cn_topic_0032380449.html)](tag:hc)[[用户数据注入](https://support.huaweicloud.com/intl/zh-cn/usermanual-ecs/zh-cn_topic_0032380449.html)][ECS服务“通过实例自定义数据配置ECS实例”章节](tag:fcs,hcso)。 用户需明确user_data的使用效果，可能产生的影响和风险由用户自行承担。 **约束限制**： - user_data的值为base64编码之后的内容。 - 注入内容（编码之前的内容）最大长度为32K。  **取值范围**：不涉及。 **默认取值**：不涉及。

        :param user_data: The user_data of this ServerOsRequest.
        :type user_data: str
        """
        self._user_data = user_data

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
        if not isinstance(other, ServerOsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
