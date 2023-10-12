# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateOrUpdateStoragePolicyStatementResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policy_statement_id': 'str',
        'actions': 'list[str]',
        'roam_actions': 'list[str]'
    }

    attribute_map = {
        'policy_statement_id': 'policy_statement_id',
        'actions': 'actions',
        'roam_actions': 'roam_actions'
    }

    def __init__(self, policy_statement_id=None, actions=None, roam_actions=None):
        """CreateOrUpdateStoragePolicyStatementResponse

        The model defined in huaweicloud sdk

        :param policy_statement_id: 支持的访问策略，内置如下四种策略: * &#x60;DEFAULT_1&#x60;：&#x60;客户端访问存储&#x60; - 上传、下载; &#x60;云端访问存储&#x60; - 读写   - action: PutObject、DeleteObject、GetObject   - roam_action: PutObject、DeleteObject、GetObject * &#x60;DEFAULT_2&#x60;：&#x60;客户端访问存储&#x60; - 下载; &#x60;云端访问存储&#x60; - 读写   - action: GetObject   - roam_action: PutObject、DeleteObject、GetObject * &#x60;DEFAULT_3&#x60;：&#x60;客户端访问存储&#x60; - 上传; &#x60;云端访问存储&#x60; - 读写   - action: PutObject、DeleteObject   - roam_action: PutObject、DeleteObject、GetObject * &#x60;DEFAULT_4&#x60;：&#x60;客户端访问存储&#x60; - 仅可查看列表,不允许上传下载; &#x60;云端访问存储&#x60; - 只读   - action:    - roam_action: GetObject
        :type policy_statement_id: str
        :param actions: 客户端访问存储可操作的权限合集 * &#x60;PutObject&#x60; -  上传、修改、重命名、移动 * &#x60;GetObject&#x60; - 下载 * &#x60;DeleteObject&#x60; - 删除
        :type actions: list[str]
        :param roam_actions: 云端访问存储可操作的权限合集 * &#x60;PutObject&#x60; -  上传、修改、重命名、移动 * &#x60;GetObject&#x60; - 下载 * &#x60;DeleteObject&#x60; - 删除
        :type roam_actions: list[str]
        """
        
        super(CreateOrUpdateStoragePolicyStatementResponse, self).__init__()

        self._policy_statement_id = None
        self._actions = None
        self._roam_actions = None
        self.discriminator = None

        if policy_statement_id is not None:
            self.policy_statement_id = policy_statement_id
        if actions is not None:
            self.actions = actions
        if roam_actions is not None:
            self.roam_actions = roam_actions

    @property
    def policy_statement_id(self):
        """Gets the policy_statement_id of this CreateOrUpdateStoragePolicyStatementResponse.

        支持的访问策略，内置如下四种策略: * `DEFAULT_1`：`客户端访问存储` - 上传、下载; `云端访问存储` - 读写   - action: PutObject、DeleteObject、GetObject   - roam_action: PutObject、DeleteObject、GetObject * `DEFAULT_2`：`客户端访问存储` - 下载; `云端访问存储` - 读写   - action: GetObject   - roam_action: PutObject、DeleteObject、GetObject * `DEFAULT_3`：`客户端访问存储` - 上传; `云端访问存储` - 读写   - action: PutObject、DeleteObject   - roam_action: PutObject、DeleteObject、GetObject * `DEFAULT_4`：`客户端访问存储` - 仅可查看列表,不允许上传下载; `云端访问存储` - 只读   - action:    - roam_action: GetObject

        :return: The policy_statement_id of this CreateOrUpdateStoragePolicyStatementResponse.
        :rtype: str
        """
        return self._policy_statement_id

    @policy_statement_id.setter
    def policy_statement_id(self, policy_statement_id):
        """Sets the policy_statement_id of this CreateOrUpdateStoragePolicyStatementResponse.

        支持的访问策略，内置如下四种策略: * `DEFAULT_1`：`客户端访问存储` - 上传、下载; `云端访问存储` - 读写   - action: PutObject、DeleteObject、GetObject   - roam_action: PutObject、DeleteObject、GetObject * `DEFAULT_2`：`客户端访问存储` - 下载; `云端访问存储` - 读写   - action: GetObject   - roam_action: PutObject、DeleteObject、GetObject * `DEFAULT_3`：`客户端访问存储` - 上传; `云端访问存储` - 读写   - action: PutObject、DeleteObject   - roam_action: PutObject、DeleteObject、GetObject * `DEFAULT_4`：`客户端访问存储` - 仅可查看列表,不允许上传下载; `云端访问存储` - 只读   - action:    - roam_action: GetObject

        :param policy_statement_id: The policy_statement_id of this CreateOrUpdateStoragePolicyStatementResponse.
        :type policy_statement_id: str
        """
        self._policy_statement_id = policy_statement_id

    @property
    def actions(self):
        """Gets the actions of this CreateOrUpdateStoragePolicyStatementResponse.

        客户端访问存储可操作的权限合集 * `PutObject` -  上传、修改、重命名、移动 * `GetObject` - 下载 * `DeleteObject` - 删除

        :return: The actions of this CreateOrUpdateStoragePolicyStatementResponse.
        :rtype: list[str]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """Sets the actions of this CreateOrUpdateStoragePolicyStatementResponse.

        客户端访问存储可操作的权限合集 * `PutObject` -  上传、修改、重命名、移动 * `GetObject` - 下载 * `DeleteObject` - 删除

        :param actions: The actions of this CreateOrUpdateStoragePolicyStatementResponse.
        :type actions: list[str]
        """
        self._actions = actions

    @property
    def roam_actions(self):
        """Gets the roam_actions of this CreateOrUpdateStoragePolicyStatementResponse.

        云端访问存储可操作的权限合集 * `PutObject` -  上传、修改、重命名、移动 * `GetObject` - 下载 * `DeleteObject` - 删除

        :return: The roam_actions of this CreateOrUpdateStoragePolicyStatementResponse.
        :rtype: list[str]
        """
        return self._roam_actions

    @roam_actions.setter
    def roam_actions(self, roam_actions):
        """Sets the roam_actions of this CreateOrUpdateStoragePolicyStatementResponse.

        云端访问存储可操作的权限合集 * `PutObject` -  上传、修改、重命名、移动 * `GetObject` - 下载 * `DeleteObject` - 删除

        :param roam_actions: The roam_actions of this CreateOrUpdateStoragePolicyStatementResponse.
        :type roam_actions: list[str]
        """
        self._roam_actions = roam_actions

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
        if not isinstance(other, CreateOrUpdateStoragePolicyStatementResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
