# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchOperateChildDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'child_list': 'list[str]',
        'parent_id': 'str'
    }

    attribute_map = {
        'child_list': 'childList',
        'parent_id': 'parentId'
    }

    def __init__(self, child_list=None, parent_id=None):
        r"""BatchOperateChildDTO

        The model defined in huaweicloud sdk

        :param child_list: **参数解释：**  子节点实例ID列表。  **约束限制：**  不涉及。  **取值范围：**  -9223372036854775808到9223372036854775807的整数。  **默认取值：**  不涉及。 
        :type child_list: list[str]
        :param parent_id: **参数解释：**  父节点实例ID。  **约束限制：**  不涉及。  **取值范围：**  -9223372036854775808到9223372036854775807的整数。  **默认取值：**  不涉及。 
        :type parent_id: str
        """
        
        

        self._child_list = None
        self._parent_id = None
        self.discriminator = None

        self.child_list = child_list
        self.parent_id = parent_id

    @property
    def child_list(self):
        r"""Gets the child_list of this BatchOperateChildDTO.

        **参数解释：**  子节点实例ID列表。  **约束限制：**  不涉及。  **取值范围：**  -9223372036854775808到9223372036854775807的整数。  **默认取值：**  不涉及。 

        :return: The child_list of this BatchOperateChildDTO.
        :rtype: list[str]
        """
        return self._child_list

    @child_list.setter
    def child_list(self, child_list):
        r"""Sets the child_list of this BatchOperateChildDTO.

        **参数解释：**  子节点实例ID列表。  **约束限制：**  不涉及。  **取值范围：**  -9223372036854775808到9223372036854775807的整数。  **默认取值：**  不涉及。 

        :param child_list: The child_list of this BatchOperateChildDTO.
        :type child_list: list[str]
        """
        self._child_list = child_list

    @property
    def parent_id(self):
        r"""Gets the parent_id of this BatchOperateChildDTO.

        **参数解释：**  父节点实例ID。  **约束限制：**  不涉及。  **取值范围：**  -9223372036854775808到9223372036854775807的整数。  **默认取值：**  不涉及。 

        :return: The parent_id of this BatchOperateChildDTO.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        r"""Sets the parent_id of this BatchOperateChildDTO.

        **参数解释：**  父节点实例ID。  **约束限制：**  不涉及。  **取值范围：**  -9223372036854775808到9223372036854775807的整数。  **默认取值：**  不涉及。 

        :param parent_id: The parent_id of this BatchOperateChildDTO.
        :type parent_id: str
        """
        self._parent_id = parent_id

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
        if not isinstance(other, BatchOperateChildDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
