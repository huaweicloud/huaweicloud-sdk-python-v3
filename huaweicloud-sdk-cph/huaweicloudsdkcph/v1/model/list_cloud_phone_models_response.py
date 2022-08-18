# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCloudPhoneModelsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'request_id': 'str',
        'phone_models': 'list[object]'
    }

    attribute_map = {
        'request_id': 'request_id',
        'phone_models': 'phone_models'
    }

    def __init__(self, request_id=None, phone_models=None):
        """ListCloudPhoneModelsResponse

        The model defined in huaweicloud sdk

        :param request_id: 请求的唯一标识ID
        :type request_id: str
        :param phone_models: 云手机的规格信息
        :type phone_models: list[object]
        """
        
        super(ListCloudPhoneModelsResponse, self).__init__()

        self._request_id = None
        self._phone_models = None
        self.discriminator = None

        self.request_id = request_id
        self.phone_models = phone_models

    @property
    def request_id(self):
        """Gets the request_id of this ListCloudPhoneModelsResponse.

        请求的唯一标识ID

        :return: The request_id of this ListCloudPhoneModelsResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ListCloudPhoneModelsResponse.

        请求的唯一标识ID

        :param request_id: The request_id of this ListCloudPhoneModelsResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def phone_models(self):
        """Gets the phone_models of this ListCloudPhoneModelsResponse.

        云手机的规格信息

        :return: The phone_models of this ListCloudPhoneModelsResponse.
        :rtype: list[object]
        """
        return self._phone_models

    @phone_models.setter
    def phone_models(self, phone_models):
        """Sets the phone_models of this ListCloudPhoneModelsResponse.

        云手机的规格信息

        :param phone_models: The phone_models of this ListCloudPhoneModelsResponse.
        :type phone_models: list[object]
        """
        self._phone_models = phone_models

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
        if not isinstance(other, ListCloudPhoneModelsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
