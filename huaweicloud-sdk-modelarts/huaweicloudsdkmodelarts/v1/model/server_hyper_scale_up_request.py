# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ServerHyperScaleUpRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'flavor': 'str',
        'root_volume': 'EvsVolume',
        'data_volume': 'ServerDataVolume',
        'image_id': 'str',
        'userdata': 'str',
        'key_pair_name': 'str'
    }

    attribute_map = {
        'flavor': 'flavor',
        'root_volume': 'root_volume',
        'data_volume': 'data_volume',
        'image_id': 'image_id',
        'userdata': 'userdata',
        'key_pair_name': 'key_pair_name'
    }

    def __init__(self, flavor=None, root_volume=None, data_volume=None, image_id=None, userdata=None, key_pair_name=None):
        r"""ServerHyperScaleUpRequest

        The model defined in huaweicloud sdk

        :param flavor: **参数解释**：服务器规格名称。 **约束限制**：不涉及。 **取值范围**：长度为1至128个字符，只能包含字母和数字及点。 **默认取值**：不涉及。
        :type flavor: str
        :param root_volume: 
        :type root_volume: :class:`huaweicloudsdkmodelarts.v1.EvsVolume`
        :param data_volume: 
        :type data_volume: :class:`huaweicloudsdkmodelarts.v1.ServerDataVolume`
        :param image_id: **参数解释**：服务器镜像ID。 **约束限制**：不涉及。 **取值范围**：长度为36个字符，符合UUID格式。 **默认取值**：不涉及。
        :type image_id: str
        :param userdata: **参数解释**： 创建云服务器过程中待注入实例自定义数据。支持注入文本、文本文件。 示例： base64编码前： * Linux服务器： &#x60;&#x60;&#x60;bash #!/bin/bash echo user_test &gt; /home/user.txt &#x60;&#x60;&#x60; base64编码后： * Linux服务器： &#x60;&#x60;&#x60;bash IyEvYmluL2Jhc2gKZWNobyB1c2VyX3Rlc3QgPiAvaG9tZS91c2VyLnR4dA&#x3D;&#x3D; &#x60;&#x60;&#x60; 了解更多实例自定义数据注入请参考[[用户数据注入](https://support.huaweicloud.com/usermanual-ecs/zh-cn_topic_0032380449.html)](tag:hc)[[用户数据注入](https://support.huaweicloud.com/intl/zh-cn/usermanual-ecs/zh-cn_topic_0032380449.html)][ECS服务“通过实例自定义数据配置ECS实例”章节](tag:fcs,hcso)。 用户需明确user_data的使用效果，可能产生的影响和风险由用户自行承担。 **约束限制**： - user_data的值为base64编码之后的内容。 - 注入内容（编码之前的内容）最大长度为32K。  **取值范围**：不涉及。 **默认取值**：不涉及。
        :type userdata: str
        :param key_pair_name: **参数解释**：服务器登录密钥对名称。admin_pass和key_pair_name必须二选一。注意超节点扩容仅支持使用密钥对创建。 **约束限制**：admin_pass和key_pair_name不能同时存在。 **取值范围**：长度为1至64个字符，只能包含字母、数字、中划线、下划线和点。 **默认取值**：不涉及。
        :type key_pair_name: str
        """
        
        

        self._flavor = None
        self._root_volume = None
        self._data_volume = None
        self._image_id = None
        self._userdata = None
        self._key_pair_name = None
        self.discriminator = None

        self.flavor = flavor
        if root_volume is not None:
            self.root_volume = root_volume
        if data_volume is not None:
            self.data_volume = data_volume
        self.image_id = image_id
        if userdata is not None:
            self.userdata = userdata
        if key_pair_name is not None:
            self.key_pair_name = key_pair_name

    @property
    def flavor(self):
        r"""Gets the flavor of this ServerHyperScaleUpRequest.

        **参数解释**：服务器规格名称。 **约束限制**：不涉及。 **取值范围**：长度为1至128个字符，只能包含字母和数字及点。 **默认取值**：不涉及。

        :return: The flavor of this ServerHyperScaleUpRequest.
        :rtype: str
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        r"""Sets the flavor of this ServerHyperScaleUpRequest.

        **参数解释**：服务器规格名称。 **约束限制**：不涉及。 **取值范围**：长度为1至128个字符，只能包含字母和数字及点。 **默认取值**：不涉及。

        :param flavor: The flavor of this ServerHyperScaleUpRequest.
        :type flavor: str
        """
        self._flavor = flavor

    @property
    def root_volume(self):
        r"""Gets the root_volume of this ServerHyperScaleUpRequest.

        :return: The root_volume of this ServerHyperScaleUpRequest.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.EvsVolume`
        """
        return self._root_volume

    @root_volume.setter
    def root_volume(self, root_volume):
        r"""Sets the root_volume of this ServerHyperScaleUpRequest.

        :param root_volume: The root_volume of this ServerHyperScaleUpRequest.
        :type root_volume: :class:`huaweicloudsdkmodelarts.v1.EvsVolume`
        """
        self._root_volume = root_volume

    @property
    def data_volume(self):
        r"""Gets the data_volume of this ServerHyperScaleUpRequest.

        :return: The data_volume of this ServerHyperScaleUpRequest.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ServerDataVolume`
        """
        return self._data_volume

    @data_volume.setter
    def data_volume(self, data_volume):
        r"""Sets the data_volume of this ServerHyperScaleUpRequest.

        :param data_volume: The data_volume of this ServerHyperScaleUpRequest.
        :type data_volume: :class:`huaweicloudsdkmodelarts.v1.ServerDataVolume`
        """
        self._data_volume = data_volume

    @property
    def image_id(self):
        r"""Gets the image_id of this ServerHyperScaleUpRequest.

        **参数解释**：服务器镜像ID。 **约束限制**：不涉及。 **取值范围**：长度为36个字符，符合UUID格式。 **默认取值**：不涉及。

        :return: The image_id of this ServerHyperScaleUpRequest.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this ServerHyperScaleUpRequest.

        **参数解释**：服务器镜像ID。 **约束限制**：不涉及。 **取值范围**：长度为36个字符，符合UUID格式。 **默认取值**：不涉及。

        :param image_id: The image_id of this ServerHyperScaleUpRequest.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def userdata(self):
        r"""Gets the userdata of this ServerHyperScaleUpRequest.

        **参数解释**： 创建云服务器过程中待注入实例自定义数据。支持注入文本、文本文件。 示例： base64编码前： * Linux服务器： ```bash #!/bin/bash echo user_test > /home/user.txt ``` base64编码后： * Linux服务器： ```bash IyEvYmluL2Jhc2gKZWNobyB1c2VyX3Rlc3QgPiAvaG9tZS91c2VyLnR4dA== ``` 了解更多实例自定义数据注入请参考[[用户数据注入](https://support.huaweicloud.com/usermanual-ecs/zh-cn_topic_0032380449.html)](tag:hc)[[用户数据注入](https://support.huaweicloud.com/intl/zh-cn/usermanual-ecs/zh-cn_topic_0032380449.html)][ECS服务“通过实例自定义数据配置ECS实例”章节](tag:fcs,hcso)。 用户需明确user_data的使用效果，可能产生的影响和风险由用户自行承担。 **约束限制**： - user_data的值为base64编码之后的内容。 - 注入内容（编码之前的内容）最大长度为32K。  **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The userdata of this ServerHyperScaleUpRequest.
        :rtype: str
        """
        return self._userdata

    @userdata.setter
    def userdata(self, userdata):
        r"""Sets the userdata of this ServerHyperScaleUpRequest.

        **参数解释**： 创建云服务器过程中待注入实例自定义数据。支持注入文本、文本文件。 示例： base64编码前： * Linux服务器： ```bash #!/bin/bash echo user_test > /home/user.txt ``` base64编码后： * Linux服务器： ```bash IyEvYmluL2Jhc2gKZWNobyB1c2VyX3Rlc3QgPiAvaG9tZS91c2VyLnR4dA== ``` 了解更多实例自定义数据注入请参考[[用户数据注入](https://support.huaweicloud.com/usermanual-ecs/zh-cn_topic_0032380449.html)](tag:hc)[[用户数据注入](https://support.huaweicloud.com/intl/zh-cn/usermanual-ecs/zh-cn_topic_0032380449.html)][ECS服务“通过实例自定义数据配置ECS实例”章节](tag:fcs,hcso)。 用户需明确user_data的使用效果，可能产生的影响和风险由用户自行承担。 **约束限制**： - user_data的值为base64编码之后的内容。 - 注入内容（编码之前的内容）最大长度为32K。  **取值范围**：不涉及。 **默认取值**：不涉及。

        :param userdata: The userdata of this ServerHyperScaleUpRequest.
        :type userdata: str
        """
        self._userdata = userdata

    @property
    def key_pair_name(self):
        r"""Gets the key_pair_name of this ServerHyperScaleUpRequest.

        **参数解释**：服务器登录密钥对名称。admin_pass和key_pair_name必须二选一。注意超节点扩容仅支持使用密钥对创建。 **约束限制**：admin_pass和key_pair_name不能同时存在。 **取值范围**：长度为1至64个字符，只能包含字母、数字、中划线、下划线和点。 **默认取值**：不涉及。

        :return: The key_pair_name of this ServerHyperScaleUpRequest.
        :rtype: str
        """
        return self._key_pair_name

    @key_pair_name.setter
    def key_pair_name(self, key_pair_name):
        r"""Sets the key_pair_name of this ServerHyperScaleUpRequest.

        **参数解释**：服务器登录密钥对名称。admin_pass和key_pair_name必须二选一。注意超节点扩容仅支持使用密钥对创建。 **约束限制**：admin_pass和key_pair_name不能同时存在。 **取值范围**：长度为1至64个字符，只能包含字母、数字、中划线、下划线和点。 **默认取值**：不涉及。

        :param key_pair_name: The key_pair_name of this ServerHyperScaleUpRequest.
        :type key_pair_name: str
        """
        self._key_pair_name = key_pair_name

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
        if not isinstance(other, ServerHyperScaleUpRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
