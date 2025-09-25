# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CertsRecordsDatastore:

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
        'status': 'str',
        'file_location': 'str',
        'file_name': 'bool',
        'update_at': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'status': 'status',
        'file_location': 'fileLocation',
        'file_name': 'fileName',
        'update_at': 'updateAt'
    }

    def __init__(self, id=None, status=None, file_location=None, file_name=None, update_at=None):
        r"""CertsRecordsDatastore

        The model defined in huaweicloud sdk

        :param id: 证书记录ID。
        :type id: str
        :param status: 证书状态。
        :type status: str
        :param file_location: 证书记录文件位置。
        :type file_location: str
        :param file_name: 证书记录文件名称。
        :type file_name: bool
        :param update_at: 证书记录更新时间。
        :type update_at: bool
        """
        
        

        self._id = None
        self._status = None
        self._file_location = None
        self._file_name = None
        self._update_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if status is not None:
            self.status = status
        if file_location is not None:
            self.file_location = file_location
        if file_name is not None:
            self.file_name = file_name
        if update_at is not None:
            self.update_at = update_at

    @property
    def id(self):
        r"""Gets the id of this CertsRecordsDatastore.

        证书记录ID。

        :return: The id of this CertsRecordsDatastore.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CertsRecordsDatastore.

        证书记录ID。

        :param id: The id of this CertsRecordsDatastore.
        :type id: str
        """
        self._id = id

    @property
    def status(self):
        r"""Gets the status of this CertsRecordsDatastore.

        证书状态。

        :return: The status of this CertsRecordsDatastore.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CertsRecordsDatastore.

        证书状态。

        :param status: The status of this CertsRecordsDatastore.
        :type status: str
        """
        self._status = status

    @property
    def file_location(self):
        r"""Gets the file_location of this CertsRecordsDatastore.

        证书记录文件位置。

        :return: The file_location of this CertsRecordsDatastore.
        :rtype: str
        """
        return self._file_location

    @file_location.setter
    def file_location(self, file_location):
        r"""Sets the file_location of this CertsRecordsDatastore.

        证书记录文件位置。

        :param file_location: The file_location of this CertsRecordsDatastore.
        :type file_location: str
        """
        self._file_location = file_location

    @property
    def file_name(self):
        r"""Gets the file_name of this CertsRecordsDatastore.

        证书记录文件名称。

        :return: The file_name of this CertsRecordsDatastore.
        :rtype: bool
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        r"""Sets the file_name of this CertsRecordsDatastore.

        证书记录文件名称。

        :param file_name: The file_name of this CertsRecordsDatastore.
        :type file_name: bool
        """
        self._file_name = file_name

    @property
    def update_at(self):
        r"""Gets the update_at of this CertsRecordsDatastore.

        证书记录更新时间。

        :return: The update_at of this CertsRecordsDatastore.
        :rtype: bool
        """
        return self._update_at

    @update_at.setter
    def update_at(self, update_at):
        r"""Sets the update_at of this CertsRecordsDatastore.

        证书记录更新时间。

        :param update_at: The update_at of this CertsRecordsDatastore.
        :type update_at: bool
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
        if not isinstance(other, CertsRecordsDatastore):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
