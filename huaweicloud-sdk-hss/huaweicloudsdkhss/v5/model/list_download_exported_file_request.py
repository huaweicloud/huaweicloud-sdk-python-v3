# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDownloadExportedFileRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'file_id': 'str',
        'region': 'str',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'file_id': 'file_id',
        'region': 'region',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, file_id=None, region=None, enterprise_project_id=None):
        """ListDownloadExportedFileRequest

        The model defined in huaweicloud sdk

        :param file_id: 文件id
        :type file_id: str
        :param region: Region Id
        :type region: str
        :param enterprise_project_id: 企业项目ID
        :type enterprise_project_id: str
        """
        
        

        self._file_id = None
        self._region = None
        self._enterprise_project_id = None
        self.discriminator = None

        self.file_id = file_id
        self.region = region
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def file_id(self):
        """Gets the file_id of this ListDownloadExportedFileRequest.

        文件id

        :return: The file_id of this ListDownloadExportedFileRequest.
        :rtype: str
        """
        return self._file_id

    @file_id.setter
    def file_id(self, file_id):
        """Sets the file_id of this ListDownloadExportedFileRequest.

        文件id

        :param file_id: The file_id of this ListDownloadExportedFileRequest.
        :type file_id: str
        """
        self._file_id = file_id

    @property
    def region(self):
        """Gets the region of this ListDownloadExportedFileRequest.

        Region Id

        :return: The region of this ListDownloadExportedFileRequest.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this ListDownloadExportedFileRequest.

        Region Id

        :param region: The region of this ListDownloadExportedFileRequest.
        :type region: str
        """
        self._region = region

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListDownloadExportedFileRequest.

        企业项目ID

        :return: The enterprise_project_id of this ListDownloadExportedFileRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListDownloadExportedFileRequest.

        企业项目ID

        :param enterprise_project_id: The enterprise_project_id of this ListDownloadExportedFileRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, ListDownloadExportedFileRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
