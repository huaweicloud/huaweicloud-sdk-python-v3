# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RemoveVpcExtendCidrResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vpc': 'Vpc',
        'request_id': 'str'
    }

    attribute_map = {
        'vpc': 'vpc',
        'request_id': 'request_id'
    }

    def __init__(self, vpc=None, request_id=None):
        r"""RemoveVpcExtendCidrResponse

        The model defined in huaweicloud sdk

        :param vpc: 
        :type vpc: :class:`huaweicloudsdkvpc.v3.Vpc`
        :param request_id: 请求ID
        :type request_id: str
        """
        
        super(RemoveVpcExtendCidrResponse, self).__init__()

        self._vpc = None
        self._request_id = None
        self.discriminator = None

        if vpc is not None:
            self.vpc = vpc
        if request_id is not None:
            self.request_id = request_id

    @property
    def vpc(self):
        r"""Gets the vpc of this RemoveVpcExtendCidrResponse.

        :return: The vpc of this RemoveVpcExtendCidrResponse.
        :rtype: :class:`huaweicloudsdkvpc.v3.Vpc`
        """
        return self._vpc

    @vpc.setter
    def vpc(self, vpc):
        r"""Sets the vpc of this RemoveVpcExtendCidrResponse.

        :param vpc: The vpc of this RemoveVpcExtendCidrResponse.
        :type vpc: :class:`huaweicloudsdkvpc.v3.Vpc`
        """
        self._vpc = vpc

    @property
    def request_id(self):
        r"""Gets the request_id of this RemoveVpcExtendCidrResponse.

        请求ID

        :return: The request_id of this RemoveVpcExtendCidrResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this RemoveVpcExtendCidrResponse.

        请求ID

        :param request_id: The request_id of this RemoveVpcExtendCidrResponse.
        :type request_id: str
        """
        self._request_id = request_id

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
        if not isinstance(other, RemoveVpcExtendCidrResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
