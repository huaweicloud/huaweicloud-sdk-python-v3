# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateDeploymentJobsParams:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'function': 'FGSDeploymentJobsParam',
        'cci': 'CciDeploymentJobsParam'
    }

    attribute_map = {
        'function': 'function',
        'cci': 'cci'
    }

    def __init__(self, function=None, cci=None):
        """CreateDeploymentJobsParams

        The model defined in huaweicloud sdk

        :param function: 
        :type function: :class:`huaweicloudsdkdevstar.v1.FGSDeploymentJobsParam`
        :param cci: 
        :type cci: :class:`huaweicloudsdkdevstar.v1.CciDeploymentJobsParam`
        """
        
        

        self._function = None
        self._cci = None
        self.discriminator = None

        if function is not None:
            self.function = function
        if cci is not None:
            self.cci = cci

    @property
    def function(self):
        """Gets the function of this CreateDeploymentJobsParams.


        :return: The function of this CreateDeploymentJobsParams.
        :rtype: :class:`huaweicloudsdkdevstar.v1.FGSDeploymentJobsParam`
        """
        return self._function

    @function.setter
    def function(self, function):
        """Sets the function of this CreateDeploymentJobsParams.


        :param function: The function of this CreateDeploymentJobsParams.
        :type function: :class:`huaweicloudsdkdevstar.v1.FGSDeploymentJobsParam`
        """
        self._function = function

    @property
    def cci(self):
        """Gets the cci of this CreateDeploymentJobsParams.


        :return: The cci of this CreateDeploymentJobsParams.
        :rtype: :class:`huaweicloudsdkdevstar.v1.CciDeploymentJobsParam`
        """
        return self._cci

    @cci.setter
    def cci(self, cci):
        """Sets the cci of this CreateDeploymentJobsParams.


        :param cci: The cci of this CreateDeploymentJobsParams.
        :type cci: :class:`huaweicloudsdkdevstar.v1.CciDeploymentJobsParam`
        """
        self._cci = cci

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
        if not isinstance(other, CreateDeploymentJobsParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
