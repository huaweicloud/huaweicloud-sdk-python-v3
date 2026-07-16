# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WorkflowStorage:

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
        'type': 'str',
        'path': 'str'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'path': 'path'
    }

    def __init__(self, name=None, type=None, path=None):
        r"""WorkflowStorage

        The model defined in huaweicloud sdk

        :param name: 工作流存储的名称。填写1-64位，只包含英文、数字、下划线（_）和中划线（-），并且以英文开头的名称。
        :type name: str
        :param type: 工作流存储的类型，当前只支持obs。
        :type type: str
        :param path: 统一存储的根路径，当前只支持OBS路径。
        :type path: str
        """
        
        

        self._name = None
        self._type = None
        self._path = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if path is not None:
            self.path = path

    @property
    def name(self):
        r"""Gets the name of this WorkflowStorage.

        工作流存储的名称。填写1-64位，只包含英文、数字、下划线（_）和中划线（-），并且以英文开头的名称。

        :return: The name of this WorkflowStorage.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this WorkflowStorage.

        工作流存储的名称。填写1-64位，只包含英文、数字、下划线（_）和中划线（-），并且以英文开头的名称。

        :param name: The name of this WorkflowStorage.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this WorkflowStorage.

        工作流存储的类型，当前只支持obs。

        :return: The type of this WorkflowStorage.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this WorkflowStorage.

        工作流存储的类型，当前只支持obs。

        :param type: The type of this WorkflowStorage.
        :type type: str
        """
        self._type = type

    @property
    def path(self):
        r"""Gets the path of this WorkflowStorage.

        统一存储的根路径，当前只支持OBS路径。

        :return: The path of this WorkflowStorage.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this WorkflowStorage.

        统一存储的根路径，当前只支持OBS路径。

        :param path: The path of this WorkflowStorage.
        :type path: str
        """
        self._path = path

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, WorkflowStorage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
