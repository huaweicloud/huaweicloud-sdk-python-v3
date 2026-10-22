# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAiGuardAttackDistributionRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        '_from': 'int',
        'to': 'int',
        'app_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'detect_type': 'str'
    }

    attribute_map = {
        '_from': 'from',
        'to': 'to',
        'app_id': 'app_id',
        'offset': 'offset',
        'limit': 'limit',
        'detect_type': 'detect_type'
    }

    def __init__(self, _from=None, to=None, app_id=None, offset=None, limit=None, detect_type=None):
        r"""ShowAiGuardAttackDistributionRequest

        The model defined in huaweicloud sdk

        :param _from: **参数解释：** 开始时间，时间格式为毫秒时间戳 **约束限制：** 不涉及 **取值范围：** 1-9999999999999 **默认取值：** 不涉及
        :type _from: int
        :param to: **参数解释：** 截止时间，时间格式为毫秒时间戳，默认当天时间戳 **约束限制：** 不涉及 **取值范围：** 1-9999999999999 **默认取值：** 当天时间戳
        :type to: int
        :param app_id: **参数解释：** 应用ID **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type app_id: str
        :param offset: **参数解释：** 分页偏移量，默认值为0 **约束限制：** 不涉及 **取值范围：** &gt;&#x3D;0 **默认取值：** 0
        :type offset: int
        :param limit: **参数解释：** 每页返回的最大数据量，默认值为2000，最大限制为2000 **约束限制：** 最大2000 **取值范围：** 0-2000 **默认取值：** 2000
        :type limit: int
        :param detect_type: **参数解释：** 检测内容类型筛选，不传则查询全部类型 **约束限制：** 不涉及 **取值范围：** - text: 文本检测 - image: 图片检测 **默认取值：** 不涉及
        :type detect_type: str
        """
        
        

        self.__from = None
        self._to = None
        self._app_id = None
        self._offset = None
        self._limit = None
        self._detect_type = None
        self.discriminator = None

        if _from is not None:
            self._from = _from
        if to is not None:
            self.to = to
        if app_id is not None:
            self.app_id = app_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if detect_type is not None:
            self.detect_type = detect_type

    @property
    def _from(self):
        r"""Gets the _from of this ShowAiGuardAttackDistributionRequest.

        **参数解释：** 开始时间，时间格式为毫秒时间戳 **约束限制：** 不涉及 **取值范围：** 1-9999999999999 **默认取值：** 不涉及

        :return: The _from of this ShowAiGuardAttackDistributionRequest.
        :rtype: int
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        r"""Sets the _from of this ShowAiGuardAttackDistributionRequest.

        **参数解释：** 开始时间，时间格式为毫秒时间戳 **约束限制：** 不涉及 **取值范围：** 1-9999999999999 **默认取值：** 不涉及

        :param _from: The _from of this ShowAiGuardAttackDistributionRequest.
        :type _from: int
        """
        self.__from = _from

    @property
    def to(self):
        r"""Gets the to of this ShowAiGuardAttackDistributionRequest.

        **参数解释：** 截止时间，时间格式为毫秒时间戳，默认当天时间戳 **约束限制：** 不涉及 **取值范围：** 1-9999999999999 **默认取值：** 当天时间戳

        :return: The to of this ShowAiGuardAttackDistributionRequest.
        :rtype: int
        """
        return self._to

    @to.setter
    def to(self, to):
        r"""Sets the to of this ShowAiGuardAttackDistributionRequest.

        **参数解释：** 截止时间，时间格式为毫秒时间戳，默认当天时间戳 **约束限制：** 不涉及 **取值范围：** 1-9999999999999 **默认取值：** 当天时间戳

        :param to: The to of this ShowAiGuardAttackDistributionRequest.
        :type to: int
        """
        self._to = to

    @property
    def app_id(self):
        r"""Gets the app_id of this ShowAiGuardAttackDistributionRequest.

        **参数解释：** 应用ID **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The app_id of this ShowAiGuardAttackDistributionRequest.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        r"""Sets the app_id of this ShowAiGuardAttackDistributionRequest.

        **参数解释：** 应用ID **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param app_id: The app_id of this ShowAiGuardAttackDistributionRequest.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def offset(self):
        r"""Gets the offset of this ShowAiGuardAttackDistributionRequest.

        **参数解释：** 分页偏移量，默认值为0 **约束限制：** 不涉及 **取值范围：** >=0 **默认取值：** 0

        :return: The offset of this ShowAiGuardAttackDistributionRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ShowAiGuardAttackDistributionRequest.

        **参数解释：** 分页偏移量，默认值为0 **约束限制：** 不涉及 **取值范围：** >=0 **默认取值：** 0

        :param offset: The offset of this ShowAiGuardAttackDistributionRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ShowAiGuardAttackDistributionRequest.

        **参数解释：** 每页返回的最大数据量，默认值为2000，最大限制为2000 **约束限制：** 最大2000 **取值范围：** 0-2000 **默认取值：** 2000

        :return: The limit of this ShowAiGuardAttackDistributionRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowAiGuardAttackDistributionRequest.

        **参数解释：** 每页返回的最大数据量，默认值为2000，最大限制为2000 **约束限制：** 最大2000 **取值范围：** 0-2000 **默认取值：** 2000

        :param limit: The limit of this ShowAiGuardAttackDistributionRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def detect_type(self):
        r"""Gets the detect_type of this ShowAiGuardAttackDistributionRequest.

        **参数解释：** 检测内容类型筛选，不传则查询全部类型 **约束限制：** 不涉及 **取值范围：** - text: 文本检测 - image: 图片检测 **默认取值：** 不涉及

        :return: The detect_type of this ShowAiGuardAttackDistributionRequest.
        :rtype: str
        """
        return self._detect_type

    @detect_type.setter
    def detect_type(self, detect_type):
        r"""Sets the detect_type of this ShowAiGuardAttackDistributionRequest.

        **参数解释：** 检测内容类型筛选，不传则查询全部类型 **约束限制：** 不涉及 **取值范围：** - text: 文本检测 - image: 图片检测 **默认取值：** 不涉及

        :param detect_type: The detect_type of this ShowAiGuardAttackDistributionRequest.
        :type detect_type: str
        """
        self._detect_type = detect_type

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
        if not isinstance(other, ShowAiGuardAttackDistributionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
