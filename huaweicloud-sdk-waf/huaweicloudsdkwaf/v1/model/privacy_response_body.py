# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PrivacyResponseBody:


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
        'policyid': 'str',
        'url': 'str',
        'category': 'str',
        'index': 'str'
    }

    attribute_map = {
        'id': 'id',
        'policyid': 'policyid',
        'url': 'url',
        'category': 'category',
        'index': 'index'
    }

    def __init__(self, id=None, policyid=None, url=None, category=None, index=None):
        """PrivacyResponseBody - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._policyid = None
        self._url = None
        self._category = None
        self._index = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if policyid is not None:
            self.policyid = policyid
        if url is not None:
            self.url = url
        if category is not None:
            self.category = category
        if index is not None:
            self.index = index

    @property
    def id(self):
        """Gets the id of this PrivacyResponseBody.

        规则id

        :return: The id of this PrivacyResponseBody.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PrivacyResponseBody.

        规则id

        :param id: The id of this PrivacyResponseBody.
        :type: str
        """
        self._id = id

    @property
    def policyid(self):
        """Gets the policyid of this PrivacyResponseBody.

        策略id

        :return: The policyid of this PrivacyResponseBody.
        :rtype: str
        """
        return self._policyid

    @policyid.setter
    def policyid(self, policyid):
        """Sets the policyid of this PrivacyResponseBody.

        策略id

        :param policyid: The policyid of this PrivacyResponseBody.
        :type: str
        """
        self._policyid = policyid

    @property
    def url(self):
        """Gets the url of this PrivacyResponseBody.

        隐私屏蔽规则应用的url

        :return: The url of this PrivacyResponseBody.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this PrivacyResponseBody.

        隐私屏蔽规则应用的url

        :param url: The url of this PrivacyResponseBody.
        :type: str
        """
        self._url = url

    @property
    def category(self):
        """Gets the category of this PrivacyResponseBody.

        屏蔽字段

        :return: The category of this PrivacyResponseBody.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this PrivacyResponseBody.

        屏蔽字段

        :param category: The category of this PrivacyResponseBody.
        :type: str
        """
        self._category = category

    @property
    def index(self):
        """Gets the index of this PrivacyResponseBody.

        屏蔽字段名

        :return: The index of this PrivacyResponseBody.
        :rtype: str
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this PrivacyResponseBody.

        屏蔽字段名

        :param index: The index of this PrivacyResponseBody.
        :type: str
        """
        self._index = index

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
        if not isinstance(other, PrivacyResponseBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
