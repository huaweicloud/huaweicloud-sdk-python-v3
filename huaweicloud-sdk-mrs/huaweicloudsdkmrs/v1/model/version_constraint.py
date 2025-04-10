# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VersionConstraint:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'other': 'dict(str, object)',
        'node_constraint': 'NodeConstraints',
        'safe_mode_kerberos_exclude_components': 'list[str]'
    }

    attribute_map = {
        'other': 'other',
        'node_constraint': 'node_constraint',
        'safe_mode_kerberos_exclude_components': 'safe_mode_kerberos_exclude_components'
    }

    def __init__(self, other=None, node_constraint=None, safe_mode_kerberos_exclude_components=None):
        r"""VersionConstraint

        The model defined in huaweicloud sdk

        :param other: 其他限制
        :type other: dict(str, object)
        :param node_constraint: 
        :type node_constraint: :class:`huaweicloudsdkmrs.v1.NodeConstraints`
        :param safe_mode_kerberos_exclude_components: 安全模式kerberos排除组件列表
        :type safe_mode_kerberos_exclude_components: list[str]
        """
        
        

        self._other = None
        self._node_constraint = None
        self._safe_mode_kerberos_exclude_components = None
        self.discriminator = None

        if other is not None:
            self.other = other
        if node_constraint is not None:
            self.node_constraint = node_constraint
        if safe_mode_kerberos_exclude_components is not None:
            self.safe_mode_kerberos_exclude_components = safe_mode_kerberos_exclude_components

    @property
    def other(self):
        r"""Gets the other of this VersionConstraint.

        其他限制

        :return: The other of this VersionConstraint.
        :rtype: dict(str, object)
        """
        return self._other

    @other.setter
    def other(self, other):
        r"""Sets the other of this VersionConstraint.

        其他限制

        :param other: The other of this VersionConstraint.
        :type other: dict(str, object)
        """
        self._other = other

    @property
    def node_constraint(self):
        r"""Gets the node_constraint of this VersionConstraint.

        :return: The node_constraint of this VersionConstraint.
        :rtype: :class:`huaweicloudsdkmrs.v1.NodeConstraints`
        """
        return self._node_constraint

    @node_constraint.setter
    def node_constraint(self, node_constraint):
        r"""Sets the node_constraint of this VersionConstraint.

        :param node_constraint: The node_constraint of this VersionConstraint.
        :type node_constraint: :class:`huaweicloudsdkmrs.v1.NodeConstraints`
        """
        self._node_constraint = node_constraint

    @property
    def safe_mode_kerberos_exclude_components(self):
        r"""Gets the safe_mode_kerberos_exclude_components of this VersionConstraint.

        安全模式kerberos排除组件列表

        :return: The safe_mode_kerberos_exclude_components of this VersionConstraint.
        :rtype: list[str]
        """
        return self._safe_mode_kerberos_exclude_components

    @safe_mode_kerberos_exclude_components.setter
    def safe_mode_kerberos_exclude_components(self, safe_mode_kerberos_exclude_components):
        r"""Sets the safe_mode_kerberos_exclude_components of this VersionConstraint.

        安全模式kerberos排除组件列表

        :param safe_mode_kerberos_exclude_components: The safe_mode_kerberos_exclude_components of this VersionConstraint.
        :type safe_mode_kerberos_exclude_components: list[str]
        """
        self._safe_mode_kerberos_exclude_components = safe_mode_kerberos_exclude_components

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
        if not isinstance(other, VersionConstraint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
