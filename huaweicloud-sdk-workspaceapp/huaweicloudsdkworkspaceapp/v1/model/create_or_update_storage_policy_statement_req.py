# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateOrUpdateStoragePolicyStatementReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'actions': 'list[str]',
        'roam_actions': 'list[str]'
    }

    attribute_map = {
        'actions': 'actions',
        'roam_actions': 'roam_actions'
    }

    def __init__(self, actions=None, roam_actions=None):
        """CreateOrUpdateStoragePolicyStatementReq

        The model defined in huaweicloud sdk

        :param actions: 客户端访问存储可操作的权限合集 允许为空,为空时配置了该策略的用户,通过云办公客户端接入后仅可查看文件列表,不可上传下载 * &#x60;PutObject&#x60; -  上传、修改、重命名、移动 * &#x60;DeleteObject&#x60; - 删除 * &#x60;GetObject&#x60; - 下载 注：PutObject和DeleteObject必须同时设置,不支持仅设置其中一个
        :type actions: list[str]
        :param roam_actions: 云端访问存储可操作的权限合集,不允许为空 * &#x60;PutObject&#x60; -  上传、修改、重命名、移动 * &#x60;DeleteObject&#x60; - 删除 * &#x60;GetObject&#x60; - 下载           注：PutObject和DeleteObject必须同时设置,不支持仅设置其中一个
        :type roam_actions: list[str]
        """
        
        

        self._actions = None
        self._roam_actions = None
        self.discriminator = None

        if actions is not None:
            self.actions = actions
        self.roam_actions = roam_actions

    @property
    def actions(self):
        """Gets the actions of this CreateOrUpdateStoragePolicyStatementReq.

        客户端访问存储可操作的权限合集 允许为空,为空时配置了该策略的用户,通过云办公客户端接入后仅可查看文件列表,不可上传下载 * `PutObject` -  上传、修改、重命名、移动 * `DeleteObject` - 删除 * `GetObject` - 下载 注：PutObject和DeleteObject必须同时设置,不支持仅设置其中一个

        :return: The actions of this CreateOrUpdateStoragePolicyStatementReq.
        :rtype: list[str]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """Sets the actions of this CreateOrUpdateStoragePolicyStatementReq.

        客户端访问存储可操作的权限合集 允许为空,为空时配置了该策略的用户,通过云办公客户端接入后仅可查看文件列表,不可上传下载 * `PutObject` -  上传、修改、重命名、移动 * `DeleteObject` - 删除 * `GetObject` - 下载 注：PutObject和DeleteObject必须同时设置,不支持仅设置其中一个

        :param actions: The actions of this CreateOrUpdateStoragePolicyStatementReq.
        :type actions: list[str]
        """
        self._actions = actions

    @property
    def roam_actions(self):
        """Gets the roam_actions of this CreateOrUpdateStoragePolicyStatementReq.

        云端访问存储可操作的权限合集,不允许为空 * `PutObject` -  上传、修改、重命名、移动 * `DeleteObject` - 删除 * `GetObject` - 下载           注：PutObject和DeleteObject必须同时设置,不支持仅设置其中一个

        :return: The roam_actions of this CreateOrUpdateStoragePolicyStatementReq.
        :rtype: list[str]
        """
        return self._roam_actions

    @roam_actions.setter
    def roam_actions(self, roam_actions):
        """Sets the roam_actions of this CreateOrUpdateStoragePolicyStatementReq.

        云端访问存储可操作的权限合集,不允许为空 * `PutObject` -  上传、修改、重命名、移动 * `DeleteObject` - 删除 * `GetObject` - 下载           注：PutObject和DeleteObject必须同时设置,不支持仅设置其中一个

        :param roam_actions: The roam_actions of this CreateOrUpdateStoragePolicyStatementReq.
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
        if not isinstance(other, CreateOrUpdateStoragePolicyStatementReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
