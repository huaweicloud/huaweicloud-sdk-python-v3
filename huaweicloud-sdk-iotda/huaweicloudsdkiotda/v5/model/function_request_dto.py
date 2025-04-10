# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FunctionRequestDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'app_id': 'str',
        'product_id': 'str',
        'urn': 'str',
        'description': 'str'
    }

    attribute_map = {
        'app_id': 'app_id',
        'product_id': 'product_id',
        'urn': 'urn',
        'description': 'description'
    }

    def __init__(self, app_id=None, product_id=None, urn=None, description=None):
        r"""FunctionRequestDTO

        The model defined in huaweicloud sdk

        :param app_id: **参数说明**：资源空间ID。此参数为非必选参数，存在多资源空间的用户需要使用该接口时，可以携带该参数查询指定资源空间下的产品列表，不携带该参数则会查询该用户下所有产品列表。 **取值范围**：长度不超过36，只允许字母、数字、下划线（_）、连接符（-）的组合。
        :type app_id: str
        :param product_id: **参数说明**：设备关联的产品ID，用于唯一标识一个产品模型，创建产品后获得。方法请参见 [[创建产品](https://support.huaweicloud.com/api-iothub/iot_06_v5_0050.html)](tag:hws)[[创建产品](https://support.huaweicloud.com/intl/zh-cn/api-iothub/iot_06_v5_0050.html)](tag:hws_hk)。 **取值范围**：长度不超过36，只允许字母、数字、下划线（_）、连接符（-）的组合。
        :type product_id: str
        :param urn: **参数说明**：产品关联函数的URN（Uniform Resource Name）。 **取值范围**：长度不超过256，只允许字母、数字、下划线（_）、连接符（-）、分隔符（:）的组合。
        :type urn: str
        :param description: **参数说明**：编解码函数描述信息。 **取值范围**：128，只允许中文、字母、数字、以及_? &#39;#().,&amp;%@!-等字符的组合。
        :type description: str
        """
        
        

        self._app_id = None
        self._product_id = None
        self._urn = None
        self._description = None
        self.discriminator = None

        if app_id is not None:
            self.app_id = app_id
        self.product_id = product_id
        self.urn = urn
        if description is not None:
            self.description = description

    @property
    def app_id(self):
        r"""Gets the app_id of this FunctionRequestDTO.

        **参数说明**：资源空间ID。此参数为非必选参数，存在多资源空间的用户需要使用该接口时，可以携带该参数查询指定资源空间下的产品列表，不携带该参数则会查询该用户下所有产品列表。 **取值范围**：长度不超过36，只允许字母、数字、下划线（_）、连接符（-）的组合。

        :return: The app_id of this FunctionRequestDTO.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        r"""Sets the app_id of this FunctionRequestDTO.

        **参数说明**：资源空间ID。此参数为非必选参数，存在多资源空间的用户需要使用该接口时，可以携带该参数查询指定资源空间下的产品列表，不携带该参数则会查询该用户下所有产品列表。 **取值范围**：长度不超过36，只允许字母、数字、下划线（_）、连接符（-）的组合。

        :param app_id: The app_id of this FunctionRequestDTO.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def product_id(self):
        r"""Gets the product_id of this FunctionRequestDTO.

        **参数说明**：设备关联的产品ID，用于唯一标识一个产品模型，创建产品后获得。方法请参见 [[创建产品](https://support.huaweicloud.com/api-iothub/iot_06_v5_0050.html)](tag:hws)[[创建产品](https://support.huaweicloud.com/intl/zh-cn/api-iothub/iot_06_v5_0050.html)](tag:hws_hk)。 **取值范围**：长度不超过36，只允许字母、数字、下划线（_）、连接符（-）的组合。

        :return: The product_id of this FunctionRequestDTO.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        r"""Sets the product_id of this FunctionRequestDTO.

        **参数说明**：设备关联的产品ID，用于唯一标识一个产品模型，创建产品后获得。方法请参见 [[创建产品](https://support.huaweicloud.com/api-iothub/iot_06_v5_0050.html)](tag:hws)[[创建产品](https://support.huaweicloud.com/intl/zh-cn/api-iothub/iot_06_v5_0050.html)](tag:hws_hk)。 **取值范围**：长度不超过36，只允许字母、数字、下划线（_）、连接符（-）的组合。

        :param product_id: The product_id of this FunctionRequestDTO.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def urn(self):
        r"""Gets the urn of this FunctionRequestDTO.

        **参数说明**：产品关联函数的URN（Uniform Resource Name）。 **取值范围**：长度不超过256，只允许字母、数字、下划线（_）、连接符（-）、分隔符（:）的组合。

        :return: The urn of this FunctionRequestDTO.
        :rtype: str
        """
        return self._urn

    @urn.setter
    def urn(self, urn):
        r"""Sets the urn of this FunctionRequestDTO.

        **参数说明**：产品关联函数的URN（Uniform Resource Name）。 **取值范围**：长度不超过256，只允许字母、数字、下划线（_）、连接符（-）、分隔符（:）的组合。

        :param urn: The urn of this FunctionRequestDTO.
        :type urn: str
        """
        self._urn = urn

    @property
    def description(self):
        r"""Gets the description of this FunctionRequestDTO.

        **参数说明**：编解码函数描述信息。 **取值范围**：128，只允许中文、字母、数字、以及_? '#().,&%@!-等字符的组合。

        :return: The description of this FunctionRequestDTO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this FunctionRequestDTO.

        **参数说明**：编解码函数描述信息。 **取值范围**：128，只允许中文、字母、数字、以及_? '#().,&%@!-等字符的组合。

        :param description: The description of this FunctionRequestDTO.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, FunctionRequestDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
