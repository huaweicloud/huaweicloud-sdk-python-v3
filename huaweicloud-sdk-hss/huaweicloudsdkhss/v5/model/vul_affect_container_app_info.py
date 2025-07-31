# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VulAffectContainerAppInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'app_name': 'str',
        'paths': 'list[VulAffectContainerAppPath]',
        'rule': 'str'
    }

    attribute_map = {
        'app_name': 'app_name',
        'paths': 'paths',
        'rule': 'rule'
    }

    def __init__(self, app_name=None, paths=None, rule=None):
        r"""VulAffectContainerAppInfo

        The model defined in huaweicloud sdk

        :param app_name: 软件名称
        :type app_name: str
        :param paths: 列表
        :type paths: list[:class:`huaweicloudsdkhss.v5.VulAffectContainerAppPath`]
        :param rule: 规则
        :type rule: str
        """
        
        

        self._app_name = None
        self._paths = None
        self._rule = None
        self.discriminator = None

        if app_name is not None:
            self.app_name = app_name
        if paths is not None:
            self.paths = paths
        if rule is not None:
            self.rule = rule

    @property
    def app_name(self):
        r"""Gets the app_name of this VulAffectContainerAppInfo.

        软件名称

        :return: The app_name of this VulAffectContainerAppInfo.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        r"""Sets the app_name of this VulAffectContainerAppInfo.

        软件名称

        :param app_name: The app_name of this VulAffectContainerAppInfo.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def paths(self):
        r"""Gets the paths of this VulAffectContainerAppInfo.

        列表

        :return: The paths of this VulAffectContainerAppInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.VulAffectContainerAppPath`]
        """
        return self._paths

    @paths.setter
    def paths(self, paths):
        r"""Sets the paths of this VulAffectContainerAppInfo.

        列表

        :param paths: The paths of this VulAffectContainerAppInfo.
        :type paths: list[:class:`huaweicloudsdkhss.v5.VulAffectContainerAppPath`]
        """
        self._paths = paths

    @property
    def rule(self):
        r"""Gets the rule of this VulAffectContainerAppInfo.

        规则

        :return: The rule of this VulAffectContainerAppInfo.
        :rtype: str
        """
        return self._rule

    @rule.setter
    def rule(self, rule):
        r"""Sets the rule of this VulAffectContainerAppInfo.

        规则

        :param rule: The rule of this VulAffectContainerAppInfo.
        :type rule: str
        """
        self._rule = rule

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
        if not isinstance(other, VulAffectContainerAppInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
