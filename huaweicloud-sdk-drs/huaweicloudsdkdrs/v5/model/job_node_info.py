# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobNodeInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'spec': 'JobNodeSpecInfo',
        'vpc': 'JobNodeVpcInfo'
    }

    attribute_map = {
        'spec': 'spec',
        'vpc': 'vpc'
    }

    def __init__(self, spec=None, vpc=None):
        """JobNodeInfo

        The model defined in huaweicloud sdk

        :param spec: 
        :type spec: :class:`huaweicloudsdkdrs.v5.JobNodeSpecInfo`
        :param vpc: 
        :type vpc: :class:`huaweicloudsdkdrs.v5.JobNodeVpcInfo`
        """
        
        

        self._spec = None
        self._vpc = None
        self.discriminator = None

        self.spec = spec
        if vpc is not None:
            self.vpc = vpc

    @property
    def spec(self):
        """Gets the spec of this JobNodeInfo.

        :return: The spec of this JobNodeInfo.
        :rtype: :class:`huaweicloudsdkdrs.v5.JobNodeSpecInfo`
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        """Sets the spec of this JobNodeInfo.

        :param spec: The spec of this JobNodeInfo.
        :type spec: :class:`huaweicloudsdkdrs.v5.JobNodeSpecInfo`
        """
        self._spec = spec

    @property
    def vpc(self):
        """Gets the vpc of this JobNodeInfo.

        :return: The vpc of this JobNodeInfo.
        :rtype: :class:`huaweicloudsdkdrs.v5.JobNodeVpcInfo`
        """
        return self._vpc

    @vpc.setter
    def vpc(self, vpc):
        """Sets the vpc of this JobNodeInfo.

        :param vpc: The vpc of this JobNodeInfo.
        :type vpc: :class:`huaweicloudsdkdrs.v5.JobNodeVpcInfo`
        """
        self._vpc = vpc

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
        if not isinstance(other, JobNodeInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
