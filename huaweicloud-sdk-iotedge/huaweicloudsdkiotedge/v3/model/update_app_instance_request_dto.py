# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateAppInstanceRequestDTO:

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
        'namespace': 'str',
        'app_version': 'str',
        'values': 'object',
        'rollback_version': 'str'
    }

    attribute_map = {
        'action': 'action',
        'namespace': 'namespace',
        'app_version': 'app_version',
        'values': 'values',
        'rollback_version': 'rollback_version'
    }

    def __init__(self, action=None, namespace=None, app_version=None, values=None, rollback_version=None):
        r"""UpdateAppInstanceRequestDTO

        The model defined in huaweicloud sdk

        :param action: 动作类型
        :type action: str
        :param namespace: 命名空间，应用实例部署于非默认命名空间(default)时必填
        :type namespace: str
        :param app_version: 升级的目标版本号，动作类型为upgrade时必填
        :type app_version: str
        :param values: 应用实例chart配置，动作类型为upgrade时必填
        :type values: object
        :param rollback_version: 回退的目标版本号，动作类型为rollback时必填
        :type rollback_version: str
        """
        
        

        self._action = None
        self._namespace = None
        self._app_version = None
        self._values = None
        self._rollback_version = None
        self.discriminator = None

        self.action = action
        if namespace is not None:
            self.namespace = namespace
        if app_version is not None:
            self.app_version = app_version
        if values is not None:
            self.values = values
        if rollback_version is not None:
            self.rollback_version = rollback_version

    @property
    def action(self):
        r"""Gets the action of this UpdateAppInstanceRequestDTO.

        动作类型

        :return: The action of this UpdateAppInstanceRequestDTO.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this UpdateAppInstanceRequestDTO.

        动作类型

        :param action: The action of this UpdateAppInstanceRequestDTO.
        :type action: str
        """
        self._action = action

    @property
    def namespace(self):
        r"""Gets the namespace of this UpdateAppInstanceRequestDTO.

        命名空间，应用实例部署于非默认命名空间(default)时必填

        :return: The namespace of this UpdateAppInstanceRequestDTO.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this UpdateAppInstanceRequestDTO.

        命名空间，应用实例部署于非默认命名空间(default)时必填

        :param namespace: The namespace of this UpdateAppInstanceRequestDTO.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def app_version(self):
        r"""Gets the app_version of this UpdateAppInstanceRequestDTO.

        升级的目标版本号，动作类型为upgrade时必填

        :return: The app_version of this UpdateAppInstanceRequestDTO.
        :rtype: str
        """
        return self._app_version

    @app_version.setter
    def app_version(self, app_version):
        r"""Sets the app_version of this UpdateAppInstanceRequestDTO.

        升级的目标版本号，动作类型为upgrade时必填

        :param app_version: The app_version of this UpdateAppInstanceRequestDTO.
        :type app_version: str
        """
        self._app_version = app_version

    @property
    def values(self):
        r"""Gets the values of this UpdateAppInstanceRequestDTO.

        应用实例chart配置，动作类型为upgrade时必填

        :return: The values of this UpdateAppInstanceRequestDTO.
        :rtype: object
        """
        return self._values

    @values.setter
    def values(self, values):
        r"""Sets the values of this UpdateAppInstanceRequestDTO.

        应用实例chart配置，动作类型为upgrade时必填

        :param values: The values of this UpdateAppInstanceRequestDTO.
        :type values: object
        """
        self._values = values

    @property
    def rollback_version(self):
        r"""Gets the rollback_version of this UpdateAppInstanceRequestDTO.

        回退的目标版本号，动作类型为rollback时必填

        :return: The rollback_version of this UpdateAppInstanceRequestDTO.
        :rtype: str
        """
        return self._rollback_version

    @rollback_version.setter
    def rollback_version(self, rollback_version):
        r"""Sets the rollback_version of this UpdateAppInstanceRequestDTO.

        回退的目标版本号，动作类型为rollback时必填

        :param rollback_version: The rollback_version of this UpdateAppInstanceRequestDTO.
        :type rollback_version: str
        """
        self._rollback_version = rollback_version

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
        if not isinstance(other, UpdateAppInstanceRequestDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
