# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ComponentAmb:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'component_id': 'str',
        'component_name': 'str',
        'component_version': 'str',
        'component_desc': 'str'
    }

    attribute_map = {
        'component_id': 'componentId',
        'component_name': 'componentName',
        'component_version': 'componentVersion',
        'component_desc': 'componentDesc'
    }

    def __init__(self, component_id=None, component_name=None, component_version=None, component_desc=None):
        r"""ComponentAmb

        The model defined in huaweicloud sdk

        :param component_id: 组件ID。
        :type component_id: str
        :param component_name: 组件名称。
        :type component_name: str
        :param component_version: 组件版本。
        :type component_version: str
        :param component_desc: 组件描述信息。
        :type component_desc: str
        """
        
        

        self._component_id = None
        self._component_name = None
        self._component_version = None
        self._component_desc = None
        self.discriminator = None

        if component_id is not None:
            self.component_id = component_id
        if component_name is not None:
            self.component_name = component_name
        if component_version is not None:
            self.component_version = component_version
        if component_desc is not None:
            self.component_desc = component_desc

    @property
    def component_id(self):
        r"""Gets the component_id of this ComponentAmb.

        组件ID。

        :return: The component_id of this ComponentAmb.
        :rtype: str
        """
        return self._component_id

    @component_id.setter
    def component_id(self, component_id):
        r"""Sets the component_id of this ComponentAmb.

        组件ID。

        :param component_id: The component_id of this ComponentAmb.
        :type component_id: str
        """
        self._component_id = component_id

    @property
    def component_name(self):
        r"""Gets the component_name of this ComponentAmb.

        组件名称。

        :return: The component_name of this ComponentAmb.
        :rtype: str
        """
        return self._component_name

    @component_name.setter
    def component_name(self, component_name):
        r"""Sets the component_name of this ComponentAmb.

        组件名称。

        :param component_name: The component_name of this ComponentAmb.
        :type component_name: str
        """
        self._component_name = component_name

    @property
    def component_version(self):
        r"""Gets the component_version of this ComponentAmb.

        组件版本。

        :return: The component_version of this ComponentAmb.
        :rtype: str
        """
        return self._component_version

    @component_version.setter
    def component_version(self, component_version):
        r"""Sets the component_version of this ComponentAmb.

        组件版本。

        :param component_version: The component_version of this ComponentAmb.
        :type component_version: str
        """
        self._component_version = component_version

    @property
    def component_desc(self):
        r"""Gets the component_desc of this ComponentAmb.

        组件描述信息。

        :return: The component_desc of this ComponentAmb.
        :rtype: str
        """
        return self._component_desc

    @component_desc.setter
    def component_desc(self, component_desc):
        r"""Sets the component_desc of this ComponentAmb.

        组件描述信息。

        :param component_desc: The component_desc of this ComponentAmb.
        :type component_desc: str
        """
        self._component_desc = component_desc

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
        if not isinstance(other, ComponentAmb):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
