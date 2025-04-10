# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IDETrashArtifactModel:

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
        'status': 'str',
        'uri': 'str'
    }

    attribute_map = {
        'id': 'id',
        'format': 'format',
        'status': 'status',
        'uri': 'uri'
    }

    def __init__(self, id=None, format=None, status=None, uri=None):
        r"""IDETrashArtifactModel

        The model defined in huaweicloud sdk

        :param id: 仓库id
        :type id: str
        :param format: 类型
        :type format: str
        :param status: 当前仓库状态
        :type status: str
        :param uri: 待还原的文件路径
        :type uri: str
        """
        
        

        self._id = None
        self._format = None
        self._status = None
        self._uri = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if format is not None:
            self.format = format
        if status is not None:
            self.status = status
        if uri is not None:
            self.uri = uri

    @property
    def id(self):
        r"""Gets the id of this IDETrashArtifactModel.

        仓库id

        :return: The id of this IDETrashArtifactModel.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this IDETrashArtifactModel.

        仓库id

        :param id: The id of this IDETrashArtifactModel.
        :type id: str
        """
        self._id = id

    @property
    def format(self):
        r"""Gets the format of this IDETrashArtifactModel.

        类型

        :return: The format of this IDETrashArtifactModel.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        r"""Sets the format of this IDETrashArtifactModel.

        类型

        :param format: The format of this IDETrashArtifactModel.
        :type format: str
        """
        self._format = format

    @property
    def status(self):
        r"""Gets the status of this IDETrashArtifactModel.

        当前仓库状态

        :return: The status of this IDETrashArtifactModel.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this IDETrashArtifactModel.

        当前仓库状态

        :param status: The status of this IDETrashArtifactModel.
        :type status: str
        """
        self._status = status

    @property
    def uri(self):
        r"""Gets the uri of this IDETrashArtifactModel.

        待还原的文件路径

        :return: The uri of this IDETrashArtifactModel.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        r"""Sets the uri of this IDETrashArtifactModel.

        待还原的文件路径

        :param uri: The uri of this IDETrashArtifactModel.
        :type uri: str
        """
        self._uri = uri

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
        if not isinstance(other, IDETrashArtifactModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
