# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTuningResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tune_result': 'AdviceResult'
    }

    attribute_map = {
        'tune_result': 'tune_result'
    }

    def __init__(self, tune_result=None):
        r"""ShowTuningResponse

        The model defined in huaweicloud sdk

        :param tune_result: 
        :type tune_result: :class:`huaweicloudsdkdas.v3.AdviceResult`
        """
        
        super(ShowTuningResponse, self).__init__()

        self._tune_result = None
        self.discriminator = None

        if tune_result is not None:
            self.tune_result = tune_result

    @property
    def tune_result(self):
        r"""Gets the tune_result of this ShowTuningResponse.

        :return: The tune_result of this ShowTuningResponse.
        :rtype: :class:`huaweicloudsdkdas.v3.AdviceResult`
        """
        return self._tune_result

    @tune_result.setter
    def tune_result(self, tune_result):
        r"""Sets the tune_result of this ShowTuningResponse.

        :param tune_result: The tune_result of this ShowTuningResponse.
        :type tune_result: :class:`huaweicloudsdkdas.v3.AdviceResult`
        """
        self._tune_result = tune_result

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
        if not isinstance(other, ShowTuningResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
