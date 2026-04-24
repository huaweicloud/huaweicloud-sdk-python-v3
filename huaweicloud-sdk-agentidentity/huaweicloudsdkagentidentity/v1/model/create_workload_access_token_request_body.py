# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateWorkloadAccessTokenRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workload_name': 'str'
    }

    attribute_map = {
        'workload_name': 'workload_name'
    }

    def __init__(self, workload_name=None):
        r"""CreateWorkloadAccessTokenRequestBody

        The model defined in huaweicloud sdk

        :param workload_name: The unique identifier for the registered workload
        :type workload_name: str
        """
        
        

        self._workload_name = None
        self.discriminator = None

        self.workload_name = workload_name

    @property
    def workload_name(self):
        r"""Gets the workload_name of this CreateWorkloadAccessTokenRequestBody.

        The unique identifier for the registered workload

        :return: The workload_name of this CreateWorkloadAccessTokenRequestBody.
        :rtype: str
        """
        return self._workload_name

    @workload_name.setter
    def workload_name(self, workload_name):
        r"""Sets the workload_name of this CreateWorkloadAccessTokenRequestBody.

        The unique identifier for the registered workload

        :param workload_name: The workload_name of this CreateWorkloadAccessTokenRequestBody.
        :type workload_name: str
        """
        self._workload_name = workload_name

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
        if not isinstance(other, CreateWorkloadAccessTokenRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
