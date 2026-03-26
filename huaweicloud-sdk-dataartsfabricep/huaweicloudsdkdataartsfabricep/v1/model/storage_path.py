# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StoragePath:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'path': 'str'
    }

    attribute_map = {
        'type': 'type',
        'path': 'path'
    }

    def __init__(self, type=None, path=None):
        r"""StoragePath

        The model defined in huaweicloud sdk

        :param type: 日志存储类型，可选值如下： OBS：日志存储在OBS CONTAINER：日志存储在容器 LTS：日志存储在LTS
        :type type: str
        :param path: 路径
        :type path: str
        """
        
        

        self._type = None
        self._path = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if path is not None:
            self.path = path

    @property
    def type(self):
        r"""Gets the type of this StoragePath.

        日志存储类型，可选值如下： OBS：日志存储在OBS CONTAINER：日志存储在容器 LTS：日志存储在LTS

        :return: The type of this StoragePath.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this StoragePath.

        日志存储类型，可选值如下： OBS：日志存储在OBS CONTAINER：日志存储在容器 LTS：日志存储在LTS

        :param type: The type of this StoragePath.
        :type type: str
        """
        self._type = type

    @property
    def path(self):
        r"""Gets the path of this StoragePath.

        路径

        :return: The path of this StoragePath.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this StoragePath.

        路径

        :param path: The path of this StoragePath.
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
        if not isinstance(other, StoragePath):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
