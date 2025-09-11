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
        'dashboard_id': 'str',
        'dashboard_type': 'str'
    }

    attribute_map = {
        'enterprise_id': 'enterprise_id',
        'is_favorite': 'is_favorite',
        'dashboard_name': 'dashboard_name',
        'dashboard_id': 'dashboard_id',
        'dashboard_type': 'dashboard_type'
    }

    def __init__(self, enterprise_id=None, is_favorite=None, dashboard_name=None, dashboard_id=None, dashboard_type=None):
        r"""ListDashboardInfosRequest

        The model defined in huaweicloud sdk

        :param enterprise_id: **参数解释**： 企业项目ID。 **约束限制**： 不涉及。 **取值范围**： 只能包含小写字母、数字、“-”、“_”，可以自定义企业项目ID，长度为36个字符。也可以为0（代表默认企业项目ID），all_granted_eps（代表所有企业项目ID）。           **默认取值**： 不涉及。 
        :type enterprise_id: str
        :param is_favorite: **参数解释**： 指定企业项目下监控看板是否收藏。 **约束限制**： 填此参数时，enterprise_id必填。 **取值范围**： - true:收藏 - false:未收藏          **默认取值**： 不涉及。 
        :type is_favorite: bool
        :param dashboard_name: **参数解释**： 监控看板名称。 **约束限制**： 不涉及。 **取值范围**： 长度为[1,128]个字符，只允许中文、英文、数字0-9、_和-          **默认取值**： 不涉及。 
        :type dashboard_name: str
        :param dashboard_id: **参数解释**： 监控看板id。 **约束限制**： 不涉及。 **取值范围**： 以db开头，包含22个字母和数字，长度为24个字符 **默认取值**： 不涉及。 
        :type dashboard_id: str
        :param dashboard_type: **参数解释**： 监控看板类型。 **约束限制**： 不涉及。 **取值范围**： - monitor_dashboard:表示监控大盘 - other:表示自定义看板 **默认取值**： 不涉及。 
        :type dashboard_type: str
        """
        
        

        self._enterprise_id = None
        self._is_favorite = None
        self._dashboard_name = None
        self._dashboard_id = None
        self._dashboard_type = None
        self.discriminator = None

        if enterprise_id is not None:
            self.enterprise_id = enterprise_id
        if is_favorite is not None:
            self.is_favorite = is_favorite
        if dashboard_name is not None:
            self.dashboard_name = dashboard_name
        if dashboard_id is not None:
            self.dashboard_id = dashboard_id
        if dashboard_type is not None:
            self.dashboard_type = dashboard_type

    @property
    def enterprise_id(self):
        r"""Gets the enterprise_id of this ListDashboardInfosRequest.

        **参数解释**： 企业项目ID。 **约束限制**： 不涉及。 **取值范围**： 只能包含小写字母、数字、“-”、“_”，可以自定义企业项目ID，长度为36个字符。也可以为0（代表默认企业项目ID），all_granted_eps（代表所有企业项目ID）。           **默认取值**： 不涉及。 

        :return: The enterprise_id of this ListDashboardInfosRequest.
        :rtype: str
        """
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, enterprise_id):
        r"""Sets the enterprise_id of this ListDashboardInfosRequest.

        **参数解释**： 企业项目ID。 **约束限制**： 不涉及。 **取值范围**： 只能包含小写字母、数字、“-”、“_”，可以自定义企业项目ID，长度为36个字符。也可以为0（代表默认企业项目ID），all_granted_eps（代表所有企业项目ID）。           **默认取值**： 不涉及。 

        :param enterprise_id: The enterprise_id of this ListDashboardInfosRequest.
        :type enterprise_id: str
        """
        self._enterprise_id = enterprise_id

    @property
    def is_favorite(self):
        r"""Gets the is_favorite of this ListDashboardInfosRequest.

        **参数解释**： 指定企业项目下监控看板是否收藏。 **约束限制**： 填此参数时，enterprise_id必填。 **取值范围**： - true:收藏 - false:未收藏          **默认取值**： 不涉及。 

        :return: The is_favorite of this ListDashboardInfosRequest.
        :rtype: bool
        """
        return self._is_favorite

    @is_favorite.setter
    def is_favorite(self, is_favorite):
        r"""Sets the is_favorite of this ListDashboardInfosRequest.

        **参数解释**： 指定企业项目下监控看板是否收藏。 **约束限制**： 填此参数时，enterprise_id必填。 **取值范围**： - true:收藏 - false:未收藏          **默认取值**： 不涉及。 

        :param is_favorite: The is_favorite of this ListDashboardInfosRequest.
        :type is_favorite: bool
        """
        self._is_favorite = is_favorite

    @property
    def dashboard_name(self):
        r"""Gets the dashboard_name of this ListDashboardInfosRequest.

        **参数解释**： 监控看板名称。 **约束限制**： 不涉及。 **取值范围**： 长度为[1,128]个字符，只允许中文、英文、数字0-9、_和-          **默认取值**： 不涉及。 

        :return: The dashboard_name of this ListDashboardInfosRequest.
        :rtype: str
        """
        return self._dashboard_name

    @dashboard_name.setter
    def dashboard_name(self, dashboard_name):
        r"""Sets the dashboard_name of this ListDashboardInfosRequest.

        **参数解释**： 监控看板名称。 **约束限制**： 不涉及。 **取值范围**： 长度为[1,128]个字符，只允许中文、英文、数字0-9、_和-          **默认取值**： 不涉及。 

        :param dashboard_name: The dashboard_name of this ListDashboardInfosRequest.
        :type dashboard_name: str
        """
        self._dashboard_name = dashboard_name

    @property
    def dashboard_id(self):
        r"""Gets the dashboard_id of this ListDashboardInfosRequest.

        **参数解释**： 监控看板id。 **约束限制**： 不涉及。 **取值范围**： 以db开头，包含22个字母和数字，长度为24个字符 **默认取值**： 不涉及。 

        :return: The dashboard_id of this ListDashboardInfosRequest.
        :rtype: str
        """
        return self._dashboard_id

    @dashboard_id.setter
    def dashboard_id(self, dashboard_id):
        r"""Sets the dashboard_id of this ListDashboardInfosRequest.

        **参数解释**： 监控看板id。 **约束限制**： 不涉及。 **取值范围**： 以db开头，包含22个字母和数字，长度为24个字符 **默认取值**： 不涉及。 

        :param dashboard_id: The dashboard_id of this ListDashboardInfosRequest.
        :type dashboard_id: str
        """
        self._dashboard_id = dashboard_id

    @property
    def dashboard_type(self):
        r"""Gets the dashboard_type of this ListDashboardInfosRequest.

        **参数解释**： 监控看板类型。 **约束限制**： 不涉及。 **取值范围**： - monitor_dashboard:表示监控大盘 - other:表示自定义看板 **默认取值**： 不涉及。 

        :return: The dashboard_type of this ListDashboardInfosRequest.
        :rtype: str
        """
        return self._dashboard_type

    @dashboard_type.setter
    def dashboard_type(self, dashboard_type):
        r"""Sets the dashboard_type of this ListDashboardInfosRequest.

        **参数解释**： 监控看板类型。 **约束限制**： 不涉及。 **取值范围**： - monitor_dashboard:表示监控大盘 - other:表示自定义看板 **默认取值**： 不涉及。 

        :param dashboard_type: The dashboard_type of this ListDashboardInfosRequest.
        :type dashboard_type: str
        """
        self._dashboard_type = dashboard_type

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
