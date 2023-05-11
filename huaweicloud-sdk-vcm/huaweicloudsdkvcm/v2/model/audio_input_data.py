# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AudioInputData:

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
        'path': 'str',
        'url': 'str'
    }

    attribute_map = {
        'bucket': 'bucket',
        'path': 'path',
        'url': 'url'
    }

    def __init__(self, bucket=None, path=None, url=None):
        """AudioInputData

        The model defined in huaweicloud sdk

        :param bucket: type为obs时输入参数  OBS桶名称。 
        :type bucket: str
        :param path: type为obs时输入参数  OBS桶内的路径，例如“output/c1.mp4”。 
        :type path: str
        :param url: type为url时输入参数  视频数据的URL，目前支持OBS URL，且需要设置该URL对匿名用户可读权限。 
        :type url: str
        """
        
        

        self._bucket = None
        self._path = None
        self._url = None
        self.discriminator = None

        if bucket is not None:
            self.bucket = bucket
        if path is not None:
            self.path = path
        if url is not None:
            self.url = url

    @property
    def bucket(self):
        """Gets the bucket of this AudioInputData.

        type为obs时输入参数  OBS桶名称。 

        :return: The bucket of this AudioInputData.
        :rtype: str
        """
        return self._bucket

    @bucket.setter
    def bucket(self, bucket):
        """Sets the bucket of this AudioInputData.

        type为obs时输入参数  OBS桶名称。 

        :param bucket: The bucket of this AudioInputData.
        :type bucket: str
        """
        self._bucket = bucket

    @property
    def path(self):
        """Gets the path of this AudioInputData.

        type为obs时输入参数  OBS桶内的路径，例如“output/c1.mp4”。 

        :return: The path of this AudioInputData.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this AudioInputData.

        type为obs时输入参数  OBS桶内的路径，例如“output/c1.mp4”。 

        :param path: The path of this AudioInputData.
        :type path: str
        """
        self._path = path

    @property
    def url(self):
        """Gets the url of this AudioInputData.

        type为url时输入参数  视频数据的URL，目前支持OBS URL，且需要设置该URL对匿名用户可读权限。 

        :return: The url of this AudioInputData.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this AudioInputData.

        type为url时输入参数  视频数据的URL，目前支持OBS URL，且需要设置该URL对匿名用户可读权限。 

        :param url: The url of this AudioInputData.
        :type url: str
        """
        self._url = url

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
        if not isinstance(other, AudioInputData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
