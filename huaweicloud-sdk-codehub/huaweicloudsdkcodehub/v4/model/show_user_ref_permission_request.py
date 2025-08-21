# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowUserRefPermissionRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'repository_id': 'int',
        'target_ref': 'str',
        'action': 'str',
        'change_request_iid': 'int'
    }

    attribute_map = {
        'repository_id': 'repository_id',
        'target_ref': 'target_ref',
        'action': 'action',
        'change_request_iid': 'change_request_iid'
    }

    def __init__(self, repository_id=None, target_ref=None, action=None, change_request_iid=None):
        r"""ShowUserRefPermissionRequest

        The model defined in huaweicloud sdk

        :param repository_id: **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。
        :type repository_id: int
        :param target_ref: **参数解释：** 分支或者标签名称。  **约束限制：** 不支持空格 [ \\ &lt; ~ ^ : ? * ! ( ) &#39; \&quot; | 等特殊字符，不支持以. / .lock结尾，分支以refs/head/开头，标签以refs/tag/开头  **取值范围：** 字符串长度不少于1，不超过210。 **默认取值：** 不涉及。
        :type target_ref: str
        :param action: **参数解释：** 动作类型，可用于查询指定动作的权限 - read，查看 - review，检视 - approval, 审核 - create-change，创建变更请求 - merge，合并变更请求 - create-delete，创建/删除分支 - push, 推送
        :type action: str
        :param change_request_iid: **参数解释：** 变更请求在仓库内部的ID。
        :type change_request_iid: int
        """
        
        

        self._repository_id = None
        self._target_ref = None
        self._action = None
        self._change_request_iid = None
        self.discriminator = None

        self.repository_id = repository_id
        self.target_ref = target_ref
        if action is not None:
            self.action = action
        if change_request_iid is not None:
            self.change_request_iid = change_request_iid

    @property
    def repository_id(self):
        r"""Gets the repository_id of this ShowUserRefPermissionRequest.

        **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。

        :return: The repository_id of this ShowUserRefPermissionRequest.
        :rtype: int
        """
        return self._repository_id

    @repository_id.setter
    def repository_id(self, repository_id):
        r"""Sets the repository_id of this ShowUserRefPermissionRequest.

        **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。

        :param repository_id: The repository_id of this ShowUserRefPermissionRequest.
        :type repository_id: int
        """
        self._repository_id = repository_id

    @property
    def target_ref(self):
        r"""Gets the target_ref of this ShowUserRefPermissionRequest.

        **参数解释：** 分支或者标签名称。  **约束限制：** 不支持空格 [ \\ < ~ ^ : ? * ! ( ) ' \" | 等特殊字符，不支持以. / .lock结尾，分支以refs/head/开头，标签以refs/tag/开头  **取值范围：** 字符串长度不少于1，不超过210。 **默认取值：** 不涉及。

        :return: The target_ref of this ShowUserRefPermissionRequest.
        :rtype: str
        """
        return self._target_ref

    @target_ref.setter
    def target_ref(self, target_ref):
        r"""Sets the target_ref of this ShowUserRefPermissionRequest.

        **参数解释：** 分支或者标签名称。  **约束限制：** 不支持空格 [ \\ < ~ ^ : ? * ! ( ) ' \" | 等特殊字符，不支持以. / .lock结尾，分支以refs/head/开头，标签以refs/tag/开头  **取值范围：** 字符串长度不少于1，不超过210。 **默认取值：** 不涉及。

        :param target_ref: The target_ref of this ShowUserRefPermissionRequest.
        :type target_ref: str
        """
        self._target_ref = target_ref

    @property
    def action(self):
        r"""Gets the action of this ShowUserRefPermissionRequest.

        **参数解释：** 动作类型，可用于查询指定动作的权限 - read，查看 - review，检视 - approval, 审核 - create-change，创建变更请求 - merge，合并变更请求 - create-delete，创建/删除分支 - push, 推送

        :return: The action of this ShowUserRefPermissionRequest.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this ShowUserRefPermissionRequest.

        **参数解释：** 动作类型，可用于查询指定动作的权限 - read，查看 - review，检视 - approval, 审核 - create-change，创建变更请求 - merge，合并变更请求 - create-delete，创建/删除分支 - push, 推送

        :param action: The action of this ShowUserRefPermissionRequest.
        :type action: str
        """
        self._action = action

    @property
    def change_request_iid(self):
        r"""Gets the change_request_iid of this ShowUserRefPermissionRequest.

        **参数解释：** 变更请求在仓库内部的ID。

        :return: The change_request_iid of this ShowUserRefPermissionRequest.
        :rtype: int
        """
        return self._change_request_iid

    @change_request_iid.setter
    def change_request_iid(self, change_request_iid):
        r"""Sets the change_request_iid of this ShowUserRefPermissionRequest.

        **参数解释：** 变更请求在仓库内部的ID。

        :param change_request_iid: The change_request_iid of this ShowUserRefPermissionRequest.
        :type change_request_iid: int
        """
        self._change_request_iid = change_request_iid

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
        if not isinstance(other, ShowUserRefPermissionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
