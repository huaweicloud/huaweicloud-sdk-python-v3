# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StartAnalysisSessionRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'collect_request_id': 'str'
    }

    attribute_map = {
        'collect_request_id': 'collect_request_id'
    }

    def __init__(self, collect_request_id=None):
        r"""StartAnalysisSessionRequestBody

        The model defined in huaweicloud sdk

        :param collect_request_id: 收集会话请求ID
        :type collect_request_id: str
        """
        
        

        self._collect_request_id = None
        self.discriminator = None

        self.collect_request_id = collect_request_id

    @property
    def collect_request_id(self):
        r"""Gets the collect_request_id of this StartAnalysisSessionRequestBody.

        收集会话请求ID

        :return: The collect_request_id of this StartAnalysisSessionRequestBody.
        :rtype: str
        """
        return self._collect_request_id

    @collect_request_id.setter
    def collect_request_id(self, collect_request_id):
        r"""Sets the collect_request_id of this StartAnalysisSessionRequestBody.

        收集会话请求ID

        :param collect_request_id: The collect_request_id of this StartAnalysisSessionRequestBody.
        :type collect_request_id: str
        """
        self._collect_request_id = collect_request_id

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
        if not isinstance(other, StartAnalysisSessionRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
