# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AuthorizeFaceRecognitionServiceResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'max_face_set_number': 'int',
        'detect_service': 'ServiceInfo',
        'live_detect_service': 'ServiceInfo',
        'compare_service': 'ServiceInfo',
        'search_service': 'ServiceInfo'
    }

    attribute_map = {
        'max_face_set_number': 'max_face_set_number',
        'detect_service': 'detect_service',
        'live_detect_service': 'live_detect_service',
        'compare_service': 'compare_service',
        'search_service': 'search_service'
    }

    def __init__(self, max_face_set_number=None, detect_service=None, live_detect_service=None, compare_service=None, search_service=None):
        """AuthorizeFaceRecognitionServiceResponse - a model defined in huaweicloud sdk"""
        
        super(AuthorizeFaceRecognitionServiceResponse, self).__init__()

        self._max_face_set_number = None
        self._detect_service = None
        self._live_detect_service = None
        self._compare_service = None
        self._search_service = None
        self.discriminator = None

        if max_face_set_number is not None:
            self.max_face_set_number = max_face_set_number
        if detect_service is not None:
            self.detect_service = detect_service
        if live_detect_service is not None:
            self.live_detect_service = live_detect_service
        if compare_service is not None:
            self.compare_service = compare_service
        if search_service is not None:
            self.search_service = search_service

    @property
    def max_face_set_number(self):
        """Gets the max_face_set_number of this AuthorizeFaceRecognitionServiceResponse.

        调用成功时表示最大的人脸库数量。 调用失败时无此字段。

        :return: The max_face_set_number of this AuthorizeFaceRecognitionServiceResponse.
        :rtype: int
        """
        return self._max_face_set_number

    @max_face_set_number.setter
    def max_face_set_number(self, max_face_set_number):
        """Sets the max_face_set_number of this AuthorizeFaceRecognitionServiceResponse.

        调用成功时表示最大的人脸库数量。 调用失败时无此字段。

        :param max_face_set_number: The max_face_set_number of this AuthorizeFaceRecognitionServiceResponse.
        :type: int
        """
        self._max_face_set_number = max_face_set_number

    @property
    def detect_service(self):
        """Gets the detect_service of this AuthorizeFaceRecognitionServiceResponse.


        :return: The detect_service of this AuthorizeFaceRecognitionServiceResponse.
        :rtype: ServiceInfo
        """
        return self._detect_service

    @detect_service.setter
    def detect_service(self, detect_service):
        """Sets the detect_service of this AuthorizeFaceRecognitionServiceResponse.


        :param detect_service: The detect_service of this AuthorizeFaceRecognitionServiceResponse.
        :type: ServiceInfo
        """
        self._detect_service = detect_service

    @property
    def live_detect_service(self):
        """Gets the live_detect_service of this AuthorizeFaceRecognitionServiceResponse.


        :return: The live_detect_service of this AuthorizeFaceRecognitionServiceResponse.
        :rtype: ServiceInfo
        """
        return self._live_detect_service

    @live_detect_service.setter
    def live_detect_service(self, live_detect_service):
        """Sets the live_detect_service of this AuthorizeFaceRecognitionServiceResponse.


        :param live_detect_service: The live_detect_service of this AuthorizeFaceRecognitionServiceResponse.
        :type: ServiceInfo
        """
        self._live_detect_service = live_detect_service

    @property
    def compare_service(self):
        """Gets the compare_service of this AuthorizeFaceRecognitionServiceResponse.


        :return: The compare_service of this AuthorizeFaceRecognitionServiceResponse.
        :rtype: ServiceInfo
        """
        return self._compare_service

    @compare_service.setter
    def compare_service(self, compare_service):
        """Sets the compare_service of this AuthorizeFaceRecognitionServiceResponse.


        :param compare_service: The compare_service of this AuthorizeFaceRecognitionServiceResponse.
        :type: ServiceInfo
        """
        self._compare_service = compare_service

    @property
    def search_service(self):
        """Gets the search_service of this AuthorizeFaceRecognitionServiceResponse.


        :return: The search_service of this AuthorizeFaceRecognitionServiceResponse.
        :rtype: ServiceInfo
        """
        return self._search_service

    @search_service.setter
    def search_service(self, search_service):
        """Sets the search_service of this AuthorizeFaceRecognitionServiceResponse.


        :param search_service: The search_service of this AuthorizeFaceRecognitionServiceResponse.
        :type: ServiceInfo
        """
        self._search_service = search_service

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
        if not isinstance(other, AuthorizeFaceRecognitionServiceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
