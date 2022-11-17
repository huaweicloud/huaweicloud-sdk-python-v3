# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UploadAsset:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'url': 'str',
        'asset_id': 'str',
        'error_code': 'str',
        'error_msg': 'str'
    }

    attribute_map = {
        'url': 'url',
        'asset_id': 'asset_id',
        'error_code': 'error_code',
        'error_msg': 'error_msg'
    }

    def __init__(self, url=None, asset_id=None, error_code=None, error_msg=None):
        """UploadAsset

        The model defined in huaweicloud sdk

        :param url: 媒资所在url 
        :type url: str
        :param asset_id: 新创建媒资的媒资id 
        :type asset_id: str
        :param error_code: 错误码。 
        :type error_code: str
        :param error_msg: 错误描述。 
        :type error_msg: str
        """
        
        

        self._url = None
        self._asset_id = None
        self._error_code = None
        self._error_msg = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if asset_id is not None:
            self.asset_id = asset_id
        if error_code is not None:
            self.error_code = error_code
        if error_msg is not None:
            self.error_msg = error_msg

    @property
    def url(self):
        """Gets the url of this UploadAsset.

        媒资所在url 

        :return: The url of this UploadAsset.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this UploadAsset.

        媒资所在url 

        :param url: The url of this UploadAsset.
        :type url: str
        """
        self._url = url

    @property
    def asset_id(self):
        """Gets the asset_id of this UploadAsset.

        新创建媒资的媒资id 

        :return: The asset_id of this UploadAsset.
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        """Sets the asset_id of this UploadAsset.

        新创建媒资的媒资id 

        :param asset_id: The asset_id of this UploadAsset.
        :type asset_id: str
        """
        self._asset_id = asset_id

    @property
    def error_code(self):
        """Gets the error_code of this UploadAsset.

        错误码。 

        :return: The error_code of this UploadAsset.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this UploadAsset.

        错误码。 

        :param error_code: The error_code of this UploadAsset.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_msg(self):
        """Gets the error_msg of this UploadAsset.

        错误描述。 

        :return: The error_msg of this UploadAsset.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        """Sets the error_msg of this UploadAsset.

        错误描述。 

        :param error_msg: The error_msg of this UploadAsset.
        :type error_msg: str
        """
        self._error_msg = error_msg

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
        if not isinstance(other, UploadAsset):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
