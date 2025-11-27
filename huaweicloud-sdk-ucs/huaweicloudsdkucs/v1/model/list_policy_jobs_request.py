# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPolicyJobsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'kind': 'str'
    }

    attribute_map = {
        'kind': 'kind'
    }

    def __init__(self, kind=None):
        r"""ListPolicyJobsRequest

        The model defined in huaweicloud sdk

        :param kind: 指定的任务类型，没有则使用默认值EnablePolicy
        :type kind: str
        """
        
        

        self._kind = None
        self.discriminator = None

        if kind is not None:
            self.kind = kind

    @property
    def kind(self):
        r"""Gets the kind of this ListPolicyJobsRequest.

        指定的任务类型，没有则使用默认值EnablePolicy

        :return: The kind of this ListPolicyJobsRequest.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        r"""Sets the kind of this ListPolicyJobsRequest.

        指定的任务类型，没有则使用默认值EnablePolicy

        :param kind: The kind of this ListPolicyJobsRequest.
        :type kind: str
        """
        self._kind = kind

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
        if not isinstance(other, ListPolicyJobsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
