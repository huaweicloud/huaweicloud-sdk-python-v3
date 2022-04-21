# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFile:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'list_file_key': 'str',
        'obs_bucket': 'str'
    }

    attribute_map = {
        'list_file_key': 'list_file_key',
        'obs_bucket': 'obs_bucket'
    }

    def __init__(self, list_file_key=None, obs_bucket=None):
        """ListFile

        The model defined in huaweicloud sdk

        :param list_file_key: 对象列表文件或URL列表文件对象名。
        :type list_file_key: str
        :param obs_bucket: 存放对象列表文件的OBS桶名。  请确保与目的端桶处于同一区域，否则将导致任务创建失败。
        :type obs_bucket: str
        """
        
        

        self._list_file_key = None
        self._obs_bucket = None
        self.discriminator = None

        self.list_file_key = list_file_key
        self.obs_bucket = obs_bucket

    @property
    def list_file_key(self):
        """Gets the list_file_key of this ListFile.

        对象列表文件或URL列表文件对象名。

        :return: The list_file_key of this ListFile.
        :rtype: str
        """
        return self._list_file_key

    @list_file_key.setter
    def list_file_key(self, list_file_key):
        """Sets the list_file_key of this ListFile.

        对象列表文件或URL列表文件对象名。

        :param list_file_key: The list_file_key of this ListFile.
        :type list_file_key: str
        """
        self._list_file_key = list_file_key

    @property
    def obs_bucket(self):
        """Gets the obs_bucket of this ListFile.

        存放对象列表文件的OBS桶名。  请确保与目的端桶处于同一区域，否则将导致任务创建失败。

        :return: The obs_bucket of this ListFile.
        :rtype: str
        """
        return self._obs_bucket

    @obs_bucket.setter
    def obs_bucket(self, obs_bucket):
        """Sets the obs_bucket of this ListFile.

        存放对象列表文件的OBS桶名。  请确保与目的端桶处于同一区域，否则将导致任务创建失败。

        :param obs_bucket: The obs_bucket of this ListFile.
        :type obs_bucket: str
        """
        self._obs_bucket = obs_bucket

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
        if not isinstance(other, ListFile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
