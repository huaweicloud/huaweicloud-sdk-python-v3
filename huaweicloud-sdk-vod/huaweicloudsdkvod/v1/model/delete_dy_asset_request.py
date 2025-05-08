# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteDyAssetRequest:

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
        'object': 'list[str]',
        'callback_url': 'str',
        'session_context': 'str'
    }

    attribute_map = {
        'bucket': 'bucket',
        'object': 'object',
        'callback_url': 'callback_url',
        'session_context': 'session_context'
    }

    def __init__(self, bucket=None, object=None, callback_url=None, session_context=None):
        r"""DeleteDyAssetRequest

        The model defined in huaweicloud sdk

        :param bucket: obs桶名称
        :type bucket: str
        :param object: obs文件路径，不包含桶名
        :type object: list[str]
        :param callback_url: 回调地址
        :type callback_url: str
        :param session_context: 用户透传信息
        :type session_context: str
        """
        
        

        self._bucket = None
        self._object = None
        self._callback_url = None
        self._session_context = None
        self.discriminator = None

        self.bucket = bucket
        self.object = object
        if callback_url is not None:
            self.callback_url = callback_url
        if session_context is not None:
            self.session_context = session_context

    @property
    def bucket(self):
        r"""Gets the bucket of this DeleteDyAssetRequest.

        obs桶名称

        :return: The bucket of this DeleteDyAssetRequest.
        :rtype: str
        """
        return self._bucket

    @bucket.setter
    def bucket(self, bucket):
        r"""Sets the bucket of this DeleteDyAssetRequest.

        obs桶名称

        :param bucket: The bucket of this DeleteDyAssetRequest.
        :type bucket: str
        """
        self._bucket = bucket

    @property
    def object(self):
        r"""Gets the object of this DeleteDyAssetRequest.

        obs文件路径，不包含桶名

        :return: The object of this DeleteDyAssetRequest.
        :rtype: list[str]
        """
        return self._object

    @object.setter
    def object(self, object):
        r"""Sets the object of this DeleteDyAssetRequest.

        obs文件路径，不包含桶名

        :param object: The object of this DeleteDyAssetRequest.
        :type object: list[str]
        """
        self._object = object

    @property
    def callback_url(self):
        r"""Gets the callback_url of this DeleteDyAssetRequest.

        回调地址

        :return: The callback_url of this DeleteDyAssetRequest.
        :rtype: str
        """
        return self._callback_url

    @callback_url.setter
    def callback_url(self, callback_url):
        r"""Sets the callback_url of this DeleteDyAssetRequest.

        回调地址

        :param callback_url: The callback_url of this DeleteDyAssetRequest.
        :type callback_url: str
        """
        self._callback_url = callback_url

    @property
    def session_context(self):
        r"""Gets the session_context of this DeleteDyAssetRequest.

        用户透传信息

        :return: The session_context of this DeleteDyAssetRequest.
        :rtype: str
        """
        return self._session_context

    @session_context.setter
    def session_context(self, session_context):
        r"""Sets the session_context of this DeleteDyAssetRequest.

        用户透传信息

        :param session_context: The session_context of this DeleteDyAssetRequest.
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
        if not isinstance(other, DeleteDyAssetRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
