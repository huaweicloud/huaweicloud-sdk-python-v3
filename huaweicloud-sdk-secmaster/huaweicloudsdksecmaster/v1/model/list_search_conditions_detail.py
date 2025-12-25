# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSearchConditionsDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'condition_id': 'str',
        'condition_name': 'str'
    }

    attribute_map = {
        'condition_id': 'condition_id',
        'condition_name': 'condition_name'
    }

    def __init__(self, condition_id=None, condition_name=None):
        r"""ListSearchConditionsDetail

        The model defined in huaweicloud sdk

        :param condition_id: 检索条件ID
        :type condition_id: str
        :param condition_name: 检索条件名称
        :type condition_name: str
        """
        
        

        self._condition_id = None
        self._condition_name = None
        self.discriminator = None

        self.condition_id = condition_id
        self.condition_name = condition_name

    @property
    def condition_id(self):
        r"""Gets the condition_id of this ListSearchConditionsDetail.

        检索条件ID

        :return: The condition_id of this ListSearchConditionsDetail.
        :rtype: str
        """
        return self._condition_id

    @condition_id.setter
    def condition_id(self, condition_id):
        r"""Sets the condition_id of this ListSearchConditionsDetail.

        检索条件ID

        :param condition_id: The condition_id of this ListSearchConditionsDetail.
        :type condition_id: str
        """
        self._condition_id = condition_id

    @property
    def condition_name(self):
        r"""Gets the condition_name of this ListSearchConditionsDetail.

        检索条件名称

        :return: The condition_name of this ListSearchConditionsDetail.
        :rtype: str
        """
        return self._condition_name

    @condition_name.setter
    def condition_name(self, condition_name):
        r"""Sets the condition_name of this ListSearchConditionsDetail.

        检索条件名称

        :param condition_name: The condition_name of this ListSearchConditionsDetail.
        :type condition_name: str
        """
        self._condition_name = condition_name

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
        if not isinstance(other, ListSearchConditionsDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
