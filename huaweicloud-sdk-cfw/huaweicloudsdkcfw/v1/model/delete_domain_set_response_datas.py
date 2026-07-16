# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteDomainSetResponseDatas:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'response_datas': 'list[DomainSetId]'
    }

    attribute_map = {
        'response_datas': 'responseDatas'
    }

    def __init__(self, response_datas=None):
        r"""DeleteDomainSetResponseDatas

        The model defined in huaweicloud sdk

        :param response_datas: **参数解释**： 批量删除域名组响应信息 **取值范围**： 不涉及 
        :type response_datas: list[:class:`huaweicloudsdkcfw.v1.DomainSetId`]
        """
        
        

        self._response_datas = None
        self.discriminator = None

        if response_datas is not None:
            self.response_datas = response_datas

    @property
    def response_datas(self):
        r"""Gets the response_datas of this DeleteDomainSetResponseDatas.

        **参数解释**： 批量删除域名组响应信息 **取值范围**： 不涉及 

        :return: The response_datas of this DeleteDomainSetResponseDatas.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.DomainSetId`]
        """
        return self._response_datas

    @response_datas.setter
    def response_datas(self, response_datas):
        r"""Sets the response_datas of this DeleteDomainSetResponseDatas.

        **参数解释**： 批量删除域名组响应信息 **取值范围**： 不涉及 

        :param response_datas: The response_datas of this DeleteDomainSetResponseDatas.
        :type response_datas: list[:class:`huaweicloudsdkcfw.v1.DomainSetId`]
        """
        self._response_datas = response_datas

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
        if not isinstance(other, DeleteDomainSetResponseDatas):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
