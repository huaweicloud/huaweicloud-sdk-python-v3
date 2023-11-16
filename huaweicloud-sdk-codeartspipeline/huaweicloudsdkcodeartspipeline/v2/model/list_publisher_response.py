# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPublisherResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'publisher_unique_id': 'str',
        'user_id': 'str',
        'tenant_id': 'str',
        'description': 'str',
        'logo_url': 'str',
        'website': 'str',
        'support_url': 'str',
        'source_url': 'str',
        'en_name': 'str',
        'name': 'str',
        'auth_status': 'str',
        'is_delete': 'int',
        'last_update_user_name': 'str',
        'last_update_user_id': 'str',
        'last_update_time': 'str'
    }

    attribute_map = {
        'publisher_unique_id': 'publisher_unique_id',
        'user_id': 'user_id',
        'tenant_id': 'tenant_id',
        'description': 'description',
        'logo_url': 'logo_url',
        'website': 'website',
        'support_url': 'support_url',
        'source_url': 'source_url',
        'en_name': 'en_name',
        'name': 'name',
        'auth_status': 'auth_status',
        'is_delete': 'is_delete',
        'last_update_user_name': 'last_update_user_name',
        'last_update_user_id': 'last_update_user_id',
        'last_update_time': 'last_update_time'
    }

    def __init__(self, publisher_unique_id=None, user_id=None, tenant_id=None, description=None, logo_url=None, website=None, support_url=None, source_url=None, en_name=None, name=None, auth_status=None, is_delete=None, last_update_user_name=None, last_update_user_id=None, last_update_time=None):
        """ListPublisherResponse

        The model defined in huaweicloud sdk

        :param publisher_unique_id: 发布商ID
        :type publisher_unique_id: str
        :param user_id: 用户ID
        :type user_id: str
        :param tenant_id: 租户ID
        :type tenant_id: str
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
        :param name: 名称
        :type name: str
        :param auth_status: 授权状态
        :type auth_status: str
        :param is_delete: 是否删除
        :type is_delete: int
        :param last_update_user_name: 最后更新人
        :type last_update_user_name: str
        :param last_update_user_id: 最后更新人ID
        :type last_update_user_id: str
        :param last_update_time: 最后更新时间
        :type last_update_time: str
        """
        
        super(ListPublisherResponse, self).__init__()

        self._publisher_unique_id = None
        self._user_id = None
        self._tenant_id = None
        self._description = None
        self._logo_url = None
        self._website = None
        self._support_url = None
        self._source_url = None
        self._en_name = None
        self._name = None
        self._auth_status = None
        self._is_delete = None
        self._last_update_user_name = None
        self._last_update_user_id = None
        self._last_update_time = None
        self.discriminator = None

        if publisher_unique_id is not None:
            self.publisher_unique_id = publisher_unique_id
        if user_id is not None:
            self.user_id = user_id
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if description is not None:
            self.description = description
        if logo_url is not None:
            self.logo_url = logo_url
        if website is not None:
            self.website = website
        if support_url is not None:
            self.support_url = support_url
        if source_url is not None:
            self.source_url = source_url
        if en_name is not None:
            self.en_name = en_name
        if name is not None:
            self.name = name
        if auth_status is not None:
            self.auth_status = auth_status
        if is_delete is not None:
            self.is_delete = is_delete
        if last_update_user_name is not None:
            self.last_update_user_name = last_update_user_name
        if last_update_user_id is not None:
            self.last_update_user_id = last_update_user_id
        if last_update_time is not None:
            self.last_update_time = last_update_time

    @property
    def publisher_unique_id(self):
        """Gets the publisher_unique_id of this ListPublisherResponse.

        发布商ID

        :return: The publisher_unique_id of this ListPublisherResponse.
        :rtype: str
        """
        return self._publisher_unique_id

    @publisher_unique_id.setter
    def publisher_unique_id(self, publisher_unique_id):
        """Sets the publisher_unique_id of this ListPublisherResponse.

        发布商ID

        :param publisher_unique_id: The publisher_unique_id of this ListPublisherResponse.
        :type publisher_unique_id: str
        """
        self._publisher_unique_id = publisher_unique_id

    @property
    def user_id(self):
        """Gets the user_id of this ListPublisherResponse.

        用户ID

        :return: The user_id of this ListPublisherResponse.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this ListPublisherResponse.

        用户ID

        :param user_id: The user_id of this ListPublisherResponse.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def tenant_id(self):
        """Gets the tenant_id of this ListPublisherResponse.

        租户ID

        :return: The tenant_id of this ListPublisherResponse.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this ListPublisherResponse.

        租户ID

        :param tenant_id: The tenant_id of this ListPublisherResponse.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def description(self):
        """Gets the description of this ListPublisherResponse.

        描述

        :return: The description of this ListPublisherResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ListPublisherResponse.

        描述

        :param description: The description of this ListPublisherResponse.
        :type description: str
        """
        self._description = description

    @property
    def logo_url(self):
        """Gets the logo_url of this ListPublisherResponse.

        图标URL

        :return: The logo_url of this ListPublisherResponse.
        :rtype: str
        """
        return self._logo_url

    @logo_url.setter
    def logo_url(self, logo_url):
        """Sets the logo_url of this ListPublisherResponse.

        图标URL

        :param logo_url: The logo_url of this ListPublisherResponse.
        :type logo_url: str
        """
        self._logo_url = logo_url

    @property
    def website(self):
        """Gets the website of this ListPublisherResponse.

        网页地址

        :return: The website of this ListPublisherResponse.
        :rtype: str
        """
        return self._website

    @website.setter
    def website(self, website):
        """Sets the website of this ListPublisherResponse.

        网页地址

        :param website: The website of this ListPublisherResponse.
        :type website: str
        """
        self._website = website

    @property
    def support_url(self):
        """Gets the support_url of this ListPublisherResponse.

        地址

        :return: The support_url of this ListPublisherResponse.
        :rtype: str
        """
        return self._support_url

    @support_url.setter
    def support_url(self, support_url):
        """Sets the support_url of this ListPublisherResponse.

        地址

        :param support_url: The support_url of this ListPublisherResponse.
        :type support_url: str
        """
        self._support_url = support_url

    @property
    def source_url(self):
        """Gets the source_url of this ListPublisherResponse.

        地址

        :return: The source_url of this ListPublisherResponse.
        :rtype: str
        """
        return self._source_url

    @source_url.setter
    def source_url(self, source_url):
        """Sets the source_url of this ListPublisherResponse.

        地址

        :param source_url: The source_url of this ListPublisherResponse.
        :type source_url: str
        """
        self._source_url = source_url

    @property
    def en_name(self):
        """Gets the en_name of this ListPublisherResponse.

        英文名

        :return: The en_name of this ListPublisherResponse.
        :rtype: str
        """
        return self._en_name

    @en_name.setter
    def en_name(self, en_name):
        """Sets the en_name of this ListPublisherResponse.

        英文名

        :param en_name: The en_name of this ListPublisherResponse.
        :type en_name: str
        """
        self._en_name = en_name

    @property
    def name(self):
        """Gets the name of this ListPublisherResponse.

        名称

        :return: The name of this ListPublisherResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListPublisherResponse.

        名称

        :param name: The name of this ListPublisherResponse.
        :type name: str
        """
        self._name = name

    @property
    def auth_status(self):
        """Gets the auth_status of this ListPublisherResponse.

        授权状态

        :return: The auth_status of this ListPublisherResponse.
        :rtype: str
        """
        return self._auth_status

    @auth_status.setter
    def auth_status(self, auth_status):
        """Sets the auth_status of this ListPublisherResponse.

        授权状态

        :param auth_status: The auth_status of this ListPublisherResponse.
        :type auth_status: str
        """
        self._auth_status = auth_status

    @property
    def is_delete(self):
        """Gets the is_delete of this ListPublisherResponse.

        是否删除

        :return: The is_delete of this ListPublisherResponse.
        :rtype: int
        """
        return self._is_delete

    @is_delete.setter
    def is_delete(self, is_delete):
        """Sets the is_delete of this ListPublisherResponse.

        是否删除

        :param is_delete: The is_delete of this ListPublisherResponse.
        :type is_delete: int
        """
        self._is_delete = is_delete

    @property
    def last_update_user_name(self):
        """Gets the last_update_user_name of this ListPublisherResponse.

        最后更新人

        :return: The last_update_user_name of this ListPublisherResponse.
        :rtype: str
        """
        return self._last_update_user_name

    @last_update_user_name.setter
    def last_update_user_name(self, last_update_user_name):
        """Sets the last_update_user_name of this ListPublisherResponse.

        最后更新人

        :param last_update_user_name: The last_update_user_name of this ListPublisherResponse.
        :type last_update_user_name: str
        """
        self._last_update_user_name = last_update_user_name

    @property
    def last_update_user_id(self):
        """Gets the last_update_user_id of this ListPublisherResponse.

        最后更新人ID

        :return: The last_update_user_id of this ListPublisherResponse.
        :rtype: str
        """
        return self._last_update_user_id

    @last_update_user_id.setter
    def last_update_user_id(self, last_update_user_id):
        """Sets the last_update_user_id of this ListPublisherResponse.

        最后更新人ID

        :param last_update_user_id: The last_update_user_id of this ListPublisherResponse.
        :type last_update_user_id: str
        """
        self._last_update_user_id = last_update_user_id

    @property
    def last_update_time(self):
        """Gets the last_update_time of this ListPublisherResponse.

        最后更新时间

        :return: The last_update_time of this ListPublisherResponse.
        :rtype: str
        """
        return self._last_update_time

    @last_update_time.setter
    def last_update_time(self, last_update_time):
        """Sets the last_update_time of this ListPublisherResponse.

        最后更新时间

        :param last_update_time: The last_update_time of this ListPublisherResponse.
        :type last_update_time: str
        """
        self._last_update_time = last_update_time

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
        if not isinstance(other, ListPublisherResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
