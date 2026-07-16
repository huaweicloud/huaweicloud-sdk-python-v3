# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowWorkflowLabelsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'offset': 'int',
        'order': 'str',
        'sort_by': 'str',
        'template_id': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'order': 'order',
        'sort_by': 'sort_by',
        'template_id': 'template_id'
    }

    def __init__(self, limit=None, offset=None, order=None, sort_by=None, template_id=None):
        r"""ShowWorkflowLabelsRequest

        The model defined in huaweicloud sdk

        :param limit: 返回的数据条目数。
        :type limit: int
        :param offset: 数据条目偏移量。
        :type offset: int
        :param order: instance order
        :type order: str
        :param sort_by: 指定排序字段。  可选值： - user_name：IAM用户名称 - create_time：创建时间
        :type sort_by: str
        :param template_id: **参数解释**：工作流模板ID。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type template_id: str
        """
        
        

        self._limit = None
        self._offset = None
        self._order = None
        self._sort_by = None
        self._template_id = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if order is not None:
            self.order = order
        if sort_by is not None:
            self.sort_by = sort_by
        if template_id is not None:
            self.template_id = template_id

    @property
    def limit(self):
        r"""Gets the limit of this ShowWorkflowLabelsRequest.

        返回的数据条目数。

        :return: The limit of this ShowWorkflowLabelsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowWorkflowLabelsRequest.

        返回的数据条目数。

        :param limit: The limit of this ShowWorkflowLabelsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ShowWorkflowLabelsRequest.

        数据条目偏移量。

        :return: The offset of this ShowWorkflowLabelsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ShowWorkflowLabelsRequest.

        数据条目偏移量。

        :param offset: The offset of this ShowWorkflowLabelsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def order(self):
        r"""Gets the order of this ShowWorkflowLabelsRequest.

        instance order

        :return: The order of this ShowWorkflowLabelsRequest.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        r"""Sets the order of this ShowWorkflowLabelsRequest.

        instance order

        :param order: The order of this ShowWorkflowLabelsRequest.
        :type order: str
        """
        self._order = order

    @property
    def sort_by(self):
        r"""Gets the sort_by of this ShowWorkflowLabelsRequest.

        指定排序字段。  可选值： - user_name：IAM用户名称 - create_time：创建时间

        :return: The sort_by of this ShowWorkflowLabelsRequest.
        :rtype: str
        """
        return self._sort_by

    @sort_by.setter
    def sort_by(self, sort_by):
        r"""Sets the sort_by of this ShowWorkflowLabelsRequest.

        指定排序字段。  可选值： - user_name：IAM用户名称 - create_time：创建时间

        :param sort_by: The sort_by of this ShowWorkflowLabelsRequest.
        :type sort_by: str
        """
        self._sort_by = sort_by

    @property
    def template_id(self):
        r"""Gets the template_id of this ShowWorkflowLabelsRequest.

        **参数解释**：工作流模板ID。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The template_id of this ShowWorkflowLabelsRequest.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        r"""Sets the template_id of this ShowWorkflowLabelsRequest.

        **参数解释**：工作流模板ID。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param template_id: The template_id of this ShowWorkflowLabelsRequest.
        :type template_id: str
        """
        self._template_id = template_id

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
        if not isinstance(other, ShowWorkflowLabelsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
