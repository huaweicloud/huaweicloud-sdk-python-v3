# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PredictUrlResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'urls': 'list[str]'
    }

    attribute_map = {
        'type': 'type',
        'urls': 'urls'
    }

    def __init__(self, type=None, urls=None):
        r"""PredictUrlResponse

        The model defined in huaweicloud sdk

        :param type: **参数解释：** 访问方式。 **取值范围：** - CONSOLE：通过控制台界面访问。 - PUBLIC：通过公网访问。 - INTERNAL：通过内网访问。
        :type type: str
        :param urls: **参数解释：** 推理请求的访问地址，仅当type为REAL_TIME时，且服务部署完成后才会确保该字段有值。
        :type urls: list[str]
        """
        
        

        self._type = None
        self._urls = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if urls is not None:
            self.urls = urls

    @property
    def type(self):
        r"""Gets the type of this PredictUrlResponse.

        **参数解释：** 访问方式。 **取值范围：** - CONSOLE：通过控制台界面访问。 - PUBLIC：通过公网访问。 - INTERNAL：通过内网访问。

        :return: The type of this PredictUrlResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this PredictUrlResponse.

        **参数解释：** 访问方式。 **取值范围：** - CONSOLE：通过控制台界面访问。 - PUBLIC：通过公网访问。 - INTERNAL：通过内网访问。

        :param type: The type of this PredictUrlResponse.
        :type type: str
        """
        self._type = type

    @property
    def urls(self):
        r"""Gets the urls of this PredictUrlResponse.

        **参数解释：** 推理请求的访问地址，仅当type为REAL_TIME时，且服务部署完成后才会确保该字段有值。

        :return: The urls of this PredictUrlResponse.
        :rtype: list[str]
        """
        return self._urls

    @urls.setter
    def urls(self, urls):
        r"""Sets the urls of this PredictUrlResponse.

        **参数解释：** 推理请求的访问地址，仅当type为REAL_TIME时，且服务部署完成后才会确保该字段有值。

        :param urls: The urls of this PredictUrlResponse.
        :type urls: list[str]
        """
        self._urls = urls

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
        if not isinstance(other, PredictUrlResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
