# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateRsuModelResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'rsu_model_id': 'str',
        'name': 'str',
        'manufacturer_name': 'str',
        'description': 'str',
        'last_modified_time': 'datetime',
        'created_time': 'datetime'
    }

    attribute_map = {
        'rsu_model_id': 'rsu_model_id',
        'name': 'name',
        'manufacturer_name': 'manufacturer_name',
        'description': 'description',
        'last_modified_time': 'last_modified_time',
        'created_time': 'created_time'
    }

    def __init__(self, rsu_model_id=None, name=None, manufacturer_name=None, description=None, last_modified_time=None, created_time=None):
        r"""UpdateRsuModelResponse

        The model defined in huaweicloud sdk

        :param rsu_model_id: **参数说明**：RSU型号ID，用于唯一标识一个RSU型号，在平台创建RSU型号后由平台分配获得。  **取值范围**：长度不小于1不超过36，只允许字母、数字、连接符（-）的组合。
        :type rsu_model_id: str
        :param name: **参数说明**: RSU型号名称。  **取值范围**：长度不低于1不超过64，只允许中文、字母、数字、下划线（_）、问号（?）、反引号（&#39;）、井号（#）、左小括号（(）、右小括号（)）、点（.）、逗号（,）、与（&amp;）、百分号（%）、At（@）、感叹号（!）、连接符（-）的组合。
        :type name: str
        :param manufacturer_name: **参数说明**: RSU的厂商名称。  **取值范围**：长度不低于1不超过32，只允许中文、字母、数字、下划线（_）、问号（?）、反引号（&#39;）、井号（#）、左小括号（(）、右小括号（)）、点（.）、逗号（,）、与（&amp;）、百分号（%）、At（@）、感叹号（!）、连接符（-）的组合。
        :type manufacturer_name: str
        :param description: **参数说明**: RSU型号的描述信息。  **取值范围**：长度不低于1不超过128，只允许中文、字母、数字、下划线（_）、问号（?）、反引号（&#39;）、井号（#）、左小括号（(）、右小括号（)）、点（.）、逗号（,）、与（&amp;）、百分号（%）、At（@）、感叹号（!）、连接符（-）的组合。
        :type description: str
        :param last_modified_time: **参数说明**: RSU型号更新的时间。  格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39;  例如：2020-12-07T01:32:17Z
        :type last_modified_time: datetime
        :param created_time: **参数说明**: 在平台创建RSU型号的时间。  格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39;  例如：2020-12-07T01:32:17Z
        :type created_time: datetime
        """
        
        super(UpdateRsuModelResponse, self).__init__()

        self._rsu_model_id = None
        self._name = None
        self._manufacturer_name = None
        self._description = None
        self._last_modified_time = None
        self._created_time = None
        self.discriminator = None

        if rsu_model_id is not None:
            self.rsu_model_id = rsu_model_id
        if name is not None:
            self.name = name
        if manufacturer_name is not None:
            self.manufacturer_name = manufacturer_name
        if description is not None:
            self.description = description
        if last_modified_time is not None:
            self.last_modified_time = last_modified_time
        if created_time is not None:
            self.created_time = created_time

    @property
    def rsu_model_id(self):
        r"""Gets the rsu_model_id of this UpdateRsuModelResponse.

        **参数说明**：RSU型号ID，用于唯一标识一个RSU型号，在平台创建RSU型号后由平台分配获得。  **取值范围**：长度不小于1不超过36，只允许字母、数字、连接符（-）的组合。

        :return: The rsu_model_id of this UpdateRsuModelResponse.
        :rtype: str
        """
        return self._rsu_model_id

    @rsu_model_id.setter
    def rsu_model_id(self, rsu_model_id):
        r"""Sets the rsu_model_id of this UpdateRsuModelResponse.

        **参数说明**：RSU型号ID，用于唯一标识一个RSU型号，在平台创建RSU型号后由平台分配获得。  **取值范围**：长度不小于1不超过36，只允许字母、数字、连接符（-）的组合。

        :param rsu_model_id: The rsu_model_id of this UpdateRsuModelResponse.
        :type rsu_model_id: str
        """
        self._rsu_model_id = rsu_model_id

    @property
    def name(self):
        r"""Gets the name of this UpdateRsuModelResponse.

        **参数说明**: RSU型号名称。  **取值范围**：长度不低于1不超过64，只允许中文、字母、数字、下划线（_）、问号（?）、反引号（'）、井号（#）、左小括号（(）、右小括号（)）、点（.）、逗号（,）、与（&）、百分号（%）、At（@）、感叹号（!）、连接符（-）的组合。

        :return: The name of this UpdateRsuModelResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateRsuModelResponse.

        **参数说明**: RSU型号名称。  **取值范围**：长度不低于1不超过64，只允许中文、字母、数字、下划线（_）、问号（?）、反引号（'）、井号（#）、左小括号（(）、右小括号（)）、点（.）、逗号（,）、与（&）、百分号（%）、At（@）、感叹号（!）、连接符（-）的组合。

        :param name: The name of this UpdateRsuModelResponse.
        :type name: str
        """
        self._name = name

    @property
    def manufacturer_name(self):
        r"""Gets the manufacturer_name of this UpdateRsuModelResponse.

        **参数说明**: RSU的厂商名称。  **取值范围**：长度不低于1不超过32，只允许中文、字母、数字、下划线（_）、问号（?）、反引号（'）、井号（#）、左小括号（(）、右小括号（)）、点（.）、逗号（,）、与（&）、百分号（%）、At（@）、感叹号（!）、连接符（-）的组合。

        :return: The manufacturer_name of this UpdateRsuModelResponse.
        :rtype: str
        """
        return self._manufacturer_name

    @manufacturer_name.setter
    def manufacturer_name(self, manufacturer_name):
        r"""Sets the manufacturer_name of this UpdateRsuModelResponse.

        **参数说明**: RSU的厂商名称。  **取值范围**：长度不低于1不超过32，只允许中文、字母、数字、下划线（_）、问号（?）、反引号（'）、井号（#）、左小括号（(）、右小括号（)）、点（.）、逗号（,）、与（&）、百分号（%）、At（@）、感叹号（!）、连接符（-）的组合。

        :param manufacturer_name: The manufacturer_name of this UpdateRsuModelResponse.
        :type manufacturer_name: str
        """
        self._manufacturer_name = manufacturer_name

    @property
    def description(self):
        r"""Gets the description of this UpdateRsuModelResponse.

        **参数说明**: RSU型号的描述信息。  **取值范围**：长度不低于1不超过128，只允许中文、字母、数字、下划线（_）、问号（?）、反引号（'）、井号（#）、左小括号（(）、右小括号（)）、点（.）、逗号（,）、与（&）、百分号（%）、At（@）、感叹号（!）、连接符（-）的组合。

        :return: The description of this UpdateRsuModelResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateRsuModelResponse.

        **参数说明**: RSU型号的描述信息。  **取值范围**：长度不低于1不超过128，只允许中文、字母、数字、下划线（_）、问号（?）、反引号（'）、井号（#）、左小括号（(）、右小括号（)）、点（.）、逗号（,）、与（&）、百分号（%）、At（@）、感叹号（!）、连接符（-）的组合。

        :param description: The description of this UpdateRsuModelResponse.
        :type description: str
        """
        self._description = description

    @property
    def last_modified_time(self):
        r"""Gets the last_modified_time of this UpdateRsuModelResponse.

        **参数说明**: RSU型号更新的时间。  格式：yyyy-MM-dd'T'HH:mm:ss'Z'  例如：2020-12-07T01:32:17Z

        :return: The last_modified_time of this UpdateRsuModelResponse.
        :rtype: datetime
        """
        return self._last_modified_time

    @last_modified_time.setter
    def last_modified_time(self, last_modified_time):
        r"""Sets the last_modified_time of this UpdateRsuModelResponse.

        **参数说明**: RSU型号更新的时间。  格式：yyyy-MM-dd'T'HH:mm:ss'Z'  例如：2020-12-07T01:32:17Z

        :param last_modified_time: The last_modified_time of this UpdateRsuModelResponse.
        :type last_modified_time: datetime
        """
        self._last_modified_time = last_modified_time

    @property
    def created_time(self):
        r"""Gets the created_time of this UpdateRsuModelResponse.

        **参数说明**: 在平台创建RSU型号的时间。  格式：yyyy-MM-dd'T'HH:mm:ss'Z'  例如：2020-12-07T01:32:17Z

        :return: The created_time of this UpdateRsuModelResponse.
        :rtype: datetime
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        r"""Sets the created_time of this UpdateRsuModelResponse.

        **参数说明**: 在平台创建RSU型号的时间。  格式：yyyy-MM-dd'T'HH:mm:ss'Z'  例如：2020-12-07T01:32:17Z

        :param created_time: The created_time of this UpdateRsuModelResponse.
        :type created_time: datetime
        """
        self._created_time = created_time

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
        if not isinstance(other, UpdateRsuModelResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
