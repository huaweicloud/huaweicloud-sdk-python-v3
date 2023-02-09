# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateFlowLogReqBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'flow_log': 'CreateFlowLogReq'
    }

    attribute_map = {
        'flow_log': 'flow_log'
    }

    def __init__(self, flow_log=None):
        """CreateFlowLogReqBody

        The model defined in huaweicloud sdk

        :param flow_log: 
        :type flow_log: :class:`huaweicloudsdkvpc.v2.CreateFlowLogReq`
        """
        
        

        self._flow_log = None
        self.discriminator = None

        self.flow_log = flow_log

    @property
    def flow_log(self):
        """Gets the flow_log of this CreateFlowLogReqBody.

        :return: The flow_log of this CreateFlowLogReqBody.
        :rtype: :class:`huaweicloudsdkvpc.v2.CreateFlowLogReq`
        """
        return self._flow_log

    @flow_log.setter
    def flow_log(self, flow_log):
        """Sets the flow_log of this CreateFlowLogReqBody.

        :param flow_log: The flow_log of this CreateFlowLogReqBody.
        :type flow_log: :class:`huaweicloudsdkvpc.v2.CreateFlowLogReq`
        """
        self._flow_log = flow_log

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
        if not isinstance(other, CreateFlowLogReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
