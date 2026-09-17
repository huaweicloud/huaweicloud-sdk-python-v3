# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchUpdateIssuesParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'list[str]',
        'attribute': 'IssueUpdateAttribute'
    }

    attribute_map = {
        'id': 'id',
        'attribute': 'attribute'
    }

    def __init__(self, id=None, attribute=None):
        r"""BatchUpdateIssuesParam

        The model defined in huaweicloud sdk

        :param id: **参数解释**： 需要更新的工作项ID数组，可通过[高级查询工作项](ListIssuesV4.xml)接口获取，响应消息体中的**id**字段的值就是工作项ID。 **约束限制**： 18~19位的数字字符串(工作项的**id**字段对应的字符串)。
        :type id: list[str]
        :param attribute: 
        :type attribute: :class:`huaweicloudsdkprojectman.v4.IssueUpdateAttribute`
        """
        
        

        self._id = None
        self._attribute = None
        self.discriminator = None

        self.id = id
        self.attribute = attribute

    @property
    def id(self):
        r"""Gets the id of this BatchUpdateIssuesParam.

        **参数解释**： 需要更新的工作项ID数组，可通过[高级查询工作项](ListIssuesV4.xml)接口获取，响应消息体中的**id**字段的值就是工作项ID。 **约束限制**： 18~19位的数字字符串(工作项的**id**字段对应的字符串)。

        :return: The id of this BatchUpdateIssuesParam.
        :rtype: list[str]
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this BatchUpdateIssuesParam.

        **参数解释**： 需要更新的工作项ID数组，可通过[高级查询工作项](ListIssuesV4.xml)接口获取，响应消息体中的**id**字段的值就是工作项ID。 **约束限制**： 18~19位的数字字符串(工作项的**id**字段对应的字符串)。

        :param id: The id of this BatchUpdateIssuesParam.
        :type id: list[str]
        """
        self._id = id

    @property
    def attribute(self):
        r"""Gets the attribute of this BatchUpdateIssuesParam.

        :return: The attribute of this BatchUpdateIssuesParam.
        :rtype: :class:`huaweicloudsdkprojectman.v4.IssueUpdateAttribute`
        """
        return self._attribute

    @attribute.setter
    def attribute(self, attribute):
        r"""Sets the attribute of this BatchUpdateIssuesParam.

        :param attribute: The attribute of this BatchUpdateIssuesParam.
        :type attribute: :class:`huaweicloudsdkprojectman.v4.IssueUpdateAttribute`
        """
        self._attribute = attribute

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
        if not isinstance(other, BatchUpdateIssuesParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
