# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RegisterScenesReqScenes:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'applications': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'applications': 'applications'
    }

    def __init__(self, name=None, applications=None):
        r"""RegisterScenesReqScenes

        The model defined in huaweicloud sdk

        :param name: 场景名称。
        :type name: str
        :param applications: 要订阅的application名字列表(当前不支持)。
        :type applications: list[str]
        """
        
        

        self._name = None
        self._applications = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if applications is not None:
            self.applications = applications

    @property
    def name(self):
        r"""Gets the name of this RegisterScenesReqScenes.

        场景名称。

        :return: The name of this RegisterScenesReqScenes.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this RegisterScenesReqScenes.

        场景名称。

        :param name: The name of this RegisterScenesReqScenes.
        :type name: str
        """
        self._name = name

    @property
    def applications(self):
        r"""Gets the applications of this RegisterScenesReqScenes.

        要订阅的application名字列表(当前不支持)。

        :return: The applications of this RegisterScenesReqScenes.
        :rtype: list[str]
        """
        return self._applications

    @applications.setter
    def applications(self, applications):
        r"""Sets the applications of this RegisterScenesReqScenes.

        要订阅的application名字列表(当前不支持)。

        :param applications: The applications of this RegisterScenesReqScenes.
        :type applications: list[str]
        """
        self._applications = applications

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
        if not isinstance(other, RegisterScenesReqScenes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
