# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchBaselineIpdIssuesParam:

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
        'attribute': 'BatchBaselineIpdIssuesParamAttribute'
    }

    attribute_map = {
        'id': 'id',
        'attribute': 'attribute'
    }

    def __init__(self, id=None, attribute=None):
        r"""BatchBaselineIpdIssuesParam

        The model defined in huaweicloud sdk

        :param id: 需要基线的工作项ID数组。可以通过查询工作项列表或者查询树状工作项接口获取，响应消息体中的id字段的值就是工作项ID。
        :type id: list[str]
        :param attribute: 
        :type attribute: :class:`huaweicloudsdkprojectman.v4.BatchBaselineIpdIssuesParamAttribute`
        """
        
        

        self._id = None
        self._attribute = None
        self.discriminator = None

        self.id = id
        self.attribute = attribute

    @property
    def id(self):
        r"""Gets the id of this BatchBaselineIpdIssuesParam.

        需要基线的工作项ID数组。可以通过查询工作项列表或者查询树状工作项接口获取，响应消息体中的id字段的值就是工作项ID。

        :return: The id of this BatchBaselineIpdIssuesParam.
        :rtype: list[str]
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this BatchBaselineIpdIssuesParam.

        需要基线的工作项ID数组。可以通过查询工作项列表或者查询树状工作项接口获取，响应消息体中的id字段的值就是工作项ID。

        :param id: The id of this BatchBaselineIpdIssuesParam.
        :type id: list[str]
        """
        self._id = id

    @property
    def attribute(self):
        r"""Gets the attribute of this BatchBaselineIpdIssuesParam.

        :return: The attribute of this BatchBaselineIpdIssuesParam.
        :rtype: :class:`huaweicloudsdkprojectman.v4.BatchBaselineIpdIssuesParamAttribute`
        """
        return self._attribute

    @attribute.setter
    def attribute(self, attribute):
        r"""Sets the attribute of this BatchBaselineIpdIssuesParam.

        :param attribute: The attribute of this BatchBaselineIpdIssuesParam.
        :type attribute: :class:`huaweicloudsdkprojectman.v4.BatchBaselineIpdIssuesParamAttribute`
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
        if not isinstance(other, BatchBaselineIpdIssuesParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
