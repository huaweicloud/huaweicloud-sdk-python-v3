# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchAssetActionReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'action': 'str',
        'asset_ids': 'list[str]',
        'params': 'str'
    }

    attribute_map = {
        'action': 'action',
        'asset_ids': 'asset_ids',
        'params': 'params'
    }

    def __init__(self, action=None, asset_ids=None, params=None):
        r"""BatchAssetActionReq

        The model defined in huaweicloud sdk

        :param action: 批量操作命令. * DELETE：删除 * DELETE_FORCE：强制删除，该模式会立即删除资产 * RESTORE：恢复 * UNACTIVE：取消激活 * ACTIVE：激活 * SHARE：共享 * UNSHARE：取消共享
        :type action: str
        :param asset_ids: 资产ID列表
        :type asset_ids: list[str]
        :param params: 操作参数
        :type params: str
        """
        
        

        self._action = None
        self._asset_ids = None
        self._params = None
        self.discriminator = None

        self.action = action
        self.asset_ids = asset_ids
        if params is not None:
            self.params = params

    @property
    def action(self):
        r"""Gets the action of this BatchAssetActionReq.

        批量操作命令. * DELETE：删除 * DELETE_FORCE：强制删除，该模式会立即删除资产 * RESTORE：恢复 * UNACTIVE：取消激活 * ACTIVE：激活 * SHARE：共享 * UNSHARE：取消共享

        :return: The action of this BatchAssetActionReq.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this BatchAssetActionReq.

        批量操作命令. * DELETE：删除 * DELETE_FORCE：强制删除，该模式会立即删除资产 * RESTORE：恢复 * UNACTIVE：取消激活 * ACTIVE：激活 * SHARE：共享 * UNSHARE：取消共享

        :param action: The action of this BatchAssetActionReq.
        :type action: str
        """
        self._action = action

    @property
    def asset_ids(self):
        r"""Gets the asset_ids of this BatchAssetActionReq.

        资产ID列表

        :return: The asset_ids of this BatchAssetActionReq.
        :rtype: list[str]
        """
        return self._asset_ids

    @asset_ids.setter
    def asset_ids(self, asset_ids):
        r"""Sets the asset_ids of this BatchAssetActionReq.

        资产ID列表

        :param asset_ids: The asset_ids of this BatchAssetActionReq.
        :type asset_ids: list[str]
        """
        self._asset_ids = asset_ids

    @property
    def params(self):
        r"""Gets the params of this BatchAssetActionReq.

        操作参数

        :return: The params of this BatchAssetActionReq.
        :rtype: str
        """
        return self._params

    @params.setter
    def params(self, params):
        r"""Sets the params of this BatchAssetActionReq.

        操作参数

        :param params: The params of this BatchAssetActionReq.
        :type params: str
        """
        self._params = params

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
        if not isinstance(other, BatchAssetActionReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
