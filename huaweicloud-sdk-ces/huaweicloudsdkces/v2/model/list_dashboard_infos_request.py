# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDashboardInfosRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enterprise_id': 'str',
        'is_favorite': 'bool',
        'dashboard_name': 'str',
        'dashboard_id': 'str'
    }

    attribute_map = {
        'enterprise_id': 'enterprise_id',
        'is_favorite': 'is_favorite',
        'dashboard_name': 'dashboard_name',
        'dashboard_id': 'dashboard_id'
    }

    def __init__(self, enterprise_id=None, is_favorite=None, dashboard_name=None, dashboard_id=None):
        """ListDashboardInfosRequest

        The model defined in huaweicloud sdk

        :param enterprise_id: 企业项目Id
        :type enterprise_id: str
        :param is_favorite: 指定企业项目下监控看板是否收藏，true:收藏，false:未收藏，填此参数时，enterprise_id必填
        :type is_favorite: bool
        :param dashboard_name: 监控看板名称
        :type dashboard_name: str
        :param dashboard_id: 监控看板id
        :type dashboard_id: str
        """
        
        

        self._enterprise_id = None
        self._is_favorite = None
        self._dashboard_name = None
        self._dashboard_id = None
        self.discriminator = None

        if enterprise_id is not None:
            self.enterprise_id = enterprise_id
        if is_favorite is not None:
            self.is_favorite = is_favorite
        if dashboard_name is not None:
            self.dashboard_name = dashboard_name
        if dashboard_id is not None:
            self.dashboard_id = dashboard_id

    @property
    def enterprise_id(self):
        """Gets the enterprise_id of this ListDashboardInfosRequest.

        企业项目Id

        :return: The enterprise_id of this ListDashboardInfosRequest.
        :rtype: str
        """
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, enterprise_id):
        """Sets the enterprise_id of this ListDashboardInfosRequest.

        企业项目Id

        :param enterprise_id: The enterprise_id of this ListDashboardInfosRequest.
        :type enterprise_id: str
        """
        self._enterprise_id = enterprise_id

    @property
    def is_favorite(self):
        """Gets the is_favorite of this ListDashboardInfosRequest.

        指定企业项目下监控看板是否收藏，true:收藏，false:未收藏，填此参数时，enterprise_id必填

        :return: The is_favorite of this ListDashboardInfosRequest.
        :rtype: bool
        """
        return self._is_favorite

    @is_favorite.setter
    def is_favorite(self, is_favorite):
        """Sets the is_favorite of this ListDashboardInfosRequest.

        指定企业项目下监控看板是否收藏，true:收藏，false:未收藏，填此参数时，enterprise_id必填

        :param is_favorite: The is_favorite of this ListDashboardInfosRequest.
        :type is_favorite: bool
        """
        self._is_favorite = is_favorite

    @property
    def dashboard_name(self):
        """Gets the dashboard_name of this ListDashboardInfosRequest.

        监控看板名称

        :return: The dashboard_name of this ListDashboardInfosRequest.
        :rtype: str
        """
        return self._dashboard_name

    @dashboard_name.setter
    def dashboard_name(self, dashboard_name):
        """Sets the dashboard_name of this ListDashboardInfosRequest.

        监控看板名称

        :param dashboard_name: The dashboard_name of this ListDashboardInfosRequest.
        :type dashboard_name: str
        """
        self._dashboard_name = dashboard_name

    @property
    def dashboard_id(self):
        """Gets the dashboard_id of this ListDashboardInfosRequest.

        监控看板id

        :return: The dashboard_id of this ListDashboardInfosRequest.
        :rtype: str
        """
        return self._dashboard_id

    @dashboard_id.setter
    def dashboard_id(self, dashboard_id):
        """Sets the dashboard_id of this ListDashboardInfosRequest.

        监控看板id

        :param dashboard_id: The dashboard_id of this ListDashboardInfosRequest.
        :type dashboard_id: str
        """
        self._dashboard_id = dashboard_id

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
        if not isinstance(other, ListDashboardInfosRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
