# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowHttpOverviewsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enterprise_project_id': 'str',
        '_from': 'int',
        'to': 'int',
        'top': 'int',
        'domain_name': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        '_from': 'from',
        'to': 'to',
        'top': 'top',
        'domain_name': 'domain_name'
    }

    def __init__(self, enterprise_project_id=None, _from=None, to=None, top=None, domain_name=None):
        r"""ShowHttpOverviewsRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: 您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id，默认为0
        :type enterprise_project_id: str
        :param _from: 起始时间
        :type _from: int
        :param to: 结束时间
        :type to: int
        :param top: 要查询的前几的结果
        :type top: int
        :param domain_name: 域名
        :type domain_name: str
        """
        
        

        self._enterprise_project_id = None
        self.__from = None
        self._to = None
        self._top = None
        self._domain_name = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self._from = _from
        self.to = to
        if top is not None:
            self.top = top
        if domain_name is not None:
            self.domain_name = domain_name

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ShowHttpOverviewsRequest.

        您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id，默认为0

        :return: The enterprise_project_id of this ShowHttpOverviewsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ShowHttpOverviewsRequest.

        您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id，默认为0

        :param enterprise_project_id: The enterprise_project_id of this ShowHttpOverviewsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def _from(self):
        r"""Gets the _from of this ShowHttpOverviewsRequest.

        起始时间

        :return: The _from of this ShowHttpOverviewsRequest.
        :rtype: int
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        r"""Sets the _from of this ShowHttpOverviewsRequest.

        起始时间

        :param _from: The _from of this ShowHttpOverviewsRequest.
        :type _from: int
        """
        self.__from = _from

    @property
    def to(self):
        r"""Gets the to of this ShowHttpOverviewsRequest.

        结束时间

        :return: The to of this ShowHttpOverviewsRequest.
        :rtype: int
        """
        return self._to

    @to.setter
    def to(self, to):
        r"""Sets the to of this ShowHttpOverviewsRequest.

        结束时间

        :param to: The to of this ShowHttpOverviewsRequest.
        :type to: int
        """
        self._to = to

    @property
    def top(self):
        r"""Gets the top of this ShowHttpOverviewsRequest.

        要查询的前几的结果

        :return: The top of this ShowHttpOverviewsRequest.
        :rtype: int
        """
        return self._top

    @top.setter
    def top(self, top):
        r"""Sets the top of this ShowHttpOverviewsRequest.

        要查询的前几的结果

        :param top: The top of this ShowHttpOverviewsRequest.
        :type top: int
        """
        self._top = top

    @property
    def domain_name(self):
        r"""Gets the domain_name of this ShowHttpOverviewsRequest.

        域名

        :return: The domain_name of this ShowHttpOverviewsRequest.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        r"""Sets the domain_name of this ShowHttpOverviewsRequest.

        域名

        :param domain_name: The domain_name of this ShowHttpOverviewsRequest.
        :type domain_name: str
        """
        self._domain_name = domain_name

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
        if not isinstance(other, ShowHttpOverviewsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
