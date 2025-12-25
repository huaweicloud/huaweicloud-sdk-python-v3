# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TrashArtifactModelForDelete:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'format': 'str',
        'uri': 'str',
        'status': 'str',
        'include_pattern': 'str'
    }

    attribute_map = {
        'id': 'id',
        'format': 'format',
        'uri': 'uri',
        'status': 'status',
        'include_pattern': 'include_pattern'
    }

    def __init__(self, id=None, format=None, uri=None, status=None, include_pattern=None):
        r"""TrashArtifactModelForDelete

        The model defined in huaweicloud sdk

        :param id: 仓库id
        :type id: str
        :param format: 仓库类型
        :type format: str
        :param uri: URI
        :type uri: str
        :param status: 状态
        :type status: str
        :param include_pattern: 路径白名单
        :type include_pattern: str
        """
        
        

        self._id = None
        self._format = None
        self._uri = None
        self._status = None
        self._include_pattern = None
        self.discriminator = None

        self.id = id
        self.format = format
        self.uri = uri
        self.status = status
        if include_pattern is not None:
            self.include_pattern = include_pattern

    @property
    def id(self):
        r"""Gets the id of this TrashArtifactModelForDelete.

        仓库id

        :return: The id of this TrashArtifactModelForDelete.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this TrashArtifactModelForDelete.

        仓库id

        :param id: The id of this TrashArtifactModelForDelete.
        :type id: str
        """
        self._id = id

    @property
    def format(self):
        r"""Gets the format of this TrashArtifactModelForDelete.

        仓库类型

        :return: The format of this TrashArtifactModelForDelete.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        r"""Sets the format of this TrashArtifactModelForDelete.

        仓库类型

        :param format: The format of this TrashArtifactModelForDelete.
        :type format: str
        """
        self._format = format

    @property
    def uri(self):
        r"""Gets the uri of this TrashArtifactModelForDelete.

        URI

        :return: The uri of this TrashArtifactModelForDelete.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        r"""Sets the uri of this TrashArtifactModelForDelete.

        URI

        :param uri: The uri of this TrashArtifactModelForDelete.
        :type uri: str
        """
        self._uri = uri

    @property
    def status(self):
        r"""Gets the status of this TrashArtifactModelForDelete.

        状态

        :return: The status of this TrashArtifactModelForDelete.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this TrashArtifactModelForDelete.

        状态

        :param status: The status of this TrashArtifactModelForDelete.
        :type status: str
        """
        self._status = status

    @property
    def include_pattern(self):
        r"""Gets the include_pattern of this TrashArtifactModelForDelete.

        路径白名单

        :return: The include_pattern of this TrashArtifactModelForDelete.
        :rtype: str
        """
        return self._include_pattern

    @include_pattern.setter
    def include_pattern(self, include_pattern):
        r"""Sets the include_pattern of this TrashArtifactModelForDelete.

        路径白名单

        :param include_pattern: The include_pattern of this TrashArtifactModelForDelete.
        :type include_pattern: str
        """
        self._include_pattern = include_pattern

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
        if not isinstance(other, TrashArtifactModelForDelete):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
