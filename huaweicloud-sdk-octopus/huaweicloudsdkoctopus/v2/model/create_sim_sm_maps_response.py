# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSimSmMapsResponse(SdkResponse):

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
        'file': 'FileCreateSrlz',
        'version': 'MapVersionEnum'
    }

    attribute_map = {
        'url': 'url',
        'id': 'id',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'file': 'file',
        'version': 'version'
    }

    def __init__(self, url=None, id=None, created_at=None, updated_at=None, file=None, version=None):
        r"""CreateSimSmMapsResponse

        The model defined in huaweicloud sdk

        :param url: 地址
        :type url: str
        :param id: ID
        :type id: int
        :param created_at: 创建时间
        :type created_at: float
        :param updated_at: 更新时间
        :type updated_at: float
        :param file: 
        :type file: :class:`huaweicloudsdkoctopus.v2.FileCreateSrlz`
        :param version: 
        :type version: :class:`huaweicloudsdkoctopus.v2.MapVersionEnum`
        """
        
        super(CreateSimSmMapsResponse, self).__init__()

        self._url = None
        self._id = None
        self._created_at = None
        self._updated_at = None
        self._file = None
        self._version = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if id is not None:
            self.id = id
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if file is not None:
            self.file = file
        if version is not None:
            self.version = version

    @property
    def url(self):
        r"""Gets the url of this CreateSimSmMapsResponse.

        地址

        :return: The url of this CreateSimSmMapsResponse.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this CreateSimSmMapsResponse.

        地址

        :param url: The url of this CreateSimSmMapsResponse.
        :type url: str
        """
        self._url = url

    @property
    def id(self):
        r"""Gets the id of this CreateSimSmMapsResponse.

        ID

        :return: The id of this CreateSimSmMapsResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CreateSimSmMapsResponse.

        ID

        :param id: The id of this CreateSimSmMapsResponse.
        :type id: int
        """
        self._id = id

    @property
    def created_at(self):
        r"""Gets the created_at of this CreateSimSmMapsResponse.

        创建时间

        :return: The created_at of this CreateSimSmMapsResponse.
        :rtype: float
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this CreateSimSmMapsResponse.

        创建时间

        :param created_at: The created_at of this CreateSimSmMapsResponse.
        :type created_at: float
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this CreateSimSmMapsResponse.

        更新时间

        :return: The updated_at of this CreateSimSmMapsResponse.
        :rtype: float
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this CreateSimSmMapsResponse.

        更新时间

        :param updated_at: The updated_at of this CreateSimSmMapsResponse.
        :type updated_at: float
        """
        self._updated_at = updated_at

    @property
    def file(self):
        r"""Gets the file of this CreateSimSmMapsResponse.

        :return: The file of this CreateSimSmMapsResponse.
        :rtype: :class:`huaweicloudsdkoctopus.v2.FileCreateSrlz`
        """
        return self._file

    @file.setter
    def file(self, file):
        r"""Sets the file of this CreateSimSmMapsResponse.

        :param file: The file of this CreateSimSmMapsResponse.
        :type file: :class:`huaweicloudsdkoctopus.v2.FileCreateSrlz`
        """
        self._file = file

    @property
    def version(self):
        r"""Gets the version of this CreateSimSmMapsResponse.

        :return: The version of this CreateSimSmMapsResponse.
        :rtype: :class:`huaweicloudsdkoctopus.v2.MapVersionEnum`
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this CreateSimSmMapsResponse.

        :param version: The version of this CreateSimSmMapsResponse.
        :type version: :class:`huaweicloudsdkoctopus.v2.MapVersionEnum`
        """
        self._version = version

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
        if not isinstance(other, CreateSimSmMapsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
