# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StartAndStopDeploymentPodResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'pod_id': 'str'
    }

    attribute_map = {
        'pod_id': 'pod_id'
    }

    def __init__(self, pod_id=None):
        """StartAndStopDeploymentPodResponse

        The model defined in huaweicloud sdk

        :param pod_id: pod的ID
        :type pod_id: str
        """
        
        super(StartAndStopDeploymentPodResponse, self).__init__()

        self._pod_id = None
        self.discriminator = None

        if pod_id is not None:
            self.pod_id = pod_id

    @property
    def pod_id(self):
        """Gets the pod_id of this StartAndStopDeploymentPodResponse.

        pod的ID

        :return: The pod_id of this StartAndStopDeploymentPodResponse.
        :rtype: str
        """
        return self._pod_id

    @pod_id.setter
    def pod_id(self, pod_id):
        """Sets the pod_id of this StartAndStopDeploymentPodResponse.

        pod的ID

        :param pod_id: The pod_id of this StartAndStopDeploymentPodResponse.
        :type pod_id: str
        """
        self._pod_id = pod_id

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
        if not isinstance(other, StartAndStopDeploymentPodResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
