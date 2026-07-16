# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RenewLeaseRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'duration': 'int',
        'id': 'str',
        'body': 'LeaseReq'
    }

    attribute_map = {
        'duration': 'duration',
        'id': 'id',
        'body': 'body'
    }

    def __init__(self, duration=None, id=None, body=None):
        r"""RenewLeaseRequest

        The model defined in huaweicloud sdk

        :param duration: **参数解释**：续订时长，推荐该参数在leaseReq中配置，若请求参数中包含duration，则忽略leaseReq的值，且实例自动停止类别为定时停止。(单位:毫秒)。 **约束限制**：不涉及。 **取值范围**：3600000-259200000。 **默认取值**：3600000。
        :type duration: int
        :param id: **参数解释**：Notebook实例ID。ID格式为通用唯一识别码（Universally Unique Identifier，简称UUID），可通过调用[[查询Notebook实例列表接口](https://support.huaweicloud.com/api-modelarts/ListNotebooks.html#section0)](tag:hc)[[查询Notebook实例列表接口](https://support.huaweicloud.com/intl/zh-cn/api-modelarts/ListNotebooks.html#section0)](tag:hk)获取。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type id: str
        :param body: Body of the RenewLeaseRequest
        :type body: :class:`huaweicloudsdkmodelarts.v1.LeaseReq`
        """
        
        

        self._duration = None
        self._id = None
        self._body = None
        self.discriminator = None

        if duration is not None:
            self.duration = duration
        self.id = id
        if body is not None:
            self.body = body

    @property
    def duration(self):
        r"""Gets the duration of this RenewLeaseRequest.

        **参数解释**：续订时长，推荐该参数在leaseReq中配置，若请求参数中包含duration，则忽略leaseReq的值，且实例自动停止类别为定时停止。(单位:毫秒)。 **约束限制**：不涉及。 **取值范围**：3600000-259200000。 **默认取值**：3600000。

        :return: The duration of this RenewLeaseRequest.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        r"""Sets the duration of this RenewLeaseRequest.

        **参数解释**：续订时长，推荐该参数在leaseReq中配置，若请求参数中包含duration，则忽略leaseReq的值，且实例自动停止类别为定时停止。(单位:毫秒)。 **约束限制**：不涉及。 **取值范围**：3600000-259200000。 **默认取值**：3600000。

        :param duration: The duration of this RenewLeaseRequest.
        :type duration: int
        """
        self._duration = duration

    @property
    def id(self):
        r"""Gets the id of this RenewLeaseRequest.

        **参数解释**：Notebook实例ID。ID格式为通用唯一识别码（Universally Unique Identifier，简称UUID），可通过调用[[查询Notebook实例列表接口](https://support.huaweicloud.com/api-modelarts/ListNotebooks.html#section0)](tag:hc)[[查询Notebook实例列表接口](https://support.huaweicloud.com/intl/zh-cn/api-modelarts/ListNotebooks.html#section0)](tag:hk)获取。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The id of this RenewLeaseRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this RenewLeaseRequest.

        **参数解释**：Notebook实例ID。ID格式为通用唯一识别码（Universally Unique Identifier，简称UUID），可通过调用[[查询Notebook实例列表接口](https://support.huaweicloud.com/api-modelarts/ListNotebooks.html#section0)](tag:hc)[[查询Notebook实例列表接口](https://support.huaweicloud.com/intl/zh-cn/api-modelarts/ListNotebooks.html#section0)](tag:hk)获取。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param id: The id of this RenewLeaseRequest.
        :type id: str
        """
        self._id = id

    @property
    def body(self):
        r"""Gets the body of this RenewLeaseRequest.

        :return: The body of this RenewLeaseRequest.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.LeaseReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this RenewLeaseRequest.

        :param body: The body of this RenewLeaseRequest.
        :type body: :class:`huaweicloudsdkmodelarts.v1.LeaseReq`
        """
        self._body = body

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RenewLeaseRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
