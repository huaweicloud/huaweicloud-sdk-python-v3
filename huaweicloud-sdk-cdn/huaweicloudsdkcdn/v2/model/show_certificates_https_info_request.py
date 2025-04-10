# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowCertificatesHttpsInfoRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'page_size': 'int',
        'page_number': 'int',
        'domain_name': 'str',
        'user_domain_id': 'str',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'page_size': 'page_size',
        'page_number': 'page_number',
        'domain_name': 'domain_name',
        'user_domain_id': 'user_domain_id',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, page_size=None, page_number=None, domain_name=None, user_domain_id=None, enterprise_project_id=None):
        r"""ShowCertificatesHttpsInfoRequest

        The model defined in huaweicloud sdk

        :param page_size: 每页的数量，取值范围1-10000，不设值时默认值为30。
        :type page_size: int
        :param page_number: 查询的页码。取值范围1-65535，不设值时默认值为1。
        :type page_number: int
        :param domain_name: 加速域名。
        :type domain_name: str
        :param user_domain_id: 域名所属用户的domain_id。
        :type user_domain_id: str
        :param enterprise_project_id: 当用户开启企业项目功能时，该参数生效，表示查询资源所属项目，\&quot;all\&quot;表示所有项目。注意：当使用子帐号调用接口时，该参数必传。 您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id。
        :type enterprise_project_id: str
        """
        
        

        self._page_size = None
        self._page_number = None
        self._domain_name = None
        self._user_domain_id = None
        self._enterprise_project_id = None
        self.discriminator = None

        if page_size is not None:
            self.page_size = page_size
        if page_number is not None:
            self.page_number = page_number
        if domain_name is not None:
            self.domain_name = domain_name
        if user_domain_id is not None:
            self.user_domain_id = user_domain_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def page_size(self):
        r"""Gets the page_size of this ShowCertificatesHttpsInfoRequest.

        每页的数量，取值范围1-10000，不设值时默认值为30。

        :return: The page_size of this ShowCertificatesHttpsInfoRequest.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        r"""Sets the page_size of this ShowCertificatesHttpsInfoRequest.

        每页的数量，取值范围1-10000，不设值时默认值为30。

        :param page_size: The page_size of this ShowCertificatesHttpsInfoRequest.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def page_number(self):
        r"""Gets the page_number of this ShowCertificatesHttpsInfoRequest.

        查询的页码。取值范围1-65535，不设值时默认值为1。

        :return: The page_number of this ShowCertificatesHttpsInfoRequest.
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        r"""Sets the page_number of this ShowCertificatesHttpsInfoRequest.

        查询的页码。取值范围1-65535，不设值时默认值为1。

        :param page_number: The page_number of this ShowCertificatesHttpsInfoRequest.
        :type page_number: int
        """
        self._page_number = page_number

    @property
    def domain_name(self):
        r"""Gets the domain_name of this ShowCertificatesHttpsInfoRequest.

        加速域名。

        :return: The domain_name of this ShowCertificatesHttpsInfoRequest.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        r"""Sets the domain_name of this ShowCertificatesHttpsInfoRequest.

        加速域名。

        :param domain_name: The domain_name of this ShowCertificatesHttpsInfoRequest.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def user_domain_id(self):
        r"""Gets the user_domain_id of this ShowCertificatesHttpsInfoRequest.

        域名所属用户的domain_id。

        :return: The user_domain_id of this ShowCertificatesHttpsInfoRequest.
        :rtype: str
        """
        return self._user_domain_id

    @user_domain_id.setter
    def user_domain_id(self, user_domain_id):
        r"""Sets the user_domain_id of this ShowCertificatesHttpsInfoRequest.

        域名所属用户的domain_id。

        :param user_domain_id: The user_domain_id of this ShowCertificatesHttpsInfoRequest.
        :type user_domain_id: str
        """
        self._user_domain_id = user_domain_id

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ShowCertificatesHttpsInfoRequest.

        当用户开启企业项目功能时，该参数生效，表示查询资源所属项目，\"all\"表示所有项目。注意：当使用子帐号调用接口时，该参数必传。 您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id。

        :return: The enterprise_project_id of this ShowCertificatesHttpsInfoRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ShowCertificatesHttpsInfoRequest.

        当用户开启企业项目功能时，该参数生效，表示查询资源所属项目，\"all\"表示所有项目。注意：当使用子帐号调用接口时，该参数必传。 您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id。

        :param enterprise_project_id: The enterprise_project_id of this ShowCertificatesHttpsInfoRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, ShowCertificatesHttpsInfoRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
