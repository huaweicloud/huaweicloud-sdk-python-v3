# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchUnbindInferApiKeysRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'service_id': 'str',
        'body': 'BatchUnBindApiKeyRequest'
    }

    attribute_map = {
        'service_id': 'service_id',
        'body': 'body'
    }

    def __init__(self, service_id=None, body=None):
        r"""BatchUnbindInferApiKeysRequest

        The model defined in huaweicloud sdk

        :param service_id: **参数解释：** 服务ID，在[创建服务](CreateInferService.xml)时即可在返回体中获取，也可通过[查询服务列表](ListInferServices.xml)获取当前用户拥有的服务，其中service_id字段即为服务ID。 **约束限制：** 不涉及。 **取值范围：** 服务ID。 **默认取值：** 不涉及。
        :type service_id: str
        :param body: Body of the BatchUnbindInferApiKeysRequest
        :type body: :class:`huaweicloudsdkmodelarts.v1.BatchUnBindApiKeyRequest`
        """
        
        

        self._service_id = None
        self._body = None
        self.discriminator = None

        self.service_id = service_id
        if body is not None:
            self.body = body

    @property
    def service_id(self):
        r"""Gets the service_id of this BatchUnbindInferApiKeysRequest.

        **参数解释：** 服务ID，在[创建服务](CreateInferService.xml)时即可在返回体中获取，也可通过[查询服务列表](ListInferServices.xml)获取当前用户拥有的服务，其中service_id字段即为服务ID。 **约束限制：** 不涉及。 **取值范围：** 服务ID。 **默认取值：** 不涉及。

        :return: The service_id of this BatchUnbindInferApiKeysRequest.
        :rtype: str
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        r"""Sets the service_id of this BatchUnbindInferApiKeysRequest.

        **参数解释：** 服务ID，在[创建服务](CreateInferService.xml)时即可在返回体中获取，也可通过[查询服务列表](ListInferServices.xml)获取当前用户拥有的服务，其中service_id字段即为服务ID。 **约束限制：** 不涉及。 **取值范围：** 服务ID。 **默认取值：** 不涉及。

        :param service_id: The service_id of this BatchUnbindInferApiKeysRequest.
        :type service_id: str
        """
        self._service_id = service_id

    @property
    def body(self):
        r"""Gets the body of this BatchUnbindInferApiKeysRequest.

        :return: The body of this BatchUnbindInferApiKeysRequest.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.BatchUnBindApiKeyRequest`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this BatchUnbindInferApiKeysRequest.

        :param body: The body of this BatchUnbindInferApiKeysRequest.
        :type body: :class:`huaweicloudsdkmodelarts.v1.BatchUnBindApiKeyRequest`
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
        if not isinstance(other, BatchUnbindInferApiKeysRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
