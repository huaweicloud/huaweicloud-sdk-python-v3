# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodeLifecycleConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'pre_install': 'str',
        'post_install': 'str',
        'wait_post_install_finish': 'bool'
    }

    attribute_map = {
        'pre_install': 'preInstall',
        'post_install': 'postInstall',
        'wait_post_install_finish': 'waitPostInstallFinish'
    }

    def __init__(self, pre_install=None, post_install=None, wait_post_install_finish=None):
        r"""NodeLifecycleConfig

        The model defined in huaweicloud sdk

        :param pre_install: **参数解释**： 安装前执行脚本。 **约束限制**： 安装前/后执行脚本统一计算字符，转码后的字符总数不能超过10240。 输入的值需要经过Base64编码，方法如下：   &#x60;&#x60;&#x60;   echo -n \&quot;待编码内容\&quot; | base64   &#x60;&#x60;&#x60; **取值范围**： 不涉及 **默认取值**： 不涉及
        :type pre_install: str
        :param post_install: **参数解释**： 安装前执行脚本。 **约束限制**： 安装前/后执行脚本统一计算字符，转码后的字符总数不能超过10240。 输入的值需要经过Base64编码，方法如下：   &#x60;&#x60;&#x60;   echo -n \&quot;待编码内容\&quot; | base64   &#x60;&#x60;&#x60; **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type post_install: str
        :param wait_post_install_finish: **参数解释：** 该参数用于控制重置/纳管/批量重置节点时， **post-install脚本执行完成前允许节点调度** 的行为。当操作的节点属于节点池时，以节点池相关配置为准。当该参数未设置或者为false时，在kubernetes节点就绪时，容器即可被调度到可用节点。当该参数为true时，在kubernetes节点就绪时且post-install脚本执行完成时，容器才可被调度到可用节点。  **约束限制：** 不涉及  **取值范围：** - false：在kubernetes节点就绪时，容器即可被调度到可用节点。           - true：在kubernetes节点就绪时且post-install脚本执行完成时，容器才可被调度到可用节点。  **默认取值：** false
        :type wait_post_install_finish: bool
        """
        
        

        self._pre_install = None
        self._post_install = None
        self._wait_post_install_finish = None
        self.discriminator = None

        if pre_install is not None:
            self.pre_install = pre_install
        if post_install is not None:
            self.post_install = post_install
        if wait_post_install_finish is not None:
            self.wait_post_install_finish = wait_post_install_finish

    @property
    def pre_install(self):
        r"""Gets the pre_install of this NodeLifecycleConfig.

        **参数解释**： 安装前执行脚本。 **约束限制**： 安装前/后执行脚本统一计算字符，转码后的字符总数不能超过10240。 输入的值需要经过Base64编码，方法如下：   ```   echo -n \"待编码内容\" | base64   ``` **取值范围**： 不涉及 **默认取值**： 不涉及

        :return: The pre_install of this NodeLifecycleConfig.
        :rtype: str
        """
        return self._pre_install

    @pre_install.setter
    def pre_install(self, pre_install):
        r"""Sets the pre_install of this NodeLifecycleConfig.

        **参数解释**： 安装前执行脚本。 **约束限制**： 安装前/后执行脚本统一计算字符，转码后的字符总数不能超过10240。 输入的值需要经过Base64编码，方法如下：   ```   echo -n \"待编码内容\" | base64   ``` **取值范围**： 不涉及 **默认取值**： 不涉及

        :param pre_install: The pre_install of this NodeLifecycleConfig.
        :type pre_install: str
        """
        self._pre_install = pre_install

    @property
    def post_install(self):
        r"""Gets the post_install of this NodeLifecycleConfig.

        **参数解释**： 安装前执行脚本。 **约束限制**： 安装前/后执行脚本统一计算字符，转码后的字符总数不能超过10240。 输入的值需要经过Base64编码，方法如下：   ```   echo -n \"待编码内容\" | base64   ``` **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The post_install of this NodeLifecycleConfig.
        :rtype: str
        """
        return self._post_install

    @post_install.setter
    def post_install(self, post_install):
        r"""Sets the post_install of this NodeLifecycleConfig.

        **参数解释**： 安装前执行脚本。 **约束限制**： 安装前/后执行脚本统一计算字符，转码后的字符总数不能超过10240。 输入的值需要经过Base64编码，方法如下：   ```   echo -n \"待编码内容\" | base64   ``` **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param post_install: The post_install of this NodeLifecycleConfig.
        :type post_install: str
        """
        self._post_install = post_install

    @property
    def wait_post_install_finish(self):
        r"""Gets the wait_post_install_finish of this NodeLifecycleConfig.

        **参数解释：** 该参数用于控制重置/纳管/批量重置节点时， **post-install脚本执行完成前允许节点调度** 的行为。当操作的节点属于节点池时，以节点池相关配置为准。当该参数未设置或者为false时，在kubernetes节点就绪时，容器即可被调度到可用节点。当该参数为true时，在kubernetes节点就绪时且post-install脚本执行完成时，容器才可被调度到可用节点。  **约束限制：** 不涉及  **取值范围：** - false：在kubernetes节点就绪时，容器即可被调度到可用节点。           - true：在kubernetes节点就绪时且post-install脚本执行完成时，容器才可被调度到可用节点。  **默认取值：** false

        :return: The wait_post_install_finish of this NodeLifecycleConfig.
        :rtype: bool
        """
        return self._wait_post_install_finish

    @wait_post_install_finish.setter
    def wait_post_install_finish(self, wait_post_install_finish):
        r"""Sets the wait_post_install_finish of this NodeLifecycleConfig.

        **参数解释：** 该参数用于控制重置/纳管/批量重置节点时， **post-install脚本执行完成前允许节点调度** 的行为。当操作的节点属于节点池时，以节点池相关配置为准。当该参数未设置或者为false时，在kubernetes节点就绪时，容器即可被调度到可用节点。当该参数为true时，在kubernetes节点就绪时且post-install脚本执行完成时，容器才可被调度到可用节点。  **约束限制：** 不涉及  **取值范围：** - false：在kubernetes节点就绪时，容器即可被调度到可用节点。           - true：在kubernetes节点就绪时且post-install脚本执行完成时，容器才可被调度到可用节点。  **默认取值：** false

        :param wait_post_install_finish: The wait_post_install_finish of this NodeLifecycleConfig.
        :type wait_post_install_finish: bool
        """
        self._wait_post_install_finish = wait_post_install_finish

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
        if not isinstance(other, NodeLifecycleConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
