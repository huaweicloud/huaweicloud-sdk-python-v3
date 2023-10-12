# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DefaultCertsResource:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'file_name': 'str',
        'file_location': 'str',
        'status': 'str',
        'column': 'str',
        'desc': 'str'
    }

    attribute_map = {
        'file_name': 'fileName',
        'file_location': 'fileLocation',
        'status': 'status',
        'column': 'column',
        'desc': 'desc'
    }

    def __init__(self, file_name=None, file_location=None, status=None, column=None, desc=None):
        """DefaultCertsResource

        The model defined in huaweicloud sdk

        :param file_name: 证书名称。
        :type file_name: str
        :param file_location: 证书路径。
        :type file_location: str
        :param status: 证书状态。
        :type status: str
        :param column: 描述列。
        :type column: str
        :param desc: 证书描述。
        :type desc: str
        """
        
        

        self._file_name = None
        self._file_location = None
        self._status = None
        self._column = None
        self._desc = None
        self.discriminator = None

        if file_name is not None:
            self.file_name = file_name
        if file_location is not None:
            self.file_location = file_location
        if status is not None:
            self.status = status
        if column is not None:
            self.column = column
        if desc is not None:
            self.desc = desc

    @property
    def file_name(self):
        """Gets the file_name of this DefaultCertsResource.

        证书名称。

        :return: The file_name of this DefaultCertsResource.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this DefaultCertsResource.

        证书名称。

        :param file_name: The file_name of this DefaultCertsResource.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def file_location(self):
        """Gets the file_location of this DefaultCertsResource.

        证书路径。

        :return: The file_location of this DefaultCertsResource.
        :rtype: str
        """
        return self._file_location

    @file_location.setter
    def file_location(self, file_location):
        """Sets the file_location of this DefaultCertsResource.

        证书路径。

        :param file_location: The file_location of this DefaultCertsResource.
        :type file_location: str
        """
        self._file_location = file_location

    @property
    def status(self):
        """Gets the status of this DefaultCertsResource.

        证书状态。

        :return: The status of this DefaultCertsResource.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DefaultCertsResource.

        证书状态。

        :param status: The status of this DefaultCertsResource.
        :type status: str
        """
        self._status = status

    @property
    def column(self):
        """Gets the column of this DefaultCertsResource.

        描述列。

        :return: The column of this DefaultCertsResource.
        :rtype: str
        """
        return self._column

    @column.setter
    def column(self, column):
        """Sets the column of this DefaultCertsResource.

        描述列。

        :param column: The column of this DefaultCertsResource.
        :type column: str
        """
        self._column = column

    @property
    def desc(self):
        """Gets the desc of this DefaultCertsResource.

        证书描述。

        :return: The desc of this DefaultCertsResource.
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        """Sets the desc of this DefaultCertsResource.

        证书描述。

        :param desc: The desc of this DefaultCertsResource.
        :type desc: str
        """
        self._desc = desc

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
        if not isinstance(other, DefaultCertsResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
