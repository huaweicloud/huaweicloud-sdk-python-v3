# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HandleAffectBaselineInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'host_id': 'str',
        'host_name': 'str',
        'public_ip': 'str',
        'private_ip': 'str',
        'asset_value': 'str',
        'check_type': 'str',
        'standard': 'str',
        'tag': 'str',
        'check_rule_name': 'str'
    }

    attribute_map = {
        'host_id': 'host_id',
        'host_name': 'host_name',
        'public_ip': 'public_ip',
        'private_ip': 'private_ip',
        'asset_value': 'asset_value',
        'check_type': 'check_type',
        'standard': 'standard',
        'tag': 'tag',
        'check_rule_name': 'check_rule_name'
    }

    def __init__(self, host_id=None, host_name=None, public_ip=None, private_ip=None, asset_value=None, check_type=None, standard=None, tag=None, check_rule_name=None):
        r"""HandleAffectBaselineInfo

        The model defined in huaweicloud sdk

        :param host_id: **参数解释** 主机id **取值范围**   字符长度1-256位
        :type host_id: str
        :param host_name: **参数解释** 服务器名称 **取值范围**   字符长度1-64位
        :type host_name: str
        :param public_ip: **参数解释** 服务器公网ip **取值范围**   字符长度0-128位
        :type public_ip: str
        :param private_ip: **参数解释** 服务器私网ip **取值范围**   字符长度0-2048位
        :type private_ip: str
        :param asset_value: **参数解释** 资产重要性，包含如下3种 **取值范围**   - important ：重要资产 - common    ：一般资产 - test      ：测试资产
        :type asset_value: str
        :param check_type: **参数解释** 基线检查的基线名称 **取值范围**   字符长度0-255位
        :type check_type: str
        :param standard: **参数解释** 标准类型，包含如下3种 **取值范围**   - cn_standard : 等保合规标准 - hw_standard : 云安全实践标准 - cis_standard : 通用安全标准
        :type standard: str
        :param tag: **参数解释** 基线检查中检查项的检查类型 **取值范围**  字符长度0-128位
        :type tag: str
        :param check_rule_name: **参数解释** 基线检查中检查项的名称 **取值范围**  字符长度0-2048位
        :type check_rule_name: str
        """
        
        

        self._host_id = None
        self._host_name = None
        self._public_ip = None
        self._private_ip = None
        self._asset_value = None
        self._check_type = None
        self._standard = None
        self._tag = None
        self._check_rule_name = None
        self.discriminator = None

        if host_id is not None:
            self.host_id = host_id
        if host_name is not None:
            self.host_name = host_name
        if public_ip is not None:
            self.public_ip = public_ip
        if private_ip is not None:
            self.private_ip = private_ip
        if asset_value is not None:
            self.asset_value = asset_value
        if check_type is not None:
            self.check_type = check_type
        if standard is not None:
            self.standard = standard
        if tag is not None:
            self.tag = tag
        if check_rule_name is not None:
            self.check_rule_name = check_rule_name

    @property
    def host_id(self):
        r"""Gets the host_id of this HandleAffectBaselineInfo.

        **参数解释** 主机id **取值范围**   字符长度1-256位

        :return: The host_id of this HandleAffectBaselineInfo.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this HandleAffectBaselineInfo.

        **参数解释** 主机id **取值范围**   字符长度1-256位

        :param host_id: The host_id of this HandleAffectBaselineInfo.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def host_name(self):
        r"""Gets the host_name of this HandleAffectBaselineInfo.

        **参数解释** 服务器名称 **取值范围**   字符长度1-64位

        :return: The host_name of this HandleAffectBaselineInfo.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this HandleAffectBaselineInfo.

        **参数解释** 服务器名称 **取值范围**   字符长度1-64位

        :param host_name: The host_name of this HandleAffectBaselineInfo.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def public_ip(self):
        r"""Gets the public_ip of this HandleAffectBaselineInfo.

        **参数解释** 服务器公网ip **取值范围**   字符长度0-128位

        :return: The public_ip of this HandleAffectBaselineInfo.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this HandleAffectBaselineInfo.

        **参数解释** 服务器公网ip **取值范围**   字符长度0-128位

        :param public_ip: The public_ip of this HandleAffectBaselineInfo.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def private_ip(self):
        r"""Gets the private_ip of this HandleAffectBaselineInfo.

        **参数解释** 服务器私网ip **取值范围**   字符长度0-2048位

        :return: The private_ip of this HandleAffectBaselineInfo.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        r"""Sets the private_ip of this HandleAffectBaselineInfo.

        **参数解释** 服务器私网ip **取值范围**   字符长度0-2048位

        :param private_ip: The private_ip of this HandleAffectBaselineInfo.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def asset_value(self):
        r"""Gets the asset_value of this HandleAffectBaselineInfo.

        **参数解释** 资产重要性，包含如下3种 **取值范围**   - important ：重要资产 - common    ：一般资产 - test      ：测试资产

        :return: The asset_value of this HandleAffectBaselineInfo.
        :rtype: str
        """
        return self._asset_value

    @asset_value.setter
    def asset_value(self, asset_value):
        r"""Sets the asset_value of this HandleAffectBaselineInfo.

        **参数解释** 资产重要性，包含如下3种 **取值范围**   - important ：重要资产 - common    ：一般资产 - test      ：测试资产

        :param asset_value: The asset_value of this HandleAffectBaselineInfo.
        :type asset_value: str
        """
        self._asset_value = asset_value

    @property
    def check_type(self):
        r"""Gets the check_type of this HandleAffectBaselineInfo.

        **参数解释** 基线检查的基线名称 **取值范围**   字符长度0-255位

        :return: The check_type of this HandleAffectBaselineInfo.
        :rtype: str
        """
        return self._check_type

    @check_type.setter
    def check_type(self, check_type):
        r"""Sets the check_type of this HandleAffectBaselineInfo.

        **参数解释** 基线检查的基线名称 **取值范围**   字符长度0-255位

        :param check_type: The check_type of this HandleAffectBaselineInfo.
        :type check_type: str
        """
        self._check_type = check_type

    @property
    def standard(self):
        r"""Gets the standard of this HandleAffectBaselineInfo.

        **参数解释** 标准类型，包含如下3种 **取值范围**   - cn_standard : 等保合规标准 - hw_standard : 云安全实践标准 - cis_standard : 通用安全标准

        :return: The standard of this HandleAffectBaselineInfo.
        :rtype: str
        """
        return self._standard

    @standard.setter
    def standard(self, standard):
        r"""Sets the standard of this HandleAffectBaselineInfo.

        **参数解释** 标准类型，包含如下3种 **取值范围**   - cn_standard : 等保合规标准 - hw_standard : 云安全实践标准 - cis_standard : 通用安全标准

        :param standard: The standard of this HandleAffectBaselineInfo.
        :type standard: str
        """
        self._standard = standard

    @property
    def tag(self):
        r"""Gets the tag of this HandleAffectBaselineInfo.

        **参数解释** 基线检查中检查项的检查类型 **取值范围**  字符长度0-128位

        :return: The tag of this HandleAffectBaselineInfo.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        r"""Sets the tag of this HandleAffectBaselineInfo.

        **参数解释** 基线检查中检查项的检查类型 **取值范围**  字符长度0-128位

        :param tag: The tag of this HandleAffectBaselineInfo.
        :type tag: str
        """
        self._tag = tag

    @property
    def check_rule_name(self):
        r"""Gets the check_rule_name of this HandleAffectBaselineInfo.

        **参数解释** 基线检查中检查项的名称 **取值范围**  字符长度0-2048位

        :return: The check_rule_name of this HandleAffectBaselineInfo.
        :rtype: str
        """
        return self._check_rule_name

    @check_rule_name.setter
    def check_rule_name(self, check_rule_name):
        r"""Sets the check_rule_name of this HandleAffectBaselineInfo.

        **参数解释** 基线检查中检查项的名称 **取值范围**  字符长度0-2048位

        :param check_rule_name: The check_rule_name of this HandleAffectBaselineInfo.
        :type check_rule_name: str
        """
        self._check_rule_name = check_rule_name

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
        if not isinstance(other, HandleAffectBaselineInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
