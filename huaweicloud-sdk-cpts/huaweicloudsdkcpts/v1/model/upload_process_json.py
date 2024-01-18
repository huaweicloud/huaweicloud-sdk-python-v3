# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UploadProcessJson:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'details': 'list[UploadProcessJsonDetail]',
        'process_status': 'int'
    }

    attribute_map = {
        'details': 'details',
        'process_status': 'process_status'
    }

    def __init__(self, details=None, process_status=None):
        """UploadProcessJson

        The model defined in huaweicloud sdk

        :param details: 工程导入进度明细信息
        :type details: list[:class:`huaweicloudsdkcpts.v1.UploadProcessJsonDetail`]
        :param process_status: 总状态（0：导入中；1：导入完成）
        :type process_status: int
        """
        
        

        self._details = None
        self._process_status = None
        self.discriminator = None

        if details is not None:
            self.details = details
        if process_status is not None:
            self.process_status = process_status

    @property
    def details(self):
        """Gets the details of this UploadProcessJson.

        工程导入进度明细信息

        :return: The details of this UploadProcessJson.
        :rtype: list[:class:`huaweicloudsdkcpts.v1.UploadProcessJsonDetail`]
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this UploadProcessJson.

        工程导入进度明细信息

        :param details: The details of this UploadProcessJson.
        :type details: list[:class:`huaweicloudsdkcpts.v1.UploadProcessJsonDetail`]
        """
        self._details = details

    @property
    def process_status(self):
        """Gets the process_status of this UploadProcessJson.

        总状态（0：导入中；1：导入完成）

        :return: The process_status of this UploadProcessJson.
        :rtype: int
        """
        return self._process_status

    @process_status.setter
    def process_status(self, process_status):
        """Sets the process_status of this UploadProcessJson.

        总状态（0：导入中；1：导入完成）

        :param process_status: The process_status of this UploadProcessJson.
        :type process_status: int
        """
        self._process_status = process_status

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
        if not isinstance(other, UploadProcessJson):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
