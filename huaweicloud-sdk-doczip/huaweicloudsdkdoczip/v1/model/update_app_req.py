# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateAppReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'basic_info': 'ApplicationBasicInfo',
        'system_config': 'SysconfigInfo',
        'blocks_config': 'object',
        'idp_detail': 'IDPDetailVo'
    }

    attribute_map = {
        'basic_info': 'basic_info',
        'system_config': 'system_config',
        'blocks_config': 'blocks_config',
        'idp_detail': 'idp_detail'
    }

    def __init__(self, basic_info=None, system_config=None, blocks_config=None, idp_detail=None):
        r"""UpdateAppReq

        The model defined in huaweicloud sdk

        :param basic_info: 
        :type basic_info: :class:`huaweicloudsdkdoczip.v1.ApplicationBasicInfo`
        :param system_config: 
        :type system_config: :class:`huaweicloudsdkdoczip.v1.SysconfigInfo`
        :param blocks_config: **参数解释**： 文档块配置。 支持more和basic两个列表，分别标识基础文档块和扩展文档块。 - basic：基础文档块列表，元素为文档块对象。 - more：扩展文档块列表，元素为文档块对象或分组标题对象。 - release_state：发布状态，true为已发布，false为未发布。 文档块对象支持字段如下： - code：文档块编码。 - pinyin：文档块简称。 - quanpin：文档块全程。 - name：文档块名称。 - icon：文档块图标。 - show：是否展示： true为展示，false为不展示。 - source：文档块来源，0标识系统文档块，分组标题对象中1标识自定义分组。 - darkIcon：暗黑模式文档块图标。 - key：文档块key值。 - data：文档块附加数据，可为字符串或对象（可选）。 分组标题对象字段如下： - source：分组来源。 - title：分组标题。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type blocks_config: object
        :param idp_detail: 
        :type idp_detail: :class:`huaweicloudsdkdoczip.v1.IDPDetailVo`
        """
        
        

        self._basic_info = None
        self._system_config = None
        self._blocks_config = None
        self._idp_detail = None
        self.discriminator = None

        if basic_info is not None:
            self.basic_info = basic_info
        if system_config is not None:
            self.system_config = system_config
        if blocks_config is not None:
            self.blocks_config = blocks_config
        if idp_detail is not None:
            self.idp_detail = idp_detail

    @property
    def basic_info(self):
        r"""Gets the basic_info of this UpdateAppReq.

        :return: The basic_info of this UpdateAppReq.
        :rtype: :class:`huaweicloudsdkdoczip.v1.ApplicationBasicInfo`
        """
        return self._basic_info

    @basic_info.setter
    def basic_info(self, basic_info):
        r"""Sets the basic_info of this UpdateAppReq.

        :param basic_info: The basic_info of this UpdateAppReq.
        :type basic_info: :class:`huaweicloudsdkdoczip.v1.ApplicationBasicInfo`
        """
        self._basic_info = basic_info

    @property
    def system_config(self):
        r"""Gets the system_config of this UpdateAppReq.

        :return: The system_config of this UpdateAppReq.
        :rtype: :class:`huaweicloudsdkdoczip.v1.SysconfigInfo`
        """
        return self._system_config

    @system_config.setter
    def system_config(self, system_config):
        r"""Sets the system_config of this UpdateAppReq.

        :param system_config: The system_config of this UpdateAppReq.
        :type system_config: :class:`huaweicloudsdkdoczip.v1.SysconfigInfo`
        """
        self._system_config = system_config

    @property
    def blocks_config(self):
        r"""Gets the blocks_config of this UpdateAppReq.

        **参数解释**： 文档块配置。 支持more和basic两个列表，分别标识基础文档块和扩展文档块。 - basic：基础文档块列表，元素为文档块对象。 - more：扩展文档块列表，元素为文档块对象或分组标题对象。 - release_state：发布状态，true为已发布，false为未发布。 文档块对象支持字段如下： - code：文档块编码。 - pinyin：文档块简称。 - quanpin：文档块全程。 - name：文档块名称。 - icon：文档块图标。 - show：是否展示： true为展示，false为不展示。 - source：文档块来源，0标识系统文档块，分组标题对象中1标识自定义分组。 - darkIcon：暗黑模式文档块图标。 - key：文档块key值。 - data：文档块附加数据，可为字符串或对象（可选）。 分组标题对象字段如下： - source：分组来源。 - title：分组标题。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The blocks_config of this UpdateAppReq.
        :rtype: object
        """
        return self._blocks_config

    @blocks_config.setter
    def blocks_config(self, blocks_config):
        r"""Sets the blocks_config of this UpdateAppReq.

        **参数解释**： 文档块配置。 支持more和basic两个列表，分别标识基础文档块和扩展文档块。 - basic：基础文档块列表，元素为文档块对象。 - more：扩展文档块列表，元素为文档块对象或分组标题对象。 - release_state：发布状态，true为已发布，false为未发布。 文档块对象支持字段如下： - code：文档块编码。 - pinyin：文档块简称。 - quanpin：文档块全程。 - name：文档块名称。 - icon：文档块图标。 - show：是否展示： true为展示，false为不展示。 - source：文档块来源，0标识系统文档块，分组标题对象中1标识自定义分组。 - darkIcon：暗黑模式文档块图标。 - key：文档块key值。 - data：文档块附加数据，可为字符串或对象（可选）。 分组标题对象字段如下： - source：分组来源。 - title：分组标题。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param blocks_config: The blocks_config of this UpdateAppReq.
        :type blocks_config: object
        """
        self._blocks_config = blocks_config

    @property
    def idp_detail(self):
        r"""Gets the idp_detail of this UpdateAppReq.

        :return: The idp_detail of this UpdateAppReq.
        :rtype: :class:`huaweicloudsdkdoczip.v1.IDPDetailVo`
        """
        return self._idp_detail

    @idp_detail.setter
    def idp_detail(self, idp_detail):
        r"""Sets the idp_detail of this UpdateAppReq.

        :param idp_detail: The idp_detail of this UpdateAppReq.
        :type idp_detail: :class:`huaweicloudsdkdoczip.v1.IDPDetailVo`
        """
        self._idp_detail = idp_detail

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
        if not isinstance(other, UpdateAppReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
