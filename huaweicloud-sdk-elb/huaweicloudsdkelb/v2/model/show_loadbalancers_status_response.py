# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowLoadbalancersStatusResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'statuses': 'StatusResp'
    }

    attribute_map = {
        'statuses': 'statuses'
    }

    def __init__(self, statuses=None):
        """ShowLoadbalancersStatusResponse

        The model defined in huaweicloud sdk

        :param statuses: 
        :type statuses: :class:`huaweicloudsdkelb.v2.StatusResp`
        """
        
        super(ShowLoadbalancersStatusResponse, self).__init__()

        self._statuses = None
        self.discriminator = None

        if statuses is not None:
            self.statuses = statuses

    @property
    def statuses(self):
        """Gets the statuses of this ShowLoadbalancersStatusResponse.

        :return: The statuses of this ShowLoadbalancersStatusResponse.
        :rtype: :class:`huaweicloudsdkelb.v2.StatusResp`
        """
        return self._statuses

    @statuses.setter
    def statuses(self, statuses):
        """Sets the statuses of this ShowLoadbalancersStatusResponse.

        :param statuses: The statuses of this ShowLoadbalancersStatusResponse.
        :type statuses: :class:`huaweicloudsdkelb.v2.StatusResp`
        """
        self._statuses = statuses

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
        if not isinstance(other, ShowLoadbalancersStatusResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
