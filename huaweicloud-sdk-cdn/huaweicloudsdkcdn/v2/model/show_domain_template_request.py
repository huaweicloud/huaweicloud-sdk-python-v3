# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDomainTemplateRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tml_name': 'str',
        'tml_id': 'str',
        'tml_type': 'int',
        'limit': 'str',
        'offset': 'str'
    }

    attribute_map = {
        'tml_name': 'tml_name',
        'tml_id': 'tml_id',
        'tml_type': 'tml_type',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, tml_name=None, tml_id=None, tml_type=None, limit=None, offset=None):
        r"""ShowDomainTemplateRequest

        The model defined in huaweicloud sdk

        :param tml_name: **参数解释：** 域名模板名称 **约束限制：** 不涉及 **取值范围：** - 1-100个字符 - 仅支持字母、数字、中文、下划线（_）、中横线（-） **默认取值：** 不涉及
        :type tml_name: str
        :param tml_id: **参数解释：** 域名模板ID，可以通过本接口获取 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type tml_id: str
        :param tml_type: **参数解释：** 域名模板类型 **约束限制：** 不涉及 **取值范围：** - 1: 系统预置模板 - 2: 租户自定义模板 **默认取值：** 不涉及
        :type tml_type: int
        :param limit: **参数解释：** 分页大小 **约束限制：** 不涉及 **取值范围：** 1-10000 **默认取值：** 30
        :type limit: str
        :param offset: **参数解释：** 查询的页码 **约束限制：** 不涉及 **取值范围：** 0-65535 **默认取值：** 0
        :type offset: str
        """
        
        

        self._tml_name = None
        self._tml_id = None
        self._tml_type = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        if tml_name is not None:
            self.tml_name = tml_name
        if tml_id is not None:
            self.tml_id = tml_id
        if tml_type is not None:
            self.tml_type = tml_type
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def tml_name(self):
        r"""Gets the tml_name of this ShowDomainTemplateRequest.

        **参数解释：** 域名模板名称 **约束限制：** 不涉及 **取值范围：** - 1-100个字符 - 仅支持字母、数字、中文、下划线（_）、中横线（-） **默认取值：** 不涉及

        :return: The tml_name of this ShowDomainTemplateRequest.
        :rtype: str
        """
        return self._tml_name

    @tml_name.setter
    def tml_name(self, tml_name):
        r"""Sets the tml_name of this ShowDomainTemplateRequest.

        **参数解释：** 域名模板名称 **约束限制：** 不涉及 **取值范围：** - 1-100个字符 - 仅支持字母、数字、中文、下划线（_）、中横线（-） **默认取值：** 不涉及

        :param tml_name: The tml_name of this ShowDomainTemplateRequest.
        :type tml_name: str
        """
        self._tml_name = tml_name

    @property
    def tml_id(self):
        r"""Gets the tml_id of this ShowDomainTemplateRequest.

        **参数解释：** 域名模板ID，可以通过本接口获取 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The tml_id of this ShowDomainTemplateRequest.
        :rtype: str
        """
        return self._tml_id

    @tml_id.setter
    def tml_id(self, tml_id):
        r"""Sets the tml_id of this ShowDomainTemplateRequest.

        **参数解释：** 域名模板ID，可以通过本接口获取 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param tml_id: The tml_id of this ShowDomainTemplateRequest.
        :type tml_id: str
        """
        self._tml_id = tml_id

    @property
    def tml_type(self):
        r"""Gets the tml_type of this ShowDomainTemplateRequest.

        **参数解释：** 域名模板类型 **约束限制：** 不涉及 **取值范围：** - 1: 系统预置模板 - 2: 租户自定义模板 **默认取值：** 不涉及

        :return: The tml_type of this ShowDomainTemplateRequest.
        :rtype: int
        """
        return self._tml_type

    @tml_type.setter
    def tml_type(self, tml_type):
        r"""Sets the tml_type of this ShowDomainTemplateRequest.

        **参数解释：** 域名模板类型 **约束限制：** 不涉及 **取值范围：** - 1: 系统预置模板 - 2: 租户自定义模板 **默认取值：** 不涉及

        :param tml_type: The tml_type of this ShowDomainTemplateRequest.
        :type tml_type: int
        """
        self._tml_type = tml_type

    @property
    def limit(self):
        r"""Gets the limit of this ShowDomainTemplateRequest.

        **参数解释：** 分页大小 **约束限制：** 不涉及 **取值范围：** 1-10000 **默认取值：** 30

        :return: The limit of this ShowDomainTemplateRequest.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowDomainTemplateRequest.

        **参数解释：** 分页大小 **约束限制：** 不涉及 **取值范围：** 1-10000 **默认取值：** 30

        :param limit: The limit of this ShowDomainTemplateRequest.
        :type limit: str
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ShowDomainTemplateRequest.

        **参数解释：** 查询的页码 **约束限制：** 不涉及 **取值范围：** 0-65535 **默认取值：** 0

        :return: The offset of this ShowDomainTemplateRequest.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ShowDomainTemplateRequest.

        **参数解释：** 查询的页码 **约束限制：** 不涉及 **取值范围：** 0-65535 **默认取值：** 0

        :param offset: The offset of this ShowDomainTemplateRequest.
        :type offset: str
        """
        self._offset = offset

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
        if not isinstance(other, ShowDomainTemplateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
