# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowQaPairDetailRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_service_key': 'str',
        'x_site': 'str',
        'x_language': 'str',
        'qa_pair_id': 'str'
    }

    attribute_map = {
        'x_service_key': 'x-service-key',
        'x_site': 'x-site',
        'x_language': 'x-language',
        'qa_pair_id': 'qa_pair_id'
    }

    def __init__(self, x_service_key=None, x_site=None, x_language=None, qa_pair_id=None):
        """ShowQaPairDetailRequest

        The model defined in huaweicloud sdk

        :param x_service_key: 调用智能客服服务标志。
        :type x_service_key: str
        :param x_site: 站点标记，0-中国站  1-国际站
        :type x_site: str
        :param x_language: 区域语言简写，en-us  zh-cn
        :type x_language: str
        :param qa_pair_id: 语料Id
        :type qa_pair_id: str
        """
        
        

        self._x_service_key = None
        self._x_site = None
        self._x_language = None
        self._qa_pair_id = None
        self.discriminator = None

        self.x_service_key = x_service_key
        if x_site is not None:
            self.x_site = x_site
        if x_language is not None:
            self.x_language = x_language
        self.qa_pair_id = qa_pair_id

    @property
    def x_service_key(self):
        """Gets the x_service_key of this ShowQaPairDetailRequest.

        调用智能客服服务标志。

        :return: The x_service_key of this ShowQaPairDetailRequest.
        :rtype: str
        """
        return self._x_service_key

    @x_service_key.setter
    def x_service_key(self, x_service_key):
        """Sets the x_service_key of this ShowQaPairDetailRequest.

        调用智能客服服务标志。

        :param x_service_key: The x_service_key of this ShowQaPairDetailRequest.
        :type x_service_key: str
        """
        self._x_service_key = x_service_key

    @property
    def x_site(self):
        """Gets the x_site of this ShowQaPairDetailRequest.

        站点标记，0-中国站  1-国际站

        :return: The x_site of this ShowQaPairDetailRequest.
        :rtype: str
        """
        return self._x_site

    @x_site.setter
    def x_site(self, x_site):
        """Sets the x_site of this ShowQaPairDetailRequest.

        站点标记，0-中国站  1-国际站

        :param x_site: The x_site of this ShowQaPairDetailRequest.
        :type x_site: str
        """
        self._x_site = x_site

    @property
    def x_language(self):
        """Gets the x_language of this ShowQaPairDetailRequest.

        区域语言简写，en-us  zh-cn

        :return: The x_language of this ShowQaPairDetailRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this ShowQaPairDetailRequest.

        区域语言简写，en-us  zh-cn

        :param x_language: The x_language of this ShowQaPairDetailRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def qa_pair_id(self):
        """Gets the qa_pair_id of this ShowQaPairDetailRequest.

        语料Id

        :return: The qa_pair_id of this ShowQaPairDetailRequest.
        :rtype: str
        """
        return self._qa_pair_id

    @qa_pair_id.setter
    def qa_pair_id(self, qa_pair_id):
        """Sets the qa_pair_id of this ShowQaPairDetailRequest.

        语料Id

        :param qa_pair_id: The qa_pair_id of this ShowQaPairDetailRequest.
        :type qa_pair_id: str
        """
        self._qa_pair_id = qa_pair_id

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
        if not isinstance(other, ShowQaPairDetailRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
