# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDomainTemplateResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'temlates': 'list[TemplateItem]'
    }

    attribute_map = {
        'total': 'total',
        'temlates': 'temlates'
    }

    def __init__(self, total=None, temlates=None):
        r"""ShowDomainTemplateResponse

        The model defined in huaweicloud sdk

        :param total: **参数解释：** 查询域名模板总数 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type total: int
        :param temlates: 
        :type temlates: list[:class:`huaweicloudsdkcdn.v2.TemplateItem`]
        """
        
        super(ShowDomainTemplateResponse, self).__init__()

        self._total = None
        self._temlates = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if temlates is not None:
            self.temlates = temlates

    @property
    def total(self):
        r"""Gets the total of this ShowDomainTemplateResponse.

        **参数解释：** 查询域名模板总数 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The total of this ShowDomainTemplateResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ShowDomainTemplateResponse.

        **参数解释：** 查询域名模板总数 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param total: The total of this ShowDomainTemplateResponse.
        :type total: int
        """
        self._total = total

    @property
    def temlates(self):
        r"""Gets the temlates of this ShowDomainTemplateResponse.

        :return: The temlates of this ShowDomainTemplateResponse.
        :rtype: list[:class:`huaweicloudsdkcdn.v2.TemplateItem`]
        """
        return self._temlates

    @temlates.setter
    def temlates(self, temlates):
        r"""Sets the temlates of this ShowDomainTemplateResponse.

        :param temlates: The temlates of this ShowDomainTemplateResponse.
        :type temlates: list[:class:`huaweicloudsdkcdn.v2.TemplateItem`]
        """
        self._temlates = temlates

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
        if not isinstance(other, ShowDomainTemplateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
