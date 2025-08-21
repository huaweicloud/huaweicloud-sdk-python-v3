# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApplyDomainTemplateResponse(SdkResponse):

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
        'status': 'str',
        'detail': 'list[ApplyTmlDetail]'
    }

    attribute_map = {
        'id': 'id',
        'status': 'status',
        'detail': 'detail'
    }

    def __init__(self, id=None, status=None, detail=None):
        r"""ApplyDomainTemplateResponse

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 操作ID **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type id: str
        :param status: **参数解释：** 应用模板状态（任务粒度） **约束限制：** 不涉及 **取值范围：** - success: 应用模板成功 - fail: 应用模板失败 **默认取值：** 不涉及
        :type status: str
        :param detail: 
        :type detail: list[:class:`huaweicloudsdkcdn.v2.ApplyTmlDetail`]
        """
        
        super(ApplyDomainTemplateResponse, self).__init__()

        self._id = None
        self._status = None
        self._detail = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if status is not None:
            self.status = status
        if detail is not None:
            self.detail = detail

    @property
    def id(self):
        r"""Gets the id of this ApplyDomainTemplateResponse.

        **参数解释：** 操作ID **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The id of this ApplyDomainTemplateResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ApplyDomainTemplateResponse.

        **参数解释：** 操作ID **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param id: The id of this ApplyDomainTemplateResponse.
        :type id: str
        """
        self._id = id

    @property
    def status(self):
        r"""Gets the status of this ApplyDomainTemplateResponse.

        **参数解释：** 应用模板状态（任务粒度） **约束限制：** 不涉及 **取值范围：** - success: 应用模板成功 - fail: 应用模板失败 **默认取值：** 不涉及

        :return: The status of this ApplyDomainTemplateResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ApplyDomainTemplateResponse.

        **参数解释：** 应用模板状态（任务粒度） **约束限制：** 不涉及 **取值范围：** - success: 应用模板成功 - fail: 应用模板失败 **默认取值：** 不涉及

        :param status: The status of this ApplyDomainTemplateResponse.
        :type status: str
        """
        self._status = status

    @property
    def detail(self):
        r"""Gets the detail of this ApplyDomainTemplateResponse.

        :return: The detail of this ApplyDomainTemplateResponse.
        :rtype: list[:class:`huaweicloudsdkcdn.v2.ApplyTmlDetail`]
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        r"""Sets the detail of this ApplyDomainTemplateResponse.

        :param detail: The detail of this ApplyDomainTemplateResponse.
        :type detail: list[:class:`huaweicloudsdkcdn.v2.ApplyTmlDetail`]
        """
        self._detail = detail

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
        if not isinstance(other, ApplyDomainTemplateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
