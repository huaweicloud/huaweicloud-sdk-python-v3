# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DownloadDbObjectTemplateRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_id': 'str',
        'x_language': 'str',
        'file_import_db_level': 'str'
    }

    attribute_map = {
        'job_id': 'job_id',
        'x_language': 'X-Language',
        'file_import_db_level': 'file_import_db_level'
    }

    def __init__(self, job_id=None, x_language=None, file_import_db_level=None):
        """DownloadDbObjectTemplateRequest

        The model defined in huaweicloud sdk

        :param job_id: 任务ID。
        :type job_id: str
        :param x_language: 请求语言类型。
        :type x_language: str
        :param file_import_db_level: 文件模板支持数据同步级别，不填默认为table表级。 - database：库级 - table：表级
        :type file_import_db_level: str
        """
        
        

        self._job_id = None
        self._x_language = None
        self._file_import_db_level = None
        self.discriminator = None

        self.job_id = job_id
        if x_language is not None:
            self.x_language = x_language
        if file_import_db_level is not None:
            self.file_import_db_level = file_import_db_level

    @property
    def job_id(self):
        """Gets the job_id of this DownloadDbObjectTemplateRequest.

        任务ID。

        :return: The job_id of this DownloadDbObjectTemplateRequest.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this DownloadDbObjectTemplateRequest.

        任务ID。

        :param job_id: The job_id of this DownloadDbObjectTemplateRequest.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def x_language(self):
        """Gets the x_language of this DownloadDbObjectTemplateRequest.

        请求语言类型。

        :return: The x_language of this DownloadDbObjectTemplateRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this DownloadDbObjectTemplateRequest.

        请求语言类型。

        :param x_language: The x_language of this DownloadDbObjectTemplateRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def file_import_db_level(self):
        """Gets the file_import_db_level of this DownloadDbObjectTemplateRequest.

        文件模板支持数据同步级别，不填默认为table表级。 - database：库级 - table：表级

        :return: The file_import_db_level of this DownloadDbObjectTemplateRequest.
        :rtype: str
        """
        return self._file_import_db_level

    @file_import_db_level.setter
    def file_import_db_level(self, file_import_db_level):
        """Sets the file_import_db_level of this DownloadDbObjectTemplateRequest.

        文件模板支持数据同步级别，不填默认为table表级。 - database：库级 - table：表级

        :param file_import_db_level: The file_import_db_level of this DownloadDbObjectTemplateRequest.
        :type file_import_db_level: str
        """
        self._file_import_db_level = file_import_db_level

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
        if not isinstance(other, DownloadDbObjectTemplateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
