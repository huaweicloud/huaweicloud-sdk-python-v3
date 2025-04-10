# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OutputObs:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'bucket': 'str',
        'path': 'str'
    }

    attribute_map = {
        'bucket': 'bucket',
        'path': 'path'
    }

    def __init__(self, bucket=None, path=None):
        r"""OutputObs

        The model defined in huaweicloud sdk

        :param bucket: 存储结果文件的OBS桶名。
        :type bucket: str
        :param path: 结果文件的OBS桶内路径，例如“output/”。
        :type path: str
        """
        
        

        self._bucket = None
        self._path = None
        self.discriminator = None

        if bucket is not None:
            self.bucket = bucket
        if path is not None:
            self.path = path

    @property
    def bucket(self):
        r"""Gets the bucket of this OutputObs.

        存储结果文件的OBS桶名。

        :return: The bucket of this OutputObs.
        :rtype: str
        """
        return self._bucket

    @bucket.setter
    def bucket(self, bucket):
        r"""Sets the bucket of this OutputObs.

        存储结果文件的OBS桶名。

        :param bucket: The bucket of this OutputObs.
        :type bucket: str
        """
        self._bucket = bucket

    @property
    def path(self):
        r"""Gets the path of this OutputObs.

        结果文件的OBS桶内路径，例如“output/”。

        :return: The path of this OutputObs.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this OutputObs.

        结果文件的OBS桶内路径，例如“output/”。

        :param path: The path of this OutputObs.
        :type path: str
        """
        self._path = path

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
        if not isinstance(other, OutputObs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
