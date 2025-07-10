# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAttackActionTypesRequest:

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
        'to': 'int'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        '_from': 'from',
        'to': 'to'
    }

    def __init__(self, enterprise_project_id=None, _from=None, to=None):
        r"""ListAttackActionTypesRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释：** 您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目ID。若需要查询当前用户所有企业项目绑定的资源信息，请传参all_granted_eps。 **约束限制：** 不涉及 **取值范围：**  - 0：代表default企业项目  - all_granted_eps：代表所有企业项目  - 其它企业项目ID：长度为36个字符  **默认取值：** 0
        :type enterprise_project_id: str
        :param _from: **参数解释：** 起始时间（13位毫秒时间戳），需要和to同时使用。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type _from: int
        :param to: **参数解释：** 结束时间（13位毫秒时间戳），需要和from同时使用。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type to: int
        """
        
        

        self._enterprise_project_id = None
        self.__from = None
        self._to = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self._from = _from
        self.to = to

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListAttackActionTypesRequest.

        **参数解释：** 您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目ID。若需要查询当前用户所有企业项目绑定的资源信息，请传参all_granted_eps。 **约束限制：** 不涉及 **取值范围：**  - 0：代表default企业项目  - all_granted_eps：代表所有企业项目  - 其它企业项目ID：长度为36个字符  **默认取值：** 0

        :return: The enterprise_project_id of this ListAttackActionTypesRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListAttackActionTypesRequest.

        **参数解释：** 您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目ID。若需要查询当前用户所有企业项目绑定的资源信息，请传参all_granted_eps。 **约束限制：** 不涉及 **取值范围：**  - 0：代表default企业项目  - all_granted_eps：代表所有企业项目  - 其它企业项目ID：长度为36个字符  **默认取值：** 0

        :param enterprise_project_id: The enterprise_project_id of this ListAttackActionTypesRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def _from(self):
        r"""Gets the _from of this ListAttackActionTypesRequest.

        **参数解释：** 起始时间（13位毫秒时间戳），需要和to同时使用。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The _from of this ListAttackActionTypesRequest.
        :rtype: int
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        r"""Sets the _from of this ListAttackActionTypesRequest.

        **参数解释：** 起始时间（13位毫秒时间戳），需要和to同时使用。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param _from: The _from of this ListAttackActionTypesRequest.
        :type _from: int
        """
        self.__from = _from

    @property
    def to(self):
        r"""Gets the to of this ListAttackActionTypesRequest.

        **参数解释：** 结束时间（13位毫秒时间戳），需要和from同时使用。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The to of this ListAttackActionTypesRequest.
        :rtype: int
        """
        return self._to

    @to.setter
    def to(self, to):
        r"""Sets the to of this ListAttackActionTypesRequest.

        **参数解释：** 结束时间（13位毫秒时间戳），需要和from同时使用。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param to: The to of this ListAttackActionTypesRequest.
        :type to: int
        """
        self._to = to

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
        if not isinstance(other, ListAttackActionTypesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
