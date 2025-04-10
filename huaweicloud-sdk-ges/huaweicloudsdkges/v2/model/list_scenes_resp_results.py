# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListScenesRespResults:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'scene': 'str',
        'name': 'str',
        'params': 'list[ListScenesRespParams]',
        'description': 'str'
    }

    attribute_map = {
        'scene': 'scene',
        'name': 'name',
        'params': 'params',
        'description': 'description'
    }

    def __init__(self, scene=None, name=None, params=None, description=None):
        r"""ListScenesRespResults

        The model defined in huaweicloud sdk

        :param scene: 场景名。
        :type scene: str
        :param name: application名称。
        :type name: str
        :param params: 参数列表。
        :type params: list[:class:`huaweicloudsdkges.v2.ListScenesRespParams`]
        :param description: 场景下应用的描述。
        :type description: str
        """
        
        

        self._scene = None
        self._name = None
        self._params = None
        self._description = None
        self.discriminator = None

        if scene is not None:
            self.scene = scene
        if name is not None:
            self.name = name
        if params is not None:
            self.params = params
        if description is not None:
            self.description = description

    @property
    def scene(self):
        r"""Gets the scene of this ListScenesRespResults.

        场景名。

        :return: The scene of this ListScenesRespResults.
        :rtype: str
        """
        return self._scene

    @scene.setter
    def scene(self, scene):
        r"""Sets the scene of this ListScenesRespResults.

        场景名。

        :param scene: The scene of this ListScenesRespResults.
        :type scene: str
        """
        self._scene = scene

    @property
    def name(self):
        r"""Gets the name of this ListScenesRespResults.

        application名称。

        :return: The name of this ListScenesRespResults.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListScenesRespResults.

        application名称。

        :param name: The name of this ListScenesRespResults.
        :type name: str
        """
        self._name = name

    @property
    def params(self):
        r"""Gets the params of this ListScenesRespResults.

        参数列表。

        :return: The params of this ListScenesRespResults.
        :rtype: list[:class:`huaweicloudsdkges.v2.ListScenesRespParams`]
        """
        return self._params

    @params.setter
    def params(self, params):
        r"""Sets the params of this ListScenesRespResults.

        参数列表。

        :param params: The params of this ListScenesRespResults.
        :type params: list[:class:`huaweicloudsdkges.v2.ListScenesRespParams`]
        """
        self._params = params

    @property
    def description(self):
        r"""Gets the description of this ListScenesRespResults.

        场景下应用的描述。

        :return: The description of this ListScenesRespResults.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ListScenesRespResults.

        场景下应用的描述。

        :param description: The description of this ListScenesRespResults.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, ListScenesRespResults):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
