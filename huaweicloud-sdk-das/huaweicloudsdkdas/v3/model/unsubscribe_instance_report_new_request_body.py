# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UnsubscribeInstanceReportNewRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'subscribe_id': 'str'
    }

    attribute_map = {
        'subscribe_id': 'subscribe_id'
    }

    def __init__(self, subscribe_id=None):
        r"""UnsubscribeInstanceReportNewRequestBody

        The model defined in huaweicloud sdk

        :param subscribe_id: 订阅ID
        :type subscribe_id: str
        """
        
        

        self._subscribe_id = None
        self.discriminator = None

        self.subscribe_id = subscribe_id

    @property
    def subscribe_id(self):
        r"""Gets the subscribe_id of this UnsubscribeInstanceReportNewRequestBody.

        订阅ID

        :return: The subscribe_id of this UnsubscribeInstanceReportNewRequestBody.
        :rtype: str
        """
        return self._subscribe_id

    @subscribe_id.setter
    def subscribe_id(self, subscribe_id):
        r"""Sets the subscribe_id of this UnsubscribeInstanceReportNewRequestBody.

        订阅ID

        :param subscribe_id: The subscribe_id of this UnsubscribeInstanceReportNewRequestBody.
        :type subscribe_id: str
        """
        self._subscribe_id = subscribe_id

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
        if not isinstance(other, UnsubscribeInstanceReportNewRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
