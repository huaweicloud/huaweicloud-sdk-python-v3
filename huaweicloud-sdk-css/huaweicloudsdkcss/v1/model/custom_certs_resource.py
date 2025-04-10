# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CustomCertsResource:

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
        'file_name': 'str',
        'file_location': 'str',
        'status': 'str',
        'update_at': 'str'
    }

    attribute_map = {
        'id': 'id',
        'file_name': 'fileName',
        'file_location': 'fileLocation',
        'status': 'status',
        'update_at': 'updateAt'
    }

    def __init__(self, id=None, file_name=None, file_location=None, status=None, update_at=None):
        r"""CustomCertsResource

        The model defined in huaweicloud sdk

        :param id: 证书id。
        :type id: str
        :param file_name: 证书名称。
        :type file_name: str
        :param file_location: 证书路径。
        :type file_location: str
        :param status: 证书状态。
        :type status: str
        :param update_at: 证书上传时间。
        :type update_at: str
        """
        
        

        self._id = None
        self._file_name = None
        self._file_location = None
        self._status = None
        self._update_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if file_name is not None:
            self.file_name = file_name
        if file_location is not None:
            self.file_location = file_location
        if status is not None:
            self.status = status
        if update_at is not None:
            self.update_at = update_at

    @property
    def id(self):
        r"""Gets the id of this CustomCertsResource.

        证书id。

        :return: The id of this CustomCertsResource.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CustomCertsResource.

        证书id。

        :param id: The id of this CustomCertsResource.
        :type id: str
        """
        self._id = id

    @property
    def file_name(self):
        r"""Gets the file_name of this CustomCertsResource.

        证书名称。

        :return: The file_name of this CustomCertsResource.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        r"""Sets the file_name of this CustomCertsResource.

        证书名称。

        :param file_name: The file_name of this CustomCertsResource.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def file_location(self):
        r"""Gets the file_location of this CustomCertsResource.

        证书路径。

        :return: The file_location of this CustomCertsResource.
        :rtype: str
        """
        return self._file_location

    @file_location.setter
    def file_location(self, file_location):
        r"""Sets the file_location of this CustomCertsResource.

        证书路径。

        :param file_location: The file_location of this CustomCertsResource.
        :type file_location: str
        """
        self._file_location = file_location

    @property
    def status(self):
        r"""Gets the status of this CustomCertsResource.

        证书状态。

        :return: The status of this CustomCertsResource.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CustomCertsResource.

        证书状态。

        :param status: The status of this CustomCertsResource.
        :type status: str
        """
        self._status = status

    @property
    def update_at(self):
        r"""Gets the update_at of this CustomCertsResource.

        证书上传时间。

        :return: The update_at of this CustomCertsResource.
        :rtype: str
        """
        return self._update_at

    @update_at.setter
    def update_at(self, update_at):
        r"""Sets the update_at of this CustomCertsResource.

        证书上传时间。

        :param update_at: The update_at of this CustomCertsResource.
        :type update_at: str
        """
        self._update_at = update_at

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
        if not isinstance(other, CustomCertsResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
