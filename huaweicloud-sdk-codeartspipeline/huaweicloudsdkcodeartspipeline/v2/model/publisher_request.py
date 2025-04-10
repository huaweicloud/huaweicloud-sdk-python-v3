# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PublisherRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'user_id': 'str',
        'description': 'str',
        'logo_url': 'str',
        'website': 'str',
        'support_url': 'str',
        'source_url': 'str',
        'en_name': 'str',
        'publisher_unique_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'user_id': 'user_id',
        'description': 'description',
        'logo_url': 'logo_url',
        'website': 'website',
        'support_url': 'support_url',
        'source_url': 'source_url',
        'en_name': 'en_name',
        'publisher_unique_id': 'publisher_unique_id'
    }

    def __init__(self, name=None, user_id=None, description=None, logo_url=None, website=None, support_url=None, source_url=None, en_name=None, publisher_unique_id=None):
        r"""PublisherRequest

        The model defined in huaweicloud sdk

        :param name: 名称
        :type name: str
        :param user_id: 用户ID
        :type user_id: str
        :param description: 描述
        :type description: str
        :param logo_url: 图标URL
        :type logo_url: str
        :param website: 网页地址
        :type website: str
        :param support_url: 地址
        :type support_url: str
        :param source_url: 地址
        :type source_url: str
        :param en_name: 英文名
        :type en_name: str
        :param publisher_unique_id: 唯一ID
        :type publisher_unique_id: str
        """
        
        

        self._name = None
        self._user_id = None
        self._description = None
        self._logo_url = None
        self._website = None
        self._support_url = None
        self._source_url = None
        self._en_name = None
        self._publisher_unique_id = None
        self.discriminator = None

        self.name = name
        if user_id is not None:
            self.user_id = user_id
        if description is not None:
            self.description = description
        if logo_url is not None:
            self.logo_url = logo_url
        if website is not None:
            self.website = website
        self.support_url = support_url
        if source_url is not None:
            self.source_url = source_url
        self.en_name = en_name
        if publisher_unique_id is not None:
            self.publisher_unique_id = publisher_unique_id

    @property
    def name(self):
        r"""Gets the name of this PublisherRequest.

        名称

        :return: The name of this PublisherRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this PublisherRequest.

        名称

        :param name: The name of this PublisherRequest.
        :type name: str
        """
        self._name = name

    @property
    def user_id(self):
        r"""Gets the user_id of this PublisherRequest.

        用户ID

        :return: The user_id of this PublisherRequest.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this PublisherRequest.

        用户ID

        :param user_id: The user_id of this PublisherRequest.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def description(self):
        r"""Gets the description of this PublisherRequest.

        描述

        :return: The description of this PublisherRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this PublisherRequest.

        描述

        :param description: The description of this PublisherRequest.
        :type description: str
        """
        self._description = description

    @property
    def logo_url(self):
        r"""Gets the logo_url of this PublisherRequest.

        图标URL

        :return: The logo_url of this PublisherRequest.
        :rtype: str
        """
        return self._logo_url

    @logo_url.setter
    def logo_url(self, logo_url):
        r"""Sets the logo_url of this PublisherRequest.

        图标URL

        :param logo_url: The logo_url of this PublisherRequest.
        :type logo_url: str
        """
        self._logo_url = logo_url

    @property
    def website(self):
        r"""Gets the website of this PublisherRequest.

        网页地址

        :return: The website of this PublisherRequest.
        :rtype: str
        """
        return self._website

    @website.setter
    def website(self, website):
        r"""Sets the website of this PublisherRequest.

        网页地址

        :param website: The website of this PublisherRequest.
        :type website: str
        """
        self._website = website

    @property
    def support_url(self):
        r"""Gets the support_url of this PublisherRequest.

        地址

        :return: The support_url of this PublisherRequest.
        :rtype: str
        """
        return self._support_url

    @support_url.setter
    def support_url(self, support_url):
        r"""Sets the support_url of this PublisherRequest.

        地址

        :param support_url: The support_url of this PublisherRequest.
        :type support_url: str
        """
        self._support_url = support_url

    @property
    def source_url(self):
        r"""Gets the source_url of this PublisherRequest.

        地址

        :return: The source_url of this PublisherRequest.
        :rtype: str
        """
        return self._source_url

    @source_url.setter
    def source_url(self, source_url):
        r"""Sets the source_url of this PublisherRequest.

        地址

        :param source_url: The source_url of this PublisherRequest.
        :type source_url: str
        """
        self._source_url = source_url

    @property
    def en_name(self):
        r"""Gets the en_name of this PublisherRequest.

        英文名

        :return: The en_name of this PublisherRequest.
        :rtype: str
        """
        return self._en_name

    @en_name.setter
    def en_name(self, en_name):
        r"""Sets the en_name of this PublisherRequest.

        英文名

        :param en_name: The en_name of this PublisherRequest.
        :type en_name: str
        """
        self._en_name = en_name

    @property
    def publisher_unique_id(self):
        r"""Gets the publisher_unique_id of this PublisherRequest.

        唯一ID

        :return: The publisher_unique_id of this PublisherRequest.
        :rtype: str
        """
        return self._publisher_unique_id

    @publisher_unique_id.setter
    def publisher_unique_id(self, publisher_unique_id):
        r"""Sets the publisher_unique_id of this PublisherRequest.

        唯一ID

        :param publisher_unique_id: The publisher_unique_id of this PublisherRequest.
        :type publisher_unique_id: str
        """
        self._publisher_unique_id = publisher_unique_id

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
        if not isinstance(other, PublisherRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
