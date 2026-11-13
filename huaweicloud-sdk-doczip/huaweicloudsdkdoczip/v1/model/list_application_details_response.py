# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListApplicationDetailsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'basic_info': 'ApplicationBasicInfoRsp',
        'system_config': 'SysconfigInfo',
        'blocks_info': 'object',
        'release_info': 'list[ReleaseAppInfo]',
        'idp_info': 'IDPDetailInfo',
        'total': 'int',
        'x_trace_id': 'str'
    }

    attribute_map = {
        'basic_info': 'basic_info',
        'system_config': 'system_config',
        'blocks_info': 'blocks_info',
        'release_info': 'release_info',
        'idp_info': 'idp_info',
        'total': 'total',
        'x_trace_id': 'X-Trace-Id'
    }

    def __init__(self, basic_info=None, system_config=None, blocks_info=None, release_info=None, idp_info=None, total=None, x_trace_id=None):
        r"""ListApplicationDetailsResponse

        The model defined in huaweicloud sdk

        :param basic_info: 
        :type basic_info: :class:`huaweicloudsdkdoczip.v1.ApplicationBasicInfoRsp`
        :param system_config: 
        :type system_config: :class:`huaweicloudsdkdoczip.v1.SysconfigInfo`
        :param blocks_info: **参数解释**： 文档块信息，仅当query_type为2或者4时返回。 支持more和basic两个列表，分别标识基础文档块和扩展文档块。 - basic：基础文档块列表，元素为文档块对象。 - more：扩展文档块列表，元素为文档块对象或分组标题对象。 - release_state：发布状态，true为已发布，false为未发布。 文档块对象支持字段如下： - code：文档块编码。 - pinyin：文档块简称。 - quanpin：文档块全程。 - name：文档块名称。 - icon：文档块图标。 - show：是否展示： true为展示，false为不展示。 - source：文档块来源，0标识系统文档块，分组标题对象中1标识自定义分组。 - darkIcon：暗黑模式文档块图标。 - key：文档块key值。 - data：文档块附加数据，可为字符串或对象（可选）。 分组标题对象字段如下： - source：分组来源。 - title：分组标题。 **取值范围**： 不涉及。
        :type blocks_info: object
        :param release_info: **参数解释**： 发布信息，仅当quey_type为3或者4时返回。 **取值范围**： 不涉及。
        :type release_info: list[:class:`huaweicloudsdkdoczip.v1.ReleaseAppInfo`]
        :param idp_info: 
        :type idp_info: :class:`huaweicloudsdkdoczip.v1.IDPDetailInfo`
        :param total: **参数解释**： 发布信息的总数量，仅当查询包含发布信息时，该字段返回。 **取值范围**： 不涉及。
        :type total: int
        :param x_trace_id: 
        :type x_trace_id: str
        """
        
        super().__init__()

        self._basic_info = None
        self._system_config = None
        self._blocks_info = None
        self._release_info = None
        self._idp_info = None
        self._total = None
        self._x_trace_id = None
        self.discriminator = None

        if basic_info is not None:
            self.basic_info = basic_info
        if system_config is not None:
            self.system_config = system_config
        if blocks_info is not None:
            self.blocks_info = blocks_info
        if release_info is not None:
            self.release_info = release_info
        if idp_info is not None:
            self.idp_info = idp_info
        if total is not None:
            self.total = total
        if x_trace_id is not None:
            self.x_trace_id = x_trace_id

    @property
    def basic_info(self):
        r"""Gets the basic_info of this ListApplicationDetailsResponse.

        :return: The basic_info of this ListApplicationDetailsResponse.
        :rtype: :class:`huaweicloudsdkdoczip.v1.ApplicationBasicInfoRsp`
        """
        return self._basic_info

    @basic_info.setter
    def basic_info(self, basic_info):
        r"""Sets the basic_info of this ListApplicationDetailsResponse.

        :param basic_info: The basic_info of this ListApplicationDetailsResponse.
        :type basic_info: :class:`huaweicloudsdkdoczip.v1.ApplicationBasicInfoRsp`
        """
        self._basic_info = basic_info

    @property
    def system_config(self):
        r"""Gets the system_config of this ListApplicationDetailsResponse.

        :return: The system_config of this ListApplicationDetailsResponse.
        :rtype: :class:`huaweicloudsdkdoczip.v1.SysconfigInfo`
        """
        return self._system_config

    @system_config.setter
    def system_config(self, system_config):
        r"""Sets the system_config of this ListApplicationDetailsResponse.

        :param system_config: The system_config of this ListApplicationDetailsResponse.
        :type system_config: :class:`huaweicloudsdkdoczip.v1.SysconfigInfo`
        """
        self._system_config = system_config

    @property
    def blocks_info(self):
        r"""Gets the blocks_info of this ListApplicationDetailsResponse.

        **参数解释**： 文档块信息，仅当query_type为2或者4时返回。 支持more和basic两个列表，分别标识基础文档块和扩展文档块。 - basic：基础文档块列表，元素为文档块对象。 - more：扩展文档块列表，元素为文档块对象或分组标题对象。 - release_state：发布状态，true为已发布，false为未发布。 文档块对象支持字段如下： - code：文档块编码。 - pinyin：文档块简称。 - quanpin：文档块全程。 - name：文档块名称。 - icon：文档块图标。 - show：是否展示： true为展示，false为不展示。 - source：文档块来源，0标识系统文档块，分组标题对象中1标识自定义分组。 - darkIcon：暗黑模式文档块图标。 - key：文档块key值。 - data：文档块附加数据，可为字符串或对象（可选）。 分组标题对象字段如下： - source：分组来源。 - title：分组标题。 **取值范围**： 不涉及。

        :return: The blocks_info of this ListApplicationDetailsResponse.
        :rtype: object
        """
        return self._blocks_info

    @blocks_info.setter
    def blocks_info(self, blocks_info):
        r"""Sets the blocks_info of this ListApplicationDetailsResponse.

        **参数解释**： 文档块信息，仅当query_type为2或者4时返回。 支持more和basic两个列表，分别标识基础文档块和扩展文档块。 - basic：基础文档块列表，元素为文档块对象。 - more：扩展文档块列表，元素为文档块对象或分组标题对象。 - release_state：发布状态，true为已发布，false为未发布。 文档块对象支持字段如下： - code：文档块编码。 - pinyin：文档块简称。 - quanpin：文档块全程。 - name：文档块名称。 - icon：文档块图标。 - show：是否展示： true为展示，false为不展示。 - source：文档块来源，0标识系统文档块，分组标题对象中1标识自定义分组。 - darkIcon：暗黑模式文档块图标。 - key：文档块key值。 - data：文档块附加数据，可为字符串或对象（可选）。 分组标题对象字段如下： - source：分组来源。 - title：分组标题。 **取值范围**： 不涉及。

        :param blocks_info: The blocks_info of this ListApplicationDetailsResponse.
        :type blocks_info: object
        """
        self._blocks_info = blocks_info

    @property
    def release_info(self):
        r"""Gets the release_info of this ListApplicationDetailsResponse.

        **参数解释**： 发布信息，仅当quey_type为3或者4时返回。 **取值范围**： 不涉及。

        :return: The release_info of this ListApplicationDetailsResponse.
        :rtype: list[:class:`huaweicloudsdkdoczip.v1.ReleaseAppInfo`]
        """
        return self._release_info

    @release_info.setter
    def release_info(self, release_info):
        r"""Sets the release_info of this ListApplicationDetailsResponse.

        **参数解释**： 发布信息，仅当quey_type为3或者4时返回。 **取值范围**： 不涉及。

        :param release_info: The release_info of this ListApplicationDetailsResponse.
        :type release_info: list[:class:`huaweicloudsdkdoczip.v1.ReleaseAppInfo`]
        """
        self._release_info = release_info

    @property
    def idp_info(self):
        r"""Gets the idp_info of this ListApplicationDetailsResponse.

        :return: The idp_info of this ListApplicationDetailsResponse.
        :rtype: :class:`huaweicloudsdkdoczip.v1.IDPDetailInfo`
        """
        return self._idp_info

    @idp_info.setter
    def idp_info(self, idp_info):
        r"""Sets the idp_info of this ListApplicationDetailsResponse.

        :param idp_info: The idp_info of this ListApplicationDetailsResponse.
        :type idp_info: :class:`huaweicloudsdkdoczip.v1.IDPDetailInfo`
        """
        self._idp_info = idp_info

    @property
    def total(self):
        r"""Gets the total of this ListApplicationDetailsResponse.

        **参数解释**： 发布信息的总数量，仅当查询包含发布信息时，该字段返回。 **取值范围**： 不涉及。

        :return: The total of this ListApplicationDetailsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListApplicationDetailsResponse.

        **参数解释**： 发布信息的总数量，仅当查询包含发布信息时，该字段返回。 **取值范围**： 不涉及。

        :param total: The total of this ListApplicationDetailsResponse.
        :type total: int
        """
        self._total = total

    @property
    def x_trace_id(self):
        r"""Gets the x_trace_id of this ListApplicationDetailsResponse.

        :return: The x_trace_id of this ListApplicationDetailsResponse.
        :rtype: str
        """
        return self._x_trace_id

    @x_trace_id.setter
    def x_trace_id(self, x_trace_id):
        r"""Sets the x_trace_id of this ListApplicationDetailsResponse.

        :param x_trace_id: The x_trace_id of this ListApplicationDetailsResponse.
        :type x_trace_id: str
        """
        self._x_trace_id = x_trace_id

    def to_dict(self):
        import warnings
        warnings.warn("ListApplicationDetailsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListApplicationDetailsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
