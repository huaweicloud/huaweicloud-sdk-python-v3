# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MountComponent:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'env_id': 'str',
        'env_name': 'str',
        'app_id': 'str',
        'app_name': 'str',
        'component_id': 'str',
        'component_name': 'str'
    }

    attribute_map = {
        'env_id': 'env_id',
        'env_name': 'env_name',
        'app_id': 'app_id',
        'app_name': 'app_name',
        'component_id': 'component_id',
        'component_name': 'component_name'
    }

    def __init__(self, env_id=None, env_name=None, app_id=None, app_name=None, component_id=None, component_name=None):
        r"""MountComponent

        The model defined in huaweicloud sdk

        :param env_id: 环境ID。
        :type env_id: str
        :param env_name: 环境名称。
        :type env_name: str
        :param app_id: 应用ID。
        :type app_id: str
        :param app_name: 应用名称。
        :type app_name: str
        :param component_id: 组件ID。
        :type component_id: str
        :param component_name: 组件名称。
        :type component_name: str
        """
        
        

        self._env_id = None
        self._env_name = None
        self._app_id = None
        self._app_name = None
        self._component_id = None
        self._component_name = None
        self.discriminator = None

        if env_id is not None:
            self.env_id = env_id
        if env_name is not None:
            self.env_name = env_name
        if app_id is not None:
            self.app_id = app_id
        if app_name is not None:
            self.app_name = app_name
        if component_id is not None:
            self.component_id = component_id
        if component_name is not None:
            self.component_name = component_name

    @property
    def env_id(self):
        r"""Gets the env_id of this MountComponent.

        环境ID。

        :return: The env_id of this MountComponent.
        :rtype: str
        """
        return self._env_id

    @env_id.setter
    def env_id(self, env_id):
        r"""Sets the env_id of this MountComponent.

        环境ID。

        :param env_id: The env_id of this MountComponent.
        :type env_id: str
        """
        self._env_id = env_id

    @property
    def env_name(self):
        r"""Gets the env_name of this MountComponent.

        环境名称。

        :return: The env_name of this MountComponent.
        :rtype: str
        """
        return self._env_name

    @env_name.setter
    def env_name(self, env_name):
        r"""Sets the env_name of this MountComponent.

        环境名称。

        :param env_name: The env_name of this MountComponent.
        :type env_name: str
        """
        self._env_name = env_name

    @property
    def app_id(self):
        r"""Gets the app_id of this MountComponent.

        应用ID。

        :return: The app_id of this MountComponent.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        r"""Sets the app_id of this MountComponent.

        应用ID。

        :param app_id: The app_id of this MountComponent.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def app_name(self):
        r"""Gets the app_name of this MountComponent.

        应用名称。

        :return: The app_name of this MountComponent.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        r"""Sets the app_name of this MountComponent.

        应用名称。

        :param app_name: The app_name of this MountComponent.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def component_id(self):
        r"""Gets the component_id of this MountComponent.

        组件ID。

        :return: The component_id of this MountComponent.
        :rtype: str
        """
        return self._component_id

    @component_id.setter
    def component_id(self, component_id):
        r"""Sets the component_id of this MountComponent.

        组件ID。

        :param component_id: The component_id of this MountComponent.
        :type component_id: str
        """
        self._component_id = component_id

    @property
    def component_name(self):
        r"""Gets the component_name of this MountComponent.

        组件名称。

        :return: The component_name of this MountComponent.
        :rtype: str
        """
        return self._component_name

    @component_name.setter
    def component_name(self, component_name):
        r"""Sets the component_name of this MountComponent.

        组件名称。

        :param component_name: The component_name of this MountComponent.
        :type component_name: str
        """
        self._component_name = component_name

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
        if not isinstance(other, MountComponent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
