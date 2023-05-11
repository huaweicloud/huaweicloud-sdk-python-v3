# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExecuteUploadImageResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'url': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'url': 'url'
    }

    def __init__(self, id=None, name=None, url=None):
        """ExecuteUploadImageResponse

        The model defined in huaweicloud sdk

        :param id: 图片id
        :type id: str
        :param name: 
        :type name: str
        :param url: 访问地址
        :type url: str
        """
        
        super(ExecuteUploadImageResponse, self).__init__()

        self._id = None
        self._name = None
        self._url = None
        self.discriminator = None

        self.id = id
        if name is not None:
            self.name = name
        self.url = url

    @property
    def id(self):
        """Gets the id of this ExecuteUploadImageResponse.

        图片id

        :return: The id of this ExecuteUploadImageResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ExecuteUploadImageResponse.

        图片id

        :param id: The id of this ExecuteUploadImageResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ExecuteUploadImageResponse.

        

        :return: The name of this ExecuteUploadImageResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ExecuteUploadImageResponse.

        

        :param name: The name of this ExecuteUploadImageResponse.
        :type name: str
        """
        self._name = name

    @property
    def url(self):
        """Gets the url of this ExecuteUploadImageResponse.

        访问地址

        :return: The url of this ExecuteUploadImageResponse.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this ExecuteUploadImageResponse.

        访问地址

        :param url: The url of this ExecuteUploadImageResponse.
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
        if not isinstance(other, ExecuteUploadImageResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
