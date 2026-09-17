# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InPlaceMigrateNodeExtendParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'alpha_cce_pre_install': 'str',
        'alpha_cce_post_install': 'str',
        'wait_post_install_finish': 'bool'
    }

    attribute_map = {
        'alpha_cce_pre_install': 'alpha.cce/preInstall',
        'alpha_cce_post_install': 'alpha.cce/postInstall',
        'wait_post_install_finish': 'waitPostInstallFinish'
    }

    def __init__(self, alpha_cce_pre_install=None, alpha_cce_post_install=None, wait_post_install_finish=None):
        r"""InPlaceMigrateNodeExtendParam

        The model defined in huaweicloud sdk

        :param alpha_cce_pre_install: **参数解释**： 安装前执行脚本。 **约束限制**： 安装前/后执行脚本统一计算字符，转码后的字符总数不能超过10240。 输入的值需要经过Base64编码，方法如下：   &#x60;&#x60;&#x60;   echo -n \&quot;待编码内容\&quot; | base64   &#x60;&#x60;&#x60;  **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type alpha_cce_pre_install: str
        :param alpha_cce_post_install: **参数解释**： 安装后执行脚本。 **约束限制**： 安装前/后执行脚本统一计算字符，转码后的字符总数不能超过10240。 输入的值需要经过Base64编码，方法如下：   &#x60;&#x60;&#x60;   echo -n \&quot;待编码内容\&quot; | base64   &#x60;&#x60;&#x60;  **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type alpha_cce_post_install: str
        :param wait_post_install_finish: **参数解释：** 该参数用于控制腾挪节点时， **post-install脚本执行完成前允许节点调度** 的行为。当该参数未设置或者为false时，在kubernetes节点就绪时，容器即可被调度到可用节点。当该参数为true时，在kubernetes节点就绪时且post-install脚本执行完成时，容器才可被调度到可用节点。 **约束限制：** 不涉及 **取值范围：** - false：在kubernetes节点就绪时，容器即可被调度到可用节点。           - true：在kubernetes节点就绪时且post-install脚本执行完成时，容器才可被调度到可用节点。  **默认取值：** false
        :type wait_post_install_finish: bool
        """
        
        

        self._alpha_cce_pre_install = None
        self._alpha_cce_post_install = None
        self._wait_post_install_finish = None
        self.discriminator = None

        if alpha_cce_pre_install is not None:
            self.alpha_cce_pre_install = alpha_cce_pre_install
        if alpha_cce_post_install is not None:
            self.alpha_cce_post_install = alpha_cce_post_install
        if wait_post_install_finish is not None:
            self.wait_post_install_finish = wait_post_install_finish

    @property
    def alpha_cce_pre_install(self):
        r"""Gets the alpha_cce_pre_install of this InPlaceMigrateNodeExtendParam.

        **参数解释**： 安装前执行脚本。 **约束限制**： 安装前/后执行脚本统一计算字符，转码后的字符总数不能超过10240。 输入的值需要经过Base64编码，方法如下：   ```   echo -n \"待编码内容\" | base64   ```  **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The alpha_cce_pre_install of this InPlaceMigrateNodeExtendParam.
        :rtype: str
        """
        return self._alpha_cce_pre_install

    @alpha_cce_pre_install.setter
    def alpha_cce_pre_install(self, alpha_cce_pre_install):
        r"""Sets the alpha_cce_pre_install of this InPlaceMigrateNodeExtendParam.

        **参数解释**： 安装前执行脚本。 **约束限制**： 安装前/后执行脚本统一计算字符，转码后的字符总数不能超过10240。 输入的值需要经过Base64编码，方法如下：   ```   echo -n \"待编码内容\" | base64   ```  **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param alpha_cce_pre_install: The alpha_cce_pre_install of this InPlaceMigrateNodeExtendParam.
        :type alpha_cce_pre_install: str
        """
        self._alpha_cce_pre_install = alpha_cce_pre_install

    @property
    def alpha_cce_post_install(self):
        r"""Gets the alpha_cce_post_install of this InPlaceMigrateNodeExtendParam.

        **参数解释**： 安装后执行脚本。 **约束限制**： 安装前/后执行脚本统一计算字符，转码后的字符总数不能超过10240。 输入的值需要经过Base64编码，方法如下：   ```   echo -n \"待编码内容\" | base64   ```  **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The alpha_cce_post_install of this InPlaceMigrateNodeExtendParam.
        :rtype: str
        """
        return self._alpha_cce_post_install

    @alpha_cce_post_install.setter
    def alpha_cce_post_install(self, alpha_cce_post_install):
        r"""Sets the alpha_cce_post_install of this InPlaceMigrateNodeExtendParam.

        **参数解释**： 安装后执行脚本。 **约束限制**： 安装前/后执行脚本统一计算字符，转码后的字符总数不能超过10240。 输入的值需要经过Base64编码，方法如下：   ```   echo -n \"待编码内容\" | base64   ```  **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param alpha_cce_post_install: The alpha_cce_post_install of this InPlaceMigrateNodeExtendParam.
        :type alpha_cce_post_install: str
        """
        self._alpha_cce_post_install = alpha_cce_post_install

    @property
    def wait_post_install_finish(self):
        r"""Gets the wait_post_install_finish of this InPlaceMigrateNodeExtendParam.

        **参数解释：** 该参数用于控制腾挪节点时， **post-install脚本执行完成前允许节点调度** 的行为。当该参数未设置或者为false时，在kubernetes节点就绪时，容器即可被调度到可用节点。当该参数为true时，在kubernetes节点就绪时且post-install脚本执行完成时，容器才可被调度到可用节点。 **约束限制：** 不涉及 **取值范围：** - false：在kubernetes节点就绪时，容器即可被调度到可用节点。           - true：在kubernetes节点就绪时且post-install脚本执行完成时，容器才可被调度到可用节点。  **默认取值：** false

        :return: The wait_post_install_finish of this InPlaceMigrateNodeExtendParam.
        :rtype: bool
        """
        return self._wait_post_install_finish

    @wait_post_install_finish.setter
    def wait_post_install_finish(self, wait_post_install_finish):
        r"""Sets the wait_post_install_finish of this InPlaceMigrateNodeExtendParam.

        **参数解释：** 该参数用于控制腾挪节点时， **post-install脚本执行完成前允许节点调度** 的行为。当该参数未设置或者为false时，在kubernetes节点就绪时，容器即可被调度到可用节点。当该参数为true时，在kubernetes节点就绪时且post-install脚本执行完成时，容器才可被调度到可用节点。 **约束限制：** 不涉及 **取值范围：** - false：在kubernetes节点就绪时，容器即可被调度到可用节点。           - true：在kubernetes节点就绪时且post-install脚本执行完成时，容器才可被调度到可用节点。  **默认取值：** false

        :param wait_post_install_finish: The wait_post_install_finish of this InPlaceMigrateNodeExtendParam.
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
        if not isinstance(other, InPlaceMigrateNodeExtendParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
