# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UploadByUrlReq:

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
        'object': 'str',
        'url': 'str',
        'file_type': 'str',
        'title': 'str',
        'callback_url': 'str',
        'session_context': 'str'
    }

    attribute_map = {
        'bucket': 'bucket',
        'object': 'object',
        'url': 'url',
        'file_type': 'file_type',
        'title': 'title',
        'callback_url': 'callback_url',
        'session_context': 'session_context'
    }

    def __init__(self, bucket=None, object=None, url=None, file_type=None, title=None, callback_url=None, session_context=None):
        r"""UploadByUrlReq

        The model defined in huaweicloud sdk

        :param bucket: OBS的bucket名称。
        :type bucket: str
        :param object: 文件的存储路径。
        :type object: str
        :param url: 视频源文件URL&lt;/br&gt; 
        :type url: str
        :param file_type: 视频类型&lt;br/&gt; 
        :type file_type: str
        :param title: 媒资标题&lt;/br&gt; 
        :type title: str
        :param callback_url: 回调url 
        :type callback_url: str
        :param session_context: 自定义上下文，回调时会回调给用户，透传信息
        :type session_context: str
        """
        
        

        self._bucket = None
        self._object = None
        self._url = None
        self._file_type = None
        self._title = None
        self._callback_url = None
        self._session_context = None
        self.discriminator = None

        if bucket is not None:
            self.bucket = bucket
        if object is not None:
            self.object = object
        if url is not None:
            self.url = url
        if file_type is not None:
            self.file_type = file_type
        if title is not None:
            self.title = title
        if callback_url is not None:
            self.callback_url = callback_url
        if session_context is not None:
            self.session_context = session_context

    @property
    def bucket(self):
        r"""Gets the bucket of this UploadByUrlReq.

        OBS的bucket名称。

        :return: The bucket of this UploadByUrlReq.
        :rtype: str
        """
        return self._bucket

    @bucket.setter
    def bucket(self, bucket):
        r"""Sets the bucket of this UploadByUrlReq.

        OBS的bucket名称。

        :param bucket: The bucket of this UploadByUrlReq.
        :type bucket: str
        """
        self._bucket = bucket

    @property
    def object(self):
        r"""Gets the object of this UploadByUrlReq.

        文件的存储路径。

        :return: The object of this UploadByUrlReq.
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        r"""Sets the object of this UploadByUrlReq.

        文件的存储路径。

        :param object: The object of this UploadByUrlReq.
        :type object: str
        """
        self._object = object

    @property
    def url(self):
        r"""Gets the url of this UploadByUrlReq.

        视频源文件URL</br> 

        :return: The url of this UploadByUrlReq.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this UploadByUrlReq.

        视频源文件URL</br> 

        :param url: The url of this UploadByUrlReq.
        :type url: str
        """
        self._url = url

    @property
    def file_type(self):
        r"""Gets the file_type of this UploadByUrlReq.

        视频类型<br/> 

        :return: The file_type of this UploadByUrlReq.
        :rtype: str
        """
        return self._file_type

    @file_type.setter
    def file_type(self, file_type):
        r"""Sets the file_type of this UploadByUrlReq.

        视频类型<br/> 

        :param file_type: The file_type of this UploadByUrlReq.
        :type file_type: str
        """
        self._file_type = file_type

    @property
    def title(self):
        r"""Gets the title of this UploadByUrlReq.

        媒资标题</br> 

        :return: The title of this UploadByUrlReq.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this UploadByUrlReq.

        媒资标题</br> 

        :param title: The title of this UploadByUrlReq.
        :type title: str
        """
        self._title = title

    @property
    def callback_url(self):
        r"""Gets the callback_url of this UploadByUrlReq.

        回调url 

        :return: The callback_url of this UploadByUrlReq.
        :rtype: str
        """
        return self._callback_url

    @callback_url.setter
    def callback_url(self, callback_url):
        r"""Sets the callback_url of this UploadByUrlReq.

        回调url 

        :param callback_url: The callback_url of this UploadByUrlReq.
        :type callback_url: str
        """
        self._callback_url = callback_url

    @property
    def session_context(self):
        r"""Gets the session_context of this UploadByUrlReq.

        自定义上下文，回调时会回调给用户，透传信息

        :return: The session_context of this UploadByUrlReq.
        :rtype: str
        """
        return self._session_context

    @session_context.setter
    def session_context(self, session_context):
        r"""Sets the session_context of this UploadByUrlReq.

        自定义上下文，回调时会回调给用户，透传信息

        :param session_context: The session_context of this UploadByUrlReq.
        :type session_context: str
        """
        self._session_context = session_context

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
        if not isinstance(other, UploadByUrlReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
