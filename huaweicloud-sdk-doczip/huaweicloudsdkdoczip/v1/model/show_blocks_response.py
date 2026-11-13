# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowBlocksResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'blocks_info': 'object',
        'x_trace_id': 'str'
    }

    attribute_map = {
        'blocks_info': 'blocks_info',
        'x_trace_id': 'X-Trace-Id'
    }

    def __init__(self, blocks_info=None, x_trace_id=None):
        r"""ShowBlocksResponse

        The model defined in huaweicloud sdk

        :param blocks_info: **参数解释**： 文档块信息。支持more和basic两个列表，分别标识基础文档块和扩展文档块。 - basic：基础文档块列表，元素为文档块对象。 - more：扩展文档块列表，元素为文档块对象或分组标题对象。 文档块对象支持字段如下： - code：文档块编码。 - pinyin：文档块简称。 - quanpin：文档块全程。 - name：文档块名称。 - icon：文档块图标。 - show：是否展示： true为展示，false为不展示。 - source：文档块来源，0标识系统文档块，分组标题对象中1标识自定义分组。 - darkIcon：暗黑模式文档块图标。 - key：文档块key值。 - data：文档块附加数据，可为字符串或对象（可选）。 分组标题对象字段如下： - source：分组来源。 - title：分组标题。 **取值范围**： [1-65535]字符。
        :type blocks_info: object
        :param x_trace_id: 
        :type x_trace_id: str
        """
        
        super().__init__()

        self._blocks_info = None
        self._x_trace_id = None
        self.discriminator = None

        if blocks_info is not None:
            self.blocks_info = blocks_info
        if x_trace_id is not None:
            self.x_trace_id = x_trace_id

    @property
    def blocks_info(self):
        r"""Gets the blocks_info of this ShowBlocksResponse.

        **参数解释**： 文档块信息。支持more和basic两个列表，分别标识基础文档块和扩展文档块。 - basic：基础文档块列表，元素为文档块对象。 - more：扩展文档块列表，元素为文档块对象或分组标题对象。 文档块对象支持字段如下： - code：文档块编码。 - pinyin：文档块简称。 - quanpin：文档块全程。 - name：文档块名称。 - icon：文档块图标。 - show：是否展示： true为展示，false为不展示。 - source：文档块来源，0标识系统文档块，分组标题对象中1标识自定义分组。 - darkIcon：暗黑模式文档块图标。 - key：文档块key值。 - data：文档块附加数据，可为字符串或对象（可选）。 分组标题对象字段如下： - source：分组来源。 - title：分组标题。 **取值范围**： [1-65535]字符。

        :return: The blocks_info of this ShowBlocksResponse.
        :rtype: object
        """
        return self._blocks_info

    @blocks_info.setter
    def blocks_info(self, blocks_info):
        r"""Sets the blocks_info of this ShowBlocksResponse.

        **参数解释**： 文档块信息。支持more和basic两个列表，分别标识基础文档块和扩展文档块。 - basic：基础文档块列表，元素为文档块对象。 - more：扩展文档块列表，元素为文档块对象或分组标题对象。 文档块对象支持字段如下： - code：文档块编码。 - pinyin：文档块简称。 - quanpin：文档块全程。 - name：文档块名称。 - icon：文档块图标。 - show：是否展示： true为展示，false为不展示。 - source：文档块来源，0标识系统文档块，分组标题对象中1标识自定义分组。 - darkIcon：暗黑模式文档块图标。 - key：文档块key值。 - data：文档块附加数据，可为字符串或对象（可选）。 分组标题对象字段如下： - source：分组来源。 - title：分组标题。 **取值范围**： [1-65535]字符。

        :param blocks_info: The blocks_info of this ShowBlocksResponse.
        :type blocks_info: object
        """
        self._blocks_info = blocks_info

    @property
    def x_trace_id(self):
        r"""Gets the x_trace_id of this ShowBlocksResponse.

        :return: The x_trace_id of this ShowBlocksResponse.
        :rtype: str
        """
        return self._x_trace_id

    @x_trace_id.setter
    def x_trace_id(self, x_trace_id):
        r"""Sets the x_trace_id of this ShowBlocksResponse.

        :param x_trace_id: The x_trace_id of this ShowBlocksResponse.
        :type x_trace_id: str
        """
        self._x_trace_id = x_trace_id

    def to_dict(self):
        import warnings
        warnings.warn("ShowBlocksResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ShowBlocksResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
