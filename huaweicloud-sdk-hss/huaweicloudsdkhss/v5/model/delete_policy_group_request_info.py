# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeletePolicyGroupRequestInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id_list': 'list[str]'
    }

    attribute_map = {
        'id_list': 'id_list'
    }

    def __init__(self, id_list=None):
        r"""DeletePolicyGroupRequestInfo

        The model defined in huaweicloud sdk

        :param id_list: **参数解释**: 需要被删除的策略组的策略组ID列表，仅支持删除非默认并且未关联服务器的策略组 **约束限制**: 需要使用 ListPolicyGroup 接口查询旗舰版和容器版策略组，在 ListPolicyGroup 接口的响应体中，deletable 等于 true 的 group_id 是可以被删除的策略组ID **取值范围**: 最少1条，最多50条 **默认取值**: 不涉及
        :type id_list: list[str]
        """
        
        

        self._id_list = None
        self.discriminator = None

        self.id_list = id_list

    @property
    def id_list(self):
        r"""Gets the id_list of this DeletePolicyGroupRequestInfo.

        **参数解释**: 需要被删除的策略组的策略组ID列表，仅支持删除非默认并且未关联服务器的策略组 **约束限制**: 需要使用 ListPolicyGroup 接口查询旗舰版和容器版策略组，在 ListPolicyGroup 接口的响应体中，deletable 等于 true 的 group_id 是可以被删除的策略组ID **取值范围**: 最少1条，最多50条 **默认取值**: 不涉及

        :return: The id_list of this DeletePolicyGroupRequestInfo.
        :rtype: list[str]
        """
        return self._id_list

    @id_list.setter
    def id_list(self, id_list):
        r"""Sets the id_list of this DeletePolicyGroupRequestInfo.

        **参数解释**: 需要被删除的策略组的策略组ID列表，仅支持删除非默认并且未关联服务器的策略组 **约束限制**: 需要使用 ListPolicyGroup 接口查询旗舰版和容器版策略组，在 ListPolicyGroup 接口的响应体中，deletable 等于 true 的 group_id 是可以被删除的策略组ID **取值范围**: 最少1条，最多50条 **默认取值**: 不涉及

        :param id_list: The id_list of this DeletePolicyGroupRequestInfo.
        :type id_list: list[str]
        """
        self._id_list = id_list

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
        if not isinstance(other, DeletePolicyGroupRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
