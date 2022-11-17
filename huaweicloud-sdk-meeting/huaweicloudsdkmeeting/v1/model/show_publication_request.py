# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowPublicationRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_request_id': 'str',
        'accept_language': 'str',
        'id': 'str'
    }

    attribute_map = {
        'x_request_id': 'X-Request-Id',
        'accept_language': 'Accept-Language',
        'id': 'id'
    }

    def __init__(self, x_request_id=None, accept_language=None, id=None):
        """ShowPublicationRequest

        The model defined in huaweicloud sdk

        :param x_request_id: 请求requestId，用来标识一路请求，用于问题跟踪定位，建议使用UUID，若不携带，则后台自动生成。
        :type x_request_id: str
        :param accept_language: 语言参数，默认为中文zh-CN，英文为en-US。
        :type accept_language: str
        :param id: 发布ID。
        :type id: str
        """
        
        

        self._x_request_id = None
        self._accept_language = None
        self._id = None
        self.discriminator = None

        if x_request_id is not None:
            self.x_request_id = x_request_id
        if accept_language is not None:
            self.accept_language = accept_language
        self.id = id

    @property
    def x_request_id(self):
        """Gets the x_request_id of this ShowPublicationRequest.

        请求requestId，用来标识一路请求，用于问题跟踪定位，建议使用UUID，若不携带，则后台自动生成。

        :return: The x_request_id of this ShowPublicationRequest.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this ShowPublicationRequest.

        请求requestId，用来标识一路请求，用于问题跟踪定位，建议使用UUID，若不携带，则后台自动生成。

        :param x_request_id: The x_request_id of this ShowPublicationRequest.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

    @property
    def accept_language(self):
        """Gets the accept_language of this ShowPublicationRequest.

        语言参数，默认为中文zh-CN，英文为en-US。

        :return: The accept_language of this ShowPublicationRequest.
        :rtype: str
        """
        return self._accept_language

    @accept_language.setter
    def accept_language(self, accept_language):
        """Sets the accept_language of this ShowPublicationRequest.

        语言参数，默认为中文zh-CN，英文为en-US。

        :param accept_language: The accept_language of this ShowPublicationRequest.
        :type accept_language: str
        """
        self._accept_language = accept_language

    @property
    def id(self):
        """Gets the id of this ShowPublicationRequest.

        发布ID。

        :return: The id of this ShowPublicationRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowPublicationRequest.

        发布ID。

        :param id: The id of this ShowPublicationRequest.
        :type id: str
        """
        self._id = id

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
        if not isinstance(other, ShowPublicationRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
