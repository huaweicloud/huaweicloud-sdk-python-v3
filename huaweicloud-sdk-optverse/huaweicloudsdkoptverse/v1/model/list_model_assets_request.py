# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListModelAssetsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'asset_code': 'str',
        'asset_source': 'str',
        'asset_type': 'str',
        'sub_asset_type': 'str',
        'chat_id': 'str',
        'asset_actions': 'list[str]',
        'asset_name': 'str',
        'offset': 'int',
        'limit': 'int',
        'sort_dir': 'str'
    }

    attribute_map = {
        'asset_code': 'asset_code',
        'asset_source': 'asset_source',
        'asset_type': 'asset_type',
        'sub_asset_type': 'sub_asset_type',
        'chat_id': 'chat_id',
        'asset_actions': 'asset_actions',
        'asset_name': 'asset_name',
        'offset': 'offset',
        'limit': 'limit',
        'sort_dir': 'sort_dir'
    }

    def __init__(self, asset_code=None, asset_source=None, asset_type=None, sub_asset_type=None, chat_id=None, asset_actions=None, asset_name=None, offset=None, limit=None, sort_dir=None):
        r"""ListModelAssetsRequest

        The model defined in huaweicloud sdk

        :param asset_code: **参数解释**： 资产编码。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type asset_code: str
        :param asset_source: **参数解释**： 资产来源。 **约束限制**： 不涉及 **取值范围**： * Preset：预置 * AIGallery：订阅 * Import：导入 * Publish：发布 **默认取值**： 不涉及 
        :type asset_source: str
        :param asset_type: **参数解释**： 资产类型。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type asset_type: str
        :param sub_asset_type: **参数解释**： 资产子类型。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type sub_asset_type: str
        :param chat_id: **参数解释**： 对话id。 **约束限制**： 不涉及 **取值范围**： 长度为[1-64]个字符。 **默认取值**： 不涉及 
        :type chat_id: str
        :param asset_actions: **参数解释**： 资产应用场景。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type asset_actions: list[str]
        :param asset_name: 模型名称，支持模糊匹配
        :type asset_name: str
        :param offset: **参数解释**： 偏移量。 **约束限制**： 不涉及 **取值范围**： 取值范围[0,100000000]。 **默认取值**： 0 
        :type offset: int
        :param limit: **参数解释**： 返回限制个数。 **约束限制**： 不涉及 **取值范围**： [1-1000] **默认取值**： 100 
        :type limit: int
        :param sort_dir: **参数解释**： 排序规则。 **约束限制**： 不涉及 **取值范围**： - DESC：降序。 - ASC：升序。 **默认取值**： DESC 
        :type sort_dir: str
        """
        
        

        self._asset_code = None
        self._asset_source = None
        self._asset_type = None
        self._sub_asset_type = None
        self._chat_id = None
        self._asset_actions = None
        self._asset_name = None
        self._offset = None
        self._limit = None
        self._sort_dir = None
        self.discriminator = None

        if asset_code is not None:
            self.asset_code = asset_code
        if asset_source is not None:
            self.asset_source = asset_source
        if asset_type is not None:
            self.asset_type = asset_type
        if sub_asset_type is not None:
            self.sub_asset_type = sub_asset_type
        if chat_id is not None:
            self.chat_id = chat_id
        if asset_actions is not None:
            self.asset_actions = asset_actions
        if asset_name is not None:
            self.asset_name = asset_name
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if sort_dir is not None:
            self.sort_dir = sort_dir

    @property
    def asset_code(self):
        r"""Gets the asset_code of this ListModelAssetsRequest.

        **参数解释**： 资产编码。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The asset_code of this ListModelAssetsRequest.
        :rtype: str
        """
        return self._asset_code

    @asset_code.setter
    def asset_code(self, asset_code):
        r"""Sets the asset_code of this ListModelAssetsRequest.

        **参数解释**： 资产编码。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param asset_code: The asset_code of this ListModelAssetsRequest.
        :type asset_code: str
        """
        self._asset_code = asset_code

    @property
    def asset_source(self):
        r"""Gets the asset_source of this ListModelAssetsRequest.

        **参数解释**： 资产来源。 **约束限制**： 不涉及 **取值范围**： * Preset：预置 * AIGallery：订阅 * Import：导入 * Publish：发布 **默认取值**： 不涉及 

        :return: The asset_source of this ListModelAssetsRequest.
        :rtype: str
        """
        return self._asset_source

    @asset_source.setter
    def asset_source(self, asset_source):
        r"""Sets the asset_source of this ListModelAssetsRequest.

        **参数解释**： 资产来源。 **约束限制**： 不涉及 **取值范围**： * Preset：预置 * AIGallery：订阅 * Import：导入 * Publish：发布 **默认取值**： 不涉及 

        :param asset_source: The asset_source of this ListModelAssetsRequest.
        :type asset_source: str
        """
        self._asset_source = asset_source

    @property
    def asset_type(self):
        r"""Gets the asset_type of this ListModelAssetsRequest.

        **参数解释**： 资产类型。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The asset_type of this ListModelAssetsRequest.
        :rtype: str
        """
        return self._asset_type

    @asset_type.setter
    def asset_type(self, asset_type):
        r"""Sets the asset_type of this ListModelAssetsRequest.

        **参数解释**： 资产类型。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param asset_type: The asset_type of this ListModelAssetsRequest.
        :type asset_type: str
        """
        self._asset_type = asset_type

    @property
    def sub_asset_type(self):
        r"""Gets the sub_asset_type of this ListModelAssetsRequest.

        **参数解释**： 资产子类型。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The sub_asset_type of this ListModelAssetsRequest.
        :rtype: str
        """
        return self._sub_asset_type

    @sub_asset_type.setter
    def sub_asset_type(self, sub_asset_type):
        r"""Sets the sub_asset_type of this ListModelAssetsRequest.

        **参数解释**： 资产子类型。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param sub_asset_type: The sub_asset_type of this ListModelAssetsRequest.
        :type sub_asset_type: str
        """
        self._sub_asset_type = sub_asset_type

    @property
    def chat_id(self):
        r"""Gets the chat_id of this ListModelAssetsRequest.

        **参数解释**： 对话id。 **约束限制**： 不涉及 **取值范围**： 长度为[1-64]个字符。 **默认取值**： 不涉及 

        :return: The chat_id of this ListModelAssetsRequest.
        :rtype: str
        """
        return self._chat_id

    @chat_id.setter
    def chat_id(self, chat_id):
        r"""Sets the chat_id of this ListModelAssetsRequest.

        **参数解释**： 对话id。 **约束限制**： 不涉及 **取值范围**： 长度为[1-64]个字符。 **默认取值**： 不涉及 

        :param chat_id: The chat_id of this ListModelAssetsRequest.
        :type chat_id: str
        """
        self._chat_id = chat_id

    @property
    def asset_actions(self):
        r"""Gets the asset_actions of this ListModelAssetsRequest.

        **参数解释**： 资产应用场景。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The asset_actions of this ListModelAssetsRequest.
        :rtype: list[str]
        """
        return self._asset_actions

    @asset_actions.setter
    def asset_actions(self, asset_actions):
        r"""Sets the asset_actions of this ListModelAssetsRequest.

        **参数解释**： 资产应用场景。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param asset_actions: The asset_actions of this ListModelAssetsRequest.
        :type asset_actions: list[str]
        """
        self._asset_actions = asset_actions

    @property
    def asset_name(self):
        r"""Gets the asset_name of this ListModelAssetsRequest.

        模型名称，支持模糊匹配

        :return: The asset_name of this ListModelAssetsRequest.
        :rtype: str
        """
        return self._asset_name

    @asset_name.setter
    def asset_name(self, asset_name):
        r"""Sets the asset_name of this ListModelAssetsRequest.

        模型名称，支持模糊匹配

        :param asset_name: The asset_name of this ListModelAssetsRequest.
        :type asset_name: str
        """
        self._asset_name = asset_name

    @property
    def offset(self):
        r"""Gets the offset of this ListModelAssetsRequest.

        **参数解释**： 偏移量。 **约束限制**： 不涉及 **取值范围**： 取值范围[0,100000000]。 **默认取值**： 0 

        :return: The offset of this ListModelAssetsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListModelAssetsRequest.

        **参数解释**： 偏移量。 **约束限制**： 不涉及 **取值范围**： 取值范围[0,100000000]。 **默认取值**： 0 

        :param offset: The offset of this ListModelAssetsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListModelAssetsRequest.

        **参数解释**： 返回限制个数。 **约束限制**： 不涉及 **取值范围**： [1-1000] **默认取值**： 100 

        :return: The limit of this ListModelAssetsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListModelAssetsRequest.

        **参数解释**： 返回限制个数。 **约束限制**： 不涉及 **取值范围**： [1-1000] **默认取值**： 100 

        :param limit: The limit of this ListModelAssetsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this ListModelAssetsRequest.

        **参数解释**： 排序规则。 **约束限制**： 不涉及 **取值范围**： - DESC：降序。 - ASC：升序。 **默认取值**： DESC 

        :return: The sort_dir of this ListModelAssetsRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this ListModelAssetsRequest.

        **参数解释**： 排序规则。 **约束限制**： 不涉及 **取值范围**： - DESC：降序。 - ASC：升序。 **默认取值**： DESC 

        :param sort_dir: The sort_dir of this ListModelAssetsRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

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
        if not isinstance(other, ListModelAssetsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
