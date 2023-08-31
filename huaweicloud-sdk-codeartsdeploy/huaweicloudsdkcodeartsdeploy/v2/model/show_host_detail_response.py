# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowHostDetailResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'result': 'HostInfoDetail'
    }

    attribute_map = {
        'status': 'status',
        'result': 'result'
    }

    def __init__(self, status=None, result=None):
        """ShowHostDetailResponse

        The model defined in huaweicloud sdk

        :param status: 请求状态
        :type status: str
        :param result: 
        :type result: :class:`huaweicloudsdkcodeartsdeploy.v2.HostInfoDetail`
        """
        
        super(ShowHostDetailResponse, self).__init__()

        self._status = None
        self._result = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if result is not None:
            self.result = result

    @property
    def status(self):
        """Gets the status of this ShowHostDetailResponse.

        请求状态

        :return: The status of this ShowHostDetailResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowHostDetailResponse.

        请求状态

        :param status: The status of this ShowHostDetailResponse.
        :type status: str
        """
        self._status = status

    @property
    def result(self):
        """Gets the result of this ShowHostDetailResponse.

        :return: The result of this ShowHostDetailResponse.
        :rtype: :class:`huaweicloudsdkcodeartsdeploy.v2.HostInfoDetail`
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this ShowHostDetailResponse.

        :param result: The result of this ShowHostDetailResponse.
        :type result: :class:`huaweicloudsdkcodeartsdeploy.v2.HostInfoDetail`
        """
        self._result = result

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
        if not isinstance(other, ShowHostDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
