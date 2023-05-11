# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AomMappingfilesInfo:

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
        'log_stream_info': 'AomMappingLogStreamInfo'
    }

    attribute_map = {
        'file_name': 'file_name',
        'log_stream_info': 'log_stream_info'
    }

    def __init__(self, file_name=None, log_stream_info=None):
        """AomMappingfilesInfo

        The model defined in huaweicloud sdk

        :param file_name: 路径名
        :type file_name: str
        :param log_stream_info: 
        :type log_stream_info: :class:`huaweicloudsdklts.v2.AomMappingLogStreamInfo`
        """
        
        

        self._file_name = None
        self._log_stream_info = None
        self.discriminator = None

        self.file_name = file_name
        self.log_stream_info = log_stream_info

    @property
    def file_name(self):
        """Gets the file_name of this AomMappingfilesInfo.

        路径名

        :return: The file_name of this AomMappingfilesInfo.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this AomMappingfilesInfo.

        路径名

        :param file_name: The file_name of this AomMappingfilesInfo.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def log_stream_info(self):
        """Gets the log_stream_info of this AomMappingfilesInfo.

        :return: The log_stream_info of this AomMappingfilesInfo.
        :rtype: :class:`huaweicloudsdklts.v2.AomMappingLogStreamInfo`
        """
        return self._log_stream_info

    @log_stream_info.setter
    def log_stream_info(self, log_stream_info):
        """Sets the log_stream_info of this AomMappingfilesInfo.

        :param log_stream_info: The log_stream_info of this AomMappingfilesInfo.
        :type log_stream_info: :class:`huaweicloudsdklts.v2.AomMappingLogStreamInfo`
        """
        self._log_stream_info = log_stream_info

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
        if not isinstance(other, AomMappingfilesInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
