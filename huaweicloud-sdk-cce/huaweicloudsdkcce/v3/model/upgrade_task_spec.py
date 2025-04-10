# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpgradeTaskSpec:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'version': 'str',
        'target_version': 'str',
        'items': 'object'
    }

    attribute_map = {
        'version': 'version',
        'target_version': 'targetVersion',
        'items': 'items'
    }

    def __init__(self, version=None, target_version=None, items=None):
        r"""UpgradeTaskSpec

        The model defined in huaweicloud sdk

        :param version: 升级前集群版本
        :type version: str
        :param target_version: 升级的目标集群版本
        :type target_version: str
        :param items: 升级任务附属信息
        :type items: object
        """
        
        

        self._version = None
        self._target_version = None
        self._items = None
        self.discriminator = None

        if version is not None:
            self.version = version
        if target_version is not None:
            self.target_version = target_version
        if items is not None:
            self.items = items

    @property
    def version(self):
        r"""Gets the version of this UpgradeTaskSpec.

        升级前集群版本

        :return: The version of this UpgradeTaskSpec.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this UpgradeTaskSpec.

        升级前集群版本

        :param version: The version of this UpgradeTaskSpec.
        :type version: str
        """
        self._version = version

    @property
    def target_version(self):
        r"""Gets the target_version of this UpgradeTaskSpec.

        升级的目标集群版本

        :return: The target_version of this UpgradeTaskSpec.
        :rtype: str
        """
        return self._target_version

    @target_version.setter
    def target_version(self, target_version):
        r"""Sets the target_version of this UpgradeTaskSpec.

        升级的目标集群版本

        :param target_version: The target_version of this UpgradeTaskSpec.
        :type target_version: str
        """
        self._target_version = target_version

    @property
    def items(self):
        r"""Gets the items of this UpgradeTaskSpec.

        升级任务附属信息

        :return: The items of this UpgradeTaskSpec.
        :rtype: object
        """
        return self._items

    @items.setter
    def items(self, items):
        r"""Sets the items of this UpgradeTaskSpec.

        升级任务附属信息

        :param items: The items of this UpgradeTaskSpec.
        :type items: object
        """
        self._items = items

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
        if not isinstance(other, UpgradeTaskSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
