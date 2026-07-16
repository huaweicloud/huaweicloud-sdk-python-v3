# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteInferDeploymentPodResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'pod_name': 'str'
    }

    attribute_map = {
        'pod_name': 'pod_name'
    }

    def __init__(self, pod_name=None):
        r"""DeleteInferDeploymentPodResponse

        The model defined in huaweicloud sdk

        :param pod_name: **参数解释：** pod名字。 **取值范围：** 不涉及。
        :type pod_name: str
        """
        
        super().__init__()

        self._pod_name = None
        self.discriminator = None

        if pod_name is not None:
            self.pod_name = pod_name

    @property
    def pod_name(self):
        r"""Gets the pod_name of this DeleteInferDeploymentPodResponse.

        **参数解释：** pod名字。 **取值范围：** 不涉及。

        :return: The pod_name of this DeleteInferDeploymentPodResponse.
        :rtype: str
        """
        return self._pod_name

    @pod_name.setter
    def pod_name(self, pod_name):
        r"""Sets the pod_name of this DeleteInferDeploymentPodResponse.

        **参数解释：** pod名字。 **取值范围：** 不涉及。

        :param pod_name: The pod_name of this DeleteInferDeploymentPodResponse.
        :type pod_name: str
        """
        self._pod_name = pod_name

    def to_dict(self):
        import warnings
        warnings.warn("DeleteInferDeploymentPodResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, DeleteInferDeploymentPodResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
