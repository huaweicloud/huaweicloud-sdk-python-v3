# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpgradeTypeInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'upgrade_type': 'str',
        'enable': 'bool',
        'upgrade_action_list': 'list[UpgradeActionInfo]'
    }

    attribute_map = {
        'upgrade_type': 'upgrade_type',
        'enable': 'enable',
        'upgrade_action_list': 'upgrade_action_list'
    }

    def __init__(self, upgrade_type=None, enable=None, upgrade_action_list=None):
        """UpgradeTypeInfo

        The model defined in huaweicloud sdk

        :param upgrade_type: 升级类型,grey&#x3D;灰度升级,inplace&#x3D;就地升级,hotfix&#x3D;热补丁升级
        :type upgrade_type: str
        :param enable: 可用，不可用
        :type enable: bool
        :param upgrade_action_list: 升级操作列表
        :type upgrade_action_list: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.UpgradeActionInfo`]
        """
        
        

        self._upgrade_type = None
        self._enable = None
        self._upgrade_action_list = None
        self.discriminator = None

        if upgrade_type is not None:
            self.upgrade_type = upgrade_type
        if enable is not None:
            self.enable = enable
        if upgrade_action_list is not None:
            self.upgrade_action_list = upgrade_action_list

    @property
    def upgrade_type(self):
        """Gets the upgrade_type of this UpgradeTypeInfo.

        升级类型,grey=灰度升级,inplace=就地升级,hotfix=热补丁升级

        :return: The upgrade_type of this UpgradeTypeInfo.
        :rtype: str
        """
        return self._upgrade_type

    @upgrade_type.setter
    def upgrade_type(self, upgrade_type):
        """Sets the upgrade_type of this UpgradeTypeInfo.

        升级类型,grey=灰度升级,inplace=就地升级,hotfix=热补丁升级

        :param upgrade_type: The upgrade_type of this UpgradeTypeInfo.
        :type upgrade_type: str
        """
        self._upgrade_type = upgrade_type

    @property
    def enable(self):
        """Gets the enable of this UpgradeTypeInfo.

        可用，不可用

        :return: The enable of this UpgradeTypeInfo.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this UpgradeTypeInfo.

        可用，不可用

        :param enable: The enable of this UpgradeTypeInfo.
        :type enable: bool
        """
        self._enable = enable

    @property
    def upgrade_action_list(self):
        """Gets the upgrade_action_list of this UpgradeTypeInfo.

        升级操作列表

        :return: The upgrade_action_list of this UpgradeTypeInfo.
        :rtype: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.UpgradeActionInfo`]
        """
        return self._upgrade_action_list

    @upgrade_action_list.setter
    def upgrade_action_list(self, upgrade_action_list):
        """Sets the upgrade_action_list of this UpgradeTypeInfo.

        升级操作列表

        :param upgrade_action_list: The upgrade_action_list of this UpgradeTypeInfo.
        :type upgrade_action_list: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.UpgradeActionInfo`]
        """
        self._upgrade_action_list = upgrade_action_list

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
        if not isinstance(other, UpgradeTypeInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
