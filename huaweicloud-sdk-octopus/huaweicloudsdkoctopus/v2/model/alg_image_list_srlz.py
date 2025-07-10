# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AlgImageListSrlz:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'url': 'str',
        'id': 'int',
        'created_at': 'float',
        'updated_at': 'float',
        'type': 'Type87eEnum',
        'version': 'str',
        'algorithm': 'str'
    }

    attribute_map = {
        'url': 'url',
        'id': 'id',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'type': 'type',
        'version': 'version',
        'algorithm': 'algorithm'
    }

    def __init__(self, url=None, id=None, created_at=None, updated_at=None, type=None, version=None, algorithm=None):
        r"""AlgImageListSrlz

        The model defined in huaweicloud sdk

        :param url: 
        :type url: str
        :param id: 
        :type id: int
        :param created_at: 
        :type created_at: float
        :param updated_at: 
        :type updated_at: float
        :param type: 镜像类型  * &#x60;build&#x60; - Build * &#x60;upload&#x60; - Upload
        :type type: :class:`huaweicloudsdkoctopus.v2.Type87eEnum`
        :param version: 镜像版本
        :type version: str
        :param algorithm: 算法
        :type algorithm: str
        """
        
        

        self._url = None
        self._id = None
        self._created_at = None
        self._updated_at = None
        self._type = None
        self._version = None
        self._algorithm = None
        self.discriminator = None

        self.url = url
        self.id = id
        self.created_at = created_at
        self.updated_at = updated_at
        self.type = type
        self.version = version
        self.algorithm = algorithm

    @property
    def url(self):
        r"""Gets the url of this AlgImageListSrlz.

        :return: The url of this AlgImageListSrlz.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this AlgImageListSrlz.

        :param url: The url of this AlgImageListSrlz.
        :type url: str
        """
        self._url = url

    @property
    def id(self):
        r"""Gets the id of this AlgImageListSrlz.

        :return: The id of this AlgImageListSrlz.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this AlgImageListSrlz.

        :param id: The id of this AlgImageListSrlz.
        :type id: int
        """
        self._id = id

    @property
    def created_at(self):
        r"""Gets the created_at of this AlgImageListSrlz.

        :return: The created_at of this AlgImageListSrlz.
        :rtype: float
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this AlgImageListSrlz.

        :param created_at: The created_at of this AlgImageListSrlz.
        :type created_at: float
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this AlgImageListSrlz.

        :return: The updated_at of this AlgImageListSrlz.
        :rtype: float
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this AlgImageListSrlz.

        :param updated_at: The updated_at of this AlgImageListSrlz.
        :type updated_at: float
        """
        self._updated_at = updated_at

    @property
    def type(self):
        r"""Gets the type of this AlgImageListSrlz.

        镜像类型  * `build` - Build * `upload` - Upload

        :return: The type of this AlgImageListSrlz.
        :rtype: :class:`huaweicloudsdkoctopus.v2.Type87eEnum`
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this AlgImageListSrlz.

        镜像类型  * `build` - Build * `upload` - Upload

        :param type: The type of this AlgImageListSrlz.
        :type type: :class:`huaweicloudsdkoctopus.v2.Type87eEnum`
        """
        self._type = type

    @property
    def version(self):
        r"""Gets the version of this AlgImageListSrlz.

        镜像版本

        :return: The version of this AlgImageListSrlz.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this AlgImageListSrlz.

        镜像版本

        :param version: The version of this AlgImageListSrlz.
        :type version: str
        """
        self._version = version

    @property
    def algorithm(self):
        r"""Gets the algorithm of this AlgImageListSrlz.

        算法

        :return: The algorithm of this AlgImageListSrlz.
        :rtype: str
        """
        return self._algorithm

    @algorithm.setter
    def algorithm(self, algorithm):
        r"""Sets the algorithm of this AlgImageListSrlz.

        算法

        :param algorithm: The algorithm of this AlgImageListSrlz.
        :type algorithm: str
        """
        self._algorithm = algorithm

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
        if not isinstance(other, AlgImageListSrlz):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
