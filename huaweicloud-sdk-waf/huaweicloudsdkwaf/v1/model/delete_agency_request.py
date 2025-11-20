# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteAgencyRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'purged': 'bool',
        'role_id_list': 'list[str]'
    }

    attribute_map = {
        'purged': 'purged',
        'role_id_list': 'role_id_list'
    }

    def __init__(self, purged=None, role_id_list=None):
        r"""DeleteAgencyRequest

        The model defined in huaweicloud sdk

        :param purged: **参数解释：** purged取值为true时，会同步删除在IAM处创建的premium_waf_svc_trust委托，purged取值为false时，不会同步删除在IAM处创建的premium_waf_svc_trust委托 **约束限制：** 不涉及 **取值范围：** - true - false  **默认取值：** 不涉及
        :type purged: bool
        :param role_id_list: **参数解释：** 待删除的代理id **约束限制：** 不涉及 **取值范围：** 从 “查询独享引擎代理”接口的返回结果中，选取需要删除代理的id值 **默认取值：** 不涉及
        :type role_id_list: list[str]
        """
        
        

        self._purged = None
        self._role_id_list = None
        self.discriminator = None

        if purged is not None:
            self.purged = purged
        if role_id_list is not None:
            self.role_id_list = role_id_list

    @property
    def purged(self):
        r"""Gets the purged of this DeleteAgencyRequest.

        **参数解释：** purged取值为true时，会同步删除在IAM处创建的premium_waf_svc_trust委托，purged取值为false时，不会同步删除在IAM处创建的premium_waf_svc_trust委托 **约束限制：** 不涉及 **取值范围：** - true - false  **默认取值：** 不涉及

        :return: The purged of this DeleteAgencyRequest.
        :rtype: bool
        """
        return self._purged

    @purged.setter
    def purged(self, purged):
        r"""Sets the purged of this DeleteAgencyRequest.

        **参数解释：** purged取值为true时，会同步删除在IAM处创建的premium_waf_svc_trust委托，purged取值为false时，不会同步删除在IAM处创建的premium_waf_svc_trust委托 **约束限制：** 不涉及 **取值范围：** - true - false  **默认取值：** 不涉及

        :param purged: The purged of this DeleteAgencyRequest.
        :type purged: bool
        """
        self._purged = purged

    @property
    def role_id_list(self):
        r"""Gets the role_id_list of this DeleteAgencyRequest.

        **参数解释：** 待删除的代理id **约束限制：** 不涉及 **取值范围：** 从 “查询独享引擎代理”接口的返回结果中，选取需要删除代理的id值 **默认取值：** 不涉及

        :return: The role_id_list of this DeleteAgencyRequest.
        :rtype: list[str]
        """
        return self._role_id_list

    @role_id_list.setter
    def role_id_list(self, role_id_list):
        r"""Sets the role_id_list of this DeleteAgencyRequest.

        **参数解释：** 待删除的代理id **约束限制：** 不涉及 **取值范围：** 从 “查询独享引擎代理”接口的返回结果中，选取需要删除代理的id值 **默认取值：** 不涉及

        :param role_id_list: The role_id_list of this DeleteAgencyRequest.
        :type role_id_list: list[str]
        """
        self._role_id_list = role_id_list

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
        if not isinstance(other, DeleteAgencyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
